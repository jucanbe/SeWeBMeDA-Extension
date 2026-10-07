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

## Item biored:test:586
Example input:
Sentence: The hazard of developing CAD ( 95 % CI ) associated with initial treatment increased by 2.4-fold ( 1.3-4.3 , P=0.004 ) with glibenclamide ; 2-fold ( 0.9-4.6 , P=0.099 ) with glipizide ; 2.9-fold ( 1.6-5.1 , P=0.000 ) with either , and was unchanged with metformin .

Example answer:
{"entities": [{"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glibenclamide", "type": "ChemicalEntity"}, {"text": "glipizide", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Finally , the IKr blockers , Terfenadine and Citalopram , which are reported to cause Torsade de Pointes ( TdP ) in clinical practice , produced early afterdepolarization ( EAD ) .

Example answer:
{"entities": [{"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}, {"text": "Torsade de Pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "ChemicalEntity"}, {"text": "5-fluorouracil", "type": "ChemicalEntity"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colorectal , breast and head and neck cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: People aged over 75 in atrial fibrillation on warfarin : the rate of major hemorrhage and stroke in more than 500 patient-years of follow-up .

Example answer:
{"entities": [{"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}, {"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient-years", "type": "OrganismTaxon"}]}

Example input:
Sentence: We herein report the case of a 70-year-old man with 5-FU-induced cardiotoxicity , in whom a high serum level of alpha-fluoro-beta-alanine ( FBAL ) was observed .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "5-FU-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fluoro-beta-alanine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Amiodarone represents an effective antiarrhythmic drug for cardioversion of recent-onset atrial fibrillation ( AF ) and maintenance of sinus rhythm .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "antiarrhythmic drug", "type": "ChemicalEntity"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atrial fibrillation following chemotherapy for stage IIIE diffuse large B-cell gastric lymphoma in a patient with myotonic dystrophy ( Steinert 's disease ) .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Steinert 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atrial fibrillation or other cardiac arrhythmias are unusual complications in patients treated with chemotherapy .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We briefly describe two patients suffering from recent-onset atrial fibrillation , who experienced an acute devastating low back pain a few minutes after initiation of intravenous amiodarone loading .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low back pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amiodarone", "type": "ChemicalEntity"}]}

Example input:
Sentence: PARTICIPANTS : Two hundred thirty-five patients aged 76 and older admitted to a major healthcare network between July 1 , 2001 , and June 30 , 2002 , with atrial fibrillation on warfarin were enrolled .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Input:
Sentence: Flecainide had been started 2 weeks prior for atrial fibrillation .

## Item biored:test:568
Example input:
Sentence: Lack of association between ADRA2B-4825 gene insertion/deletion polymorphism and migraine in Chinese Han population .

Example answer:
{"entities": [{"text": "ADRA2B-4825", "type": "GeneOrGeneProduct"}, {"text": "gene insertion/deletion", "type": "SequenceVariant"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate the association of DNA polymorphisms within steroid synthesis genes ( CYP11B2 , CYP11B1 ) and the postoperative resolution of hypertension in Chinese patients undergoing adrenalectomy for aldosterone-producing adenomas ( APA ) .

Example answer:
{"entities": [{"text": "steroid synthesis genes", "type": "GeneOrGeneProduct"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "aldosterone-producing adenomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : AA genotype of A 1166C polymorphism was associated with lower minimal systolic blood pressure ( SBP ) and diastolic blood pressure ( DBP ) during HUT compared with other genotypes ( minimal SBP : AA 59.6+/-21,8 , AC 79.9+/-22.7 , CC 65.4+/-22.7 mmHg , P=0.007 ) , ( minimal DBP : AA 36.4+/-22.7 , AC 52.3+/-22.9 , CC 45.4+/-19.5 mmHg , P=0.007 ) .AA genotype was also associated with higher SDNN compared to other genotypes in the early phase of HUT ( SDNN in 5 minutes of tilt : AA 59.7+/-24.6 , AC 50.6+/-20.6 , CC 46.0+/-13.2 , P=0.01 ) and at syncope occurrence ( SDNN : AA 71.0+/-20.9 , AC 58.2+/-17.9 , CC 58+/-10 , P=0.04 ) CONCLUSION : AA genotype of A 1166C polymorphism in the ATR1 gene may be associated with hypotension and decline in sympathetic tone during HUT .

Example answer:
{"entities": [{"text": "A 1166C", "type": "SequenceVariant"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Renal angiotensin II receptor type 2 ( AT2R ) gene expression in adult offspring was reduced by PCE , whereas the renal angiotensin II receptor type 1a ( AT1aR ) /AT2R expression ratio was increased .

Example answer:
{"entities": [{"text": "angiotensin II receptor type 2", "type": "GeneOrGeneProduct"}, {"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "angiotensin II receptor type 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1aR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The objective of the present study was to examine the association of the T704C polymorphism of exon 2 of the angiotensinogen ( AGT ) gene with HCM in a South Indian population from Andhra Pradesh .

Example answer:
{"entities": [{"text": "T704C", "type": "SequenceVariant"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "AGT", "type": "GeneOrGeneProduct"}, {"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : In the present study , we aimed to substantiate the putative significance of angiotensin I-converting enzyme ( ACE ) on gastric cancer biology by investigating the influence of its gene polymorphism on gastric cancer progression .

Example answer:
{"entities": [{"text": "angiotensin I-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The M235T polymorphism of the angiotensinogen gene in South Indian patients of hypertrophic cardiomyopathy .

Example answer:
{"entities": [{"text": "M235T", "type": "SequenceVariant"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Angiotensin converting enzyme gene polymorphism in Turkish asthmatic patients .

## Item biored:test:577
Example input:
Sentence: An increased representation of the PNP AA genotype was observed in AD patients with fast cognitive deterioration in comparison with that from patients with slow deterioration rate .

Example answer:
{"entities": [{"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive deterioration", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The risk for type 2 diabetes in the AA genotype carriers was increased in the control group ( 5.56 [ 1.78-17.39 ] , P = 0.003 ) but not in the intervention group .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We therefore examined the associations with AD of the DBH -1021T allele and of the above interactions in the Epistasis Project , with 1757 cases of AD and 6294 elderly controls .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}]}

Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the application of this high-throughput genotyping method , negative results from the two-stage DNA pooling design used to screen loci within the TPH , AADC and MAOA genes did not support their role in migraine susceptibility .

Example answer:
{"entities": [{"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The distribution of the ACE genotypes did not differ significantly from the control group of 189 patients without gastric cancer .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : AA genotype of A 1166C polymorphism was associated with lower minimal systolic blood pressure ( SBP ) and diastolic blood pressure ( DBP ) during HUT compared with other genotypes ( minimal SBP : AA 59.6+/-21,8 , AC 79.9+/-22.7 , CC 65.4+/-22.7 mmHg , P=0.007 ) , ( minimal DBP : AA 36.4+/-22.7 , AC 52.3+/-22.9 , CC 45.4+/-19.5 mmHg , P=0.007 ) .AA genotype was also associated with higher SDNN compared to other genotypes in the early phase of HUT ( SDNN in 5 minutes of tilt : AA 59.7+/-24.6 , AC 50.6+/-20.6 , CC 46.0+/-13.2 , P=0.01 ) and at syncope occurrence ( SDNN : AA 71.0+/-20.9 , AC 58.2+/-17.9 , CC 58+/-10 , P=0.04 ) CONCLUSION : AA genotype of A 1166C polymorphism in the ATR1 gene may be associated with hypotension and decline in sympathetic tone during HUT .

Example answer:
{"entities": [{"text": "A 1166C", "type": "SequenceVariant"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The DD ACE genotype was significantly more frequent in asthmatics compared with controls ( p < 0.001 ) .

## Item biored:test:589
Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doses were flexibly titrated up to 0.6 mg/day for clonidine and 60 mg/day for methylphenidate ( both with divided dosing ) .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "methylphenidate", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The hazard decreased 0.3-fold ( 0.7-1.7 , P=0.385 ) with glimepiride , 0.4-fold ( 0.7-1.3 , P=0.192 ) with gliclazide , and 0.4-fold ( 0.7-1.1 , P=0.09 ) with either .

Example answer:
{"entities": [{"text": "glimepiride", "type": "ChemicalEntity"}, {"text": "gliclazide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Optimal control of the absences was achieved with sodium valproate , lamotrigine , or ethosuximide alone or in combination .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "ChemicalEntity"}, {"text": "lamotrigine", "type": "ChemicalEntity"}, {"text": "ethosuximide", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Etoricoxib 90 mg demonstrated a significantly lower risk for discontinuing treatment due to GI AEs compared with diclofenac 150 mg. Discontinuations from renovascular AEs , although less common than discontinuations from GI AEs , were significantly higher with etoricoxib .

Example answer:
{"entities": [{"text": "Etoricoxib", "type": "ChemicalEntity"}, {"text": "GI AEs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "etoricoxib", "type": "ChemicalEntity"}]}

Example input:
Sentence: The cumulative discontinuation rate due to GI AEs was significantly lower with etoricoxib than diclofenac ( 5.2 vs 8.5 events per 100 patient-years , respectively ; hazard ratio 0.62 ( 95 % CI : 0.47 , 0.81 ; p < or=0.001 ) ) .

Example answer:
{"entities": [{"text": "GI AEs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "patient-years", "type": "OrganismTaxon"}]}

Example input:
Sentence: On the 10th day of paroxetine and alprazolam treatment , the patient exhibited marked psychomotor retardation , disorientation , and severe muscle rigidity with tremors .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tremors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Also , the multichannel blockers Amiodarone , Paroxetine , Terfenadine and Citalopram prolonged FPDc in a concentration dependent manner .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "Paroxetine", "type": "ChemicalEntity"}, {"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}]}

Example input:
Sentence: Medical treatment was initiated at a daily dose of 20 mg paroxetine and 1.2 mg alprazolam .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Input:
Sentence: Paroxetine was discontinued and the dose of flecainide was reduced to 50 mg twice daily .

## Item biored:test:570
Example input:
Sentence: Despite the application of this high-throughput genotyping method , negative results from the two-stage DNA pooling design used to screen loci within the TPH , AADC and MAOA genes did not support their role in migraine susceptibility .

Example answer:
{"entities": [{"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Renal angiotensin II receptor type 2 ( AT2R ) gene expression in adult offspring was reduced by PCE , whereas the renal angiotensin II receptor type 1a ( AT1aR ) /AT2R expression ratio was increased .

Example answer:
{"entities": [{"text": "angiotensin II receptor type 2", "type": "GeneOrGeneProduct"}, {"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "angiotensin II receptor type 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1aR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ACE was expressed by endothelial cells in all ( 100 % ) specimens and by tumor cells in 56 ( 56 % ) specimens .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: HAT subjects had increased anti-inflammatory genes TGFB1 , TIMP1 , TIMP3 , and TIMP4 while proinflammatory PIG7 and MMP2 were also significantly increased ; all genes , p < 0.025 .

Example answer:
{"entities": [{"text": "TGFB1", "type": "GeneOrGeneProduct"}, {"text": "TIMP1", "type": "GeneOrGeneProduct"}, {"text": "TIMP3", "type": "GeneOrGeneProduct"}, {"text": "TIMP4", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PIG7", "type": "GeneOrGeneProduct"}, {"text": "MMP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Our study shows that ACE is expressed locally in gastric cancer and that the gene polymorphism influences metastatic behavior .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : In the present study , we aimed to substantiate the putative significance of angiotensin I-converting enzyme ( ACE ) on gastric cancer biology by investigating the influence of its gene polymorphism on gastric cancer progression .

Example answer:
{"entities": [{"text": "angiotensin I-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Several candidate genes have been identified with a potential role in the pathogenesis of asthma , including the angiotensin converting enzyme ( ACE ) gene .

## Item biored:test:553
Example input:
Sentence: Compared to many other ethnic groups , deafness-associated variants of the coding region of GJB2 are rare in Sudan and Kenya , suggesting a role of other genetic , or epigenetic factors as a cause for deafness in these countries .

Example answer:
{"entities": [{"text": "deafness-associated", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified 10 new families segregating DFNB7/B11 deafness and TMC1 mutations , including three novel alleles .

Example answer:
{"entities": [{"text": "DFNB7/B11 deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation at the DFNA36 hearing loss locus reveals a critical function and potential genotype-phenotype correlation for amino acid-572 of TMC1 .

Example answer:
{"entities": [{"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel missense mutation in the paired domain of human PAX9 causes oligodontia .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}, {"text": "oligodontia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The slower progression of hearing loss associated with p.D572H , in comparison with that caused by p.D572N , may reflect a correlation of DFNA36 phenotype with TMC1 genotype .

Example answer:
{"entities": [{"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.D572H", "type": "SequenceVariant"}, {"text": "p.D572N", "type": "SequenceVariant"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also detected p.R34X among normal control samples of African-American and northern European origins , raising the possibility that p.R34X and other mutations of TMC1 are prevalent contributors to the genetic load of deafness across a variety of populations and continents .

Example answer:
{"entities": [{"text": "p.R34X", "type": "SequenceVariant"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A single mutation , p.R34X , causes deafness in 10 ( 1.8 % ) of the families .

Example answer:
{"entities": [{"text": "p.R34X", "type": "SequenceVariant"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Overall , 9 different TMC1 mutations account for deafness in 19 ( 3.4 % ) of the 557 Pakistani families .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We screened affected family members for homozygosity at short-tandem repeats flanking known autosomal recessive ( DFNB ) deafness loci , followed by TMC1 sequence analysis in families segregating deafness linked to DFNB7/B11 .

Example answer:
{"entities": [{"text": "autosomal recessive ( DFNB ) deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We previously reported that mutations of transmembrane channel-like gene 1 ( TMC1 ) cause non-syndromic recessive deafness at the DFNB7/B11 locus on chromosome 9q13-q21 in nine Pakistani families .

Example answer:
{"entities": [{"text": "transmembrane channel-like gene 1", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "non-syndromic recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: As the AUNA1 deafness locus on 13q14-21 overlaps the IT in the PCDH9 ( protocadherin-9 ) gene region , PCDH9 was investigated as a candidate gene for deafness in both families .

## Item biored:test:626
Example input:
Sentence: The extent of hypotension and changes in brain tissue oxygenation ( PbtO ( 2 ) ) and in cerebral blood flow were studied in a separate group of animals .

Example answer:
{"entities": [{"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the hypertensive group ( n = 7 ) , the MAP was elevated by 25-30 mm Hg beginning 2 h after MCAO .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Insights could be gained by pooling data on MB frequency stratified by antithrombotic use in cohorts with ICH and ischemic stroke ( IS ) /transient ischemic attack ( TIA ) .

Example answer:
{"entities": [{"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic attack", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We performed a systematic review of published and unpublished data from cohorts with stroke or TIA to compare the presence of MB in : ( 1 ) antithrombotic users vs nonantithrombotic users with ICH ; ( 2 ) antithrombotic users vs nonusers with IS/TIA ; and ( 3 ) ICH vs ischemic events stratified by antithrombotic use .

Example answer:
{"entities": [{"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hemodynamic parameters and heart rate variability during a tilt test in relation to gene polymorphism of renin-angiotensin and serotonin system .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hemodynamic parameters and lead II electrocardiograph were monitored and recorded continuously .

Example answer:
{"entities": []}

Example input:
Sentence: In these trials , Hp typing of 69 DM individuals and treating those with the Hp 2-2 with vitamin E prevented one myocardial infarct , stroke or cardiovascular death .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "myocardial infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three time domain indexes of hemodynamic variability were employed : the standard deviation of mean arterial pressure as a measure of blood pressure variability and the standard deviation of beat-to-beat intervals ( SDRR ) and the root mean square of successive differences in R-wave-to-R-wave intervals as measures of heart rate variability .

Example answer:
{"entities": []}

Example input:
Sentence: In the periphery of the ischemic territory , SG in the cortex was greater ( less edema accumulation ) in the hypertensive group ( 1.041 +/- 0.001 vs 1.039 +/- 0.001 , P less than 0.05 ) .

Example answer:
{"entities": [{"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Heart rate ( HR ) , MAP , stroke volume ( SV ) , cardiac output ( CO ) , and frontal lobe oxygenation ( S ( c ) O ( 2 ) ) were registered .

## Item biored:test:547
Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A single mutation , p.R34X , causes deafness in 10 ( 1.8 % ) of the families .

Example answer:
{"entities": [{"text": "p.R34X", "type": "SequenceVariant"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The goal of this study was to define the identities , origins and frequencies of TMC1 mutations in an expanded cohort of 557 large Pakistani families segregating recessive deafness .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "recessive deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel missense mutation in the paired domain of human PAX9 causes oligodontia .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}, {"text": "oligodontia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Puratrophin-1 -- normally expressed in a wide range of cells , including epithelial hair cells in the cochlea -- was aggregated in Purkinje cells of the chromosome 16q22.1-linked ADCA brains .

Example answer:
{"entities": [{"text": "Puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "ADCA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A large proportion of non-syndromic autosomal recessive deafness ( NSARD ) in many populations is caused by variants of the GJB2 gene .

Example answer:
{"entities": [{"text": "non-syndromic autosomal recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NSARD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The slower progression of hearing loss associated with p.D572H , in comparison with that caused by p.D572N , may reflect a correlation of DFNA36 phenotype with TMC1 genotype .

Example answer:
{"entities": [{"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.D572H", "type": "SequenceVariant"}, {"text": "p.D572N", "type": "SequenceVariant"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation at the DFNA36 hearing loss locus reveals a critical function and potential genotype-phenotype correlation for amino acid-572 of TMC1 .

Example answer:
{"entities": [{"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We previously reported that mutations of transmembrane channel-like gene 1 ( TMC1 ) cause non-syndromic recessive deafness at the DFNB7/B11 locus on chromosome 9q13-q21 in nine Pakistani families .

Example answer:
{"entities": [{"text": "transmembrane channel-like gene 1", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "non-syndromic recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened affected family members for homozygosity at short-tandem repeats flanking known autosomal recessive ( DFNB ) deafness loci , followed by TMC1 sequence analysis in families segregating deafness linked to DFNB7/B11 .

Example answer:
{"entities": [{"text": "autosomal recessive ( DFNB ) deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Pure monosomy and pure trisomy of 13q21.2-31.1 consequent to a familial insertional translocation : exclusion of PCDH9 as the responsible gene for autosomal dominant auditory neuropathy ( AUNA1 ) .

## Item biored:test:627
Example input:
Sentence: Moreover , bupivacaine significantly increased COX-2 gene expression at 48 h as compared with the lidocaine/placebo group .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "lidocaine/placebo", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND AND OBJECTIVE : Despite advantages of induction and maintenance of anaesthesia with sevoflurane , postoperative nausea and vomiting occurs frequently .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "postoperative nausea and vomiting", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a separate group of mice not subjected to behavioral studies , the same dose of NTG ( n = 3 ) and NTG + NIMO ( n = 3 ) caused mean arterial blood pressure to decrease from 85.9 +/- 3.8 mm Hg sem to 31.6 +/- 0.8 mm Hg sem and from 86.2 +/- 3.7 mm Hg sem to 32.6 +/- 0.2 mm Hg sem , respectively .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: The doses calculated to cause 50 % reversal of hyperalgesia ( ED50 ) were 7.54 ( 1.81 ) and 4.83 ( 1.54 ) in the carrageenan model and 44.18 ( 1.37 ) and 9.14 ( 1.24 ) in the STZ-induced neuropathy model for CNSB002 and morphine , respectively ( mg/kg ; mean , SEM ) .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan", "type": "ChemicalEntity"}, {"text": "STZ-induced", "type": "ChemicalEntity"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the hypertensive group ( n = 7 ) , the MAP was elevated by 25-30 mm Hg beginning 2 h after MCAO .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These results suggest that bupivacaine stimulates COX-2 gene expression after tissue injury , which is associated with higher PGE2 production and pain after the local anesthetic effect dissipates .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "tissue injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: RESULTS : Induction of anesthesia was followed by a decrease in MAP , HR , SV , and CO concomitant with an elevation in S ( c ) O ( 2 ) .

## Item biored:test:583
Example input:
Sentence: The authors report here a depressed patient comorbid with postprandial dyspepsia who developed RLS after mirtazapine had been added to his domperidone therapy .

Example answer:
{"entities": [{"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "postprandial dyspepsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mirtazapine", "type": "ChemicalEntity"}, {"text": "domperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: ) , on ergometrine-induced wet dog shake ( WDS ) behavior and fluoxetine-induced penile erections was studied in rats .

Example answer:
{"entities": []}

Example input:
Sentence: PURPOSE : We present a case of a patient who developed seizures shortly after initiating treatment with levofloxacin and to discuss the potential drug-drug interactions related to the inhibition of cytochrome P450 ( CYP ) 1A2 in this case , as well as in other cases , of levofloxacin-induced seizures .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levofloxacin", "type": "ChemicalEntity"}, {"text": "cytochrome P450 ( CYP ) 1A2", "type": "GeneOrGeneProduct"}, {"text": "levofloxacin-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Co-administration of lidocaine with desipramine reversed the changes of convulsive activity of lidocaine and cocaine induced by repeated administration of desipramine .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "desipramine", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Also , the multichannel blockers Amiodarone , Paroxetine , Terfenadine and Citalopram prolonged FPDc in a concentration dependent manner .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "ChemicalEntity"}, {"text": "Paroxetine", "type": "ChemicalEntity"}, {"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}]}

Example input:
Sentence: trazodone enhanced dexamphetamine stereotypy , and antagonized haloperidol catalepsy , ergometrine-induced WDS behavior and fluoxetine-induced penile erections .

Example answer:
{"entities": []}

Example input:
Sentence: Telaprevir was considered the probable causative agent of an interaction with simvastatin according to the Drug Interaction Probability Scale .

Example answer:
{"entities": [{"text": "Telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the 10th day of paroxetine and alprazolam treatment , the patient exhibited marked psychomotor retardation , disorientation , and severe muscle rigidity with tremors .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tremors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This patient presented with symptoms of neuroleptic malignant syndrome ( NMS ) , thus demonstrating that NMS-like symptoms can occur after combined paroxetine and alprazolam treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: Possible neuroleptic malignant syndrome related to concomitant treatment with paroxetine and alprazolam .

Example answer:
{"entities": [{"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Input:
Sentence: OBJECTIVE : To describe a case of flecainide-induced delirium associated with a pharmacokinetic drug interaction with paroxetine .

## Item biored:test:629
Example input:
Sentence: However , the threshold ( 61.6 +/- 8.7 mg. l ( -1 ) ) during 1.6 % sevoflurane was not significant from that during 0.8 % sevoflurane , indicating a celling effect .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: There was a remarkable reduction in total cholesterol level as well , to the extent of 23 % in young and 21 % in aged animals with this dose of DCE .

Example answer:
{"entities": [{"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "DCE", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Meta-analysis of the two trials demonstrated a significant overall reduction in the composite end point in Hp 2-2 DM individuals with vitamin E ( odds ratio : 0.58 ; 95 % CI : 0.40-0.86 ; p = 0.006 ) .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In univariate analysis , the OR for the C4A deletion was 1.38 , p = 0.075 , but after simultaneous adjustment for the other four SNPs the odds ratio was 1.01 , p = 0.98 .

Example answer:
{"entities": [{"text": "C4A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PbtO ( 2 ) decreased from 51.7 +/- 4.5 mm Hg sem to 33.8 +/- 5.2 mm Hg sem in the NTG group and from 38.6 +/- 6.1 mm Hg sem to 25.4 +/- 2.0 mm Hg sem in the NTG + NIMO groups , respectively .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: The mean reduction in MSSBP/MSDBP with VAL/HCTZ 320/25 mg was 24.7/16.6 mm Hg , compared with 5.9/7.0 mm Hg with placebo .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The reduction in MSSBP was significantly greater with VAL/HCTZ 320/25 mg compared with VAL/HCTZ 160/12.5 mg ( P < 0.002 ) .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Input:
Sentence: However , a 14 % ( from 70 +/- 8 % to 60 +/- 7 % ) reduction in S ( c ) O ( 2 ) ( P < 0.05 ) followed with no change in CO ( 3.7 +/- 1.1 to 3.4 +/- 0.9 l min ( -1 ) ) .

## Item biored:test:516
Example input:
Sentence: The CASP8 -652 6N del variant genotypes or haplotypes were inversely associated with SCCHN risk ( adjusted OR , 0.70 ; 95 % CI , 0.57-0.85 for the ins/del + del/del genotypes compared with the ins/ins genotype ; adjusted OR , 0.73 ; 95 % CI , 0.55-0.97 for the del-D haplotype compared with the ins-D haplotype ) .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We found that the presence of the -1021T allele was associated with AD : odds ratio = 1.2 ( 95 % confidence interval : 1.06-1.4 , p = 0.005 ) .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients were genotyped for rs4704559 , rs10942891 and rs4704560 by allelic discrimination with Taqman assays .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "rs4704559", "type": "SequenceVariant"}, {"text": "rs10942891", "type": "SequenceVariant"}, {"text": "rs4704560", "type": "SequenceVariant"}]}

Example input:
Sentence: D allelic was significantly associated with DDD ( p value = 0.027 , odds ratio = 1.41 with 95 % CI = 1.04-1.90 ) while Genotypic association on the presence of D allele was also significantly associated with DDD ( p value = 0.046 , odds ratio = 1.50 with 95 % CI = 1.01-2.24 ) .

Example answer:
{"entities": [{"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Significantly lower frequency of SIM2 C-G haplotype ( rs2073601-rs2073416 ) was noticed in individuals with DS ( P value =0.01669 ) and their fathers ( P value=0.01185 ) .

Example answer:
{"entities": [{"text": "SIM2", "type": "GeneOrGeneProduct"}, {"text": "rs2073601-rs2073416", "type": "SequenceVariant"}, {"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The -930G allele carrier state was a risk factor for CAD ( OR 2.03 , 95 % CI 1.21-3.44 , P=0.007 ) .

Example answer:
{"entities": [{"text": "-930G", "type": "SequenceVariant"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The G allele of rs1111875 ( OR = 1.43 , 95 % CI = 1.18-1.72 , p = 1.8 x 10 ( -4 ) ) in HHEX ) , the T allele of rs10811661 ( OR = 1.47 , 95 % CI = 1.23-1.75 , p = 2.1 x 10 ( -5 ) ) in CDKN2A/B ) and the C allele of rs2237892 ( OR = 1.31 , 95 % CI = 1.10-1.56 , p = 0.003 ) in KCNQ1 showed significant associations with T2DM .

## Item biored:test:584
Example input:
Sentence: The patient was a 45-year-old man who was hospitalized due to nephrotic syndrome .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "man", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: We studied a 43-yr-old female , who presented with manifestations consistent with tissue-selective glucocorticoid hypersensitivity .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "hypersensitivity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The mutation was identified in a 22-year-old French woman coming to medical attention because of an increasing overweight .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "overweight", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 74-year-old man with depressive symptoms was admitted to a psychiatric hospital due to insomnia , loss of appetite , exhaustion , and agitation .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "depressive symptoms", "type": "DiseaseOrPhenotypicFeature"}, {"text": "psychiatric", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insomnia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "loss of appetite", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agitation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CASE SUMMARY : A 69-year-old white female presented to the emergency department with a history of confusion and paranoia over the past several days .

## Item biored:test:588
Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Telaprevir was considered the probable causative agent of an interaction with simvastatin according to the Drug Interaction Probability Scale .

Example answer:
{"entities": [{"text": "Telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In patients requiring the concurrent use of statins and CYP3A4 inhibitors , pravastatin , fluvastatin , and rosuvastatin carry the lowest risk of drug interactions ; atorvastatin carries moderate risk , whereas simvastatin and lovastatin have the highest risk and should be avoided in patients taking concomitant CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "statins", "type": "ChemicalEntity"}, {"text": "CYP3A4", "type": "GeneOrGeneProduct"}, {"text": "pravastatin", "type": "ChemicalEntity"}, {"text": "fluvastatin", "type": "ChemicalEntity"}, {"text": "rosuvastatin", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "lovastatin", "type": "ChemicalEntity"}, {"text": "CYP3A4 inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: PURPOSE : We present a case of a patient who developed seizures shortly after initiating treatment with levofloxacin and to discuss the potential drug-drug interactions related to the inhibition of cytochrome P450 ( CYP ) 1A2 in this case , as well as in other cases , of levofloxacin-induced seizures .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levofloxacin", "type": "ChemicalEntity"}, {"text": "cytochrome P450 ( CYP ) 1A2", "type": "GeneOrGeneProduct"}, {"text": "levofloxacin-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: The authors report here a depressed patient comorbid with postprandial dyspepsia who developed RLS after mirtazapine had been added to his domperidone therapy .

Example answer:
{"entities": [{"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "postprandial dyspepsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mirtazapine", "type": "ChemicalEntity"}, {"text": "domperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Medical treatment was initiated at a daily dose of 20 mg paroxetine and 1.2 mg alprazolam .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

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
Sentence: A metabolic drug interaction between flecainide and paroxetine , which the patient had been taking for more than 5 years , was considered .

## Item biored:test:518
Example input:
Sentence: Carriers of HLX1 exon 1 SNP rs12141189 showed increased IL-5 ( LpA , p = 0.007 ; Ppg , p = 0.10 ) , trendwise increased IL-13 ( LpA ) , higher GM-CSF ( LpA/Ppg , p < 0.05 ) and trendwise decreased IFN-g secretion ( Derp1+LpA-stimulation , p = 0.1 ) .

Example answer:
{"entities": [{"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs12141189", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "LpA", "type": "ChemicalEntity"}, {"text": "Ppg", "type": "ChemicalEntity"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "GM-CSF", "type": "GeneOrGeneProduct"}, {"text": "LpA/Ppg", "type": "ChemicalEntity"}, {"text": "IFN-g", "type": "GeneOrGeneProduct"}, {"text": "Derp1+LpA-stimulation", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neither rs2230912 nor any of 8 other SNPs genotyped across P2RX7 was found to be associated with mood disorder in general , nor specifically with bipolar or unipolar disorder .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar or unipolar disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Carriers of TBX21 promoter SNP rs17250932 and HLX1 promoter SNP rs2738751 showed reduced or trendwise reduced ( p < 0.07 ) IL-5 , IL-13 and TNF-a secretion after LpA-stimulation .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "rs17250932", "type": "SequenceVariant"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because polymorphism of CD72 , another inhibitory receptor of B cells , was associated with murine SLE , we identified human CD72 polymorphisms , tested their association with SLE and examined genetic interaction with FCGR2B in the Japanese ( 160 SLE , 277 controls ) , Thais ( 87 SLE , 187 controls ) and Caucasians ( 94 families containing SLE members ) .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "FCGR2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

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
Sentence: In conclusion , we have shown that SNPs in HHEX , CDKN2A/B , CDKAL1 , KCNQ1 and SLC30A8 confer a risk of T2DM in the Korean population .

## Item biored:test:572
Example input:
Sentence: Further association was identified in individuals over 40 years of age .

Example answer:
{"entities": []}

Example input:
Sentence: Ten consecutive patients ( mean age , 58.4 +/- 6.8 years ; 7 men , 3 women ) with similar characteristics at the duration of disease ( mean disease time , 8.4 +/- 3.5 years ) , disabling motor fluctuations ( Hoehn _ Yahr stage 3-5 in off-drug phases ) and levodopa-induced dyskinesias were selected .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The mean onset age was 58.5 + 9.8 years .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : Medically healthy 7- to 17-year-old males chronically treated , in a naturalistic setting , with risperidone were recruited for this cross-sectional study through child psychiatry outpatient clinics between November 2005 and June 2007 .

Example answer:
{"entities": [{"text": "risperidone", "type": "ChemicalEntity"}, {"text": "outpatient", "type": "OrganismTaxon"}]}

Example input:
Sentence: These 24 patients were mostly adults ( 96 % ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : The mean age was 65.6 + 8.5 years .

Example answer:
{"entities": []}

Example input:
Sentence: PATIENTS AND METHODS : We examined 102 patients ( men/women , 40/62 ; median age , 42 ) diagnosed with chronic ITP and 188 healthy controls ( men/women , 78/110 ; median age , 38 ) .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "men/women", "type": "OrganismTaxon"}, {"text": "chronic ITP", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PARTICIPANTS : Two hundred thirty-five patients aged 76 and older admitted to a major healthcare network between July 1 , 2001 , and June 30 , 2002 , with atrial fibrillation on warfarin were enrolled .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Two hundred twenty-eight patients ( 42 % men ) with a mean age of 81.1 ( range 76-94 ) were included in the analysis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}]}

Input:
Sentence: Ninety-seven asthmatic patients ( M/F 25/72 , mean age 39 +/- 13 years ) and 96 healthy subjects ( M/F 26/70 , mean age 38 +/- 12 years ) were included .

## Item biored:test:535
Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The same variants in the IRF6 gene that are associated with isolated orofacial clefts are also associated with human tooth agenesis ( rs861019 , P = 0.058 ; rs17015215-V274I , P = 0.0006 ; rs7802 , P = 0.004 ) .

Example answer:
{"entities": [{"text": "IRF6", "type": "GeneOrGeneProduct"}, {"text": "orofacial clefts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tooth agenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs861019", "type": "SequenceVariant"}, {"text": "rs17015215-V274I", "type": "SequenceVariant"}, {"text": "rs7802", "type": "SequenceVariant"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Mutation analysis of FOXF2 in patients with disorders of sex development ( DSD ) in combination with cleft palate .

## Item biored:test:579
Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Presence or absence of a CCR5 wt/DD32 genotype and progressive or long-term nonprogressive course of infection stratify the clinical populations in a two-way design .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: D allelic was significantly associated with DDD ( p value = 0.027 , odds ratio = 1.41 with 95 % CI = 1.04-1.90 ) while Genotypic association on the presence of D allele was also significantly associated with DDD ( p value = 0.046 , odds ratio = 1.50 with 95 % CI = 1.01-2.24 ) .

Example answer:
{"entities": [{"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Despite the application of this high-throughput genotyping method , negative results from the two-stage DNA pooling design used to screen loci within the TPH , AADC and MAOA genes did not support their role in migraine susceptibility .

Example answer:
{"entities": [{"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interactions have been reported between the low-activity -1021T allele ( rs1611115 ) of DBH and polymorphisms of the pro-inflammatory cytokine genes , IL1A and IL6 , contributing to the risk of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "rs1611115", "type": "SequenceVariant"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further follow-up of the cohort is required to study the polymorphisms ' relevance for immune-mediated diseases such as childhood asthma .

Example answer:
{"entities": [{"text": "immune-mediated diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Asthmatics with the DD genotype appeared to have a higher incidence of asthmatic episode exacerbations due to viral infections , but again this was not statistically significant ( p = 0.08 ) .

## Item biored:test:603
Example input:
Sentence: These results unravel a hidden link between AR and a functional putative PCa risk SNP , whose allele alteration affects androgen regulation of its host gene MLPH .

Example answer:
{"entities": [{"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "ChemicalEntity"}, {"text": "MLPH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These studies have produced intriguing but inconsistent results , potentially because the known functional variants : ADRB1 Arg389Gly and Gly49Ser , ADRB2 Arg16Gly and Gln27Glu , and ADRB3 Arg64Trp provided an incomplete picture of the total functional diversity at these genes .

Example answer:
{"entities": [{"text": "ADRB1", "type": "GeneOrGeneProduct"}, {"text": "Arg389Gly", "type": "SequenceVariant"}, {"text": "Gly49Ser", "type": "SequenceVariant"}, {"text": "ADRB2", "type": "GeneOrGeneProduct"}, {"text": "Arg16Gly", "type": "SequenceVariant"}, {"text": "Gln27Glu", "type": "SequenceVariant"}, {"text": "ADRB3", "type": "GeneOrGeneProduct"}, {"text": "Arg64Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: D90A-SOD1 mediated amyotrophic lateral sclerosis : a single founder for all cases with evidence for a Cis-acting disease modifier in the recessive haplotype .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An increased representation of the PNP AA genotype was observed in AD patients with fast cognitive deterioration in comparison with that from patients with slow deterioration rate .

Example answer:
{"entities": [{"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive deterioration", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report on a new allele at the arylsulfatase A ( ARSA ) locus causing late-onset metachromatic leukodystrophy ( MLD ) .

Example answer:
{"entities": [{"text": "arylsulfatase A", "type": "GeneOrGeneProduct"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "metachromatic leukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We propose that a cis-acting regulatory polymorphism has arisen close to D90A-SOD1 in the recessive founder , which decreases ALS susceptibility in heterozygotes and slows disease progression .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast to alleles that cause early-onset MLD , the arginine84 to glutamine substitution is associated with some residual ARSA activity .

Example answer:
{"entities": [{"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine84 to glutamine", "type": "SequenceVariant"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A comparison of genotypes , ARSA activities , and clinical data on 4 individuals carrying the allele of 81 patients with MLD examined , further validates the concept that different degrees of residual ARSA activity are the basis of phenotypical variation in MLD ..

Example answer:
{"entities": [{"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Findings point toward a possible mediating role of ADORA2A variants on phenotypic expression in ASD that need to be replicated in a larger sample .

## Item biored:test:594
Example input:
Sentence: All of the patients ' plasma blood urea nitrogen ( BUN ) and creatinine levels were measured on the second and seventh day after the administration of intravenous contrast material .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "BUN", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fasting serum insulin concentrations differed among groups ( F ( 33 ) = 3.35 ; P = .047 ) ( clozapine > olanzapine > risperidone ) with significant differences between clozapine and risperidone ( t ( 33 ) = 2.32 ; P = .03 ) and olanzapine and risperidone ( t ( 33 ) = 2.15 ; P = .04 ) .

Example answer:
{"entities": [{"text": "insulin", "type": "ChemicalEntity"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The cumulative discontinuation rate due to GI AEs was significantly lower with etoricoxib than diclofenac ( 5.2 vs 8.5 events per 100 patient-years , respectively ; hazard ratio 0.62 ( 95 % CI : 0.47 , 0.81 ; p < or=0.001 ) ) .

Example answer:
{"entities": [{"text": "GI AEs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "patient-years", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: We herein report the case of a 70-year-old man with 5-FU-induced cardiotoxicity , in whom a high serum level of alpha-fluoro-beta-alanine ( FBAL ) was observed .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "5-FU-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fluoro-beta-alanine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Finally , the IKr blockers , Terfenadine and Citalopram , which are reported to cause Torsade de Pointes ( TdP ) in clinical practice , produced early afterdepolarization ( EAD ) .

Example answer:
{"entities": [{"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}, {"text": "Torsade de Pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : Supratherapeutic flecainide plasma concentrations may cause delirium .

## Item biored:test:637
Example input:
Sentence: The second mutation is the di-nucleotide substitution c.467C > A and c.468C > T in exon 3 that causes the missense mutation A118D in the SEA domain of the extracellular stem region of matriptase-2 .

Example answer:
{"entities": [{"text": "c.467C > A", "type": "SequenceVariant"}, {"text": "c.468C > T", "type": "SequenceVariant"}, {"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: The deletion seems to occur due to exon skipping during processing of VLCAD pre-mRNA .

Example answer:
{"entities": [{"text": "VLCAD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This mutation leads to the activation of a cryptic splice site , 32 bp downstream of the mutation site and to subsequent aberrant out-of-frame splicing , resulting in two alternative mRNA transcripts and a downstream PTC .

Example answer:
{"entities": []}

Example input:
Sentence: Three aberrantly spliced cDNA species were identified : exon 22 and exon 22 to 23 skipping , and insertion of an 87-base pair cryptic exon .

Example answer:
{"entities": []}

Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Analysis of PTPN22 transcripts from a subject heterozygous for this variant indicated that it interfered with normal mRNA splicing , resulting in a premature termination codon after exon 17 .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Input:
Sentence: In vitro splicing assays showed that the mutant minigene dramatically affected pre-mRNA processing , causing exon 2 to be completely skipped .

## Item biored:test:638
Example input:
Sentence: This mutation leads to the activation of a cryptic splice site , 32 bp downstream of the mutation site and to subsequent aberrant out-of-frame splicing , resulting in two alternative mRNA transcripts and a downstream PTC .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The frameshift caused by the c.1052delA deletion removes the last 81 amino acids of the protein , including the third zinc-finger motif .

Example answer:
{"entities": [{"text": "c.1052delA", "type": "SequenceVariant"}]}

Example input:
Sentence: To determine whether c.609+28_610-16del allele-derived transcripts were subject to nonsense-mediated mRNA decay ( NMD ) , patient fibroblasts were incubated with the protein synthesis inhibitor anisomycin .

Example answer:
{"entities": [{"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "anisomycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Analysis of PTPN22 transcripts from a subject heterozygous for this variant indicated that it interfered with normal mRNA splicing , resulting in a premature termination codon after exon 17 .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We found a single nucleotide deletion c.342delA , located in exon 3 , which resulted in a frameshift at amino acid position 58 ( p.Arg58fs or p.R58fs ) .

Example answer:
{"entities": [{"text": "c.342delA", "type": "SequenceVariant"}, {"text": "p.Arg58fs", "type": "SequenceVariant"}, {"text": "p.R58fs", "type": "SequenceVariant"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Input:
Sentence: The putative product from a new out-of-frame translational start point in exon 3 is expected to yield a nonsense 25-amino-acid peptide .

## Item biored:test:539
Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Also , it records a novel deletion in exon 1 of SRD5A2 gene in a patient with severe hypospadias .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "hypospadias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This finding adds another locus to the spectrum of genes associated with osteogenesis imperfecta and reveals that SP7/OSX also plays a key role in human bone development .

Example answer:
{"entities": [{"text": "osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SP7/OSX", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The same variants in the IRF6 gene that are associated with isolated orofacial clefts are also associated with human tooth agenesis ( rs861019 , P = 0.058 ; rs17015215-V274I , P = 0.0006 ; rs7802 , P = 0.004 ) .

Example answer:
{"entities": [{"text": "IRF6", "type": "GeneOrGeneProduct"}, {"text": "orofacial clefts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tooth agenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs861019", "type": "SequenceVariant"}, {"text": "rs17015215-V274I", "type": "SequenceVariant"}, {"text": "rs7802", "type": "SequenceVariant"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We hypothesized that humans with disorders of sex development ( DSD ) in combination with cleft palate could have mutations in the FOXF2 gene .

## Item biored:test:591
Example input:
Sentence: The aim of this study is to investigate and compare the protective effects of isotonic sodium chloride with sodium bicarbonate infusion and isotonic sodium chloride infusion with diltiazem , a calcium channel blocker , in preventing CIN .

Example answer:
{"entities": [{"text": "sodium chloride", "type": "ChemicalEntity"}, {"text": "sodium bicarbonate", "type": "ChemicalEntity"}, {"text": "diltiazem", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Drug-drug interactions related to the inhibition of CYP1A2 by levofloxacin are likely involved in the clinical outcome of these cases .

Example answer:
{"entities": [{"text": "CYP1A2", "type": "GeneOrGeneProduct"}, {"text": "levofloxacin", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVE : This study determined the antihyperalgesic effect of CNSB002 , a sodium channel blocker with antioxidant properties given alone and in combinations with morphine in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The influence of sevoflurane on lidocaine-induced convulsions was studied in cats .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "lidocaine-induced", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Studies of synergy between morphine and a novel sodium channel blocker , CNSB002 , in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Inhibition of Na ( + ) channels by local anesthetics may regulate desipramine-induced down-regulation of NET function .

Example answer:
{"entities": [{"text": "Na ( + )", "type": "ChemicalEntity"}, {"text": "anesthetics", "type": "ChemicalEntity"}, {"text": "desipramine-induced", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Apamin , a selective blocker of calcium-dependent potassium channels , was administered intracerebroventricularly in rats anesthetized with 0.8 % sevoflurane to investigate the mechanism of the anticonvulsive effects .

Example answer:
{"entities": [{"text": "Apamin", "type": "ChemicalEntity"}, {"text": "calcium-dependent", "type": "ChemicalEntity"}, {"text": "potassium", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Input:
Sentence: DISCUSSION : Flecainide and pharmacologically similar agents that interact with sodium channels may cause delirium in susceptible patients .

## Item biored:test:628
Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: According to annexin V binding , erythrocytes from patients indeed showed a significant increase of PS exposure within 1 week of treatment with azathioprine .

Example answer:
{"entities": [{"text": "annexin V", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PS", "type": "ChemicalEntity"}, {"text": "azathioprine", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a separate group of mice not subjected to behavioral studies , the same dose of NTG ( n = 3 ) and NTG + NIMO ( n = 3 ) caused mean arterial blood pressure to decrease from 85.9 +/- 3.8 mm Hg sem to 31.6 +/- 0.8 mm Hg sem and from 86.2 +/- 3.7 mm Hg sem to 32.6 +/- 0.2 mm Hg sem , respectively .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the hypertensive group ( n = 7 ) , the MAP was elevated by 25-30 mm Hg beginning 2 h after MCAO .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: After administration of phenylephrine , MAP increased ( 51 +/- 12 to 81 +/- 13 mmHg ; P < 0.001 ; mean +/- SD ) .

## Item biored:test:582
Example input:
Sentence: The authors report here a depressed patient comorbid with postprandial dyspepsia who developed RLS after mirtazapine had been added to his domperidone therapy .

Example answer:
{"entities": [{"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "postprandial dyspepsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mirtazapine", "type": "ChemicalEntity"}, {"text": "domperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Medical treatment was initiated at a daily dose of 20 mg paroxetine and 1.2 mg alprazolam .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

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
Sentence: Delirium in a patient with toxic flecainide plasma concentrations : the role of a pharmacokinetic drug interaction with paroxetine .

## Item biored:test:559
Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: POLG mutations associated with Alpers ' syndrome and mitochondrial DNA depletion .

Example answer:
{"entities": [{"text": "POLG", "type": "GeneOrGeneProduct"}, {"text": "Alpers ' syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial DNA depletion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Expression of the master regulators of oxidative metabolism transcription factor A mitochondrial , PGC-1a , AMPK , and serine-threonine liver kinase B1 was altered by high glucose , as well as their downstream signaling networks .

Example answer:
{"entities": [{"text": "master regulators of oxidative metabolism transcription factor A mitochondrial", "type": "GeneOrGeneProduct"}, {"text": "PGC-1a", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "serine-threonine liver kinase B1", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Myotonic dystrophy ( DM ) , the most prevalent muscular disorder in adults , is caused by ( CTG ) n-repeat expansion in a gene encoding a protein kinase ( DM protein kinase ; DMPK ) and involves changes in cytoarchitecture and ion homeostasis .

Example answer:
{"entities": [{"text": "Myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM protein kinase", "type": "GeneOrGeneProduct"}, {"text": "DMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Depletion of mitochondrial DNA in fibroblast cultures from patients with POLG1 mutations is a consequence of catalytic mutations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It is an autosomal recessive , developmental mitochondrial DNA depletion disorder characterized by deficiency in mitochondrial DNA polymerase gamma ( POLG ) catalytic activity , refractory seizures , neurodegeneration , and liver disease .

Example answer:
{"entities": [{"text": "mitochondrial DNA depletion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DNA polymerase gamma", "type": "GeneOrGeneProduct"}, {"text": "POLG", "type": "GeneOrGeneProduct"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Deoxyguanosine kinase ( dGK ) deficiency is a frequent cause of mitochondrial DNA depletion associated with a hepatocerebral phenotype .

## Item biored:test:607
Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : To study the 2 drugs most clearly implicated ( clozapine and olanzapine ) and risperidone using a frequently sampled intravenous glucose tolerance test .

Example answer:
{"entities": [{"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a genotype test , we found a trend to point-wise association ( P = 0.053 ) of the G472A SNP in Hispanic subjects with opiate addiction .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Syncope and QT prolongation among patients treated with methadone for heroin dependence in the city of Copenhagen .

Example answer:
{"entities": [{"text": "Syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "heroin dependence", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : In this cross-sectional study interview , ECGs and blood samples were collected in a population of adult heroin addicts treated with methadone or buprenorphine on a daily basis .

Example answer:
{"entities": [{"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "buprenorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Methadone is associated with QT prolongation and higher reporting of syncope in a population of heroin addicts .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As heroin addicts sometimes faint while using illicit drugs , doctors might attribute too many episodes of syncope to illicit drug use and thereby underestimate the incidence of TdP in this special population , and the high mortality in this population may , in part , be caused by the proarrhythmic effect of methadone .

Example answer:
{"entities": [{"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Input:
Sentence: Drug-related globus pallidus infarctions are most often associated with heroin .

## Item biored:test:605
Example input:
Sentence: Daily treatment of cocaine increased [ ( 3 ) H ] norepinephrine uptake into the hippocampus .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Smoking of crack cocaine as a risk factor for HIV infection among people who use injection drugs .

Example answer:
{"entities": [{"text": "crack cocaine", "type": "ChemicalEntity"}, {"text": "HIV infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Repeated administration of cocaine induces up-regulation of hippocampal NET function .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results provide evidence for a possible mechanistic role of oxidative and nitrosative stress and NFkappaB in the alterations induced by cocaine .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: INTERPRETATION : Smoking of crack cocaine was found to be an independent risk factor for HIV seroconversion among people who were injection drug users .

Example answer:
{"entities": [{"text": "crack cocaine", "type": "ChemicalEntity"}, {"text": "HIV seroconversion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: After adjusting for potential confounders , we found that the risk of HIV seroconversion among participants who were daily smokers of crack cocaine increased over time ( period 1 : hazard ratio [ HR ] 1.03 , 95 % confidence interval [ CI ] 0.57-1.85 ; period 2 : HR 1.68 , 95 % CI 1.01-2.80 ; and period 3 : HR 2.74 , 95 % CI 1.06-7.11 ) .

Example answer:
{"entities": [{"text": "HIV seroconversion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crack cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Different mechanisms have been suggested for cocaine toxicity including an increase in oxidative stress but the association between oxidative status in the brain and cocaine induced-behaviour is poorly understood .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Cocaine is a widely abused psychostimulant that has both rewarding and aversive properties .

Example answer:
{"entities": [{"text": "Cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cocaine causes memory and learning impairments in rats : involvement of nuclear factor kappa B and oxidative stress , and prevention by topiramate .

Example answer:
{"entities": [{"text": "Cocaine", "type": "ChemicalEntity"}, {"text": "memory and learning impairments", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "topiramate", "type": "ChemicalEntity"}]}

Input:
Sentence: Cocaine is a risk factor for both ischemic and haemorrhagic stroke .

## Item biored:test:630
Example input:
Sentence: Daily administration of desipramine , an inhibitor of the NET , for 5 days decreased [ ( 3 ) H ] norepinephrine uptake in the P2 fractions of hippocampus but not cortex , striatum or amygdalae .

Example answer:
{"entities": [{"text": "desipramine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fourth group received a single dose of ZnSO ( 4 ) ( 0.1 micromol/10 microl normal saline , i.c.v ) then BCNU ( 20 mg/kg , i.v , once ) after 24 h. The obtained data revealed that BCNU administration resulted in deterioration of learning and short-term memory ( STM ) , as measured by using radial arm water maze , accompanied with decreased hippocampal glutathione reductase ( GR ) activity and reduced glutathione ( GSH ) content .

Example answer:
{"entities": [{"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "deterioration of learning and short-term memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutathione reductase", "type": "GeneOrGeneProduct"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "GSH", "type": "ChemicalEntity"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Input:
Sentence: The administration of ephedrine led to a similar increase in MAP ( 53 +/- 9 to 79 +/- 8 mmHg ; P < 0.001 ) , restored CO ( 3.2 +/- 1.2 to 5.0 +/- 1.3 l min ( -1 ) ) , and preserved S ( c ) O ( 2 ) .

## Item biored:test:575
Example input:
Sentence: Despite the application of this high-throughput genotyping method , negative results from the two-stage DNA pooling design used to screen loci within the TPH , AADC and MAOA genes did not support their role in migraine susceptibility .

Example answer:
{"entities": [{"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : AA genotype of A 1166C polymorphism was associated with lower minimal systolic blood pressure ( SBP ) and diastolic blood pressure ( DBP ) during HUT compared with other genotypes ( minimal SBP : AA 59.6+/-21,8 , AC 79.9+/-22.7 , CC 65.4+/-22.7 mmHg , P=0.007 ) , ( minimal DBP : AA 36.4+/-22.7 , AC 52.3+/-22.9 , CC 45.4+/-19.5 mmHg , P=0.007 ) .AA genotype was also associated with higher SDNN compared to other genotypes in the early phase of HUT ( SDNN in 5 minutes of tilt : AA 59.7+/-24.6 , AC 50.6+/-20.6 , CC 46.0+/-13.2 , P=0.01 ) and at syncope occurrence ( SDNN : AA 71.0+/-20.9 , AC 58.2+/-17.9 , CC 58+/-10 , P=0.04 ) CONCLUSION : AA genotype of A 1166C polymorphism in the ATR1 gene may be associated with hypotension and decline in sympathetic tone during HUT .

Example answer:
{"entities": [{"text": "A 1166C", "type": "SequenceVariant"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : The present study aimed to estimate the association between susceptibility to migraine and the 12-nucleotide insertion/deletion ( indel ) polymorphism in promoter region of alpha ( 2B ) -adrenergic receptor gene ( ADRA2B ) .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "12-nucleotide insertion/deletion ( indel )", "type": "SequenceVariant"}, {"text": "alpha ( 2B ) -adrenergic receptor", "type": "GeneOrGeneProduct"}, {"text": "ADRA2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Twenty-four of 113 ( 21 % ) gastric cancer patients had the II , 57 ( 51 % ) the ID , and 32 ( 28 % ) the DD genotype .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : We demonstrated that individuals with the presence of D allele for the -1607 promoter polymorphism of MMP1 are about 1.5 times more susceptible to develop DDD when compared with those having G allele only .

Example answer:
{"entities": [{"text": "D allele for the -1607", "type": "SequenceVariant"}, {"text": "MMP1", "type": "GeneOrGeneProduct"}, {"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The distribution of the ACE genotypes did not differ significantly from the control group of 189 patients without gastric cancer .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The frequency of the ACE genotypes ( I = insertion and D = deletion ) among asthmatics and controls were compared : asthmatics showed a 40.2 % prevalence of the DD genotype ( n = 39 ) , ID was 45.4 % ( n = 44 ) , and II was 14.4 % ( n = 14.4 ) .

## Item biored:test:578
Example input:
Sentence: RESULTS : AA genotype of A 1166C polymorphism was associated with lower minimal systolic blood pressure ( SBP ) and diastolic blood pressure ( DBP ) during HUT compared with other genotypes ( minimal SBP : AA 59.6+/-21,8 , AC 79.9+/-22.7 , CC 65.4+/-22.7 mmHg , P=0.007 ) , ( minimal DBP : AA 36.4+/-22.7 , AC 52.3+/-22.9 , CC 45.4+/-19.5 mmHg , P=0.007 ) .AA genotype was also associated with higher SDNN compared to other genotypes in the early phase of HUT ( SDNN in 5 minutes of tilt : AA 59.7+/-24.6 , AC 50.6+/-20.6 , CC 46.0+/-13.2 , P=0.01 ) and at syncope occurrence ( SDNN : AA 71.0+/-20.9 , AC 58.2+/-17.9 , CC 58+/-10 , P=0.04 ) CONCLUSION : AA genotype of A 1166C polymorphism in the ATR1 gene may be associated with hypotension and decline in sympathetic tone during HUT .

Example answer:
{"entities": [{"text": "A 1166C", "type": "SequenceVariant"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , the -1021T allele with presumed low activity may be associated with misregulation of inflammation , which could contribute to the onset of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : When compared with Crohn 's disease patients without CARD15 mutations , the presence of at least one CARD15 variant in Crohn 's disease patients more frequently led to gASCA positivity ( 66.1 % versus 51.5 % , p < 0.0001 ) and ALCA positivity ( 43.3 % versus 34.9 % , p = 0.018 ) and higher gASCA titers ( 85.7 versus 51.8 ELISA units , p < 0.0001 ) , independent of ileal involvement .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CARD15", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Similarly , Crohn 's disease patients carrying NOD1/CARD4 indel had a higher prevalence of gASCA antibodies than wild-type patients ( 63.8 % versus 55.2 % , p = 0.014 ) , also with a gene dosage effect .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "NOD1/CARD4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the application of this high-throughput genotyping method , negative results from the two-stage DNA pooling design used to screen loci within the TPH , AADC and MAOA genes did not support their role in migraine susceptibility .

Example answer:
{"entities": [{"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A gene dosage effect , with increasing gASCA and ALCA positivity for patients carrying none , one and two CARD15 variants , respectively , was seen for both markers .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CARD15", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , the ACE genotypes correlated with the number of lymph node metastases and the Unio Internationale Contra Cancrum ( UICC ) tumor stage .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "lymph node metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the influence of TBX21 and HLX1 single nucleotide polymorphisms ( SNPs ) , which have previously been shown to be associated with asthma , on T ( H ) 1/T ( H ) 2 lineage cytokines at birth .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "asthma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The distribution of the ACE genotypes did not differ significantly from the control group of 189 patients without gastric cancer .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Asthmatics with the ID ACE genotype showed a higher frequency of drug allergies , although this was not statistically significant ( p = 0.08 ) .

## Item biored:test:544
Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One sporadic BCC presented the mutation g.2885G > C in exon 17 of PTCH1 , which predicts the substitution p.R962T in an external domain of the protein .

Example answer:
{"entities": [{"text": "BCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "g.2885G > C", "type": "SequenceVariant"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "p.R962T", "type": "SequenceVariant"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The second mutation is the di-nucleotide substitution c.467C > A and c.468C > T in exon 3 that causes the missense mutation A118D in the SEA domain of the extracellular stem region of matriptase-2 .

Example answer:
{"entities": [{"text": "c.467C > A", "type": "SequenceVariant"}, {"text": "c.468C > T", "type": "SequenceVariant"}, {"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Characterization of a novel BCHE `` silent '' allele : point mutation ( p.Val204Asp ) causes loss of activity and prolonged apnea with suxamethonium .

Example answer:
{"entities": [{"text": "BCHE", "type": "GeneOrGeneProduct"}, {"text": "p.Val204Asp", "type": "SequenceVariant"}, {"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "suxamethonium", "type": "ChemicalEntity"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Input:
Sentence: Two silent mutations , c.1272C > T ( Ser424Ser ) and c.1284T > C ( Tyr428Tyr ) , respectively , occurred in the coding region of exon 2 , again in both patients and normal controls .

## Item biored:test:599
Example input:
Sentence: Further analyses of C. elegans RAB-28 , recently associated with autosomal-recessive cone-rod dystrophy , reveal that this small GTPase is exclusively expressed in ciliated neurons where it dynamically associates with IFT trains .

Example answer:
{"entities": [{"text": "C. elegans", "type": "OrganismTaxon"}, {"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "cone-rod dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An antibody against the synthetic C-terminal peptides deduced from the cDNA of the gene responsible for X-linked adrenoleukodystrophy ( ALD ) was produced to characterize the product of the ALD gene .

Example answer:
{"entities": [{"text": "X-linked adrenoleukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our findings suggest that the G51S PNP polymorphism is associated with a faster rate of cognitive decline in AD patients , highlighting the important role of purine metabolism in the progression of this neurodegenerative disorder .

Example answer:
{"entities": [{"text": "G51S", "type": "SequenceVariant"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "neurodegenerative disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast to alleles that cause early-onset MLD , the arginine84 to glutamine substitution is associated with some residual ARSA activity .

Example answer:
{"entities": [{"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine84 to glutamine", "type": "SequenceVariant"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We propose that a cis-acting regulatory polymorphism has arisen close to D90A-SOD1 in the recessive founder , which decreases ALS susceptibility in heterozygotes and slows disease progression .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , AT2R gene and protein expressions in fetal kidneys were inhibited by PCE , associated with the repression of the gene expression of glial-cell-line-derived neurotrophic factor ( GDNF ) /tyrosine kinase receptor ( c-Ret ) signaling pathway .

Example answer:
{"entities": [{"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "glial-cell-line-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "GDNF", "type": "GeneOrGeneProduct"}, {"text": "kinase receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Ret", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Renal angiotensin II receptor type 2 ( AT2R ) gene expression in adult offspring was reduced by PCE , whereas the renal angiotensin II receptor type 1a ( AT1aR ) /AT2R expression ratio was increased .

Example answer:
{"entities": [{"text": "angiotensin II receptor type 2", "type": "GeneOrGeneProduct"}, {"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "angiotensin II receptor type 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1aR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In vivo characterization of a dual adenosine A2A/A1 receptor antagonist in animal models of Parkinson 's disease .

Example answer:
{"entities": [{"text": "adenosine A2A/A1 receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The in vivo characterization of a dual adenosine A ( 2A ) /A ( 1 ) receptor antagonist in several animal models of Parkinson 's disease is described .

Example answer:
{"entities": [{"text": "adenosine A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Its gene product , the adenosine A ( 2A ) receptor , is strongly expressed in the caudate nucleus , which also is involved in ASD .

## Item biored:test:636
Example input:
Sentence: Characterization of a novel BCHE `` silent '' allele : point mutation ( p.Val204Asp ) causes loss of activity and prolonged apnea with suxamethonium .

Example answer:
{"entities": [{"text": "BCHE", "type": "GeneOrGeneProduct"}, {"text": "p.Val204Asp", "type": "SequenceVariant"}, {"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "suxamethonium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: To determine whether c.609+28_610-16del allele-derived transcripts were subject to nonsense-mediated mRNA decay ( NMD ) , patient fibroblasts were incubated with the protein synthesis inhibitor anisomycin .

Example answer:
{"entities": [{"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "anisomycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation resulted in replacement of a non-polar amino acid ( proline ) with a polar amino acid ( serine ) at position 29 ( P29S ) .

Example answer:
{"entities": [{"text": "( proline ) with a polar amino acid ( serine ) at position 29", "type": "SequenceVariant"}, {"text": "P29S", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The C139T mutation , predicted to result in the substitution of an arginine by a tryptophan ( R47W ) in the N-terminal subdomain , affected conserved residues in the PAX9 paired domain .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "arginine by a tryptophan", "type": "SequenceVariant"}, {"text": "R47W", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Analysis of PTPN22 transcripts from a subject heterozygous for this variant indicated that it interfered with normal mRNA splicing , resulting in a premature termination codon after exon 17 .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Input:
Sentence: This resulted in a silent change at codon 34 of the mature protein .

## Item biored:test:619
Example input:
Sentence: However , a longitudinal follow-up study on survival in the same sample indicated that 192RR homozygotes have a poorer survival compared to QQ homozygotes ( hazard rate : 1.38 , P = 0.04 ) .

Example answer:
{"entities": [{"text": "192RR", "type": "SequenceVariant"}]}

Example input:
Sentence: Patients developing ESRD had a 6-year survival after onset of ESRD of 27 % for the patients receiving hemodialysis versus 71.4 % for the patients developing ESRD who subsequently received kidney transplants .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , SNP1 of UP Ia gene affecting a C to T conversion and an Ala7Val change , and SNP7 of UP III affecting a C to G conversion and a Pro154Ala change , were marginally associated with VUR ( both P= 0.08 ) .

Example answer:
{"entities": [{"text": "UP Ia", "type": "GeneOrGeneProduct"}, {"text": "C to T", "type": "SequenceVariant"}, {"text": "Ala7Val", "type": "SequenceVariant"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "C to G", "type": "SequenceVariant"}, {"text": "Pro154Ala", "type": "SequenceVariant"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Re-expression of LKB1 or knockdown of VEGF receptor 2 decreased the overproliferation and -migration observed in LKB1 ( endo-/- ) cells .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Moreover , the abundance and proliferative index of lymph node , thymus and CNS CD4 ( + ) CD25 ( + ) FoxP3 ( + ) Tregs were strikingly reduced in VPAC2-deficient mice with EAE .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}, {"text": "VPAC2-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The development of ESRD decreases survival , particularly in those patients treated with dialysis only .

Example answer:
{"entities": [{"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our results thus indicates that PON1 192RR homozygosity is associated with increased mortality in women in the second half of life and that this increased mortality is possibly related to CHD severity and survival after CHD rather than susceptibility to development of CHD .

Example answer:
{"entities": [{"text": "PON1", "type": "GeneOrGeneProduct"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: VDR expression was not significantly related with patient survival , prognosis , or clinical outcome .

## Item biored:test:612
Example input:
Sentence: VEGF-stimulated hRMVEC proliferation was measured following transfection with NOX4 siRNA or STAT3 siRNA , or respective controls .

Example answer:
{"entities": [{"text": "VEGF-stimulated", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA-damage response gene GADD45A induces differentiation in hematopoietic stem cells without inhibiting cell cycle or survival .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The transcription factor hepatocyte nuclear factor ( HNF ) -6 is an upstream regulator of several genes involved in the pathogenesis of maturity-onset diabetes of the young .

Example answer:
{"entities": [{"text": "hepatocyte nuclear factor ( HNF ) -6", "type": "GeneOrGeneProduct"}, {"text": "maturity-onset diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Cisplatin-treated DCs down-regulated the expression of cell surface molecules ( CD80 , CD86 , MHC class I and II ) and up-regulated endocytic capacity in a dose-dependent manner .

Example answer:
{"entities": [{"text": "Cisplatin-treated", "type": "ChemicalEntity"}, {"text": "CD80", "type": "GeneOrGeneProduct"}, {"text": "CD86", "type": "GeneOrGeneProduct"}, {"text": "MHC class I and II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TNF-alpha or conditioned media ( CM ) of TNF-alpha-stimulated C4-2B cells upregulated BMP-2 and BMP-dependent Smad transcripts and inhibited receptor activator of NF-kappaB ligand transcripts in RAW 264.7 preosteoclast cells , respectively , implying that this factor may contribute to suppression of osteoclastogenesis via direct and paracrine mechanisms .

Example answer:
{"entities": [{"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha-stimulated", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "BMP-2", "type": "GeneOrGeneProduct"}, {"text": "BMP-dependent", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "receptor activator of NF-kappaB ligand", "type": "GeneOrGeneProduct"}, {"text": "RAW 264.7", "type": "CellLine"}]}

Example input:
Sentence: Knockdown of either NOX4 or STAT3 inhibited VEGF-induced EC proliferation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Re-expression of LKB1 or knockdown of VEGF receptor 2 decreased the overproliferation and -migration observed in LKB1 ( endo-/- ) cells .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , AT2R gene and protein expressions in fetal kidneys were inhibited by PCE , associated with the repression of the gene expression of glial-cell-line-derived neurotrophic factor ( GDNF ) /tyrosine kinase receptor ( c-Ret ) signaling pathway .

Example answer:
{"entities": [{"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "glial-cell-line-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "GDNF", "type": "GeneOrGeneProduct"}, {"text": "kinase receptor", "type": "GeneOrGeneProduct"}, {"text": "c-Ret", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We show that FGFR2 signalling correlates with maintenance of expression of a key transcription factor for basal cell self-renewal and differentiation : SOX2 .

Example answer:
{"entities": [{"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "SOX2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The vitamin D receptor ( VDR ) is a transcription factor , which plays an important role in cellular differentiation and inhibition of proliferation .

## Item biored:test:561
Example input:
Sentence: Depletion of mitochondrial DNA in fibroblast cultures from patients with POLG1 mutations is a consequence of catalytic mutations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated clinical and cellular phenotypes of 24 children with mutations in the catalytic ( alpha ) subunit of the mitochondrial DNA ( mtDNA ) gamma polymerase ( POLG1 ) .

Example answer:
{"entities": [{"text": "mitochondrial DNA ( mtDNA ) gamma polymerase", "type": "GeneOrGeneProduct"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Input:
Sentence: This new DGUOK homozygous mutation ( c.444-62C > A ) was identified in three patients from two North-African consanguineous families with combined respiratory chain deficiencies and mitochondrial DNA depletion in the liver .

## Item biored:test:593
Example input:
Sentence: Co-administration of lidocaine with desipramine reversed the changes of convulsive activity of lidocaine and cocaine induced by repeated administration of desipramine .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "desipramine", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Medical treatment was initiated at a daily dose of 20 mg paroxetine and 1.2 mg alprazolam .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: This patient presented with symptoms of neuroleptic malignant syndrome ( NMS ) , thus demonstrating that NMS-like symptoms can occur after combined paroxetine and alprazolam treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NMS-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the 10th day of paroxetine and alprazolam treatment , the patient exhibited marked psychomotor retardation , disorientation , and severe muscle rigidity with tremors .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tremors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Possible neuroleptic malignant syndrome related to concomitant treatment with paroxetine and alprazolam .

Example answer:
{"entities": [{"text": "neuroleptic malignant syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: The adverse drug reaction score obtained by the Naranjo algorithm was 6 in our case , indicating a probable relationship between the patient 's NMS-like adverse symptoms and the combined treatment used in this case .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "NMS-like", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Telaprevir was considered the probable causative agent of an interaction with simvastatin according to the Drug Interaction Probability Scale .

Example answer:
{"entities": [{"text": "Telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Input:
Sentence: According to the Naranjo probability scale , flecainide was the probable cause of the patient 's delirium ; the Horn Drug Interaction Probability Scale indicates a possible pharmacokinetic drug interaction between flecainide and paroxetine .

## Item biored:test:641
Example input:
Sentence: In its regulatory subunit , p85alpha , there is a common amino acid substitution ( the Met326Ile polymorphism ) , and this amino acid may be crucial for the function of the p85alpha regulatory subunit and PI3-kinase .

Example answer:
{"entities": [{"text": "p85alpha", "type": "GeneOrGeneProduct"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "PI3-kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Molecular dynamic simulations of structural changes induced by L1503R indicated that the mean value of all-atom root-mean-squared-deviation was shifted from those with wild type or another mutation L1503Q that has been reported to be a group II mutation , which is susceptible to ADAMTS13 proteolysis .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "L1503Q", "type": "SequenceVariant"}, {"text": "ADAMTS13", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , each affected child was heterozygous for the G1681A mutation in exon 7 that led to an Ala467Thr substitution in POLG , within the linker region of the protein .

Example answer:
{"entities": [{"text": "G1681A", "type": "SequenceVariant"}, {"text": "Ala467Thr", "type": "SequenceVariant"}, {"text": "POLG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Moreover , the only R to G mutation at position 76 was found to strongly impact on protein folding and oligomerization by altering the hydrogen bond network .

Example answer:
{"entities": [{"text": "R to G mutation at position 76", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Direct sequencing of the encoding regions of the candidate genes revealed a heterozygous mutation c.592C -- > T in exon 2 of the gap junction protein , alpha 8 ( GJA8 ) gene .

Example answer:
{"entities": [{"text": "c.592C -- > T", "type": "SequenceVariant"}, {"text": "gap junction protein , alpha 8", "type": "GeneOrGeneProduct"}, {"text": "GJA8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : This report is the first to relate p.R198W mutation in GJA8 with CCMC .

Example answer:
{"entities": [{"text": "p.R198W", "type": "SequenceVariant"}, {"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Data from in silico analysis confirmed that the C88Y mutation would affect subunit conformation .
