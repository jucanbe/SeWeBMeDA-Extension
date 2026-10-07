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

## Item biored:test:604
Example input:
Sentence: After adjusting for potential confounders , we found that the risk of HIV seroconversion among participants who were daily smokers of crack cocaine increased over time ( period 1 : hazard ratio [ HR ] 1.03 , 95 % confidence interval [ CI ] 0.57-1.85 ; period 2 : HR 1.68 , 95 % CI 1.01-2.80 ; and period 3 : HR 2.74 , 95 % CI 1.06-7.11 ) .

Example answer:
{"entities": [{"text": "HIV seroconversion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crack cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Massive proteinuria and acute renal failure after oral bisphosphonate ( alendronate ) administration in a patient with focal segmental glomerulosclerosis .

Example answer:
{"entities": [{"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bisphosphonate", "type": "ChemicalEntity"}, {"text": "alendronate", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "focal segmental glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cocaine causes memory and learning impairments in rats : involvement of nuclear factor kappa B and oxidative stress , and prevention by topiramate .

Example answer:
{"entities": [{"text": "Cocaine", "type": "ChemicalEntity"}, {"text": "memory and learning impairments", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "topiramate", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether the risk of HIV seroconversion among daily smokers of crack cocaine changed over time , we used Cox proportional hazards regression and divided the study into 3 periods : May 1 , 1996-Nov. 30 , 1999 ( period 1 ) , Dec. 1 , 1999-Nov. 30 , 2002 ( period 2 ) , and Dec. 1 , 2002-Dec. 30 , 2005 ( period 3 ) .

Example answer:
{"entities": [{"text": "HIV seroconversion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crack cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: As heroin addicts sometimes faint while using illicit drugs , doctors might attribute too many episodes of syncope to illicit drug use and thereby underestimate the incidence of TdP in this special population , and the high mortality in this population may , in part , be caused by the proarrhythmic effect of methadone .

Example answer:
{"entities": [{"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Complications were observed in two patients : one had a left homonymous hemianopsia after pallidotomy and another one developed left hemiballistic movements 3 days after subthalamotomy which partly improved within 1 month with Valproate 1000 mg/day .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "homonymous hemianopsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Second , a stereotactic injection of collagenase was administered to induce hemorrhage in the right striatum .

Example answer:
{"entities": [{"text": "collagenase", "type": "ChemicalEntity"}, {"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Bilateral haemorrhagic infarction of the globus pallidus after cocaine and alcohol intoxication .

## Item biored:test:623
Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ovx significantly enhanced the hypotensive response to alpha-methyldopa , in contrast to no effect on rilmenidine hypotension .

Example answer:
{"entities": [{"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient was treated with hyperosmolar therapy , hyperventilation , sedation , and chemical paralysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "hyperventilation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice subjected to hypotensive episodes showed a significant decrease in latency time ( 178 +/- 156 s ) compared with those injected with saline , NTG + NIMO , or delayed NTG ( 580 +/- 81 s , 557 +/- 67 s , and 493 +/- 146 s , respectively ) .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "enflurane", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND : Vasopressor agents are used to correct anesthesia-induced hypotension .

## Item biored:test:581
Example input:
Sentence: PURPOSE : In the present study , we aimed to substantiate the putative significance of angiotensin I-converting enzyme ( ACE ) on gastric cancer biology by investigating the influence of its gene polymorphism on gastric cancer progression .

Example answer:
{"entities": [{"text": "angiotensin I-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The distribution of the ACE genotypes did not differ significantly from the control group of 189 patients without gastric cancer .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Our study shows that ACE is expressed locally in gastric cancer and that the gene polymorphism influences metastatic behavior .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : The present study aimed to estimate the association between susceptibility to migraine and the 12-nucleotide insertion/deletion ( indel ) polymorphism in promoter region of alpha ( 2B ) -adrenergic receptor gene ( ADRA2B ) .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "12-nucleotide insertion/deletion ( indel )", "type": "SequenceVariant"}, {"text": "alpha ( 2B ) -adrenergic receptor", "type": "GeneOrGeneProduct"}, {"text": "ADRA2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Lack of association between ADRA2B-4825 gene insertion/deletion polymorphism and migraine in Chinese Han population .

Example answer:
{"entities": [{"text": "ADRA2B-4825", "type": "GeneOrGeneProduct"}, {"text": "gene insertion/deletion", "type": "SequenceVariant"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Despite the application of this high-throughput genotyping method , negative results from the two-stage DNA pooling design used to screen loci within the TPH , AADC and MAOA genes did not support their role in migraine susceptibility .

Example answer:
{"entities": [{"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We found a higher frequency of the ACE DD gene mutation in Turkish asthmatic patients compared with non-asthmatics , suggesting that this ACE gene polymorphism may be a risk factor for asthma but does not increase the severity of the disease .

## Item biored:test:642
Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Gene polymorphism resulting in the substitution of glutamine with lysine at residue 223 in the carbohydrate recognition domain of SP-A2 increases susceptibility to meningococcal disease , as well as the risk of death .

Example answer:
{"entities": [{"text": "glutamine with lysine at residue 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "SP-A2", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ApoE gene analysis showed a nucleotide substitution of G to C at codon 158 of exon 4 .

Example answer:
{"entities": [{"text": "ApoE", "type": "GeneOrGeneProduct"}, {"text": "G to C at codon 158", "type": "SequenceVariant"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single nucleotide substitution I280S ( 1123T -- > G ) was present either on both alleles or in a hemizygous form with complete deletion of the second allele .

Example answer:
{"entities": [{"text": "I280S", "type": "SequenceVariant"}, {"text": "1123T -- > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: The CASP8 -652 6N del variant genotypes or haplotypes were inversely associated with SCCHN risk ( adjusted OR , 0.70 ; 95 % CI , 0.57-0.85 for the ins/del + del/del genotypes compared with the ins/ins genotype ; adjusted OR , 0.73 ; 95 % CI , 0.55-0.97 for the del-D haplotype compared with the ins-D haplotype ) .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Indeed , two different bioinformatics approaches , PolyPhen and SIFT analysis , predicted C88Y to be a damaging substitution .

## Item biored:test:600
Example input:
Sentence: We propose that a cis-acting regulatory polymorphism has arisen close to D90A-SOD1 in the recessive founder , which decreases ALS susceptibility in heterozygotes and slows disease progression .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: By positional cloning , we have identified the gene strongly associated with a form of degenerative ataxia ( chromosome 16q22.1-linked ADCA ) that clinically shows progressive pure cerebellar ataxia .

Example answer:
{"entities": [{"text": "degenerative ataxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebellar ataxia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A comparison of genotypes , ARSA activities , and clinical data on 4 individuals carrying the allele of 81 patients with MLD examined , further validates the concept that different degrees of residual ARSA activity are the basis of phenotypical variation in MLD ..

Example answer:
{"entities": [{"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Overall , eight families with six mutations in ARX were identified ( 1.31 % ) : five duplication mutations in pA2 ( 0.82 % ) with three new clinical reports of families with the dup24bp and two duplications larger than the dup24bp mutation discovered ( dup27bp , dup33bp ) ; and three point mutations ( 0.6 % ) , including one novel mutation in the homeodomain ( c.1074G > T ) .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "dup24bp", "type": "SequenceVariant"}, {"text": "dup27bp", "type": "SequenceVariant"}, {"text": "dup33bp", "type": "SequenceVariant"}, {"text": "c.1074G > T", "type": "SequenceVariant"}]}

Example input:
Sentence: Although haploinsufficiency of the T-box transcription factor gene TBX1 is thought to cause the phenotype , to date , only four different point mutations in TBX1 have been reported in association with six of the major features of 22q11.2 deletion syndrome .

Example answer:
{"entities": [{"text": "T-box transcription factor", "type": "GeneOrGeneProduct"}, {"text": "TBX1", "type": "GeneOrGeneProduct"}, {"text": "22q11.2 deletion syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Deletion 22q11.2 syndrome is the most frequent known microdeletion syndrome and is associated with a highly variable phenotype , including DiGeorge and Shprintzen ( velocardiofacial ) syndromes .

Example answer:
{"entities": [{"text": "Deletion 22q11.2 syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DiGeorge and Shprintzen ( velocardiofacial ) syndromes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: As autistic symptoms are increased in individuals with 22q11.2 deletion syndrome , and large 22q11.2 deletions and duplications have been observed in ASD individuals , in this study , 98 individuals with ASD and 234 control individuals were genotyped for eight single-nucleotide polymorphisms in ADORA2A .

## Item biored:test:598
Example input:
Sentence: Previously , three beta-AR genes ( ADRB1 , ADRB2 and ADRB3 ) were resequenced , identifying polymorphisms that were used in genetic association studies of cardiovascular and metabolic disorders .

Example answer:
{"entities": [{"text": "beta-AR", "type": "GeneOrGeneProduct"}, {"text": "ADRB1", "type": "GeneOrGeneProduct"}, {"text": "ADRB2", "type": "GeneOrGeneProduct"}, {"text": "ADRB3", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular and metabolic disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: By positional cloning , we have identified the gene strongly associated with a form of degenerative ataxia ( chromosome 16q22.1-linked ADCA ) that clinically shows progressive pure cerebellar ataxia .

Example answer:
{"entities": [{"text": "degenerative ataxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebellar ataxia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A Cys 23-Ser 23 substitution in the 5-HT ( 2C ) receptor gene influences body weight regulation in females with seasonal affective disorder : an Austrian-Canadian collaborative study .

Example answer:
{"entities": [{"text": "Cys 23-Ser 23", "type": "SequenceVariant"}, {"text": "5-HT ( 2C ) receptor", "type": "GeneOrGeneProduct"}, {"text": "seasonal affective disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : These findings do not support a functional significance of ADRA2B indel polymorphism at position -4825 relative to the start codon in the far upstream region of the promoter in the present migraine subjects .

Example answer:
{"entities": [{"text": "ADRA2B", "type": "GeneOrGeneProduct"}, {"text": "indel polymorphism at position -4825", "type": "SequenceVariant"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate the association of DNA polymorphisms within steroid synthesis genes ( CYP11B2 , CYP11B1 ) and the postoperative resolution of hypertension in Chinese patients undergoing adrenalectomy for aldosterone-producing adenomas ( APA ) .

Example answer:
{"entities": [{"text": "steroid synthesis genes", "type": "GeneOrGeneProduct"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "aldosterone-producing adenomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Deletion 22q11.2 syndrome is the most frequent known microdeletion syndrome and is associated with a highly variable phenotype , including DiGeorge and Shprintzen ( velocardiofacial ) syndromes .

Example answer:
{"entities": [{"text": "Deletion 22q11.2 syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DiGeorge and Shprintzen ( velocardiofacial ) syndromes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our data do not provide support for rs2230912 or the other polymorphisms studied within the P2RX7 locus , being involved in susceptibility to mood disorders .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The gene P2RX7 is located in this chromosomal region and has been recently reported as a susceptibility gene for bipolar disorder and unipolar depression .

Example answer:
{"entities": [{"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "bipolar disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "unipolar depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neither rs2230912 nor any of 8 other SNPs genotyped across P2RX7 was found to be associated with mood disorder in general , nor specifically with bipolar or unipolar disorder .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar or unipolar disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The adenosine A ( 2A ) receptor gene ( ADORA2A ) is associated with panic disorder and is located on chromosome 22q11.23 .

## Item biored:test:608
Example input:
Sentence: Co-administration of lidocaine with desipramine reversed the changes of convulsive activity of lidocaine and cocaine induced by repeated administration of desipramine .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "desipramine", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : In this study , we evaluated the performance of dopamine beta-hydroxylase knockout ( Dbh -/- ) mice , which lack norepinephrine ( NE ) , in the elevated plus maze ( EPM ) to examine the contribution of noradrenergic signaling to cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "NE", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Memory retrieval of experiences acquired prior to cocaine administration was impaired and negatively correlated with NFkappaB activity in the frontal cortex .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Repeated administration of cocaine induces up-regulation of hippocampal NET function .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cocaine causes memory and learning impairments in rats : involvement of nuclear factor kappa B and oxidative stress , and prevention by topiramate .

Example answer:
{"entities": [{"text": "Cocaine", "type": "ChemicalEntity"}, {"text": "memory and learning impairments", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "topiramate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Daily treatment of cocaine increased [ ( 3 ) H ] norepinephrine uptake into the hippocampus .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: As heroin addicts sometimes faint while using illicit drugs , doctors might attribute too many episodes of syncope to illicit drug use and thereby underestimate the incidence of TdP in this special population , and the high mortality in this population may , in part , be caused by the proarrhythmic effect of methadone .

Example answer:
{"entities": [{"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Input:
Sentence: Bilateral basal ganglia infarcts after the use of cocaine , without concurrent heroin use , have never been reported .

## Item biored:test:595
Example input:
Sentence: Randomised clinical trials and observational studies have shown an increased risk of myocardial infarction , stroke , hypertension and heart failure during treatment with cyclooxygenase inhibitors .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heart failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cyclooxygenase inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cyclooxygenase inhibitors cause complex changes in renal , vascular and cardiac prostanoid profiles thereby increasing vascular resistance and fluid retention .

Example answer:
{"entities": [{"text": "Cyclooxygenase inhibitors", "type": "ChemicalEntity"}, {"text": "prostanoid", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the 10th day of paroxetine and alprazolam treatment , the patient exhibited marked psychomotor retardation , disorientation , and severe muscle rigidity with tremors .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tremors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Clinicians are exhorted to pay close attention when initiating levofloxacin therapy in patients taking medications with epileptogenic properties that are CYP1A2 substrates .

Example answer:
{"entities": [{"text": "levofloxacin", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CYP1A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In patients requiring the concurrent use of statins and CYP3A4 inhibitors , pravastatin , fluvastatin , and rosuvastatin carry the lowest risk of drug interactions ; atorvastatin carries moderate risk , whereas simvastatin and lovastatin have the highest risk and should be avoided in patients taking concomitant CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "statins", "type": "ChemicalEntity"}, {"text": "CYP3A4", "type": "GeneOrGeneProduct"}, {"text": "pravastatin", "type": "ChemicalEntity"}, {"text": "fluvastatin", "type": "ChemicalEntity"}, {"text": "rosuvastatin", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "lovastatin", "type": "ChemicalEntity"}, {"text": "CYP3A4 inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: Also , the multichannel blockers Amiodarone , Paroxetine , Terfenadine and Citalopram prolonged FPDc in a concentration dependent manner .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "Paroxetine", "type": "ChemicalEntity"}, {"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}]}

Input:
Sentence: Because toxicity may occur when flecainide is prescribed with paroxetine and other potent CYP2D6 inhibitors , flecainide plasma concentrations should be monitored closely with commencement of CYP2D6 inhibitors .

## Item biored:test:614
Example input:
Sentence: Our results thus indicates that PON1 192RR homozygosity is associated with increased mortality in women in the second half of life and that this increased mortality is possibly related to CHD severity and survival after CHD rather than susceptibility to development of CHD .

Example answer:
{"entities": [{"text": "PON1", "type": "GeneOrGeneProduct"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , Kras ( G12D ) -induced immortalization can also be abrogated by Sag deletion via senescence induction , which is again rescued by simultaneous deletion of Cdkn2a .

Example answer:
{"entities": [{"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Cdkn2a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , SNP1 of UP Ia gene affecting a C to T conversion and an Ala7Val change , and SNP7 of UP III affecting a C to G conversion and a Pro154Ala change , were marginally associated with VUR ( both P= 0.08 ) .

Example answer:
{"entities": [{"text": "UP Ia", "type": "GeneOrGeneProduct"}, {"text": "C to T", "type": "SequenceVariant"}, {"text": "Ala7Val", "type": "SequenceVariant"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "C to G", "type": "SequenceVariant"}, {"text": "Pro154Ala", "type": "SequenceVariant"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Input:
Sentence: However , the prognostic role of VDR expression or its relationship with PIK3CA or KRAS mutation remains uncertain .

## Item biored:test:597
Example input:
Sentence: RESULTS : We found that cocaine dose-dependently increased anxiety-like behavior in control ( Dbh +/- ) mice , as measured by a decrease in open arm exploration .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: These data suggest that U-II may be involved in some aspects of psychiatric disorders .

Example answer:
{"entities": [{"text": "U-II", "type": "GeneOrGeneProduct"}, {"text": "psychiatric disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A comparison of genotypes , ARSA activities , and clinical data on 4 individuals carrying the allele of 81 patients with MLD examined , further validates the concept that different degrees of residual ARSA activity are the basis of phenotypical variation in MLD ..

Example answer:
{"entities": [{"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: X-linked mental retardation has been traditionally divided into syndromic ( S-XLMR ) and non-syndromic forms ( NS-XLMR ) , although the borderlines between these phenotypes begin to vanish and mutations in a single gene , for example PQBP1 , can cause S-XLMR as well as NS-XLMR .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PQBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Epilepsy and/or movement disorder were major features in all 21 .

Example answer:
{"entities": [{"text": "Epilepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "movement disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alzheimer 's disease ( AD ) is a polygenic and multifactorial complex disease , whose etiopathology is still unclear , however several genetic factors have shown to increase the risk of developing the disease .

Example answer:
{"entities": [{"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Alpers ' syndrome is a fatal neurogenetic disorder first described more than 70 years ago .

Example answer:
{"entities": [{"text": "Alpers ' syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurogenetic disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Autosomal dominant cerebellar ataxia ( ADCA ) is a group of heterogeneous neurodegenerative disorders .

Example answer:
{"entities": [{"text": "Autosomal dominant cerebellar ataxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ARX mutations cause a diverse spectrum of human disorders , ranging from severe brain and genital malformations to non-syndromic intellectual disability ( ID ) .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "brain and genital malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ID", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Autism spectrum disorders ( ASDs ) are heterogeneous disorders presenting with increased rates of anxiety .

## Item biored:test:635
Example input:
Sentence: The paternal mutation is a G -- > A transition located at the 5 ' donor splice site within intron 51 , designated IVS51 + 1G -- > A .

Example answer:
{"entities": [{"text": "G -- > A", "type": "SequenceVariant"}, {"text": "IVS51 + 1G -- > A", "type": "SequenceVariant"}]}

Example input:
Sentence: Another POF patient of African origin showed a homozygous nucleotide change in the tenth of DMC1 gene that led to an alteration of the amino acid composition of the protein ( M200V ) .

Example answer:
{"entities": [{"text": "POF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "M200V", "type": "SequenceVariant"}]}

Example input:
Sentence: Sequencing of the GJB2 gene showed that the child was heterozygous for a novel nucleotide change , c.263C > T , in exon 2 , leading to a substitution of alanine for valine at position 88 ( p.Ala88Val ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "alanine for valine at position 88", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RT-PCR analysis , performed on a patient homozygous for the intronic deletion ( c.609+28_610-16del ) , failed to detect any GNPTG RNA transcripts .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In 10 of these families , all the homozygotes have a 137-bp insertion in their cDNA caused by a point mutation in a sequence resembling a splice-donor site .

Example answer:
{"entities": [{"text": "137-bp insertion", "type": "SequenceVariant"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Input:
Sentence: RESULTS : Patient 1 had a homozygous G to A nucleotide change at the 5 ' donor splice site of exon/intron 2 .

## Item biored:test:510
Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A recent addition to the list of widely confirmed type 1 diabetes risk loci is the PTPN22 gene encoding a lymphoid-specific phosphatase ( Lyp ) .

Example answer:
{"entities": [{"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "lymphoid-specific phosphatase", "type": "GeneOrGeneProduct"}, {"text": "Lyp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conclude that the SNPs of SLC2A2 predict the conversion to diabetes in obese subjects with IGT .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hepatocyte nuclear factor-6 : associations between genetic variability and type II diabetes and between genetic variability and estimates of insulin secretion .

Example answer:
{"entities": [{"text": "Hepatocyte nuclear factor-6", "type": "GeneOrGeneProduct"}, {"text": "type II diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because polymorphism of CD72 , another inhibitory receptor of B cells , was associated with murine SLE , we identified human CD72 polymorphisms , tested their association with SLE and examined genetic interaction with FCGR2B in the Japanese ( 160 SLE , 277 controls ) , Thais ( 87 SLE , 187 controls ) and Caucasians ( 94 families containing SLE members ) .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "FCGR2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Association between polymorphisms in SLC30A8 , HHEX , CDKN2A/B , IGF2BP2 , FTO , WFS1 , CDKAL1 , KCNQ1 and type 2 diabetes in the Korean population .

## Item biored:test:615
Example input:
Sentence: Analyses of markers associated with the mTOR pathway were carried out on archival tumor from a subgroup using immunohistochemistry ( IHC ) and direct mutation sequencing .

Example answer:
{"entities": [{"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Combination of polymorphisms within 5 ' and 3 ' untranslated regions of thymidylate synthase gene modulates survival in 5 fluorouracil-treated colorectal cancer patients .

Example answer:
{"entities": [{"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "5", "type": "ChemicalEntity"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : The purpose of this study was to analyze the value of germline and tumor thymidylate synthase ( TS ) genotyping as a prognostic marker in a series of colorectal cancer patients receiving adjuvant fluorouracil ( FU ) -based treatment .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil", "type": "ChemicalEntity"}, {"text": "FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Twenty-four of 113 ( 21 % ) gastric cancer patients had the II , 57 ( 51 % ) the ID , and 32 ( 28 % ) the DD genotype .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Tumor thymidylate synthase 1494del6 genotype as a prognostic factor in colorectal cancer patients receiving fluorouracil-based adjuvant treatment .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil-based", "type": "ChemicalEntity"}]}

Example input:
Sentence: VNTR and ins/del 6 bp genotypes varied with tumour anatomical site : 2R/2R genotype was rare in left-sided tumours ( 7.0 % vs. 26.3 % of right-sided and 24.1 % of rectal cancers ; P < 0.01 ) , where the variant allele 6- was very frequent ( 69.0 % ) .

Example answer:
{"entities": [{"text": "ins/del 6 bp", "type": "SequenceVariant"}, {"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumours", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rectal cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Among 619 colorectal cancers in two prospective cohort studies , 233 ( 38 % ) tumors showed VDR overexpression by immunohistochemistry .

## Item biored:test:672
Example input:
Sentence: A total of five SNPs were identified to show the possible association with severe myelosuppression ( P ( Fisher ) < 0.01 ) and were further examined in 7 cases and 20 controls in the second stage of the study .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: For most of the variants identified in the Kenyan and Sudanese study population , a causative association with NSARD appears to be unlikely .

Example answer:
{"entities": [{"text": "NSARD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We therefore examined the associations with AD of the DBH -1021T allele and of the above interactions in the Epistasis Project , with 1757 cases of AD and 6294 elderly controls .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}]}

Example input:
Sentence: Further association was identified in individuals over 40 years of age .

Example answer:
{"entities": []}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: Studies of additional cases yielded a second set of data that , in combination with the first set , confirmed a weak association of UP III SNP7 in VUR ( P= 0.036 adjusted for both subsets of cases vs. controls ) .

Example answer:
{"entities": [{"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Multivariate logistic regression revealed the common haplotypes H1 ( AGACT ) , H2 ( AGAWT ) , and H3 ( AGAWC ) were associated with the persistent postoperative hypertension ( P = .01 , 0.03 , 0.005 after Bonferroni correction ) .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Moreover , this association remained significant after Bonferroni correction .

## Item biored:test:606
Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Complications were observed in two patients : one had a left homonymous hemianopsia after pallidotomy and another one developed left hemiballistic movements 3 days after subthalamotomy which partly improved within 1 month with Valproate 1000 mg/day .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "homonymous hemianopsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: As heroin addicts sometimes faint while using illicit drugs , doctors might attribute too many episodes of syncope to illicit drug use and thereby underestimate the incidence of TdP in this special population , and the high mortality in this population may , in part , be caused by the proarrhythmic effect of methadone .

Example answer:
{"entities": [{"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 61-year-old Japanese man with nephrotic syndrome due to focal segmental glomerulosclerosis was initially responding well to steroid therapy .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal segmental glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Six patients were operated on in the globus pallidus interna ( GPi ) and four in the subthalamic nucleus ( STN ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We present the case of a 31-year-old man with bilateral ischemia of the globus pallidus after excessive alcohol and intranasal cocaine use .

## Item biored:test:552
Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: The slower progression of hearing loss associated with p.D572H , in comparison with that caused by p.D572N , may reflect a correlation of DFNA36 phenotype with TMC1 genotype .

Example answer:
{"entities": [{"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.D572H", "type": "SequenceVariant"}, {"text": "p.D572N", "type": "SequenceVariant"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DiGeorge and Velocardiofacial syndromes ( DGS/VCFS ) are endowed by a similar complex phenotype including cardiovascular , craniofacial , and thymic malformations , and are associated with heterozygous deletions of 22q11 chromosomal band .

Example answer:
{"entities": [{"text": "DiGeorge and Velocardiofacial syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular , craniofacial , and thymic malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We screened affected family members for homozygosity at short-tandem repeats flanking known autosomal recessive ( DFNB ) deafness loci , followed by TMC1 sequence analysis in families segregating deafness linked to DFNB7/B11 .

Example answer:
{"entities": [{"text": "autosomal recessive ( DFNB ) deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Analysis of a nuclear family with three affected offspring identified an autosomal-recessive form of spondyloepimetaphyseal dysplasia characterized by severe short stature and a unique constellation of radiographic findings .

Example answer:
{"entities": [{"text": "spondyloepimetaphyseal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The phenotype of pure monosomy included deafness , duodenal stenosis , developmental and growth delay , vertebral anomalies , and facial dysmorphisms ; the trisomy was manifested by only minor dysmorphisms .

## Item biored:test:649
Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: HBsAg , anti-HBs , anti-HBc , and anti-HIV 1/2 were determined as part of routine diagnosis using Axsym assays ( Abbott Laboratories , North Chicago , IL ) .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "1/2", "type": "OrganismTaxon"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus", "type": "OrganismTaxon"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum samples were PCR amplified with HBV reverse transcriptase ( RT ) primers , followed by direct sequencing across the tyrosine-methionine-aspartate-aspartate ( YMDD ) motif of the major catalytic region in the C domain of the HBV RT enzyme .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: The HBV viral loads for mono-infected and co-infected patients ranged from 3.32 x 10 ( 2 ) to 3.82 x 10 ( 7 ) and < 200 to 4.40 x 10 ( 3 ) copies/ml , respectively .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: HBV viral load was performed with Amplicor HBV Monitor test v2.0 ( Roche Diagnostics , Penzberg , Germany ) .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Input:
Sentence: The load of HBV was determined using an `` in-house '' real-time polymerase chain reaction .

## Item biored:test:556
Example input:
Sentence: We identified 10 new families segregating DFNB7/B11 deafness and TMC1 mutations , including three novel alleles .

Example answer:
{"entities": [{"text": "DFNB7/B11 deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Compared to many other ethnic groups , deafness-associated variants of the coding region of GJB2 are rare in Sudan and Kenya , suggesting a role of other genetic , or epigenetic factors as a cause for deafness in these countries .

Example answer:
{"entities": [{"text": "deafness-associated", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation at the DFNA36 hearing loss locus reveals a critical function and potential genotype-phenotype correlation for amino acid-572 of TMC1 .

Example answer:
{"entities": [{"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also detected p.R34X among normal control samples of African-American and northern European origins , raising the possibility that p.R34X and other mutations of TMC1 are prevalent contributors to the genetic load of deafness across a variety of populations and continents .

Example answer:
{"entities": [{"text": "p.R34X", "type": "SequenceVariant"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Overall , 9 different TMC1 mutations account for deafness in 19 ( 3.4 % ) of the 557 Pakistani families .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A large proportion of non-syndromic autosomal recessive deafness ( NSARD ) in many populations is caused by variants of the GJB2 gene .

Example answer:
{"entities": [{"text": "non-syndromic autosomal recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NSARD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened affected family members for homozygosity at short-tandem repeats flanking known autosomal recessive ( DFNB ) deafness loci , followed by TMC1 sequence analysis in families segregating deafness linked to DFNB7/B11 .

Example answer:
{"entities": [{"text": "autosomal recessive ( DFNB ) deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A single mutation , p.R34X , causes deafness in 10 ( 1.8 % ) of the families .

Example answer:
{"entities": [{"text": "p.R34X", "type": "SequenceVariant"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The slower progression of hearing loss associated with p.D572H , in comparison with that caused by p.D572N , may reflect a correlation of DFNA36 phenotype with TMC1 genotype .

Example answer:
{"entities": [{"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.D572H", "type": "SequenceVariant"}, {"text": "p.D572N", "type": "SequenceVariant"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We previously reported that mutations of transmembrane channel-like gene 1 ( TMC1 ) cause non-syndromic recessive deafness at the DFNB7/B11 locus on chromosome 9q13-q21 in nine Pakistani families .

Example answer:
{"entities": [{"text": "transmembrane channel-like gene 1", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "non-syndromic recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We conclude that AUNA1 deafness does not share a common etiology with deafness associated with monosomy 13q21.2-q31.3 ; deafness may result from monosomy of PCHD9 or another gene in the IT , as has been demonstrated in contiguous gene deletion syndromes .

## Item biored:test:602
Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Targeting IDO itself or the p38 MAPK signaling pathway could provide a novel therapy for comorbid depressive disorders in HIV-1-infected patients .

Example answer:
{"entities": [{"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "p38 MAPK", "type": "GeneOrGeneProduct"}, {"text": "depressive disorders", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HIV-1-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our data do not provide support for rs2230912 or the other polymorphisms studied within the P2RX7 locus , being involved in susceptibility to mood disorders .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Autosomal dominant cerebellar ataxia ( ADCA ) is a group of heterogeneous neurodegenerative disorders .

Example answer:
{"entities": [{"text": "Autosomal dominant cerebellar ataxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast to alleles that cause early-onset MLD , the arginine84 to glutamine substitution is associated with some residual ARSA activity .

Example answer:
{"entities": [{"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine84 to glutamine", "type": "SequenceVariant"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Neither rs2230912 nor any of 8 other SNPs genotyped across P2RX7 was found to be associated with mood disorder in general , nor specifically with bipolar or unipolar disorder .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar or unipolar disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A comparison of genotypes , ARSA activities , and clinical data on 4 individuals carrying the allele of 81 patients with MLD examined , further validates the concept that different degrees of residual ARSA activity are the basis of phenotypical variation in MLD ..

Example answer:
{"entities": [{"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In addition , association of ADORA2A variants with anxiety was replicated for individuals with ASD .

## Item biored:test:512
Example input:
Sentence: Our aim was to study the associations of individual single nucleotide polymorphisms and haplotypes with adiposity , glucose metabolism , and the risk of type 2 diabetes ( T2D ) .

Example answer:
{"entities": [{"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Our results showed substantial evidence of association between -1607 promoter polymorphism of MMP1 and DDD in the Southern Chinese subjects .

Example answer:
{"entities": [{"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because polymorphism of CD72 , another inhibitory receptor of B cells , was associated with murine SLE , we identified human CD72 polymorphisms , tested their association with SLE and examined genetic interaction with FCGR2B in the Japanese ( 160 SLE , 277 controls ) , Thais ( 87 SLE , 187 controls ) and Caucasians ( 94 families containing SLE members ) .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "FCGR2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The aim of the present study was to investigate the association among the polymorphisms of SLC30A8 , HHEX , CDKN2A/B , IGF2BP2 , FTO , WFS1 , CDKAL1 and KCNQ1 and the risk of T2DM in the Korean population .

## Item biored:test:592
Example input:
Sentence: Medical treatment was initiated at a daily dose of 20 mg paroxetine and 1.2 mg alprazolam .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: PURPOSE : We present a case of a patient who developed seizures shortly after initiating treatment with levofloxacin and to discuss the potential drug-drug interactions related to the inhibition of cytochrome P450 ( CYP ) 1A2 in this case , as well as in other cases , of levofloxacin-induced seizures .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levofloxacin", "type": "ChemicalEntity"}, {"text": "cytochrome P450 ( CYP ) 1A2", "type": "GeneOrGeneProduct"}, {"text": "levofloxacin-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Co-administration of lidocaine with desipramine reversed the changes of convulsive activity of lidocaine and cocaine induced by repeated administration of desipramine .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "desipramine", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Daily administration of desipramine , an inhibitor of the NET , for 5 days decreased [ ( 3 ) H ] norepinephrine uptake in the P2 fractions of hippocampus but not cortex , striatum or amygdalae .

Example answer:
{"entities": [{"text": "desipramine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The authors report here a depressed patient comorbid with postprandial dyspepsia who developed RLS after mirtazapine had been added to his domperidone therapy .

Example answer:
{"entities": [{"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "postprandial dyspepsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mirtazapine", "type": "ChemicalEntity"}, {"text": "domperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Also , the multichannel blockers Amiodarone , Paroxetine , Terfenadine and Citalopram prolonged FPDc in a concentration dependent manner .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "Paroxetine", "type": "ChemicalEntity"}, {"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}]}

Example input:
Sentence: This patient presented with symptoms of neuroleptic malignant syndrome ( NMS ) , thus demonstrating that NMS-like symptoms can occur after combined paroxetine and alprazolam treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: Possible neuroleptic malignant syndrome related to concomitant treatment with paroxetine and alprazolam .

Example answer:
{"entities": [{"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the 10th day of paroxetine and alprazolam treatment , the patient exhibited marked psychomotor retardation , disorientation , and severe muscle rigidity with tremors .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tremors", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A MEDLINE search ( 1966-January 2009 ) revealed one in vivo pharmacokinetic study on the interaction between flecainide , a CYP2D6 substrate , and paroxetine , a CYP2D6 inhibitor , as well as 3 case reports of flecainide-induced delirium .

## Item biored:test:610
Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in PDE6H and in KCNV2 have been described in CDSRR .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Our results suggest that the PI3-kinase gene Met326Ile polymorphism may not be a major determinant for the development of PCOS , but it may modulate the concentrations of serum 17-OHP or free testosterone in PCOS patients .

Example answer:
{"entities": [{"text": "PI3-kinase", "type": "GeneOrGeneProduct"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "PCOS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "17-OHP", "type": "ChemicalEntity"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : About 10-15 % of adult , and most pediatric , gastrointestinal stromal tumors ( GIST ) lack mutations in KIT , PDGFRA , SDHx , or RAS pathway components ( KRAS , BRAF , NF1 ) .

Example answer:
{"entities": [{"text": "gastrointestinal stromal tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KIT", "type": "GeneOrGeneProduct"}, {"text": "PDGFRA", "type": "GeneOrGeneProduct"}, {"text": "SDHx", "type": "GeneOrGeneProduct"}, {"text": "RAS", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Phosphatidylinositol 3-kinase p85alpha regulatory subunit gene Met326Ile polymorphism in women with polycystic ovary syndrome .

Example answer:
{"entities": [{"text": "Phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "p85alpha", "type": "GeneOrGeneProduct"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "polycystic ovary syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found that the E333D mutation neither significantly affected the affinity of the receptor for T3 nor modified heterodimer formation with retinoid X receptor ( RXR ) when bound to DNA .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "T3", "type": "ChemicalEntity"}, {"text": "retinoid X receptor", "type": "GeneOrGeneProduct"}, {"text": "RXR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Vitamin D receptor expression is associated with PIK3CA and KRAS mutations in colorectal cancer .

## Item biored:test:611
Example input:
Sentence: Cisplatin-treated DCs down-regulated the expression of cell surface molecules ( CD80 , CD86 , MHC class I and II ) and up-regulated endocytic capacity in a dose-dependent manner .

Example answer:
{"entities": [{"text": "Cisplatin-treated", "type": "ChemicalEntity"}, {"text": "CD80", "type": "GeneOrGeneProduct"}, {"text": "CD86", "type": "GeneOrGeneProduct"}, {"text": "MHC class I and II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recently , we have shown that moderate diet restriction remarkably protects against doxorubicin-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have shown that the oncoprotein gankyrin is critical for inflammation-induced tumorigenesis in the colon .

Example answer:
{"entities": [{"text": "oncoprotein", "type": "GeneOrGeneProduct"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "inflammation-induced", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The high expression of FASN is considered a promising molecular target for colon cancer therapy .

Example answer:
{"entities": [{"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Lifelong administration of vitamin E to Hp 2-2 DM individuals in the Kaiser population would increase their life expectancy by 3 years .

Example answer:
{"entities": [{"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Liver metastases from colorectal cancer ( CRC ) are a clinically significant problem .

Example answer:
{"entities": [{"text": "Liver metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Vitamin E reduces cardiovascular disease in individuals with diabetes mellitus and the haptoglobin 2-2 genotype .

Example answer:
{"entities": [{"text": "Vitamin E", "type": "ChemicalEntity"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "haptoglobin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Meta-analysis of the two trials demonstrated a significant overall reduction in the composite end point in Hp 2-2 DM individuals with vitamin E ( odds ratio : 0.58 ; 95 % CI : 0.40-0.86 ; p = 0.006 ) .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results suggested that emodin-regulated cell growth and apoptosis were mediated by inhibiting FASN and provide a molecular basis for colon cancer therapy .

Example answer:
{"entities": [{"text": "emodin-regulated", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Vitamin D is associated with decreased risks of various cancers , including colon cancer .

## Item biored:test:663
Example input:
Sentence: Thirty-six nonobese subjects with schizophrenia or schizoaffective disorder , matched by body mass index and treated with either clozapine , olanzapine , or risperidone , were included in the analysis .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "schizoaffective disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Several studies have suggested that the regulator of G-protein signaling 4 ( RGS4 ) may be a positional and functional candidate gene for schizophrenia .

Example answer:
{"entities": [{"text": "regulator of G-protein signaling 4", "type": "GeneOrGeneProduct"}, {"text": "RGS4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among these three SNPs , neither SNP4 , SNP7 , SNP18 has shown significant association with schizophrenia in single locus association analysis , nor any compositions of the three SNP haplotypes has shown significantly associations with the DSM-IV diagnosed schizophrenia .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted an association study assessing how PD risk in Italy was influenced by the serotonin transporter gene ( SLC6A4 ) polymorphic region 5-HTTLPR , consisting of an insertion/deletion ( long allele-L/short allele-S ) of 43 bp in the SLC6A4 promoter region .

Example answer:
{"entities": [{"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "insertion/deletion ( long allele-L/short allele-S ) of 43 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: BACKGROUND : While the incidence of new-onset diabetes mellitus may be increasing in patients with schizophrenia treated with certain atypical antipsychotic agents , it remains unclear whether atypical agents are directly affecting glucose metabolism or simply increasing known risk factors for diabetes .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antipsychotic agents", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The brain neurotransmitter 5-hydroxytryptamine ( 5-HT ; serotonin ) is involved in nociceptive pathways and has been implicated in the pathophysiology of migraine .

Example answer:
{"entities": [{"text": "neurotransmitter", "type": "ChemicalEntity"}, {"text": "5-hydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serotonin transporter gene polymorphic element 5-HTTLPR increases the risk of sporadic Parkinson 's disease in Italy .

Example answer:
{"entities": [{"text": "Serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because 5-HT transporters play a key element in the regulation of synaptic 5-HT transmission it may be important to control for the potential covariance effect of a polymorphism in the 5-HT transporter promoter gene region ( 5-HTTLPR ) when studying the effects of MDMA as well as cognitive functioning .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HT transporter promoter gene region", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND : Altered serotonergic neural transmission is hypothesized to be a susceptibility factor for psychotic disorders such as schizophrenia .

## Item biored:test:644
Example input:
Sentence: Affected children have a high serum T3 : T4 ratio and variable degrees of intellectual deficit and constipation but exhibit a consistently severe skeletal dysplasia .

Example answer:
{"entities": [{"text": "T3", "type": "ChemicalEntity"}, {"text": "T4", "type": "ChemicalEntity"}, {"text": "intellectual deficit", "type": "DiseaseOrPhenotypicFeature"}, {"text": "constipation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hemoglobin", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaundice", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Intracerebral hemorrhage ( ICH ) is a devastating disease without effective treatment .

Example answer:
{"entities": [{"text": "Intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anemia and hepatitis often occur within 12 weeks of initiating generic HAART .

Example answer:
{"entities": [{"text": "Anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alternatively , anemia could result from accelerated suicidal erythrocyte death or eryptosis , which is characterized by exposure of phosphatidylserine ( PS ) at the erythrocyte surface and by cell shrinkage .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "phosphatidylserine", "type": "ChemicalEntity"}, {"text": "PS", "type": "ChemicalEntity"}]}

Example input:
Sentence: INTERPRETATION AND CONCLUSIONS : Taken together with the previous report , 5 of our 12 patients with hemochromatosis manifesting in middle age had mutations in the TfR2 gene .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TfR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In an attempt to improve developmental delay and alleviate symptoms of hypothyroidism , patients are receiving varying doses and durations of T4 treatment , but responses have been inconsistent so far .

Example answer:
{"entities": [{"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypothyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "T4", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with RTH are usually euthyroid but can occasionally present with signs and symptoms of thyrotoxicosis or rarely with hypothyroidism .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thyrotoxicosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypothyroidism", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: First described by Zinn et al in 1986 , deficiency of FH results in early onset , severe encephalopathy .

Example answer:
{"entities": [{"text": "deficiency of FH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Moreover , diagnosis of central hypothyroidism should be considered in the face of severe infant anemia of uncertain etiology .

## Item biored:test:651
Example input:
Sentence: To the best of our knowledge , this constitutes the first report of HBV lamivudine-resistant strains in therapy-na ve HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PATIENTS AND METHODS : Six unrelated families and 10 sporadic patients were examined clinically .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Included were 5,128 CL/P cases , 1,745 CPO cases , and 3,712 controls ( like-sexed , non-malformed liveborn infant , born immediately after a malformed one , in the same hospital ) , over 4,199,630 consecutive births .

Example answer:
{"entities": [{"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : One hundred and fifty-eight patients with wet AMD , 80 patients with soft drusen , and 220 matched control subjects were recruited among Han Chinese in mainland China .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thirty-five lamivudine-na ve HBV infected patients with or without HIV co-infection were studied : 15 chronic HBV mono-infected patients and 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "HBV infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV mono-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Twenty-eight patients with co-infection were identified .

## Item biored:test:643
Example input:
Sentence: PURPOSE : The purpose of this study was to analyze the value of germline and tumor thymidylate synthase ( TS ) genotyping as a prognostic marker in a series of colorectal cancer patients receiving adjuvant fluorouracil ( FU ) -based treatment .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil", "type": "ChemicalEntity"}, {"text": "FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , the main outcome measure was the sequencing of genomic DNA from peripheral blood samples of 41 women with POF and 36 fertile women ( controls ) .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : To describe clinical and genetic features of a Thai family with non-autoimmune hyperthyroidism ( NAH ) caused by an activating germline mutation in the thyrotropin receptor ( TSHR ) gene .

Example answer:
{"entities": [{"text": "non-autoimmune hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thyrotropin receptor", "type": "GeneOrGeneProduct"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: First described by Zinn et al in 1986 , deficiency of FH results in early onset , severe encephalopathy .

Example answer:
{"entities": [{"text": "deficiency of FH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Resistance to thyroid hormone ( RTH ) is an inherited syndrome characterized by elevated serum thyroid hormones ( TH ) , failure to suppress pituitary thyroid stimulating hormone ( TSH ) secretion , and variable peripheral tissue responsiveness to TH .

Example answer:
{"entities": [{"text": "Resistance to thyroid hormone", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thyroid hormones", "type": "ChemicalEntity"}, {"text": "TH", "type": "ChemicalEntity"}, {"text": "thyroid stimulating hormone", "type": "GeneOrGeneProduct"}, {"text": "TSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Resistance to thyroid hormone syndrome ( RTH ) is a rare disorder , usually inherited as an autosomal dominant trait .

Example answer:
{"entities": [{"text": "Resistance to thyroid hormone syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Biochemical tests showed elevated free thyroxine ( T4 : 20.8 pg/ml ( normal , 8.5-18 ) ) and triiodothyronine ( T3 : 5.7 pg/ml ( normal , 1.4-4 ) ) in the serum , together with an inappropriately nonsuppressed TSH level of 4.7 mU/ml ( normal , 0.4-4 ) .

Example answer:
{"entities": [{"text": "thyroxine", "type": "ChemicalEntity"}, {"text": "T4", "type": "ChemicalEntity"}, {"text": "triiodothyronine", "type": "ChemicalEntity"}, {"text": "T3", "type": "ChemicalEntity"}, {"text": "TSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: GENETIC ANALYSIS : Genomic DNA was extracted from peripheral blood leukocytes and mutation analysis of the entire coding sequence of the TSHR gene was performed in both children and their parents by direct DNA sequencing .

Example answer:
{"entities": [{"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new genetic disorder has been identified that results from mutation of THRA , encoding thyroid hormone receptor a1 ( TRa1 ) .

Example answer:
{"entities": [{"text": "THRA", "type": "GeneOrGeneProduct"}, {"text": "thyroid hormone receptor a1", "type": "GeneOrGeneProduct"}, {"text": "TRa1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSIONS : In isolated TSH deficiency , the exact molecular diagnosis is mandatory for diagnosis of isolated pituitary deficiency , delineation of prognosis , and genetic counseling .

## Item biored:test:632
Example input:
Sentence: Expanding clinical spectrum of non-autoimmune hyperthyroidism due to an activating germline mutation , p.M453T , in the thyrotropin receptor gene .

Example answer:
{"entities": [{"text": "non-autoimmune hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.M453T", "type": "SequenceVariant"}, {"text": "thyrotropin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thyroid hormone receptor a mutation causes a severe and thyroxine-resistant skeletal dysplasia in female mice .

Example answer:
{"entities": [{"text": "Thyroid hormone receptor a", "type": "GeneOrGeneProduct"}, {"text": "thyroxine-resistant", "type": "ChemicalEntity"}, {"text": "skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , in transient transfection assays , the E333D TRbeta mutant exhibited impaired transcriptional regulation on two distinct positively regulated thyroid response elements ( F2- and DR4-TREs ) as well as on the negatively regulated human TSHalpha promoter .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "TSHalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new genetic disorder has been identified that results from mutation of THRA , encoding thyroid hormone receptor a1 ( TRa1 ) .

Example answer:
{"entities": [{"text": "THRA", "type": "GeneOrGeneProduct"}, {"text": "thyroid hormone receptor a1", "type": "GeneOrGeneProduct"}, {"text": "TRa1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report a novel natural RTH mutation ( E333D ) located in the large carboxy-terminal ligand binding domain of TRbeta .

Example answer:
{"entities": [{"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The disorder is associated with diverse mutations in the thyroid hormone beta receptor ( TRbeta ) .

Example answer:
{"entities": [{"text": "thyroid hormone beta receptor", "type": "GeneOrGeneProduct"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Affected individuals are usually heterozygous for mutations in the thyroid hormone receptor beta gene ( TR-beta ) .

Example answer:
{"entities": [{"text": "thyroid hormone receptor beta", "type": "GeneOrGeneProduct"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation ( E333D ) in the thyroid hormone beta receptor causing resistance to thyroid hormone syndrome .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "thyroid hormone beta receptor", "type": "GeneOrGeneProduct"}, {"text": "resistance to thyroid hormone syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Two novel mutations of the TSH-beta subunit gene underlying congenital central hypothyroidism undetectable in neonatal TSH screening .

## Item biored:test:648
Example input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hemoglobin", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaundice", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: The search for HbF-associated polymorphisms ( such as the XmnI , BCL11A and MYB polymorphisms ) has recently gained great attention , in order to stratify b-thalassemia patients with respect to expectancy of the first transfusion , need for annual intake of blood , response to HbF inducers ( the most studied of which is hydroxyurea ) .

Example answer:
{"entities": [{"text": "HbF-associated", "type": "GeneOrGeneProduct"}, {"text": "BCL11A", "type": "GeneOrGeneProduct"}, {"text": "MYB", "type": "GeneOrGeneProduct"}, {"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HbF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Patients Fifty subjects signed informed consent and 41 underwent the frequently sampled intravenous glucose tolerance test .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : In this cross-sectional study interview , ECGs and blood samples were collected in a population of adult heroin addicts treated with methadone or buprenorphine on a daily basis .

Example answer:
{"entities": [{"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "buprenorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Serum samples were collected from cirrhotic potential liver transplant patients ( LTx ) with ( n=61 ) and without HCC ( n=78 ) as well as from healthy controls ( HCs ; n=39 ) .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Blood sampling , karyotype , hormonal dosage , ultrasound , and ovarian biopsy were carried out on most patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The latter group was further sub-divided into 13 occult HBV ( HBsAg-negative ) and 7 overt HBV ( HBsAg- positive ) patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "HBsAg-negative", "type": "ChemicalEntity"}, {"text": "HBsAg-", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: HBsAg , anti-HBs , anti-HBc , and anti-HIV 1/2 were determined as part of routine diagnosis using Axsym assays ( Abbott Laboratories , North Chicago , IL ) .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "1/2", "type": "OrganismTaxon"}]}

Input:
Sentence: Patients provided blood samples for HBsAg detection .

## Item biored:test:661
Example input:
Sentence: Both the precordial pain and the electrocardiographic changes disappeared spontaneously after the discontinuation of 5-FU .

Example answer:
{"entities": [{"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : Markers of fibrinolysis , thrombin-activatable fibrinolysis inhibitor ( TAFI ) , tissue-type plasminogen activator ( tPA ) , and plasminogen activator inhibitor-1 ( PAI-1 ) levels were studied for the evaluation of short-term effects of raloxifene administration in postmenopausal women .

Example answer:
{"entities": [{"text": "thrombin-activatable fibrinolysis inhibitor", "type": "GeneOrGeneProduct"}, {"text": "TAFI", "type": "GeneOrGeneProduct"}, {"text": "tissue-type plasminogen activator", "type": "GeneOrGeneProduct"}, {"text": "tPA", "type": "GeneOrGeneProduct"}, {"text": "plasminogen activator inhibitor-1", "type": "GeneOrGeneProduct"}, {"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "raloxifene", "type": "ChemicalEntity"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolongation of the QT interval in the ECG of patients with torsade de pointes ( TdP ) has been reported in methadone users .

Example answer:
{"entities": [{"text": "Prolongation of the QT interval", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "torsade de pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Flow cytometry experiments confirmed that the transfectants ' diminished resistance to DOX was caused by increased drug accumulation induced by the exogenous Rab6c .

Example answer:
{"entities": [{"text": "DOX", "type": "ChemicalEntity"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Finally , the IKr blockers , Terfenadine and Citalopram , which are reported to cause Torsade de Pointes ( TdP ) in clinical practice , produced early afterdepolarization ( EAD ) .

Example answer:
{"entities": [{"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}, {"text": "Torsade de Pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We propose that the alteration in the replication/nuclear location pattern of the non-deleted TDR22 indicates an altered gene regulation hence an altered transcritpion in DGS/VCFS .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Three months of raloxifene treatment was associated with a significant decrease in the plasma TAFI antigen concentrations ( 16 % change , P < 0.01 ) , and a significant increase in tPA antigen concentrations ( 25 % change , P < 0.05 ) .

Example answer:
{"entities": [{"text": "raloxifene", "type": "ChemicalEntity"}, {"text": "TAFI", "type": "GeneOrGeneProduct"}, {"text": "tPA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: No putative TDF resistance change was detected after prolonged use of TDF .

## Item biored:test:647
Example input:
Sentence: METHODS : This study included 133 patients with AVSD and 200 healthy controls .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A total of 484 recurrence cases and 484 controls were matched on age , race , and pathologic stage and grade .

Example answer:
{"entities": []}

Example input:
Sentence: To determine whether the risk of HIV seroconversion among daily smokers of crack cocaine changed over time , we used Cox proportional hazards regression and divided the study into 3 periods : May 1 , 1996-Nov. 30 , 1999 ( period 1 ) , Dec. 1 , 1999-Nov. 30 , 2002 ( period 2 ) , and Dec. 1 , 2002-Dec. 30 , 2005 ( period 3 ) .

Example answer:
{"entities": [{"text": "HIV seroconversion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crack cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: We therefore conducted a case-control study with 515 incident lung cancer cases and 1030 age- and sex-matched controls without cancer , and further conducted a meta-analysis .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus", "type": "OrganismTaxon"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We analysed data from 23,868 men with prostate cancer and 23,051 controls from 25 studies within the international PRACTICAL Consortium .

Example answer:
{"entities": [{"text": "men", "type": "OrganismTaxon"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine the incidence of clinically significant adverse events after long-term , fixed-dose , generic highly active antiretroviral therapy ( HAART ) use among HIV-infected individuals in South India , we examined the experiences of 3154 HIV-infected individuals who received a minimum of 3 months of generic HAART between February 1996 and December 2006 at a tertiary HIV care referral center in South India .

Example answer:
{"entities": [{"text": "HIV-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thirty-five lamivudine-na ve HBV infected patients with or without HIV co-infection were studied : 15 chronic HBV mono-infected patients and 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "HBV infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV mono-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Input:
Sentence: A cross-sectional study of 847 patients with HIV was conducted .

## Item biored:test:659
Example input:
Sentence: Flow cytometry experiments confirmed that the transfectants ' diminished resistance to DOX was caused by increased drug accumulation induced by the exogenous Rab6c .

Example answer:
{"entities": [{"text": "DOX", "type": "ChemicalEntity"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: A 70 % reduction in Wnt signaling was also observed in the SF188 and SJ-GBM2 UCHL1 knockdowns ( KDs ) using a TCF-dependent TOPflash reporter assay .

Example answer:
{"entities": [{"text": "Wnt", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "TCF-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the WFS1 gene of these patients , we identified a novel mutation , a nine nucleotide insertion ( AFF344-345ins ) .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "nine nucleotide insertion", "type": "SequenceVariant"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}]}

Example input:
Sentence: Sequence analysis of the VWF gene from two unrelated type 2A VWD patients showed an identical , novel , heterozygous T -- > G transversion at nucleotide 4508 , resulting in the substitution of L1503R in the VWF A2 domain .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "type 2A VWD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "T -- > G transversion at nucleotide 4508", "type": "SequenceVariant"}, {"text": "L1503R", "type": "SequenceVariant"}]}

Example input:
Sentence: The protective role of mangiferin was analyzed by triphenyl tetrazolium chloride ( TTC ) test used for macroscopic enzyme mapping assay of the ischemic myocardium .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "triphenyl tetrazolium chloride", "type": "ChemicalEntity"}, {"text": "TTC", "type": "ChemicalEntity"}, {"text": "ischemic myocardium", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we show that the candidate gene HIRA/Tuple1 mapping on the non-deleted TDR22 , in DGS/VCFS subjects presents a delayed replication timing .

Example answer:
{"entities": [{"text": "HIRA/Tuple1", "type": "GeneOrGeneProduct"}, {"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This substitution , which was not found in 60 unrelated normal individuals , was introduced into a full-length VWF cDNA and subsequently expressed in 293T cells .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: We propose that the alteration in the replication/nuclear location pattern of the non-deleted TDR22 indicates an altered gene regulation hence an altered transcritpion in DGS/VCFS .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: No putative TDF resistance substitution was detected .

## Item biored:test:656
Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recent data highlight the presence , in HIV-1-seropositive patients with lymphoma , of p17 variants ( vp17s ) endowed with B-cell clonogenicity , suggesting a role of vp17s in lymphomagenesis .

Example answer:
{"entities": [{"text": "HIV-1-seropositive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "lymphomagenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: The patient showed an R227Q mutation that has been described in an Asian population and MPH patients , along with a novel frameshift mutation , Tdel219 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "R227Q", "type": "SequenceVariant"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Tdel219", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we report a novel natural RTH mutation ( E333D ) located in the large carboxy-terminal ligand binding domain of TRbeta .

Example answer:
{"entities": [{"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations of MKS3/TMEM67 , found recently in Meckel-Gruber syndrome ( MKS ) type 3 and Joubert syndrome ( JBTS ) type 6 , are predominantly truncating mutations .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "Meckel-Gruber syndrome ( MKS ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome ( JBTS ) type 6", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Three CYP17 gene mutations were identified from these patients .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: This pattern and an accompanying rtV173L mutation was found in four patients .

## Item biored:test:622
Example input:
Sentence: Mice subjected to hypotensive episodes showed a significant decrease in latency time ( 178 +/- 156 s ) compared with those injected with saline , NTG + NIMO , or delayed NTG ( 580 +/- 81 s , 557 +/- 67 s , and 493 +/- 146 s , respectively ) .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Maximal contraction to norepinephrine was modestly reduced in arteries from LNNA compared with control rats whereas the maximum contraction to ET-1 was significantly reduced ( 54 % control ) .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Prolonged hypothermia as a bridge to recovery for cerebral edema and intracranial hypertension associated with fulminant hepatic failure .

Example answer:
{"entities": [{"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Phenylephrine but not ephedrine reduces frontal lobe oxygenation following anesthesia-induced hypotension .

## Item biored:test:633
Example input:
Sentence: Takotsubo syndrome ( TS ) , also known as broken heart syndrome , is characterized by left ventricle apical ballooning with elevated cardiac biomarkers and electrocardiographic changes suggestive of an acute coronary syndrome ( ie , ST-segment elevation , T wave inversions , and pathologic Q waves ) .

Example answer:
{"entities": [{"text": "Takotsubo syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "broken heart syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute coronary syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , in transient transfection assays , the E333D TRbeta mutant exhibited impaired transcriptional regulation on two distinct positively regulated thyroid response elements ( F2- and DR4-TREs ) as well as on the negatively regulated human TSHalpha promoter .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "TSHalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new genetic disorder has been identified that results from mutation of THRA , encoding thyroid hormone receptor a1 ( TRa1 ) .

Example answer:
{"entities": [{"text": "THRA", "type": "GeneOrGeneProduct"}, {"text": "thyroid hormone receptor a1", "type": "GeneOrGeneProduct"}, {"text": "TRa1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In an attempt to improve developmental delay and alleviate symptoms of hypothyroidism , patients are receiving varying doses and durations of T4 treatment , but responses have been inconsistent so far .

Example answer:
{"entities": [{"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypothyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "T4", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVE : To describe clinical and genetic features of a Thai family with non-autoimmune hyperthyroidism ( NAH ) caused by an activating germline mutation in the thyrotropin receptor ( TSHR ) gene .

Example answer:
{"entities": [{"text": "non-autoimmune hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thyrotropin receptor", "type": "GeneOrGeneProduct"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation ( E333D ) in the thyroid hormone beta receptor causing resistance to thyroid hormone syndrome .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "thyroid hormone beta receptor", "type": "GeneOrGeneProduct"}, {"text": "resistance to thyroid hormone syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The disorder is associated with diverse mutations in the thyroid hormone beta receptor ( TRbeta ) .

Example answer:
{"entities": [{"text": "thyroid hormone beta receptor", "type": "GeneOrGeneProduct"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Affected individuals are usually heterozygous for mutations in the thyroid hormone receptor beta gene ( TR-beta ) .

Example answer:
{"entities": [{"text": "thyroid hormone receptor beta", "type": "GeneOrGeneProduct"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONTEXT : Patients with TSH-beta subunit defects and congenital hypothyroidism are missed by TSH-based neonatal screening .

## Item biored:test:690
Example input:
Sentence: MC is clinically distinct from other multiple exostosis or multiple enchondromatosis syndromes and is unlinked to EXT1 and EXT2 , the genes responsible for autosomal dominant multiple osteochondromas ( MO ) .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple exostosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple enchondromatosis syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EXT1", "type": "GeneOrGeneProduct"}, {"text": "EXT2", "type": "GeneOrGeneProduct"}, {"text": "multiple osteochondromas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : LAT and HAT groups were matched in age , obesity , insulin , and glucose , and had similar expression of insulin-related genes ( InsR , IRS-1 ) .

Example answer:
{"entities": [{"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "insulin-related", "type": "GeneOrGeneProduct"}, {"text": "InsR", "type": "GeneOrGeneProduct"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Reversible inferior colliculus lesion in metronidazole-induced encephalopathy : magnetic resonance findings on diffusion-weighted and fluid attenuated inversion recovery imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Volumetric BMD of the ultradistal radius was measured using peripheral quantitative computed tomography , and areal BMD of the lumbar spine was estimated using dual-energy x-ray absorptiometry .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSION : Taken together , the profile of C5L2 receptor , ASP gene expression and metabolic factors in adipose tissue from morbidly obese HAT subjects suggests a compensatory response associated with the increased plasma ASP and TG .

Example answer:
{"entities": [{"text": "C5L2", "type": "GeneOrGeneProduct"}, {"text": "ASP", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TG", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Subcutaneous ( SC ) and omental ( OM ) adipose tissues ( n = 21 ) were analysed by microarray , and biologic pathways in lipid metabolism and inflammation were specifically examined .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Absence of mechanical adipose tissue in the orbits and scalp was revealed by head magnetic resonance imaging .

## Item biored:test:624
Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Inhibition of Na ( + ) channels by local anesthetics may regulate desipramine-induced down-regulation of NET function .

Example answer:
{"entities": [{"text": "Na ( + )", "type": "ChemicalEntity"}, {"text": "anesthetics", "type": "ChemicalEntity"}, {"text": "desipramine-induced", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The extent of hypotension and changes in brain tissue oxygenation ( PbtO ( 2 ) ) and in cerebral blood flow were studied in a separate group of animals .

Example answer:
{"entities": [{"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Down-regulation of norepinephrine transporter function induced by chronic administration of desipramine linking to the alteration of sensitivity of local-anesthetics-induced convulsions and the counteraction by co-administration with local anesthetics .

Example answer:
{"entities": [{"text": "norepinephrine transporter", "type": "GeneOrGeneProduct"}, {"text": "desipramine", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anesthetics", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We describe the effect of phenylephrine and ephedrine on frontal lobe oxygenation ( S ( c ) O ( 2 ) ) following anesthesia-induced hypotension .

## Item biored:test:514
Example input:
Sentence: Significantly lower frequency of SIM2 C-G haplotype ( rs2073601-rs2073416 ) was noticed in individuals with DS ( P value =0.01669 ) and their fathers ( P value=0.01185 ) .

Example answer:
{"entities": [{"text": "SIM2", "type": "GeneOrGeneProduct"}, {"text": "rs2073601-rs2073416", "type": "SequenceVariant"}, {"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SNP rs6235 was not associated with parameters of glucose metabolism .

Example answer:
{"entities": [{"text": "rs6235", "type": "SequenceVariant"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The risk of developing T2D was approximately 2-fold in individuals with genotypes associated with higher 2-hour plasma glucose levels ; the hazard ratios were 2.192 ( p = 0.025 ) for rs2073162-A , 2.191 ( p = 0.027 ) for rs2073163-C , and 1.998 ( p = 0.054 ) for rs1155974-T .

Example answer:
{"entities": [{"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "rs2073162-A", "type": "SequenceVariant"}, {"text": "rs2073163-C", "type": "SequenceVariant"}, {"text": "rs1155974-T", "type": "SequenceVariant"}]}

Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: None of the SNPs or indels were associated with diabetes-related traits or accounted for a previously identified quantitative trait locus on chromosome 13 for fasting serum glucose .

Example answer:
{"entities": [{"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Markers rs2073163 and rs1155794 from haploblock 2 were associated with 2-hour plasma glucose levels in men during the 3-year follow-up .

Example answer:
{"entities": [{"text": "rs2073163", "type": "SequenceVariant"}, {"text": "rs1155794", "type": "SequenceVariant"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Patients were genotyped for rs4704559 , rs10942891 and rs4704560 by allelic discrimination with Taqman assays .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "rs4704559", "type": "SequenceVariant"}, {"text": "rs10942891", "type": "SequenceVariant"}, {"text": "rs4704560", "type": "SequenceVariant"}]}

Input:
Sentence: We genotyped rs13266634 , rs1111875 , rs10811661 , rs4402960 , rs8050136 , rs734312 , rs7754840 and rs2237892 and measured the body weight , body mass index and fasting plasma glucose in all patients and controls .

## Item biored:test:601
Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: Unlike in other populations , rs2274700 and rs1410996 did not show a significant association with AMD in the Chinese population of this study .

Example answer:
{"entities": [{"text": "rs2274700", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neither rs2230912 nor any of 8 other SNPs genotyped across P2RX7 was found to be associated with mood disorder in general , nor specifically with bipolar or unipolar disorder .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar or unipolar disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both minor alleles , adjusted for sex , age , BMI and insulin sensitivity were associated with elevated AUCproinsulin and AUCproinsulin/AUCinsulin ( rs6235 : p ( additive ) model < or= 0.009 , effect sizes 8/8 % , rs6232 : pdominant model < or= 0.01 , effect sizes 10/21 % ) .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "rs6232", "type": "SequenceVariant"}]}

Example input:
Sentence: Our data do not provide support for rs2230912 or the other polymorphisms studied within the P2RX7 locus , being involved in susceptibility to mood disorders .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : This study showed that SNPs rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , but not rs7535263 , rs1410996 , or rs2274700 , in CFH were significantly associated with wet AMD in a mainland Han Chinese population .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "rs7535263", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "rs2274700", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Nominal association with the disorder was observed for rs2236624-CC , and phenotypic variability in ASD symptoms was influenced by rs3761422 , rs5751876 and rs35320474 .

## Item biored:test:699
Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: For this purpose we developed a high-throughput methodology to genotype both normal and deleted alleles using a chip-based matrix-assisted laser desorption-time-of-flight ( MALDI-TOF ) mass spectrometer and Multiplex PCR .

Example answer:
{"entities": []}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also designed a rapid polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) method to analyze the same mutation , amplifying exon 4 and digesting with PstI restriction enzyme .

Example answer:
{"entities": [{"text": "PstI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: High-resolution melting curve analysis ( hrMCA ) has recently been developed as a post-PCR mutation scanning method which enables simple , rapid , cost-effective , and highly sensitive mutation screening of large genes .
