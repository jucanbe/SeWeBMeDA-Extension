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

## Item biored:test:811
Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the saline group , 45 % of the mice developed large hematomas ( i.e. , > 15 microL ) .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "hematomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Adult female Thra1 ( PV/+ ) mice had short stature , grossly abnormal bone morphology but normal bone strength despite high bone mass .

Example answer:
{"entities": [{"text": "Thra1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , we demonstrate that mice genetically engineered to have unilateral brain DA deficits develop METH-induced dopaminergic deficits that are of comparable magnitude on both sides of the brain .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "dopaminergic deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the abundance and proliferative index of lymph node , thymus and CNS CD4 ( + ) CD25 ( + ) FoxP3 ( + ) Tregs were strikingly reduced in VPAC2-deficient mice with EAE .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}, {"text": "VPAC2-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Compared with WT mice , the liver weight and liver metastatic rate were significantly lower in AT1aKO .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "liver metastatic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The model mice had much higher serum levels of ALT and AST than the normal mice .

## Item biored:test:762
Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gankyrin binds to Src homology 2 domain-containing protein tyrosine phosphatase-1 ( SHP-1 ) , mainly expressed in liver non-parenchymal cells , resulting in phosphorylation and activation of signal transducer and activator of transcription 3 ( STAT3 ) .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "Src homology 2 domain-containing protein tyrosine phosphatase-1", "type": "GeneOrGeneProduct"}, {"text": "SHP-1", "type": "GeneOrGeneProduct"}, {"text": "signal transducer and activator of transcription 3", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The presence of wild-type SLURP-1 is essential for normal T-cell activation .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SLURP-1 is an allosteric agonist to the nicotinic acetylcholine receptor ( nAchR ) and it regulates epidermal homeostasis .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "nicotinic acetylcholine receptor", "type": "GeneOrGeneProduct"}, {"text": "nAchR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: MAIN METHODS : Since NNK-dependent transformation can be abolished by the nicotinergic secreted mammalian Ly-6/urokinase plasminogen activator receptor related protein-1 ( SLURP-1 ) , we compared effects of NNK and recombinant ( r ) SLURP-1 on the expression of genes related to tumorigenesis in human immortalized bronchial and oral epithelial cell lines BEP2D and Het-1A , respectively .

## Item biored:test:618
Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combination of polymorphisms within 5 ' and 3 ' untranslated regions of thymidylate synthase gene modulates survival in 5 fluorouracil-treated colorectal cancer patients .

Example answer:
{"entities": [{"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "5", "type": "ChemicalEntity"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Tumor thymidylate synthase 1494del6 genotype as a prognostic factor in colorectal cancer patients receiving fluorouracil-based adjuvant treatment .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil-based", "type": "ChemicalEntity"}]}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SNP 10510452_139 in the promoter region was shown to have a high posterior probability ( P = 0.77-0.86 ) of influencing BMI , fat mass , and waist circumference in Hispanic children .

Example answer:
{"entities": [{"text": "SNP 10510452_139", "type": "SequenceVariant"}]}

Example input:
Sentence: Our results thus indicates that PON1 192RR homozygosity is associated with increased mortality in women in the second half of life and that this increased mortality is possibly related to CHD severity and survival after CHD rather than susceptibility to development of CHD .

Example answer:
{"entities": [{"text": "PON1", "type": "GeneOrGeneProduct"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VNTR and ins/del 6 bp genotypes varied with tumour anatomical site : 2R/2R genotype was rare in left-sided tumours ( 7.0 % vs. 26.3 % of right-sided and 24.1 % of rectal cancers ; P < 0.01 ) , where the variant allele 6- was very frequent ( 69.0 % ) .

Example answer:
{"entities": [{"text": "ins/del 6 bp", "type": "SequenceVariant"}, {"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumours", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rectal cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: VDR was not independently associated with body mass index , family history of colorectal cancer , tumor location ( colon versus rectum ) , stage , tumor grade , signet ring cells , CIMP , MSI , LINE-1 hypomethylation , BRAF , p53 , p21 , beta-catenin , or cyclooxygenase-2 .

## Item biored:test:843
Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : The effect of pretreatment with trazodone on dexamphetamine- and apomorphine-induced oral stereotypies , on catalepsy induced by haloperidol and apomorphine ( 0.05 mg/kg , i.p .

Example answer:
{"entities": [{"text": "trazodone", "type": "ChemicalEntity"}, {"text": "dexamphetamine-", "type": "ChemicalEntity"}, {"text": "apomorphine-induced", "type": "ChemicalEntity"}, {"text": "oral stereotypies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , there is convincing clinical evidence that monotherapy with continuous subcutaneous apomorphine infusions is associated with marked reductions of preexisting levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : In a 16-week multicenter , double-blind trial , 122 children with ADHD were randomly assigned to clonidine ( n = 31 ) , methylphenidate ( n = 29 ) , clonidine and methylphenidate ( n = 32 ) , or placebo ( n = 30 ) .

Example answer:
{"entities": [{"text": "ADHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}, {"text": "methylphenidate", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : We found that cocaine dose-dependently increased anxiety-like behavior in control ( Dbh +/- ) mice , as measured by a decrease in open arm exploration .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: induced catalepsy and antagonized apomorphine and dexamphetamine stereotypies .

Example answer:
{"entities": []}

Example input:
Sentence: did not induce catalepsy , and did not antagonize apomorphine ( 1.5 and 3 mg/kg ) stereotypy and apomorphine ( 0.05 mg/kg ) -induced catalepsy .

Example answer:
{"entities": []}

Example input:
Sentence: The results showed a significant increase in escape latencies and traveled distances to find platform in scopolamine-treated group as compared to saline group .

Example answer:
{"entities": [{"text": "scopolamine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Amphetamine abuse was predictive of larger cranial to body growth ratios .

Example answer:
{"entities": [{"text": "Amphetamine", "type": "ChemicalEntity"}]}

Input:
Sentence: RESULTS : In the amphetamine-induced locomotion test , there were significant increases in all movements compared with the amphetamine-free group .

## Item biored:test:785
Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "mitochondrial impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: N-Acetylglucosamine ( O-GlcNAc ) transferase ( OGT ) regulates protein O-GlcNAcylation , an essential and dynamic post-translational modification .

Example answer:
{"entities": [{"text": "N-Acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "O-GlcNAcylation", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In TIPE2 over-expression cells , caspase-3 , caspase-9 , and Bax were significantly up-regulated while Bcl-2 was down-regulated .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "caspase-9", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also observed apoptotic cell death in TD as demonstrated by PI/Annexin V staining , TUNEL assay , and Cell Death ELISA .

Example answer:
{"entities": [{"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: We conclude that defects in O-GlcNAc homeostasis and host cell factor 1 proteolysis may play roles in mediation of XLID in individuals with OGT mutations .

Example answer:
{"entities": [{"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OGT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Immunofluorescence staining and subcellular fractionation analyses revealed increased mitochondrial translocation of Bad and Bax proteins from cytoplasm following OGD ( 4 h ) and simultaneously increased release of Cyt C from mitochondria followed by activation of caspase-3 .

## Item biored:test:829
Example input:
Sentence: Bortezomib ( bort ) -dexamethasone ( dex ) is an effective therapy for relapsed/refractory ( R/R ) multiple myeloma ( MM ) .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After verifying the epidural space , bupivacaine and triamcinolone diacetate were injected .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "triamcinolone diacetate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prevention of etomidate-induced myoclonus : which is superior : Fentanyl , midazolam , or a combination ?

Example answer:
{"entities": [{"text": "etomidate-induced", "type": "ChemicalEntity"}, {"text": "myoclonus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "midazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : In this retrospective comparative study , we aimed to compare the effectiveness of fentanyl , midazolam , and a combination of fentanyl and midazolam to prevent etomidate-induced myoclonus .

Example answer:
{"entities": [{"text": "fentanyl", "type": "ChemicalEntity"}, {"text": "midazolam", "type": "ChemicalEntity"}, {"text": "etomidate-induced", "type": "ChemicalEntity"}, {"text": "myoclonus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The first group of patients was administered isotonic sodium chloride ; the second group was administered a solution that of 5 % dextrose and sodium bicarbonate , while the third group was administered isotonic sodium chloride before and after the contrast injection .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "sodium chloride", "type": "ChemicalEntity"}, {"text": "dextrose", "type": "ChemicalEntity"}, {"text": "sodium bicarbonate", "type": "ChemicalEntity"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient was treated with hyperosmolar therapy , hyperventilation , sedation , and chemical paralysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "hyperventilation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: INTERVENTIONS : Continuous sedation with dexmedetomidine or propofol .

## Item biored:test:789
Example input:
Sentence: CONCLUSIONS : Overall , these results suggest that KCa3.1 is involved in the regulation of Ca2+ homeostasis in astrocytes and attenuation of the UPR and ER stress , thus contributing to memory deficits and neuronal loss .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: IPA-3 , which prevents PAK2 binding to small-GTPases partially inhibited PAK2-activation , as well as reduced CCK-induced ERK1/2 activation and amylase release induced by CCK or bombesin .

Example answer:
{"entities": [{"text": "IPA-3", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small-GTPases", "type": "GeneOrGeneProduct"}, {"text": "PAK2-activation", "type": "GeneOrGeneProduct"}, {"text": "CCK-induced", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "amylase", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "bombesin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Voltage-Dependent Anion Channel 1 ( VDAC1 ) Participates the Apoptosis of the Mitochondrial Dysfunction in Desminopathy .

Example answer:
{"entities": [{"text": "Voltage-Dependent Anion Channel 1", "type": "GeneOrGeneProduct"}, {"text": "VDAC1", "type": "GeneOrGeneProduct"}, {"text": "Mitochondrial Dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Desminopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , apoptotic proteins are also involved in the desminopathies , like bax , ATF2 , but not bcl-2 , bcl-xl or HK2 .

Example answer:
{"entities": [{"text": "desminopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: VDAC1 regulates mitochondrial uptake across the outer membrane and mitochondrial outer membrane permeabilization ( MOMP ) .

Example answer:
{"entities": [{"text": "VDAC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In TIPE2 over-expression cells , caspase-3 , caspase-9 , and Bax were significantly up-regulated while Bcl-2 was down-regulated .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "caspase-9", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Meanwhile apoptosis related proteins bax and ATF2 were involved in desminopathy patients and desminopathy rat model , but not bcl-2 , bcl-xl or HK2.VDAC1 and desmin are closely relevant in the tissue splices of deminopathies patients and rats with desminopathy at protein lever .

Example answer:
{"entities": [{"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2.VDAC1", "type": "GeneOrGeneProduct"}, {"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Our results indicate a regulatory role of NP1 in Bad/Bax-dependent mitochondrial release of Cyt C and caspase-3 activation .

## Item biored:test:846
Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: While powerful antiparkinsonian effects had been observed as early as 1951 , the potential of treating fluctuating Parkinson 's disease by subcutaneous administration of apomorphine has only recently become the subject of systematic study .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: A number of small scale clinical trials have unequivocally shown that intermittent subcutaneous apomorphine injections produce antiparkinsonian benefit close if not identical to that seen with levodopa and that apomorphine rescue injections can reliably revert off-periods even in patients with complex on-off motor swings .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Continuous subcutaneous apomorphine infusions can reduce daily off-time by more than 50 % in this group of patients , which appears to be a stronger effect than that generally seen with add-on therapy with oral dopamine agonists or COMT inhibitors .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "dopamine agonists", "type": "ChemicalEntity"}, {"text": "COMT inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed a significant increase in escape latencies and traveled distances to find platform in scopolamine-treated group as compared to saline group .

Example answer:
{"entities": [{"text": "scopolamine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Extended follow-up studies of up to 8 years have demonstrated long-term persistence of apomorphine efficacy .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: did not induce catalepsy , and did not antagonize apomorphine ( 1.5 and 3 mg/kg ) stereotypy and apomorphine ( 0.05 mg/kg ) -induced catalepsy .

Example answer:
{"entities": []}

Input:
Sentence: There was no significant difference between groups in terms of total climbing time in the apomorphine-induced climbing test ( p > 0.05 ) .

## Item biored:test:801
Example input:
Sentence: In this study , we establish the unilateral ureteric obstruction ( UUO ) or folic acid ( FA ) -induced mice renal interstitial fibrosis in vivo and the transforming growth factor ( TGF ) -beta1-stimulated human proximal tubular epithelial cell ( HK-2 ) model in vitro .

Example answer:
{"entities": [{"text": "unilateral ureteric obstruction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "UUO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "folic acid", "type": "ChemicalEntity"}, {"text": "FA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor ( TGF )", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Example input:
Sentence: For in vivo experiments , a model of myocardial infarction ( MI ) was established using both TIEG1 KO and WT mice .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: For in vitro experiments , cardiomyocytes were isolated from both TIEG1 knockout ( KO ) and wile-type ( WT ) mice , and the apoptotic ratios were evaluated after a 48-h ischaemic insult .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ( Anacardiaceae ) , on isoproterenol ( ISPH ) -induced myocardial infarction ( MI ) in rats through its antioxidative mechanism .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "ISPH", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Viruses were evaluated for replication in SCID mice transplanted with human hepatoma cells ( SCID-HuH-7 mice ) , in mosquitoes , and in rhesus monkeys .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hepatoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCID-HuH-7", "type": "CellLine"}, {"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Input:
Sentence: Cultured mycelium Cordyceps sinensis protects liver sinusoidal endothelial cells in acute liver injured mice .

## Item biored:test:839
Example input:
Sentence: Daily administration of desipramine , an inhibitor of the NET , for 5 days decreased [ ( 3 ) H ] norepinephrine uptake in the P2 fractions of hippocampus but not cortex , striatum or amygdalae .

Example answer:
{"entities": [{"text": "desipramine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , intraspinal injection of 5,7-DHT to produce a more selective lesion of only descending serotonin projections in the spinal cord did not affect this hypotension .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: hiPS-CMs were seeded onto MEA and FPD was measured for 2min every 10min for 30min after drug exposure for the vehicle and each drug concentration .

Example answer:
{"entities": []}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Administration of salvianolic acid A for a period of 8 days significantly attenuated isoproterenol-induced cardiac dysfunction and myocardial injury and improved mitochondrial respiratory function .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Data were obtained from two clinical trials : 1 ) acute Epo exposure ( rHuEpo , 400 IU/kg ) followed by WAT biopsies after 1 h and 2 ) 10 weeks treatment with the erythropoiesis-stimulating agent ( ESA ) Darbepoietin-alpha .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "erythropoiesis-stimulating agent", "type": "ChemicalEntity"}, {"text": "ESA", "type": "ChemicalEntity"}, {"text": "Darbepoietin-alpha", "type": "ChemicalEntity"}]}

Example input:
Sentence: In spontaneously hypertensive , stroke-prone rats , microinjection of methyldopa into the area of the midline B3 serotonin cell group in the ventral medulla caused a potent hypotension of 30-40 mm Hg , which was maximal 2-3 h after administration and was abolished by the serotonin neurotoxin 5,7-dihydroxytryptamine ( 5,7-DHT ) injected intracerebroventricularly .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke-prone", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5,7-dihydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5,7-DHT", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Upon pretreatment with mangiferin ( 100 mg/kg body weight suspended in 2 ml of dimethyl sulphoxide ) given intraperitoneally for 28 days to MI rats protected the above-mentioned parameters to fall from the normal levels .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "dimethyl sulphoxide", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: The DHEA was administered intraperitoneally ( ip ) for 5 days .

## Item biored:test:795
Example input:
Sentence: The current study aimed to assess the impact of MDMA use on three separate central executive processes ( set shifting , inhibition and memory updating ) and also on `` prefrontal '' mediated social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of the study was to investigate the effects of moderate and heavy MDMA use on cognitive function , as well as the effects of long-term abstention from MDMA , in subjects genotyped for 5-HTTLPR .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: Memory function and serotonin transporter promoter gene polymorphism in ecstasy ( MDMA ) users .

Example answer:
{"entities": [{"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "impaired social and emotional judgement processes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fifteen moderate MDMA users ( < 55 lifetime tablets ) , 22 heavy MDMA+ users ( > 55 lifetime tablets ) , 16 ex-MDMA+ users ( last tablet > 1 year ago ) and 13 controls were compared on a battery of neuropsychological tests .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "MDMA+", "type": "ChemicalEntity"}]}

Example input:
Sentence: Compared with MDMA-free polydrug controls , MDMA polydrug users showed impairments in set shifting and memory updating , and also in social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA-free", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: To address the potential confounding effects of the cannabis use of the ecstasy using group , a second analysis included 14 previously tested cannabis users ( Nestor , L. , Roberts , G. , Garavan , H. , Hester , R. , 2008 .

Example answer:
{"entities": [{"text": "cannabis", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Input:
Sentence: METHODS : A sample of 997 participants ( 52 % male ) was recruited to four control groups ( non-drug ( ND ) , alcohol/nicotine ( AN ) , cannabis/alcohol/nicotine ( CAN ) , non-ecstasy polydrug ( PD ) ) , and two ecstasy polydrug groups ( present ( MDMA ) and past users ( EX-MDMA ) .

## Item biored:test:822
Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anesthesia was continued uneventfully with propofol infusion while all facilities were available to detect and treat malignant hyperthermia .

Example answer:
{"entities": [{"text": "propofol", "type": "ChemicalEntity"}, {"text": "malignant hyperthermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "enflurane", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A comparison of severe hemodynamic disturbances between dexmedetomidine and propofol for sedation in neurocritical care patients .

## Item biored:test:825
Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anesthesia was continued uneventfully with propofol infusion while all facilities were available to detect and treat malignant hyperthermia .

Example answer:
{"entities": [{"text": "propofol", "type": "ChemicalEntity"}, {"text": "malignant hyperthermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The primary objective of this study is to compare the prevalence of severe hemodynamic effects in neurocritical care patients receiving dexmedetomidine and propofol .

## Item biored:test:857
Example input:
Sentence: Moreover , by regulating the expression of BIK ( BCL2-interacting killer ) , Star-PAP induced apoptosis of breast cancer cells through the mitochondrial pathway .

Example answer:
{"entities": [{"text": "BIK", "type": "GeneOrGeneProduct"}, {"text": "BCL2-interacting killer", "type": "GeneOrGeneProduct"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , apoptotic proteins are also involved in the desminopathies , like bax , ATF2 , but not bcl-2 , bcl-xl or HK2 .

Example answer:
{"entities": [{"text": "desminopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The results of the present study suggested that atorvastatin protected against contrast-induced renal tubular cell apoptosis through the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced renal tubular cell apoptosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study aimed to investigate whether atorvastatin protects against CIN via anti-apoptotic effects by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: The apoptosis rate of cells was quantified via flow cytometry following Annexin V/propidium iodide staining .

Example answer:
{"entities": [{"text": "Annexin", "type": "GeneOrGeneProduct"}, {"text": "iodide", "type": "ChemicalEntity"}]}

Example input:
Sentence: We also observed apoptotic cell death in TD as demonstrated by PI/Annexin V staining , TUNEL assay , and Cell Death ELISA .

Example answer:
{"entities": [{"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: To confirm the pro-apoptotic effects , we performed flow cytometric detection , cardiac histology , transmission electron microscopy and terminal deoxynucleotidyl transferase-mediated dUTP-biotin nick end labeling assay .

## Item biored:test:858
Example input:
Sentence: The results demonstrated that hypoxia induced apoptosis , increased ROS production , and promoted autophagy in a time-dependent manner relative to that observed under normoxia .

Example answer:
{"entities": [{"text": "hypoxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results suggested that emodin-regulated cell growth and apoptosis were mediated by inhibiting FASN and provide a molecular basis for colon cancer therapy .

Example answer:
{"entities": [{"text": "emodin-regulated", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , by regulating the expression of BIK ( BCL2-interacting killer ) , Star-PAP induced apoptosis of breast cancer cells through the mitochondrial pathway .

Example answer:
{"entities": [{"text": "BIK", "type": "GeneOrGeneProduct"}, {"text": "BCL2-interacting killer", "type": "GeneOrGeneProduct"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also observed apoptotic cell death in TD as demonstrated by PI/Annexin V staining , TUNEL assay , and Cell Death ELISA .

Example answer:
{"entities": [{"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The apoptosis rate of cells was quantified via flow cytometry following Annexin V/propidium iodide staining .

Example answer:
{"entities": [{"text": "Annexin", "type": "GeneOrGeneProduct"}, {"text": "iodide", "type": "ChemicalEntity"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: The results showed that aconitine stimulated apoptosis time-dependently .

## Item biored:test:833
Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Groups were compared regarding adverse events and changes from baseline to week 16 in electrocardiograms and vital signs .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : In this study population , combination therapies with VAL/HCTZ were associated with significantly greater BP reductions compared with either monotherapy , were well tolerated , and were associated with less hypokalemia than HCTZ alone .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rates of response and BP control were significantly higher in the groups that received combination treatment compared with those that received monotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: No Hardy Weinberg disequilibrium and no significant difference in allele frequencies between patients and controls were observed for any variation .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}]}

Input:
Sentence: When analyzed separately , no differences could be found in the prevalence of severe hypotension or bradycardia in either the unmatched or matched cohorts .

## Item biored:test:860
Example input:
Sentence: Flow cytometry analysis found TIPE2 overexpression promoted apoptosis of H446 .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "H446", "type": "CellLine"}]}

Example input:
Sentence: The apoptosis rate of cells was quantified via flow cytometry following Annexin V/propidium iodide staining .

Example answer:
{"entities": [{"text": "Annexin", "type": "GeneOrGeneProduct"}, {"text": "iodide", "type": "ChemicalEntity"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , by regulating the expression of BIK ( BCL2-interacting killer ) , Star-PAP induced apoptosis of breast cancer cells through the mitochondrial pathway .

Example answer:
{"entities": [{"text": "BIK", "type": "GeneOrGeneProduct"}, {"text": "BCL2-interacting killer", "type": "GeneOrGeneProduct"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Meanwhile apoptosis related proteins bax and ATF2 were involved in desminopathy patients and desminopathy rat model , but not bcl-2 , bcl-xl or HK2.VDAC1 and desmin are closely relevant in the tissue splices of deminopathies patients and rats with desminopathy at protein lever .

Example answer:
{"entities": [{"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2.VDAC1", "type": "GeneOrGeneProduct"}, {"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In TIPE2 over-expression cells , caspase-3 , caspase-9 , and Bax were significantly up-regulated while Bcl-2 was down-regulated .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "caspase-9", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , apoptotic proteins are also involved in the desminopathies , like bax , ATF2 , but not bcl-2 , bcl-xl or HK2 .

Example answer:
{"entities": [{"text": "desminopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The expression analysis of apoptosis-related proteins revealed that pro-apoptotic protein expression was upregulated , and anti-apoptotic protein BCL-2 expression was downregulated .

## Item biored:test:830
Example input:
Sentence: RESULTS : Overall , 1048 eligible injection drug users were included in our study .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : This study included 133 patients with AVSD and 200 healthy controls .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Two hundred twenty-eight patients ( 42 % men ) with a mean age of 81.1 ( range 76-94 ) were included in the analysis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: The efficacy and tolerability of VAL/HCTZ combinations were maintained during the extension ( 797 patients ) .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Eighty-five patients were enrolled , 42 in stratum 1 and 43 in stratum .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: A total of 167 patients receiving methadone fulfilled the inclusion criteria and were compared with a control group of 80 injection drug users not receiving methadone .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PATIENTS AND METHODS : A total of 4086 patients ( mean age 60.8 years ) diagnosed with RA were enrolled and received etoricoxib 90 mg daily ( n = 2032 ) or diclofenac 75 mg twice daily ( n = 2054 ) .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}]}

Input:
Sentence: MEASUREMENTS AND MAIN RESULTS : A total of 342 patients ( 105 dexmedetomidine and 237 propofol ) were included in the analysis , with 190 matched ( 95 in each group ) by propensity score .

## Item biored:test:845
Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "extrapyramidal symptoms", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : The effect of pretreatment with trazodone on dexamphetamine- and apomorphine-induced oral stereotypies , on catalepsy induced by haloperidol and apomorphine ( 0.05 mg/kg , i.p .

Example answer:
{"entities": [{"text": "trazodone", "type": "ChemicalEntity"}, {"text": "dexamphetamine-", "type": "ChemicalEntity"}, {"text": "apomorphine-induced", "type": "ChemicalEntity"}, {"text": "oral stereotypies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: did not induce catalepsy , and did not antagonize apomorphine ( 1.5 and 3 mg/kg ) stereotypy and apomorphine ( 0.05 mg/kg ) -induced catalepsy .

Example answer:
{"entities": []}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haloperidol-induced catalepsy was challenged with prior intracollicular microinjections of glutamate NMDA receptor antagonists , MK-801 ( 15 or 30 mmol/0.5 microl ) and AP7 ( 10 or 20 nmol/0.5 microl ) , or of the NMDA receptor agonist N-methyl-d-aspartate ( NMDA , 20 or 30 nmol/0.5 microl ) .

Example answer:
{"entities": [{"text": "Haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glutamate NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "NMDA receptor", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-d-aspartate", "type": "ChemicalEntity"}, {"text": "NMDA", "type": "ChemicalEntity"}]}

Input:
Sentence: There was a significant difference between groups in the haloperidol-induced catalepsy test ( p < 0.05 ) .

## Item biored:test:831
Example input:
Sentence: Patients with essential hypertension ( mean sitting diastolic BP [ MSDBP ] , > or =95 mm Hg and < 110 mm Hg ) were randomized to 1 of 8 treatment groups : VAL 160 or 320 mg ; HCTZ 12.5 or 25 mg ; VAL/HCTZ 160/12.5 , 320/12.5 , or 320/25 mg ; or placebo .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolonged hypothermia as a bridge to recovery for cerebral edema and intracranial hypertension associated with fulminant hepatic failure .

Example answer:
{"entities": [{"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In spontaneously hypertensive , stroke-prone rats , microinjection of methyldopa into the area of the midline B3 serotonin cell group in the ventral medulla caused a potent hypotension of 30-40 mm Hg , which was maximal 2-3 h after administration and was abolished by the serotonin neurotoxin 5,7-dihydroxytryptamine ( 5,7-DHT ) injected intracerebroventricularly .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke-prone", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5,7-dihydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5,7-DHT", "type": "ChemicalEntity"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "drowsiness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "enflurane", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a separate group of mice not subjected to behavioral studies , the same dose of NTG ( n = 3 ) and NTG + NIMO ( n = 3 ) caused mean arterial blood pressure to decrease from 85.9 +/- 3.8 mm Hg sem to 31.6 +/- 0.8 mm Hg sem and from 86.2 +/- 3.7 mm Hg sem to 32.6 +/- 0.2 mm Hg sem , respectively .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}]}

Input:
Sentence: The primary outcome of this study was a composite of severe hypotension ( mean arterial pressure < 60 mm Hg ) and bradycardia ( heart rate < 50 beats/min ) during sedative infusion .

## Item biored:test:765
Example input:
Sentence: ZnSO ( 4 ) pretreatment counteracted BCNU-induced inhibition of GR and depletion of GSH and resulted in significant reduction in the levels of MDA and TNFalpha as well as the activity of caspase-3 .

Example answer:
{"entities": [{"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Meanwhile , Co-IP results demonstrated that Hsp90beta could interact with and stabilize TAK1 , AMPKalpha , IKKalpha/beta , HIF-1alpha and Raptor , whereas Hsp90beta inhibition disrupted this process .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "TAK1", "type": "GeneOrGeneProduct"}, {"text": "AMPKalpha", "type": "GeneOrGeneProduct"}, {"text": "IKKalpha/beta", "type": "GeneOrGeneProduct"}, {"text": "HIF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "Raptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , apoptotic proteins are also involved in the desminopathies , like bax , ATF2 , but not bcl-2 , bcl-xl or HK2 .

Example answer:
{"entities": [{"text": "desminopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of caspases , RIP1 , or RIP3 blocks radiation/TNFa-induced cell death , whereas inhibition of RIP1 blocks TNFa-induced caspase activation , suggesting that caspases and RIP1 act sequentially to mediate the non-compensatory cell death pathways .

Example answer:
{"entities": [{"text": "caspases", "type": "GeneOrGeneProduct"}, {"text": "RIP1", "type": "GeneOrGeneProduct"}, {"text": "RIP3", "type": "GeneOrGeneProduct"}, {"text": "TNFa-induced", "type": "GeneOrGeneProduct"}, {"text": "caspase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , by regulating the expression of BIK ( BCL2-interacting killer ) , Star-PAP induced apoptosis of breast cancer cells through the mitochondrial pathway .

Example answer:
{"entities": [{"text": "BIK", "type": "GeneOrGeneProduct"}, {"text": "BCL2-interacting killer", "type": "GeneOrGeneProduct"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: NNK also upregulated the anti-apoptotic BCL2 ( Het-1A ) and downregulated the pro-apoptotic TNF ( Het-1A ) , BAX and CASP8 ( BEP2D ) , all of which could be abolished , in part , by rSLURP-1 .

## Item biored:test:821
Example input:
Sentence: CONCLUSION : Our results suggest that use of high-dose TXA in older patients in conjunction with cardiopulmonary bypass and open-chamber cardiac surgery is associated with clinical seizures in susceptible patients .

Example answer:
{"entities": [{"text": "TXA", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Eighty-seven percent of the patients had received immunomodulatory drugs included in some line of therapy before bort-dex .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Bort-dex was an effective salvage treatment for MM patients , particularly for those in first relapse .

Example answer:
{"entities": [{"text": "Bort-dex", "type": "ChemicalEntity"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Bortezomib and dexamethasone as salvage therapy in patients with relapsed/refractory multiple myeloma : analysis of long-term clinical outcomes .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Bortezomib ( bort ) -dexamethasone ( dex ) is an effective therapy for relapsed/refractory ( R/R ) multiple myeloma ( MM ) .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Physicians should recognise the possibility of fatal bacterial infections related to bortezomib plus high-dose dexamethasone in elderly patients , and we believe this case warrants further investigation .

## Item biored:test:871
Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a prevention study , rats received 4 days of LF treatment followed by Dex and continued during the test period .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Four animal groups ( n = 6 ) were tested during 9 weeks : control , CsA , SRL , and conversion ( CsA for 3 weeks followed by SRL for 6 weeks ) .

Example answer:
{"entities": [{"text": "CsA", "type": "ChemicalEntity"}, {"text": "SRL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Forty-five minutes later , the animals were randomly treated with PCC ( 100 U/kg ) or saline i.v .

Example answer:
{"entities": [{"text": "PCC", "type": "ChemicalEntity"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Input:
Sentence: Animals were also treated with lithium for 6 weeks .

## Item biored:test:870
Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Using Western blot analysis and RT-PCR , we have demonstrated that TD induces HIF-1a expression and activity in primary mouse astrocytes .

Example answer:
{"entities": [{"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : We found that the presence of the -1021T allele was associated with AD : odds ratio = 1.2 ( 95 % confidence interval : 1.06-1.4 , p = 0.005 ) .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , the -1021T allele with presumed low activity may be associated with misregulation of inflammation , which could contribute to the onset of AD .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we establish the unilateral ureteric obstruction ( UUO ) or folic acid ( FA ) -induced mice renal interstitial fibrosis in vivo and the transforming growth factor ( TGF ) -beta1-stimulated human proximal tubular epithelial cell ( HK-2 ) model in vitro .

Example answer:
{"entities": [{"text": "unilateral ureteric obstruction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "UUO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "folic acid", "type": "ChemicalEntity"}, {"text": "FA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor ( TGF )", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: RESULTS : We found that sorted SUM159PT cell populations with high ADAM12 levels had elevated expression of CSC markers and an increased ability to form mammospheres .

Example answer:
{"entities": [{"text": "SUM159PT", "type": "CellLine"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study highlights the importance of the 5 ' untranslated region ( UTR ) in identification of genes of human disease , suggests that a single-nucleotide substitution in the 5 ' UTR could be associated with protein aggregation , and indicates that the GEF protein is associated with cerebellar degeneration in humans .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "GEF", "type": "GeneOrGeneProduct"}, {"text": "cerebellar degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , SNP1 of UP Ia gene affecting a C to T conversion and an Ala7Val change , and SNP7 of UP III affecting a C to G conversion and a Pro154Ala change , were marginally associated with VUR ( both P= 0.08 ) .

Example answer:
{"entities": [{"text": "UP Ia", "type": "GeneOrGeneProduct"}, {"text": "C to T", "type": "SequenceVariant"}, {"text": "Ala7Val", "type": "SequenceVariant"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "C to G", "type": "SequenceVariant"}, {"text": "Pro154Ala", "type": "SequenceVariant"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Similar results were observed with UT-A1 expression .

## Item biored:test:766
Example input:
Sentence: In the functional aspect , overexpression of FLNBv4 led to upregulation of RANKL , OCN , OPG and RUNX2 , which are closely related to GCT cell survival and differentiation .

Example answer:
{"entities": [{"text": "FLNBv4", "type": "GeneOrGeneProduct"}, {"text": "RANKL", "type": "GeneOrGeneProduct"}, {"text": "OCN", "type": "GeneOrGeneProduct"}, {"text": "OPG", "type": "GeneOrGeneProduct"}, {"text": "RUNX2", "type": "GeneOrGeneProduct"}, {"text": "GCT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CD133 ( + ) ACC cells produced activated NOTCH1 ( N1ICD ) and generated CD133 ( - ) cells that expressed JAG1 as well as neural differentiation factors NR2F1 , NR2F2 , and p27Kip1 .

Example answer:
{"entities": [{"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "N1ICD", "type": "GeneOrGeneProduct"}, {"text": "JAG1", "type": "GeneOrGeneProduct"}, {"text": "NR2F1", "type": "GeneOrGeneProduct"}, {"text": "NR2F2", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have shown that MPNSTs express neuregulin-1 ( NRG-1 ) beta isoforms , which promote Schwann cell migration during development , and NRG-1 alpha isoforms , whose effects on Schwann cells are poorly understood .

Example answer:
{"entities": [{"text": "MPNSTs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuregulin-1 ( NRG-1 ) beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gankyrin deficiency in non-parenchymal cells , but not in parenchymal cells , reduced STAT3 activity , interleukin ( IL ) -6 production , and cancer stem cell marker ( Bmi1 and epithelial cell adhesion molecule [ EpCAM ] ) expression , leading to attenuated tumorigenic potential .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "interleukin ( IL ) -6", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bmi1", "type": "GeneOrGeneProduct"}, {"text": "epithelial cell adhesion molecule", "type": "GeneOrGeneProduct"}, {"text": "EpCAM", "type": "GeneOrGeneProduct"}, {"text": "tumorigenic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: b-Catenin is a critical component of canonical Wnt signaling and is essential for the regulation of cell differentiation and morphogenesis during embryogenesis .

Example answer:
{"entities": [{"text": "b-Catenin", "type": "GeneOrGeneProduct"}, {"text": "Wnt", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: NNK decreased expression of the CTNNB1 gene encoding the intercellular adhesion molecule beta-catenin ( BEP2D ) , as well as tumor suppressors CDKN3 and FOXD3 in BEP2D cells and SERPINB5 in Het-1A cells .

## Item biored:test:803
Example input:
Sentence: Although treatment with the pancreatic b-cell toxin streptozotocin induced hyperglycemia and raised plasma ghrelin levels in wild-type mice , hyperglycemia was averted in similarly treated Gcgr ( -/- ) mice and the plasma ghrelin level was further increased .

Example answer:
{"entities": [{"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "hyperglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Male CD-1 mice were treated with warfarin ( 2 mg/kg over 24 h ) , resulting in a mean ( +/-s.d . )

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Contrary to Escherichia coli ( E. coli ) LPS , LPS from Spirulina has low toxicity and barely induces in vivo production of IL-6 and IL-23 in mice .

Example answer:
{"entities": [{"text": "Escherichia coli", "type": "OrganismTaxon"}, {"text": "E. coli", "type": "OrganismTaxon"}, {"text": "LPS", "type": "ChemicalEntity"}, {"text": "Spirulina", "type": "OrganismTaxon"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IL-23", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Administration of Spirulina LPS suppressed tumor growth in C3H/HeN mice , but not in Toll-like receptor 4 ( TLR4 ) -mutant C3H/HeJ mice , by reducing serum levels of IL-17 and IL-23 , while increasing interferon ( IFN ) -g levels .

Example answer:
{"entities": [{"text": "Spirulina", "type": "OrganismTaxon"}, {"text": "LPS", "type": "ChemicalEntity"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Toll-like receptor 4", "type": "GeneOrGeneProduct"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-23", "type": "GeneOrGeneProduct"}, {"text": "interferon ( IFN ) -g", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Of note , injection of anti-IL-17 antibody in tumor-bearing C3H/HeN mice in the absence of Spirulina LPS markedly suppressed tumor growth and augmented IFN-g responses .

Example answer:
{"entities": [{"text": "tumor-bearing", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Spirulina", "type": "OrganismTaxon"}, {"text": "LPS", "type": "ChemicalEntity"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IFN-g", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tumors implanted in LKB1 ( endo-/- ) mice but not macrophage-specific LKB1-knockout mice grew faster and showed enhanced vascular permeability and increased angiogenesis as compared with those implanted in wild-type mice .

Example answer:
{"entities": [{"text": "Tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "LKB1-knockout", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse model of BLM-induced PF was established , and Bach1 siRNA ( 1x109 pfu ) was administered to the mice via the tail vein .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "BLM-induced", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: The mice were injected intraperitoneally with lipopolysaccharide ( LPS ) and D-galactosamine ( D-GalN ) .

## Item biored:test:838
Example input:
Sentence: The ethanolic extract of Daucus carota seeds ( DCE ) was administered orally in three doses ( 100 , 200 , 400 mg/kg ) for seven successive days to different groups of young and aged mice .

Example answer:
{"entities": [{"text": "extract of Daucus carota seeds", "type": "ChemicalEntity"}, {"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Administration of graded doses of U-II ( 1-10,000 ng/mouse ) provoked : ( 1 ) a dose-dependent reduction in the number of head dips in the hole-board test ; ( 2 ) a dose-dependent reduction in the number of entries in the white chamber in the black-and-white compartment test , and in the number of entries in the central platform and open arms in the plus-maze test ; and ( 3 ) a dose-dependent increase in the duration of immobility in the forced-swimming test and tail suspension test .

Example answer:
{"entities": [{"text": "U-II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The extent of inhibition of brain cholinesterase activity evoked by DCE at the dose of 400 mg/kg was 22 % in young and 19 % in aged mice .

Example answer:
{"entities": [{"text": "cholinesterase", "type": "GeneOrGeneProduct"}, {"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition , we demonstrate that mice genetically engineered to have unilateral brain DA deficits develop METH-induced dopaminergic deficits that are of comparable magnitude on both sides of the brain .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "dopaminergic deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male CD-1 mice were treated with warfarin ( 2 mg/kg over 24 h ) , resulting in a mean ( +/-s.d . )

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ninety-six Swiss-Webster mice ( 30-35 g , 6-8 wk ) , were randomized into 6 groups 1 ) saline ( control ) , 2 ) NTG immediately after learning , 3 ) NTG 3 h after learning , 4 ) NTG and NIMO , 5 ) vehicle , and 6 ) NIMO alone .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Input:
Sentence: METHODS : Seventy Swiss albino female mice ( 25-35 g ) were divided into 4 groups : amphetamine-free ( control ) , amphetamine , 50 , and 100 mg/kg DHEA .

## Item biored:test:740
Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: No association was found between PAI-1 serum levels or 4G/5G genotype with liver fibrosis in obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In particular , subjects with stage IV had a two times higher probability of having either IL1B-31TT ( or IL1B-511CC ) genotype compared with stage I subjects .

Example answer:
{"entities": [{"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Serum levels of lipid are associated with the response to pegylated interferon plus ribavirin ( PEG-IFN/RBV ) therapy , while single nucleotide polymorphisms ( SNPs ) around the human interleukin 28B ( IL28B ) gene locus and amino acid substitutions in the core region of the HCV have been reported to affect the efficacy of PEG-IFN/RBV therapy in chronic hepatitis with HCV genotype 1b infection .

## Item biored:test:800
Example input:
Sentence: To address the potential confounding effects of the cannabis use of the ecstasy using group , a second analysis included 14 previously tested cannabis users ( Nestor , L. , Roberts , G. , Garavan , H. , Hester , R. , 2008 .

Example answer:
{"entities": [{"text": "cannabis", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Memory function and serotonin transporter promoter gene polymorphism in ecstasy ( MDMA ) users .

Example answer:
{"entities": [{"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

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

Input:
Sentence: CONCLUSIONS : Given this record of impaired memory and clinically significant levels of depression , impulsiveness , and sleep disturbance , the prognosis for the current generation of ecstasy users is a major cause for concern .

## Item biored:test:797
Example input:
Sentence: The latter two deficits remained significant after controlling for other drug use .

Example answer:
{"entities": []}

Example input:
Sentence: Fifteen moderate MDMA users ( < 55 lifetime tablets ) , 22 heavy MDMA+ users ( > 55 lifetime tablets ) , 16 ex-MDMA+ users ( last tablet > 1 year ago ) and 13 controls were compared on a battery of neuropsychological tests .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "MDMA+", "type": "ChemicalEntity"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of the study was to investigate the effects of moderate and heavy MDMA use on cognitive function , as well as the effects of long-term abstention from MDMA , in subjects genotyped for 5-HTTLPR .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "impaired social and emotional judgement processes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Compared with MDMA-free polydrug controls , MDMA polydrug users showed impairments in set shifting and memory updating , and also in social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA-free", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Heavy and ex-MDMA+ users performed significantly poorer on memory tasks than controls .

Example answer:
{"entities": []}

Input:
Sentence: RESULTS : While the CAN and PD groups tended to record greater deficits than the non-drug controls , the MDMA and EX-MDMA groups recorded greater deficits than all the control groups on ten of the 13 psychometric measures .

## Item biored:test:835
Example input:
Sentence: The incidence of discontinuations for hypertension-related and oedema-related AEs were significantly higher with etoricoxib ( 2.5 % and 1.1 % respectively ) compared with diclofenac ( 1.5 % and 0.4 % respectively ; p < 0.001 for hypertension and p < 0.01 for oedema ) .

Example answer:
{"entities": [{"text": "hypertension-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oedema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prehospital care providers who are managing any patient with a syncopal episode that fails to recover within a reasonable time frame should consider the Bezold-Jarisch reflex as the cause and manage the patient accordingly .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "syncopal episode", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : In this study population , combination therapies with VAL/HCTZ were associated with significantly greater BP reductions compared with either monotherapy , were well tolerated , and were associated with less hypokalemia than HCTZ alone .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "enflurane", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "drowsiness", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Providers should similarly consider the likelihood of hypotension or bradycardia before starting either sedative .

## Item biored:test:844
Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Maximal contraction to norepinephrine was modestly reduced in arteries from LNNA compared with control rats whereas the maximum contraction to ET-1 was significantly reduced ( 54 % control ) .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Our results indicate that trazodone at 2.5-20 mg/kg does not block pre- and postsynaptic striatal D2 DA receptors , while at 30 , 40 and 50 mg/kg it blocks postsynaptic striatal D2 DA receptors .

Example answer:
{"entities": [{"text": "D2 DA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In spontaneously hypertensive , stroke-prone rats , microinjection of methyldopa into the area of the midline B3 serotonin cell group in the ventral medulla caused a potent hypotension of 30-40 mm Hg , which was maximal 2-3 h after administration and was abolished by the serotonin neurotoxin 5,7-dihydroxytryptamine ( 5,7-DHT ) injected intracerebroventricularly .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke-prone", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5,7-dihydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5,7-DHT", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Both DHEA 50 mg/kg ( p < 0.05 ) , and 100 mg/kg ( p < 0.01 ) significantly decreased all movements compared with the amphetamine-induced locomotion group .

## Item biored:test:848
Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "extrapyramidal symptoms", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore , DCE may prove to be a useful remedy for the management of cognitive dysfunctions on account of its multifarious beneficial effects such as , memory improving property , cholesterol lowering property and anticholinesterase activity .

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "cognitive dysfunctions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Efficacy and safety of asenapine in a placebo- and haloperidol-controlled trial in patients with acute exacerbation of schizophrenia .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol-controlled", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Asenapine is approved by the Food and Drugs Administration in adults for acute treatment of schizophrenia or of manic or mixed episodes associated with bipolar I disorder with or without psychotic features .

Example answer:
{"entities": [{"text": "Asenapine", "type": "ChemicalEntity"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "manic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar I disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "psychotic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : While the incidence of new-onset diabetes mellitus may be increasing in patients with schizophrenia treated with certain atypical antipsychotic agents , it remains unclear whether atypical agents are directly affecting glucose metabolism or simply increasing known risk factors for diabetes .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antipsychotic agents", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thirty-six nonobese subjects with schizophrenia or schizoaffective disorder , matched by body mass index and treated with either clozapine , olanzapine , or risperidone , were included in the analysis .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "schizoaffective disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Glucose metabolism in patients with schizophrenia treated with atypical antipsychotic agents : a frequently sampled intravenous glucose tolerance test and minimal model analysis .

Example answer:
{"entities": [{"text": "Glucose", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antipsychotic agents", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Input:
Sentence: We suggest that DHEA displays typical neuroleptic-like effects , and may be used in the treatment of schizophrenia .

## Item biored:test:859
Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In TIPE2 over-expression cells , caspase-3 , caspase-9 , and Bax were significantly up-regulated while Bcl-2 was down-regulated .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "caspase-9", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used rat pancreatic acini to explore the ability of GI-hormones/neurotransmitters/growth-factors to activate Group-I-PAKs and the signaling cascades involved .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "Group-I-PAKs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A major disease-causing gene for HypoPP has been identified as CACNA1S , which encodes the skeletal muscle calcium channel alpha-subunit with four transmembrane domains ( I-IV ) , each with six transmembrane segments ( S1-S6 ) .

Example answer:
{"entities": [{"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "skeletal muscle calcium channel alpha-subunit", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Overload increased GLUT1 , GLUT3 , GLUT6 , and GLUT10 protein levels twofold to fivefold .

Example answer:
{"entities": [{"text": "GLUT1", "type": "GeneOrGeneProduct"}, {"text": "GLUT3", "type": "GeneOrGeneProduct"}, {"text": "GLUT6", "type": "GeneOrGeneProduct"}, {"text": "GLUT10", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Importantly , this is the first experimental evidence that removal of CB from amyloid precursor protein/presenilin transgenic mice aggravates AD pathogenesis , suggesting that CB has a critical role in AD pathogenesis .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "amyloid precursor", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Calbindin-D28k ( CB ) , one of the major calcium-binding and buffering proteins , has a critical role in preventing a neuronal death as well as maintaining calcium homeostasis .

Example answer:
{"entities": [{"text": "Calbindin-D28k", "type": "GeneOrGeneProduct"}, {"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "neuronal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: The expression analysis of Ca ( 2+ ) handling proteins demonstrated that aconitine promoted Ca ( 2+ ) overload through the expression regulation of Ca ( 2+ ) handling proteins .

## Item biored:test:816
Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 61-year-old Japanese man with nephrotic syndrome due to focal segmental glomerulosclerosis was initially responding well to steroid therapy .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal segmental glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: We herein report the case of a 70-year-old man with 5-FU-induced cardiotoxicity , in whom a high serum level of alpha-fluoro-beta-alanine ( FBAL ) was observed .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "5-FU-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fluoro-beta-alanine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Bort-dex was an effective salvage treatment for MM patients , particularly for those in first relapse .

Example answer:
{"entities": [{"text": "Bort-dex", "type": "ChemicalEntity"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Bortezomib ( bort ) -dexamethasone ( dex ) is an effective therapy for relapsed/refractory ( R/R ) multiple myeloma ( MM ) .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Bortezomib and dexamethasone as salvage therapy in patients with relapsed/refractory multiple myeloma : analysis of long-term clinical outcomes .

Example answer:
{"entities": [{"text": "Bortezomib", "type": "ChemicalEntity"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple myeloma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Necrotising fasciitis after bortezomib and dexamethasone-containing regimen in an elderly patient of Waldenstrom macroglobulinaemia .

## Item biored:test:850
Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The melanocortin agonist melanotan II increased insulin-stimulated AKT phosphorylation in the rat hypothalamus in vivo .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "melanotan II", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : The involvement of water-soluble carotenoids , crocins , as the main and active components of Crocus sativus L. extract in learning and memory processes has been proposed .

Example answer:
{"entities": [{"text": "carotenoids", "type": "ChemicalEntity"}, {"text": "crocins", "type": "ChemicalEntity"}, {"text": "Crocus sativus L. extract", "type": "ChemicalEntity"}]}

Example input:
Sentence: ( Anacardiaceae ) , on isoproterenol ( ISPH ) -induced myocardial infarction ( MI ) in rats through its antioxidative mechanism .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "ISPH", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The ethanolic extract of Daucus carota seeds ( DCE ) was administered orally in three doses ( 100 , 200 , 400 mg/kg ) for seven successive days to different groups of young and aged mice .

Example answer:
{"entities": [{"text": "extract of Daucus carota seeds", "type": "ChemicalEntity"}, {"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: It is widely used in folk medicine to treat skin diseases in both humans and animals as well as the seed decoction has been used to treat diarrheas and inflammatory diseases .

Example answer:
{"entities": [{"text": "skin diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "diarrheas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory diseases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Garcinielliptone FC ( GFC ) isolated from hexanic fraction seed extract of species Platonia insignis Mart .

Example answer:
{"entities": [{"text": "Garcinielliptone FC", "type": "ChemicalEntity"}, {"text": "GFC", "type": "ChemicalEntity"}, {"text": "Platonia insignis Mart", "type": "OrganismTaxon"}]}

Example input:
Sentence: These data suggest that pilocarpine produced antiarrhythmic actions on arrhythmic rat and guinea pig models induced by aconitine or ouabain via stimulating the cardiac M ( 3 ) -mAChR .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "M ( 3 ) -mAChR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: [ Ca ( 2+ ) ] ( i ) overload induced by aconitine or ouabain was reduced in isolated myocytes pretreated with pilocarpine .

Example answer:
{"entities": [{"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "aconitine", "type": "ChemicalEntity"}, {"text": "ouabain", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: Aconitine is a major bioactive diterpenoid alkaloid with high content derived from herbal aconitum plants .

## Item biored:test:805
Example input:
Sentence: Oxidative stress was assessed by determining plasma and liver levels of 15-F ( 2t ) -IsoP , lipid hydroperoxides ( LPO ) , and thiobarbituric acid reactive substances ( TBARs ) .

Example answer:
{"entities": [{"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}, {"text": "lipid hydroperoxides", "type": "ChemicalEntity"}, {"text": "LPO", "type": "ChemicalEntity"}, {"text": "thiobarbituric acid reactive substances", "type": "ChemicalEntity"}, {"text": "TBARs", "type": "ChemicalEntity"}]}

Example input:
Sentence: A routine laboratory work-up 10 weeks after conversion revealed elevated serum aminotransferase levels .

Example answer:
{"entities": [{"text": "serum aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Clinicians should be aware of potential hepatotoxicity with simvastatin-ezetimibe especially in elderly patients and should carefully monitor serum aminotransferase levels when starting therapy and titrating the dosage .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin-ezetimibe", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "serum aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: A repeat work-up revealed further elevations in aminotransferase levels , and liver biopsy revealed evidence of moderate-to-severe drug toxicity .

Example answer:
{"entities": [{"text": "aminotransferase", "type": "ChemicalEntity"}, {"text": "drug toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Serum samples were collected from cirrhotic potential liver transplant patients ( LTx ) with ( n=61 ) and without HCC ( n=78 ) as well as from healthy controls ( HCs ; n=39 ) .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Abstract Serum aminotransferase elevations are a commonly known adverse effect of 3-hydroxy-3-methylglutaryl coenzyme A reductase inhibitor ( statin ) therapy .

Example answer:
{"entities": [{"text": "Serum aminotransferase", "type": "ChemicalEntity"}, {"text": "3-hydroxy-3-methylglutaryl coenzyme A reductase", "type": "GeneOrGeneProduct"}, {"text": "statin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Liver toxicity was evaluated based on serum levels of alpha-glutathione S-transferase ( alpha-GST ) and by histology .

Example answer:
{"entities": [{"text": "Liver toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-glutathione S-transferase", "type": "GeneOrGeneProduct"}, {"text": "alpha-GST", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Laboratory tests showed an elevation of creatine phosphokinase ( 2218 IU/L ) , aspartate aminotransferase ( 134 IU/L ) , alanine aminotransferase ( 78 IU/L ) , and BUN ( 27.9 mg/ml ) levels .

Example answer:
{"entities": [{"text": "creatine phosphokinase", "type": "ChemicalEntity"}, {"text": "aspartate aminotransferase", "type": "ChemicalEntity"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Laboratory evaluation revealed 66,680 U/L creatine kinase , 93 mg/dL blood urea nitrogen , 4.6 mg/dL creatinine , 1579 U/L aspartate aminotransferase , and 738 U/L alanine aminotransferase .

Example answer:
{"entities": [{"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "aspartate aminotransferase", "type": "ChemicalEntity"}, {"text": "alanine aminotransferase", "type": "ChemicalEntity"}]}

Input:
Sentence: The Serum liver function parameters including alanine aminotransferase ( ALT ) and aspartate aminotransferase ( AST ) levels were assayed with the commercial kit .

## Item biored:test:787
Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study aimed to explore the effect of MT induction on carmustine ( BCNU ) -induced hippocampal cognitive dysfunction in rats .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "carmustine", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "cognitive dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In 5 mM glucose medium , we observed a stepwise activation of oxidative metabolism during cell differentiation that was characterized by peroxisome proliferator-activated receptor-g coactivator 1a ( PGC-1a ) -dependent stimulation of mitochondrial biogenesis and function , with concomitant reduction of the glycolytic enzyme content .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "peroxisome proliferator-activated receptor-g coactivator 1a", "type": "GeneOrGeneProduct"}, {"text": "PGC-1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "mitochondrial impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , glial activation and neuroinflammation were attenuated in the hippocampi of KCa3.1-/-/APP/PS1 mice , as compared with APP/PS1 mice .

Example answer:
{"entities": [{"text": "neuroinflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCa3.1-/-/APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metallothionein induction reduces caspase-3 activity and TNFalpha levels with preservation of cognitive function and intact hippocampal neurons in carmustine-treated rats .

Example answer:
{"entities": [{"text": "Metallothionein", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "carmustine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This NP1 induction preceded the increased mitochondrial release of cytochrome C ( Cyt C ) into the cytosol , activation of caspase-3 and OGD time-dependent cell death in WT primary hippocampal neurons .

## Item biored:test:842
Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: The tests included open-field exploratory behaviour , elevated plus maze and elevated zero maze , social interaction and novelty-suppressed feeding latency behaviour .

Example answer:
{"entities": []}

Example input:
Sentence: The statistical analysis was performed for the combined G1359A and A1359A as a group and wild type G1359G as second group , with a dominant model .

Example answer:
{"entities": [{"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}, {"text": "G1359G", "type": "SequenceVariant"}]}

Example input:
Sentence: In order to explain the reduced genetic heterogeneity detected by Alu insertions among Basque subpopulations , values of the Wright 's F ( ST ) statistic were estimated for both Alu markers and a set of short tandem repeats ( STRs ) in terms of two geographical scales : ( 1 ) the Basque Country , ( 2 ) Europe ( including Basques ) .

Example answer:
{"entities": []}

Example input:
Sentence: Association and Hardy-Weinberg equilibrium checking were assessed by Chi-square test and Mann-Whitney U test .

Example answer:
{"entities": []}

Example input:
Sentence: Bayesian quantitative trait nucleotide analysis was used to statistically infer the most likely functional polymorphisms .

Example answer:
{"entities": []}

Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As compared with the standard approach of analyzing sequences from each patient independently , the HPM provides more efficient estimation of evolutionary parameters such as nucleotide substitution rates and d ( N ) /d ( S ) rate ratios , as shown by significant shrinkage of the estimator variance .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Chi square , Fisher exact , Mann-Whitney U-tests , ROC curve analysis and forward stepwise logistic regression analyses were applied .

Example answer:
{"entities": []}

Example input:
Sentence: A Kruskal-Wallis 1-way analysis of variance indicated a significant difference among the 4 treatment groups ( H = 15.34 ; P < 0.001 ) .

Example answer:
{"entities": []}

Input:
Sentence: Statistical analysis was carried out using Kruskal-Wallis test for hyper locomotion , and one-way ANOVA for climbing and catalepsy tests .

## Item biored:test:788
Example input:
Sentence: Voltage-Dependent Anion Channel 1 ( VDAC1 ) Participates the Apoptosis of the Mitochondrial Dysfunction in Desminopathy .

Example answer:
{"entities": [{"text": "Voltage-Dependent Anion Channel 1", "type": "GeneOrGeneProduct"}, {"text": "VDAC1", "type": "GeneOrGeneProduct"}, {"text": "Mitochondrial Dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Desminopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Live imaging of Tuba1a-mutant neurons revealed slowed migration and increased neuronal branching , which correlated with directionality alterations and perturbed nucleus-centrosome ( N-C ) coupling .

Example answer:
{"entities": [{"text": "Tuba1a-mutant", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These biochemical lesions result in apoptotic cell death in both neurons and astrocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Brain-derived neurotrophic factor significantly inhibited Dox-induced cardiomyocyte apoptosis , oxidative stress and cardiac dysfunction in rats .

Example answer:
{"entities": [{"text": "cardiac", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , memory deficits and neuronal loss in APP/PS1 mice were reversed in KCa3.1-/-/APP/PS1 mice .

Example answer:
{"entities": [{"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "KCa3.1-/-/APP/PS1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "mitochondrial impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Overall , these results suggest that KCa3.1 is involved in the regulation of Ca2+ homeostasis in astrocytes and attenuation of the UPR and ER stress , thus contributing to memory deficits and neuronal loss .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In contrast , in NP1-KO neurons there was no translocation of Bad and Bax from cytosol to the mitochondria , and no evidence of D ( m ) loss , increased Cyt C release and caspase-3 activation following OGD ; which resulted in significantly reduced neuronal death .
