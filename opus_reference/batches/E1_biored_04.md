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

## Item biored:test:174
Example input:
Sentence: An opposite effect was observed for the TLR4 D299G and TLR2 P631H variants , with a lower prevalence of ACCA antibodies ( 23.4 % versus 35 % , p = 0.013 ) and Omp antibodies ( 20.5 % versus 34.6 % , p = 0.009 ) , respectively .

Example answer:
{"entities": [{"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "D299G", "type": "SequenceVariant"}, {"text": "TLR2", "type": "GeneOrGeneProduct"}, {"text": "P631H", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : As a potential explanation of our findings , we hypothesize that in b-thalassemia the Gg-globin-XmnI/Ag-globin- ( G- > A ) genotype is frequently under genetic linkage with b ( 0 ) -thalassemia mutations , but not with the b ( + ) -thalassemia mutation here studied ( i.e .

Example answer:
{"entities": [{"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Gg-globin-XmnI/Ag-globin-", "type": "GeneOrGeneProduct"}, {"text": "G- > A", "type": "SequenceVariant"}, {"text": "b ( 0 ) -thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "b ( + ) -thalassemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Arg124Cys and Arg555Trp appear to be the predominant mutations causing LCD and GCD , respectively , in the population studied .

Example answer:
{"entities": [{"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Twenty-four of 113 ( 21 % ) gastric cancer patients had the II , 57 ( 51 % ) the ID , and 32 ( 28 % ) the DD genotype .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In GCD , 18 patients with GCD type I had a mutation of arginine 555-to-tryptophan ( Arg555Trp ) and 1 patient with GCD type III ( Reis-Bucklers dystrophy ) , had the Arg124Leu mutation .

Example answer:
{"entities": [{"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "GCD type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 555-to-tryptophan", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GCD type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Reis-Bucklers dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Arg124Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: On the contrary , the DBP Glu-containing genotype was not accompanied by differences in the prevalence of GAD65 antibodies .

## Item biored:test:153
Example input:
Sentence: RAMH induced a shift in the localization of PKCalpha expression from the cytosolic domain into the membrane region of Mz-ChA-1 cells .

Example answer:
{"entities": [{"text": "RAMH", "type": "ChemicalEntity"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Mz-ChA-1", "type": "CellLine"}]}

Example input:
Sentence: These findings identify an autosomal-recessive skeletal dysplasia and a significant role for the aggrecan C-type lectin domain in regulating endochondral ossification and , thereby , height .

Example answer:
{"entities": [{"text": "autosomal-recessive skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aggrecan", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: BMPR signalling was markedly impaired in TAK1-deficient chondrocytes as evidenced by reduced expression of known BMP target genes as well as reduced phosphorylation of Smad1/5/8 and p38/Jnk/Erk MAP kinases .

Example answer:
{"entities": [{"text": "BMPR", "type": "GeneOrGeneProduct"}, {"text": "TAK1-deficient", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "p38/Jnk/Erk", "type": "GeneOrGeneProduct"}, {"text": "MAP kinases", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aryl hydrocarbon receptor interacting protein ( AIP ) gene mutation analysis in children and adolescents with sporadic pituitary adenomas .

Example answer:
{"entities": [{"text": "Aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "pituitary adenomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Association of sporadic chondrocalcinosis with a -4-basepair G-to-A transition in the 5'-untranslated region of ANKH that promotes enhanced expression of ANKH protein and excess generation of extracellular inorganic pyrophosphate .

## Item biored:test:182
Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Ag-globin gene sequencing was performed on genomic DNA isolated from a total of 75 b-thalassemia patients , including 31 b ( 0 ) 39/b ( 0 ) 39 , 33 b ( 0 ) 39/b ( + ) IVSI-110 , 9 b ( + ) IVSI-110/b ( + ) IVSI-110 , one b ( 0 ) IVSI-1/b ( + ) IVSI-6 and one b ( 0 ) 39/b ( + ) IVSI-6 .

Example answer:
{"entities": [{"text": "Ag-globin", "type": "GeneOrGeneProduct"}, {"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The second objective was to employ RB1 molecular deletion and microsatellite-based linkage analysis as laboratory tools , while counseling families with a history of retinoblastoma ( RB ) .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "retinoblastoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Using denaturing high-pressure liquid chromatography and sequencing , we screened peripheral blood DNA from 184 familial melanoma cases for BRAF promoter variants .

## Item biored:test:167
Example input:
Sentence: In addition , the previously described variants g.3352delG ( commonly designated 30delG or 35 delG ) , g.3426G > A [ p.Val37Ile ] , g.3697G > A [ p.Arg127His ] , g.3774G > A [ p.Val153Ile ] , and g.3795G > A [ p.Gly160Ser ] were identified .

Example answer:
{"entities": [{"text": "g.3352delG", "type": "SequenceVariant"}, {"text": "30delG", "type": "SequenceVariant"}, {"text": "35 delG", "type": "SequenceVariant"}, {"text": "g.3426G > A", "type": "SequenceVariant"}, {"text": "p.Val37Ile", "type": "SequenceVariant"}, {"text": "g.3697G > A", "type": "SequenceVariant"}, {"text": "p.Arg127His", "type": "SequenceVariant"}, {"text": "g.3774G > A", "type": "SequenceVariant"}, {"text": "p.Val153Ile", "type": "SequenceVariant"}, {"text": "g.3795G > A", "type": "SequenceVariant"}, {"text": "p.Gly160Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : This study showed that SNPs rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , but not rs7535263 , rs1410996 , or rs2274700 , in CFH were significantly associated with wet AMD in a mainland Han Chinese population .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "rs7535263", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "rs2274700", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: We also found an interaction between the presence of DBH -1021T and the -889TT genotype ( rs1800587 ) of IL1A : synergy factor = 1.9 ( 1.2-3.1 , 0.005 ) .

Example answer:
{"entities": [{"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}, {"text": "-889TT", "type": "SequenceVariant"}, {"text": "rs1800587", "type": "SequenceVariant"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The CASP8 -652 6N del variant genotypes or haplotypes were inversely associated with SCCHN risk ( adjusted OR , 0.70 ; 95 % CI , 0.57-0.85 for the ins/del + del/del genotypes compared with the ins/ins genotype ; adjusted OR , 0.73 ; 95 % CI , 0.55-0.97 for the del-D haplotype compared with the ins-D haplotype ) .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A haplotype containing these four SNPs ( CATA ) significantly increased protection of wet AMD with a P value of 0.0005 and an odds ratio of 0.29 ( 95 % confidence interval : 0.15-0.60 ) .

Example answer:
{"entities": [{"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These DBP variants lead to differences in the affinity for 1.25 ( OH ) 2D3 .

## Item biored:test:186
Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A single nucleotide polymorphism in the IRF5 promoter region is associated with susceptibility to rheumatoid arthritis in the Japanese population .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "rheumatoid arthritis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : We examined the genetic association of the promoter insertion/deletion ( indel ) in IRF5 gene with systemic lupus erythematosus ( SLE ) in distinct populations and assessed its role in gene expression .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: We also observed a 20 bp insertion/deletion polymorphism 1,109 bp upstream of the initiation codon , but this variant was not associated with prostate cancer .

Example answer:
{"entities": [{"text": "20 bp insertion/deletion polymorphism 1,109 bp upstream of the initiation codon", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We corroborated the association of the promoter indel with SLE in 5 different populations and revealed that rs10954213 is the main single-nucleotide polymorphism responsible for altered IRF5 expression in PBMC .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs10954213", "type": "SequenceVariant"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These findings indicate that the promoter polymorphism of IRF5 is a genetic factor conferring predisposition to RA , and that it contributes considerably to disease pathogenesis in patients that were SE negative .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Our results therefore suggest that the BRAF polymorphism is not significantly associated with melanoma and the promoter insertion/deletion linked with the polymorphism is not a causal variant .

## Item biored:test:206
Example input:
Sentence: Interestingly , there is a stronger finding with -521 C/T allele frequencies with heroin dependence ( p=0.0002 ) .

Example answer:
{"entities": [{"text": "-521 C/T", "type": "SequenceVariant"}, {"text": "heroin dependence", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our data do not provide support for rs2230912 or the other polymorphisms studied within the P2RX7 locus , being involved in susceptibility to mood disorders .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further follow-up of the cohort is required to study the polymorphisms ' relevance for immune-mediated diseases such as childhood asthma .

Example answer:
{"entities": [{"text": "immune-mediated diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This single nucleotide polymorphism ( SNP ) seemed to be functional as it was associated with decreased lung cancer risk .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a genotype test , we found a trend to point-wise association ( P = 0.053 ) of the G472A SNP in Hispanic subjects with opiate addiction .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These observations strongly suggest that the -120-bp duplication polymorphism of DRD4 is associated with schizophrenia and that the -521 C/T polymorphism is associated with heroin addiction .

Example answer:
{"entities": [{"text": "-120-bp duplication", "type": "SequenceVariant"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-521 C/T", "type": "SequenceVariant"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: Association study of polymorphisms in the promoter region of DRD4 with schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the possible association between three functional polymorphisms in the promoter region of the dopamine D4 receptor ( DRD4 ) gene and schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "dopamine D4 receptor", "type": "GeneOrGeneProduct"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Clarifying the functional relevance of polymorphisms associated with susceptibility to a complex disorder such as drug addiction provides a foundation for clinical association studies .

## Item biored:test:154
Example input:
Sentence: These results indicate that some ARM phenotypes in the b-catenin GOF mutants were caused by abnormal Bmp signaling .

Example answer:
{"entities": [{"text": "ARM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aryl hydrocarbon receptor interacting protein ( AIP ) gene mutation analysis in children and adolescents with sporadic pituitary adenomas .

Example answer:
{"entities": [{"text": "Aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "pituitary adenomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Pituitary adenoma predisposition ( PAP ) has been recently associated with germline mutations in the aryl hydrocarbon receptor interacting protein ( AIP ) gene .

Example answer:
{"entities": [{"text": "Pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hypomorphic mutations in meckelin ( MKS3/TMEM67 ) cause nephronophthisis with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "meckelin", "type": "GeneOrGeneProduct"}, {"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "nephronophthisis with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Loss-of-function mutations in PTPN11 cause metachondromatosis , but not Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "metachondromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: OBJECTIVE : Certain mutations in ANKH , which encodes a multiple-pass transmembrane protein that regulates inorganic pyrophosphate ( PPi ) transport , are linked to autosomal-dominant familial chondrocalcinosis .

## Item biored:test:156
Example input:
Sentence: To investigate the GSTP1 Ile105Val genotype frequency in prostate cancer cases in the Kashmiri population , we designed a case-control study , in which 50 prostate cancer cases and 45 benign prostate hyperplasia cases were studied for GSTP1 Ile105Val polymorphism , compared to 80 controls taken from the general population , employing the PCR-RFLP technique .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genetic polymorphism of the glutathione-S-transferase P1 gene ( GSTP1 ) and susceptibility to prostate cancer in the Kashmiri population .

Example answer:
{"entities": [{"text": "glutathione-S-transferase P1", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : We performed comprehensive genomic profiling ( CGP ) for coding regions in more than 300 cancer-related genes of 186 GISTs to assess for their somatic alterations .

Example answer:
{"entities": [{"text": "cancer-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GISTs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We next sequenced PTPN11 in DNA samples from 54 patients with the multiple enchondromatosis disorders Ollier disease or Maffucci syndrome , but found no coding sequence PTPN11 mutations .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "enchondromatosis disorders Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : ANKH variants identified by genomic sequencing were screened for association with chondrocalcinosis in 128 patients with severe sporadic chondrocalcinosis or pseudogout and in ethnically matched healthy controls .

## Item biored:test:164
Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the current study , the haplotype structure of the PTPN22 region was determined , and individual haplotypes were tested for association with type 1 diabetes in family-based tests .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results support the conclusion that the 1858C/T allele is the major risk variant for type 1 diabetes in the PTPN22 locus , but they suggest that additional infrequent coding variants at PTPN22 may also contribute to type 1 diabetes risk .

Example answer:
{"entities": [{"text": "1858C/T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A recent addition to the list of widely confirmed type 1 diabetes risk loci is the PTPN22 gene encoding a lymphoid-specific phosphatase ( Lyp ) .

Example answer:
{"entities": [{"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "lymphoid-specific phosphatase", "type": "GeneOrGeneProduct"}, {"text": "Lyp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , evidence supporting a role for PTPN22 in type 1 diabetes derives entirely from the study of just one coding single nucleotide polymorphism , 1858C/T .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "1858C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: No independent role of the -1123 G > C and+2740 A > G variants in the association of PTPN22 with type 1 diabetes and juvenile idiopathic arthritis in two Caucasian populations .

Example answer:
{"entities": [{"text": "-1123 G > C", "type": "SequenceVariant"}, {"text": "A > G", "type": "SequenceVariant"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Its +1858C > T ( R620W ) polymorphism has been shown to associate with a risk for multiple autoimmune diseases , including type 1 diabetes ( T1D ) and juvenile idiopathic arthritis ( JIA ) .

Example answer:
{"entities": [{"text": "+1858C > T", "type": "SequenceVariant"}, {"text": "R620W", "type": "SequenceVariant"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Vitamin D-binding protein gene polymorphism association with IA-2 autoantibodies in type 1 diabetes .

## Item biored:test:178
Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Founder mutations in the BRCA1 gene in Polish families with breast-ovarian cancer .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : While mutations were absent in non-GH-secreting adenoma patients , germline AIP mutations can be found in children and adolescents with GH-secreting tumours , even in the absence of family history .

Example answer:
{"entities": [{"text": "adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "GH-secreting tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As only the two family members homozygous for the mutation showed WFS , these data support the notion that this mutation is the cause of WFS .

Example answer:
{"entities": [{"text": "WFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Input:
Sentence: Germ line mutations in BRAF have not been identified as causal in families predisposed to melanoma .

## Item biored:test:179
Example input:
Sentence: MSH5 and DMC1 mutations may be one explanation for POF , albeit uncommon .

Example answer:
{"entities": [{"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In agreement with the expectation that this mutation alters the LYAR binding activity , we found that the Ag ( +25 G- > A ) and Gg-globin-XmnI polymorphisms are associated with high HbF in erythroid precursor cells isolated from b ( 0 ) 39/b ( 0 ) 39 thalassemia patients .

Example answer:
{"entities": [{"text": "LYAR", "type": "GeneOrGeneProduct"}, {"text": "Ag", "type": "GeneOrGeneProduct"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Gg-globin-XmnI", "type": "GeneOrGeneProduct"}, {"text": "HbF", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39/b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Another POF patient of African origin showed a homozygous nucleotide change in the tenth of DMC1 gene that led to an alteration of the amino acid composition of the protein ( M200V ) .

Example answer:
{"entities": [{"text": "POF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "M200V", "type": "SequenceVariant"}]}

Example input:
Sentence: Thus the present study indicates that individuals with the variant w1/m1 genotype exhibit an increased risk while those with w2/m2 genotype exhibit a decreased risk for prostate cancer .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These findings indicate that the promoter polymorphism of IRF5 is a genetic factor conferring predisposition to RA , and that it contributes considerably to disease pathogenesis in patients that were SE negative .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , whether RNASEL variation contributes to the increased risk of prostate cancer observed in populations of African ancestry remains unclear .

Example answer:
{"entities": [{"text": "RNASEL", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , a recent study suggested that a BRAF haplotype was associated with risk of sporadic melanoma in men .

## Item biored:test:141
Example input:
Sentence: also significantly augmented hippocampal LTP in saline-treated ( 1ml/kg , s.c. ) rats .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Serotonin was depleted beginning on postnatal day 26 with parachlorophenylalanine ( PCPA 100 mg/kg , every other day ) ; controls received saline .

Example answer:
{"entities": [{"text": "Serotonin", "type": "ChemicalEntity"}, {"text": "parachlorophenylalanine", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Input:
Sentence: IT MK-801 significantly reduced the number of dark-stained alpha-motoneurons after morphine-induced spastic paraparesis compared with the saline group .

## Item biored:test:162
Example input:
Sentence: RAMH induced a shift in the localization of PKCalpha expression from the cytosolic domain into the membrane region of Mz-ChA-1 cells .

Example answer:
{"entities": [{"text": "RAMH", "type": "ChemicalEntity"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Mz-ChA-1", "type": "CellLine"}]}

Example input:
Sentence: Object of the present study was to study the influence of SLCO1B1 * 5 , * 15 and * 15+C1007G , a novel haplotype found in a patient with pravastatin-induced myopathy , on the functional properties of OATP1B1 by transient expression systems of HEK293 and HeLa cells using endogenous conjugates and statins as substrates .

Example answer:
{"entities": [{"text": "SLCO1B1", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pravastatin-induced", "type": "ChemicalEntity"}, {"text": "myopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OATP1B1", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "HeLa", "type": "CellLine"}]}

Example input:
Sentence: BMPR signalling was markedly impaired in TAK1-deficient chondrocytes as evidenced by reduced expression of known BMP target genes as well as reduced phosphorylation of Smad1/5/8 and p38/Jnk/Erk MAP kinases .

Example answer:
{"entities": [{"text": "BMPR", "type": "GeneOrGeneProduct"}, {"text": "TAK1-deficient", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "p38/Jnk/Erk", "type": "GeneOrGeneProduct"}, {"text": "MAP kinases", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These findings identify an autosomal-recessive skeletal dysplasia and a significant role for the aggrecan C-type lectin domain in regulating endochondral ossification and , thereby , height .

Example answer:
{"entities": [{"text": "autosomal-recessive skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aggrecan", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results indicate that some ARM phenotypes in the b-catenin GOF mutants were caused by abnormal Bmp signaling .

Example answer:
{"entities": [{"text": "ARM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both sporadic and inherited BCCs are associated with mutations in the tumor suppressor gene PTCH1 , but there is still uncertainty on the role of its homolog PTCH2 .

Example answer:
{"entities": [{"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Input:
Sentence: CONCLUSION : A subset of sporadic chondrocalcinosis appears to be heritable via a -4-bp G-to-A ANKH 5'-UTR transition that up-regulates expression of ANKH and extracellular PPi in chondrocyte cells .

## Item biored:test:228
Example input:
Sentence: RESULTS : By clinical examination , the patients and the pedigrees were divided into the following three groups : AN , coloboma of iris and choroids , and the anterior segment malformations including peters anomaly .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroids", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "peters anomaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a second series , cytosolic Ca2+ activity ( Fluo3 fluorescence ) , cell volume ( forward scatter ) , and PS-exposure ( annexin V binding ) were determined by FACS analysis in erythrocytes from healthy volunteers .

Example answer:
{"entities": [{"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "Fluo3", "type": "ChemicalEntity"}, {"text": "PS-exposure", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Isoforms of NADPH oxidase MRNA were measured in several types of cultured vascular ecs : human retinal microvascular ECs ( hRMVECs ) , choroidal ECs ( CECs ) , and human umbilical vascular ECs ( HUVECs ) using real-time PCR .

Example answer:
{"entities": [{"text": "NADPH oxidase", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , eight individuals who had both microcoria and glaucoma were screened for glaucoma genes : myocilin ( MYOC ) , optineurin ( OPTN ) and CYP1B1 .

Example answer:
{"entities": [{"text": "microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocilin", "type": "GeneOrGeneProduct"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "optineurin", "type": "GeneOrGeneProduct"}, {"text": "OPTN", "type": "GeneOrGeneProduct"}, {"text": "CYP1B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Our findings further confirmed that different kind of mutations might cause different ocular phenotype , and clearly clinical phenotype classification might increase the mutation detection rate of the PAX6 gene .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Six affected family members were examined clinically including visual acuity , color cornea photography , applanation tonography , and fundoscopy .

Example answer:
{"entities": []}

Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Detailed characterization of the patients ' phenotype was performed with fundal photography , visual field testing , fundal fluorescein angiography , and electroretinography ( ERG ) .

## Item biored:test:210
Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This shift in balance may contribute to increased bladder dysfunction in VIP ( -/- ) mice with bladder inflammation and altered neurochemical expression in micturition pathways .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both , Ro4368554 ( 3 and 10 mg/kg , intraperitoneally ( i.p . ) )

Example answer:
{"entities": []}

Example input:
Sentence: A rat model of IUGR was established by PCE , male fetuses and adult offspring at the age of postnatal week 24 were euthanized .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "IUGR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Intracerebroventricular ( i.c.v . )

Example answer:
{"entities": []}

Example input:
Sentence: Given VIP 's role as an anti-inflammatory mediator , we hypothesized that VIP ( -/- ) mice would exhibit enhanced inflammatory mediator expression after cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Exaggerated expression of inflammatory mediators in vasoactive intestinal polypeptide knockout ( VIP-/- ) mice with cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vasoactive intestinal polypeptide", "type": "GeneOrGeneProduct"}, {"text": "VIP-/-", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: VCM was administrated intraperitoneally ( i.p . )

## Item biored:test:176
Example input:
Sentence: A new Rab6 homolog cDNA , Rab6c , was discovered by a hypermethylated DNA fragment probe that was isolated from a human multidrug resistant ( MDR ) breast cancer cell line , MCF7/AdrR , by the methylation sensitive-representational difference analysis ( MS-RDA ) technique .

Example answer:
{"entities": [{"text": "Rab6", "type": "GeneOrGeneProduct"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCF7/AdrR", "type": "CellLine"}]}

Example input:
Sentence: Ten independent rare SNPs ( MAF = 0.001-0.009 ) were associated with obesity-related traits ( P = 0.01-0.00002 ) .

Example answer:
{"entities": [{"text": "obesity-related", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we assessed the genetic role of IRF5 in susceptibility to rheumatoid arthritis ( RA ) in Japanese subjects .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "rheumatoid arthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MSH5 and DMC1 mutations may be one explanation for POF , albeit uncommon .

Example answer:
{"entities": [{"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : These findings indicate that the promoter polymorphism of IRF5 is a genetic factor conferring predisposition to RA , and that it contributes considerably to disease pathogenesis in patients that were SE negative .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Input:
Sentence: No Evidence for BRAF as a melanoma/nevus susceptibility gene .

## Item biored:test:212
Example input:
Sentence: Ezetimibe undergoes extensive glucuronidation by uridine diphosphate glucoronosyltransferases ( UGT ) in the intestine and liver and may have inhibited the glucuronidation of simvastatin hydroxy acid , resulting in increased simvastatin exposure and subsequent hepatotoxicity .

Example answer:
{"entities": [{"text": "Ezetimibe", "type": "ChemicalEntity"}, {"text": "uridine diphosphate glucoronosyltransferases", "type": "GeneOrGeneProduct"}, {"text": "UGT", "type": "GeneOrGeneProduct"}, {"text": "simvastatin hydroxy acid", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One month of oral galactose treatment initiated immediately after the STZ-icv administration , successfully prevented development of the STZ-icv-induced cognitive deficits .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}, {"text": "STZ-icv", "type": "ChemicalEntity"}, {"text": "STZ-icv-induced", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Etifoxine significantly reduced neurodeficits and perihematomal brain edema after ICH induction by injection of either autologous blood or collagenase .

Example answer:
{"entities": [{"text": "Etifoxine", "type": "ChemicalEntity"}, {"text": "neurodeficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "collagenase", "type": "ChemicalEntity"}]}

Example input:
Sentence: According to annexin V binding , erythrocytes from patients indeed showed a significant increase of PS exposure within 1 week of treatment with azathioprine .

Example answer:
{"entities": [{"text": "annexin V", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PS", "type": "ChemicalEntity"}, {"text": "azathioprine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient 's observations were within normal limits , he was administered oxygen via a face mask and glyceryl trinitrate ( GTN ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "glyceryl trinitrate", "type": "ChemicalEntity"}, {"text": "GTN", "type": "ChemicalEntity"}]}

Example input:
Sentence: At pH 9 , a higher rate of etodolac release from ED was observed as compared to aqueous buffer of pH 7.4 and 80 % human plasma ( pH 7.4 ) , following first-order kinetics .

Example answer:
{"entities": [{"text": "etodolac", "type": "ChemicalEntity"}, {"text": "ED", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Biological evaluation suggested that conjugates ( ED1-ED4 ) retained comparable analgesic and antiinflammatory activities with remarkably reduced ulcerogenicity as compared to their parent drug -- etodolac .

Example answer:
{"entities": [{"text": "etodolac", "type": "ChemicalEntity"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHOD : Data were obtained from two clinical trials : 1 ) acute Epo exposure ( rHuEpo , 400 IU/kg ) followed by WAT biopsies after 1 h and 2 ) 10 weeks treatment with the erythropoiesis-stimulating agent ( ESA ) Darbepoietin-alpha .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "erythropoiesis-stimulating agent", "type": "ChemicalEntity"}, {"text": "ESA", "type": "ChemicalEntity"}, {"text": "Darbepoietin-alpha", "type": "ChemicalEntity"}]}

Input:
Sentence: Erdosteine was administered orally .

## Item biored:test:165
Example input:
Sentence: VDAC1 regulates mitochondrial uptake across the outer membrane and mitochondrial outer membrane permeabilization ( MOMP ) .

Example answer:
{"entities": [{"text": "VDAC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cisplatin-treated DCs down-regulated the expression of cell surface molecules ( CD80 , CD86 , MHC class I and II ) and up-regulated endocytic capacity in a dose-dependent manner .

Example answer:
{"entities": [{"text": "Cisplatin-treated", "type": "ChemicalEntity"}, {"text": "CD80", "type": "GeneOrGeneProduct"}, {"text": "CD86", "type": "GeneOrGeneProduct"}, {"text": "MHC class I and II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Calbindin-D28k ( CB ) , one of the major calcium-binding and buffering proteins , has a critical role in preventing a neuronal death as well as maintaining calcium homeostasis .

Example answer:
{"entities": [{"text": "Calbindin-D28k", "type": "GeneOrGeneProduct"}, {"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "neuronal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Meanwhile apoptosis related proteins bax and ATF2 were involved in desminopathy patients and desminopathy rat model , but not bcl-2 , bcl-xl or HK2.VDAC1 and desmin are closely relevant in the tissue splices of deminopathies patients and rats with desminopathy at protein lever .

Example answer:
{"entities": [{"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2.VDAC1", "type": "GeneOrGeneProduct"}, {"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: To investigate this question , we have developed in vitro motility assays with purified DDB and BICD2 's membrane vesicle partner , the GTPase Rab6a .

Example answer:
{"entities": [{"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "GTPase Rab6a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rab6a-GTP , either in solution or bound to artificial liposomes , released BICD2 from an autoinhibited state and promoted robust dynein-dynactin transport .

Example answer:
{"entities": [{"text": "Rab6a-GTP", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein-dynactin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our interpretation is that Ent3p mediates the transport of alpha-syn to the vacuole for proteolytic degradation .

Example answer:
{"entities": [{"text": "Ent3p", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Lastly , overexpression of Ent3p , which is a clathrin adapter protein involved in protein transport between the Golgi and the vacuole , causes alpha-syn to redistribute from the plasma membrane into cytoplasmic vesicular structures .

Example answer:
{"entities": [{"text": "Ent3p", "type": "GeneOrGeneProduct"}, {"text": "clathrin", "type": "ChemicalEntity"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Bicaudal D2 ( BICD2 ) joins dynein with dynactin into a ternary complex ( termed DDB ) capable of processive movement .

Example answer:
{"entities": [{"text": "Bicaudal D2", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein", "type": "GeneOrGeneProduct"}, {"text": "dynactin", "type": "GeneOrGeneProduct"}, {"text": "DDB", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: BACKGROUND : Vitamin D-binding protein ( DBP ) is the main systemic transporter of 1.25 ( OH ) 2D3 and is essential for its cellular endocytosis .

## Item biored:test:177
Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Identification of a gain-of-function mutation of the prolactin receptor in women with benign breast tumors .

Example answer:
{"entities": [{"text": "prolactin receptor", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "benign breast tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : About 10-15 % of adult , and most pediatric , gastrointestinal stromal tumors ( GIST ) lack mutations in KIT , PDGFRA , SDHx , or RAS pathway components ( KRAS , BRAF , NF1 ) .

Example answer:
{"entities": [{"text": "gastrointestinal stromal tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KIT", "type": "GeneOrGeneProduct"}, {"text": "PDGFRA", "type": "GeneOrGeneProduct"}, {"text": "SDHx", "type": "GeneOrGeneProduct"}, {"text": "RAS", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Input:
Sentence: Somatic mutations of BRAF have been identified in both melanoma tumors and benign nevi .

## Item biored:test:234
Example input:
Sentence: The development of ESRD decreases survival , particularly in those patients treated with dialysis only .

Example answer:
{"entities": [{"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Age at onset of symptoms was variable ( 3-42 years old ) .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : Patients who are more than 10 years post-OLTX have CRF and ESRD at a high rate .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Two patients , ages 69 and 44 years old , demonstrated a degree of severity `` Bad '' according to best-corrected vision and corneal commitment .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Overall survival from the time of OLTX was not significantly different among groups , but by year 13 , the survival of the patients who had ESRD was only 28.2 % compared with 54.6 % in the control group .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten consecutive patients ( mean age , 58.4 +/- 6.8 years ; 7 men , 3 women ) with similar characteristics at the duration of disease ( mean disease time , 8.4 +/- 3.5 years ) , disabling motor fluctuations ( Hoehn _ Yahr stage 3-5 in off-drug phases ) and levodopa-induced dyskinesias were selected .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore the GG distribution within cases was even greater in younger men ( < 65 years ; 42 % ; P = 0.012 ) .

Example answer:
{"entities": [{"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: Moreover , in this family , the age of onset of the disease decreased in succeeding generations , which could be interpreted as anticipation .

Example answer:
{"entities": []}

Example input:
Sentence: Groups were compared regarding adverse events and changes from baseline to week 16 in electrocardiograms and vital signs .

Example answer:
{"entities": []}

Input:
Sentence: There was good correlation between clinical stage of disease and ERG changes , but age did not correlate with disease severity .

## Item biored:test:184
Example input:
Sentence: Another POF patient of African origin showed a homozygous nucleotide change in the tenth of DMC1 gene that led to an alteration of the amino acid composition of the protein ( M200V ) .

Example answer:
{"entities": [{"text": "POF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "M200V", "type": "SequenceVariant"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The search for HbF-associated polymorphisms ( such as the XmnI , BCL11A and MYB polymorphisms ) has recently gained great attention , in order to stratify b-thalassemia patients with respect to expectancy of the first transfusion , need for annual intake of blood , response to HbF inducers ( the most studied of which is hydroxyurea ) .

Example answer:
{"entities": [{"text": "HbF-associated", "type": "GeneOrGeneProduct"}, {"text": "BCL11A", "type": "GeneOrGeneProduct"}, {"text": "MYB", "type": "GeneOrGeneProduct"}, {"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HbF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A single nucleotide polymorphism in the IRF5 promoter region is associated with susceptibility to rheumatoid arthritis in the Japanese population .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "rheumatoid arthritis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These findings indicate that the promoter polymorphism of IRF5 is a genetic factor conferring predisposition to RA , and that it contributes considerably to disease pathogenesis in patients that were SE negative .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Here we describe the characterization of the rs368698783 ( +25 G- > A ) polymorphism of the Ag-globin gene associated in b ( 0 ) 39 thalassemia patients with high HbF in erythroid precursor cells .

Example answer:
{"entities": [{"text": "rs368698783", "type": "SequenceVariant"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Ag-globin", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HbF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In agreement with the expectation that this mutation alters the LYAR binding activity , we found that the Ag ( +25 G- > A ) and Gg-globin-XmnI polymorphisms are associated with high HbF in erythroid precursor cells isolated from b ( 0 ) 39/b ( 0 ) 39 thalassemia patients .

Example answer:
{"entities": [{"text": "LYAR", "type": "GeneOrGeneProduct"}, {"text": "Ag", "type": "GeneOrGeneProduct"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Gg-globin-XmnI", "type": "GeneOrGeneProduct"}, {"text": "HbF", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39/b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We therefore investigated the contribution of this BRAF polymorphism to melanoma susceptibility in 581 consecutively recruited incident cases , 258 incident cases in a study of late relapse , 673 female general practitioner controls , and the 184 familial cases .

## Item biored:test:202
Example input:
Sentence: The former constituted two major haplotypes that contained one or two repeats of 13 nucleotides in intron 8 ( designated as * 1 and * 2 , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : We found that the presence of the -1021T allele was associated with AD : odds ratio = 1.2 ( 95 % confidence interval : 1.06-1.4 , p = 0.005 ) .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The V89L polymorphism was found in heterozygosis in one of them ( with A207D ) and in one case with an otherwise normal gene sequence .

Example answer:
{"entities": [{"text": "V89L", "type": "SequenceVariant"}, {"text": "A207D", "type": "SequenceVariant"}]}

Example input:
Sentence: The single nucleotide substitution I280S ( 1123T -- > G ) was present either on both alleles or in a hemizygous form with complete deletion of the second allele .

Example answer:
{"entities": [{"text": "I280S", "type": "SequenceVariant"}, {"text": "1123T -- > G", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA samples of 760 anonymous AJ subjects were submitted for analysis , subsequently detecting six individuals heterozygous for the GALT deletion mutation , giving a carrier frequency of 1 in 127 ( 0.79 % ) .

Example answer:
{"entities": [{"text": "GALT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: With the exception of g.3318-34C > T and g.3352delG , all variants occurred heterozygously .

Example answer:
{"entities": [{"text": "g.3318-34C > T", "type": "SequenceVariant"}, {"text": "g.3352delG", "type": "SequenceVariant"}]}

Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: Haplotype reconstruction via the expectation-maximization algorithm showed in both populations that only the haplotype containing the minor ( W ) allele at codon 620 was associated with T1D ( OR=2.26 , 95 % CI 1.68-3.02 in Czechs , OR=14.8 , 95 % CI 2.0-651 in Azeri ) or JIA ( OR=2.43 , 95 % CI 1.66-3.56 in Czechs ) .

Example answer:
{"entities": [{"text": "( W ) allele at codon 620", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Direct sequencing of the encoding regions of the candidate genes revealed a heterozygous mutation c.592C -- > T in exon 2 of the gap junction protein , alpha 8 ( GJA8 ) gene .

Example answer:
{"entities": [{"text": "c.592C -- > T", "type": "SequenceVariant"}, {"text": "gap junction protein , alpha 8", "type": "GeneOrGeneProduct"}, {"text": "GJA8", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In 8 heterozygous samples measured , the A118 mRNA allele was 1.5-2.5-fold more abundant than the G118 allele .

## Item biored:test:187
Example input:
Sentence: When the patients were stratified by the SE , the rs729302 A allele was found to confer increased risk to RA in patients that were SE negative ( OR 1.50 , 95 % CI 1.17 to 1.92 , p = 0.001 ) as compared with patients carrying the SE ( OR 1.11 , 95 % CI 0.93 to 1.33 , p = 0.24 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neither 36 control women nor 39 other patients with POF possessed this genetic perturbation .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Since healthy relatives of the VUR probands are not reliable negative controls for VUR , we used a population of 90 race-matched , healthy individuals , unrelated to the VUR patients , as controls to perform an association study .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Input:
Sentence: In addition , we found that there was no association between the BRAF genotype and mean total number of banal or atypical nevi in either the cases or controls .

## Item biored:test:52
Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Low activity of patient plasma butyrylcholinesterase with butyrylthiocholine ( BTC ) and benzoylcholine , and values of dibucaine and fluoride numbers fit with heterozygous atypical silent genotype .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "butyrylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "butyrylthiocholine", "type": "ChemicalEntity"}, {"text": "BTC", "type": "ChemicalEntity"}, {"text": "benzoylcholine", "type": "ChemicalEntity"}, {"text": "dibucaine", "type": "ChemicalEntity"}, {"text": "fluoride", "type": "ChemicalEntity"}]}

Example input:
Sentence: Studies of synergy between morphine and a novel sodium channel blocker , CNSB002 , in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Butyrylcholinesterase deficiency is characterized by prolonged apnea after the use of muscle relaxants ( suxamethonium or mivacurium ) in patients who have mutations in the BCHE gene .

Example answer:
{"entities": [{"text": "Butyrylcholinesterase deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle relaxants", "type": "ChemicalEntity"}, {"text": "suxamethonium", "type": "ChemicalEntity"}, {"text": "mivacurium", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BCHE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Taking into account that the sarcolemmal integrity is stabilized by the dystrophin-glycoprotein complex ( DGC ) that connects actin and laminin in contractile machinery and extracellular matrix and by integrins , this study tests the hypothesis that isoproterenol affects sarcolemmal stability through changes in the DGC and integrins .

Example answer:
{"entities": [{"text": "dystrophin-glycoprotein", "type": "GeneOrGeneProduct"}, {"text": "actin", "type": "GeneOrGeneProduct"}, {"text": "laminin", "type": "GeneOrGeneProduct"}, {"text": "isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVE : This study determined the antihyperalgesic effect of CNSB002 , a sodium channel blocker with antioxidant properties given alone and in combinations with morphine in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Such organophosphorus ( OP ) compounds as diisopropylfluorophosphate ( DFP ) , sarin and soman are potent inhibitors of acetylcholinesterases ( AChEs ) and butyrylcholinesterases ( BChEs ) .

## Item biored:test:192
Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Loss-of-function experiments demonstrate that Chl serves as a BMP antagonist with functions that overlap and are redundant with those of Chd in forming the dorsoventral axis .

Example answer:
{"entities": [{"text": "Chl", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}, {"text": "Chd", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , M ( 3 ) -muscarinic acetylcholine receptor ( mAChR ) antagonist 4-DAMP ( 4-diphenylacetoxy-N-methylpiperidine-methiodide ) partially abolished the beneficial effects of pilocarpine .

Example answer:
{"entities": [{"text": "M ( 3 ) -muscarinic acetylcholine receptor", "type": "GeneOrGeneProduct"}, {"text": "mAChR", "type": "GeneOrGeneProduct"}, {"text": "4-DAMP", "type": "ChemicalEntity"}, {"text": "4-diphenylacetoxy-N-methylpiperidine-methiodide", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Control rats were injected with saline instead of pilocarpine .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this work CCR2 and CCL2 expression were examined following status epilepticus ( SE ) induced by pilocarpine injection .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : The data show that CCR2 and CCL2 are up-regulated in the hippocampus after pilocarpine-induced SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : SE was induced by pilocarpine injection .

Example answer:
{"entities": [{"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: The Pilo group was injected with the same drugs , except for CHX .

## Item biored:test:237
Example input:
Sentence: Phenotypic characteristics expressed in syndromes give clues to the factors involved in the cause of isolated forms of the same defects .

Example answer:
{"entities": []}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Further age stratification showed significant genotypic as well as allelic association in the group of over 40 years ( genotypic : p value = 0.035 , odds ratio = 1.617 with 95 % CI = 1.033-2.529 ; allelic : p value = 0.033 , odds ratio = 1.445 with 95 % CI = 1.029-2.029 ) .

Example answer:
{"entities": []}

Example input:
Sentence: This suggests that they may represent hypomorphic alleles , leading to a milder phenotype compared with the more severe MKS or JBTS phenotype .

Example answer:
{"entities": [{"text": "MKS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : The phenotypic and genotypic characteristics of all subjects were evaluated in a Taiwanese OPMD family .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The polymorphism distribution was also analyzed in AD patients stratified according to differential progressive rate of cognitive decline during a 2-year follow-up .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A Stratified analysis of the genotypes with age of onset and tumor grade showed the w1/m1 genotype to be significantly associated with an early age of onset ; however the tumor grades did not have significant association with the variant genotypes .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: They presented with different clinical severity and variable age of onset .

Example answer:
{"entities": []}

Example input:
Sentence: The phenotype of homozygotes is stereotyped with an extended survival , whereas that of affected heterozygotes varies .

Example answer:
{"entities": []}

Example input:
Sentence: Clinical phenotype shows considerable variation between individuals , such as bleeding , platelet count and the percentage of large platelets .

Example answer:
{"entities": [{"text": "bleeding", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Phenotype characterization showed clinical heterogeneity , and age did not correlate with disease severity .

## Item biored:test:163
Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both sporadic and inherited BCCs are associated with mutations in the tumor suppressor gene PTCH1 , but there is still uncertainty on the role of its homolog PTCH2 .

Example answer:
{"entities": [{"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations in PDE6H and in KCNV2 have been described in CDSRR .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings identify an autosomal-recessive skeletal dysplasia and a significant role for the aggrecan C-type lectin domain in regulating endochondral ossification and , thereby , height .

Example answer:
{"entities": [{"text": "autosomal-recessive skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aggrecan", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results indicate that some ARM phenotypes in the b-catenin GOF mutants were caused by abnormal Bmp signaling .

Example answer:
{"entities": [{"text": "ARM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Input:
Sentence: Distinct ANKH mutations associated with heritable chondrocalcinosis may promote disease by divergent effects on extracellular PPi and chondrocyte hypertrophy , which is likely to mediate differences in the clinical phenotypes and severity of the disease .

## Item biored:test:171
Example input:
Sentence: METHODS : Analysis of the Met326Ile polymorphism was carried out on DNA samples from 256 PCOS patients and 283 controls .

Example answer:
{"entities": [{"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "PCOS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Our results showed substantial evidence of association between -1607 promoter polymorphism of MMP1 and DDD in the Southern Chinese subjects .

Example answer:
{"entities": [{"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have investigated this gene in a large UK case-control sample ( bipolar I disorder N = 687 , unipolar recurrent major depression N = 1,036 , controls N = 1,204 ) .

Example answer:
{"entities": [{"text": "bipolar I disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "unipolar recurrent major depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We genotyped eight single nucleotide polymorphisms ( SNPs ) in the three genes , DBH , IL1A and IL6 .

Example answer:
{"entities": [{"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We therefore examined the associations with AD of the DBH -1021T allele and of the above interactions in the Epistasis Project , with 1757 cases of AD and 6294 elderly controls .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}]}

Example input:
Sentence: Genetic analysis identified a novel V876E mutation in all HypoPP patients in the family , but not in normal family members or 160 control people .

Example answer:
{"entities": [{"text": "V876E", "type": "SequenceVariant"}, {"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: 110 patients , 68 controls , and 115 first-degree relatives were genotyped for the DBP polymorphism in codon 416 .

## Item biored:test:151
Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "ChemicalEntity"}, {"text": "escitalopram", "type": "ChemicalEntity"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: We herein report the case of a 70-year-old man with 5-FU-induced cardiotoxicity , in whom a high serum level of alpha-fluoro-beta-alanine ( FBAL ) was observed .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "5-FU-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fluoro-beta-alanine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Late-onset scleroderma renal crisis induced by tacrolimus and prednisolone : a case report .

Example answer:
{"entities": [{"text": "scleroderma renal crisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tacrolimus", "type": "ChemicalEntity"}, {"text": "prednisolone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Multivariate logistic regression revealed the common haplotypes H1 ( AGACT ) , H2 ( AGAWT ) , and H3 ( AGAWC ) were associated with the persistent postoperative hypertension ( P = .01 , 0.03 , 0.005 after Bonferroni correction ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Of 13 documented fractures , 3 occurred after risperidone and SSRIs were started , and none occurred in patients with hyperprolactinemia .

Example answer:
{"entities": [{"text": "fractures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}, {"text": "SSRIs", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Input:
Sentence: CONCLUSIONS : As of March 24 , 2005 , this is the first reported case of amisulpride- and tiapride-induced hypertensive crisis in a patient with pheochromocytoma .

## Item biored:test:96
Example input:
Sentence: Analysis of a nuclear family with three affected offspring identified an autosomal-recessive form of spondyloepimetaphyseal dysplasia characterized by severe short stature and a unique constellation of radiographic findings .

Example answer:
{"entities": [{"text": "spondyloepimetaphyseal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The clinical features included hearing impairment , ichthyosiform erythroderma with hyperkeratotic plaques , palmoplantar keratoderma , alopecia of the scalp and eyelashes , and a thick vernix caseosa-like covering of the scalp .

Example answer:
{"entities": [{"text": "hearing impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ichthyosiform erythroderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "palmoplantar keratoderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alopecia of the scalp and eyelashes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On histological analysis , features characteristic of KID syndrome , such as acanthosis and papillomatosis of the epidermis with basket-weave hyperkeratosis , were seen .

Example answer:
{"entities": [{"text": "KID syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acanthosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "papillomatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkeratosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: D90A-SOD1 mediated amyotrophic lateral sclerosis : a single founder for all cases with evidence for a Cis-acting disease modifier in the recessive haplotype .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ectodermal dysplasia-skin fragility syndrome resulting from a new homozygous mutation , 888delC , in the desmosomal protein plakophilin 1 .

Example answer:
{"entities": [{"text": "Ectodermal dysplasia-skin fragility syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "888delC", "type": "SequenceVariant"}, {"text": "plakophilin 1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We found 8 p53 mutations in 7/17 ( 41 % ) precancerous actinic keratosis ( AK ) , suggesting that p53 mutations are early events in RTR skin carcinogenesis .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "actinic keratosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report an unusual case of an inherited disorder of the desmosomal protein plakophilin 1 , resulting in ectodermal dysplasia-skin fragility syndrome .

Example answer:
{"entities": [{"text": "inherited disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "plakophilin 1", "type": "GeneOrGeneProduct"}, {"text": "ectodermal dysplasia-skin fragility syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Disseminated superficial actinic porokeratosis ( DSAP ) is an uncommon autosomal dominant chronic keratinization disorder , characterized by multiple superficial keratotic lesions surrounded by a slightly raised keratotic border .

## Item biored:test:195
Example input:
Sentence: Control ( saline P20 ) rats acquired both discriminations immediately .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: When combined with the initial linkage paper our haplotype and linkage data map the MCOR locus to a 6-7 cM region between D13S265 and D13S1280 .

Example answer:
{"entities": [{"text": "MCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Four ultraconserved regions distal to ARX ( uc466-469 ) were also screened in a subset of 94 patients , with three unique nucleotide changes identified in two ( uc466 , uc467 ) .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Four animal groups ( n = 6 ) were tested during 9 weeks : control , CsA , SRL , and conversion ( CsA for 3 weeks followed by SRL for 6 weeks ) .

Example answer:
{"entities": [{"text": "CsA", "type": "ChemicalEntity"}, {"text": "SRL", "type": "ChemicalEntity"}]}

Example input:
Sentence: The dual-luciferase reporter assay revealed that the -395A carrier of a 498-bp DNA fragment ( containing the G-395A site ) upstream of the Klotho gene has higher relative luciferase activity than the -395G carrier .

Example answer:
{"entities": [{"text": "-395A", "type": "SequenceVariant"}, {"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "-395G", "type": "SequenceVariant"}]}

Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PbtO ( 2 ) decreased from 51.7 +/- 4.5 mm Hg sem to 33.8 +/- 5.2 mm Hg sem in the NTG group and from 38.6 +/- 6.1 mm Hg sem to 25.4 +/- 2.0 mm Hg sem in the NTG + NIMO groups , respectively .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Functional analyses reveal that whilst cilium structure , sensory function and IFT are seemingly normal in a rab-28 null allele , overexpression of predicted GDP or GTP locked variants of RAB-28 perturbs cilium and sensory pore morphogenesis and function .

Example answer:
{"entities": [{"text": "rab-28", "type": "GeneOrGeneProduct"}, {"text": "GDP", "type": "ChemicalEntity"}, {"text": "GTP", "type": "ChemicalEntity"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: However , the results of the width of the GAP43-ir band in the IML showed that CHX+Pilo and control animals had a significantly larger band ( p = 0.03 ) as compared with that in the Pilo group .

## Item biored:test:161
Example input:
Sentence: The Shh ( CreERT2/+ ) ; b-catenin ( flox ( ex3 ) /+ ) ; BmprIA ( flox/- ) mutants displayed partial restoration of URS elongation compared with the b-catenin GOF mutants .

Example answer:
{"entities": [{"text": "Shh", "type": "GeneOrGeneProduct"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "BmprIA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: PTCH1 gene mutations in exon 17 and loss of heterozygosity on D9S180 microsatellite in sporadic and inherited human basal cell carcinomas .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "basal cell carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Co-transfection experiment of both wild-type and mutant plasmids indicated the dominant-negative mechanism of disease development ; as more of mutant DNA was transfected , VWF secretion was impaired in the media , whereas more of VWF was stored in the cell lysates .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Transfection of complementary DNA for both the wild-type ANKH and the -4-bp ANKH protein variant promoted increased extracellular PPi in CH-8 cells , but unexpectedly , these ANKH mutants had divergent effects on the expression of extracellular PPi and the chondrocyte hypertrophy marker , type X collagen .

## Item biored:test:222
Example input:
Sentence: Lower doses ( 3 and 10mg/kg ) did not suppress seizures , however , after administration of 10mg/kg , significant reductions in seizures duration ( 24.3+/-6.8s ) and seizure number ( 1.6+/-0.34 ) were found .

Example answer:
{"entities": [{"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Patients with dyskinesia had lower onset age ( p < 0.001 ) , longer duration of levodopa therapy ( p < 0.001 ) , longer disease duration ( p < 0.001 ) , higher total daily levodopa dose ( p < 0.001 ) , and higher total UPDRS scores ( p = 0.005 ) than patients without dyskinesia .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In both types , purinoceptor desensitization with alpha , beta-methylene adenosine-5'-triphosphate ( alpha , beta-meATP ) caused further reductions at low frequencies ( < 10 Hz ) .

Example answer:
{"entities": [{"text": "alpha , beta-methylene adenosine-5'-triphosphate", "type": "ChemicalEntity"}, {"text": "alpha , beta-meATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chronic T treatment significantly decreased 5-HT and 5-HIAA in certain brain areas , but to a much lesser extent than PCPA .

Example answer:
{"entities": [{"text": "T", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HIAA", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Generally , atropine reduced contractions , but in contrast to controls , it also reduced responses to low electrical field stimulation intensity ( 1-5 Hz ) in inflamed preparations .

Example answer:
{"entities": [{"text": "atropine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Apamin ( 10 ng ) had a tendency to decrease the convulsive threshold ( 21.6 +/- 2.2 to 19.9 +/- 2.5 mg. l ( -1 ) ) but this was not statistically significant .

Example answer:
{"entities": [{"text": "Apamin", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , there is convincing clinical evidence that monotherapy with continuous subcutaneous apomorphine infusions is associated with marked reductions of preexisting levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice subjected to hypotensive episodes showed a significant decrease in latency time ( 178 +/- 156 s ) compared with those injected with saline , NTG + NIMO , or delayed NTG ( 580 +/- 81 s , 557 +/- 67 s , and 493 +/- 146 s , respectively ) .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chronic pulsatile levodopa therapy for Parkinson 's disease ( PD ) leads to the development of motor fluctuations and dyskinesia .

Example answer:
{"entities": [{"text": "levodopa", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: rTMS at 1 Hz was observed to markedly reduce drug-induced dyskinesias , whereas 5-Hz rTMS induced a slight but not significant increase .

## Item biored:test:232
Example input:
Sentence: Linkage disequilibrium analysis indicates that D90A homozygotes and heterozygotes share a rare haplotype and are all descended from a single ancient founder ( alpha 0.974 ) c.895 generations ago .

Example answer:
{"entities": [{"text": "D90A", "type": "SequenceVariant"}]}

Example input:
Sentence: One possibility might be that individuals who are compound heterozygotes for ATM mutations are more common than we realize ..

Example answer:
{"entities": [{"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Non-syndromic deafness is genetically heterogeneous .

Example answer:
{"entities": [{"text": "Non-syndromic deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The polymorphism distribution was also analyzed in AD patients stratified according to differential progressive rate of cognitive decline during a 2-year follow-up .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients were divided into three groups and each group had 20 patients .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Eighty-one percent of patients with dyskinesia had clinical fluctuations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The first was to estimate the frequency of loss of heterozygosity ( LOH ) of the RB1 gene as a mechanism in disease causation in tumors of patients from India .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Consequently , there is genetic heterogeneity , but until recently , little is known about the genes involving in the pathogenesis of AVSD .

Example answer:
{"entities": [{"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Clinical heterogeneity was present in the patients .

## Item biored:test:233
Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: The patient was a compound heterozygote for SRD5A2 mutations , carrying 2 mutations in exon 4 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , the same deletion patterns covered the entire p14 gene for all cases except for one case , which suggested the hemizygous deletion of exons 1beta and 2 and homozygous deletion of exon 3 .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: The compound heterozygous mutations , c.892C > T and c.1072T > C , were identified in exon 3 of CHST6 in three patients .

Example answer:
{"entities": [{"text": "c.892C > T", "type": "SequenceVariant"}, {"text": "c.1072T > C", "type": "SequenceVariant"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Compound heterozygotes for the deletion in exon 7 seemed to have more severe disease compared to patients homozygous for the deletion .

## Item biored:test:121
Example input:
Sentence: Like human TRPV6 , the truncated human TRPV6 ( Delta695-725 ) , which lacks the C-terminal domain required for Ca ( 2+ ) -calmodulin binding , does not form constitutive active channels , whereas the human TRPV6 ( D542A ) , carrying a point mutation in the presumed pore region , does not function as a channel .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "TRPV6", "type": "GeneOrGeneProduct"}, {"text": "Delta695-725", "type": "SequenceVariant"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "D542A", "type": "SequenceVariant"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: If recombinantly expressed TRPV6 forms open channels , one would expect Ca ( 2+ ) -induced current inhibition , because TRPV6 is negatively regulated by internal Ca ( 2+ ) .

Example answer:
{"entities": [{"text": "TRPV6", "type": "GeneOrGeneProduct"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Characterization of a novel BCHE `` silent '' allele : point mutation ( p.Val204Asp ) causes loss of activity and prolonged apnea with suxamethonium .

Example answer:
{"entities": [{"text": "BCHE", "type": "GeneOrGeneProduct"}, {"text": "p.Val204Asp", "type": "SequenceVariant"}, {"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "suxamethonium", "type": "ChemicalEntity"}]}

Example input:
Sentence: In contrast , dialyzing 0.5 mm EGTA into TRPV6-expressing cells readily activated Ca ( 2+ ) inward currents , which were undetectable in non-transfected cells .

Example answer:
{"entities": [{"text": "EGTA", "type": "ChemicalEntity"}, {"text": "TRPV6-expressing", "type": "GeneOrGeneProduct"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Inhibition of Na ( + ) channels by local anesthetics may regulate desipramine-induced down-regulation of NET function .

Example answer:
{"entities": [{"text": "Na ( + )", "type": "ChemicalEntity"}, {"text": "anesthetics", "type": "ChemicalEntity"}, {"text": "desipramine-induced", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of this study is to show that FPD from MEA ( Multielectrode array ) of hiPS-CMs can detect QT prolongation induced by multichannel blockers .

Example answer:
{"entities": [{"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Input:
Sentence: CONCLUSIONS : These findings suggest that the Na ( v ) 1.5/V1763M channel dysfunction and possible neighboring mutants contribute to a persistent inward current due to altered inactivation kinetics and clinically congenital LQTS with perinatal onset of arrhythmias that responded to lidocaine and mexiletine .

## Item biored:test:188
Example input:
Sentence: In addition , rats that experienced SE exhibited CCR2-labeling in populations of hypertrophied astrocytes , especially in CA1 and dentate gyrus .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCR2-labeling", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The histological features were improved in hippocampus of rats treated with ZnSO ( 4 ) + BCNU compared to only BCNU-treated animals .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "BCNU-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition , GABA content of mice hippocampus treated with GFC75 plus P400 showed an increase of 46.90 % when compared with seized mice .

Example answer:
{"entities": [{"text": "GABA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Chemokine CCL2 and its receptor CCR2 are increased in the hippocampus following pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Growth-associated protein 43 expression in hippocampal molecular layer of chronic epileptic rats treated with cycloheximide .

## Item biored:test:146
Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVE : To report a case of a severe interaction between simvastatin , amiodarone , and atazanavir resulting in rhabdomyolysis and acute renal failure .

Example answer:
{"entities": [{"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We herein report the case of a 70-year-old man with 5-FU-induced cardiotoxicity , in whom a high serum level of alpha-fluoro-beta-alanine ( FBAL ) was observed .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "5-FU-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fluoro-beta-alanine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CASE SUMMARY : A 42-year-old white man developed acute hypertension with severe headache and vomiting 2 hours after the first doses of amisulpride 100 mg and tiapride 100 mg .

## Item biored:test:180
Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymorphisms in the IRF5 gene have been associated with susceptibility to systemic lupus erythaematosus ( SLE ) in Caucasian and Asian populations , but their involvement in other autoimmune diseases is still uncertain .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythaematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These findings indicate that the promoter polymorphism of IRF5 is a genetic factor conferring predisposition to RA , and that it contributes considerably to disease pathogenesis in patients that were SE negative .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Polymorphisms or other variants in the BRAF gene may therefore act as candidate low-penetrance genes for nevus/melanoma susceptibility .

## Item biored:test:191
Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: In Alzheimer 's disease groups , rats were injected with STZ-icv bilaterally ( 3 mg/kg ) in first day and 3 days later , a similar STZ-icv application was repeated .

Example answer:
{"entities": [{"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ-icv", "type": "ChemicalEntity"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were anesthetized with i.p .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : SE was induced by pilocarpine injection .

Example answer:
{"entities": [{"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Sprague-Dawley rats were injected with saline on postnatal day ( P ) 20 , or a convulsant dose of pilocarpine on P20 or P45 .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Control rats were injected with saline instead of pilocarpine .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: METHODS : CHX was injected before the Pilo injection in adult Wistar rats .
