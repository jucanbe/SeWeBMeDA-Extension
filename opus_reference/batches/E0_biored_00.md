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

## Item biored:test:15
Input:
Sentence: This region includes the last five exons detected by cDNA5b-7 , all exons detected by cDNA8 , and the first two exons detected by cDNA9 .

## Item biored:test:12
Input:
Sentence: ( ABSTRACT TRUNCATED AT 250 WORDS )

## Item biored:test:19
Input:
Sentence: Clinical findings are presented for all 80 patients allowing a correlation of phenotypic severity with the genotype .

## Item biored:test:23
Input:
Sentence: This is in agreement with recent findings by Baumbach et al .

## Item biored:test:25
Input:
Sentence: but is in contrast to findings , by Malhotra et al .

## Item biored:test:24
Input:
Sentence: and Koenig et al .

## Item biored:test:48
Input:
Sentence: This mutation was not found in 50 controls .

## Item biored:test:49
Input:
Sentence: Reverse transcription-PCR revealed that a large proportion of the mutant transcripts were spliced aberrantly , causing premature termination of the protein synthesis .

## Item biored:test:64
Input:
Sentence: METHODS : Family history and clinical data were recorded .

## Item biored:test:68
Input:
Sentence: Linkage analysis was performed , and candidate genes were PCR amplified and screened for mutations on both strands using direct sequencing .

## Item biored:test:73
Input:
Sentence: Electron microscopy showed that cortical lens fiber morphology was normal .

## Item biored:test:46
Input:
Sentence: No mutations were found in 76 male patients .

## Item biored:test:26
Input:
Sentence: at the 5 ' end of the gene .

## Item biored:test:47
Input:
Sentence: However , one female patient was heterozygous for a normal allele and a mutant allele with an A to C substitution at nucleotide 879 in exon 9 .

## Item biored:test:41
Input:
Sentence: The routine use of pethidine via PCA even for a brief postoperative analgesia should be reconsidered .

## Item biored:test:65
Input:
Sentence: The phenotype was documented by both slit lamp and Scheimpflug photography .

## Item biored:test:34
Input:
Sentence: It is suggested that nefiracetam augments molecular processes in the early stages of events which ultimately lead to consolidation of memory .

## Item biored:test:37
Input:
Sentence: Twenty-three h postoperatively he developed a brief self-limited seizure .

## Item biored:test:39
Input:
Sentence: No other risk factors for CNS toxicity were identified .

## Item biored:test:66
Input:
Sentence: One cortical lens was evaluated by electron microscopy after cataract extraction .

## Item biored:test:67
Input:
Sentence: Lenticular phenotyping and genotyping were performed independently with short tandem repeat polymorphism .

## Item biored:test:63
Input:
Sentence: PURPOSE : To identify the genetic defect leading to the congenital nuclear cataract affecting a large five-generation Swiss family .

## Item biored:test:22
Input:
Sentence: Thus , with two exceptions , frameshift deletions of the gene resulted in more severe phenotype than did in-frame deletions .

## Item biored:test:70
Input:
Sentence: Linkage was observed on chromosome 17 for DNA marker D17S1857 ( lod score : 3.44 at theta = 0 ) .

## Item biored:test:7
Input:
Sentence: Five PMs were studied according to the same protocol , except for a higher terbutaline dose ( 0.75 mg ) on day 2 .

## Item biored:test:36
Input:
Sentence: A healthy 17-year-old male received standard intermittent doses of pethidine via a patient-controlled analgesia ( PCA ) pump for management of postoperative pain control .

## Item biored:test:16
Input:
Sentence: These 80 individuals account for approximately 75 % of 109 deletions of the gene , detected among 181 patients analyzed with the entire dystrophin cDNA .

## Item biored:test:85
Input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

## Item biored:test:69
Input:
Sentence: RESULTS : Affected individuals had a congenital nuclear lactescent cataract in both eyes .

## Item biored:test:17
Input:
Sentence: Endpoints for many of these deletions were further characterized using two genomic probes , p20 ( DXS269 ; Wapenaar et al . )

## Item biored:test:18
Input:
Sentence: and GMGX11 ( DXS239 ; present paper ) .

## Item biored:test:57
Input:
Sentence: All rats were terminated either 24 h or 3 weeks after the DFP injection .

## Item biored:test:72
Input:
Sentence: This mutation involved a deletion of glycine-91 , cosegregated in all affected individuals , and was not observed in unaffected individuals or in 250 normal control subjects from the same ethnic background .

## Item biored:test:80
Input:
Sentence: Through linkage with the Swedish Cancer Register , all subjects in this cohort diagnosed with bladder cancer were identified .

## Item biored:test:76
Input:
Sentence: These results indicate phenotypic heterogeneity related to mutations in this gene .

## Item biored:test:79
Input:
Sentence: METHODS : In the population based , nationwide Swedish Inpatient Register a cohort of 1065 patients with Wegener 's granulomatosis , 1969-95 , was identified .

## Item biored:test:83
Input:
Sentence: RESULTS : The median cumulative doses of cyclophosphamide among cases ( n = 11 ) and controls ( n = 25 ) were 113 g and 25 g , respectively .

## Item biored:test:40
Input:
Sentence: This method allowed frequent self-dosing of pethidine at short time intervals and rapid accumulation of pethidine and norpethidine .

## Item biored:test:71
Input:
Sentence: Direct sequencing of CRYBA3/A1 , which maps to the vicinity , revealed an in-frame 3-bp deletion in exon 4 ( 279delGAG ) .

## Item biored:test:3
Input:
Sentence: We investigated if the latter also applies to the beta-2 adrenoceptor antagonism by metoprolol .

## Item biored:test:11
Input:
Sentence: There was a difference in metoprolol potency with higher racemic metoprolol IC50 values in PMs ( 72 +/- 7 ng.ml-1 ) than EMs ( 42 +/- 8 ng.ml-1 , P less than .001 ) .

## Item biored:test:30
Input:
Sentence: A step-down passive avoidance paradigm was employed and nefiracetam ( 3 mg/kg ) and apomorphine ( 0.5 mg/kg ) were given alone or in combination during training and at the 10-12h post-training period of consolidation .

## Item biored:test:13
Input:
Sentence: Molecular and phenotypic analysis of patients with deletions within the deletion-rich region of the Duchenne muscular dystrophy ( DMD ) gene .

## Item biored:test:54
Input:
Sentence: The protective action of subcutaneously ( SC ) administered antidotes or their combinations in DFP ( 2.0 mg/kg BW ) intoxication was studied in 9-10-weeks-old Han-Wistar male rats .

## Item biored:test:21
Input:
Sentence: Of these , eight BMD patients and one intermediate patient had gene deletions predicted to leave the reading frame intact , while 21 DMD patients , 7 intermediate patients , and 1 BMD patient had gene deletions predicted to disrupt the reading frame .

## Item biored:test:62
Input:
Sentence: CRYBA3/A1 gene mutation associated with suture-sparing autosomal dominant congenital nuclear cataract : a novel phenotype .

## Item biored:test:97
Input:
Sentence: Thus far , although two loci for DSAP have been identified , the genetic basis and pathogenesis of this disorder have not been elucidated yet .

## Item biored:test:51
Input:
Sentence: Organophosphate-induced convulsions and prevention of neuropathological damages .

## Item biored:test:75
Input:
Sentence: A splice mutation ( IVS3+1G/A ) in this gene has been reported in a zonular cataract with sutural opacities .

## Item biored:test:35
Input:
Sentence: Pethidine-associated seizure in a healthy adolescent receiving pethidine for postoperative pain control .

## Item biored:test:38
Input:
Sentence: Both plasma pethidine and norpethidine were elevated in the range associated with clinical manifestations of central nervous system excitation .

## Item biored:test:6
Input:
Sentence: Six EMs received 0.5 mg of terbutaline s.c. on two different occasions : 1 ) 1 hr after administration of a placebo and 2 ) 1 hr after 150 mg of metoprolol p.o .

## Item biored:test:28
Input:
Sentence: Nefiracetam is a novel pyrrolidone derivative which attenuates scopolamine-induced learning and post-training consolidation deficits .

## Item biored:test:31
Input:
Sentence: Co-administration of nefiracetam and apomorphine during training or 10h thereafter produced no significant anti-amnesic effect .

## Item biored:test:1
Input:
Sentence: The metabolism of the cardioselective beta-blocker metoprolol is under genetic control of the debrisoquine/sparteine type .

## Item biored:test:105
Input:
Sentence: METHODS : We analyzed 186 individuals with spontaneous HCV clearance , 501 chronically HCV infected patients , and 217 healthy controls .

## Item biored:test:20
Input:
Sentence: Thirty-eight independent patients were old enough to be classified as DMD , BMD , or intermediate phenotype and had deletions of exons with sequenced intron/exon boundaries .

## Item biored:test:106
Input:
Sentence: IL12B 3'-UTR and promoter genotyping was performed by Taqman-based assays with allele-specific oligonucleotide probes and PCR-based allele-specific DNA-amplification , respectively .

## Item biored:test:114
Input:
Sentence: METHODS : Mutational analysis and DNA sequencing were conducted in a newborn .

## Item biored:test:9
Input:
Sentence: In PMs , metoprolol increased the terbutaline area under the plasma concentration vs. time curve ( +67 % ) .

## Item biored:test:107
Input:
Sentence: RESULTS : The proportion of IL12B promoter and 3'-UTR genotypes did not differ significantly between the different cohorts .

## Item biored:test:5
Input:
Sentence: By using pharmacokinetic pharmacodynamic modeling the pharmacodynamics of racemic metoprolol and the active S-isomer , were quantitated in EMs and PMs in terms of IC50 values , representing metoprolol plasma concentrations resulting in half-maximum receptor occupancy .

## Item biored:test:60
Input:
Sentence: Atropine-MK801 did not offer any additional protection against DFP toxicity .

## Item biored:test:117
Input:
Sentence: The proband was heterozygous but the mutation was absent in the parents and the sister .

## Item biored:test:4
Input:
Sentence: The drug effect studied was the antagonism by metoprolol of terbutaline-induced hypokalemia .

## Item biored:test:32
Input:
Sentence: However , administration of nefiracetam during training completely reversed the amnesia induced by apomorphine at the 10h post-training time and the converse was also true .

## Item biored:test:81
Input:
Sentence: Nested within the cohort , a matched case-control study was performed to estimate the association between cyclophosphamide and bladder cancer using odds ratios ( ORs ) as relative risk .

## Item biored:test:45
Input:
Sentence: We screened all 17 exons of the FMR1 gene for mutations in 90 autistic or mentally retarded children using polymerase chain reaction ( PCR ) -single strand conformation polymorphism ( SSCP ) analysis .

## Item biored:test:0
Input:
Sentence: Debrisoquine phenotype and the pharmacokinetics and beta-2 receptor pharmacodynamics of metoprolol and its enantiomers .

## Item biored:test:58
Input:
Sentence: The rats treated with DFP-atropine showed severe typical OP-induced toxicity signs .

## Item biored:test:127
Input:
Sentence: Genotypes were analyzed by disease-free survival analysis using a Cox proportional hazards model .

## Item biored:test:130
Input:
Sentence: In contrast to the result of Healey et al .

## Item biored:test:84
Input:
Sentence: The risk of bladder cancer doubled for every 10 g increment in cyclophosphamide ( OR = 2.0 , 95 % confidence interval ( CI ) 0.8 to 4.9 ) .

## Item biored:test:82
Input:
Sentence: In the cohort the cumulative risk of bladder cancer after Wegener 's granulomatosis , and the relative prevalence of a history of bladder cancer at the time of diagnosis of Wegener 's granulomatosis , were also estimated .

## Item biored:test:86
Input:
Sentence: The absolute risk for bladder cancer in the cohort reached 10 % 16 years after diagnosis of Wegener 's granulomatosis , and a history of bladder cancer was ( non-significantly ) twice as common as expected at the time of diagnosis of Wegener 's granulomatosis .

## Item biored:test:44
Input:
Sentence: It is usually caused by an expansion of the trinucleotide repeat in the 5'-untranslated region of the FMR1 gene , but in a small number of patients deletions and point mutations have been identified .

## Item biored:test:74
Input:
Sentence: CONCLUSIONS : The DeltaG91 mutation in CRYBA3/A1 is associated with an autosomal dominant congenital nuclear lactescent cataract .

## Item biored:test:119
Input:
Sentence: We also found a similar electrophysiological profile for the neighboring V1764M mutant .

## Item biored:test:125
Input:
Sentence: The study includes 778 women carrying a BRCA1 germ-line mutation belonging to 403 families .

## Item biored:test:95
Input:
Sentence: Fine mapping and identification of a candidate gene SSH1 in disseminated superficial actinic porokeratosis .

## Item biored:test:10
Input:
Sentence: Higher metoprolol/alpha-hydroxymetoprolol ratios in PMs were predictive for higher R-/S-isomer ratios of unchanged drug .

## Item biored:test:100
Input:
Sentence: SSH1 encodes a phosphatase that plays a pivotal role in actin dynamics .

## Item biored:test:42
Input:
Sentence: Single-strand conformation polymorphism analysis of the FMR1 gene in autistic and mentally retarded children in Japan .

## Item biored:test:140
Input:
Sentence: This increase persisted for 8 hrs .

## Item biored:test:50
Input:
Sentence: Although uncommon , point mutations in the FMR1 gene may be a cause of autism and mental retardation in Japanese patients .

## Item biored:test:8
Input:
Sentence: Blood samples for the analysis of plasma potassium , terbutaline , metoprolol ( racemic , R- and S-isomer ) , and alpha-hydroxymetoprolol concentrations were taken at regular time intervals , during 8 hr after metoprolol .

## Item biored:test:27
Input:
Sentence: Nefiracetam ( DM-9384 ) reverses apomorphine-induced amnesia of a passive avoidance response : delayed emergence of the memory retention effects .

## Item biored:test:29
Input:
Sentence: Given that apomorphine inhibits passive avoidance retention when given during training or in a defined 10-12h post-training period , we evaluated the ability of nefiracetam to attenuate amnesia induced by dopaminergic agonism .

## Item biored:test:98
Input:
Sentence: In this study , we performed a genome-wide linkage analysis in three Chinese affected families and localized the gene in an 8.0 cM interval defined by D12S330 and D12S354 on chromosome 12 .

## Item biored:test:93
Input:
Sentence: TCR protected against pathological changes induced by isoproterenol in rat heart .

## Item biored:test:137
Input:
Sentence: Microdialysis samples were collected preischemia , before IT injection , and at 2 , 4 , 8 , 24 , and 48 h of reperfusion ( after IT injection ) .

## Item biored:test:77
Input:
Sentence: Urinary bladder cancer in Wegener 's granulomatosis : risks and relation to cyclophosphamide .

## Item biored:test:135
Input:
Sentence: Spinal cord ischemia was induced by aortic occlusion for 6 min with a balloon catheter .

## Item biored:test:78
Input:
Sentence: OBJECTIVE : To assess and characterise the risk of bladder cancer , and its relation to cyclophosphamide , in patients with Wegener 's granulomatosis .

## Item biored:test:120
Input:
Sentence: But , the other neighboring I1762A mutant had no persistent current and was still associated with a positive shift of inactivation .

## Item biored:test:157
Input:
Sentence: The effects of specific variants on expression of common markers were evaluated by in vitro transcription/translation .

## Item biored:test:90
Input:
Sentence: The present study was done to investigate the protective effect of TCR on experimentally induced myocardial infarction in rats .

## Item biored:test:43
Input:
Sentence: Fragile X syndrome is one of the most common causes of mental retardation in males , and patients with fragile X syndrome occasionally develop autism .

## Item biored:test:87
Input:
Sentence: CONCLUSION : The results indicate a dose-response relationship between cyclophosphamide and the risk of bladder cancer , high cumulative risks in the entire cohort , and also the possibility of risk factors operating even before Wegener 's granulomatosis .

## Item biored:test:94
Input:
Sentence: The results show that pretreatment with TCR may be useful in preventing the damage induced by isoproterenol in rat heart .
