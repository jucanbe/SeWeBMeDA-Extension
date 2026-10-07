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

## Item biored:test:485
Input:
Sentence: Analyses indicated no association between the NQO1 * 2 polymorphism and the risk of anthracycline-related CHF ( odds ratio [ OR ] , 1.04 ; P=.97 ) .

## Item biored:test:540
Input:
Sentence: Eighteen children with DSD and cleft palate were identified in the L beck DSD database ( about 1,500 entries ) .

## Item biored:test:467
Input:
Sentence: Pretreatment with either VPU ( 50 and 100 mg/kg ) or VPA ( 300 and 600 mg/kg ) completely abolished pilocarpine-evoked increases in extracellular glutamate and aspartate .

## Item biored:test:522
Input:
Sentence: The aim of this study was to test if the IGF-1 gene polymorphisms are associated with the GH-dose of GH-deficient adults .

## Item biored:test:478
Input:
Sentence: BACKGROUND : Exposure to anthracyclines as part of cancer therapy has been associated with the development of congestive heart failure ( CHF ) .

## Item biored:test:524
Input:
Sentence: Patients received GH-treatment for 12 months with finished dose-titration of GH and centralized IGF-1 measurements .

## Item biored:test:466
Input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

## Item biored:test:465
Input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

## Item biored:test:508
Input:
Sentence: CONCLUSION : It is possible that CCND3 rs2479717 , or another variant it tags , is associated with prognosis after a diagnosis of breast cancer .

## Item biored:test:531
Input:
Sentence: Intracranial hemorrhage has been reported in a small number of OI patients .

## Item biored:test:519
Input:
Sentence: Growth hormone dose in growth hormone-deficient adults is not associated with IGF-1 gene polymorphisms .

## Item biored:test:549
Input:
Sentence: Offspring of IT balanced carriers are at high risk to have either pure partial trisomy or monosomy for the inserted segment as manifested by `` pure '' phenotypes .

## Item biored:test:574
Input:
Sentence: Blood samples were obtained from all patients and genomic DNA was isolated .

## Item biored:test:435
Input:
Sentence: No CHRNA1 , CHRNB1 , or CHRND mutations were detected , but a homozygous RAPSN frameshift mutation , c.1177-1178delAA , was identified in a family with three children affected with lethal fetal akinesia sequence .

## Item biored:test:562
Input:
Sentence: Brain MRIs are normal in DGUOK patients in the literature .

## Item biored:test:349
Input:
Sentence: We report a case of Gitelman syndrome ( GS ) in a dizygotic twin who presented at 12 years of age with growth delay , metabolic alkalosis , hypomagnesemia and hypokalemia with inappropriate kaliuresis , and idiopathic intracranial hypertension with bilateral papilledema ( pseudotumor cerebri ) .

## Item biored:test:576
Input:
Sentence: In the control subjects , the frequency of DD was 18.8 % ( n = 18 ) , ID was 50 % ( n = 48 ) and II was 31.3 % ( n = 30 ) .

## Item biored:test:525
Input:
Sentence: GH-dose after 1 year of treatment , IGF-1 concentrations , IGF-1-standard deviation score ( SDS ) , the IGF-1 : GH ratio and anthropometric data were analyzed by genotype .

## Item biored:test:569
Input:
Sentence: Asthma is a chronic inflammatory disease of the airways .

## Item biored:test:434
Input:
Sentence: We hypothesized that mutations in acetylcholine receptor-related genes might also result in a MPS/fetal akinesia phenotype and so we analyzed 15 cases of lethal MPS/fetal akinesia without CHRNG mutations for mutations in the CHRNA1 , CHRNB1 , CHRND , and rapsyn ( RAPSN ) genes .

## Item biored:test:527
Input:
Sentence: CONCLUSION : IGF-1 gene polymorphisms were not associated with the responsiveness to exogenous GH in GHD .

## Item biored:test:534
Input:
Sentence: These observations suggest that mutations in this region of the collagen type I alpha 2 chain carry a high risk of abnormal limb development and intracranial bleeding .

## Item biored:test:526
Input:
Sentence: RESULTS : Except for rs1019731 , which showed a significant difference of IGF-1-SDS by genotypes ( p = 0.02 ) , all polymorphisms showed no associations with the GH-doses , IGF-1 concentrations , IGF-1-SDS and IGF-1 : GH ratio after adjusting for the confounding variables gender , age and BMI .

## Item biored:test:546
Input:
Sentence: However , it can not be excluded that the 2 unique DNA sequence alterations could have affected FOXF2 on the mRNA or protein level thus contributing to the observed disturbances in genital and palate development .

## Item biored:test:483
Input:
Sentence: Enzyme activity assays with recombinant CBR3 isoforms ( CBR3 V244 and CBR3 M244 ) and the anthracycline substrate doxorubicin were used to investigate the functional impact of the CBR3 V244M polymorphism .

## Item biored:test:470
Input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

## Item biored:test:469
Input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

## Item biored:test:572
Input:
Sentence: Ninety-seven asthmatic patients ( M/F 25/72 , mean age 39 +/- 13 years ) and 96 healthy subjects ( M/F 26/70 , mean age 38 +/- 12 years ) were included .

## Item biored:test:543
Input:
Sentence: Two patients carried a c.262G > A sequence variation predicting for an Ala88Thr exchange which was also detected in 2 normal controls .

## Item biored:test:490
Input:
Sentence: Recovery of tacrolimus-associated brachial neuritis after conversion to everolimus in a pediatric renal transplant recipient -- case report and review of the literature .

## Item biored:test:482
Input:
Sentence: Thirty patients with CHF ( cases ) and 115 matched controls were genotyped for polymorphisms in NQO1 ( NQO1 * 2 ) and CBR3 ( the CBR3 valine [ V ] to methionine [ M ] substitution at position 244 [ V244M ] ) .

## Item biored:test:536
Input:
Sentence: In contrast to disorders of sexual differentiation caused by lack of androgen production or inhibited androgen action , defects affecting development of the bipotent genital anlagen have rarely been investigated in humans .

## Item biored:test:535
Input:
Sentence: Mutation analysis of FOXF2 in patients with disorders of sex development ( DSD ) in combination with cleft palate .

## Item biored:test:542
Input:
Sentence: Two heterozygous DNA sequence variations were solely present in one single patient each but in none of the 20 normal controls : a duplication of GCC ( c.97GCC [ 9 ] + [ 10 ] ) resulting in an extra alanine within exon 1 and a 25 * G > A substitution in the 3'-untranslated region .

## Item biored:test:555
Input:
Sentence: DNA sequencing of coding regions in the AUNA1 family and in the retained homologue chromosome in the monosomic patient revealed no mutations .

## Item biored:test:520
Input:
Sentence: AIMS : Several SNPs and a microsatellite cytosine-adenine repeat promoter polymorphism of the IGF-1 gene have been reported to be associated with circulating IGF-1 serum concentrations .

## Item biored:test:565
Input:
Sentence: In silico analysis of the putative impact of the insertion shows serious clashes in protein conformation : this insertion disrupts the alpha5 helix of the dGK kinase domain , rendering the protein unable to bind purine deoxyribonucleosides .

## Item biored:test:439
Input:
Sentence: BACKGROUND : Autosomal dominant polycystic kidney disease ( ADPKD ) , which is caused by mutations in polycystins 1 ( PC1 ) and 2 ( PC2 ) , is one of the most commonly inherited renal diseases , affecting ~1 : 1000 Caucasians .

## Item biored:test:521
Input:
Sentence: Variance in IGF-1 concentrations due to genetic variations may affect different response to growth hormone ( GH ) treatment , resulting in different individually required GH-doses in GH-deficient patients .

## Item biored:test:528
Input:
Sentence: Therefore , genetic variations of the IGF-1 gene seem not to be major influencing factors of the GH-IGF-axis causing variable response to exogenous GH-treatment .

## Item biored:test:532
Input:
Sentence: Here we describe three patients , a boy ( aged 15 years ) and two girls ( aged 17 and 7 years ) with OI type III who suffered intracranial hemorrhage and in addition had brachydactyly and nail hypoplasia .

## Item biored:test:560
Input:
Sentence: In this study , we describe a new splice site mutation in the DGUOK gene and the clinical , radiologic , and genetic features of these DGUOK patients .

## Item biored:test:563
Input:
Sentence: Interestingly , we found subtentorial abnormal myelination and moderate hyperintensity in the bilateral pallidi in our patients .

## Item biored:test:587
Input:
Sentence: Laboratory test findings on admission were notable only for a flecainide plasma concentration of 1360 microg/L ( reference range 200-1000 ) .

## Item biored:test:487
Input:
Sentence: In line , recombinant CBR3 V244 ( G allele ) synthesized 2.6-fold more cardiotoxic doxorubicinol per unit of time than CBR3 M244 ( A allele ; CBR3 V244 [ 8.26+/-3.57 nmol/hour.mg ] vs CBR3 M244 [ 3.22+/-0.67 nmol/hour.mg ] ; P=.01 ) .

## Item biored:test:523
Input:
Sentence: MATERIALS & METHODS : A total of nine tagging SNPs , five additionally selected SNPs and a cytosine-adenine repeat polymorphism were determined in 133 German adult patients ( 66 men , 67 women ; mean age 45.4 years +/- 13.1 standard deviation ; majority Caucasian ) with GH-deficiency ( GHD ) of different origin , derived from the prospective Pfizer International Metabolic Study ( KIMS ) Pharmacogenetics Study .

## Item biored:test:573
Input:
Sentence: At baseline , all participants completed a questionnaire on demographics , symptoms , triggering factors , severity of asthma , and the presence of atopism .

## Item biored:test:566
Input:
Sentence: In addition , a common haplotype that segregated with the disease in both families was detected by haplotype reconstruction with 10 markers ( microsatellites and SNPs ) , which span 4.6 Mb of DNA covering the DGUOK locus .

## Item biored:test:558
Input:
Sentence: The first founder DGUOK mutation associated with hepatocerebral mitochondrial DNA depletion syndrome .

## Item biored:test:533
Input:
Sentence: In all of these patients , OI was caused by glycine mutations affecting exon 49 of the COL1A2 gene , which codes for the most carboxy-terminal part of the triple-helical domain of the collagen type I alpha 2 chain .

## Item biored:test:590
Input:
Sentence: Her delirium resolved 3 days later .

## Item biored:test:580
Input:
Sentence: Patients with mild or moderate-severe asthma had similar frequencies of these mutations .

## Item biored:test:584
Input:
Sentence: CASE SUMMARY : A 69-year-old white female presented to the emergency department with a history of confusion and paranoia over the past several days .

## Item biored:test:480
Input:
Sentence: Thus , in this study , the authors examined whether common polymorphisms in candidate genes involved in the pharmacodynamics of anthracyclines ( in particular , the nicotinamide adenine dinucleotide phosphate : quinone oxidoreductase 1 gene NQO1 and the carbonyl reductase 3 gene CBR3 ) had an impact on the risk of anthracycline-related CHF .

## Item biored:test:488
Input:
Sentence: CONCLUSIONS : The functional CBR3 V244M polymorphism may have an impact on the risk of anthracycline-related CHF among childhood cancer survivors by modulating the intracardiac formation of cardiotoxic anthracycline alcohol metabolites .

## Item biored:test:570
Input:
Sentence: Several candidate genes have been identified with a potential role in the pathogenesis of asthma , including the angiotensin converting enzyme ( ACE ) gene .

## Item biored:test:571
Input:
Sentence: We aimed to investigate the frequency of an ACE gene polymorphism in Turkish asthmatic patients and to determine its impact on clinical parameters and disease severity .

## Item biored:test:564
Input:
Sentence: This new mutation creates a cryptic splice site in intron 3 ( in position -62 ) and is predicted to result in a larger protein with an in-frame insertion of 20 amino acids .

## Item biored:test:529
Input:
Sentence: Osteogenesis imperfecta type III with intracranial hemorrhage and brachydactyly associated with mutations in exon 49 of COL1A2 .

## Item biored:test:554
Input:
Sentence: Genotyping of STRs and single nucleotide polymorphisms defined the AUNA1 breakpoint as 35 kb 5 ' to PCDH9 , with a 2.4 Mb area of overlap with the IT .

## Item biored:test:589
Input:
Sentence: Paroxetine was discontinued and the dose of flecainide was reduced to 50 mg twice daily .

## Item biored:test:539
Input:
Sentence: We hypothesized that humans with disorders of sex development ( DSD ) in combination with cleft palate could have mutations in the FOXF2 gene .

## Item biored:test:538
Input:
Sentence: Moreover , Foxf2 knockout mice present with cleft palate in combination with hypoplasia of the genital tubercle .

## Item biored:test:577
Input:
Sentence: The DD ACE genotype was significantly more frequent in asthmatics compared with controls ( p < 0.001 ) .

## Item biored:test:626
Input:
Sentence: Heart rate ( HR ) , MAP , stroke volume ( SV ) , cardiac output ( CO ) , and frontal lobe oxygenation ( S ( c ) O ( 2 ) ) were registered .

## Item biored:test:594
Input:
Sentence: CONCLUSIONS : Supratherapeutic flecainide plasma concentrations may cause delirium .

## Item biored:test:627
Input:
Sentence: RESULTS : Induction of anesthesia was followed by a decrease in MAP , HR , SV , and CO concomitant with an elevation in S ( c ) O ( 2 ) .

## Item biored:test:597
Input:
Sentence: Autism spectrum disorders ( ASDs ) are heterogeneous disorders presenting with increased rates of anxiety .

## Item biored:test:629
Input:
Sentence: However , a 14 % ( from 70 +/- 8 % to 60 +/- 7 % ) reduction in S ( c ) O ( 2 ) ( P < 0.05 ) followed with no change in CO ( 3.7 +/- 1.1 to 3.4 +/- 0.9 l min ( -1 ) ) .

## Item biored:test:567
Input:
Sentence: In conclusion , we report a new DGUOK splice site mutation that provide insight into a critical protein domain ( dGK kinase domain ) and the first founder mutation in a North-African population .

## Item biored:test:619
Input:
Sentence: VDR expression was not significantly related with patient survival , prognosis , or clinical outcome .

## Item biored:test:588
Input:
Sentence: A metabolic drug interaction between flecainide and paroxetine , which the patient had been taking for more than 5 years , was considered .

## Item biored:test:586
Input:
Sentence: Flecainide had been started 2 weeks prior for atrial fibrillation .

## Item biored:test:464
Input:
Sentence: The present study aimed to investigate the anticonvulsant activity as well as the effects on the level of hippocampal amino acid neurotransmitters ( glutamate , aspartate , glycine and GABA ) of N- ( 2-propylpentanoyl ) urea ( VPU ) in comparison to its parent compound , valproic acid ( VPA ) .

## Item biored:test:623
Input:
Sentence: BACKGROUND : Vasopressor agents are used to correct anesthesia-induced hypotension .

## Item biored:test:559
Input:
Sentence: Deoxyguanosine kinase ( dGK ) deficiency is a frequent cause of mitochondrial DNA depletion associated with a hepatocerebral phenotype .

## Item biored:test:636
Input:
Sentence: This resulted in a silent change at codon 34 of the mature protein .

## Item biored:test:637
Input:
Sentence: In vitro splicing assays showed that the mutant minigene dramatically affected pre-mRNA processing , causing exon 2 to be completely skipped .

## Item biored:test:544
Input:
Sentence: Two silent mutations , c.1272C > T ( Ser424Ser ) and c.1284T > C ( Tyr428Tyr ) , respectively , occurred in the coding region of exon 2 , again in both patients and normal controls .

## Item biored:test:638
Input:
Sentence: The putative product from a new out-of-frame translational start point in exon 3 is expected to yield a nonsense 25-amino-acid peptide .

## Item biored:test:607
Input:
Sentence: Drug-related globus pallidus infarctions are most often associated with heroin .

## Item biored:test:630
Input:
Sentence: The administration of ephedrine led to a similar increase in MAP ( 53 +/- 9 to 79 +/- 8 mmHg ; P < 0.001 ) , restored CO ( 3.2 +/- 1.2 to 5.0 +/- 1.3 l min ( -1 ) ) , and preserved S ( c ) O ( 2 ) .

## Item biored:test:578
Input:
Sentence: Asthmatics with the ID ACE genotype showed a higher frequency of drug allergies , although this was not statistically significant ( p = 0.08 ) .

## Item biored:test:628
Input:
Sentence: After administration of phenylephrine , MAP increased ( 51 +/- 12 to 81 +/- 13 mmHg ; P < 0.001 ; mean +/- SD ) .

## Item biored:test:561
Input:
Sentence: This new DGUOK homozygous mutation ( c.444-62C > A ) was identified in three patients from two North-African consanguineous families with combined respiratory chain deficiencies and mitochondrial DNA depletion in the liver .

## Item biored:test:517
Input:
Sentence: Rs13266634 ( OR = 1.19 , 95 % CI = 1.00-1.42 , p = 0.045 ) in SLC30A8 showed a nominal association with the risk of T2DM , whereas SNPs in IGF2BP2 , FTO and WFS1 were not associated .

## Item biored:test:568
Input:
Sentence: Angiotensin converting enzyme gene polymorphism in Turkish asthmatic patients .

## Item biored:test:547
Input:
Sentence: Pure monosomy and pure trisomy of 13q21.2-31.1 consequent to a familial insertional translocation : exclusion of PCDH9 as the responsible gene for autosomal dominant auditory neuropathy ( AUNA1 ) .

## Item biored:test:582
Input:
Sentence: Delirium in a patient with toxic flecainide plasma concentrations : the role of a pharmacokinetic drug interaction with paroxetine .

## Item biored:test:603
Input:
Sentence: Findings point toward a possible mediating role of ADORA2A variants on phenotypic expression in ASD that need to be replicated in a larger sample .

## Item biored:test:583
Input:
Sentence: OBJECTIVE : To describe a case of flecainide-induced delirium associated with a pharmacokinetic drug interaction with paroxetine .

## Item biored:test:612
Input:
Sentence: The vitamin D receptor ( VDR ) is a transcription factor , which plays an important role in cellular differentiation and inhibition of proliferation .

## Item biored:test:605
Input:
Sentence: Cocaine is a risk factor for both ischemic and haemorrhagic stroke .

## Item biored:test:611
Input:
Sentence: Vitamin D is associated with decreased risks of various cancers , including colon cancer .

## Item biored:test:608
Input:
Sentence: Bilateral basal ganglia infarcts after the use of cocaine , without concurrent heroin use , have never been reported .

## Item biored:test:641
Input:
Sentence: Data from in silico analysis confirmed that the C88Y mutation would affect subunit conformation .

## Item biored:test:591
Input:
Sentence: DISCUSSION : Flecainide and pharmacologically similar agents that interact with sodium channels may cause delirium in susceptible patients .

## Item biored:test:593
Input:
Sentence: According to the Naranjo probability scale , flecainide was the probable cause of the patient 's delirium ; the Horn Drug Interaction Probability Scale indicates a possible pharmacokinetic drug interaction between flecainide and paroxetine .

## Item biored:test:615
Input:
Sentence: Among 619 colorectal cancers in two prospective cohort studies , 233 ( 38 % ) tumors showed VDR overexpression by immunohistochemistry .

## Item biored:test:595
Input:
Sentence: Because toxicity may occur when flecainide is prescribed with paroxetine and other potent CYP2D6 inhibitors , flecainide plasma concentrations should be monitored closely with commencement of CYP2D6 inhibitors .
