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

## Item biored:test:664
Example input:
Sentence: However , intraspinal injection of 5,7-DHT to produce a more selective lesion of only descending serotonin projections in the spinal cord did not affect this hypotension .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The serotonin 2C receptor ( 5-HT ( 2C ) ) plays a key role in control of appetite and satiety .

Example answer:
{"entities": [{"text": "serotonin 2C receptor", "type": "GeneOrGeneProduct"}, {"text": "5-HT ( 2C )", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The antidepressant trazodone is a 5-HT 2A/2C receptor antagonist .

Example answer:
{"entities": [{"text": "trazodone", "type": "ChemicalEntity"}, {"text": "5-HT 2A/2C receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: Effects of the antidepressant trazodone , a 5-HT 2A/2C receptor antagonist , on dopamine-dependent behaviors in rats .

Example answer:
{"entities": [{"text": "trazodone", "type": "ChemicalEntity"}, {"text": "5-HT 2A/2C receptor", "type": "GeneOrGeneProduct"}, {"text": "dopamine-dependent", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: RATIONALE : 5-Hydroxytryptamine , via stimulation of 5-HT 2C receptors , exerts a tonic inhibitory influence on dopaminergic neurotransmission , whereas activation of 5-HT 2A receptors enhances stimulated DAergic neurotransmission .

Example answer:
{"entities": [{"text": "5-Hydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5-HT 2C receptors", "type": "GeneOrGeneProduct"}, {"text": "5-HT 2A receptors", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Antagonists at serotonin type 6 ( 5-HT ( 6 ) ) receptors show activity in models of learning and memory .

Example answer:
{"entities": [{"text": "serotonin type 6 ( 5-HT ( 6 ) ) receptors", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "5-HT6 receptor", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "serotonergic", "type": "ChemicalEntity"}, {"text": "memory deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Input:
Sentence: The serotonin 6 ( 5-HT6 ) receptor is therapeutically targeted by several second generation antipsychotics , such as clozapine and olanzapine , and d-amphetamine-induced hyperactivity in rats is corrected with the use of a selective 5-HT6 receptor antagonist .

## Item biored:test:723
Example input:
Sentence: The antibody reacted with the 80 kDa band protein in control fibroblasts , while no bands were detected in the fibroblasts from a patient with ALD ( # 163 ) , in which mRNA of the ALD gene was undetectable based on Northern blot analysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "ALD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the carbohydrate sulfotransferase gene ( CHST6 ) for a Chinese family with macular corneal dystrophy ( MCD ) and to investigate the histopathological changes in the affected cornea .

Example answer:
{"entities": [{"text": "carbohydrate sulfotransferase gene", "type": "GeneOrGeneProduct"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "macular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Her cells accumulated lipid-linked oligosaccharides lacking three glucose residues , and sequencing of the ALG6 gene showed what initially appeared to be a homozygous novel point mutation ( 338G > A ) .

Example answer:
{"entities": [{"text": "lipid-linked oligosaccharides", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "ALG6", "type": "GeneOrGeneProduct"}, {"text": "338G > A", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: We report on a new allele at the arylsulfatase A ( ARSA ) locus causing late-onset metachromatic leukodystrophy ( MLD ) .

Example answer:
{"entities": [{"text": "arylsulfatase A", "type": "GeneOrGeneProduct"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "metachromatic leukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A 24-year-old SLS female was homozygous for a 352-kb deletion involving ALDH3A2 and 4 contiguous genes including ALDH3A1 , which codes for the major soluble protein in cornea .

## Item biored:test:747
Example input:
Sentence: Novel compound heterozygous mutation of MLYCD in a Chinese patient with malonic aciduria .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "malonic aciduria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The D487_S488_F489 deletion had been identified in two previously genotyped Chinese families .

Example answer:
{"entities": [{"text": "D487_S488_F489 deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We previously reported that mutations of transmembrane channel-like gene 1 ( TMC1 ) cause non-syndromic recessive deafness at the DFNB7/B11 locus on chromosome 9q13-q21 in nine Pakistani families .

Example answer:
{"entities": [{"text": "transmembrane channel-like gene 1", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "non-syndromic recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We identified 10 new families segregating DFNB7/B11 deafness and TMC1 mutations , including three novel alleles .

Example answer:
{"entities": [{"text": "DFNB7/B11 deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Identification of a novel FBN1 gene mutation in a Chinese family with Marfan syndrome .

## Item biored:test:711
Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further analyses of C. elegans RAB-28 , recently associated with autosomal-recessive cone-rod dystrophy , reveal that this small GTPase is exclusively expressed in ciliated neurons where it dynamically associates with IFT trains .

Example answer:
{"entities": [{"text": "C. elegans", "type": "OrganismTaxon"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "cone-rod dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We therefore performed a mutation analysis of the GUCA1B gene in a clinically well characterized group of patients of European and North-American geographical origin with autosomal dominantly inherited cone dystrophy and cone rod dystrophy .

## Item biored:test:727
Example input:
Sentence: RESULTS : Women with a deletion allele had a significantly greater risk of preterm delivery [ adjusted odds ratio ( AOR ) : 3.0 ; 95 % CI : 1.0 , 8.8 ; P < 0.05 ] than did those without a deletion allele .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA samples of 760 anonymous AJ subjects were submitted for analysis , subsequently detecting six individuals heterozygous for the GALT deletion mutation , giving a carrier frequency of 1 in 127 ( 0.79 % ) .

Example answer:
{"entities": [{"text": "GALT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The compound heterozygous mutations , c.892C > T and c.1072T > C , were identified in exon 3 of CHST6 in three patients .

Example answer:
{"entities": [{"text": "c.892C > T", "type": "SequenceVariant"}, {"text": "c.1072T > C", "type": "SequenceVariant"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: Seven hundred fifty three subjects , corresponding to 251 full trios of childhood-onset SLE families , were genotyped and analyzed using transmission disequilibrium testing ( TDT ) and multitest corrections .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings extend the body of evidence for compound heterozygous mutations leading to HS-RDEB and provide the basis for prenatal diagnosis in this family .

Example answer:
{"entities": [{"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One possibility might be that individuals who are compound heterozygotes for ATM mutations are more common than we realize ..

Example answer:
{"entities": [{"text": "ATM", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Geneticists should consider the possibility of compound heterozygosity for large deletions in patients with SLS and other inborn errors of metabolism , which has implications for carrier testing and prenatal diagnosis .

## Item biored:test:709
Example input:
Sentence: TGFBI gene mutations causing lattice and granular corneal dystrophies in Indian patients .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "lattice and granular corneal dystrophies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The relationship between microcoria , glaucoma , and the MYOC Q48H mutation in this family is discussed .

Example answer:
{"entities": [{"text": "microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "Q48H", "type": "SequenceVariant"}]}

Example input:
Sentence: Data presented here supports the hypothesis that congenital microcoria is a potential risk factor for glaucoma , although this observation is complicated by the partial segregation of MYOC Q48H ( 1q24.3-q25.2 ) , a mutation known to be associated with glaucoma in India .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "Q48H", "type": "SequenceVariant"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the carbohydrate sulfotransferase gene ( CHST6 ) for a Chinese family with macular corneal dystrophy ( MCD ) and to investigate the histopathological changes in the affected cornea .

Example answer:
{"entities": [{"text": "carbohydrate sulfotransferase gene", "type": "GeneOrGeneProduct"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "macular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Macular corneal dystrophy in a Chinese family related with novel mutations of CHST6 .

Example answer:
{"entities": [{"text": "Macular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Background : Heterozygous mutations in GUCA1A ( MIM # 600364 ) have been identified to cause autosomal dominantly inherited cone dystrophy , cone rod dystrophy and macular dystrophy .

## Item biored:test:735
Example input:
Sentence: 5-Aza-2'-deoxy-cytidine and/or Trichostatin A treatments induced DOCK8 expression in lung cancer cell lines with reduced DOCK8 expression .

Example answer:
{"entities": [{"text": "5-Aza-2'-deoxy-cytidine", "type": "ChemicalEntity"}, {"text": "Trichostatin A", "type": "ChemicalEntity"}, {"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Aberrant expression of UCHL1 in pediatric high-grade gliomas may promote cell invasion , transformation , and self-renewal properties , at least in part , by modulating Wnt/Beta catenin activity .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Wnt/Beta catenin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A g-secretase inhibitor , DAPT , selectively depleted CD133 ( + ) cells , suppressed N1ICD and SKP2 , induced p27Kip1 , inhibited ACC growthin vivo , and sensitized CD133 ( + ) cells to radiation .

Example answer:
{"entities": [{"text": "g-secretase", "type": "GeneOrGeneProduct"}, {"text": "DAPT", "type": "ChemicalEntity"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "SKP2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: UCHL1 might act as an oncogene in glioma within the gene network that imparts stem-like characteristics to these cancer cells .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) is associated with stem-like cancer cell functions in pediatric high-grade glioma .

Example answer:
{"entities": [{"text": "Ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work we used SF188 and SJ-GBM2 cell lines to study the function of the ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) , a deubiquitinase de-regulated in several cancers , in pediatric high-grade gliomas .

Example answer:
{"entities": [{"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We identified in ACC CD133-positive CSC that expressed NOTCH1 and SOX10 , formed spheroids , and initiated tumors in nude mice .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133-positive", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Input:
Sentence: Compared with spheroid-forming U87-DACH1-low cells , adherent U87-DACH1-high cells display lower tumorigenicity , indicating DACH1 decreases the number of tumor-initiating cells .

## Item biored:test:717
Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Arg124Cys and Arg555Trp appear to be the predominant mutations causing LCD and GCD , respectively , in the population studied .

Example answer:
{"entities": [{"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , eight individuals who had both microcoria and glaucoma were screened for glaucoma genes : myocilin ( MYOC ) , optineurin ( OPTN ) and CYP1B1 .

Example answer:
{"entities": [{"text": "microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocilin", "type": "GeneOrGeneProduct"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "optineurin", "type": "GeneOrGeneProduct"}, {"text": "OPTN", "type": "GeneOrGeneProduct"}, {"text": "CYP1B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TGFBI gene mutations causing lattice and granular corneal dystrophies in Indian patients .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "lattice and granular corneal dystrophies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Data presented here supports the hypothesis that congenital microcoria is a potential risk factor for glaucoma , although this observation is complicated by the partial segregation of MYOC Q48H ( 1q24.3-q25.2 ) , a mutation known to be associated with glaucoma in India .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "Q48H", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Conclusion : The absence of clearly pathogenic mutations in the selected patient group suggests that the GUCA1B gene is a minor cause for retinal degenerations in Europeans or North-Americans .

## Item biored:test:683
Example input:
Sentence: The 1858T risk allele occurred on only a single haplotype that was strongly associated with type 1 diabetes ( P = 7.9 x 10 ( -5 ) ) .

Example answer:
{"entities": [{"text": "1858T", "type": "SequenceVariant"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A multiple logistic regression analysis indicated that the odds ratio for EH in the -395A allele carriers as compared with the control group was 0.593 ( P=0.024 ) after adjusting for current traditional risk factors .

Example answer:
{"entities": [{"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-395A", "type": "SequenceVariant"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Our results indicate that the PSA/ARE GG genotype confers an increased risk of PC especially among younger men .

Example answer:
{"entities": [{"text": "PSA/ARE", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs25531 and the haplotype 5-HTTLPR/rs25531 did not associate with risk of PD .

Example answer:
{"entities": [{"text": "rs25531", "type": "SequenceVariant"}, {"text": "5-HTTLPR/rs25531", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found that the presence of the -1021T allele was associated with AD : odds ratio = 1.2 ( 95 % confidence interval : 1.06-1.4 , p = 0.005 ) .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The p.A1369S variant was associated with a significantly lower risk of type 2 diabetes ( odds ratio [ OR ] 0.93 ; 95 % CI 0.91 , 0.95 ; P = 1.2 x 10 ( -11 ) ) .

Example answer:
{"entities": [{"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In a multivariate logistic regression analysis including age , sex , smoking , diabetes , arterial hypertension and hypercholesterolemia , the FGG 10034 T variant was not significantly associated with the presence of PAD ( Odds ratio 1.07 , 95 % confidence interval 0.84 - 1.37 ; p = 0.60 ) .

## Item biored:test:725
Example input:
Sentence: Her cells accumulated lipid-linked oligosaccharides lacking three glucose residues , and sequencing of the ALG6 gene showed what initially appeared to be a homozygous novel point mutation ( 338G > A ) .

Example answer:
{"entities": [{"text": "lipid-linked oligosaccharides", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "ALG6", "type": "GeneOrGeneProduct"}, {"text": "338G > A", "type": "SequenceVariant"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A detailed analysis of the DNA breakpoints in the two genes , previously characterized by other groups , validated the observation that Alu-mediated unequal recombination is the main type of deletion in MSH2 ( n=34 ) , but not in MLH1 ( n=21 ) ( P < 0.0001 ) .

Example answer:
{"entities": [{"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Novel compound heterozygous mutation of MLYCD in a Chinese patient with malonic aciduria .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "malonic aciduria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Her mother was heterozygous for the Asn45Ser mutation , and her father , for the nine-nucleotide deletion .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: The patient was a compound heterozygote for SRD5A2 mutations , carrying 2 mutations in exon 4 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The other 19-month-old female patient was a compound heterozygote for a 1.44-Mb contiguous gene deletion and a missense mutation ( c.407C > T , P136L ) in ALDH3A2 .

## Item biored:test:669
Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: Results of this analysis indicated that there is a strong finding of -120 bp duplication allele frequencies with schizophrenia ( p=0.008 ) and weak finding with -1240 L/S and for paranoid schizophrenia ( p=0.022 ) .

Example answer:
{"entities": [{"text": "-120 bp duplication", "type": "SequenceVariant"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-1240 L/S", "type": "SequenceVariant"}, {"text": "paranoid schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a genotype test , we found a trend to point-wise association ( P = 0.053 ) of the G472A SNP in Hispanic subjects with opiate addiction .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neither rs2230912 nor any of 8 other SNPs genotyped across P2RX7 was found to be associated with mood disorder in general , nor specifically with bipolar or unipolar disorder .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar or unipolar disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We genotyped 1498 German subjects for SNPs rs6232 and rs6235 within PCSK1 .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "PCSK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Among these three SNPs , neither SNP4 , SNP7 , SNP18 has shown significant association with schizophrenia in single locus association analysis , nor any compositions of the three SNP haplotypes has shown significantly associations with the DSM-IV diagnosed schizophrenia .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , these three SNP markers were genotyped in 218 schizophrenia pedigrees of Taiwan ( 864 individuals ) for association analysis .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHOD : Using five tagging SNPs ( rs6693503 , rs1805054 , rs4912138 , rs3790757 and rs9659997 ) , we conducted a genetic association analysis of case-control samples ( 197 METH-induced psychosis patients and 337 controls ) in the Japanese population .

## Item biored:test:743
Example input:
Sentence: One is the Lys198Asn polymorphism , which showed a positive association with BP in overweight people .

Example answer:
{"entities": [{"text": "Lys198Asn", "type": "SequenceVariant"}, {"text": "overweight", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The level of the 137-bp PCR product containing the insertion was lowest in two patients who showed a later onset of cerebellar ataxia .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cerebellar ataxia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: His apoE phenotype was apoE3/2 and he had mild dyslipidemia with a mid-band on polyacrylamide gel electrophoresis .

Example answer:
{"entities": [{"text": "apoE", "type": "GeneOrGeneProduct"}, {"text": "apoE3/2", "type": "GeneOrGeneProduct"}, {"text": "dyslipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyacrylamide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In pooled follow-up data for 768 antithrombotic users , presence of MB at baseline was associated with a substantially increased risk of subsequent ICH ( OR , 12.1 ; 95 % CI , 3.4-42.5 ; P < 0.001 ) .

Example answer:
{"entities": [{"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel apolipoprotein E mutation , ApoE Osaka ( Arg158 Pro ) , in a dyslipidemic patient with lipoprotein glomerulopathy .

Example answer:
{"entities": [{"text": "apolipoprotein E", "type": "GeneOrGeneProduct"}, {"text": "ApoE", "type": "GeneOrGeneProduct"}, {"text": "Arg158 Pro", "type": "SequenceVariant"}, {"text": "dyslipidemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "lipoprotein glomerulopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A significant association was noted between higher levels of apoB-100 ( P = 1.1 10 ( -3 ) ) and LDL cholesterol ( P = 0.02 ) and the subjects having Arg70 .

## Item biored:test:715
Example input:
Sentence: The C139T mutation , predicted to result in the substitution of an arginine by a tryptophan ( R47W ) in the N-terminal subdomain , affected conserved residues in the PAX9 paired domain .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "arginine by a tryptophan", "type": "SequenceVariant"}, {"text": "R47W", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sequence analysis of aggrecan complementary DNA from an affected individual revealed homozygosity for a missense mutation ( c.6799G -- > A ) that predicts a p.D2267N amino acid substitution in the C-type lectin domain within the G3 domain of aggrecan .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "c.6799G -- > A", "type": "SequenceVariant"}, {"text": "p.D2267N", "type": "SequenceVariant"}]}

Example input:
Sentence: ApoE gene analysis showed a nucleotide substitution of G to C at codon 158 of exon 4 .

Example answer:
{"entities": [{"text": "ApoE", "type": "GeneOrGeneProduct"}, {"text": "G to C at codon 158", "type": "SequenceVariant"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The genetic polymorphism rs1052133 , which leads to substitution of the amino acid at codon 326 from Ser to Cys , shows functional differences , namely a decrease in enzyme activity in hOGG1-Cys326 .

Example answer:
{"entities": [{"text": "rs1052133", "type": "SequenceVariant"}, {"text": "326 from Ser to Cys", "type": "SequenceVariant"}, {"text": "hOGG1-Cys326", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The polymorphism rs2234671 at position Ex2+860G > C of the CXCR1 gene causes a conservative amino acid substitution ( S276T ) .

Example answer:
{"entities": [{"text": "rs2234671", "type": "SequenceVariant"}, {"text": "Ex2+860G > C", "type": "SequenceVariant"}, {"text": "CXCR1", "type": "GeneOrGeneProduct"}, {"text": "S276T", "type": "SequenceVariant"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The sequence variant c.465G > T encodes a conservative amino acid substitution , p.Glu155Asp , located in EF-hand 4 , the calcium binding site of GCAP2 protein .

## Item biored:test:732
Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "MPTP-induced", "type": "ChemicalEntity"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In this work we used SF188 and SJ-GBM2 cell lines to study the function of the ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) , a deubiquitinase de-regulated in several cancers , in pediatric high-grade gliomas .

Example answer:
{"entities": [{"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using Western blot analysis and RT-PCR , we have demonstrated that TD induces HIF-1a expression and activity in primary mouse astrocytes .

Example answer:
{"entities": [{"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: PURPOSE : The anthracyclines daunorubicin and doxorubicin and the epipodophyllotoxin etoposide are potent DNA cleavage-enhancing drugs that are widely used in clinical oncology ; however , myelosuppression and cardiac toxicity limit their use .

Example answer:
{"entities": [{"text": "anthracyclines", "type": "ChemicalEntity"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "epipodophyllotoxin", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Example input:
Sentence: Flow cytometry experiments confirmed that the transfectants ' diminished resistance to DOX was caused by increased drug accumulation induced by the exogenous Rab6c .

Example answer:
{"entities": [{"text": "DOX", "type": "ChemicalEntity"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Input:
Sentence: We then generated U87TR-Da glioma cells , where DACH1 expression could be activated by exposure of the cells to doxycycline .

## Item biored:test:736
Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , AT2R gene and protein expressions in fetal kidneys were inhibited by PCE , associated with the repression of the gene expression of glial-cell-line-derived neurotrophic factor ( GDNF ) /tyrosine kinase receptor ( c-Ret ) signaling pathway .

Example answer:
{"entities": [{"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "glial-cell-line-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "GDNF", "type": "GeneOrGeneProduct"}, {"text": "kinase receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Ret", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Focused transcriptomics revealed that myocyte-specific enhancer factor 2C ( MEF2C ) and myogenic factor 5 ( MYF5 ) expression was inhibited by high glucose levels , and endoribonuclease-prepared small interfering RNA-mediated combined inhibition of those transcription factors phenocopied the glycolytic shift that was observed in high glucose conditions .

Example answer:
{"entities": [{"text": "myocyte-specific enhancer factor 2C", "type": "GeneOrGeneProduct"}, {"text": "MEF2C", "type": "GeneOrGeneProduct"}, {"text": "myogenic factor 5", "type": "GeneOrGeneProduct"}, {"text": "MYF5", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditionally deleting one copy of FGF receptor 2 ( FGFR2 ) in adult mouse airway basal cells results in self-renewal and differentiation phenotypes .

Example answer:
{"entities": [{"text": "FGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: In tissue samples with normal fibroblasts ( NFs ) serving as control samples , expression of TGF-beta1 and -beta2 was decreased when compared to keloid fibroblasts ( KFs ) , while expression of TGF-beta3 and of TGF-betaRII was significantly higher in NFs .

Example answer:
{"entities": [{"text": "TGF-beta1 and -beta2", "type": "GeneOrGeneProduct"}, {"text": "keloid", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-beta3", "type": "GeneOrGeneProduct"}, {"text": "TGF-betaRII", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse embryonic fibroblasts exhibiting disruption or overexpression of IGF-1R ( R- cells and R+ cells ) were used to examine the level of apoptosis , autophagy , and production of reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We show that FGFR2 signalling correlates with maintenance of expression of a key transcription factor for basal cell self-renewal and differentiation : SOX2 .

Example answer:
{"entities": [{"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "SOX2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Gene expression analysis and chromatin immunoprecipitation assay reveal that fibroblast growth factor 2 ( FGF2/bFGF ) is transcriptionally repressed by DACH1 , especially in cells cultured in serum-free medium .

## Item biored:test:734
Example input:
Sentence: CD11c+ cells induced by IL-3 or IL-3/CSF-1 were competent in cellular maturation and endocytosis .

Example answer:
{"entities": [{"text": "CD11c+", "type": "GeneOrGeneProduct"}, {"text": "IL-3", "type": "GeneOrGeneProduct"}, {"text": "IL-3/CSF-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The majority of CXCR5 ( + ) PD1 ( + ) CD4 ( + ) T follicular helper ( Tfh ) cells ( > 90 % ) are CD25 ( - ) Bcl6 ( hi ) , while a small subpopulation ( < 10 % ) are CD25 ( + ) Bcl6 ( low ) but do not express FoxP3 and are not T regulatory cells .

Example answer:
{"entities": [{"text": "CXCR5", "type": "GeneOrGeneProduct"}, {"text": "PD1", "type": "GeneOrGeneProduct"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "Bcl6", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Example input:
Sentence: A g-secretase inhibitor , DAPT , selectively depleted CD133 ( + ) cells , suppressed N1ICD and SKP2 , induced p27Kip1 , inhibited ACC growthin vivo , and sensitized CD133 ( + ) cells to radiation .

Example answer:
{"entities": [{"text": "g-secretase", "type": "GeneOrGeneProduct"}, {"text": "DAPT", "type": "ChemicalEntity"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "SKP2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found that sorted SUM159PT cell populations with high ADAM12 levels had elevated expression of CSC markers and an increased ability to form mammospheres .

Example answer:
{"entities": [{"text": "SUM159PT", "type": "CellLine"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These results establish in the majority of ACC the presence of a previously uncharacterized population of CD133 ( + ) cells with neural stem properties , which are driven by SOX10 , NOTCH1 , and FABP7 .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "FABP7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CD133 ( + ) ACC cells produced activated NOTCH1 ( N1ICD ) and generated CD133 ( - ) cells that expressed JAG1 as well as neural differentiation factors NR2F1 , NR2F2 , and p27Kip1 .

Example answer:
{"entities": [{"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "JAG1", "type": "GeneOrGeneProduct"}, {"text": "NR2F1", "type": "GeneOrGeneProduct"}, {"text": "NR2F2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : We identified in ACC CD133-positive CSC that expressed NOTCH1 and SOX10 , formed spheroids , and initiated tumors in nude mice .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133-positive", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: U87-DACH1-low cells form spheroids with CD133 and Nestin expression in serum-free medium but U87-DACH1-high cells do not .

## Item biored:test:646
Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In all clones with combined immune escape and LAM resistance mutations , the nucleotide analogues adefovir and tenofovir remained effective in suppressing viral replication in vitro .

Example answer:
{"entities": [{"text": "LAM", "type": "ChemicalEntity"}, {"text": "adefovir", "type": "ChemicalEntity"}, {"text": "tenofovir", "type": "ChemicalEntity"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: To the best of our knowledge , this constitutes the first report of HBV lamivudine-resistant strains in therapy-na ve HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-containing", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thirty-five lamivudine-na ve HBV infected patients with or without HIV co-infection were studied : 15 chronic HBV mono-infected patients and 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "HBV infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV mono-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus", "type": "OrganismTaxon"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "ChemicalEntity"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV and HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: This study analyzed the genotype distribution and frequency of lamivudine ( LAM ) and tenofovir ( TDF ) resistance mutations in a group of patients co-infected with HIV and hepatitis B virus ( HBV ) .

## Item biored:test:796
Example input:
Sentence: The current study aimed to assess the impact of MDMA use on three separate central executive processes ( set shifting , inhibition and memory updating ) and also on `` prefrontal '' mediated social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Compared with MDMA-free polydrug controls , MDMA polydrug users showed impairments in set shifting and memory updating , and also in social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA-free", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: For comparison of sleep architecture variables , 12 healthy comparison participants underwent a single night of experimental polysomnography that followed 1 night of accommodation polysomnography .

Example answer:
{"entities": []}

Example input:
Sentence: Behavioral measures included locomotion , irritability , copulation , partner preference , and aggression .

Example answer:
{"entities": [{"text": "irritability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aggression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We collected 837 independent subjects ( 393 PD , 444 controls ) .

Example answer:
{"entities": [{"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "ChemicalEntity"}, {"text": "scopolamine-", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fifteen moderate MDMA users ( < 55 lifetime tablets ) , 22 heavy MDMA+ users ( > 55 lifetime tablets ) , 16 ex-MDMA+ users ( last tablet > 1 year ago ) and 13 controls were compared on a battery of neuropsychological tests .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "MDMA+", "type": "ChemicalEntity"}]}

Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "impaired social and emotional judgement processes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical evaluation included the use of the Unified Parkinson 's Disease Rating Scale ( UPDRS ) , Hoehn_Yahr score and Schwab England activities of daily living ( ADL ) score in 'on'- and 'off'-drug conditions before surgery and 6 months after surgery .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Input:
Sentence: Participants completed a drug history questionnaire , Beck Depression Inventory , Barratt Impulsiveness Scale , Pittsburgh Sleep Quality Index , and Wechsler Memory Scale-Revised which , in total , provided 13 psychometric measures .

## Item biored:test:780
Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "MPTP-induced", "type": "ChemicalEntity"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Live imaging of Tuba1a-mutant neurons revealed slowed migration and increased neuronal branching , which correlated with directionality alterations and perturbed nucleus-centrosome ( N-C ) coupling .

Example answer:
{"entities": [{"text": "Tuba1a-mutant", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: High-signal intensity lesions on DWI tended to show low signal intensity on ADC map ( 3/4 ) , but in one patient , high signal intensity was shown at bilateral dentate nuclei on not only DWI but also ADC map .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Increased numbers of neurons that expressed CCR2 was observed following SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , the role of TD-induced HIF-1a in neurological injury is currently unknown .

Example answer:
{"entities": [{"text": "TD-induced", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "neurological injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The extent of neuronal injury was determined by 2,3,5-triphenyltetrazolium staining .

Example answer:
{"entities": [{"text": "neuronal injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "2,3,5-triphenyltetrazolium", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results demonstrate that induction of HIF-1a mediated transcriptional up-regulation of pro-apoptotic/inflammatory signaling contributes to astrocyte cell death during thiamine deficiency .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "thiamine deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These biochemical lesions result in apoptotic cell death in both neurons and astrocytes .

Example answer:
{"entities": []}

Input:
Sentence: Here , we investigated how this specific signal is propagated to cause the HI neuronal death .

## Item biored:test:737
Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that IGF-1R may increase cell viability under hypoxic conditions by promoting autophagy and scavenging ROS production , which is closed with PI3K/Akt/mTOR signaling pathway .

Example answer:
{"entities": [{"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "hypoxic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "PI3K/Akt/mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The identification of FH as a tumor suppressor was an unexpected finding and following the identification of subunits of succinate dehydrogenase in 2000 and 2001 , was only the second description of the involvement of an enzyme of intermediary metabolism in tumorigenesis .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditionally deleting one copy of FGF receptor 2 ( FGFR2 ) in adult mouse airway basal cells results in self-renewal and differentiation phenotypes .

Example answer:
{"entities": [{"text": "FGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : LOH of the RB1 gene could play an important role in tumor formation .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The transforming growth factor ( TGF ) -b-inducible early gene-1 ( TIEG1 ) plays a crucial role in modulating cell apoptosis and proliferation in a number of diseases , including pancreatic cancer , leukaemia and osteoporosis .

Example answer:
{"entities": [{"text": "transforming growth factor ( TGF ) -b-inducible early gene-1", "type": "GeneOrGeneProduct"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "osteoporosis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Exogenous bFGF rescues spheroid-forming activity and tumorigenicity of the U87-DACH1-high cells , suggesting that loss of DACH1 increases the number of tumor-initiating cells through transcriptional activation of bFGF .

## Item biored:test:724
Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: D90A-SOD1 mediated amyotrophic lateral sclerosis : a single founder for all cases with evidence for a Cis-acting disease modifier in the recessive haplotype .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We also found a significant contribution of the Gln/Gln or Arg/Gln versus Arg/Arg genotype to the presence of either the malar rash or photosensitivity manifestations of SLE OR=2.241 ( 1.328-3.781 , p=0.0023 , pcorr=0.0414 ) .

Example answer:
{"entities": [{"text": "malar rash", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She had profound insulin resistance , diabetes , severe hypertriglyceridemia and relapsing pancreatitis , while her pre-pubescent daughter had normal fat distribution but elevated plasma triglycerides and C-peptide and depressed high-density lipoprotein cholesterol .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertriglyceridemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}, {"text": "high-density lipoprotein cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The neurologic evaluation revealed loss of sensation in the saddle area and medial aspect of her right leg .

Example answer:
{"entities": [{"text": "loss of sensation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The clinical findings from this patient include recurrent fractures , mild bone deformities , delayed tooth eruption , normal hearing , and white sclera .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "fractures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bone deformities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tooth eruption", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Clinical features included hypotonia , abnormal movements , convulsions , and moderate mental retardation with relative sparing of gross motor function , activities of daily living skills , and receptive language .

Example answer:
{"entities": [{"text": "hypotonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "abnormal movements", "type": "DiseaseOrPhenotypicFeature"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The clinical features included hearing impairment , ichthyosiform erythroderma with hyperkeratotic plaques , palmoplantar keratoderma , alopecia of the scalp and eyelashes , and a thick vernix caseosa-like covering of the scalp .

Example answer:
{"entities": [{"text": "hearing impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ichthyosiform erythroderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "palmoplantar keratoderma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alopecia of the scalp and eyelashes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Although lacking corneal disease , she showed severe symptoms of SLS with uncommon deterioration in oral motor function and loss of ambulation .

## Item biored:test:759
Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the WFS1 gene of these patients , we identified a novel mutation , a nine nucleotide insertion ( AFF344-345ins ) .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "nine nucleotide insertion", "type": "SequenceVariant"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}]}

Example input:
Sentence: A missense mutation in BCOR was described in a family with Lenz microphthalmia syndrome , a phenotype showing substantial overlapping features with that described in the two cousins .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}, {"text": "Lenz microphthalmia syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Since the first molecular characterization of an FH mutation by Bourgeron et al in 1994 , a series of reports of both FH deficiency patients and patients with MCUL/HLRRC have described 107 variants , of which 93 are thought to be pathogenic .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "FH deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MCUL/HLRRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation at the DFNA36 hearing loss locus reveals a critical function and potential genotype-phenotype correlation for amino acid-572 of TMC1 .

Example answer:
{"entities": [{"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , the MLFs infected with Bach1 siRNA exhibited increased mRNA and protein expression levels of heme oxygenase-1 and glutathione peroxidase 1 , but decreased levels of TGF-b1 and interleukin-6 in the cell supernatants compared with the cells exposed to TGF-b1 alone .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "heme oxygenase-1", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase 1", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "interleukin-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The molecular basis of FDH involves mutations in the PORCN gene , which encodes an enzyme that allows membrane targeting and secretion of several Wnt proteins critical for normal tissue development .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The FH mutation database : an online database of fumarate hydratase mutations involved in the MCUL ( HLRCC ) tumor syndrome and congenital fumarase deficiency .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "fumarate hydratase", "type": "GeneOrGeneProduct"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HLRCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fumarase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified 10 new families segregating DFNB7/B11 deafness and TMC1 mutations , including three novel alleles .

Example answer:
{"entities": [{"text": "DFNB7/B11 deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Our result expands the mutation spectrum of FBN1 and contributes to the study of the molecular pathogenesis of Marfan syndrome .

## Item biored:test:738
Example input:
Sentence: Both sporadic and inherited BCCs are associated with mutations in the tumor suppressor gene PTCH1 , but there is still uncertainty on the role of its homolog PTCH2 .

Example answer:
{"entities": [{"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aberrant expression of UCHL1 in pediatric high-grade gliomas may promote cell invasion , transformation , and self-renewal properties , at least in part , by modulating Wnt/Beta catenin activity .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Wnt/Beta catenin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: UCHL1 might act as an oncogene in glioma within the gene network that imparts stem-like characteristics to these cancer cells .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : LOH of the RB1 gene could play an important role in tumor formation .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work we used SF188 and SJ-GBM2 cell lines to study the function of the ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) , a deubiquitinase de-regulated in several cancers , in pediatric high-grade gliomas .

Example answer:
{"entities": [{"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gliomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A g-secretase inhibitor , DAPT , selectively depleted CD133 ( + ) cells , suppressed N1ICD and SKP2 , induced p27Kip1 , inhibited ACC growthin vivo , and sensitized CD133 ( + ) cells to radiation .

Example answer:
{"entities": [{"text": "g-secretase", "type": "GeneOrGeneProduct"}, {"text": "DAPT", "type": "ChemicalEntity"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "SKP2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The identification of FH as a tumor suppressor was an unexpected finding and following the identification of subunits of succinate dehydrogenase in 2000 and 2001 , was only the second description of the involvement of an enzyme of intermediary metabolism in tumorigenesis .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Input:
Sentence: These results illustrate that DACH1 is a distinctive tumor suppressor , which does not only suppress growth of tumor cells but also regulates bFGF-mediated tumor-initiating activity of glioma cells .

## Item biored:test:757
Example input:
Sentence: CONCLUSIONS : Two novel CRELD1 mutations were identified in the calcium-binding EGF domain in patients with AVSD .

Example answer:
{"entities": [{"text": "CRELD1", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Expression of the normal and mutant G3 domains in mammalian cells showed that the mutation created a functional N-glycosylation site but did not adversely affect protein trafficking and secretion .

Example answer:
{"entities": []}

Example input:
Sentence: We also demonstrate that the A118D SEA domain mutation causes an intra-molecular structural imbalance that impairs matriptase-2 activation .

Example answer:
{"entities": [{"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This frameshift mutation leads to a caveolin-1 protein that contains all known functional domains but has a change in only the final 20 amino acids of the C-terminus .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study we report a novel CACNA1S mutation in a new region of the protein , the S3 segment of domain III .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations T71N and A190T in hippocalcin did not affect stability , calcium-binding affinity or translocation to cellular membranes ( Ca2+/myristoyl switch ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "Ca2+/myristoyl", "type": "ChemicalEntity"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This generates a conformational shift in the p17 R76G mutant which enables a functional epitope ( s ) , masked in refp17 , to elicit B-cell growth-promoting signals after its interaction with a still unknown receptor ( s ) .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "R76G", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The D2267 residue is predicted to coordinate binding of a calcium ion , which influences the conformational binding loops of the C-type lectin domain that mediate interactions with tenascins and other extracellular-matrix proteins .

Example answer:
{"entities": [{"text": "D2267", "type": "SequenceVariant"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Input:
Sentence: The mutant residue located in the calcium binding epidermal growth factor-like # 15 domain is highly conserved among mammalian species and could probably induce conformation change of the domain .

## Item biored:test:793
Example input:
Sentence: The current study aimed to assess the impact of MDMA use on three separate central executive processes ( set shifting , inhibition and memory updating ) and also on `` prefrontal '' mediated social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , temperature effects of drugs that have been used to manipulate brain DA neurotransmission confound interpretation of the data .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : Thus , in contradiction to animal studies , Epo treatment within a physiological relevant range in humans does not exert direct effects in a subcutaneous WAT .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Future studies are needed to assess the therapeutic potential emerging from our finding for human W-ICH .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "W-ICH", "type": "ChemicalEntity"}]}

Example input:
Sentence: Future research should include animal studies that address mechanistic hypotheses and studies of human populations that integrate early-life exposure , molecular alterations , and latent disease outcomes .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of the study was to investigate the effects of moderate and heavy MDMA use on cognitive function , as well as the effects of long-term abstention from MDMA , in subjects genotyped for 5-HTTLPR .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A second aim of the study was to determine whether these effects differ for females and males .

Example answer:
{"entities": []}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Example input:
Sentence: While the mechanisms underlying cocaine 's rewarding effects have been studied extensively , less attention has been paid to the unpleasant behavioral states induced by cocaine , such as anxiety .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Unfortunately , the results from human research investigating its psychological effects have been inconsistent .

## Item biored:test:744
Example input:
Sentence: In particular , subjects with stage IV had a two times higher probability of having either IL1B-31TT ( or IL1B-511CC ) genotype compared with stage I subjects .

Example answer:
{"entities": [{"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: After adjustment for sex and age , we found no association of SNPs rs6235 and rs6232 with BMI or other weight-related traits ( all p > or= 0.07 ) .

Example answer:
{"entities": [{"text": "rs6235", "type": "SequenceVariant"}, {"text": "rs6232", "type": "SequenceVariant"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs25531 and the haplotype 5-HTTLPR/rs25531 did not associate with risk of PD .

Example answer:
{"entities": [{"text": "rs25531", "type": "SequenceVariant"}, {"text": "5-HTTLPR/rs25531", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One is the Lys198Asn polymorphism , which showed a positive association with BP in overweight people .

Example answer:
{"entities": [{"text": "Lys198Asn", "type": "SequenceVariant"}, {"text": "overweight", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Input:
Sentence: A significant association was also observed between subjects carrying the rs8099917 TT responder genotype and higher levels of apoB-100 ( P = 6.4 10 ( -3 ) ) and LDL cholesterol ( P = 4.2 10 ( -3 ) ) .

## Item biored:test:616
Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore , epigenetic mechanisms , including DNA methylation and histone deacetylation , were indicated to be involved in DOCK8 down-regulation in lung cancer cells .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To identify a gene for MC , we performed linkage analysis with high-density SNP arrays in a single family , used a targeted array to capture exons and promoter sequences from the linked interval in 16 participants from 11 MC families , and sequenced the captured DNA using high-throughput parallel sequencing technologies .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Methylation of the 5'CpG island of the p14 gene was not suggested for any case without homozygous deletion .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We analyzed for PIK3CA and KRAS mutations and LINE-1 methylation by Pyrosequencing , microsatellite instability ( MSI ) , and DNA methylation ( epigenetic changes ) in eight CpG island methylator phenotype ( CIMP ) -specific promoters [ CACNA1G , CDKN2A ( p16 ) , CRABP1 , IGF2 , MLH1 , NEUROG1 , RUNX3 , and SOCS1 ] by MethyLight ( real-time PCR ) .

## Item biored:test:807
Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Light and electron microscopic observations of renal biopsy clearly showed characteristic findings of LPG , including lamellate thrombi in the lumen of dilated glomerular capillaries .

Example answer:
{"entities": [{"text": "LPG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lamellate thrombi", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whole cell recordings from non-transfected HEK cells and cells expressing human TRPV6 revealed the presence of a basal inward current in both types of cells when the internal solution contained 0.1 mm EGTA and 100 nm ( i ) or if the cytosolic Ca ( 2+ ) buffering remained undisturbed in perforated patch-clamp experiments .

Example answer:
{"entities": [{"text": "HEK", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "TRPV6", "type": "GeneOrGeneProduct"}, {"text": "EGTA", "type": "ChemicalEntity"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Immunoelectron microscopy further revealed an increased labeling of alpha-ENaC in the apical plasma membrane of cortical collecting duct principal cells of PAN-treated rats , indicating enhanced apical targeting of alpha-ENaC subunits .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "PAN-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The half button and ultrathin sections from the other half button were examined with special stains under a light microscope ( LM ) and an electron microscope ( EM ) separately .

Example answer:
{"entities": []}

Example input:
Sentence: Observation by electronic microscope revealed structural damage of podocytes ; the reduced expression level of podocyte marker genes , nephrin and podocin , was also detected by q-PCR .

Example answer:
{"entities": [{"text": "nephrin", "type": "GeneOrGeneProduct"}, {"text": "podocin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Transmission electron microscopy revealed the enlargement of smooth endoplasmic reticulum and the presence of intracytoplasmic vacuoles .

Example answer:
{"entities": []}

Input:
Sentence: The LSECs and sub-endothelial basement membrane were observed with the scanning and transmission electronic microscope .

## Item biored:test:733
Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: ADAM12 knockdown also diminished ALDEFLUOR ( + ) and CD44 ( hi ) /CD24 ( -/lo ) CSC-enriched populations in vitro and reduced tumorigenesis in mice in vivo .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The mutants also displayed reduced cell proliferation in the URS mesenchyme .

Example answer:
{"entities": []}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Utilizing the Eu-myc mouse model , where Myc is overexpressed specifically in B cells , both basal and stimulated BCR signaling were increased in precancerous B lymphocytes from Eu-myc mice compared with wild-type littermates .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "Myc", "type": "GeneOrGeneProduct"}, {"text": "BCR", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A g-secretase inhibitor , DAPT , selectively depleted CD133 ( + ) cells , suppressed N1ICD and SKP2 , induced p27Kip1 , inhibited ACC growthin vivo , and sensitized CD133 ( + ) cells to radiation .

Example answer:
{"entities": [{"text": "g-secretase", "type": "GeneOrGeneProduct"}, {"text": "DAPT", "type": "ChemicalEntity"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "SKP2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Input:
Sentence: Both ex vivo cellular proliferation and in vivo growth of s.c. transplanted tumors in mice are reduced in U87TR-Da cells with DACH1 expression ( U87-DACH1-high ) , compared with DACH1-nonexpressing U87TR-Da cells ( U87-DACH1-low ) .

## Item biored:test:705
Example input:
Sentence: METHODS : We performed comprehensive genomic profiling ( CGP ) for coding regions in more than 300 cancer-related genes of 186 GISTs to assess for their somatic alterations .

Example answer:
{"entities": [{"text": "cancer-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GISTs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sequence analysis of aggrecan complementary DNA from an affected individual revealed homozygosity for a missense mutation ( c.6799G -- > A ) that predicts a p.D2267N amino acid substitution in the C-type lectin domain within the G3 domain of aggrecan .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "c.6799G -- > A", "type": "SequenceVariant"}, {"text": "p.D2267N", "type": "SequenceVariant"}]}

Example input:
Sentence: The metrics from DNA damage and repair study were correlated with the genotypes of common polymorphisms of the hOGG1 and RAD51 genes : a G -- > C transversion at 1245 position of the hOGG1 gene producing a Ser -- > Cys substitution at the codon 326 ( the Ser326Cys polymorphism ) and a G -- > C substitution at position 135 ( 5'-untranslated region ) of the RAD51 gene ( the G135C polymorphism ) .

Example answer:
{"entities": [{"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "RAD51", "type": "GeneOrGeneProduct"}, {"text": "G -- > C transversion at 1245 position", "type": "SequenceVariant"}, {"text": "Ser -- > Cys substitution at the codon 326", "type": "SequenceVariant"}, {"text": "Ser326Cys", "type": "SequenceVariant"}, {"text": "G -- > C substitution at position 135", "type": "SequenceVariant"}, {"text": "G135C", "type": "SequenceVariant"}]}

Example input:
Sentence: We genotyped candidate single-nucleotide polymorphisms ( SNP ) in IL10 , CRP , GPX1 , GSR , GSTP1 , hOGG1 , IL1B , IL1RN , IL6 , IL8 , MPO , NOS2 , NOS3 , SOD1 , SOD2 , SOD3 , TLR4 , and TNF and tagging SNPs in IL10 , CRP , GSR , IL1RN , IL6 , NOS2 , and NOS3 .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "IL1RN", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "IL8", "type": "GeneOrGeneProduct"}, {"text": "MPO", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "NOS3", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "SOD3", "type": "GeneOrGeneProduct"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "TNF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This mutation was linked to a novel single nucleotide polymorphism ( SNP ) in intron 3 ( IVS3 + 18C > T ) .

Example answer:
{"entities": [{"text": "IVS3 + 18C > T", "type": "SequenceVariant"}]}

Example input:
Sentence: The -930A > G polymorphism was genotyped using the TaqMan - Pre-designed SNP Genotyping Assay ( Applied Biosystems ) .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: Seven SNPs in CFH and two SNPs in C2 , CFB ' , and C3 were genotyped using the ABI SNaPshot method .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Input:
Sentence: Furthermore , we established a small amplicon genotyping ( SAG ) method for detecting three high frequency coding-region SNPs ( rs1800255 : G > A , rs1801184 : T > C , and rs2271683 : A > G ) in COL3A1 to differentiate mutations before sequencing .

## Item biored:test:760
Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: NF-kB functions as a molecular link between tumor cells and Th1/Tc1 T cells in the tumor microenvironment to exert radiation-mediated tumor suppression .

Example answer:
{"entities": [{"text": "NF-kB", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SLURP1 mutation-impaired T-cell activation in a family with mal de Meleda .

Example answer:
{"entities": [{"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "mal de Meleda", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the association of the SLURP1 gene mutation with T-cell activation in a Taiwanese family with MDM .

Example answer:
{"entities": [{"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To test that SLURP-1 is essential for T-cell activation .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The presence of wild-type SLURP-1 is essential for normal T-cell activation .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SLURP-1 is an allosteric agonist to the nicotinic acetylcholine receptor ( nAchR ) and it regulates epidermal homeostasis .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "nicotinic acetylcholine receptor", "type": "GeneOrGeneProduct"}, {"text": "nAchR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Reciprocal effects of NNK and SLURP-1 on oncogene expression in target epithelial cells .

## Item biored:test:695
Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To investigate the GSTP1 Ile105Val genotype frequency in prostate cancer cases in the Kashmiri population , we designed a case-control study , in which 50 prostate cancer cases and 45 benign prostate hyperplasia cases were studied for GSTP1 Ile105Val polymorphism , compared to 80 controls taken from the general population , employing the PCR-RFLP technique .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings extend the causes of CDG to larger DNA deletions and identify the first Japanese CDG-Ic mutation .

Example answer:
{"entities": [{"text": "CDG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDG-Ic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The allele frequencies of polymorphisms at codon 787 CAG/CAA ( Gln/Gln ) in glioblastomas in Japan were G/G ( 82.4 % ) , G/A ( 10.8 % ) , A/A ( 6.8 % ) , corresponding to G 0.878 versus A 0.122 , significantly different from those in glioblastomas in Switzerland : G/G ( 27.2 % ) , G/A ( 28.4 % ) , A/A ( 44.4 % ) , corresponding to G 0.414 versus A 0.586 ( p < 0.0001 ) .

Example answer:
{"entities": [{"text": "codon 787 CAG/CAA", "type": "SequenceVariant"}, {"text": "Gln/Gln", "type": "SequenceVariant"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our study suggests that p.R246Q mutation is common amongst patients with SRD5A2 gene defect from the Northern states of India .

Example answer:
{"entities": [{"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There is a strong evidence for the unitary origin of the CCR5-Delta32 mutation , this it is found principally in Europe and Western Asia , with generally a north-south downhill cline frequency .

Example answer:
{"entities": [{"text": "CCR5-Delta32", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We reviewed the genotype of CGL cases from Japan , India , China and Taiwan , and found that BSCL2 is a major causative gene for CGL in Asian .

## Item biored:test:758
Example input:
Sentence: CONCLUSIONS : The R124C mutation in TGFBI cosegregated with LCD type I in the investigated family .

Example answer:
{"entities": [{"text": "R124C", "type": "SequenceVariant"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "LCD type I", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified 10 new families segregating DFNB7/B11 deafness and TMC1 mutations , including three novel alleles .

Example answer:
{"entities": [{"text": "DFNB7/B11 deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: As only the two family members homozygous for the mutation showed WFS , these data support the notion that this mutation is the cause of WFS .

Example answer:
{"entities": [{"text": "WFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hypomorphic mutations in meckelin ( MKS3/TMEM67 ) cause nephronophthisis with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "meckelin", "type": "GeneOrGeneProduct"}, {"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "nephronophthisis with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the WFS1 gene of these patients , we identified a novel mutation , a nine nucleotide insertion ( AFF344-345ins ) .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "nine nucleotide insertion", "type": "SequenceVariant"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : We indentified a novel p.S1235P mutation in FBN1 , which is the causative mutation for MFS in this family .

## Item biored:test:769
Example input:
Sentence: CONCLUSION : SELP and IRAK1 were identified as novel SLE-associated genes with a high degree of significance , suggesting new directions in understanding the pathogenesis of SLE .

Example answer:
{"entities": [{"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}, {"text": "SLE-associated", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The SLC6A4 promoter single nucleotide polymorphism rs25531 ( A -- > G ) was evaluated too .

Example answer:
{"entities": [{"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "rs25531", "type": "SequenceVariant"}, {"text": "A -- > G", "type": "SequenceVariant"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CD72 polymorphisms associated with alternative splicing modify susceptibility to human systemic lupus erythematosus through epistatic interaction with FCGR2B .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It has been shown that DNA repair is reduced in patients with systemic lupus erythematosus ( SLE ) and that the X-ray repair cross-complementing ( XRCC1 ) Arg399Gln ( rs25487 ) polymorphism may contribute to DNA repair .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "X-ray repair cross-complementing", "type": "GeneOrGeneProduct"}, {"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "rs25487", "type": "SequenceVariant"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Polymorphisms in the IRF5 gene have been associated with susceptibility to systemic lupus erythaematosus ( SLE ) in Caucasian and Asian populations , but their involvement in other autoimmune diseases is still uncertain .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythaematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: XRCC1 Arg399Gln gene polymorphism and the risk of systemic lupus erythematosus in the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Contribution of STAT4 gene single-nucleotide polymorphism to systemic lupus erythematosus in the Polish population .

## Item biored:test:798
Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fifteen moderate MDMA users ( < 55 lifetime tablets ) , 22 heavy MDMA+ users ( > 55 lifetime tablets ) , 16 ex-MDMA+ users ( last tablet > 1 year ago ) and 13 controls were compared on a battery of neuropsychological tests .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "MDMA+", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy-specific hypoactivity was evident in the right dorsal anterior cingulated cortex ( ACC ) and left posterior cingulated cortex .

Example answer:
{"entities": [{"text": "Ecstasy-specific", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: To address the potential confounding effects of the cannabis use of the ecstasy using group , a second analysis included 14 previously tested cannabis users ( Nestor , L. , Roberts , G. , Garavan , H. , Hester , R. , 2008 .

Example answer:
{"entities": [{"text": "cannabis", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "Learning and memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: It has been consistently shown that ecstasy users display impairments in learning and memory performance .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "impairments in learning and memory", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Strikingly , despite prolonged abstinence ( mean , 4.98 ; range , 4-9 years ) , past ecstasy users showed few signs of recovery .

## Item biored:test:772
Example input:
Sentence: We evaluated the frequency of the XRCC1 Arg399Gln substitution in patients with SLE ( n=265 ) and controls ( n=360 ) in a sample of the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: The OR for the 399 Gln allele in patients with SLE was 1.406 ( 95 % CI=1.111-1.779 , p=0.0045 ) .

Example answer:
{"entities": [{"text": "399 Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our studies may confirm that the XRCC1 Arg399Gln polymorphism may increase the risk of incidence of SLE and the occurrence of some SLE manifestations .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The odds ratio ( OR ) for SLE patients with the Gln/Gln versus Gln/Arg or Arg/Arg genotypes was 1.553 ( 95 % confidence interval [ CI ] =0.9573-2.520 ; p=0.0729 ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: We found that patients with the STAT4 C/G and CC genotypes exhibited a 1.583-fold increased risk of SLE incidence ( 95 % CI = 1.168-2.145 , p = 0.003 ) , with OR for the C/C versus C/G and G/G genotypes was 1.967 ( 95 % CI = 1.152-3.358 , p = 0.0119 ) .

## Item biored:test:777
Example input:
Sentence: Alpha-lipoic acid prevents mitochondrial damage and neurotoxicity in experimental chemotherapy neuropathy .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "MPTP-induced", "type": "ChemicalEntity"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Voltage-Dependent Anion Channel 1 ( VDAC1 ) Participates the Apoptosis of the Mitochondrial Dysfunction in Desminopathy .

Example answer:
{"entities": [{"text": "Voltage-Dependent Anion Channel 1", "type": "GeneOrGeneProduct"}, {"text": "VDAC1", "type": "GeneOrGeneProduct"}, {"text": "Mitochondrial Dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Desminopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The study investigates if alpha-lipoic acid is neuroprotective against chemotherapy induced neurotoxicity , if mitochondrial damage plays a critical role in toxic neurodegenerative cascade , and if neuroprotective effects of alpha-lipoic acid depend on mitochondria protection .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "toxic neurodegenerative cascade", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "mitochondrial impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Brain-derived neurotrophic factor significantly inhibited Dox-induced cardiomyocyte apoptosis , oxidative stress and cardiac dysfunction in rats .

Example answer:
{"entities": [{"text": "cardiac", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Alpha-lipoic acid protects sensory neurons through its anti-oxidant and mitochondrial regulatory functions , possibly inducing the expression of frataxin .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Critical role of neuronal pentraxin 1 in mitochondria-mediated hypoxic-ischemic neuronal injury .

## Item biored:test:799
Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy-specific hypoactivity was evident in the right dorsal anterior cingulated cortex ( ACC ) and left posterior cingulated cortex .

Example answer:
{"entities": [{"text": "Ecstasy-specific", "type": "ChemicalEntity"}]}

Example input:
Sentence: To address the potential confounding effects of the cannabis use of the ecstasy using group , a second analysis included 14 previously tested cannabis users ( Nestor , L. , Roberts , G. , Garavan , H. , Hester , R. , 2008 .

Example answer:
{"entities": [{"text": "cannabis", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "Learning and memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: It has been consistently shown that ecstasy users display impairments in learning and memory performance .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "impairments in learning and memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Input:
Sentence: Compared with present ecstasy users , the past users showed no change for ten measures , increased impairment for two measures , and improvement on just one measure .

## Item biored:test:775
Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: A haplotype containing these four SNPs ( CATA ) significantly increased protection of wet AMD with a P value of 0.0005 and an odds ratio of 0.29 ( 95 % confidence interval : 0.15-0.60 ) .

Example answer:
{"entities": [{"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Seven SNPs in CFH and two SNPs in C2 , CFB ' , and C3 were genotyped using the ABI SNaPshot method .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: 3R G > C SNP genotyping did not add prognostic information .

Example answer:
{"entities": [{"text": "G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We genotyped candidate single-nucleotide polymorphisms ( SNP ) in IL10 , CRP , GPX1 , GSR , GSTP1 , hOGG1 , IL1B , IL1RN , IL6 , IL8 , MPO , NOS2 , NOS3 , SOD1 , SOD2 , SOD3 , TLR4 , and TNF and tagging SNPs in IL10 , CRP , GSR , IL1RN , IL6 , NOS2 , and NOS3 .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "IL1RN", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "IL8", "type": "GeneOrGeneProduct"}, {"text": "MPO", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "NOS3", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "SOD3", "type": "GeneOrGeneProduct"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "TNF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CASP8 -652 6N del variant genotypes or haplotypes were inversely associated with SCCHN risk ( adjusted OR , 0.70 ; 95 % CI , 0.57-0.85 for the ins/del + del/del genotypes compared with the ins/ins genotype ; adjusted OR , 0.73 ; 95 % CI , 0.55-0.97 for the del-D haplotype compared with the ins-D haplotype ) .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In univariate analysis , the OR for the C4A deletion was 1.38 , p = 0.075 , but after simultaneous adjustment for the other four SNPs the odds ratio was 1.01 , p = 0.98 .

Example answer:
{"entities": [{"text": "C4A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Input:
Sentence: Moreover , we found a contribution of STAT4 C/C and C/G genotypes to the presence of the anti-snRNP Ab OR = 3.237 ( 1.667-6.288 , p = 0.0003 ) , ( p ( corr ) = 0.0051 ) and the presence of the anti-Scl-70 Ab OR = 2.665 ( 1.380-5.147 , p = 0.0028 ) , ( p ( corr ) = 0.0476 ) .

## Item biored:test:820
Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: Fourteen days after hospitalization , creatine kinase level had returned to 230 IU/L and the patient was discharged .

Example answer:
{"entities": [{"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: 7 days later , the fever disappeared and the patient 's serum CPK levels were normalized ( 175 IU/L ) .

Example answer:
{"entities": [{"text": "fever", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "CPK", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient achieved a partial response 6 months after the initiation of the S-1 treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "S-1", "type": "ChemicalEntity"}]}

Example input:
Sentence: Renal failure developed after a prolonged course of vancomycin therapy in 2 patients who were receiving tenofovir disoproxil fumarate as part of an antiretroviral regimen .

Example answer:
{"entities": [{"text": "Renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vancomycin", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "tenofovir disoproxil fumarate", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Our patient was admitted to the MICU after being found unresponsive with presumed toxicity from acetaminophen which was ingested over a 2-day period .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: One month after starting the antiviral therapy , the patient was admitted to the hospital because he developed rhabdomyolysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Despite immediate intravenous antimicrobial therapy , he succumbed 23 h after the onset .
