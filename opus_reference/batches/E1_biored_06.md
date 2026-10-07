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

## Item biored:test:223
Example input:
Sentence: The patient was a compound heterozygote for SRD5A2 mutations , carrying 2 mutations in exon 4 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TGFBI gene mutations causing lattice and granular corneal dystrophies in Indian patients .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "lattice and granular corneal dystrophies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Point mutations in the BICD2 gene have been identified in patients with a dominant form of spinal muscular atrophy , but how these mutations cause disease is unknown .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "spinal muscular atrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: With the advent of next-generation sequencing technologies , the homozygous mutations T71N and A190T in the neuronal calcium sensor ( NCS ) hippocalcin were identified as the genetic cause of primary isolated dystonia ( DYT2 dystonia ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "neuronal calcium sensor", "type": "GeneOrGeneProduct"}, {"text": "NCS", "type": "GeneOrGeneProduct"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "primary isolated dystonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In GCD , 18 patients with GCD type I had a mutation of arginine 555-to-tryptophan ( Arg555Trp ) and 1 patient with GCD type III ( Reis-Bucklers dystrophy ) , had the Arg124Leu mutation .

Example answer:
{"entities": [{"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "GCD type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 555-to-tryptophan", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GCD type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Reis-Bucklers dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Arg124Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: Disease-associated mutations in human BICD2 hyperactivate motility of dynein-dynactin .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein-dynactin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Characterization of Bietti crystalline dystrophy patients with CYP4V2 mutations .

## Item biored:test:245
Example input:
Sentence: There was also a statistically significant p-value of the ( 2 ) test for the trend observed in the XRCC1 Arg399Gln polymorphism ( ptrend=0.0048 ) .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}]}

Example input:
Sentence: Odds ratios and 95 % confidence intervals for cancer risk by MLH1 -93 polymorphism status , and stratified by previous exposure to methylating chemotherapy , were calculated using unconditional logistic regression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: No correlation was found between tumor type , tumor location , local tumor growth , distant metastases , and the ACE genotype .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A Stratified analysis of the genotypes with age of onset and tumor grade showed the w1/m1 genotype to be significantly associated with an early age of onset ; however the tumor grades did not have significant association with the variant genotypes .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients with the II genotype had a highly significantly smaller number of lymph node metastases ( P < 0.001 ) and a significantly lower UICC tumor stage ( P = 0.01 ) than patients with the DD genotype .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "lymph node metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We did not observe any correlation between studied polymorphisms and breast cancer progression evaluated by node-metastasis , tumor size and Bloom-Richardson grading .

## Item biored:test:252
Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether c.609+28_610-16del allele-derived transcripts were subject to nonsense-mediated mRNA decay ( NMD ) , patient fibroblasts were incubated with the protein synthesis inhibitor anisomycin .

Example answer:
{"entities": [{"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "anisomycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A haplotype containing these four SNPs ( CATA ) significantly increased protection of wet AMD with a P value of 0.0005 and an odds ratio of 0.29 ( 95 % confidence interval : 0.15-0.60 ) .

Example answer:
{"entities": [{"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: FISH analysis confirmed c-REL amplification in patients with gains at 2p16.1 .

## Item biored:test:55
Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "ChemicalEntity"}, {"text": "calcium-dependent", "type": "ChemicalEntity"}, {"text": "potassium", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: In Alzheimer 's disease groups , rats were injected with STZ-icv bilaterally ( 3 mg/kg ) in first day and 3 days later , a similar STZ-icv application was repeated .

Example answer:
{"entities": [{"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ-icv", "type": "ChemicalEntity"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

## Item biored:test:254
Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using PCR-RFLP , we confirmed the heterozygous mutation in six affected family members and excluded it in three healthy members .

Example answer:
{"entities": []}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subsequent mutation analysis of PQBP1 , located within the delineated linkage interval in Xp11.23 , revealed a 2-bp deletion , c.461_462delAG , that cosegregated with the disease .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "c.461_462delAG", "type": "SequenceVariant"}]}

Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Homozygous deletion of 9p21.3 was detected in five of 12 patients with PCLBCL , leg type , but in zero of 19 patients with PCFCL .

## Item biored:test:278
Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Maximal contraction to norepinephrine was modestly reduced in arteries from LNNA compared with control rats whereas the maximum contraction to ET-1 was significantly reduced ( 54 % control ) .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Renal angiotensin II receptor type 2 ( AT2R ) gene expression in adult offspring was reduced by PCE , whereas the renal angiotensin II receptor type 1a ( AT1aR ) /AT2R expression ratio was increased .

Example answer:
{"entities": [{"text": "angiotensin II receptor type 2", "type": "GeneOrGeneProduct"}, {"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "angiotensin II receptor type 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1aR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The renin-angiotensin system is involved in tumor growth and metastases .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: The cause appears to be the Bezold-Jarish reflex , stimulation of the ventricular walls which in turn decreases sympathetic outflow from the vasomotor centre .

Example answer:
{"entities": []}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We have previously shown that a permanent deficiency in the brain renin-angiotensin system ( RAS ) may increase the sensitivity of the baroreflex control of heart rate .

## Item biored:test:261
Example input:
Sentence: In Mz-ChA-1 cells stimulated with ( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide ( RAMH ) , we measured ( a ) cell growth , ( b ) IP ( 3 ) and cyclic AMP levels , and ( c ) phosphorylation of PKC and mitogen-activated protein kinase isoforms .

Example answer:
{"entities": [{"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide", "type": "ChemicalEntity"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study was aimed at investigating the effects of Daucus carota seeds on cognitive functions , total serum cholesterol levels and brain cholinesterase activity in mice .

Example answer:
{"entities": [{"text": "Daucus carota", "type": "OrganismTaxon"}, {"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "cholinesterase", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Curcumin is the active component of tumeric , and this polyphenolic compound has been extensively investigated as an anticancer drug that modulates multiple pathways and genes .

Example answer:
{"entities": [{"text": "Curcumin", "type": "ChemicalEntity"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Methanolic extracts from Pueraria thunbergiana exhibited an activation effect ( 46 % ) on ChAT in vitro .

## Item biored:test:255
Example input:
Sentence: In the original MB-DRM German family , we demonstrated a linkage of the disease to the SEPN1 locus ( 1p36 ) , and subsequently a homozygous SEPN1 deletion ( del 92 nucleotide -19/+73 ) in the affected patients .

Example answer:
{"entities": [{"text": "SEPN1", "type": "GeneOrGeneProduct"}, {"text": "del 92 nucleotide -19/+73", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Microdissected MC lesions from two patients with PTPN11 mutations demonstrated loss-of-heterozygosity for the wild-type allele .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PTPN11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Example input:
Sentence: We have shown that hyperopia and LCA are linked to the mutant CRB1 gene itself and are not dependent on unlinked modifiers .

Example answer:
{"entities": [{"text": "hyperopia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Methylation of the 5'CpG island of the p14 gene was not suggested for any case without homozygous deletion .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Complete methylation of the promoter region of the CDKN2A gene was demonstrated in one PCLBCL , leg type , patient with hemizygous deletion , in one patient without deletion , but in zero of 19 patients with PCFCL .

## Item biored:test:258
Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Carriers of TBX21 promoter SNP rs17250932 and HLX1 promoter SNP rs2738751 showed reduced or trendwise reduced ( p < 0.07 ) IL-5 , IL-13 and TNF-a secretion after LpA-stimulation .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "rs17250932", "type": "SequenceVariant"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Single nucleotide polymorphism in ABCG2 is associated with irinotecan-induced severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan-induced", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our observation of frequent p14 gene abnormalities ( 90 % ) and inactivation ( 40-60 % ) was in striking contrast to the same pathological subtype of systemic lymphoma in which p14 gene abnormalities and inactivation were infrequent , suggesting a difference in carcinogenesis between PCNSL and systemic lymphoma .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "systemic lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Inactivation of CDKN2A by either deletion or methylation of its promoter could be an important prognostic parameter for the group of PCLBCL , leg type .

## Item biored:test:257
Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: These results support the conclusion that the 1858C/T allele is the major risk variant for type 1 diabetes in the PTPN22 locus , but they suggest that additional infrequent coding variants at PTPN22 may also contribute to type 1 diabetes risk .

Example answer:
{"entities": [{"text": "1858C/T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction performed with DNA isolated from somatic human-rodent cell hybrids containing defined human chromosomes as template gave a human-specific signal which mapped the NDUFS2 and NDUFS3 subunits to chromosomes 1 and 11 , respectively .

Example answer:
{"entities": [{"text": "human-rodent", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "human-specific", "type": "OrganismTaxon"}, {"text": "NDUFS2", "type": "GeneOrGeneProduct"}, {"text": "NDUFS3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS AND FINDINGS : Cord blood mononuclear cells ( CBMCs ) of 200 neonates were genotyped for two TBX21 and three HLX1 SNPs .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : We corroborated the association of the promoter indel with SLE in 5 different populations and revealed that rs10954213 is the main single-nucleotide polymorphism responsible for altered IRF5 expression in PBMC .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs10954213", "type": "SequenceVariant"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our observation of frequent p14 gene abnormalities ( 90 % ) and inactivation ( 40-60 % ) was in striking contrast to the same pathological subtype of systemic lymphoma in which p14 gene abnormalities and inactivation were infrequent , suggesting a difference in carcinogenesis between PCNSL and systemic lymphoma .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "systemic lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSION : Our results demonstrate prominent differences in chromosomal alterations between PCFCL and PCLBCL , leg type , that support their classification as separate entities within the WHO-EORTC scheme .

## Item biored:test:300
Example input:
Sentence: RESULTS : By clinical examination , the patients and the pedigrees were divided into the following three groups : AN , coloboma of iris and choroids , and the anterior segment malformations including peters anomaly .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroids", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "peters anomaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Of 13 documented fractures , 3 occurred after risperidone and SSRIs were started , and none occurred in patients with hyperprolactinemia .

Example answer:
{"entities": [{"text": "fractures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}, {"text": "SSRIs", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After adjusting for the stage of sexual development and height and BMI z scores , serum prolactin was negatively associated with trabecular volumetric BMD at the ultradistal radius ( P < .03 ) .

Example answer:
{"entities": [{"text": "prolactin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Pituitary adenoma predisposition ( PAP ) has been recently associated with germline mutations in the aryl hydrocarbon receptor interacting protein ( AIP ) gene .

Example answer:
{"entities": [{"text": "Pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PATIENTS : A population-based cohort consisting of 36 apparently sporadic paediatric pituitary adenoma patients , referred to two medical centres in Italy , was included in the study .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Identification of a gain-of-function mutation of the prolactin receptor in women with benign breast tumors .

Example answer:
{"entities": [{"text": "prolactin receptor", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "benign breast tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Hyperprolactinemia was present in 49 % of 83 boys ( n = 41 ) treated with risperidone for a mean of 2.9 years .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Multiple fibroadenomas ( MFA ) are benign breast tumors which appear most frequently in young women , including at puberty , when Prl has well-recognized proliferative actions on the breast .

Example answer:
{"entities": [{"text": "Multiple fibroadenomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MFA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign breast tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "Prl", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There is currently no known genetic disease linked to prolactin ( Prl ) or its receptor ( PrlR ) in humans .

Example answer:
{"entities": [{"text": "genetic disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prolactin", "type": "GeneOrGeneProduct"}, {"text": "Prl", "type": "GeneOrGeneProduct"}, {"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Input:
Sentence: There was also a prolactinoma .

## Item biored:test:301
Example input:
Sentence: The exon 4 sequence of TGFBI of the proband exhibits the heterozygous single-nucleotide mutation , C417T , leading to amino acid substitution ( R124C ) in the encoded TGF-induced protein .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "C417T", "type": "SequenceVariant"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGF-induced protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Molecular characterization by DNA sequencing analysis and multiplex ligation-dependent probe amplification of the MLYCD gene revealed a heterozygous mutation ( c.920T > G , p.Leu307Arg ) in the patient and his father and a heterozygous deletion comprising exon 1 in the patient and his mother .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "c.920T > G", "type": "SequenceVariant"}, {"text": "p.Leu307Arg", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a prospective study involving 74 MFA patients and 170 control subjects , we identified four patients harboring a heterozygous single nucleotide polymorphism in exon 6 of the PrlR gene , encoding Ile ( 146 ) -- > Leu substitution in its extracellular domain .

Example answer:
{"entities": [{"text": "MFA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "Ile ( 146 ) -- > Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: This study aimed to identify mutations in a Chinese pedigree with MEN1 .

Example answer:
{"entities": [{"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutation in exon 10 of MEN1 gene might induce development of parathyroid hyperplasia and pituitary adenoma and cosegregate with MEN1 syndrome .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}, {"text": "parathyroid hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1 syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: BACKGROUND : Multiple endocrine neoplasia type 1 ( MEN1 ) is an autosomal dominant cancer syndrome which is caused by germline mutations of the tumor suppressor gene MEN1 .

Example answer:
{"entities": [{"text": "Multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All of the coded regions and their adjacent sequences of the MEN1 gene were amplified and sequenced .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Sequence analysis of the MEN1 gene from leukocyte genomic DNA revealed heterozygous mutations in both probands .

## Item biored:test:268
Example input:
Sentence: Prolonged hypothermia as a bridge to recovery for cerebral edema and intracranial hypertension associated with fulminant hepatic failure .

Example answer:
{"entities": [{"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Alternatively , anemia could result from accelerated suicidal erythrocyte death or eryptosis , which is characterized by exposure of phosphatidylserine ( PS ) at the erythrocyte surface and by cell shrinkage .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "phosphatidylserine", "type": "ChemicalEntity"}, {"text": "PS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hemoglobin", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaundice", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Anemia and hepatitis often occur within 12 weeks of initiating generic HAART .

Example answer:
{"entities": [{"text": "Anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Definition and management of anemia in patients infected with hepatitis C virus .

## Item biored:test:214
Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "calcineurin inhibitors", "type": "ChemicalEntity"}, {"text": "mammalian target of rapamycin ( mToR ) inhibitors", "type": "ChemicalEntity"}, {"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "chronic allograft nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Example input:
Sentence: In conclusion , Sal treatment improves kidney function , ameliorates the deposition of the ECM components and relieves the protein levels of EMT markers in mouse kidneys and HK-2 cells .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Input:
Sentence: Erdosteine administration with VCM injections caused significantly decreased renal MDA and urinary NAG excretion , and increased SOD activity , but not CAT activity in renal tissue when compared with VCM alone .

## Item biored:test:304
Example input:
Sentence: The missense mutation ( c.920T > G ) was not found in 100 healthy controls and has not been reported previously .

Example answer:
{"entities": [{"text": "c.920T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Human TBX1 missense mutations cause gain of function resulting in the same phenotype as 22q11.2 deletions .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "TBX1", "type": "GeneOrGeneProduct"}, {"text": "22q11.2 deletions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Two novel missense mutations were detected in the catalytic subdomain of the PCSK9 gene .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All of the coded regions and their adjacent sequences of the MEN1 gene were amplified and sequenced .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study aimed to identify mutations in a Chinese pedigree with MEN1 .

Example answer:
{"entities": [{"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutation in exon 10 of MEN1 gene might induce development of parathyroid hyperplasia and pituitary adenoma and cosegregate with MEN1 syndrome .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}, {"text": "parathyroid hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1 syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Multiple endocrine neoplasia type 1 ( MEN1 ) is an autosomal dominant cancer syndrome which is caused by germline mutations of the tumor suppressor gene MEN1 .

Example answer:
{"entities": [{"text": "Multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In conclusion , we have identified 2 novel missense mutations in the MEN1 gene .

## Item biored:test:247
Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The expression of MLPH in primary prostate tumors was significantly lower in those with the G compared with the T allele and correlated significantly with AR protein .

Example answer:
{"entities": [{"text": "MLPH", "type": "GeneOrGeneProduct"}, {"text": "prostate tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymorphic MLH1 and risk of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Odds ratios and 95 % confidence intervals for cancer risk by MLH1 -93 polymorphism status , and stratified by previous exposure to methylating chemotherapy , were calculated using unconditional logistic regression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Loss of MLH1 , a major component of DNA MMR , results in tolerance to the cytotoxic effects of methylating agents and persistence of mutagenised cells at high risk of malignant transformation .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cytotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Therefore , MMR may play a role in the breast carcinogenesis and the Gly322Asp polymorphism of the hMSH2 gene may be considered as a potential marker in breast cancer .

## Item biored:test:280
Example input:
Sentence: Rats were exposed to BCNU on embryonic day 15 and melatonin was given until delivery .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At puberty ( P40 ) , half the PCPA-treated rats and half the saline-treated rats began treatment with testosterone ( T , 5 mg/kg , 5 days/week ) .

Example answer:
{"entities": [{"text": "PCPA-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: We hypothesized that Thra1 ( PV/+ ) mice could be used to predict the skeletal outcome of human THRA mutations and determine whether prolonged treatment with a supraphysiological dose of T4 ameliorates the skeletal abnormalities .

Example answer:
{"entities": [{"text": "Thra1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "THRA", "type": "GeneOrGeneProduct"}, {"text": "T4", "type": "ChemicalEntity"}, {"text": "skeletal abnormalities", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have generated transgenic mice that express a constitutively active version of human H-Ras in their lenses and corneas .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "H-Ras", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In Alzheimer 's disease groups , rats were injected with STZ-icv bilaterally ( 3 mg/kg ) in first day and 3 days later , a similar STZ-icv application was repeated .

Example answer:
{"entities": [{"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ-icv", "type": "ChemicalEntity"}]}

Example input:
Sentence: A rat model of IUGR was established by PCE , male fetuses and adult offspring at the age of postnatal week 24 were euthanized .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "IUGR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Input:
Sentence: Transgenic rats with low brain angiotensinogen ( TGR ) were used .

## Item biored:test:289
Example input:
Sentence: The mean reduction in MSSBP/MSDBP with VAL/HCTZ 320/25 mg was 24.7/16.6 mm Hg , compared with 5.9/7.0 mm Hg with placebo .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the present study , we investigated whether 50 mg/kg per day , p.o. , Ato could prevent endothelial NO synthase ( eNOS ) downregulation and the increase in O2- in Sprague-Dawley ( SD ) rats , thereby reducing blood pressure .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "endothelial NO synthase", "type": "GeneOrGeneProduct"}, {"text": "eNOS", "type": "GeneOrGeneProduct"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: Aortic superoxide production was lower in the Dex + Ato group compared with the group treated with Dex alone ( P < 0.0001 ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: Treatment with Ato improved endothelial function , reduced superoxide production and reduced SBP in Dex-treated SD rats .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}, {"text": "Dex-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Input:
Sentence: In this prevention study , SBP in the atorva + dex group was increased from 115 +/- 0.4 to 124 +/- 1.5 mmHg , but this was significantly lower than in the dex-only group ( P ' < 0.05 ) .

## Item biored:test:288
Example input:
Sentence: Dexamethasone- ( Dex- ) induced hypertension is associated with enhanced oxidative stress .

Example answer:
{"entities": [{"text": "Dexamethasone-", "type": "ChemicalEntity"}, {"text": "Dex-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "tempol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "LNNA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone ( Dex ) -induced hypertension is characterized by endothelial dysfunction associated with nitric oxide ( NO ) deficiency and increased superoxide ( O2- ) production .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitric oxide", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}, {"text": "O2-", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chronic administration of LF strongly reduced the blood pressure and production of ROS and improved antioxidant capacity in Dex-induced hypertension , suggesting the role of inhibition of oxidative stress as another mechanism of antihypertensive action of LF .

Example answer:
{"entities": [{"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "Dex-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Treatment with Ato improved endothelial function , reduced superoxide production and reduced SBP in Dex-treated SD rats .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}, {"text": "Dex-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Aortic superoxide production was lower in the Dex + Ato group compared with the group treated with Dex alone ( P < 0.0001 ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Input:
Sentence: Dex increased systolic blood pressure ( SBP ) from 109 +/- 1.8 to 135 +/- 0.6 mmHg and plasma superoxide ( 5711 +/- 284.9 saline , 7931 +/- 392.8 U/ml dex , P < 0.001 ) .

## Item biored:test:298
Example input:
Sentence: OBJECTIVE : Five Chinese patients with 17alpha-hydroxylase deficiency were genotyped .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "17alpha-hydroxylase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The study group consisted of 66 Polish families with cancer who have at least three related females affected with breast or ovarian cancer and who had cancer diagnosed , in at least one of the three affected females , at age < 50 years .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast or ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : We have confirmed the localization of the congenital microcoria locus ( MCOR ) to 13q31-q32 in a large Asian Indian family and conclude that current information suggests this is a single locus disorder and genetically homogeneous .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A patient of Chinese origin with ambiguous genitalia at 14 months , a 46 , XY karyotype , and normal T secretion under human chorionic gonadotropin ( hCG ) stimulation underwent a gonadectomy at 20 months .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "human chorionic gonadotropin", "type": "ChemicalEntity"}, {"text": "hCG", "type": "ChemicalEntity"}]}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS : The five patients derived from four families living in Shandong Province , China .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: The index patient in the second family was a 46-yr-old woman of Chinese origin living in Taiwan .

## Item biored:test:203
Example input:
Sentence: The human mu opiate receptor ( h mu OR1 ) shares 95 % amino acid identity with the rat sequence .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "mu opiate receptor", "type": "GeneOrGeneProduct"}, {"text": "h mu OR1", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: A human mu opiate receptor cDNA has been identified from a cerebral cortical cDNA library using sequences from the rat mu opiate receptor cDNA .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "mu opiate receptor", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that OPRM1 is expressed in all leukemic cells tested .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Consistent with this premise , patient leukemic cells with relatively high levels of OPRM1 are more sensitive to L-asparaginase treatment compared to OPRM1-depleted leukemic cells , further indicating that OPRM1 loss has a crucial role in L-asparaginase resistance in leukemic patients .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Specific knockdown of OPRM1 confers L-asparaginase resistance , validating our genome-wide retroviral shRNA library screening data .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Transfection into Chinese hamster ovary cells of a cDNA representing only the coding region of OPRM1 , carrying adenosine , guanosine , cytidine , and thymidine in position 118 , resulted in 1.5-fold lower mRNA levels only for OPRM1-G118 , and more than 10-fold lower OPRM1 protein levels , measured by Western blotting and receptor binding assay .

## Item biored:test:224
Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In GCD , 18 patients with GCD type I had a mutation of arginine 555-to-tryptophan ( Arg555Trp ) and 1 patient with GCD type III ( Reis-Bucklers dystrophy ) , had the Arg124Leu mutation .

Example answer:
{"entities": [{"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "GCD type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 555-to-tryptophan", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GCD type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Reis-Bucklers dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Arg124Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: A missense mutation in BCOR was described in a family with Lenz microphthalmia syndrome , a phenotype showing substantial overlapping features with that described in the two cousins .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}, {"text": "Lenz microphthalmia syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With the advent of next-generation sequencing technologies , the homozygous mutations T71N and A190T in the neuronal calcium sensor ( NCS ) hippocalcin were identified as the genetic cause of primary isolated dystonia ( DYT2 dystonia ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "neuronal calcium sensor", "type": "GeneOrGeneProduct"}, {"text": "NCS", "type": "GeneOrGeneProduct"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "primary isolated dystonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Disease-associated mutations in human BICD2 hyperactivate motility of dynein-dynactin .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein-dynactin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Point mutations in the BICD2 gene have been identified in patients with a dominant form of spinal muscular atrophy , but how these mutations cause disease is unknown .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "spinal muscular atrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: PURPOSE : Mutations of the CYP4V2 gene , a novel family member of the cytochrome P450 genes on chromosome 4q35 , have recently been identified in patients with Bietti crystalline dystrophy ( BCD ) .

## Item biored:test:218
Example input:
Sentence: In conclusion , Sal treatment improves kidney function , ameliorates the deposition of the ECM components and relieves the protein levels of EMT markers in mouse kidneys and HK-2 cells .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our results show that treatment with Sal can ameliorate tubular injury and deposition of the extracellular matrix ( ECM ) components ( including collagen SH and collagen I ) .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "tubular injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "collagen SH", "type": "GeneOrGeneProduct"}, {"text": "collagen I", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Also , histopathological renal tissue damage mediated by cisplatin was ameliorated by coenzyme Q10 treatment .

Example answer:
{"entities": [{"text": "renal tissue damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "coenzyme Q10", "type": "ChemicalEntity"}]}

Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Oxidative stress may be involved in the development of stone formation in the renal system .

Example answer:
{"entities": [{"text": "stone formation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , Hsp90beta inhibition-mediated renal improvements also accompanied the reduction of renal oxidative stress .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The nephroprotective effect of coenzyme Q10 was investigated in mice with acute renal injury induced by a single i.p .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "acute renal injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results of the present study suggested that atorvastatin protected against contrast-induced renal tubular cell apoptosis through the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced renal tubular cell apoptosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hsp90beta inhibition caused the destabilization of upstream mediators in various pathogenic signalling events , thereby effectively ameliorating this nephropathy owing to renal hypoxia and oxidative stress .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoxia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: It is concluded that oxidative tubular damage plays an important role in the VCM-induced nephrotoxicity and the modulation of oxidative stress with erdosteine reduces the VCM-induced kidney damage both at the biochemical and histological levels .

## Item biored:test:250
Example input:
Sentence: To investigate the GSTP1 Ile105Val genotype frequency in prostate cancer cases in the Kashmiri population , we designed a case-control study , in which 50 prostate cancer cases and 45 benign prostate hyperplasia cases were studied for GSTP1 Ile105Val polymorphism , compared to 80 controls taken from the general population , employing the PCR-RFLP technique .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: HPV DNA was detected in 78 % of skin lesions ( 60 % Basal Cell Carcinomas , 82 % AK and 79 % SCCs ) .

Example answer:
{"entities": [{"text": "HPV", "type": "OrganismTaxon"}, {"text": "skin lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Basal Cell Carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The majority of CXCR5 ( + ) PD1 ( + ) CD4 ( + ) T follicular helper ( Tfh ) cells ( > 90 % ) are CD25 ( - ) Bcl6 ( hi ) , while a small subpopulation ( < 10 % ) are CD25 ( + ) Bcl6 ( low ) but do not express FoxP3 and are not T regulatory cells .

Example answer:
{"entities": [{"text": "CXCR5", "type": "GeneOrGeneProduct"}, {"text": "PD1", "type": "GeneOrGeneProduct"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "Bcl6", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our observation of frequent p14 gene abnormalities ( 90 % ) and inactivation ( 40-60 % ) was in striking contrast to the same pathological subtype of systemic lymphoma in which p14 gene abnormalities and inactivation were infrequent , suggesting a difference in carcinogenesis between PCNSL and systemic lymphoma .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "systemic lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: PATIENTS AND METHODS : Skin biopsy samples of 31 patients with a PCLBCL classified as either primary cutaneous follicle center lymphoma ( PCFCL ; n = 19 ) or PCLBCL , leg type ( n = 12 ) , according to the WHO-European Organisation for Research and Treatment of Cancer ( EORTC ) classification , were investigated using array-based comparative genomic hybridization , fluorescence in situ hybridization ( FISH ) , and examination of promoter hypermethylation .

## Item biored:test:264
Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "cholinesterase", "type": "GeneOrGeneProduct"}, {"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Therefore , these results demonstrate the effectiveness of crocin ( 30 mg/kg ) in antagonizing the cognitive deficits caused by STZ-icv in rats and its potential in the treatment of neurodegenerative diseases such as Alzheimer 's disease .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STZ-icv", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "neurodegenerative diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : It was found out that crocin ( 30 mg/kg ) -treated STZ-injected rats show higher correct choices and lower errors in Y-maze than vehicle-treated STZ-injected rats .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "STZ-injected", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have investigated the effects of continuous daily oral galactose ( 200 mg/kg/day ) treatment on cognitive deficits in streptozotocin-induced ( STZ-icv ) rat model of sAD , tested by Morris Water Maze and Passive Avoidance test , respectively .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin-induced", "type": "ChemicalEntity"}, {"text": "STZ-icv", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "sAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The extent of memory improvement evoked by DCE was 23 % at the dose of 200 mg/kg and 35 % at the dose of 400 mg/kg in young mice using elevated plus maze .

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Furthermore , DCE reversed the amnesia induced by scopolamine ( 0.4 mg/kg , i.p . )

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "scopolamine", "type": "ChemicalEntity"}]}

Input:
Sentence: Administration of daidzein ( 4.5 mg/kg body weight ) to mice was shown significantly to reverse scopolamine-induced amnesia , according to the results of a Y-maze test .

## Item biored:test:324
Example input:
Sentence: GENETIC ANALYSIS : Genomic DNA was extracted from peripheral blood leukocytes and mutation analysis of the entire coding sequence of the TSHR gene was performed in both children and their parents by direct DNA sequencing .

Example answer:
{"entities": [{"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we show that the candidate gene HIRA/Tuple1 mapping on the non-deleted TDR22 , in DGS/VCFS subjects presents a delayed replication timing .

Example answer:
{"entities": [{"text": "HIRA/Tuple1", "type": "GeneOrGeneProduct"}, {"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The Typically Deleted Region in the 22q11.21 subband ( here called TDR22 ) is very gene-dense , and the extent of the deletion has been defined precisely in several studies .

Example answer:
{"entities": []}

Example input:
Sentence: A 28 bp variable number of tandem repeats ( VNTR ) , a G/C single nucleotide polymorphism ( SNP ) , and a deletion of 6 bp at position 1494 were studied .

Example answer:
{"entities": [{"text": "28 bp variable number of tandem repeats", "type": "SequenceVariant"}, {"text": "G/C", "type": "SequenceVariant"}, {"text": "deletion of 6 bp at position 1494", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: Analysis of the sequences surrounding the microdeletion breakpoints revealed either intrinsic repetitivity of the deleted region or short direct repeats adjacent to the breakpoint junctions .

Example answer:
{"entities": []}

Input:
Sentence: Sequence analysis of the deleted regions revealed the presence of direct repeats of homologous sequences .

## Item biored:test:266
Example input:
Sentence: In addition , crocin in the mentioned dose could significantly attenuated learning and memory impairment in treated STZ-injected group in passive avoidance test .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "learning and memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STZ-injected", "type": "ChemicalEntity"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , we demonstrate that mice genetically engineered to have unilateral brain DA deficits develop METH-induced dopaminergic deficits that are of comparable magnitude on both sides of the brain .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "dopaminergic deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The extent of memory improvement evoked by DCE was 23 % at the dose of 200 mg/kg and 35 % at the dose of 400 mg/kg in young mice using elevated plus maze .

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : STZ administration and castration markedly decreased both STL1 ( the short memory ) and STL2 ( the long memory ) in passive avoidance tests .

Example answer:
{"entities": [{"text": "STZ", "type": "ChemicalEntity"}, {"text": "STL1", "type": "GeneOrGeneProduct"}, {"text": "STL2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: By way of contrast , mice treated with daidzein prior to the scopolamine injections were noticeably protected from this performance impairment ( an approximately 12 % -21 % decrease in alternation behavior ) .

## Item biored:test:292
Example input:
Sentence: CONCLUSIONS : Our data suggest that in a model representative of human retinopathy of prematurity , NOX4 was increased at a time point when IVNV developed .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Altogether , our results suggest that NOX4 may regulate VEGFR2-mediated IVNV through activated STAT3 .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2-mediated", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Knockdown of either NOX4 or STAT3 inhibited VEGF-induced EC proliferation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thymus weight was used as a marker of glucocorticoid activity .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thymus weight was used as a marker of glucocorticoid activity , and serum urate to assess XO inhibition .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "urate", "type": "ChemicalEntity"}, {"text": "XO", "type": "ChemicalEntity"}]}

Input:
Sentence: Atorva affected neither plasma NOx nor thymus weight .

## Item biored:test:275
Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Socs2 , plus five additional targets , further proved to comprise new EPOR/Jak2/Stat5 response genes ( which are important for erythropoiesis during anemia ) .

Example answer:
{"entities": [{"text": "Socs2", "type": "GeneOrGeneProduct"}, {"text": "EPOR/Jak2/Stat5", "type": "GeneOrGeneProduct"}, {"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , antithrombin treatment markedly suppressed puromycin aminonucleoside-induced apoptosis of renal tubular epithelial cells .

Example answer:
{"entities": [{"text": "antithrombin", "type": "ChemicalEntity"}, {"text": "puromycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations leading to abrogation of matriptase-2 proteolytic activity in humans are associated with an iron-refractory iron deficiency anemia ( IRIDA ) due to elevated hepcidin levels .

Example answer:
{"entities": [{"text": "matriptase-2", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "iron-refractory iron deficiency anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IRIDA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepcidin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alternatively , anemia could result from accelerated suicidal erythrocyte death or eryptosis , which is characterized by exposure of phosphatidylserine ( PS ) at the erythrocyte surface and by cell shrinkage .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "phosphatidylserine", "type": "ChemicalEntity"}, {"text": "PS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Erythropoietin does not activate erythropoietin receptor signaling or lipolytic pathways in human subcutaneous white adipose tissue in vivo .

Example answer:
{"entities": [{"text": "Erythropoietin", "type": "GeneOrGeneProduct"}, {"text": "erythropoietin receptor", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Data were obtained from two clinical trials : 1 ) acute Epo exposure ( rHuEpo , 400 IU/kg ) followed by WAT biopsies after 1 h and 2 ) 10 weeks treatment with the erythropoiesis-stimulating agent ( ESA ) Darbepoietin-alpha .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "erythropoiesis-stimulating agent", "type": "ChemicalEntity"}, {"text": "ESA", "type": "ChemicalEntity"}, {"text": "Darbepoietin-alpha", "type": "ChemicalEntity"}]}

Input:
Sentence: Recombinant human erythropoietin has been used to manage ribavirin-associated anemia but has other potential disadvantages .

## Item biored:test:265
Example input:
Sentence: In addition , we demonstrate that mice genetically engineered to have unilateral brain DA deficits develop METH-induced dopaminergic deficits that are of comparable magnitude on both sides of the brain .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "dopaminergic deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Intracerebroventricular injection of U-II also caused an increase in : food intake at doses of 100 and 1,000 ng/mouse , water intake at doses of 100-10,000 ng/mouse , and horizontal locomotion activity at a dose of 10,000 ng/mouse .

Example answer:
{"entities": [{"text": "U-II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : STZ administration and castration markedly decreased both STL1 ( the short memory ) and STL2 ( the long memory ) in passive avoidance tests .

Example answer:
{"entities": [{"text": "STZ", "type": "ChemicalEntity"}, {"text": "STL1", "type": "GeneOrGeneProduct"}, {"text": "STL2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The extent of memory improvement evoked by DCE was 23 % at the dose of 200 mg/kg and 35 % at the dose of 400 mg/kg in young mice using elevated plus maze .

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Similarly , significant improvements in memory scores were observed using passive avoidance apparatus and aged mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The results showed a significant increase in escape latencies and traveled distances to find platform in scopolamine-treated group as compared to saline group .

Example answer:
{"entities": [{"text": "scopolamine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : It was found out that crocin ( 30 mg/kg ) -treated STZ-injected rats show higher correct choices and lower errors in Y-maze than vehicle-treated STZ-injected rats .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "STZ-injected", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Injections of scopolamine into mice resulted in impaired performance on Y-maze tests ( a 37 % decreases in alternation behavior ) .

## Item biored:test:331
Example input:
Sentence: PBMCs from homozygotes and wild-type controls were stimulated with anti-CD3/anti-CD28 antibodies and the level of T-cell activation was determined by the stimulation index .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mutations were confirmed by screening at least 100 unrelated normal control subjects .

Example answer:
{"entities": []}

Example input:
Sentence: PCR products were screened by the method of single-strand conformation polymorphism followed by sequencing .

Example answer:
{"entities": []}

Example input:
Sentence: After PCR amplification , samples were run on an ABI PRISM 310 genetic analyzer for LOH , deletion detection , and haplotype generation .

Example answer:
{"entities": []}

Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Control was defined as MSDBP < 90 mm Hg compared with baseline .

Example answer:
{"entities": []}

Example input:
Sentence: Control ( saline P20 ) rats acquired both discriminations immediately .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Optimal control of the absences was achieved with sodium valproate , lamotrigine , or ethosuximide alone or in combination .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "ChemicalEntity"}, {"text": "lamotrigine", "type": "ChemicalEntity"}, {"text": "ethosuximide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Controls were only screened using denaturing high-performance liquid chromatography and gel electrophoresis .

## Item biored:test:274
Example input:
Sentence: Conversion to SRL prevented CsA-induced renal damage evolution ( absent/mild grade lesions ) , while NGAL ( serum versus urine ) seems to be a feasible biomarker of CsA replacement to SRL .

Example answer:
{"entities": [{"text": "SRL", "type": "ChemicalEntity"}, {"text": "CsA-induced", "type": "ChemicalEntity"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NGAL", "type": "GeneOrGeneProduct"}, {"text": "CsA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-containing", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: This retrospective study investigated the combination of bort ( 1.3 mg/m ( 2 ) on days 1 , 4 , 8 , and 11 every 3 weeks ) and dex ( 20 mg on the day of and the day after bort ) as salvage treatment in 85 patients with R/R MM after prior autologous stem cell transplantation or conventional chemotherapy .

Example answer:
{"entities": [{"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Meta-analysis of the two trials demonstrated a significant overall reduction in the composite end point in Hp 2-2 DM individuals with vitamin E ( odds ratio : 0.58 ; 95 % CI : 0.40-0.86 ; p = 0.006 ) .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rapid reversal of anticoagulation reduces hemorrhage volume in a mouse model of warfarin-associated intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "warfarin-associated", "type": "ChemicalEntity"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using a mouse model , we tested whether the rapid reversal of anticoagulation using human prothrombin complex concentrate ( PCC ) can reduce hemorrhagic blood volume .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "prothrombin complex concentrate", "type": "ChemicalEntity"}, {"text": "PCC", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Input:
Sentence: Although ribavirin-associated anemia can be reversed by dose reduction or discontinuation , this approach compromises outcomes by significantly decreasing SVR rates .

## Item biored:test:282
Example input:
Sentence: The intracellular Leu concentration was increased in septic muscle , compared to basal control conditions , and oral Leu further increased the intracellular Leu concentration similarly in both control and septic rats .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ritanserin-treated rats ( 4 microg/0.5 microl/side ) showed a significant decrease in the mentioned parameters as compared to DMSO-treated group .

Example answer:
{"entities": [{"text": "Ritanserin-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "DMSO-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Plasma and liver 15-F ( 2t ) -IsoP were elevated and reached a plateau after day 2 of VPA treatment compared to control .

Example answer:
{"entities": [{"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the current study , we investigated whether a physiological intervention by feeding 40 % high fat diet ( HFD ) , which induces obesity in male Sprague-Dawley rats ( 250-275 g ) , sensitizes to doxorubicin-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "fat", "type": "ChemicalEntity"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Input:
Sentence: LV hypertrophy induced by Iso treatment was significantly higher in TGR than in SD rats ( in g LV wt/100 g body wt , 0.28 +/- 0.004 vs. 0.24 +/- 0.004 , respectively ) .

## Item biored:test:332
Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutations were confirmed by screening at least 100 unrelated normal control subjects .

Example answer:
{"entities": []}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Direct sequencing was used for mutation analysis .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Input:
Sentence: Confirmation of mutations identified was obtained by DNA sequencing .

## Item biored:test:256
Example input:
Sentence: Recent data highlight the presence , in HIV-1-seropositive patients with lymphoma , of p17 variants ( vp17s ) endowed with B-cell clonogenicity , suggesting a role of vp17s in lymphomagenesis .

Example answer:
{"entities": [{"text": "HIV-1-seropositive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "lymphomagenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the original MB-DRM German family , we demonstrated a linkage of the disease to the SEPN1 locus ( 1p36 ) , and subsequently a homozygous SEPN1 deletion ( del 92 nucleotide -19/+73 ) in the affected patients .

Example answer:
{"entities": [{"text": "SEPN1", "type": "GeneOrGeneProduct"}, {"text": "del 92 nucleotide -19/+73", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Carriers of TBX21 promoter SNP rs17250932 and HLX1 promoter SNP rs2738751 showed reduced or trendwise reduced ( p < 0.07 ) IL-5 , IL-13 and TNF-a secretion after LpA-stimulation .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "rs17250932", "type": "SequenceVariant"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: n = 15 ) after methylating chemotherapy for Hodgkin lymphoma compared to patients without previous methylating exposure ( t-AML , 30.4 % , n = 69 ; breast cancer patients , 27.2 % , n = 22 ) .

Example answer:
{"entities": [{"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our observation of frequent p14 gene abnormalities ( 90 % ) and inactivation ( 40-60 % ) was in striking contrast to the same pathological subtype of systemic lymphoma in which p14 gene abnormalities and inactivation were infrequent , suggesting a difference in carcinogenesis between PCNSL and systemic lymphoma .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "systemic lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Seven of seven PCLBCL , leg type , patients with deletion of 9p21.3 and/or complete methylation of CDKN2A died as a result of their lymphoma .

## Item biored:test:262
Example input:
Sentence: BACKGROUND : The involvement of water-soluble carotenoids , crocins , as the main and active components of Crocus sativus L. extract in learning and memory processes has been proposed .

Example answer:
{"entities": [{"text": "carotenoids", "type": "ChemicalEntity"}, {"text": "crocins", "type": "ChemicalEntity"}, {"text": "Crocus sativus L. extract", "type": "ChemicalEntity"}]}

Example input:
Sentence: Daucus carota extract ( 200 , 400 mg/kg , p.o . )

Example answer:
{"entities": [{"text": "Daucus carota extract", "type": "ChemicalEntity"}]}

Example input:
Sentence: Salidroside ( Sal ) is an active ingredient that is isolated from Rhodiola rosea , which has been reported to have anti-inflammatory activities and a renal protective effect .

Example answer:
{"entities": [{"text": "Salidroside", "type": "ChemicalEntity"}, {"text": "Sal", "type": "ChemicalEntity"}, {"text": "Rhodiola rosea", "type": "OrganismTaxon"}]}

Example input:
Sentence: The current study dealt with the protective role of mangiferin , a polyphenol from Mangifera indica Linn .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "polyphenol", "type": "ChemicalEntity"}, {"text": "Mangifera indica Linn", "type": "OrganismTaxon"}]}

Example input:
Sentence: Garcinielliptone FC ( GFC ) isolated from hexanic fraction seed extract of species Platonia insignis Mart .

Example answer:
{"entities": [{"text": "Garcinielliptone FC", "type": "ChemicalEntity"}, {"text": "GFC", "type": "ChemicalEntity"}, {"text": "Platonia insignis Mart", "type": "OrganismTaxon"}]}

Example input:
Sentence: N-acylimidazole derivative of etodolac ( EAI ) , was condensed with the polysaccharide polymer dextran of different molecular weights ( 40000 , 60000 , 110000 and 200000 ) .

Example answer:
{"entities": [{"text": "N-acylimidazole", "type": "ChemicalEntity"}, {"text": "etodolac", "type": "ChemicalEntity"}, {"text": "EAI", "type": "ChemicalEntity"}, {"text": "dextran", "type": "ChemicalEntity"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: Instead , oral administration of S-1 ( a derivative of 5-FU ) , at 200 mg/day twice a week , was instituted , because S-1 has a strong inhibitory effect on dihydropyrimidine dehydrogenase , which catalyzes the degradative of 5-FU into FBAL .

Example answer:
{"entities": [{"text": "S-1", "type": "ChemicalEntity"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "dihydropyrimidine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Curcumin is the active component of tumeric , and this polyphenolic compound has been extensively investigated as an anticancer drug that modulates multiple pathways and genes .

Example answer:
{"entities": [{"text": "Curcumin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The ethanolic extract of Daucus carota seeds ( DCE ) was administered orally in three doses ( 100 , 200 , 400 mg/kg ) for seven successive days to different groups of young and aged mice .

Example answer:
{"entities": [{"text": "extract of Daucus carota seeds", "type": "ChemicalEntity"}, {"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Via the sequential isolation of Pueraria thunbergiana , the active component was ultimately identified as daidzein ( 4',7-dihydroxy-isoflavone ) .

## Item biored:test:270
Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-containing", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It has shown promising results alone or in combination with other chemotherapeutic agents in colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers .

Example answer:
{"entities": [{"text": "colorectal , breast , pancreaticobiliary , gastric , renal cell and head and neck cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "ChemicalEntity"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV and HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most common regimens were 3TC + d4T + nevirapine ( NVP ) ( 54.8 % ) , zidovudine ( AZT ) + 3TC + NVP ( 14.5 % ) , 3TC + d4T + efavirenz ( EFV ) ( 20.1 % ) , and AZT + 3TC + EFV ( 5.4 % ) .

Example answer:
{"entities": [{"text": "3TC", "type": "ChemicalEntity"}, {"text": "d4T", "type": "ChemicalEntity"}, {"text": "nevirapine", "type": "ChemicalEntity"}, {"text": "NVP", "type": "ChemicalEntity"}, {"text": "zidovudine", "type": "ChemicalEntity"}, {"text": "AZT", "type": "ChemicalEntity"}, {"text": "efavirenz", "type": "ChemicalEntity"}, {"text": "EFV", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Input:
Sentence: The current best treatment for HCV infection is combination therapy with pegylated interferon and ribavirin .

## Item biored:test:308
Example input:
Sentence: Upon pretreatment with mangiferin ( 100 mg/kg body weight suspended in 2 ml of dimethyl sulphoxide ) given intraperitoneally for 28 days to MI rats protected the above-mentioned parameters to fall from the normal levels .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "dimethyl sulphoxide", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male CD-1 mice were treated with warfarin ( 2 mg/kg over 24 h ) , resulting in a mean ( +/-s.d . )

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Sprague-Dawley rats were injected with saline on postnatal day ( P ) 20 , or a convulsant dose of pilocarpine on P20 or P45 .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: At puberty ( P40 ) , half the PCPA-treated rats and half the saline-treated rats began treatment with testosterone ( T , 5 mg/kg , 5 days/week ) .

Example answer:
{"entities": [{"text": "PCPA-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Input:
Sentence: Male rats were treated with MA ( 10 mg/kg , every 2 h for four injections ) .

## Item biored:test:259
Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "ChemicalEntity"}, {"text": "scopolamine-", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Testosterone ameliorates streptozotocin-induced memory impairment in male rats .

Example answer:
{"entities": [{"text": "Testosterone", "type": "ChemicalEntity"}, {"text": "streptozotocin-induced", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The extent of memory improvement evoked by DCE was 23 % at the dose of 200 mg/kg and 35 % at the dose of 400 mg/kg in young mice using elevated plus maze .

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , DCE reversed the amnesia induced by scopolamine ( 0.4 mg/kg , i.p . )

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "scopolamine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Daidzein activates choline acetyltransferase from MC-IXC cells and improves drug-induced amnesia .

## Item biored:test:277
Example input:
Sentence: Isoproterenol ( 100mg/kg ) was injected subcutaneously on the 13th and 14th days to induce acute myocardial infarction .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "acute myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Severe alterations in the structural integrity of the sarcolemma of cardiomyocytes have been demonstrated to be caused by isoproterenol .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The mechanism of isoproterenol-induced myocardial damage is unknown , but a mismatch of oxygen supply vs. demand following coronary hypotension and myocardial hyperactivity is the best explanation for the complex morphological alterations observed .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial hyperactivity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol induces primary loss of dystrophin in rat hearts : correlation with myocardial injury .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Enhanced isoproterenol-induced cardiac hypertrophy in transgenic rats with low brain angiotensinogen .
