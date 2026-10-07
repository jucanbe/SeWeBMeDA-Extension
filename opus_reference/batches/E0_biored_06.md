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

## Item biored:test:553
Input:
Sentence: As the AUNA1 deafness locus on 13q14-21 overlaps the IT in the PCDH9 ( protocadherin-9 ) gene region , PCDH9 was investigated as a candidate gene for deafness in both families .

## Item biored:test:649
Input:
Sentence: The load of HBV was determined using an `` in-house '' real-time polymerase chain reaction .

## Item biored:test:648
Input:
Sentence: Patients provided blood samples for HBsAg detection .

## Item biored:test:647
Input:
Sentence: A cross-sectional study of 847 patients with HIV was conducted .

## Item biored:test:651
Input:
Sentence: Twenty-eight patients with co-infection were identified .

## Item biored:test:505
Input:
Sentence: This SNP is part of a large linkage disequilibrium block , which contains CCND3 , BYSL , TRFP , USP49 , C6ofr49 , FRS3 , and PGC .

## Item biored:test:642
Input:
Sentence: Indeed , two different bioinformatics approaches , PolyPhen and SIFT analysis , predicted C88Y to be a damaging substitution .

## Item biored:test:602
Input:
Sentence: In addition , association of ADORA2A variants with anxiety was replicated for individuals with ASD .

## Item biored:test:652
Input:
Sentence: The distribution of HBV genotypes among these patients was A ( n = 9 ; 50 % ) , D ( n = 4 ; 22.2 % ) , G ( n = 3 ; 16.7 % ) , and F ( n = 2 ; 11.1 % ) .

## Item biored:test:604
Input:
Sentence: Bilateral haemorrhagic infarction of the globus pallidus after cocaine and alcohol intoxication .

## Item biored:test:598
Input:
Sentence: The adenosine A ( 2A ) receptor gene ( ADORA2A ) is associated with panic disorder and is located on chromosome 22q11.23 .

## Item biored:test:599
Input:
Sentence: Its gene product , the adenosine A ( 2A ) receptor , is strongly expressed in the caudate nucleus , which also is involved in ASD .

## Item biored:test:579
Input:
Sentence: Asthmatics with the DD genotype appeared to have a higher incidence of asthmatic episode exacerbations due to viral infections , but again this was not statistically significant ( p = 0.08 ) .

## Item biored:test:672
Input:
Sentence: Moreover , this association remained significant after Bonferroni correction .

## Item biored:test:656
Input:
Sentence: This pattern and an accompanying rtV173L mutation was found in four patients .

## Item biored:test:635
Input:
Sentence: RESULTS : Patient 1 had a homozygous G to A nucleotide change at the 5 ' donor splice site of exon/intron 2 .

## Item biored:test:614
Input:
Sentence: However , the prognostic role of VDR expression or its relationship with PIK3CA or KRAS mutation remains uncertain .

## Item biored:test:659
Input:
Sentence: No putative TDF resistance substitution was detected .

## Item biored:test:606
Input:
Sentence: We present the case of a 31-year-old man with bilateral ischemia of the globus pallidus after excessive alcohol and intranasal cocaine use .

## Item biored:test:575
Input:
Sentence: The frequency of the ACE genotypes ( I = insertion and D = deletion ) among asthmatics and controls were compared : asthmatics showed a 40.2 % prevalence of the DD genotype ( n = 39 ) , ID was 45.4 % ( n = 44 ) , and II was 14.4 % ( n = 14.4 ) .

## Item biored:test:644
Input:
Sentence: Moreover , diagnosis of central hypothyroidism should be considered in the face of severe infant anemia of uncertain etiology .

## Item biored:test:661
Input:
Sentence: No putative TDF resistance change was detected after prolonged use of TDF .

## Item biored:test:617
Input:
Sentence: VDR overexpression was significantly associated with KRAS mutation ( odds ratio , 1.55 ; 95 % confidence interval , 1.11-2.16 ) and PIK3CA mutation ( odds ratio , 2.17 ; 95 % confidence interval , 1.36-3.47 ) , both of which persisted in multivariate logistic regression analysis .

## Item biored:test:516
Input:
Sentence: The G allele of rs1111875 ( OR = 1.43 , 95 % CI = 1.18-1.72 , p = 1.8 x 10 ( -4 ) ) in HHEX ) , the T allele of rs10811661 ( OR = 1.47 , 95 % CI = 1.23-1.75 , p = 2.1 x 10 ( -5 ) ) in CDKN2A/B ) and the C allele of rs2237892 ( OR = 1.31 , 95 % CI = 1.10-1.56 , p = 0.003 ) in KCNQ1 showed significant associations with T2DM .

## Item biored:test:643
Input:
Sentence: CONCLUSIONS : In isolated TSH deficiency , the exact molecular diagnosis is mandatory for diagnosis of isolated pituitary deficiency , delineation of prognosis , and genetic counseling .

## Item biored:test:592
Input:
Sentence: A MEDLINE search ( 1966-January 2009 ) revealed one in vivo pharmacokinetic study on the interaction between flecainide , a CYP2D6 substrate , and paroxetine , a CYP2D6 inhibitor , as well as 3 case reports of flecainide-induced delirium .

## Item biored:test:653
Input:
Sentence: Eighteen patients were treated with LAM and six patients were treated with LAM plus TDF .

## Item biored:test:633
Input:
Sentence: CONTEXT : Patients with TSH-beta subunit defects and congenital hypothyroidism are missed by TSH-based neonatal screening .

## Item biored:test:654
Input:
Sentence: The length of exposure to LAM and TDF varied from 4 to 216 months .

## Item biored:test:632
Input:
Sentence: Two novel mutations of the TSH-beta subunit gene underlying congenital central hypothyroidism undetectable in neonatal TSH screening .

## Item biored:test:624
Input:
Sentence: We describe the effect of phenylephrine and ephedrine on frontal lobe oxygenation ( S ( c ) O ( 2 ) ) following anesthesia-induced hypotension .

## Item biored:test:518
Input:
Sentence: In conclusion , we have shown that SNPs in HHEX , CDKN2A/B , CDKAL1 , KCNQ1 and SLC30A8 confer a risk of T2DM in the Korean population .

## Item biored:test:622
Input:
Sentence: Phenylephrine but not ephedrine reduces frontal lobe oxygenation following anesthesia-induced hypotension .

## Item biored:test:680
Input:
Sentence: The study was designed as case-control study including 891 patients with documented PAD and 777 control subjects .

## Item biored:test:663
Input:
Sentence: BACKGROUND : Altered serotonergic neural transmission is hypothesized to be a susceptibility factor for psychotic disorders such as schizophrenia .

## Item biored:test:679
Input:
Sentence: Aim of the present study was to analyze the role of this polymorphism in peripheral arterial disease ( PAD ) .

## Item biored:test:610
Input:
Sentence: Vitamin D receptor expression is associated with PIK3CA and KRAS mutations in colorectal cancer .

## Item biored:test:699
Input:
Sentence: High-resolution melting curve analysis ( hrMCA ) has recently been developed as a post-PCR mutation scanning method which enables simple , rapid , cost-effective , and highly sensitive mutation screening of large genes .

## Item biored:test:634
Input:
Sentence: OBJECTIVE : Our objective was to report the molecular consequences of a novel splice-junction mutation and a novel missense mutation in the TSH-beta subunit gene found in two patients with congenital central hypothyroidism and conventional treatment-resistant anemia .

## Item biored:test:670
Input:
Sentence: The age and sex of the control subjects did not differ from those of the methamphetamine dependence patients .

## Item biored:test:552
Input:
Sentence: The phenotype of pure monosomy included deafness , duodenal stenosis , developmental and growth delay , vertebral anomalies , and facial dysmorphisms ; the trisomy was manifested by only minor dysmorphisms .

## Item biored:test:693
Input:
Sentence: About 1 year later , abdominal computed tomography revealed enlargement of kidneys .

## Item biored:test:596
Input:
Sentence: Adenosine A ( 2A ) receptor gene ( ADORA2A ) variants may increase autistic symptoms and anxiety in autism spectrum disorder .

## Item biored:test:655
Input:
Sentence: LAM resistance substitutions ( rtL180M + rtM204V ) were detected in 10 ( 50 % ) of the 20 patients with viremia .

## Item biored:test:620
Input:
Sentence: In conclusion , VDR overexpression in colorectal cancer is independently associated with PIK3CA and KRAS mutations .

## Item biored:test:676
Input:
Sentence: Conversion of fibrinogen to fibrin plays an essential role in hemostasis and results in stabilization of the fibrin clot .

## Item biored:test:556
Input:
Sentence: We conclude that AUNA1 deafness does not share a common etiology with deafness associated with monosomy 13q21.2-q31.3 ; deafness may result from monosomy of PCHD9 or another gene in the IT , as has been demonstrated in contiguous gene deletion syndromes .

## Item biored:test:640
Input:
Sentence: This cysteine residue is conserved among all dimeric pituitary and placental glycoprotein hormone-beta subunits .

## Item biored:test:625
Input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

## Item biored:test:639
Input:
Sentence: In patient 2 , sequence analysis revealed a compound heterozygosis for the already reported 313delT ( C105Vfs114X ) mutation and for a second novel mutation in exon 3 , substituting G for A at cDNA nucleotide position 323 , resulting in a C88Y change .

## Item biored:test:700
Input:
Sentence: We established a hrMCA method to screen for COL3A1 mutations using genomic DNA .

## Item biored:test:701
Input:
Sentence: PCR primers pairs for COL3A1 ( 52 amplicons ) were designed to cover all coding regions of the 52 exons , including the splicing sites .

## Item biored:test:645
Input:
Sentence: High frequency of lamivudine resistance mutations in Brazilian patients co-infected with HIV and hepatitis B .

## Item biored:test:702
Input:
Sentence: We used 15 DNA samples ( 8 validation samples and 7 samples of clinically suspected vEDS patients ) in this study .

## Item biored:test:650
Input:
Sentence: HBV genotypes/subgenotypes , antiviral resistance , basal core promoter ( BCP ) , and precore mutations were detected by DNA sequencing .

## Item biored:test:510
Input:
Sentence: Association between polymorphisms in SLC30A8 , HHEX , CDKN2A/B , IGF2BP2 , FTO , WFS1 , CDKAL1 , KCNQ1 and type 2 diabetes in the Korean population .

## Item biored:test:692
Input:
Sentence: However , echocardiography indicated no sign of cardiomyopathy and he showed no distinct intellectual impairment that interfered with daily life .

## Item biored:test:609
Input:
Sentence: In our patient , transient cardiac arrhythmia or respiratory dysfunction related to cocaine and/or ethanol use were the most likely causes of cerebral hypoperfusion .

## Item biored:test:687
Input:
Sentence: Congenital generalized lipodystrophy ( CGL ) is a rare autosomal recessive disease that is characterized by a near-complete absence of adipose tissue from birth or early infancy .

## Item biored:test:681
Input:
Sentence: FGG genotypes were determined by exonuclease ( TaqMan ) assays .

## Item biored:test:512
Input:
Sentence: The aim of the present study was to investigate the association among the polymorphisms of SLC30A8 , HHEX , CDKN2A/B , IGF2BP2 , FTO , WFS1 , CDKAL1 and KCNQ1 and the risk of T2DM in the Korean population .

## Item biored:test:660
Input:
Sentence: The data suggest that prolonged LAM use is associated with the emergence of particular changes in the HBV genome , including substitutions that may elicit a vaccine escape phenotype .

## Item biored:test:682
Input:
Sentence: FGG genotype frequencies were not significantly different between PAD patients ( CC : 57.3 % , CT : 36.7 % , TT : 5.8 % ) and control subjects ( CC : 60.9 % , CT : 33.5 % , TT 5.6 % ; p=0.35 ) .

## Item biored:test:690
Input:
Sentence: Absence of mechanical adipose tissue in the orbits and scalp was revealed by head magnetic resonance imaging .

## Item biored:test:696
Input:
Sentence: A novel mutation screening system for Ehlers-Danlos Syndrome , vascular type by high-resolution melting curve analysis in combination with small amplicon genotyping using genomic DNA .

## Item biored:test:722
Input:
Sentence: The deletions were defined using long distance inverse PCR and microarray-based comparative genomic hybridization .

## Item biored:test:621
Input:
Sentence: Our data support potential interactions between the VDR , RAS-MAPK and PI3K-AKT pathways , and possible influence by KRAS or PIK3CA mutation on therapy or chemoprevention targeting VDR .

## Item biored:test:713
Input:
Sentence: Mutation analysis of all coding exons of the GUCA1B gene was performed by polymerase chain reaction amplification of genomic DNA and subsequent DNA sequencing .

## Item biored:test:716
Input:
Sentence: All sequence variants were previously reported in healthy subjects .

## Item biored:test:666
Input:
Sentence: These animal models were considered to reflect the positive symptoms of schizophrenia , and the above evidence suggests that altered 5-HT6 receptors are involved in the pathophysiology of psychotic disorders .

## Item biored:test:707
Input:
Sentence: A better understanding of the genotype-phenotype correlation in COL3A1 using this method will lead to improve in diagnosis and treatment .

## Item biored:test:671
Input:
Sentence: RESULTS : rs6693503 was associated with METH-induced psychosis patients in the allele/genotype-wise analysis .

## Item biored:test:585
Input:
Sentence: On admission the patient was taking carvedilol 12 mg twice daily , warfarin 2 mg/day , folic acid 1 mg/day , levothyroxine 100 microg/day , pantoprazole 40 mg/day , paroxetine 40 mg/day , and flecainide 100 mg twice daily .

## Item biored:test:646
Input:
Sentence: This study analyzed the genotype distribution and frequency of lamivudine ( LAM ) and tenofovir ( TDF ) resistance mutations in a group of patients co-infected with HIV and hepatitis B virus ( HBV ) .

## Item biored:test:698
Input:
Sentence: Most COL3A1 mutations are detected by using total RNA from patient-derived fibroblasts , which requires an invasive skin biopsy .

## Item biored:test:718
Input:
Sentence: Large contiguous gene deletions in Sjogren-Larsson syndrome .

## Item biored:test:581
Input:
Sentence: We found a higher frequency of the ACE DD gene mutation in Turkish asthmatic patients compared with non-asthmatics , suggesting that this ACE gene polymorphism may be a risk factor for asthma but does not increase the severity of the disease .

## Item biored:test:600
Input:
Sentence: As autistic symptoms are increased in individuals with 22q11.2 deletion syndrome , and large 22q11.2 deletions and duplications have been observed in ASD individuals , in this study , 98 individuals with ASD and 234 control individuals were genotyped for eight single-nucleotide polymorphisms in ADORA2A .

## Item biored:test:712
Input:
Sentence: Material and Methods : Twenty-four unrelated patients diagnosed with cone dystrophy or cone rod dystrophy according to standard diagnostic criteria and a family history consistent with an autosomal dominant mode of inheritance were included in the study .

## Item biored:test:703
Input:
Sentence: The eight known COL3A1 mutations in validation samples were all successfully detected by the hrMCA .

## Item biored:test:601
Input:
Sentence: Nominal association with the disorder was observed for rs2236624-CC , and phenotypic variability in ASD symptoms was influenced by rs3761422 , rs5751876 and rs35320474 .

## Item biored:test:675
Input:
Sentence: The fibrinogen gamma 10034C > T polymorphism is not associated with Peripheral Arterial Disease .

## Item biored:test:662
Input:
Sentence: Serotonin 6 receptor gene is associated with methamphetamine-induced psychosis in a Japanese population .

## Item biored:test:658
Input:
Sentence: Mutations in the BCP region ( A1762T , G1764A ) and in the precore region ( G1896A , G1899A ) were also found .

## Item biored:test:667
Input:
Sentence: The symptoms of methamphetamine ( METH ) -induced psychosis are similar to those of paranoid type schizophrenia .

## Item biored:test:710
Input:
Sentence: However , the role of GUCA1B gene mutations in inherited retinal disease has been controversial .

## Item biored:test:720
Input:
Sentence: More than 70 mutations have been identified in SLS patients , including small deletions or insertions , missense mutations , splicing defects and complex nucleotide changes .

## Item biored:test:684
Input:
Sentence: The FGG 10034C > T polymorphism was furthermore not associated with age at onset of PAD .

## Item biored:test:674
Input:
Sentence: CONCLUSION : HTR6 may play an important role in the pathophysiology of METH-induced psychosis in the Japanese population .

## Item biored:test:668
Input:
Sentence: Therefore , we conducted an analysis of the association of the 5-HT6 gene ( HTR6 ) with METH-induced psychosis .

## Item biored:test:697
Input:
Sentence: Ehlers-Danlos syndrome , vascular type ( vEDS ) ( MIM # 130050 ) is an autosomal dominant disorder caused by type III procollagen gene ( COL3A1 ) mutations .

## Item biored:test:726
Input:
Sentence: These studies suggest that large gene deletions may account for up to 5 % of the mutant alleles in SLS .

## Item biored:test:749
Input:
Sentence: METHODS : Patients and family members were given complete physical , ophthalmic , and cardiovascular examinations .

## Item biored:test:754
Input:
Sentence: Protein structure was modeled based on the Protein data bank and mutated in DeepView v4.0.1 to predict the functional consequences of the mutation .

## Item biored:test:686
Input:
Sentence: A Taiwanese boy with congenital generalized lipodystrophy caused by homozygous Ile262fs mutation in the BSCL2 gene .

## Item biored:test:677
Input:
Sentence: Fibrinogen consists of three pairs of non-identical polypeptide chains , encoded by different genes ( fibrinogen alpha [ FGA ] , fibrinogen beta [ FGB ] and fibrinogen gamma [ FGG ] ) .

## Item biored:test:708
Input:
Sentence: Mutation screening of the GUCA1B gene in patients with autosomal dominant cone and cone rod dystrophy .

## Item biored:test:689
Input:
Sentence: We report a 3-month-old Taiwanese boy with initial presentation of a lack of subcutaneous fat , prominent musculature , generalized eruptive xanthomas , and extreme hypertriglyceridemia .

## Item biored:test:729
Input:
Sentence: Loss or reduction in function of tumor suppressor genes contributes to tumorigenesis .

## Item biored:test:694
Input:
Sentence: He had a homozygous insertion of a nucleotide , 783insG ( Ile262fs mutation ) , in exon 7 of the BSCL2 gene .
