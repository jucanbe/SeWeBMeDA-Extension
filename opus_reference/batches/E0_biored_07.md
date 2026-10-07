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

## Item biored:test:691
Input:
Sentence: Hepatomegaly was noticed , and histological examination of a liver biopsy specimen suggested severe hepatic steatosis and periportal necrosis .

## Item biored:test:613
Input:
Sentence: A link between VDR and the RAS-mitogen-activated protein kinase ( MAPK ) or phosphatidylinositol 3-kinase ( PI3K ) -AKT pathway has been suggested .

## Item biored:test:751
Input:
Sentence: All of the 65 coding exons and their flanking intronic boundaries of FBN1 were amplified in the proband by polymerase chain reaction and followed by direct sequencing .

## Item biored:test:752
Input:
Sentence: The mutation identified in the proband was screened in the other family members and the 170 healthy Chinese individuals by direct sequencing .

## Item biored:test:706
Input:
Sentence: The use of hrMCA in combination with SAG from genomic DNA enables rapid detection of COL3A1 mutations with high efficiency and specificity .

## Item biored:test:753
Input:
Sentence: Protein conservation analysis was performed in six species using an online ClustalW tool .

## Item biored:test:711
Input:
Sentence: We therefore performed a mutation analysis of the GUCA1B gene in a clinically well characterized group of patients of European and North-American geographical origin with autosomal dominantly inherited cone dystrophy and cone rod dystrophy .

## Item biored:test:727
Input:
Sentence: Geneticists should consider the possibility of compound heterozygosity for large deletions in patients with SLS and other inborn errors of metabolism , which has implications for carrier testing and prenatal diagnosis .

## Item biored:test:728
Input:
Sentence: Homozygously deleted gene DACH1 regulates tumor-initiating activity of glioma cells .

## Item biored:test:721
Input:
Sentence: We now describe 2 SLS patients whose disease is caused by large contiguous gene deletions of the ALDH3A2 locus on 17p11.2 .

## Item biored:test:665
Input:
Sentence: In addition , the disrupted prepulse inhibition induced by d-amphetamine or phencyclidine was restored by 5-HT6 receptor antagonist in an animal study using rats .

## Item biored:test:685
Input:
Sentence: We conclude that the thrombophilic FGG 10034 T gene variant does not contribute to the genetic susceptibility to PAD .

## Item biored:test:715
Input:
Sentence: The sequence variant c.465G > T encodes a conservative amino acid substitution , p.Glu155Asp , located in EF-hand 4 , the calcium binding site of GCAP2 protein .

## Item biored:test:756
Input:
Sentence: This mutation was also present in two family members but absent in the other , unaffected family members and the 170 healthy Chinese individuals .

## Item biored:test:731
Input:
Sentence: We found decreased cell proliferation of a series of glioma cell lines by forced expression of DACH1 .

## Item biored:test:704
Input:
Sentence: In addition , we identified five novel COL3A1 mutations , including one deletion ( c.2187delA ) and one nonsense mutation ( c.2992C > T ) that could not be determined by the conventional total RNA method .

## Item biored:test:709
Input:
Sentence: Background : Heterozygous mutations in GUCA1A ( MIM # 600364 ) have been identified to cause autosomal dominantly inherited cone dystrophy , cone rod dystrophy and macular dystrophy .

## Item biored:test:673
Input:
Sentence: In the haplotype-wise analysis , we detected an association between two markers ( rs6693503 and rs1805054 ) and three markers ( rs6693503 , rs1805054 and rs4912138 ) in HTR6 and METH-induced psychosis patients , respectively .

## Item biored:test:730
Input:
Sentence: Here , by allelic DNA copy number analysis using single-nucleotide polymorphism genotyping array and mass spectrometry , we report homozygous deletion in glioblastoma multiformes at chromosome 13q21 , where DACH1 gene is located .

## Item biored:test:657
Input:
Sentence: Three patients with the triple polymerase substitution pattern ( rtV173L + rtL180M + rtM204V ) had associated changes in the envelope gene ( sE164D + sI195M ) .

## Item biored:test:714
Input:
Sentence: Results : Three different sequence variants , c.-17T > C , c.171T > C , c.465G > T were identified .

## Item biored:test:631
Input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

## Item biored:test:723
Input:
Sentence: A 24-year-old SLS female was homozygous for a 352-kb deletion involving ALDH3A2 and 4 contiguous genes including ALDH3A1 , which codes for the major soluble protein in cornea .

## Item biored:test:737
Input:
Sentence: Exogenous bFGF rescues spheroid-forming activity and tumorigenicity of the U87-DACH1-high cells , suggesting that loss of DACH1 increases the number of tumor-initiating cells through transcriptional activation of bFGF .

## Item biored:test:757
Input:
Sentence: The mutant residue located in the calcium binding epidermal growth factor-like # 15 domain is highly conserved among mammalian species and could probably induce conformation change of the domain .

## Item biored:test:724
Input:
Sentence: Although lacking corneal disease , she showed severe symptoms of SLS with uncommon deterioration in oral motor function and loss of ambulation .

## Item biored:test:705
Input:
Sentence: Furthermore , we established a small amplicon genotyping ( SAG ) method for detecting three high frequency coding-region SNPs ( rs1800255 : G > A , rs1801184 : T > C , and rs2271683 : A > G ) in COL3A1 to differentiate mutations before sequencing .

## Item biored:test:780
Input:
Sentence: Here , we investigated how this specific signal is propagated to cause the HI neuronal death .

## Item biored:test:759
Input:
Sentence: Our result expands the mutation spectrum of FBN1 and contributes to the study of the molecular pathogenesis of Marfan syndrome .

## Item biored:test:750
Input:
Sentence: Genomic DNA was extracted from leukocytes of venous blood of six individuals in the family and 170 healthy Chinese individuals .

## Item biored:test:717
Input:
Sentence: Conclusion : The absence of clearly pathogenic mutations in the selected patient group suggests that the GUCA1B gene is a minor cause for retinal degenerations in Europeans or North-Americans .

## Item biored:test:688
Input:
Sentence: Mutations in the BSCL2 gene are known to result in CGL2 , a more severe phenotype than CGL1 , with earlier onset , more extensive fat loss and biochemical changes , more severe intellectual impairment , and more severe cardiomyopathy .

## Item biored:test:793
Input:
Sentence: Unfortunately , the results from human research investigating its psychological effects have been inconsistent .

## Item biored:test:664
Input:
Sentence: The serotonin 6 ( 5-HT6 ) receptor is therapeutically targeted by several second generation antipsychotics , such as clozapine and olanzapine , and d-amphetamine-induced hyperactivity in rats is corrected with the use of a selective 5-HT6 receptor antagonist .

## Item biored:test:743
Input:
Sentence: A significant association was noted between higher levels of apoB-100 ( P = 1.1 10 ( -3 ) ) and LDL cholesterol ( P = 0.02 ) and the subjects having Arg70 .

## Item biored:test:796
Input:
Sentence: Participants completed a drug history questionnaire , Beck Depression Inventory , Barratt Impulsiveness Scale , Pittsburgh Sleep Quality Index , and Wechsler Memory Scale-Revised which , in total , provided 13 psychometric measures .

## Item biored:test:683
Input:
Sentence: In a multivariate logistic regression analysis including age , sex , smoking , diabetes , arterial hypertension and hypercholesterolemia , the FGG 10034 T variant was not significantly associated with the presence of PAD ( Odds ratio 1.07 , 95 % confidence interval 0.84 - 1.37 ; p = 0.60 ) .

## Item biored:test:747
Input:
Sentence: Identification of a novel FBN1 gene mutation in a Chinese family with Marfan syndrome .

## Item biored:test:746
Input:
Sentence: In particular , serum apoB-100 concentration might be an informative marker for judging changes in HCV-associated intracellular lipoprotein metabolism in patients carrying the rs8099917 responder genotype .

## Item biored:test:738
Input:
Sentence: These results illustrate that DACH1 is a distinctive tumor suppressor , which does not only suppress growth of tumor cells but also regulates bFGF-mediated tumor-initiating activity of glioma cells .

## Item biored:test:732
Input:
Sentence: We then generated U87TR-Da glioma cells , where DACH1 expression could be activated by exposure of the cells to doxycycline .

## Item biored:test:772
Input:
Sentence: We found that patients with the STAT4 C/G and CC genotypes exhibited a 1.583-fold increased risk of SLE incidence ( 95 % CI = 1.168-2.145 , p = 0.003 ) , with OR for the C/C versus C/G and G/G genotypes was 1.967 ( 95 % CI = 1.152-3.358 , p = 0.0119 ) .

## Item biored:test:734
Input:
Sentence: U87-DACH1-low cells form spheroids with CD133 and Nestin expression in serum-free medium but U87-DACH1-high cells do not .

## Item biored:test:773
Input:
Sentence: The OR for the STAT4 C allele frequency showed a 1.539-fold increased risk of SLE ( 95 % CI = 1.209-1.959 , p = 0.0004 ) .

## Item biored:test:777
Input:
Sentence: Critical role of neuronal pentraxin 1 in mitochondria-mediated hypoxic-ischemic neuronal injury .

## Item biored:test:736
Input:
Sentence: Gene expression analysis and chromatin immunoprecipitation assay reveal that fibroblast growth factor 2 ( FGF2/bFGF ) is transcriptionally repressed by DACH1 , especially in cells cultured in serum-free medium .

## Item biored:test:807
Input:
Sentence: The LSECs and sub-endothelial basement membrane were observed with the scanning and transmission electronic microscope .

## Item biored:test:778
Input:
Sentence: Developing brain is highly susceptible to hypoxic-ischemic ( HI ) injury leading to severe neurological disabilities in surviving infants and children .

## Item biored:test:755
Input:
Sentence: RESULTS : A novel heterozygous c.3703T > C change in exon 29 of FBN1 was detected in the proband , which resulted in the substitution of serine by proline at codon 1235 ( p.S1235P ) .

## Item biored:test:760
Input:
Sentence: Reciprocal effects of NNK and SLURP-1 on oncogene expression in target epithelial cells .

## Item biored:test:758
Input:
Sentence: CONCLUSIONS : We indentified a novel p.S1235P mutation in FBN1 , which is the causative mutation for MFS in this family .

## Item biored:test:669
Input:
Sentence: METHOD : Using five tagging SNPs ( rs6693503 , rs1805054 , rs4912138 , rs3790757 and rs9659997 ) , we conducted a genetic association analysis of case-control samples ( 197 METH-induced psychosis patients and 337 controls ) in the Japanese population .

## Item biored:test:725
Input:
Sentence: The other 19-month-old female patient was a compound heterozygote for a 1.44-Mb contiguous gene deletion and a missense mutation ( c.407C > T , P136L ) in ALDH3A2 .

## Item biored:test:798
Input:
Sentence: Strikingly , despite prolonged abstinence ( mean , 4.98 ; range , 4-9 years ) , past ecstasy users showed few signs of recovery .

## Item biored:test:799
Input:
Sentence: Compared with present ecstasy users , the past users showed no change for ten measures , increased impairment for two measures , and improvement on just one measure .

## Item biored:test:678
Input:
Sentence: A functional single nucleotide polymorphism ( SNP ) in the 3 ' untranslated region of the FGG gene ( FGG 10034C > T , rs2066865 ) has been associated with deep venous thrombosis and myocardial infarction .

## Item biored:test:744
Input:
Sentence: A significant association was also observed between subjects carrying the rs8099917 TT responder genotype and higher levels of apoB-100 ( P = 6.4 10 ( -3 ) ) and LDL cholesterol ( P = 4.2 10 ( -3 ) ) .

## Item biored:test:794
Input:
Sentence: OBJECTIVES : The present study aimed to be the largest to date in sample size and 5HT-related behaviors ; the first to compare present ecstasy users with past users after an abstinence of 4 or more years , and the first to include robust controls for other recreational substances .

## Item biored:test:695
Input:
Sentence: We reviewed the genotype of CGL cases from Japan , India , China and Taiwan , and found that BSCL2 is a major causative gene for CGL in Asian .

## Item biored:test:733
Input:
Sentence: Both ex vivo cellular proliferation and in vivo growth of s.c. transplanted tumors in mice are reduced in U87TR-Da cells with DACH1 expression ( U87-DACH1-high ) , compared with DACH1-nonexpressing U87TR-Da cells ( U87-DACH1-low ) .

## Item biored:test:767
Input:
Sentence: These pro-oncogenic effects of NNK were abolished by rSLURP-1 that also upregulated RUNX3 .

## Item biored:test:770
Input:
Sentence: The STAT4 has been found to be a susceptible gene in the development of systemic lupus erythematosus ( SLE ) in various populations .

## Item biored:test:776
Input:
Sentence: Our studies confirmed an association of the STAT4 C ( rs7582694 ) variant with the development of SLE and occurrence of some clinical manifestations of the disease .

## Item biored:test:818
Input:
Sentence: However , information is limited concerning the safety of the regimen in elderly patients .

## Item biored:test:809
Input:
Sentence: Expression of von Willebrand factor ( vWF ) was investigated with immunofluorescence staining .

## Item biored:test:735
Input:
Sentence: Compared with spheroid-forming U87-DACH1-low cells , adherent U87-DACH1-high cells display lower tumorigenicity , indicating DACH1 decreases the number of tumor-initiating cells .

## Item biored:test:820
Input:
Sentence: Despite immediate intravenous antimicrobial therapy , he succumbed 23 h after the onset .

## Item biored:test:779
Input:
Sentence: Previously , we have reported induction of neuronal pentraxin 1 ( NP1 ) , a novel neuronal protein of long-pentraxin family , following HI neuronal injury .

## Item biored:test:826
Input:
Sentence: DESIGN : Multicenter , retrospective , propensity-matched cohort study .

## Item biored:test:827
Input:
Sentence: SETTING : Neurocritical care units at two academic medical centers with dedicated neurocritical care teams and board-certified neurointensivists .

## Item biored:test:828
Input:
Sentence: PATIENTS : Neurocritical care patients admitted between July 2009 and September 2012 were evaluated and then matched 1:1 based on propensity scoring of baseline characteristics .

## Item biored:test:745
Input:
Sentence: Our results suggest that apoB-100 and LDL cholesterol are markers of impaired cellular lipoprotein pathways and/or host endogenous interferon response to HCV in chronic HCV infection .

## Item biored:test:790
Input:
Sentence: Together our findings demonstrate a novel mechanism by which NP1 regulates mitochondria-driven hippocampal cell death ; suggesting NP1 as a potential therapeutic target against HI brain injury in neonates .

## Item biored:test:832
Input:
Sentence: No difference in the primary composite outcome in both the unmatched ( 30 % vs 30 % , p = 0.94 ) or matched cohorts ( 28 % vs 34 % , p = 0.35 ) could be found .

## Item biored:test:784
Input:
Sentence: OGD also caused a time-dependent decrease in the phosphorylation of Bad ( Ser136 ) , and Bax protein levels .

## Item biored:test:769
Input:
Sentence: Contribution of STAT4 gene single-nucleotide polymorphism to systemic lupus erythematosus in the Polish population .

## Item biored:test:742
Input:
Sentence: Our results demonstrated that both the aa 70 substitution in the core region of the HCV and the rs8099917 SNP located proximal to the IL28B were independent factors in determining serum apoB-100 and low-density lipoprotein ( LDL ) cholesterol levels .

## Item biored:test:768
Input:
Sentence: SIGNIFICANCE : The obtained results identified target genes for both NNK and SLURP-1 and shed light on the molecular mechanism of their reciprocal effects on tumorigenic transformation of bronchial and oral epithelial cells .

## Item biored:test:748
Input:
Sentence: PURPOSE : To identify the mutation in the fibrillin-1 gene ( FBN1 ) in a Chinese family with Marfan syndrome ( MFS ) .

## Item biored:test:824
Input:
Sentence: However , both agents are associated with significant hemodynamic side effects .

## Item biored:test:841
Input:
Sentence: The study was conducted at the Animal Experiment Laboratories , Department of Pharmacology , Medical School , Eskisehir Osmangazi University , Eskisehir , Turkey between March and May 2012 .

## Item biored:test:792
Input:
Sentence: RATIONALE : Ecstasy ( 3,4-methylenedioxymethamphetamine , MDMA ) is a worldwide recreational drug of abuse .

## Item biored:test:771
Input:
Sentence: There are evident population differences in the context of clinical manifestations of SLE , therefore we investigated the prevalence of the STAT4 G > C ( rs7582694 ) polymorphism in patients with SLE ( n = 253 ) and controls ( n = 521 ) in a sample of the Polish population .

## Item biored:test:741
Input:
Sentence: The aim of this study was to elucidate the relationship between serum lipid and factors that are able to predict the efficacy of PEG-IFN/RB therapy , with specific focus on apolipoprotein B-100 ( apoB-100 ) in 148 subjects with chronic HCV G1b infection .

## Item biored:test:346
Input:
Sentence: Variants of coagulation factors [ factor V 1691G > A ( factor V Leiden ) , factor V 4070A > G ( factor V HR2 haplotype ) , factor VII Arg353Gln , factor XIII Val34Leu , beta-fibrinogen -455G > A , prothrombin 20210G > A ] , coagulation inhibitors [ tissue factor pathway inhibitor 536C > T , thrombomodulin 127G > A ] , fibrinolytic factors [ angiotensin converting enzyme intron 16 insertion/deletion , factor VII-activating protease 1601G > A ( FSAP Marburg I ) , plasminogen activator inhibitor 1-675 insertion/deletion ( 5G/4G ) , tissue plasminogen activator intron h deletion/insertion ] , and other factors implicated in influencing susceptibility to thromboembolic diseases [ apolipoprotein E2/E3/E4 , glycoprotein Ia 807C > T , methylenetetrahydrofolate reductase 677C > T ] were included .

## Item biored:test:775
Input:
Sentence: Moreover , we found a contribution of STAT4 C/C and C/G genotypes to the presence of the anti-snRNP Ab OR = 3.237 ( 1.667-6.288 , p = 0.0003 ) , ( p ( corr ) = 0.0051 ) and the presence of the anti-Scl-70 Ab OR = 2.665 ( 1.380-5.147 , p = 0.0028 ) , ( p ( corr ) = 0.0476 ) .

## Item biored:test:843
Input:
Sentence: RESULTS : In the amphetamine-induced locomotion test , there were significant increases in all movements compared with the amphetamine-free group .

## Item biored:test:839
Input:
Sentence: The DHEA was administered intraperitoneally ( ip ) for 5 days .

## Item biored:test:785
Input:
Sentence: Immunofluorescence staining and subcellular fractionation analyses revealed increased mitochondrial translocation of Bad and Bax proteins from cytoplasm following OGD ( 4 h ) and simultaneously increased release of Cyt C from mitochondria followed by activation of caspase-3 .

## Item biored:test:815
Input:
Sentence: Its action mechanism was associated with the down-regulation of MMP-2/9 activities and inhibition of peroxidation in injured liver .

## Item biored:test:781
Input:
Sentence: We used wild-type ( WT ) and NP1 knockout ( NP1-KO ) mouse hippocampal cultures , modeled in vitro following exposure to oxygen glucose deprivation ( OGD ) , and in vivo neonatal ( P9-10 ) mouse model of HI brain injury .

## Item biored:test:833
Input:
Sentence: When analyzed separately , no differences could be found in the prevalence of severe hypotension or bradycardia in either the unmatched or matched cohorts .

## Item biored:test:786
Input:
Sentence: NP1 protein was immunoprecipitated with Bad and Bax proteins ; OGD caused increased interactions of NP1 with Bad and Bax , thereby , facilitating their mitochondrial translocation and dissipation of mitochondrial membrane potential ( D ( m ) ) .

## Item biored:test:830
Input:
Sentence: MEASUREMENTS AND MAIN RESULTS : A total of 342 patients ( 105 dexmedetomidine and 237 propofol ) were included in the analysis , with 190 matched ( 95 in each group ) by propensity score .

## Item biored:test:846
Input:
Sentence: There was no significant difference between groups in terms of total climbing time in the apomorphine-induced climbing test ( p > 0.05 ) .

## Item biored:test:618
Input:
Sentence: VDR was not independently associated with body mass index , family history of colorectal cancer , tumor location ( colon versus rectum ) , stage , tumor grade , signet ring cells , CIMP , MSI , LINE-1 hypomethylation , BRAF , p53 , p21 , beta-catenin , or cyclooxygenase-2 .

## Item biored:test:805
Input:
Sentence: The Serum liver function parameters including alanine aminotransferase ( ALT ) and aspartate aminotransferase ( AST ) levels were assayed with the commercial kit .

## Item biored:test:774
Input:
Sentence: We also observed an increased frequency of STAT4 C/C and C/G genotypes in SLE patients with renal symptoms OR = 2.259 ( 1.365-3.738 , p = 0.0014 ) , ( p ( corr ) = 0.0238 ) and in SLE patients with neurologic manifestations OR = 2.867 ( 1.467-5.604 , p = 0.0016 ) , ( p ( corr ) = 0.0272 ) .

## Item biored:test:823
Input:
Sentence: OBJECTIVE : Dexmedetomidine and propofol are commonly used sedatives in neurocritical care as they allow for frequent neurologic examinations .

## Item biored:test:831
Input:
Sentence: The primary outcome of this study was a composite of severe hypotension ( mean arterial pressure < 60 mm Hg ) and bradycardia ( heart rate < 50 beats/min ) during sedative infusion .
