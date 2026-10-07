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

## Item biored:test:541
Example input:
Sentence: To identify a gene for MC , we performed linkage analysis with high-density SNP arrays in a single family , used a targeted array to capture exons and promoter sequences from the linked interval in 16 participants from 11 MC families , and sequenced the captured DNA using high-throughput parallel sequencing technologies .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sequence analysis of the VWF gene from two unrelated type 2A VWD patients showed an identical , novel , heterozygous T -- > G transversion at nucleotide 4508 , resulting in the substitution of L1503R in the VWF A2 domain .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "type 2A VWD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "T -- > G transversion at nucleotide 4508", "type": "SequenceVariant"}, {"text": "L1503R", "type": "SequenceVariant"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We evaluated 16 single nucleotide polymorphisms ( SNPs ) spanning the entire COX-2 gene in 94 subjects of the control group .

Example answer:
{"entities": [{"text": "COX-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the present investigation four SNPs in two transcription factors , Single minded 2 ( SIM2 ) and V-ets erythroblastosis virus E26 oncogene homolog2 ( ETS2 ) , located in the 21 { st } chromosome were genotyped to understand their role in DS .

Example answer:
{"entities": [{"text": "Single minded 2", "type": "GeneOrGeneProduct"}, {"text": "SIM2", "type": "GeneOrGeneProduct"}, {"text": "V-ets erythroblastosis virus E26 oncogene homolog2", "type": "GeneOrGeneProduct"}, {"text": "ETS2", "type": "GeneOrGeneProduct"}, {"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We analyzed the nucleotidic sequence of the CYP2F1 gene in DNA samples from 90 French Caucasians consisting in 44 patients with lung cancer and 46 control individuals , using single-strand conformation polymorphism analysis of PCR products ( PCR-SSCP ) .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The goal of this study was to perform 5-alpha-reductase type 2 gene ( SRD5A2 ) analysis in a male pseudohermaphrodite ( MPH ) patient with normal testosterone ( T ) production and normal androgen receptor ( AR ) gene coding sequences .

Example answer:
{"entities": [{"text": "5-alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "male pseudohermaphrodite", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The HFE and TfR2 genes were analyzed by sequencing the coding region and splicing sites .

Example answer:
{"entities": [{"text": "HFE", "type": "GeneOrGeneProduct"}, {"text": "TfR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , the main outcome measure was the sequencing of genomic DNA from peripheral blood samples of 41 women with POF and 36 fertile women ( controls ) .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Genomic DNA sequence analysis of the FOXF2 gene was performed and compared with 10 normal female and 10 normal male controls , respectively .

## Item biored:test:557
Example input:
Sentence: A combination of fluorescence in situ hybridization ( FISH ) and Southern blot analysis demonstrated disruption of a synaptotagmin gene ( SYT14 ) at the 1q32 breakpoint .

Example answer:
{"entities": [{"text": "synaptotagmin", "type": "GeneOrGeneProduct"}, {"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , haplotype analysis showed that the patient does not carry any paternal DNA markers extending 33kb in the telomeric direction from the ALG6 region , and microsatellite analysis extended the abnormal region to at least 2.5Mb .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "ALG6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TS enhancer region , 3R G > C single nucleotide polymorphism ( SNP ) , and TS 1494del6 polymorphisms were assessed in both fresh-frozen normal mucosa and tumor .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "G > C", "type": "SequenceVariant"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To investigate the underlying molecular mechanisms , we characterized the DNA breakpoints of 11 germ-line deletions , six for MLH1 and five for MSH2 .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , to date there is no evidence for a mechanism of haploinsufficiency that can fully explain the DGS/VCFS phenotype .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Similarly , protein mislocalization of the homeodomain mutations also correlated with clinical severity , suggesting an emerging genotype vs cellular phenotype correlation .

Example answer:
{"entities": []}

Example input:
Sentence: Linkage disequilibrium analysis and transmission distortion of the marker alleles were performed .

Example answer:
{"entities": []}

Example input:
Sentence: Analysis of the sequences surrounding the microdeletion breakpoints revealed either intrinsic repetitivity of the deleted region or short direct repeats adjacent to the breakpoint junctions .

Example answer:
{"entities": []}

Example input:
Sentence: Other regions , such as the transactivation domain , seem to be slightly more polymorphic in the human population and the impact on functionality should be further examined .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Plotting the distribution of known DNA breakpoints among the introns of the two genes showed that , the highest breakpoint density is co-localized with the highest Alu density .

Example answer:
{"entities": []}

Input:
Sentence: Precise characterization of the breakpoints of the translocated region is useful to identify which genes may be contributing to the phenotype , either through haploinsufficiency or extra dosage effects , in order to define genotype-phenotype correlations .

## Item biored:test:524
Example input:
Sentence: Five hours after starting the infusions , a study of the pituitary responses to LH-releasing hormone ( LH-RH ) was carried out .

Example answer:
{"entities": [{"text": "LH-releasing hormone", "type": "GeneOrGeneProduct"}, {"text": "LH-RH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Total follow-up on warfarin was 530 years ( mean 28 months ) .

Example answer:
{"entities": [{"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Data were obtained from two clinical trials : 1 ) acute Epo exposure ( rHuEpo , 400 IU/kg ) followed by WAT biopsies after 1 h and 2 ) 10 weeks treatment with the erythropoiesis-stimulating agent ( ESA ) Darbepoietin-alpha .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "erythropoiesis-stimulating agent", "type": "ChemicalEntity"}, {"text": "ESA", "type": "ChemicalEntity"}, {"text": "Darbepoietin-alpha", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a prevention study , rats received 4 days of LF treatment followed by Dex and continued during the test period .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Plasma TAFI , tPA , and PAI-1 antigen levels were measured at baseline and after 3 months of treatment by commercially available ELISA kits .

Example answer:
{"entities": [{"text": "TAFI", "type": "GeneOrGeneProduct"}, {"text": "tPA", "type": "GeneOrGeneProduct"}, {"text": "PAI-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Group ADR+LOS ( 6 ) received losartan ( 10 mg/kg/b.w./day by gavages ) for 6 weeks and group ADR+LOS ( 12 ) for 12 weeks after second injection of ADR .

Example answer:
{"entities": [{"text": "ADR+LOS", "type": "ChemicalEntity"}, {"text": "losartan", "type": "ChemicalEntity"}, {"text": "ADR", "type": "ChemicalEntity"}]}

Example input:
Sentence: Among the subjects treated with methadone , 28 % men and 32 % women had prolonged QTc interval .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "prolonged QTc interval", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : A total of 4086 patients ( mean age 60.8 years ) diagnosed with RA were enrolled and received etoricoxib 90 mg daily ( n = 2032 ) or diclofenac 75 mg twice daily ( n = 2054 ) .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient achieved a partial response 6 months after the initiation of the S-1 treatment .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "S-1", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Mean ( SD ; maximum ) duration of treatment was 19.3 ( 10.3 ; 32.9 ) and 19.1 ( 10.4 ; 33.1 ) months in the etoricoxib and diclofenac groups , respectively .

Example answer:
{"entities": [{"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}]}

Input:
Sentence: Patients received GH-treatment for 12 months with finished dose-titration of GH and centralized IGF-1 measurements .

## Item biored:test:493
Example input:
Sentence: Epilepsy and/or movement disorder were major features in all 21 .

Example answer:
{"entities": [{"text": "Epilepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "movement disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine seizures cause age-dependent impairment in auditory location discrimination .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "impairment in auditory location discrimination", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients with seizures did not have permanent neurological abnormalities .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurological abnormalities", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Intracerebral hemorrhage ( ICH ) is a devastating disease without effective treatment .

Example answer:
{"entities": [{"text": "Intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is an autosomal recessive , developmental mitochondrial DNA depletion disorder characterized by deficiency in mitochondrial DNA polymerase gamma ( POLG ) catalytic activity , refractory seizures , neurodegeneration , and liver disease .

Example answer:
{"entities": [{"text": "mitochondrial DNA depletion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DNA polymerase gamma", "type": "GeneOrGeneProduct"}, {"text": "POLG", "type": "GeneOrGeneProduct"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Clinical features included hypotonia , abnormal movements , convulsions , and moderate mental retardation with relative sparing of gross motor function , activities of daily living skills , and receptive language .

Example answer:
{"entities": [{"text": "hypotonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "abnormal movements", "type": "DiseaseOrPhenotypicFeature"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the classical form it presents as neonatal apnea , intractable seizures , and hypotonia , followed by significant psychomotor retardation .

Example answer:
{"entities": [{"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Migraine is a common debilitating primary headache disorder with significant mental , physical and social health implications .

Example answer:
{"entities": [{"text": "Migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "headache disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Hypotension and a resultant decrease in cerebral blood flow have been implicated in the development of cognitive dysfunction .

Example answer:
{"entities": [{"text": "Hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cognitive dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: First described by Zinn et al in 1986 , deficiency of FH results in early onset , severe encephalopathy .

Example answer:
{"entities": [{"text": "deficiency of FH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: It is characterized by encephalopathy , headaches , seizures , or neurological deficits .

## Item biored:test:484
Example input:
Sentence: The -930A > G polymorphism of the CYBA gene is associated with premature coronary artery disease .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}, {"text": "CYBA", "type": "GeneOrGeneProduct"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , a longitudinal follow-up study on survival in the same sample indicated that 192RR homozygotes have a poorer survival compared to QQ homozygotes ( hazard rate : 1.38 , P = 0.04 ) .

Example answer:
{"entities": [{"text": "192RR", "type": "SequenceVariant"}]}

Example input:
Sentence: The androgen receptor ( AR ) gene has polymorphic regions containing variable length glutamine and glycine repeats and these are believed to be associated with PC risk .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Two coding polymorphisms , 55M/L and 192Q/R , and a promoter variant , -107C/T , has been extensively studied with respect to susceptibility to CHD .

Example answer:
{"entities": [{"text": "55M/L", "type": "SequenceVariant"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "-107C/T", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our results thus indicates that PON1 192RR homozygosity is associated with increased mortality in women in the second half of life and that this increased mortality is possibly related to CHD severity and survival after CHD rather than susceptibility to development of CHD .

Example answer:
{"entities": [{"text": "PON1", "type": "GeneOrGeneProduct"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using self-reported data on ischemic heart disease to evaluate the impact of the PON 192Q/R polymorphism on susceptibility to CHD , we found only a nonsignificant trend of 192RR homozygosity in women being a risk factor .

Example answer:
{"entities": [{"text": "ischemic heart disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PON", "type": "GeneOrGeneProduct"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}]}

Input:
Sentence: RESULTS : Multivariate analyses adjusted for sex and primary disease recurrence were used to test for associations between the candidate genetic polymorphisms ( NQO1 * 2 and CBR3 V244M ) and the risk of CHF .

## Item biored:test:513
Example input:
Sentence: The risk for type 2 diabetes in the AA genotype carriers was increased in the control group ( 5.56 [ 1.78-17.39 ] , P = 0.003 ) but not in the intervention group .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : This study included 133 patients with AVSD and 200 healthy controls .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIMS : This study sought to assess the risk of developing coronary artery disease ( CAD ) associated with initial treatment of type 2 diabetes with different sulphonylureas .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sulphonylureas", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Thirty-seven unrelated patients were studied , 18 with LCD and 19 with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MATERIAL AND METHODS : Case-control study of 50 obese patients undergoing bariatric surgery and 71 non-obese subjects matched by age and sex .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The risk of developing T2D was approximately 2-fold in individuals with genotypes associated with higher 2-hour plasma glucose levels ; the hazard ratios were 2.192 ( p = 0.025 ) for rs2073162-A , 2.191 ( p = 0.027 ) for rs2073163-C , and 1.998 ( p = 0.054 ) for rs1155974-T .

Example answer:
{"entities": [{"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "rs2073162-A", "type": "SequenceVariant"}, {"text": "rs2073163-C", "type": "SequenceVariant"}, {"text": "rs1155974-T", "type": "SequenceVariant"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : In type 2 diabetic patients , cases who developed CAD were compared retrospectively with controls that did not .

Example answer:
{"entities": [{"text": "type 2 diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: This study was based on a multicenter case-control study , including 908 patients with T2DM and 502 non-diabetic controls .

## Item biored:test:564
Example input:
Sentence: This mutation resulted in replacement of a non-polar amino acid ( proline ) with a polar amino acid ( serine ) at position 29 ( P29S ) .

Example answer:
{"entities": [{"text": "( proline ) with a polar amino acid ( serine ) at position 29", "type": "SequenceVariant"}, {"text": "P29S", "type": "SequenceVariant"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: The C139T mutation , predicted to result in the substitution of an arginine by a tryptophan ( R47W ) in the N-terminal subdomain , affected conserved residues in the PAX9 paired domain .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "arginine by a tryptophan", "type": "SequenceVariant"}, {"text": "R47W", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation was linked to a novel single nucleotide polymorphism ( SNP ) in intron 3 ( IVS3 + 18C > T ) .

Example answer:
{"entities": [{"text": "IVS3 + 18C > T", "type": "SequenceVariant"}]}

Example input:
Sentence: We found a single nucleotide deletion c.342delA , located in exon 3 , which resulted in a frameshift at amino acid position 58 ( p.Arg58fs or p.R58fs ) .

Example answer:
{"entities": [{"text": "c.342delA", "type": "SequenceVariant"}, {"text": "p.Arg58fs", "type": "SequenceVariant"}, {"text": "p.R58fs", "type": "SequenceVariant"}]}

Example input:
Sentence: Three aberrantly spliced cDNA species were identified : exon 22 and exon 22 to 23 skipping , and insertion of an 87-base pair cryptic exon .

Example answer:
{"entities": []}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation leads to the activation of a cryptic splice site , 32 bp downstream of the mutation site and to subsequent aberrant out-of-frame splicing , resulting in two alternative mRNA transcripts and a downstream PTC .

Example answer:
{"entities": []}

Input:
Sentence: This new mutation creates a cryptic splice site in intron 3 ( in position -62 ) and is predicted to result in a larger protein with an in-frame insertion of 20 amino acids .

## Item biored:test:469
Example input:
Sentence: CONCLUSION : The data show that CCR2 and CCL2 are up-regulated in the hippocampus after pilocarpine-induced SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The current data showed that pilocarpine significantly delayed onset of arrhythmias , decreased the time course of ventricular tachycardia and fibrillation , reduced arrhythmia score , and increased the survival time of arrhythmic rats and guinea pigs .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventricular tachycardia and fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "guinea pigs", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Behavioral and neurochemical studies in mice pretreated with garcinielliptone FC in pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "garcinielliptone FC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study aimed to evaluate the GFC effects at doses of 25 , 50 or 75 mg/kg on seizure parameters to determine their anticonvulsant activity and its effects on amino acid ( r-aminobutyric acid ( GABA ) , glutamine , aspartate and glutathione ) levels as well as on acetylcholinesterase ( AChE ) activity in mice hippocampus after seizures .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "r-aminobutyric acid", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Input:
Sentence: Based on the finding that VPU and VPA could protect the animals against pilocarpine-induced seizure it is suggested that the reduction of inhibitory amino acid neurotransmitters was comparatively minor and offset by a pronounced reduction of glutamate and aspartate .

## Item biored:test:537
Example input:
Sentence: Focused transcriptomics revealed that myocyte-specific enhancer factor 2C ( MEF2C ) and myogenic factor 5 ( MYF5 ) expression was inhibited by high glucose levels , and endoribonuclease-prepared small interfering RNA-mediated combined inhibition of those transcription factors phenocopied the glycolytic shift that was observed in high glucose conditions .

Example answer:
{"entities": [{"text": "myocyte-specific enhancer factor 2C", "type": "GeneOrGeneProduct"}, {"text": "MEF2C", "type": "GeneOrGeneProduct"}, {"text": "myogenic factor 5", "type": "GeneOrGeneProduct"}, {"text": "MYF5", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The transcription factor hepatocyte nuclear factor ( HNF ) -6 is an upstream regulator of several genes involved in the pathogenesis of maturity-onset diabetes of the young .

Example answer:
{"entities": [{"text": "hepatocyte nuclear factor ( HNF ) -6", "type": "GeneOrGeneProduct"}, {"text": "maturity-onset diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present investigation four SNPs in two transcription factors , Single minded 2 ( SIM2 ) and V-ets erythroblastosis virus E26 oncogene homolog2 ( ETS2 ) , located in the 21 { st } chromosome were genotyped to understand their role in DS .

Example answer:
{"entities": [{"text": "Single minded 2", "type": "GeneOrGeneProduct"}, {"text": "SIM2", "type": "GeneOrGeneProduct"}, {"text": "V-ets erythroblastosis virus E26 oncogene homolog2", "type": "GeneOrGeneProduct"}, {"text": "ETS2", "type": "GeneOrGeneProduct"}, {"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study highlights the importance of the 5 ' untranslated region ( UTR ) in identification of genes of human disease , suggests that a single-nucleotide substitution in the 5 ' UTR could be associated with protein aggregation , and indicates that the GEF protein is associated with cerebellar degeneration in humans .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "GEF", "type": "GeneOrGeneProduct"}, {"text": "cerebellar degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: PAX9 and MSX1 are transcription factors that play essential roles in craniofacial and limb development .

Example answer:
{"entities": [{"text": "PAX9", "type": "GeneOrGeneProduct"}, {"text": "MSX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OSX encodes a transcription factor containing three Cys2-His2 zinc-finger DNA-binding domains at its C terminus , which , in mice , has been shown to be essential for bone formation .

Example answer:
{"entities": [{"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We show that FGFR2 signalling correlates with maintenance of expression of a key transcription factor for basal cell self-renewal and differentiation : SOX2 .

Example answer:
{"entities": [{"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "SOX2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We have previously documented that the transcription factor FOXF2 is highly expressed in human foreskin .

## Item biored:test:546
Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To elucidate the pathogenic mechanism producing oligodontia phenotype caused by this mutation , we analyzed the binding of wild-type and mutant PAX9 paired domain protein to double-stranded DNA targets .

Example answer:
{"entities": [{"text": "oligodontia phenotype", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel missense mutation in the paired domain of human PAX9 causes oligodontia .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}, {"text": "oligodontia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: The same variants in the IRF6 gene that are associated with isolated orofacial clefts are also associated with human tooth agenesis ( rs861019 , P = 0.058 ; rs17015215-V274I , P = 0.0006 ; rs7802 , P = 0.004 ) .

Example answer:
{"entities": [{"text": "IRF6", "type": "GeneOrGeneProduct"}, {"text": "orofacial clefts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tooth agenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs861019", "type": "SequenceVariant"}, {"text": "rs17015215-V274I", "type": "SequenceVariant"}, {"text": "rs7802", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : Gene polymorphism resulting in the substitution of glutamine with lysine at residue 223 in the carbohydrate recognition domain of SP-A2 increases susceptibility to meningococcal disease , as well as the risk of death .

Example answer:
{"entities": [{"text": "glutamine with lysine at residue 223", "type": "SequenceVariant"}, {"text": "carbohydrate", "type": "ChemicalEntity"}, {"text": "SP-A2", "type": "GeneOrGeneProduct"}, {"text": "meningococcal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Also , it records a novel deletion in exon 1 of SRD5A2 gene in a patient with severe hypospadias .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "hypospadias", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , it can not be excluded that the 2 unique DNA sequence alterations could have affected FOXF2 on the mRNA or protein level thus contributing to the observed disturbances in genital and palate development .

## Item biored:test:526
Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The genotype distribution of the Met326Ile polymorphism in the PCOS group was not different from that of the controls ( Met326Met/Met326Ile/Ile326Ile rates were 73.4 % /23.4 % /3.2 % and 70.3 % /26.1 % /3.6 % for the PCOS and control groups , respectively , P = 0.72 ) .

Example answer:
{"entities": [{"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "PCOS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Met326Met/Met326Ile/Ile326Ile", "type": "SequenceVariant"}]}

Example input:
Sentence: Our aim was to study the associations of individual single nucleotide polymorphisms and haplotypes with adiposity , glucose metabolism , and the risk of type 2 diabetes ( T2D ) .

Example answer:
{"entities": [{"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Two single nucleotide polymorphisms ( SNPs ) in GPX4 ( rs713041 and rs757229 ) were associated with all-cause mortality even after adjusting for multiple hypothesis testing ( adjusted P = .0041 and P = .0035 ) .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "rs713041", "type": "SequenceVariant"}, {"text": "rs757229", "type": "SequenceVariant"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: This Ag ( +25 G- > A ) polymorphism is associated with the Gg-globin-XmnI polymorphism and both are linked with the b ( 0 ) 39-globin gene , but not with the b ( + ) IVSI-110-globin gene .

Example answer:
{"entities": [{"text": "Ag", "type": "GeneOrGeneProduct"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Gg-globin-XmnI", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39-globin", "type": "GeneOrGeneProduct"}, {"text": "b ( + ) IVSI-110-globin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After adjustment for sex and age , we found no association of SNPs rs6235 and rs6232 with BMI or other weight-related traits ( all p > or= 0.07 ) .

Example answer:
{"entities": [{"text": "rs6235", "type": "SequenceVariant"}, {"text": "rs6232", "type": "SequenceVariant"}]}

Input:
Sentence: RESULTS : Except for rs1019731 , which showed a significant difference of IGF-1-SDS by genotypes ( p = 0.02 ) , all polymorphisms showed no associations with the GH-doses , IGF-1 concentrations , IGF-1-SDS and IGF-1 : GH ratio after adjusting for the confounding variables gender , age and BMI .

