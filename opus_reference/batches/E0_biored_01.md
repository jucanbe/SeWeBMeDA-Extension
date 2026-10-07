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

## Item biored:test:112
Input:
Sentence: OBJECTIVE : Congenital long QT syndrome ( LQTS ) with in utero onset of the rhythm disturbances is associated with a poor prognosis .

## Item biored:test:113
Input:
Sentence: In this study we investigated a newborn patient with fetal bradycardia , 2:1 atrioventricular block and ventricular tachycardia soon after birth .

## Item biored:test:56
Input:
Sentence: The control rats received atropine sulfate , but also saline and olive oil instead of other antidotes and DFP , respectively .

## Item biored:test:110
Input:
Sentence: No association of IL12B polymorphisms and self-limited HCV infection could be demonstrated .

## Item biored:test:91
Input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

## Item biored:test:53
Input:
Sentence: The acute toxicity of OPs is the result of their irreversible binding with AChEs in the central nervous system ( CNS ) , which elevates acetylcholine ( ACh ) levels .

## Item biored:test:109
Input:
Sentence: CONCLUSIONS : IL12B 3'-UTR 1188-C-allele carriers appear to be capable of responding more efficiently to antiviral combination therapy as a consequence of a reduced relapse rate .

## Item biored:test:33
Input:
Sentence: These effects were not mediated by a dopaminergic mechanism as nefiracetam , at millimolar concentrations , failed to displace either [ 3H ] SCH 23390 or [ 3H ] spiperone binding from D1 or D2 dopamine receptor subtypes , respectively .

## Item biored:test:170
Input:
Sentence: DESIGN AND METHODS : The present analysis was a case control study .

## Item biored:test:2
Input:
Sentence: The two metabolic phenotypes , extensive ( EM ) and poor metabolizers ( PM ) , show different stereoselective metabolism , resulting in apparently higher beta-1 adrenoceptor antagonistic potency of racemic metoprolol in EMs .

## Item biored:test:126
Input:
Sentence: The two BRCA2 variants were analyzed by the TaqMan allelic discrimination technique .

## Item biored:test:128
Input:
Sentence: We found no evidence of a significant modification of breast cancer penetrance in BRCA1 mutation carriers by either polymorphism .

## Item biored:test:136
Input:
Sentence: In a microdialysis study , 10 muL of saline ( group C ; n = 8 ) or 30 mug of morphine ( group M ; n = 8 ) was injected intrathecally ( IT ) 0.5 h after reflow , and 30 mug of morphine ( group SM ; n = 8 ) or 10 muL of saline ( group SC ; n = 8 ) was injected IT 0.5 h after sham operation .

## Item biored:test:14
Input:
Sentence: Eighty unrelated individuals with Duchenne muscular dystrophy ( DMD ) or Becker muscular dystrophy ( BMD ) were found to have deletions in the major deletion-rich region of the DMD locus .

## Item biored:test:131
Input:
Sentence: on newborn females and adult female controls , we found no departure from Hardy-Weinberg equilibrium in the distribution of N372H alleles for our female BRCA1 carriers .

## Item biored:test:103
Input:
Sentence: BACKGROUND/AIMS : Interleukin-12 ( IL-12 ) governs the Th1-type immune response , affecting the spontaneous and treatment-induced recovery from HCV-infection .

## Item biored:test:101
Input:
Sentence: Our data suggested that cytoskeleton disorganization in epidermal cells is likely associated with the pathogenesis of DSAP .

## Item biored:test:88
Input:
Sentence: Cardioprotective effect of tincture of Crataegus on isoproterenol-induced myocardial infarction in rats .

## Item biored:test:89
Input:
Sentence: Tincture of Crataegus ( TCR ) , an alcoholic extract of the berries of hawthorn ( Crataegus oxycantha ) , is used in herbal and homeopathic medicine .

## Item biored:test:108
Input:
Sentence: However , HCV genotype 1-infected patients with high baseline viremia carrying the IL12B 3'-UTR 1188-C-allele showed significantly higher sustained virologic response ( SVR ) rates ( 25.3 % vs. 46 % vs. 54.5 % for A/A , A/C and C/C ) due to reduced relapse rates ( 24.2 % vs. 12 % vs. zero % for A/A , A/C and C/C ) .

## Item biored:test:148
Input:
Sentence: Abdominal ultrasound showed an adrenal mass , and postoperative histologic examination confirmed the diagnosis of pheochromocytoma .

## Item biored:test:59
Input:
Sentence: When CPA , diazepam or 2PAM was given immediately after DFP-atropine , these treatments prevented , delayed or shortened the occurrence of serious signs of poisoning .

## Item biored:test:139
Input:
Sentence: After IT morphine , the cerebrospinal fluid ( CSF ) glutamate concentration was increased in group M relative to both baseline and group C ( P < 0.05 ) .

## Item biored:test:111
Input:
Sentence: A novel SCN5A mutation manifests as a malignant form of long QT syndrome with perinatal onset of tachycardia/bradycardia .

## Item biored:test:52
Input:
Sentence: Such organophosphorus ( OP ) compounds as diisopropylfluorophosphate ( DFP ) , sarin and soman are potent inhibitors of acetylcholinesterases ( AChEs ) and butyrylcholinesterases ( BChEs ) .

## Item biored:test:172
Input:
Sentence: DNA typing of DBP locus was performed by the PCR-restriction fragment length polymorphism method ( RFLP ) .

## Item biored:test:181
Input:
Sentence: We hypothesized that promoter variants would be the most likely candidates for determinants of risk .

## Item biored:test:118
Input:
Sentence: Expression of this mutant channel in tsA201 mammalian cells by site-directed mutagenesis revealed a persistent tetrodotoxin-sensitive but lidocaine-resistant current that was associated with a positive shift of the steady-state inactivation curve , steeper activation curve and faster recovery from inactivation .

## Item biored:test:92
Input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

## Item biored:test:147
Input:
Sentence: Both drugs were immediately discontinued , and the patient recovered after subsequent nicardipine and verapamil treatment .

## Item biored:test:152
Input:
Sentence: Physicians and other healthcare professionals should be aware of this potential adverse effect of tiapride and amisulpride .

## Item biored:test:122
Input:
Sentence: Common BRCA2 variants and modification of breast and ovarian cancer risk in BRCA1 mutation carriers .

## Item biored:test:171
Input:
Sentence: 110 patients , 68 controls , and 115 first-degree relatives were genotyped for the DBP polymorphism in codon 416 .

## Item biored:test:133
Input:
Sentence: The activation of spinal N-methyl-D-aspartate receptors may contribute to degeneration of spinal motor neurons induced by neuraxial morphine after a noninjurious interval of spinal cord ischemia .

## Item biored:test:132
Input:
Sentence: We conclude that if these single-nucleotide polymorphisms do modify the risk of cancer in BRCA1 mutation carriers , their effects are not significantly larger than that of N372H previously observed in the general population .

## Item biored:test:149
Input:
Sentence: DISCUSSION : Drug-induced symptoms of pheochromocytoma are often associated with the use of substituted benzamide drugs , but the underlying mechanism is unknown .

## Item biored:test:129
Input:
Sentence: In respect of ovarian cancer risk , we also saw no effect with the N372H variant but we did observe a borderline association with the 5'-untranslated region 203A allele ( hazard ratio , 1.43 ; CI , 1.01-2.00 ) .

## Item biored:test:61
Input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

## Item biored:test:96
Input:
Sentence: Disseminated superficial actinic porokeratosis ( DSAP ) is an uncommon autosomal dominant chronic keratinization disorder , characterized by multiple superficial keratotic lesions surrounded by a slightly raised keratotic border .

## Item biored:test:104
Input:
Sentence: We investigated whether the IL12B polymorphisms within the promoter region ( 4 bp insertion/deletion ) and the 3'-UTR ( 1188-A/C ) , which have been reported to influence IL-12 synthesis , are associated with the outcome of HCV infection .

## Item biored:test:159
Input:
Sentence: RESULTS : Sporadic chondrocalcinosis was associated with a G-to-A transition in the ANKH 5'-untranslated region ( 5'-UTR ) at 4 bp upstream of the start codon ( in homozygotes of the minor allele , genotype relative risk 6.0 , P = 0.0006 ; overall genotype association P = 0.02 ) .

## Item biored:test:158
Input:
Sentence: The function of these variants was studied in transfected human immortalized CH-8 articular chondrocytes .

## Item biored:test:175
Input:
Sentence: These finding supports a role of the vitamin D endocrine system in the autoimmune process of type 1 diabetes .

## Item biored:test:192
Input:
Sentence: The Pilo group was injected with the same drugs , except for CHX .

## Item biored:test:193
Input:
Sentence: Animals were killed between 30 and 60 days later , and brain sections were processed for GAP43 immunohistochemistry .

## Item biored:test:185
Input:
Sentence: We found no statistically significant difference in either genotype or allele frequencies between cases and controls overall or between male and female cases for the BRAF polymorphism in the two incident case series .

## Item biored:test:143
Input:
Sentence: We suggest that opioids may be neurotoxic in the setting of spinal cord ischemia via NMDA receptor activation .

## Item biored:test:145
Input:
Sentence: OBJECTIVE : To describe the unmasking of pheochromocytoma in a patient treated with amisulpride and tiapride .

## Item biored:test:155
Input:
Sentence: This study investigated the potential for ANKH sequence variants to promote sporadic chondrocalcinosis .

## Item biored:test:138
Input:
Sentence: Second , we investigated the effect of IT MK-801 ( 30 mug ) on the histopathologic changes in the spinal cord after morphine-induced spastic paraparesis .

## Item biored:test:144
Input:
Sentence: Pheochromocytoma unmasked by amisulpride and tiapride .

## Item biored:test:168
Input:
Sentence: Correlations between DBP alleles and type 1 diabetes have been described in different populations .

## Item biored:test:123
Input:
Sentence: The HH genotype of the nonconservative amino acid substitution polymorphism N372H in the BRCA2 gene was reported to be associated with a 1.3- to 1.5-fold increase in risk of both breast and ovarian cancer .

## Item biored:test:150
Input:
Sentence: In our case , use of the Naranjo probability scale indicated a possible relationship between the hypertensive crisis and amisulpride and tiapride therapy .

## Item biored:test:115
Input:
Sentence: The 2:1 atrioventricular block improved to 1:1 conduction only after intravenous lidocaine infusion or a high dose of mexiletine , which also controlled the ventricular tachycardia .

## Item biored:test:102
Input:
Sentence: Influence of interleukin 12B ( IL12B ) polymorphisms on spontaneous and treatment-induced recovery from hepatitis C virus infection .

## Item biored:test:211
Input:
Sentence: with 200mgkg ( -1 ) twice daily for 7 days .

## Item biored:test:167
Input:
Sentence: These DBP variants lead to differences in the affinity for 1.25 ( OH ) 2D3 .

## Item biored:test:166
Input:
Sentence: There are two known polymorphisms in exon 11 of the DBP gene resulting in amino acid variants : GAT -- > GAG substitution replaces aspartic acid by glutamic acid in codon 416 ; and ACG -- > AAG substitution in codon 420 leads to an exchange of threonine for lysine .

## Item biored:test:178
Input:
Sentence: Germ line mutations in BRAF have not been identified as causal in families predisposed to melanoma .

## Item biored:test:99
Input:
Sentence: Upon screening 30 candidate genes , we identified a missense mutation , p.Ser63Asn in SSH1 in one family , a frameshift mutation , p.Ser19CysfsX24 in an alternative variant ( isoform f ) of SSH1 in another family , and a frameshift mutation , p.Pro27ProfsX54 in the same alternative variant in one non-familial case with DSAP .

## Item biored:test:176
Input:
Sentence: No Evidence for BRAF as a melanoma/nevus susceptibility gene .

## Item biored:test:179
Input:
Sentence: However , a recent study suggested that a BRAF haplotype was associated with risk of sporadic melanoma in men .

## Item biored:test:182
Input:
Sentence: Using denaturing high-pressure liquid chromatography and sequencing , we screened peripheral blood DNA from 184 familial melanoma cases for BRAF promoter variants .

## Item biored:test:206
Input:
Sentence: Clarifying the functional relevance of polymorphisms associated with susceptibility to a complex disorder such as drug addiction provides a foundation for clinical association studies .

## Item biored:test:210
Input:
Sentence: VCM was administrated intraperitoneally ( i.p . )

## Item biored:test:228
Input:
Sentence: Detailed characterization of the patients ' phenotype was performed with fundal photography , visual field testing , fundal fluorescein angiography , and electroretinography ( ERG ) .

## Item biored:test:187
Input:
Sentence: In addition , we found that there was no association between the BRAF genotype and mean total number of banal or atypical nevi in either the cases or controls .

## Item biored:test:184
Input:
Sentence: We therefore investigated the contribution of this BRAF polymorphism to melanoma susceptibility in 581 consecutively recruited incident cases , 258 incident cases in a study of late relapse , 673 female general practitioner controls , and the 184 familial cases .

## Item biored:test:142
Input:
Sentence: These data indicate that IT morphine induces spastic paraparesis with a concomitant increase in CSF glutamate , which is involved in NMDA receptor activation .

## Item biored:test:186
Input:
Sentence: Our results therefore suggest that the BRAF polymorphism is not significantly associated with melanoma and the promoter insertion/deletion linked with the polymorphism is not a causal variant .

## Item biored:test:212
Input:
Sentence: Erdosteine was administered orally .

## Item biored:test:116
Input:
Sentence: RESULTS : A novel , spontaneous LQTS-3 mutation was identified in the transmembrane segment 6 of domain IV of the Na ( v ) 1.5 cardiac sodium channel , with a G -- > A substitution at codon 1763 , which changed a valine ( GTG ) to a methionine ( ATG ) .

## Item biored:test:174
Input:
Sentence: On the contrary , the DBP Glu-containing genotype was not accompanied by differences in the prevalence of GAD65 antibodies .

## Item biored:test:165
Input:
Sentence: BACKGROUND : Vitamin D-binding protein ( DBP ) is the main systemic transporter of 1.25 ( OH ) 2D3 and is essential for its cellular endocytosis .

## Item biored:test:205
Input:
Sentence: These results indicate that OPRM1-G118 is a functional variant with deleterious effects on both mRNA and protein yield .

## Item biored:test:134
Input:
Sentence: We investigated the relationship between the degeneration of spinal motor neurons and activation of N-methyl-d-aspartate ( NMDA ) receptors after neuraxial morphine following a noninjurious interval of aortic occlusion in rats .

## Item biored:test:169
Input:
Sentence: Therefore , we investigated the polymorphism in codon 416 of the DBP gene for an association with autoimmune markers of type 1 diabetes .

## Item biored:test:121
Input:
Sentence: CONCLUSIONS : These findings suggest that the Na ( v ) 1.5/V1763M channel dysfunction and possible neighboring mutants contribute to a persistent inward current due to altered inactivation kinetics and clinically congenital LQTS with perinatal onset of arrhythmias that responded to lidocaine and mexiletine .

## Item biored:test:222
Input:
Sentence: rTMS at 1 Hz was observed to markedly reduce drug-induced dyskinesias , whereas 5-Hz rTMS induced a slight but not significant increase .

## Item biored:test:151
Input:
Sentence: CONCLUSIONS : As of March 24 , 2005 , this is the first reported case of amisulpride- and tiapride-induced hypertensive crisis in a patient with pheochromocytoma .

## Item biored:test:225
Input:
Sentence: The aim of this study was to investigate the spectrum of mutations in this gene in BCD patients from Singapore , and to characterize their phenotype .

## Item biored:test:227
Input:
Sentence: The 11 exons of the CYP4V2 gene were amplified from genomic DNA of patients by polymerase chain reaction and then sequenced .

## Item biored:test:164
Input:
Sentence: Vitamin D-binding protein gene polymorphism association with IA-2 autoantibodies in type 1 diabetes .

## Item biored:test:180
Input:
Sentence: Polymorphisms or other variants in the BRAF gene may therefore act as candidate low-penetrance genes for nevus/melanoma susceptibility .

## Item biored:test:226
Input:
Sentence: METHODS : Nine patients with BCD from six families were recruited into the study .

## Item biored:test:231
Input:
Sentence: Haplotype analysis in patients and controls indicated a founder effect for this deletion mutation in exon 7 .

## Item biored:test:177
Input:
Sentence: Somatic mutations of BRAF have been identified in both melanoma tumors and benign nevi .

## Item biored:test:154
Input:
Sentence: OBJECTIVE : Certain mutations in ANKH , which encodes a multiple-pass transmembrane protein that regulates inorganic pyrophosphate ( PPi ) transport , are linked to autosomal-dominant familial chondrocalcinosis .

## Item biored:test:232
Input:
Sentence: Clinical heterogeneity was present in the patients .

## Item biored:test:217
Input:
Sentence: Erdosteine caused a marked reduction in the extent of tubular damage .

## Item biored:test:202
Input:
Sentence: In 8 heterozygous samples measured , the A118 mRNA allele was 1.5-2.5-fold more abundant than the G118 allele .

## Item biored:test:141
Input:
Sentence: IT MK-801 significantly reduced the number of dark-stained alpha-motoneurons after morphine-induced spastic paraparesis compared with the saline group .

## Item biored:test:220
Input:
Sentence: The neural mechanisms and circuitry involved in levodopa-induced dyskinesia are unclear .

## Item biored:test:239
Input:
Sentence: The response of the cell to DNA damage and its ability to maintain genomic stability by DNA repair are crucial in preventing cancer initiation and progression .

## Item biored:test:183
Input:
Sentence: We identified a promoter insertion/deletion in linkage disequilibrium with the previously described BRAF polymorphism in intron 11 ( rs1639679 ) reported to be associated with melanoma susceptibility in males .

## Item biored:test:219
Input:
Sentence: rTMS of supplementary motor area modulates therapy-induced dyskinesias in Parkinson disease .

## Item biored:test:160
Input:
Sentence: This -4-bp transition , as well as 2 mutations previously linked with familial and sporadic chondrocalcinosis ( +14 bp C-to-T and C-terminal GAG deletion , respectively ) , but not the French familial chondrocalcinosis kindred 143-bp T-to-C mutation , increased reticulocyte ANKH transcription/ANKH translation in vitro .

## Item biored:test:146
Input:
Sentence: CASE SUMMARY : A 42-year-old white man developed acute hypertension with severe headache and vomiting 2 hours after the first doses of amisulpride 100 mg and tiapride 100 mg .

## Item biored:test:230
Input:
Sentence: The third mutation , a previously identified 15-bp deletion that included the 3 ' splice site for exon 7 , was found in all nine patients , with six patients carrying the deletion in the homozygous state .
