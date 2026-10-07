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

## Item biored:test:378
Example input:
Sentence: RESULTS : Meta-analysis of the two trials demonstrated a significant overall reduction in the composite end point in Hp 2-2 DM individuals with vitamin E ( odds ratio : 0.58 ; 95 % CI : 0.40-0.86 ; p = 0.006 ) .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cox regression analysis of IHC scores found that only phospho AKT ( pAKT ) was a significant independent predictor of worse PFS .

Example answer:
{"entities": [{"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "pAKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These point-wise significant results are not significant experiment-wise ( at P < 0.05 ) after correction for multiple testing .

Example answer:
{"entities": []}

Example input:
Sentence: There was a decrease in the perception of pinprick test .

Example answer:
{"entities": []}

Example input:
Sentence: In both types , purinoceptor desensitization with alpha , beta-methylene adenosine-5'-triphosphate ( alpha , beta-meATP ) caused further reductions at low frequencies ( < 10 Hz ) .

Example answer:
{"entities": [{"text": "alpha , beta-methylene adenosine-5'-triphosphate", "type": "ChemicalEntity"}, {"text": "alpha , beta-meATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 70 % reduction in Wnt signaling was also observed in the SF188 and SJ-GBM2 UCHL1 knockdowns ( KDs ) using a TCF-dependent TOPflash reporter assay .

Example answer:
{"entities": [{"text": "Wnt", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "TCF-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The hazard decreased 0.3-fold ( 0.7-1.7 , P=0.385 ) with glimepiride , 0.4-fold ( 0.7-1.3 , P=0.192 ) with gliclazide , and 0.4-fold ( 0.7-1.1 , P=0.09 ) with either .

Example answer:
{"entities": [{"text": "glimepiride", "type": "ChemicalEntity"}, {"text": "gliclazide", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

## Item biored:test:322
Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Since the first molecular characterization of an FH mutation by Bourgeron et al in 1994 , a series of reports of both FH deficiency patients and patients with MCUL/HLRRC have described 107 variants , of which 93 are thought to be pathogenic .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "FH deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MCUL/HLRRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: An unrelated individual with HHRH was a compound heterozygote for an 85-bp deletion in intron 10 and a G-to-A substitution at the last nucleotide in exon 7 .

## Item biored:test:281
Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Under isoflurane anesthesia , the MCA of 14 spontaneously hypertensive rats was occluded .

Example answer:
{"entities": [{"text": "isoflurane", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Maximal contraction to norepinephrine was modestly reduced in arteries from LNNA compared with control rats whereas the maximum contraction to ET-1 was significantly reduced ( 54 % control ) .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Isoproterenol induces primary loss of dystrophin in rat hearts : correlation with myocardial injury .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These rats also showed declines in left ventricular systolic pressure , maximum and minimum rate of developed left ventricular pressure , and elevation of left ventricular end-diastolic pressure and ST-segment .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Input:
Sentence: In isolated hearts , Iso induced a significantly greater increase in left ventricular ( LV ) pressure and maximal contraction ( +dP/dt ( max ) ) in the TGR than in the Sprague-Dawley ( SD ) rats .

## Item biored:test:303
Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: Direct sequencing of the TRbeta gene revealed a heterozygous transition 1284A > C in exon 9 resulting in substitution of glutamic acid 333 by aspartic acid residue ( E333D ) .

Example answer:
{"entities": [{"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "1284A > C", "type": "SequenceVariant"}, {"text": "glutamic acid 333 by aspartic acid", "type": "SequenceVariant"}, {"text": "E333D", "type": "SequenceVariant"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Her mother was heterozygous for the Asn45Ser mutation , and her father , for the nine-nucleotide deletion .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA sequencing analysis showed the patient to be a compound heterozygote for two mutations in the GPIX gene , a novel nine-nucleotide deletion starting at position 1952 of the gene that changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline ) and a previously reported point mutation that changes the codon asparagine ( AAC ) for serine ( AGC ) at residue 45 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "nine-nucleotide deletion starting at position 1952", "type": "SequenceVariant"}, {"text": "changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline )", "type": "SequenceVariant"}, {"text": "asparagine ( AAC ) for serine ( AGC ) at residue 45", "type": "SequenceVariant"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Input:
Sentence: The Chinese index patient and one of her siblings had a heterozygous mutation at codon 418 of exon 9 ( GAC -- > TAT ) that results in a substitution of aspartic acid by tyrosine .

## Item biored:test:312
Example input:
Sentence: Malondialdehyde level in BCNU-exposed group was higher than those in control groups and melatonin decreased malondialdehyde levels in BCNU group ( P < 0.01 ) , while there were no significant differences in the superoxide dismutase levels between these groups .

Example answer:
{"entities": [{"text": "Malondialdehyde", "type": "ChemicalEntity"}, {"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "tempol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "LNNA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Carotid arteries , vena cava , and sympathetic ganglia from LNNA rats had higher basal levels of superoxide compared with those from control rats .

Example answer:
{"entities": [{"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "superoxide", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Activities of heart tissue enzymic antioxidants and serum non-enzymic antioxidants levels rose significantly upon mangiferin administration as compared to ISPH-induced MI rats .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "ISPH-induced", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The heart tissue antioxidant enzymes such as superoxide dismutase , catalase , glutathione peroxidase , glutathione transferase and glutathione reductase activities , non-enzymic antioxidants such as cerruloplasmin , Vitamin C , Vitamin E and glutathione levels were altered in MI rats .

Example answer:
{"entities": [{"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "glutathione transferase", "type": "GeneOrGeneProduct"}, {"text": "glutathione reductase", "type": "GeneOrGeneProduct"}, {"text": "cerruloplasmin", "type": "GeneOrGeneProduct"}, {"text": "Vitamin C", "type": "ChemicalEntity"}, {"text": "Vitamin E", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of this study is to examine the role of gastric acid back-diffusion , mast cell histamine release , lipid peroxide ( LPO ) generation and mucosal microvascular permeability in modulating gastric hemorrhage and ulcer in rats with atherosclerosis induced by coadministration of vitamin D2 and cholesterol .

Example answer:
{"entities": [{"text": "histamine", "type": "ChemicalEntity"}, {"text": "lipid peroxide", "type": "ChemicalEntity"}, {"text": "LPO", "type": "ChemicalEntity"}, {"text": "gastric hemorrhage and ulcer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "atherosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin D2", "type": "ChemicalEntity"}, {"text": "cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Input:
Sentence: The level of lipid peroxidation was higher and the reduced glutathione concentration was lower in the MA-treated rats .

## Item biored:test:339
Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Two patients , ages 69 and 44 years old , demonstrated a degree of severity `` Bad '' according to best-corrected vision and corneal commitment .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The second objective was to employ RB1 molecular deletion and microsatellite-based linkage analysis as laboratory tools , while counseling families with a history of retinoblastoma ( RB ) .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "retinoblastoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mild glycine encephalopathy ( NKH ) in a large kindred due to a silent exonic GLDC splice mutation .

Example answer:
{"entities": [{"text": "glycine encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NKH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The most relevant adverse event was peripheral neuropathy , which occurred in 78 % of the patients ( grade II , 38 % ; grade III , 21 % ) and led to treatment discontinuation in 6 % .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: NPHP can be associated with retinal degeneration ( Senior-Loken syndrome ) , brainstem and cerebellar anomalies ( Joubert syndrome ) , or liver fibrosis .

Example answer:
{"entities": [{"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinal degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Senior-Loken syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebellar anomalies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : Cone dystrophy with supernormal rod response ( CDSRR ) is a retinal disorder characterized by reduced visual acuity , color vision defects , and specific alterations of ERG responses that feature elevated scotopic b-wave amplitudes at high luminance intensities .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinal disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "color vision defects", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Our data suggest that in a model representative of human retinopathy of prematurity , NOX4 was increased at a time point when IVNV developed .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In full-term children with retinal detachment only 15 % appear to have the full features of Norrie disease and this is important for counselling parents on the possible long-term outcome .

## Item biored:test:357
Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The child had a height of -4 SD , elevated serum GH concentrations , abnormally low serum IGF-I and IGFBP-3 concentrations and normal GHBP concentrations .

Example answer:
{"entities": [{"text": "GH", "type": "GeneOrGeneProduct"}, {"text": "IGF-I", "type": "GeneOrGeneProduct"}, {"text": "IGFBP-3", "type": "GeneOrGeneProduct"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To date , 46 mutations in the PYGM gene have been detected in GSD-V patients .

Example answer:
{"entities": [{"text": "PYGM", "type": "GeneOrGeneProduct"}, {"text": "GSD-V", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Our results indicate that the PSA/ARE GG genotype confers an increased risk of PC especially among younger men .

Example answer:
{"entities": [{"text": "PSA/ARE", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: An important subset of children with nonketotic hyperglycinemia are atypical variants who present in a heterogeneous manner .

Example answer:
{"entities": [{"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , the frequency of GJB2 variants was studied in 406 and 183 apparently unrelated children from Kenya and Sudan , respectively , with mostly severe to profound non-syndromic deafness .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "non-syndromic deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our findings suggest that the additive effects of both mutations in the GPIX gene are responsible for the BSS phenotype of the patient .

Example answer:
{"entities": [{"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Input:
Sentence: This study provides further evidence for the phenotypical heterogeneity of GS and its association with severe manifestations in children .

## Item biored:test:340
Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we describe the characterization of the rs368698783 ( +25 G- > A ) polymorphism of the Ag-globin gene associated in b ( 0 ) 39 thalassemia patients with high HbF in erythroid precursor cells .

Example answer:
{"entities": [{"text": "rs368698783", "type": "SequenceVariant"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Ag-globin", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HbF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Haplotype reconstruction via the expectation-maximization algorithm showed in both populations that only the haplotype containing the minor ( W ) allele at codon 620 was associated with T1D ( OR=2.26 , 95 % CI 1.68-3.02 in Czechs , OR=14.8 , 95 % CI 2.0-651 in Azeri ) or JIA ( OR=2.43 , 95 % CI 1.66-3.56 in Czechs ) .

Example answer:
{"entities": [{"text": "( W ) allele at codon 620", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using self-reported data on ischemic heart disease to evaluate the impact of the PON 192Q/R polymorphism on susceptibility to CHD , we found only a nonsignificant trend of 192RR homozygosity in women being a risk factor .

Example answer:
{"entities": [{"text": "ischemic heart disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PON", "type": "GeneOrGeneProduct"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Gene polymorphisms implicated in influencing susceptibility to venous and arterial thromboembolism : frequency distribution in a healthy German population .

## Item biored:test:315
Example input:
Sentence: T and C alleles of SOD2 T2734C individually were linked to patients with bullous and erythematous erysipelas , respectively .

Example answer:
{"entities": [{"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "erythematous erysipelas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In two unrelated pedigrees of Alpers ' syndrome , each affected child was found to carry a homozygous mutation in exon 17 of the POLG locus that led to a Glu873Stop mutation just upstream of the polymerase domain of the protein .

Example answer:
{"entities": [{"text": "Alpers ' syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG", "type": "GeneOrGeneProduct"}, {"text": "Glu873Stop", "type": "SequenceVariant"}]}

Example input:
Sentence: Peroxisomal proliferator activated receptor-gamma deficiency in a Canadian kindred with familial partial lipodystrophy type 3 ( FPLD3 ) .

Example answer:
{"entities": [{"text": "Peroxisomal proliferator activated receptor-gamma", "type": "GeneOrGeneProduct"}, {"text": "familial partial lipodystrophy type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A two base pair deletion in the PQBP1 gene is associated with microphthalmia , microcephaly , and mental retardation .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We also detected p.R34X among normal control samples of African-American and northern European origins , raising the possibility that p.R34X and other mutations of TMC1 are prevalent contributors to the genetic load of deafness across a variety of populations and continents .

Example answer:
{"entities": [{"text": "p.R34X", "type": "SequenceVariant"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A major disease-causing gene for HypoPP has been identified as CACNA1S , which encodes the skeletal muscle calcium channel alpha-subunit with four transmembrane domains ( I-IV ) , each with six transmembrane segments ( S1-S6 ) .

Example answer:
{"entities": [{"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "skeletal muscle calcium channel alpha-subunit", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Intronic deletions in the SLC34A3 gene cause hereditary hypophosphatemic rickets with hypercalciuria .

## Item biored:test:387
Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: No TS point mutation was detected in primary tumors or metastases .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A naturalistic auditory location discrimination method was used to evaluate this question using an animal model of status epilepticus .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: These 2 SNPs had a false discovery rate for multitest correction of < 0.05 , and therefore a > 95 % probability of being considered as proven .

Example answer:
{"entities": []}

Example input:
Sentence: If confirmed in larger series , routine testing for these translocations may be indicated for this subset of GIST .

Example answer:
{"entities": [{"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The challenge was considered positive if one or more of the following appeared : erythema , rush or urticaria-angioedema .

Example answer:
{"entities": [{"text": "erythema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "urticaria-angioedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Example input:
Sentence: The diagnosis of LCD or GCD was made on the basis of clinical and/or histopathological evaluation .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It could be proved by the observation of a positive stain reaction and the enlarged collagen fibers as well as hyperplastic fibroblasts under microscopes .

Example answer:
{"entities": [{"text": "collagen", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This could not be confirmed by any technical examination .

## Item biored:test:347
Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Significant differences were detected in genotypic distribution ( p = 0.04 ) as well as the allelic frequency ( p = 0.003 ) between the SHCM patients and controls .

Example answer:
{"entities": [{"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Association and Hardy-Weinberg equilibrium checking were assessed by Chi-square test and Mann-Whitney U test .

Example answer:
{"entities": []}

Example input:
Sentence: In the Basque area , estimates of Wahlund 's effect for both genetic markers showed no statistical difference between Basque subpopulations .

Example answer:
{"entities": []}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotype frequencies of the G472A SNP varied significantly ( P = 0.029 ) among the three main ethnic/cultural groups ( Caucasians , Hispanics , and African Americans ) .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: No Hardy Weinberg disequilibrium and no significant difference in allele frequencies between patients and controls were observed for any variation .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: The distribution of glycoprotein Ia 807C > T deviated significantly from the Hardy-Weinberg equilibrium , and a comparison with previously published data indicates marked region and ethnicity dependent differences in the genotype distributions of some other factors .

## Item biored:test:389
Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: Viruses were evaluated for replication in SCID mice transplanted with human hepatoma cells ( SCID-HuH-7 mice ) , in mosquitoes , and in rhesus monkeys .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hepatoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCID-HuH-7", "type": "CellLine"}, {"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: All patients had some response to the combined therapy and five of the seven went into complete remission after one or two courses of AraG/VP/CPM .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AraG/VP/CPM", "type": "ChemicalEntity"}]}

Example input:
Sentence: Her intracranial pressure remained elevated despite maximal medical therapy .

Example answer:
{"entities": []}

Example input:
Sentence: Correspondingly , CD4 ( + ) T cells were the major producers within an accelerated and amplified IL-10 response during the early stage of secondary malaria infection .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "malaria infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She had a gradual return of motor function and ability of feeling Foley catheter .

Example answer:
{"entities": []}

Example input:
Sentence: Consistently , the surviving CD4 ( + ) YFP ( + ) GFP ( + ) T cell-derived cells were unresponsive and failed to proliferate during the early phase of secondary infection .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , the main outcome measure was the sequencing of genomic DNA from peripheral blood samples of 41 women with POF and 36 fertile women ( controls ) .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At discharge , she had complete recovery of neurological and hepatic functions .

Example answer:
{"entities": []}

Example input:
Sentence: The patient achieved a partial response 6 months after the initiation of the S-1 treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "S-1", "type": "ChemicalEntity"}]}

Input:
Sentence: She had a complete sustained viral response .

## Item biored:test:305
Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cocaine causes memory and learning impairments in rats : involvement of nuclear factor kappa B and oxidative stress , and prevention by topiramate .

Example answer:
{"entities": [{"text": "Cocaine", "type": "ChemicalEntity"}, {"text": "memory and learning impairments", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "topiramate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dopamine is not essential for the development of methamphetamine-induced neurotoxicity .

Example answer:
{"entities": [{"text": "Dopamine", "type": "ChemicalEntity"}, {"text": "methamphetamine-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Methamphetamine-induced neurotoxicity and microglial activation are not mediated by fractalkine receptor signaling .

Example answer:
{"entities": [{"text": "Methamphetamine-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Effect of alpha-tocopherol and deferoxamine on methamphetamine-induced neurotoxicity .

## Item biored:test:279
Example input:
Sentence: The metabolic responses to isoprenaline in dogs ( an increase in circulating glucose , lactate and free fatty acids ) were all blocked by ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}, {"text": "dogs", "type": "OrganismTaxon"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "fatty acids", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The mechanism of isoproterenol-induced myocardial damage is unknown , but a mismatch of oxygen supply vs. demand following coronary hypotension and myocardial hyperactivity is the best explanation for the complex morphological alterations observed .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial hyperactivity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At dose levels of ( + ) -propranolol which attenuated the responses to isoprenaline , there was a significant prolongation of the PR interval of the electrocardiogram.3 .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The beta-adrenergic receptors ( beta-AR ) are G protein-coupled receptors activated by epinephrine and norepinephrine and are involved in a variety of their physiological functions .

Example answer:
{"entities": [{"text": "beta-adrenergic receptors", "type": "GeneOrGeneProduct"}, {"text": "beta-AR", "type": "GeneOrGeneProduct"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "norepinephrine", "type": "ChemicalEntity"}]}

Input:
Sentence: In this study we aimed at studying the involvement of the brain RAS in the cardiac reactivity to the beta-adrenoceptor ( beta-AR ) agonist isoproterenol ( Iso ) .

## Item biored:test:351
Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : Atrioventricular septal defects ( AVSDs ) occur as clinical defects of several different syndromes , as autosomal dominant defects , and as sporadically occurring malformations .

Example answer:
{"entities": [{"text": "Atrioventricular septal defects", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AVSDs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant defects", "type": "DiseaseOrPhenotypicFeature"}, {"text": "malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prehospital care providers who are managing any patient with a syncopal episode that fails to recover within a reasonable time frame should consider the Bezold-Jarisch reflex as the cause and manage the patient accordingly .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "syncopal episode", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Early correct diagnosis of the syndrome is crucial for appropriate preventive care and therapy .

Example answer:
{"entities": []}

Example input:
Sentence: Histopathologically , typical findings were observed in the cerebella from the control groups , but the findings consistent with early embryonic development were noted in BCNU-exposed cortical dysplasia group .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Women were significantly more likely to experience lactic acidosis , while men were significantly more likely to experience immune reconstitution syndrome ( p < 0.05 ) .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "lactic acidosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "immune reconstitution syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genetic basis of the other forms remain unknown , including the early-onset , recessive form with Mallory body-like inclusions ( MB-DRMs ) , first described in five related German patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Bernard-Soulier syndrome ( BSS ) is a rare inherited bleeding disorder due to quantitative or qualitative abnormalities in the platelet glycoprotein ( GP ) Ib/IX/V complex , the major von Willebrand factor receptor .

Example answer:
{"entities": [{"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inherited bleeding disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycoprotein ( GP ) Ib/IX/V", "type": "GeneOrGeneProduct"}, {"text": "von Willebrand factor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alpers ' syndrome is a fatal neurogenetic disorder first described more than 70 years ago .

Example answer:
{"entities": [{"text": "Alpers ' syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurogenetic disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Based on the early onset and normocalciuria , Bartter syndrome was diagnosed first .

## Item biored:test:373
Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Blood sampling , karyotype , hormonal dosage , ultrasound , and ovarian biopsy were carried out on most patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : The first part of this study was an 8-week , multicenter , randomized , double-blind , placebo controlled , parallel-group trial .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : DNA samples of 126 SIDS cases and 261 controls were investigated .

Example answer:
{"entities": [{"text": "SIDS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A subgroup of 512 subjects underwent a hyperinsulinemic-euglycemic clamp .

Example answer:
{"entities": [{"text": "hyperinsulinemic-euglycemic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Input:
Sentence: METHODS : The study group comprised 40 patients undergoing Sestamibi-SPECT/dobutamine stress test .

## Item biored:test:272
Example input:
Sentence: Anemia and hepatitis often occur within 12 weeks of initiating generic HAART .

Example answer:
{"entities": [{"text": "Anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One month after starting the antiviral therapy , the patient was admitted to the hospital because he developed rhabdomyolysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

Example answer:
{"entities": [{"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hemoglobin", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "hepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaundice", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Input:
Sentence: Hemoglobin concentrations decrease mainly as a result of ribavirin-induced hemolysis , and this anemia can be problematic in patients with HCV infection , especially those who have comorbid renal or cardiovascular disorders .

## Item biored:test:354
Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: Sequence analysis of aggrecan complementary DNA from an affected individual revealed homozygosity for a missense mutation ( c.6799G -- > A ) that predicts a p.D2267N amino acid substitution in the C-type lectin domain within the G3 domain of aggrecan .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "c.6799G -- > A", "type": "SequenceVariant"}, {"text": "p.D2267N", "type": "SequenceVariant"}]}

Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: Three aberrantly spliced cDNA species were identified : exon 22 and exon 22 to 23 skipping , and insertion of an 87-base pair cryptic exon .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: Analysis of PTPN22 transcripts from a subject heterozygous for this variant indicated that it interfered with normal mRNA splicing , resulting in a premature termination codon after exon 17 .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Analysis of complementary DNA showed that the heterozygous nucleotide change c.2633+1G > C caused the appearance of 2 RNA molecules , 1 normal transcript and 1 skipping the entire exon 22 ( r.2521_2634del ) .

## Item biored:test:334
Example input:
Sentence: RESULTS : In the Czechs , all three SNPs were in a tight linkage disequlibrium , while in the Azeri , the linkage disequlibrium was limited to between the promoter and 3'-UTR polymorphism , D ' ( -1123 , +2740 ) =0.99 , r ( 2 ) =0.72 .

Example answer:
{"entities": []}

Example input:
Sentence: The Typically Deleted Region in the 22q11.21 subband ( here called TDR22 ) is very gene-dense , and the extent of the deletion has been defined precisely in several studies .

Example answer:
{"entities": []}

Example input:
Sentence: RT-PCR analysis , performed on a patient homozygous for the intronic deletion ( c.609+28_610-16del ) , failed to detect any GNPTG RNA transcripts .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also observed a 20 bp insertion/deletion polymorphism 1,109 bp upstream of the initiation codon , but this variant was not associated with prostate cancer .

Example answer:
{"entities": [{"text": "20 bp insertion/deletion polymorphism 1,109 bp upstream of the initiation codon", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We used high-resolution karyotyping to confirm a deletion ( 10-12Mb ) [ del ( 1 ) ( p31.2p32.3 ) ] and found no structural abnormalities in the father , suggesting a de novo event .

Example answer:
{"entities": [{"text": "deletion ( 10-12Mb )", "type": "SequenceVariant"}, {"text": "del ( 1 ) ( p31.2p32.3 )", "type": "SequenceVariant"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subsequent mutation analysis of PQBP1 , located within the delineated linkage interval in Xp11.23 , revealed a 2-bp deletion , c.461_462delAG , that cosegregated with the disease .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "c.461_462delAG", "type": "SequenceVariant"}]}

Example input:
Sentence: We found a single nucleotide deletion c.342delA , located in exon 3 , which resulted in a frameshift at amino acid position 58 ( p.Arg58fs or p.R58fs ) .

Example answer:
{"entities": [{"text": "c.342delA", "type": "SequenceVariant"}, {"text": "p.Arg58fs", "type": "SequenceVariant"}, {"text": "p.R58fs", "type": "SequenceVariant"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Input:
Sentence: Furthermore , a previously described 14-bp deletion located in the 5 ' unstranslated region of the NDP gene was detected in three cases of regressed ROP .

## Item biored:test:358
Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The genetic basis of the other forms remain unknown , including the early-onset , recessive form with Mallory body-like inclusions ( MB-DRMs ) , first described in five related German patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DiGeorge and Velocardiofacial syndromes ( DGS/VCFS ) are endowed by a similar complex phenotype including cardiovascular , craniofacial , and thymic malformations , and are associated with heterozygous deletions of 22q11 chromosomal band .

Example answer:
{"entities": [{"text": "DiGeorge and Velocardiofacial syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular , craniofacial , and thymic malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Using patient demographics , tumor characteristics , and CGP , we show that GIST lacking alterations in canonical genes occur in younger patients , frequently metastasize to lymph nodes , and most contain deleterious genomic alterations , including gene fusions involving FGFR1 and NTRK3 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "metastasize to lymph nodes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : By clinical examination , the patients and the pedigrees were divided into the following three groups : AN , coloboma of iris and choroids , and the anterior segment malformations including peters anomaly .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroids", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "peters anomaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : While mutations were absent in non-GH-secreting adenoma patients , germline AIP mutations can be found in children and adolescents with GH-secreting tumours , even in the absence of family history .

Example answer:
{"entities": [{"text": "adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "GH-secreting tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: It also shows the independent segregation of familial cavernomatosis and GS .

## Item biored:test:302
Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA sequencing analysis showed the patient to be a compound heterozygote for two mutations in the GPIX gene , a novel nine-nucleotide deletion starting at position 1952 of the gene that changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline ) and a previously reported point mutation that changes the codon asparagine ( AAC ) for serine ( AGC ) at residue 45 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "nine-nucleotide deletion starting at position 1952", "type": "SequenceVariant"}, {"text": "changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline )", "type": "SequenceVariant"}, {"text": "asparagine ( AAC ) for serine ( AGC ) at residue 45", "type": "SequenceVariant"}]}

Example input:
Sentence: An analysis of the multiple single-nucleotide polymorphisms in SP-A demonstrated that homozygosity for alleles encoding lysine ( in 1A1 ) rather than glutamine ( in 1A5 ) at amino acid 223 in the carbohydrate recognition domain was associated with an increased risk of meningococcal disease ( OR , 6.7 ; 95 % CI , 1.4-31.5 ) .

Example answer:
{"entities": [{"text": "SP-A", "type": "GeneOrGeneProduct"}, {"text": "lysine ( in 1A1 ) rather than glutamine ( in 1A5 ) at amino acid 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Gene polymorphism resulting in the substitution of glutamine with lysine at residue 223 in the carbohydrate recognition domain of SP-A2 increases susceptibility to meningococcal disease , as well as the risk of death .

Example answer:
{"entities": [{"text": "glutamine with lysine at residue 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "SP-A2", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The Turkish patient and her affected relatives all had a heterozygous A to G transition at codon 557 ( AAG -- > GAG ) of exon 10 of MEN1 that results in a replacement of lysine by glutamic acid .

## Item biored:test:260
Example input:
Sentence: Catechol-O-methyltransferase ( COMT ) catalyzes the breakdown of catechol neurotransmitters , including dopamine , which plays a prominent role in drug reward .

Example answer:
{"entities": [{"text": "Catechol-O-methyltransferase", "type": "GeneOrGeneProduct"}, {"text": "COMT", "type": "GeneOrGeneProduct"}, {"text": "catechol neurotransmitters", "type": "ChemicalEntity"}, {"text": "dopamine", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: BACKGROUND : The loss of noradrenergic neurones of the locus coeruleus is a major feature of Alzheimer 's disease ( AD ) .

Example answer:
{"entities": [{"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although marked reductions of CB expression have been observed in the brains of mice and humans with Alzheimer disease ( AD ) , it is unknown whether these changes contribute to AD-related dysfunction .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "Alzheimer disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD-related", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : KCa3.1 channels expression and cell localization in the brains of AD patients and APP/PS1 mice model were measured by immunoblotting and immunostaining .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: These mediators may also have a pivotal role in the control of neurodegenerative processes associated with AD .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: reduced significantly the brain acetylcholinesterase activity and cholesterol levels in young and aged mice .

Example answer:
{"entities": [{"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Importantly , this is the first experimental evidence that removal of CB from amyloid precursor protein/presenilin transgenic mice aggravates AD pathogenesis , suggesting that CB has a critical role in AD pathogenesis .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "amyloid precursor", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : The intermediate-conductance Ca2+-activated K+ channel KCa3.1 was recently shown to control the phenotype switch of reactive astrogliosis ( RA ) in Alzheimer 's disease ( AD ) .

Example answer:
{"entities": [{"text": "intermediate-conductance Ca2+-activated K+ channel", "type": "GeneOrGeneProduct"}, {"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "reactive astrogliosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The choline acetyltransferase ( ChAT ) activator , which enhances cholinergic transmission via an augmentation of the enzymatic production of acetylcholine ( ACh ) , is an important factor in the treatment of Alzheimer 's disease ( AD ) .

## Item biored:test:337
Example input:
Sentence: Mild glycine encephalopathy ( NKH ) in a large kindred due to a silent exonic GLDC splice mutation .

Example answer:
{"entities": [{"text": "glycine encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NKH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We next sequenced PTPN11 in DNA samples from 54 patients with the multiple enchondromatosis disorders Ollier disease or Maffucci syndrome , but found no coding sequence PTPN11 mutations .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "enchondromatosis disorders Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSION : Two novel mutations within the coding region of the NDP gene were found , one associated with a severe disease phenotypes of Norrie disease and the other with FEVR .

## Item biored:test:374
Example input:
Sentence: Low activity of patient plasma butyrylcholinesterase with butyrylthiocholine ( BTC ) and benzoylcholine , and values of dibucaine and fluoride numbers fit with heterozygous atypical silent genotype .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "butyrylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "butyrylthiocholine", "type": "ChemicalEntity"}, {"text": "BTC", "type": "ChemicalEntity"}, {"text": "benzoylcholine", "type": "ChemicalEntity"}, {"text": "dibucaine", "type": "ChemicalEntity"}, {"text": "fluoride", "type": "ChemicalEntity"}]}

Example input:
Sentence: Echocardiography was performed at 3 and 28 days post-MI , whereas the haemodynamics test was performed 28 days post-MI .

Example answer:
{"entities": []}

Example input:
Sentence: Three time domain indexes of hemodynamic variability were employed : the standard deviation of mean arterial pressure as a measure of blood pressure variability and the standard deviation of beat-to-beat intervals ( SDRR ) and the root mean square of successive differences in R-wave-to-R-wave intervals as measures of heart rate variability .

Example answer:
{"entities": []}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Systolic blood pressure ( SBP ) was measured on alternate days using the tail-cuff method .

Example answer:
{"entities": []}

Example input:
Sentence: H9c2 cells were treated with Dox ( 1 uM ) and/or BDNF ( 400 ng/ml ) for 24 hrs .

Example answer:
{"entities": []}

Example input:
Sentence: Patients with essential hypertension ( mean sitting diastolic BP [ MSDBP ] , > or =95 mm Hg and < 110 mm Hg ) were randomized to 1 of 8 treatment groups : VAL 160 or 320 mg ; HCTZ 12.5 or 25 mg ; VAL/HCTZ 160/12.5 , 320/12.5 , or 320/25 mg ; or placebo .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hemodynamic parameters and lead II electrocardiograph were monitored and recorded continuously .

Example answer:
{"entities": []}

Example input:
Sentence: Prolongation of the QT interval in the ECG of patients with torsade de pointes ( TdP ) has been reported in methadone users .

Example answer:
{"entities": [{"text": "Prolongation of the QT interval", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "torsade de pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Input:
Sentence: Simultaneous measurements of ECG and brachial artery dP/dtejc were performed at each dobutamine level .

## Item biored:test:243
Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We did not observe any correlation between the Ser1245Cys polymorphism of the hOGG1 gene and gastric cancer , including subjects with impaired DNA repair and/or high levels of endogenous oxidative DNA lesions .

Example answer:
{"entities": [{"text": "Ser1245Cys", "type": "SequenceVariant"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have investigated three other single-nucleotide polymorphisms in the hPER2 gene , one downstream of the transcription start site ( C-1228T ) , one in exon 2 in the 5'-untranslated region ( 5'-UTR ) ( C111G ) , and one missense mutation ( G3853A ) causing a glycine to glutamine substitution in the predicted protein .

Example answer:
{"entities": [{"text": "hPER2", "type": "GeneOrGeneProduct"}, {"text": "C-1228T", "type": "SequenceVariant"}, {"text": "C111G", "type": "SequenceVariant"}, {"text": "G3853A", "type": "SequenceVariant"}, {"text": "glycine to glutamine", "type": "SequenceVariant"}]}

Example input:
Sentence: Polymorphic MLH1 and risk of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genetic polymorphism rs1052133 , which leads to substitution of the amino acid at codon 326 from Ser to Cys , shows functional differences , namely a decrease in enzyme activity in hOGG1-Cys326 .

Example answer:
{"entities": [{"text": "rs1052133", "type": "SequenceVariant"}, {"text": "326 from Ser to Cys", "type": "SequenceVariant"}, {"text": "hOGG1-Cys326", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Gene polymorphism resulting in the substitution of glutamine with lysine at residue 223 in the carbohydrate recognition domain of SP-A2 increases susceptibility to meningococcal disease , as well as the risk of death .

Example answer:
{"entities": [{"text": "glutamine with lysine at residue 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "SP-A2", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We performed a case-control study to test the association between two polymorphisms in the hMSH2 gene : an A -- > G transition at 127 position producing an Asn -- > Ser substitution at codon 127 ( the Asn127Ser polymorphism ) and a G -- > A transition at 1032 position resulting in a Gly -- > Asp change at codon 322 ( the Gly322Asp polymorphism ) and breast cancer risk and cancer progression .

## Item biored:test:379
Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TIEG1 deficiency confers enhanced myocardial protection in the infarcted heart by mediating the Pten/Akt signalling pathway .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "infarcted heart", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Pten/Akt", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolongation of the QT interval in the ECG of patients with torsade de pointes ( TdP ) has been reported in methadone users .

Example answer:
{"entities": [{"text": "Prolongation of the QT interval", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "torsade de pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: hiPS-CMs using MEA system and FPDc can predict the effects of drug candidates on QT interval .

Example answer:
{"entities": []}

Example input:
Sentence: The aim of this study is to show that FPD from MEA ( Multielectrode array ) of hiPS-CMs can detect QT prolongation induced by multichannel blockers .

Example answer:
{"entities": [{"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The protective role of mangiferin was analyzed by triphenyl tetrazolium chloride ( TTC ) test used for macroscopic enzyme mapping assay of the ischemic myocardium .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "triphenyl tetrazolium chloride", "type": "ChemicalEntity"}, {"text": "TTC", "type": "ChemicalEntity"}, {"text": "ischemic myocardium", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In these trials , Hp typing of 69 DM individuals and treating those with the Hp 2-2 with vitamin E prevented one myocardial infarct , stroke or cardiovascular death .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "myocardial infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Input:
Sentence: CONCLUSIONS : If ECG alone is used for specificity , the combination with dP/dtejc improved the sensitivity of the test and could be a cost-savings alternative to cardiac imaging or perfusion studies to detect myocardial ischemia , especially in patients unable to exercise .

## Item biored:test:311
Example input:
Sentence: Estrogen replacement ( 17beta-estradiol subcutaneous pellet , 14.2 microg/day , 12 wk ) of Ovx rats restored the hemodynamic and locomotor effects of alpha-methyldopa to sham-operated levels .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: In both types , purinoceptor desensitization with alpha , beta-methylene adenosine-5'-triphosphate ( alpha , beta-meATP ) caused further reductions at low frequencies ( < 10 Hz ) .

Example answer:
{"entities": [{"text": "alpha , beta-methylene adenosine-5'-triphosphate", "type": "ChemicalEntity"}, {"text": "alpha , beta-meATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: These findings suggest that estrogen downregulates alpha2- but not I1-receptor-mediated hypotension and highlight a role for the cardiac autonomic control in alpha-methyldopa-estrogen interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "alpha2- but not", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-methyldopa-estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chronic T treatment significantly decreased 5-HT and 5-HIAA in certain brain areas , but to a much lesser extent than PCPA .

Example answer:
{"entities": [{"text": "T", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HIAA", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: alpha-TC and DFO attenuated the MA-induced hyperthermia as well as the alterations in the locomotor activity .

## Item biored:test:401
Example input:
Sentence: A Kruskal-Wallis 1-way analysis of variance indicated a significant difference among the 4 treatment groups ( H = 15.34 ; P < 0.001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The homeostasis model assessment of insulin resistance also differed significantly among groups ( F ( 33 ) = 4.92 ; P = .01 ) ( clozapine > olanzapine > risperidone ) ( clozapine vs risperidone , t ( 33 ) = 2.94 ; P = .006 ; olanzapine vs risperidone , t ( 33 ) = 2.42 ; P = .02 ) .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: The dose of ( - ) -propranolol was significantly smaller than that of ( + ) -propranolol in both species but much higher than that required to produce evidence of beta-blockade.8 .

Example answer:
{"entities": []}

Example input:
Sentence: Thromboxane levels were not significantly affected by any of the treatments , indicating that the effects seen were attributable to inhibition of COX-2 , but not COX-1 .

Example answer:
{"entities": [{"text": "Thromboxane", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "COX-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The racemic compound was significantly less potent than either isomer.6 .

Example answer:
{"entities": []}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Many such agents have also found a place in skin care products .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : Pharmacokinetic differences in statins are an important consideration for assessing the risk of potential drug interactions .

Example answer:
{"entities": [{"text": "statins", "type": "ChemicalEntity"}]}

Example input:
Sentence: A comparison of individual selective and unselective cyclooxygenase inhibitors suggests substance-specific differences , which may depend on differences in pharmacokinetic parameters or inhibitory potency and may be contributed by prostaglandin-independent effects .

Example answer:
{"entities": [{"text": "cyclooxygenase inhibitors", "type": "ChemicalEntity"}, {"text": "prostaglandin-independent", "type": "ChemicalEntity"}]}

Example input:
Sentence: If confirmed , this may be important because most Indian patients receive the cheaper older sulphonylureas , and present guidelines do not distinguish between individual agents .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "sulphonylureas", "type": "ChemicalEntity"}]}

Input:
Sentence: Any true difference between the agents is small and not likely to be clinically significant .

## Item biored:test:314
Example input:
Sentence: These results indicate that the TSPO ligand etifoxine attenuates brain injury and inflammation after ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "etifoxine", "type": "ChemicalEntity"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Concomitant curcumin administration prevented the cognitive impairment and decreased the increased oxidative stress induced by these antiepileptic drugs .

Example answer:
{"entities": [{"text": "curcumin", "type": "ChemicalEntity"}, {"text": "cognitive impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antiepileptic drugs", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The study investigates if alpha-lipoic acid is neuroprotective against chemotherapy induced neurotoxicity , if mitochondrial damage plays a critical role in toxic neurodegenerative cascade , and if neuroprotective effects of alpha-lipoic acid depend on mitochondria protection .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "toxic neurodegenerative cascade", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid prevents mitochondrial damage and neurotoxicity in experimental chemotherapy neuropathy .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This suggests that alpha-TC and DFO ameliorate the MA-induced neuronal damage by decreasing the level of oxidative stress .

## Item biored:test:213
Example input:
Sentence: This shift in balance may contribute to increased bladder dysfunction in VIP ( -/- ) mice with bladder inflammation and altered neurochemical expression in micturition pathways .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Carotid arteries , vena cava , and sympathetic ganglia from LNNA rats had higher basal levels of superoxide compared with those from control rats .

Example answer:
{"entities": [{"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "superoxide", "type": "ChemicalEntity"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: VCM administration to control rats significantly increased renal malondialdehyde ( MDA ) and urinary N-acetyl-beta-d-glucosaminidase ( NAG , a marker of renal tubular injury ) excretion but decreased superoxide dismutase ( SOD ) and catalase ( CAT ) activities .

## Item biored:test:290
Example input:
Sentence: LF lowered ( P < 0.01 ) and dose dependently prevented ( P < 0.001 ) Dex-induced hypertension .

Example answer:
{"entities": [{"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "Dex-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Endothelial-dependent relaxation and eNOS mRNA expression were greater in the Dex + Ato group than in the Dex only group ( P < 0.05 and P < 0.0001 , respectively ) .

Example answer:
{"entities": [{"text": "eNOS", "type": "GeneOrGeneProduct"}, {"text": "Dex", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the present study , we investigated whether 50 mg/kg per day , p.o. , Ato could prevent endothelial NO synthase ( eNOS ) downregulation and the increase in O2- in Sprague-Dawley ( SD ) rats , thereby reducing blood pressure .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "endothelial NO synthase", "type": "GeneOrGeneProduct"}, {"text": "eNOS", "type": "GeneOrGeneProduct"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "tempol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "LNNA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chronic administration of LF strongly reduced the blood pressure and production of ROS and improved antioxidant capacity in Dex-induced hypertension , suggesting the role of inhibition of oxidative stress as another mechanism of antihypertensive action of LF .

Example answer:
{"entities": [{"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "Dex-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Treatment with Ato improved endothelial function , reduced superoxide production and reduced SBP in Dex-treated SD rats .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}, {"text": "Dex-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Aortic superoxide production was lower in the Dex + Ato group compared with the group treated with Dex alone ( P < 0.0001 ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Input:
Sentence: Atorva reversed dex-induced hypertension ( 129 +/- 0.6 mmHg , vs. 135 +/- 0.6 mmHg P ' < 0.05 ) and decreased plasma superoxide ( 7931 +/- 392.8 dex , 1187 +/- 441.2 atorva + dex , P < 0.0001 ) .

## Item biored:test:287
Example input:
Sentence: Antioxidant effects of bovine lactoferrin on dexamethasone-induced hypertension in rat .

Example answer:
{"entities": [{"text": "Antioxidant", "type": "ChemicalEntity"}, {"text": "bovine", "type": "OrganismTaxon"}, {"text": "lactoferrin", "type": "GeneOrGeneProduct"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Treatment with Ato improved endothelial function , reduced superoxide production and reduced SBP in Dex-treated SD rats .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}, {"text": "Dex-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In the present study , we investigated whether 50 mg/kg per day , p.o. , Ato could prevent endothelial NO synthase ( eNOS ) downregulation and the increase in O2- in Sprague-Dawley ( SD ) rats , thereby reducing blood pressure .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "endothelial NO synthase", "type": "GeneOrGeneProduct"}, {"text": "eNOS", "type": "GeneOrGeneProduct"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Anti-oxidant effects of atorvastatin in dexamethasone-induced hypertension in the rat .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Input:
Sentence: To assess the antioxidant effects of atorvastatin ( atorva ) on dexamethasone ( dex ) -induced hypertension , 60 male Sprague-Dawley rats were treated with atorva 30 mg/kg/day or tap water for 15 days .

## Item biored:test:375
Example input:
Sentence: The brains were sectioned along coronal planes spanning the distribution of ischemia produced by MCAO .

Example answer:
{"entities": [{"text": "ischemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of this study is to show that FPD from MEA ( Multielectrode array ) of hiPS-CMs can detect QT prolongation induced by multichannel blockers .

Example answer:
{"entities": [{"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the periphery of the ischemic territory , SG in the cortex was greater ( less edema accumulation ) in the hypertensive group ( 1.041 +/- 0.001 vs 1.039 +/- 0.001 , P less than 0.05 ) .

Example answer:
{"entities": [{"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Comparable histological injuries in patients with hypoxia/ischemia and TD have been described in the thalamus and mammillary bodies , suggesting a congruency between the cellular responses to these stresses .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hypoxia/ischemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Twenty-one of the 24 patients did not have evidence of new cerebral ischemic injury , but seizures were likely due to ischemic brain injury in 3 patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cerebral ischemic injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic brain injury", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In 19 of the 40 patients perfusion defects compatible with ischemia were detected on SPECT .

## Item biored:test:317
Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The FH mutation database : an online database of fumarate hydratase mutations involved in the MCUL ( HLRCC ) tumor syndrome and congenital fumarase deficiency .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "fumarate hydratase", "type": "GeneOrGeneProduct"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HLRCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fumarase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The G-395A polymorphism of the human Klotho gene is associated with EH and may be a potential regulatory site .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Since the first molecular characterization of an FH mutation by Bourgeron et al in 1994 , a series of reports of both FH deficiency patients and patients with MCUL/HLRRC have described 107 variants , of which 93 are thought to be pathogenic .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "FH deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MCUL/HLRRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: OBJECTIVE : Our objective was to determine whether mutations in the SLC34A3 gene , which encodes sodium-phosphate cotransporter type IIc , are responsible for the occurrence of HHRH .

## Item biored:test:330
Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RT-PCR analysis , performed on a patient homozygous for the intronic deletion ( c.609+28_610-16del ) , failed to detect any GNPTG RNA transcripts .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We progressively screened DNA samples from 613 individuals with ID initially for the most frequent ARX mutations ( c.304ins ( GCG ) ( 7 ) 'expansion ' of pA1 and c.429_452dup 'dup24bp ' of pA2 ) .

Example answer:
{"entities": [{"text": "ID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "c.304ins ( GCG ) ( 7 )", "type": "SequenceVariant"}, {"text": "c.429_452dup", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The second objective was to employ RB1 molecular deletion and microsatellite-based linkage analysis as laboratory tools , while counseling families with a history of retinoblastoma ( RB ) .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "retinoblastoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: We next sequenced PTPN11 in DNA samples from 54 patients with the multiple enchondromatosis disorders Ollier disease or Maffucci syndrome , but found no coding sequence PTPN11 mutations .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "enchondromatosis disorders Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: METHODS : A dataset comprising 13 Norrie-FEVR , one Coat 's disease , 31 ROP patients and 90 ex-premature babies of < 32 weeks ' gestation underwent an ophthalmologic examination and were screened for mutations within the NDP gene by direct DNA sequencing , denaturing high-performance liquid chromatography or gel electrophoresis .

## Item biored:test:362
Example input:
Sentence: CONCLUSIONS : In contrast to a single GCG expansion in most of OPMD patients in the literature , an insertion of ( GCG ) 4GCA in the PABPN1 gene was found in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: the skipping of exon 9 ( p.G204_K247del ) or the retention of introns 8 and 9 ( p.G204VfsX28 ) .

Example answer:
{"entities": [{"text": "p.G204_K247del", "type": "SequenceVariant"}, {"text": "p.G204VfsX28", "type": "SequenceVariant"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three microdeletions were also identified , two of which ( c.611delG and c.640_667del28 ) were located within the coding region whereas one ( c.609+28_610-16del ) was located entirely within intron 8 .

Example answer:
{"entities": [{"text": "c.611delG", "type": "SequenceVariant"}, {"text": "c.640_667del28", "type": "SequenceVariant"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}]}

Example input:
Sentence: Interestingly , a nucleotide insertion of c.1146+25insA in exon 6 was detected in five VSD patients , but not in 486 normal healthy controls .

Example answer:
{"entities": [{"text": "c.1146+25insA", "type": "SequenceVariant"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Input:
Sentence: A 6-base insertion in intron 7 ( 6bINS ) of ENG has been reported to be associated with microvascular disturbance .

## Item biored:test:382
Example input:
Sentence: Eighty-one percent of patients with dyskinesia had clinical fluctuations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , patient relapse often occurs due to development of resistance .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: A 74-year-old man with depressive symptoms was admitted to a psychiatric hospital due to insomnia , loss of appetite , exhaustion , and agitation .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "depressive symptoms", "type": "DiseaseOrPhenotypicFeature"}, {"text": "psychiatric", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insomnia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "loss of appetite", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agitation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Two hundred twenty-eight patients ( 42 % men ) with a mean age of 81.1 ( range 76-94 ) were included in the analysis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: These 24 patients were mostly adults ( 96 % ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Careful therapeutic intervention is necessary in cases involving elderly patients who suffer from depression .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Across all groups , no more than 5 % of patients had clinically significant weight change .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We have investigated this gene in a large UK case-control sample ( bipolar I disorder N = 687 , unipolar recurrent major depression N = 1,036 , controls N = 1,204 ) .

Example answer:
{"entities": [{"text": "bipolar I disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "unipolar recurrent major depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient had depressed of mental status lasting at least 24 h prior to admission .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On an intention-to-treat basis , 55 % of the patients achieved at least partial response , including 19 % CR and 35 % achieved at least very good partial response .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Twenty-three percent to 44 % of patients develop depression .

## Item biored:test:394
Example input:
Sentence: The mean reduction in MSSBP/MSDBP with VAL/HCTZ 320/25 mg was 24.7/16.6 mm Hg , compared with 5.9/7.0 mm Hg with placebo .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "tempol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "LNNA", "type": "ChemicalEntity"}]}

Example input:
Sentence: This retrospective study investigated the combination of bort ( 1.3 mg/m ( 2 ) on days 1 , 4 , 8 , and 11 every 3 weeks ) and dex ( 20 mg on the day of and the day after bort ) as salvage treatment in 85 patients with R/R MM after prior autologous stem cell transplantation or conventional chemotherapy .

Example answer:
{"entities": [{"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The extent of memory improvement evoked by DCE was 23 % at the dose of 200 mg/kg and 35 % at the dose of 400 mg/kg in young mice using elevated plus maze .

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , DCE reversed the amnesia induced by scopolamine ( 0.4 mg/kg , i.p . )

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "scopolamine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Increased CCR2 was observed in the hippocampus after SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Input:
Sentence: The primary outcome was a postdose SCr increase > or = 0.5 mg/dL ( 44.2 micromol/L ) over baseline .

## Item biored:test:395
Example input:
Sentence: RESULTS : Increased CCR2 was observed in the hippocampus after SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The hazard decreased 0.3-fold ( 0.7-1.7 , P=0.385 ) with glimepiride , 0.4-fold ( 0.7-1.3 , P=0.192 ) with gliclazide , and 0.4-fold ( 0.7-1.1 , P=0.09 ) with either .

Example answer:
{"entities": [{"text": "glimepiride", "type": "ChemicalEntity"}, {"text": "gliclazide", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Short-term losartan treatment , besides antihypertensive effect , improved glomerular filtration rate and ameliorated glomerulosclerosis resulting in decreased proteinuria .

Example answer:
{"entities": [{"text": "losartan", "type": "ChemicalEntity"}, {"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , an increase of serum creatinine at various times postoperatively is more predictive of the development of CRF or ESRD .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients developing ESRD had a 6-year survival after onset of ESRD of 27 % for the patients receiving hemodialysis versus 71.4 % for the patients developing ESRD who subsequently received kidney transplants .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The second episode was more severe than the first ; and although both were treated with intensive corticosteroid therapy , renal function remained impaired .

Example answer:
{"entities": [{"text": "corticosteroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Losartan reduces the rate of progression of ADR-induced focal segmental glomerulosclerosis to end-stage renal disease in SHR .

Example answer:
{"entities": [{"text": "Losartan", "type": "ChemicalEntity"}, {"text": "ADR-induced", "type": "ChemicalEntity"}, {"text": "focal segmental glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "end-stage renal disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Secondary outcomes were a postdose SCr increase > or = 25 % , a postdose estimated glomerular filtration rate decrease of > or = 25 % , and the mean peak change in SCr .

## Item biored:test:383
Example input:
Sentence: We report the mutational spectrum in 68 Italian patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The identification of around 7 % of homozygotes for the frameshift mutation in our Caucasian population suggests the existence of an interindividual variation of the CYP2F1 activity and , consequently , the possibility of interindividual differences in the toxic response to some pneumotoxicants and in the susceptibility to certain chemically induced diseases .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Several studies have suggested that the regulator of G-protein signaling 4 ( RGS4 ) may be a positional and functional candidate gene for schizophrenia .

Example answer:
{"entities": [{"text": "regulator of G-protein signaling 4", "type": "GeneOrGeneProduct"}, {"text": "RGS4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The polymorphism distribution was also analyzed in AD patients stratified according to differential progressive rate of cognitive decline during a 2-year follow-up .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thirty-six nonobese subjects with schizophrenia or schizoaffective disorder , matched by body mass index and treated with either clozapine , olanzapine , or risperidone , were included in the analysis .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "schizoaffective disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Results of this analysis indicated that there is a strong finding of -120 bp duplication allele frequencies with schizophrenia ( p=0.008 ) and weak finding with -1240 L/S and for paranoid schizophrenia ( p=0.022 ) .

Example answer:
{"entities": [{"text": "-120 bp duplication", "type": "SequenceVariant"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-1240 L/S", "type": "SequenceVariant"}, {"text": "paranoid schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Eighty-one percent of patients with dyskinesia had clinical fluctuations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , patient relapse often occurs due to development of resistance .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Input:
Sentence: A minority of patients evolve to psychosis .
