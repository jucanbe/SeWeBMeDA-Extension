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

## Item biored:test:285
Example input:
Sentence: Maximal contraction to norepinephrine was modestly reduced in arteries from LNNA compared with control rats whereas the maximum contraction to ET-1 was significantly reduced ( 54 % control ) .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The mutant receptor hGRalphaD401H did not exert a dominant positive or negative effect upon the wild-type receptor , it preserved its ability to bind to glucocorticoid response elements , and displayed a normal interaction with the glucocorticoid receptor-interacting protein 1 coactivator .

Example answer:
{"entities": [{"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "glucocorticoid receptor-interacting protein 1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The cause appears to be the Bezold-Jarish reflex , stimulation of the ventricular walls which in turn decreases sympathetic outflow from the vasomotor centre .

Example answer:
{"entities": []}

Example input:
Sentence: Notably , administration of a ghrelin receptor antagonist further reduced blood glucose levels into the markedly hypoglycemic range in overnight-fasted , streptozotocin-treated Gcgr ( -/- ) mice .

Example answer:
{"entities": [{"text": "ghrelin receptor", "type": "GeneOrGeneProduct"}, {"text": "blood glucose", "type": "ChemicalEntity"}, {"text": "streptozotocin-treated", "type": "ChemicalEntity"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : The mutant receptor hGRalphaD401H enhances the transcriptional activity of glucocorticoid-responsive genes .

Example answer:
{"entities": [{"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid-responsive genes", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have recently shown that estrogen negatively modulates the hypotensive effect of clonidine ( mixed alpha2-/I1-receptor agonist ) in female rats and implicates the cardiovascular autonomic control in this interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}, {"text": "alpha2-/I1-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings suggest that estrogen downregulates alpha2- but not I1-receptor-mediated hypotension and highlight a role for the cardiac autonomic control in alpha-methyldopa-estrogen interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "alpha2- but not", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-methyldopa-estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: The beta-adrenergic receptors ( beta-AR ) are G protein-coupled receptors activated by epinephrine and norepinephrine and are involved in a variety of their physiological functions .

Example answer:
{"entities": [{"text": "beta-adrenergic receptors", "type": "GeneOrGeneProduct"}, {"text": "beta-AR", "type": "GeneOrGeneProduct"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "norepinephrine", "type": "ChemicalEntity"}]}

Input:
Sentence: These results indicate that TGR are more sensitive to beta-AR agonist-induced cardiac inotropic response and hypertrophy , possibly due to chronically low sympathetic outflow directed to the heart .

## Item biored:test:276
Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , antithrombin treatment markedly suppressed puromycin aminonucleoside-induced apoptosis of renal tubular epithelial cells .

Example answer:
{"entities": [{"text": "antithrombin", "type": "ChemicalEntity"}, {"text": "puromycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An experimental group of rats was treated with puromycin aminonucleoside ( PAN ; 180 mg/kg iv ) , whereas the control group received only vehicle .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "puromycin aminonucleoside", "type": "ChemicalEntity"}, {"text": "PAN", "type": "ChemicalEntity"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using a mouse model , we tested whether the rapid reversal of anticoagulation using human prothrombin complex concentrate ( PCC ) can reduce hemorrhagic blood volume .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "prothrombin complex concentrate", "type": "ChemicalEntity"}, {"text": "PCC", "type": "ChemicalEntity"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Input:
Sentence: Viramidine , a liver-targeting prodrug of ribavirin , has the potential to maintain the virologic efficacy of ribavirin while decreasing the risk of hemolytic anemia in patients with chronic hepatitis C .

## Item biored:test:320
Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: In the original MB-DRM German family , we demonstrated a linkage of the disease to the SEPN1 locus ( 1p36 ) , and subsequently a homozygous SEPN1 deletion ( del 92 nucleotide -19/+73 ) in the affected patients .

Example answer:
{"entities": [{"text": "SEPN1", "type": "GeneOrGeneProduct"}, {"text": "del 92 nucleotide -19/+73", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In 10 of these families , all the homozygotes have a 137-bp insertion in their cDNA caused by a point mutation in a sequence resembling a splice-donor site .

Example answer:
{"entities": [{"text": "137-bp insertion", "type": "SequenceVariant"}]}

Example input:
Sentence: Her mother was heterozygous for the Asn45Ser mutation , and her father , for the nine-nucleotide deletion .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}]}

Input:
Sentence: RESULTS : Two affected siblings in one family were homozygous for a 101-bp deletion in intron 9 .

## Item biored:test:294
Example input:
Sentence: We describe a novel germline mutation of BMPR1A in a family with juvenile polyposis and colon cancer .

Example answer:
{"entities": [{"text": "BMPR1A", "type": "GeneOrGeneProduct"}, {"text": "juvenile polyposis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study aimed to identify mutations in a Chinese pedigree with MEN1 .

Example answer:
{"entities": [{"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel variant ( K294E ) was identified in a single heterozygous individual with prostate cancer .

Example answer:
{"entities": [{"text": "K294E", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutation analysis in a Chinese family with multiple endocrine neoplasia type 1 .

Example answer:
{"entities": [{"text": "multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutation in exon 10 of MEN1 gene might induce development of parathyroid hyperplasia and pituitary adenoma and cosegregate with MEN1 syndrome .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}, {"text": "parathyroid hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1 syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Multiple endocrine neoplasia type 1 ( MEN1 ) is an autosomal dominant cancer syndrome which is caused by germline mutations of the tumor suppressor gene MEN1 .

Example answer:
{"entities": [{"text": "Multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Two novel mutations in the MEN1 gene in subjects with multiple endocrine neoplasia-1 .

## Item biored:test:318
Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ApoE gene analysis showed a nucleotide substitution of G to C at codon 158 of exon 4 .

Example answer:
{"entities": [{"text": "ApoE", "type": "GeneOrGeneProduct"}, {"text": "G to C at codon 158", "type": "SequenceVariant"}]}

Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: DNA was isolated from peripheral leukocytes and the region of interest in the AGT gene bearing a missense mutation methionine to threonine substitution at codon 235 ( M235T ) of exon 2 , was amplified by polymerase chain reaction ( PCR ) .

Example answer:
{"entities": [{"text": "AGT", "type": "GeneOrGeneProduct"}, {"text": "methionine to threonine substitution at codon 235", "type": "SequenceVariant"}, {"text": "M235T", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation was linked to a novel single nucleotide polymorphism ( SNP ) in intron 3 ( IVS3 + 18C > T ) .

Example answer:
{"entities": [{"text": "IVS3 + 18C > T", "type": "SequenceVariant"}]}

Input:
Sentence: DESIGN AND SETTING : Mutation analysis of exons and adjacent introns in the SLC34A3 gene was conducted at an academic research laboratory and medical center .

## Item biored:test:296
Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutation analysis in a Chinese family with multiple endocrine neoplasia type 1 .

Example answer:
{"entities": [{"text": "multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We screened one family with nonsyndromic oligodontia for mutations in PAX9 and MSX1 .

Example answer:
{"entities": [{"text": "nonsyndromic oligodontia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}, {"text": "MSX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We identified 10 new families segregating DFNB7/B11 deafness and TMC1 mutations , including three novel alleles .

Example answer:
{"entities": [{"text": "DFNB7/B11 deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All of the coded regions and their adjacent sequences of the MEN1 gene were amplified and sequenced .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study aimed to identify mutations in a Chinese pedigree with MEN1 .

Example answer:
{"entities": [{"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutation in exon 10 of MEN1 gene might induce development of parathyroid hyperplasia and pituitary adenoma and cosegregate with MEN1 syndrome .

Example answer:
{"entities": [{"text": "MEN1", "type": "GeneOrGeneProduct"}, {"text": "parathyroid hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1 syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Multiple endocrine neoplasia type 1 ( MEN1 ) is an autosomal dominant cancer syndrome which is caused by germline mutations of the tumor suppressor gene MEN1 .

Example answer:
{"entities": [{"text": "Multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We describe 2 families with MEN1 with novel mutations in the MEN1 gene .

## Item biored:test:286
Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: We studied the role of xanthine oxidase ( XO ) , which is implicated in the production of reactive oxygen species , in dexamethasone-induced hypertension ( dex-HT ) .

Example answer:
{"entities": [{"text": "xanthine oxidase", "type": "ChemicalEntity"}, {"text": "XO", "type": "ChemicalEntity"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dex-HT", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone- ( Dex- ) induced hypertension is associated with enhanced oxidative stress .

Example answer:
{"entities": [{"text": "Dexamethasone-", "type": "ChemicalEntity"}, {"text": "Dex-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : The aim of the study was to investigate the antihypertensive effects of angiotensin II type-1 receptor blocker , losartan , and its potential in slowing down renal disease progression in spontaneously hypertensive rats ( SHR ) with adriamycin ( ADR ) nephropathy .

Example answer:
{"entities": [{"text": "angiotensin II type-1 receptor", "type": "GeneOrGeneProduct"}, {"text": "losartan", "type": "ChemicalEntity"}, {"text": "renal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "adriamycin", "type": "ChemicalEntity"}, {"text": "ADR", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Glucocorticoid-induced hypertension ( GC-HT ) in the rat is associated with nitric oxide-redox imbalance .

Example answer:
{"entities": [{"text": "Glucocorticoid-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GC-HT", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "nitric", "type": "ChemicalEntity"}]}

Example input:
Sentence: Role of xanthine oxidase in dexamethasone-induced hypertension in rats .

Example answer:
{"entities": [{"text": "xanthine oxidase", "type": "ChemicalEntity"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Anti-oxidant effects of atorvastatin in dexamethasone-induced hypertension in the rat .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Input:
Sentence: Atorvastatin prevented and reversed dexamethasone-induced hypertension in the rat .

## Item biored:test:321
Example input:
Sentence: The phenotype co-segregates with short-tandem repeat markers flanking the TMC1 gene at the DFNA36 locus on chromosome 9q31-q21 .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These findings suggest that 521T > C , existing commonly in SLCO1B1 * 5 , * 15 and * 15+C1007G , is the key single nucleotide polymorphism ( SNP ) that determines the functional properties of SLCO1B1 * 5 , * 15 and * 15+C1007G allelic proteins and that decreased activities of these variant proteins are mainly caused by a sorting error produced by this SNP .

Example answer:
{"entities": [{"text": "521T > C", "type": "SequenceVariant"}, {"text": "SLCO1B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotype analysis of p.R34X-linked markers indicates that it arose from a common founder .

Example answer:
{"entities": [{"text": "p.R34X-linked", "type": "SequenceVariant"}]}

Example input:
Sentence: Haplotype reconstruction via the expectation-maximization algorithm showed in both populations that only the haplotype containing the minor ( W ) allele at codon 620 was associated with T1D ( OR=2.26 , 95 % CI 1.68-3.02 in Czechs , OR=14.8 , 95 % CI 2.0-651 in Azeri ) or JIA ( OR=2.43 , 95 % CI 1.66-3.56 in Czechs ) .

Example answer:
{"entities": [{"text": "( W ) allele at codon 620", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Distinct patterns of germ-line deletions in MLH1 and MSH2 : the implication of Alu repetitive element in the genetic etiology of Lynch syndrome ( HNPCC ) .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The D487_S488_F489 deletion had been identified in two previously genotyped Chinese families .

Example answer:
{"entities": [{"text": "D487_S488_F489 deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Input:
Sentence: Haplotype analysis of the SLC34A3 locus in the family showed that the two deletions are on different haplotypes .

## Item biored:test:323
Example input:
Sentence: This mutation leads to the activation of a cryptic splice site , 32 bp downstream of the mutation site and to subsequent aberrant out-of-frame splicing , resulting in two alternative mRNA transcripts and a downstream PTC .

Example answer:
{"entities": []}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation was linked to a novel single nucleotide polymorphism ( SNP ) in intron 3 ( IVS3 + 18C > T ) .

Example answer:
{"entities": [{"text": "IVS3 + 18C > T", "type": "SequenceVariant"}]}

Example input:
Sentence: Three aberrantly spliced cDNA species were identified : exon 22 and exon 22 to 23 skipping , and insertion of an 87-base pair cryptic exon .

Example answer:
{"entities": []}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: the skipping of exon 9 ( p.G204_K247del ) or the retention of introns 8 and 9 ( p.G204VfsX28 ) .

Example answer:
{"entities": [{"text": "p.G204_K247del", "type": "SequenceVariant"}, {"text": "p.G204VfsX28", "type": "SequenceVariant"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Input:
Sentence: The intron 9 deletion ( and likely the other two mutations ) identified in this study causes aberrant RNA splicing .

## Item biored:test:342
Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Two microsatellites , 1 insertion/deletion , and 8 single nucleotide polymorphisms ( SNPs ) in the regulatory region of iNOS were genotyped in 200 POAG patients and 200 age-matched controls .

Example answer:
{"entities": [{"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The search for HbF-associated polymorphisms ( such as the XmnI , BCL11A and MYB polymorphisms ) has recently gained great attention , in order to stratify b-thalassemia patients with respect to expectancy of the first transfusion , need for annual intake of blood , response to HbF inducers ( the most studied of which is hydroxyurea ) .

Example answer:
{"entities": [{"text": "HbF-associated", "type": "GeneOrGeneProduct"}, {"text": "BCL11A", "type": "GeneOrGeneProduct"}, {"text": "MYB", "type": "GeneOrGeneProduct"}, {"text": "b-thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HbF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: This suggests that the TfR2 gene is involved in hemochromatosis in Japanese patients .

Example answer:
{"entities": [{"text": "TfR2", "type": "GeneOrGeneProduct"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : We genotyped eight single nucleotide polymorphisms ( SNPs ) in the three genes , DBH , IL1A and IL6 .

Example answer:
{"entities": [{"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We genotyped candidate single-nucleotide polymorphisms ( SNP ) in IL10 , CRP , GPX1 , GSR , GSTP1 , hOGG1 , IL1B , IL1RN , IL6 , IL8 , MPO , NOS2 , NOS3 , SOD1 , SOD2 , SOD3 , TLR4 , and TNF and tagging SNPs in IL10 , CRP , GSR , IL1RN , IL6 , NOS2 , and NOS3 .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "hOGG1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "IL1RN", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}, {"text": "IL8", "type": "GeneOrGeneProduct"}, {"text": "MPO", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "NOS3", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "SOD3", "type": "GeneOrGeneProduct"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "TNF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The genetic polymorphism rs1052133 , which leads to substitution of the amino acid at codon 326 from Ser to Cys , shows functional differences , namely a decrease in enzyme activity in hOGG1-Cys326 .

Example answer:
{"entities": [{"text": "rs1052133", "type": "SequenceVariant"}, {"text": "326 from Ser to Cys", "type": "SequenceVariant"}, {"text": "hOGG1-Cys326", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : We selected 13 single nucleotide polymorphisms ( SNPs ) and a CGGGG insertion-deletion polymorphism in the IRF5 gene .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Many of these hereditary factors consist of defined gene polymorphisms , such as single nucleotide polymorphisms ( SNPs ) or insertion-deletion polymorphisms , which directly or indirectly affect the hemostatic system .

## Item biored:test:343
Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : We genotyped eight single nucleotide polymorphisms ( SNPs ) in the three genes , DBH , IL1A and IL6 .

Example answer:
{"entities": [{"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Seven single nucleotide polymorphisms from two different haploblocks were genotyped from 507 participants of the Finnish Diabetes Prevention Study ( DPS ) .

Example answer:
{"entities": [{"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The haplotypes having the wild-type ( R ) allele at codon 620 and minor alleles at -1123 and/or +2740 were neutral as to the risk of autoimmune conditions in both populations .

Example answer:
{"entities": [{"text": "( R ) allele at codon 620", "type": "SequenceVariant"}, {"text": "autoimmune conditions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The frequencies of individual hemostatic gene polymorphisms in different normal populations are well defined .

## Item biored:test:326
Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Her mother was heterozygous for the Asn45Ser mutation , and her father , for the nine-nucleotide deletion .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: Haplotype reconstruction via the expectation-maximization algorithm showed in both populations that only the haplotype containing the minor ( W ) allele at codon 620 was associated with T1D ( OR=2.26 , 95 % CI 1.68-3.02 in Czechs , OR=14.8 , 95 % CI 2.0-651 in Azeri ) or JIA ( OR=2.43 , 95 % CI 1.66-3.56 in Czechs ) .

Example answer:
{"entities": [{"text": "( W ) allele at codon 620", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Linkage disequilibrium analysis indicates that D90A homozygotes and heterozygotes share a rare haplotype and are all descended from a single ancient founder ( alpha 0.974 ) c.895 generations ago .

Example answer:
{"entities": [{"text": "D90A", "type": "SequenceVariant"}]}

Example input:
Sentence: the skipping of exon 9 ( p.G204_K247del ) or the retention of introns 8 and 9 ( p.G204VfsX28 ) .

Example answer:
{"entities": [{"text": "p.G204_K247del", "type": "SequenceVariant"}, {"text": "p.G204VfsX28", "type": "SequenceVariant"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: The former constituted two major haplotypes that contained one or two repeats of 13 nucleotides in intron 8 ( designated as * 1 and * 2 , respectively ) .

Example answer:
{"entities": []}

Input:
Sentence: Haplotype analysis suggests that the two intron 9 deletions arose independently .

## Item biored:test:267
Example input:
Sentence: In addition , crocin in the mentioned dose could significantly attenuated learning and memory impairment in treated STZ-injected group in passive avoidance test .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "learning and memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STZ-injected", "type": "ChemicalEntity"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The extent of memory improvement evoked by DCE was 23 % at the dose of 200 mg/kg and 35 % at the dose of 400 mg/kg in young mice using elevated plus maze .

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "ChemicalEntity"}, {"text": "scopolamine-", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , DCE reversed the amnesia induced by scopolamine ( 0.4 mg/kg , i.p . )

Example answer:
{"entities": [{"text": "DCE", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "scopolamine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These results indicate that daidzein might play a role in acetylcholine biosynthesis as a ChAT activator , and that it also ameliorates scopolamine-induced amnesia .

## Item biored:test:327
Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: These included missense ( p.T286M ) and nonsense ( p.W111X ) mutations and a transition in the obligate AG-dinucleotide of the intron 8 acceptor splice site ( c.610-2A > G ) .

Example answer:
{"entities": [{"text": "p.T286M", "type": "SequenceVariant"}, {"text": "p.W111X", "type": "SequenceVariant"}, {"text": "AG-dinucleotide", "type": "SequenceVariant"}, {"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: This mutation was linked to a novel single nucleotide polymorphism ( SNP ) in intron 3 ( IVS3 + 18C > T ) .

Example answer:
{"entities": [{"text": "IVS3 + 18C > T", "type": "SequenceVariant"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The identification of three independent deletions in introns 9 and 10 suggests that the SLC34A3 gene may be susceptible to unequal crossing over because of sequence misalignment during meiosis .

## Item biored:test:353
Example input:
Sentence: Seven distinct mutations were identified ; five of these occurred in two or more families .

Example answer:
{"entities": []}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations were confirmed by screening at least 100 unrelated normal control subjects .

Example answer:
{"entities": []}

Example input:
Sentence: Using PCR-RFLP , we confirmed the heterozygous mutation in six affected family members and excluded it in three healthy members .

Example answer:
{"entities": []}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The missense mutation ( c.920T > G ) was not found in 100 healthy controls and has not been reported previously .

Example answer:
{"entities": [{"text": "c.920T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation , designated p.E300X , was not detected in DNA from either parent or in 100 control chromosomes .

Example answer:
{"entities": [{"text": "p.E300X", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutations were found in 35 ( 53 % ) of the 66 families studied .

Example answer:
{"entities": []}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: In total , recurrent mutations were found in 33 ( 94 % ) of the 35 families with detected mutations .

Example answer:
{"entities": []}

Input:
Sentence: These mutations were not detected in 200 normal chromosomes and cosegregated within the family .

## Item biored:test:297
Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS : The five patients derived from four families living in Shandong Province , China .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: There is currently no known genetic disease linked to prolactin ( Prl ) or its receptor ( PrlR ) in humans .

Example answer:
{"entities": [{"text": "genetic disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prolactin", "type": "GeneOrGeneProduct"}, {"text": "Prl", "type": "GeneOrGeneProduct"}, {"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: OBJECTIVE : To describe clinical and genetic features of a Thai family with non-autoimmune hyperthyroidism ( NAH ) caused by an activating germline mutation in the thyrotropin receptor ( TSHR ) gene .

Example answer:
{"entities": [{"text": "non-autoimmune hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thyrotropin receptor", "type": "GeneOrGeneProduct"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition to hyperthyroidism , ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers were consistently found in all affected individuals .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS : A population-based cohort consisting of 36 apparently sporadic paediatric pituitary adenoma patients , referred to two medical centres in Italy , was included in the study .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Peroxisomal proliferator activated receptor-gamma deficiency in a Canadian kindred with familial partial lipodystrophy type 3 ( FPLD3 ) .

Example answer:
{"entities": [{"text": "Peroxisomal proliferator activated receptor-gamma", "type": "GeneOrGeneProduct"}, {"text": "familial partial lipodystrophy type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: One family was of Turkish origin , and the index patient had primary hyperparathyroidism ( PHPT ) plus a prolactinoma ; three relatives had PHPT only .

## Item biored:test:263
Example input:
Sentence: CONCLUSION : Therefore , these results demonstrate the effectiveness of crocin ( 30 mg/kg ) in antagonizing the cognitive deficits caused by STZ-icv in rats and its potential in the treatment of neurodegenerative diseases such as Alzheimer 's disease .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STZ-icv", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "neurodegenerative diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore , the present study was carried out to investigate the effect of chronic curcumin administration on phenobarbitone- and carbamazepine-induced cognitive impairment and oxidative stress in rats .

Example answer:
{"entities": [{"text": "curcumin", "type": "ChemicalEntity"}, {"text": "phenobarbitone-", "type": "ChemicalEntity"}, {"text": "carbamazepine-induced", "type": "ChemicalEntity"}, {"text": "cognitive impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Curcumin ameliorates cognitive dysfunction and oxidative damage in phenobarbitone and carbamazepine administered rats .

Example answer:
{"entities": [{"text": "Curcumin", "type": "ChemicalEntity"}, {"text": "cognitive dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "impairment of learning and memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was aimed at investigating the effects of Daucus carota seeds on cognitive functions , total serum cholesterol levels and brain cholinesterase activity in mice .

Example answer:
{"entities": [{"text": "Daucus carota", "type": "OrganismTaxon"}, {"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "cholinesterase", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In order to investigate the effects of daidzein from Pueraria thunbergiana on scopolamine-induced impairments of learning and memory , we conducted a series of in vivo tests .

## Item biored:test:319
Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Since the first molecular characterization of an FH mutation by Bourgeron et al in 1994 , a series of reports of both FH deficiency patients and patients with MCUL/HLRRC have described 107 variants , of which 93 are thought to be pathogenic .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "FH deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MCUL/HLRRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : To describe clinical and genetic features of a Thai family with non-autoimmune hyperthyroidism ( NAH ) caused by an activating germline mutation in the thyrotropin receptor ( TSHR ) gene .

Example answer:
{"entities": [{"text": "non-autoimmune hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thyrotropin receptor", "type": "GeneOrGeneProduct"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PATIENTS AND METHODS : Six unrelated families and 10 sporadic patients were examined clinically .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Since healthy relatives of the VUR probands are not reliable negative controls for VUR , we used a population of 90 race-matched , healthy individuals , unrelated to the VUR patients , as controls to perform an association study .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: DESIGN AND METHODS : Nine patients clinically diagnosed with hemochromatosis were included in the study .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS : Three affected individuals from the same family ( a father and his two children ) were studied .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}]}

Input:
Sentence: PATIENTS OR OTHER PARTICIPANTS : Members of two unrelated families with HHRH participated in the study .

## Item biored:test:293
Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: We studied the role of xanthine oxidase ( XO ) , which is implicated in the production of reactive oxygen species , in dexamethasone-induced hypertension ( dex-HT ) .

Example answer:
{"entities": [{"text": "xanthine oxidase", "type": "ChemicalEntity"}, {"text": "XO", "type": "ChemicalEntity"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dex-HT", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : The aim of the study was to investigate the antihypertensive effects of angiotensin II type-1 receptor blocker , losartan , and its potential in slowing down renal disease progression in spontaneously hypertensive rats ( SHR ) with adriamycin ( ADR ) nephropathy .

Example answer:
{"entities": [{"text": "angiotensin II type-1 receptor", "type": "GeneOrGeneProduct"}, {"text": "losartan", "type": "ChemicalEntity"}, {"text": "renal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "adriamycin", "type": "ChemicalEntity"}, {"text": "ADR", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexamethasone- ( Dex- ) induced hypertension is associated with enhanced oxidative stress .

Example answer:
{"entities": [{"text": "Dexamethasone-", "type": "ChemicalEntity"}, {"text": "Dex-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Glucocorticoid-induced hypertension ( GC-HT ) in the rat is associated with nitric oxide-redox imbalance .

Example answer:
{"entities": [{"text": "Glucocorticoid-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GC-HT", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "nitric", "type": "ChemicalEntity"}]}

Example input:
Sentence: Role of xanthine oxidase in dexamethasone-induced hypertension in rats .

Example answer:
{"entities": [{"text": "xanthine oxidase", "type": "ChemicalEntity"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Atorvastatin ( Ato ) possesses pleiotropic properties that have been reported to improve endothelial function through increased availability of NO and reduced O2- production in various forms of hypertension .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "Ato", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Anti-oxidant effects of atorvastatin in dexamethasone-induced hypertension in the rat .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "dexamethasone-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Input:
Sentence: Thus , atorvastatin prevented and reversed dexamethasone-induced hypertension in the rat .

## Item biored:test:313
Example input:
Sentence: The deletion of any of these five genes enhanced the toxicity of alpha-syn as judged by growth defects compared with wild-type cells expressing alpha-syn , which indicates that these genes protect cells from alpha-syn .

Example answer:
{"entities": [{"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ADAM12 knockdown also diminished ALDEFLUOR ( + ) and CD44 ( hi ) /CD24 ( -/lo ) CSC-enriched populations in vitro and reduced tumorigenesis in mice in vivo .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We propose that the alteration in the replication/nuclear location pattern of the non-deleted TDR22 indicates an altered gene regulation hence an altered transcritpion in DGS/VCFS .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Coenzyme Q10 significantly compensated deficits in the antioxidant defense mechanisms ( reduced glutathione level and superoxide dismutase activity ) , suppressed lipid peroxidation , decreased the elevations of tumor necrosis factor-alpha , nitric oxide and platinum ion concentration , and attenuated the reductions of selenium and zinc ions in renal tissue resulted from cisplatin administration .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "nitric oxide", "type": "ChemicalEntity"}, {"text": "platinum", "type": "ChemicalEntity"}, {"text": "selenium", "type": "ChemicalEntity"}, {"text": "zinc", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In both types , purinoceptor desensitization with alpha , beta-methylene adenosine-5'-triphosphate ( alpha , beta-meATP ) caused further reductions at low frequencies ( < 10 Hz ) .

Example answer:
{"entities": [{"text": "alpha , beta-methylene adenosine-5'-triphosphate", "type": "ChemicalEntity"}, {"text": "alpha , beta-meATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These changes were significantly attenuated by alpha-TC and DFO .

## Item biored:test:208
Example input:
Sentence: In addition , Hsp90beta inhibition-mediated renal improvements also accompanied the reduction of renal oxidative stress .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: The results showed that atorvastatin ameliorated the apoptosis and deterioration of renal function ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "apoptosis and deterioration of renal function", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated the effects of antithrombin , a plasma inhibitor of coagulation factors , in rats with puromycin aminonucleoside-induced nephrosis , which is an experimental model of human nephrotic syndrome .

Example answer:
{"entities": [{"text": "antithrombin", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "puromycin", "type": "ChemicalEntity"}, {"text": "nephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results of the present study suggested that atorvastatin protected against contrast-induced renal tubular cell apoptosis through the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced renal tubular cell apoptosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , Sal treatment improves kidney function , ameliorates the deposition of the ECM components and relieves the protein levels of EMT markers in mouse kidneys and HK-2 cells .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The nephroprotective effect of coenzyme Q10 was investigated in mice with acute renal injury induced by a single i.p .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "acute renal injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Vancomycin nephrotoxicity is infrequent but may result from coadministration with a nephrotoxic agent .

Example answer:
{"entities": [{"text": "Vancomycin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nephrotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The aims of this study were to examine vancomycin ( VCM ) -induced oxidative stress that promotes production of reactive oxygen species ( ROS ) and to investigate the role of erdosteine , an expectorant agent , which has also antioxidant properties , on kidney tissue against the possible VCM-induced renal impairment in rats .

## Item biored:test:291
Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone ( Dex ) -induced hypertension is characterized by endothelial dysfunction associated with nitric oxide ( NO ) deficiency and increased superoxide ( O2- ) production .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitric oxide", "type": "ChemicalEntity"}, {"text": "NO", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}, {"text": "O2-", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The superoxide scavenger tempol ( 30 , 100 , and 300 micromol kg ( -1 ) , IV ) did not change arterial pressure in control rats but caused a dose-dependent decrease in LNNA rats ( -18 +/- 8 , -26 +/- 15 , and -54 +/- 11 mm Hg ) .

Example answer:
{"entities": [{"text": "superoxide", "type": "ChemicalEntity"}, {"text": "tempol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "LNNA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Similarly , ganglionic blockade with hexamethonium caused a significantly greater fall in LNNA hypertensive rats ( 76 +/- 9 mm Hg ) compared with control rats ( 35 +/- 10 mm Hg ) .

Example answer:
{"entities": [{"text": "hexamethonium", "type": "ChemicalEntity"}, {"text": "LNNA", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In a separate group of mice not subjected to behavioral studies , the same dose of NTG ( n = 3 ) and NTG + NIMO ( n = 3 ) caused mean arterial blood pressure to decrease from 85.9 +/- 3.8 mm Hg sem to 31.6 +/- 0.8 mm Hg sem and from 86.2 +/- 3.7 mm Hg sem to 32.6 +/- 0.2 mm Hg sem , respectively .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ritanserin-treated rats ( 4 microg/0.5 microl/side ) showed a significant decrease in the mentioned parameters as compared to DMSO-treated group .

Example answer:
{"entities": [{"text": "Ritanserin-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "DMSO-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Input:
Sentence: Plasma nitrate/nitrite ( NOx ) was decreased in dex-treated rats compared to saline-treated rats ( 11.2 +/- 1.08 microm , 15.3 +/- 1.17 microm , respectively , P < 0.05 ) .

## Item biored:test:253
Example input:
Sentence: Our observation of frequent p14 gene abnormalities ( 90 % ) and inactivation ( 40-60 % ) was in striking contrast to the same pathological subtype of systemic lymphoma in which p14 gene abnormalities and inactivation were infrequent , suggesting a difference in carcinogenesis between PCNSL and systemic lymphoma .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}, {"text": "systemic lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: By multipoint linkage analysis with markers spanning the entire X-chromosome we mapped the disease locus to a 28-Mb interval between Xp11.4 and Xq12 , including the BCOR gene .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subsequent mutation analysis of PQBP1 , located within the delineated linkage interval in Xp11.23 , revealed a 2-bp deletion , c.461_462delAG , that cosegregated with the disease .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "c.461_462delAG", "type": "SequenceVariant"}]}

Example input:
Sentence: Ten primary central nervous system lymphomas ( PCNSL , brain lymphomas ) were examined for p14 gene exon 1beta deletion , mutation and methylation by Southern blot analysis , nucleotide analysis of polymerase chain reaction clones and Southern blot-based methylation assay .

Example answer:
{"entities": [{"text": "primary central nervous system lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCNSL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain lymphomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mantle cell lymphoma ( MCL ) is characterized by the t ( 11 ; 14 ) ( q13 ; q32 ) translocation and several other cytogenetic aberrations , including heterozygous loss of chromosomal arms 1p , 6q , 11q and 13q and/or gains of 3q and 8q .

Example answer:
{"entities": [{"text": "Mantle cell lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In PCLBCL , leg type , most prominent aberrations were a high-level DNA amplification of 18q21.31-q21.33 ( 67 % ) , including the BCL-2 and MALT1 genes as confirmed by FISH , and deletions of a small region within 9p21.3 containing the CDKN2A , CDKN2B , and NSG-x genes .

## Item biored:test:341
Example input:
Sentence: Vitamin E reduces cardiovascular disease in individuals with diabetes mellitus and the haptoglobin 2-2 genotype .

Example answer:
{"entities": [{"text": "Vitamin E", "type": "ChemicalEntity"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "haptoglobin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Excessive signaling by DDR1 and DDR2 has been linked to the progression of various human diseases , including fibrosis , atherosclerosis and cancer .

Example answer:
{"entities": [{"text": "DDR1", "type": "GeneOrGeneProduct"}, {"text": "DDR2", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "atherosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Indeed , as gene flows from colonizers to European native populations were extremely low , the mutational changes might be associated with vulnerability to imported infections .

Example answer:
{"entities": [{"text": "infections", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These data suggest that while NO deficiency increases oxidative stress and sympathetic activity in both arterial and venous vessels , the impact on veins does not make a major contribution to this form of hypertension .

Example answer:
{"entities": [{"text": "NO", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: `` Angiogenesis and blood vessel development '' , `` neuron differentiation/development '' , cell adhesion '' , and `` cell migration '' also showed significant enrichment in our GO analysis .

Example answer:
{"entities": []}

Example input:
Sentence: Adverse cardiovascular effects occurred mainly , but not exclusively , in patients with concomitant risk factors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Genetic Variation at the Sulfonylurea Receptor , Type 2 Diabetes , and Coronary Heart Disease .

Example answer:
{"entities": [{"text": "Sulfonylurea Receptor", "type": "GeneOrGeneProduct"}, {"text": "Type 2 Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Coronary Heart Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Evolvement and progression of cardiovascular diseases affecting the venous and arterial system are influenced by a multitude of environmental and hereditary factors .

## Item biored:test:325
Example input:
Sentence: CONCLUSIONS : The G-395A polymorphism of the human Klotho gene is associated with EH and may be a potential regulatory site .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hypomorphic mutations in meckelin ( MKS3/TMEM67 ) cause nephronophthisis with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "meckelin", "type": "GeneOrGeneProduct"}, {"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "nephronophthisis with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Distinct patterns of germ-line deletions in MLH1 and MSH2 : the implication of Alu repetitive element in the genetic etiology of Lynch syndrome ( HNPCC ) .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: We present a patient with RTH found to be homo-/hemizygous for a mutation in the TR-beta gene .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The FH mutation database : an online database of fumarate hydratase mutations involved in the MCUL ( HLRCC ) tumor syndrome and congenital fumarase deficiency .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "fumarate hydratase", "type": "GeneOrGeneProduct"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HLRCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fumarase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Since the first molecular characterization of an FH mutation by Bourgeron et al in 1994 , a series of reports of both FH deficiency patients and patients with MCUL/HLRRC have described 107 variants , of which 93 are thought to be pathogenic .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "FH deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MCUL/HLRRC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSION : HHRH is caused by biallelic mutations in the SLC34A3 gene .

## Item biored:test:344
Example input:
Sentence: The frequency of 4G/5G genotypes in Chilean Hispanic healthy subjects was similar to that described in other populations .

Example answer:
{"entities": []}

Example input:
Sentence: We therefore tested the hypothesis that variability in the HNF-6 gene is associated with subsets of Type II ( non-insulin-dependent ) diabetes mellitus and estimates of insulin secretion in glucose tolerant subjects .

Example answer:
{"entities": [{"text": "HNF-6", "type": "GeneOrGeneProduct"}, {"text": "Type II ( non-insulin-dependent ) diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: PURPOSE : The prognosis of breast cancer varies considerably among individuals , and inherited genetic factors may help explain this variability .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The identification of around 7 % of homozygotes for the frameshift mutation in our Caucasian population suggests the existence of an interindividual variation of the CYP2F1 activity and , consequently , the possibility of interindividual differences in the toxic response to some pneumotoxicants and in the susceptibility to certain chemically induced diseases .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genetic Variation at the Sulfonylurea Receptor , Type 2 Diabetes , and Coronary Heart Disease .

Example answer:
{"entities": [{"text": "Sulfonylurea Receptor", "type": "GeneOrGeneProduct"}, {"text": "Type 2 Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Coronary Heart Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , to date there is no evidence for a mechanism of haploinsufficiency that can fully explain the DGS/VCFS phenotype .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hepatocyte nuclear factor-6 : associations between genetic variability and type II diabetes and between genetic variability and estimates of insulin secretion .

Example answer:
{"entities": [{"text": "Hepatocyte nuclear factor-6", "type": "GeneOrGeneProduct"}, {"text": "type II diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: However , descriptions of patterns of genetic variability of a larger extent of different factors of hereditary hypercoagulability in single populations are scarce .

## Item biored:test:345
Example input:
Sentence: FINDINGS : Similar distribution of the allelic and genotypic frequencies were observed between the groups ( p > 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In addition , two SNPs found in a GWAS of European ancestry women were confirmed in our study , indicating that African Americans share some genetic risk factors for SLE with European and Chinese subjects .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: His father and paternal grandmother showed a mild thrombocytopenia ( 108 x 10 ( 9 ) /L and 120 x 10 ( 9 ) /L platelets respectively ) while mothers and sister 's referred normal platelet counts .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The frequencies of these genetic alterations were similar to those reported for primary glioblastomas at the population level in Switzerland .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We genotyped 1498 German subjects for SNPs rs6232 and rs6235 within PCSK1 .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "PCSK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Haplotype reconstruction via the expectation-maximization algorithm showed in both populations that only the haplotype containing the minor ( W ) allele at codon 620 was associated with T1D ( OR=2.26 , 95 % CI 1.68-3.02 in Czechs , OR=14.8 , 95 % CI 2.0-651 in Azeri ) or JIA ( OR=2.43 , 95 % CI 1.66-3.56 in Czechs ) .

Example answer:
{"entities": [{"text": "( W ) allele at codon 620", "type": "SequenceVariant"}, {"text": "T1D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "JIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our results added to all these previous data suggest that the actual European allele frequency distribution might not be due to genes spreading , but to a negative selection resulting in the spread of pathogens principally during Roman expansion .

Example answer:
{"entities": []}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: Our analyses showed strong negative correlations in Europe between the allele frequency and two historical parameters , i.e .

Example answer:
{"entities": []}

Input:
Sentence: The aim of this study was i ) to give a detailed description of the frequencies of factors of hereditary thrombophilia and their combinations in a German population ( n = 282 ) and ii ) to compare their distributions with those reported for other regions .

## Item biored:test:365
Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: For this purpose we developed a high-throughput methodology to genotype both normal and deleted alleles using a chip-based matrix-assisted laser desorption-time-of-flight ( MALDI-TOF ) mass spectrometer and Multiplex PCR .

Example answer:
{"entities": []}

Example input:
Sentence: Polymerase chain reaction performed with DNA isolated from somatic human-rodent cell hybrids containing defined human chromosomes as template gave a human-specific signal which mapped the NDUFS2 and NDUFS3 subunits to chromosomes 1 and 11 , respectively .

Example answer:
{"entities": [{"text": "human-rodent", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "human-specific", "type": "OrganismTaxon"}, {"text": "NDUFS2", "type": "GeneOrGeneProduct"}, {"text": "NDUFS3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA was isolated from peripheral blood and genotyping was performed with PCR-based methods .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was isolated from the leukocytes and genotyping was performed using the Sequenom platform .

Example answer:
{"entities": []}

Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotyping was determined by the polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) technique .

Example answer:
{"entities": []}

Example input:
Sentence: Genotyping was performed by kinetic polymerase chain-reaction or TaqMan assays .

Example answer:
{"entities": []}

Input:
Sentence: Genotyping was performed by polymerase-chain-reaction-based fluorescence and direct sequencing of genomic DNA .

## Item biored:test:284
Example input:
Sentence: We have recently shown that estrogen negatively modulates the hypotensive effect of clonidine ( mixed alpha2-/I1-receptor agonist ) in female rats and implicates the cardiovascular autonomic control in this interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}, {"text": "alpha2-/I1-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "adrenergic antagonists", "type": "ChemicalEntity"}, {"text": "beta-adrenergic receptor", "type": "GeneOrGeneProduct"}, {"text": "propranolol", "type": "ChemicalEntity"}, {"text": "cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "alpha ( 1 )", "type": "GeneOrGeneProduct"}, {"text": "prazosin", "type": "ChemicalEntity"}, {"text": "alpha ( 2 )", "type": "GeneOrGeneProduct"}, {"text": "yohimbine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: At dose levels of ( + ) -propranolol which attenuated the responses to isoprenaline , there was a significant prolongation of the PR interval of the electrocardiogram.3 .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , administration of a ghrelin receptor antagonist further reduced blood glucose levels into the markedly hypoglycemic range in overnight-fasted , streptozotocin-treated Gcgr ( -/- ) mice .

Example answer:
{"entities": [{"text": "ghrelin receptor", "type": "GeneOrGeneProduct"}, {"text": "blood glucose", "type": "ChemicalEntity"}, {"text": "streptozotocin-treated", "type": "ChemicalEntity"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Input:
Sentence: The decrease in the heart rate ( HR ) induced by the beta-AR antagonist metoprolol in conscious rats was significantly attenuated in TGR compared with SD rats ( -9.9 +/- 1.7 % vs. -18.1 +/- 1.5 % ) , whereas the effect of parasympathetic blockade by atropine on HR was similar in both strains .

## Item biored:test:299
Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Hyperprolactinemia was present in 49 % of 83 boys ( n = 41 ) treated with risperidone for a mean of 2.9 years .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 61-year-old Japanese man with nephrotic syndrome due to focal segmental glomerulosclerosis was initially responding well to steroid therapy .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal segmental glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Six patients were operated on in the globus pallidus interna ( GPi ) and four in the subthalamic nucleus ( STN ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After 7 days , PAN treatment induced significant proteinuria , hypoalbuminemia , decreased urinary sodium excretion , and extensive ascites .

Example answer:
{"entities": [{"text": "PAN", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sodium", "type": "ChemicalEntity"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CLINICAL FEATURES : A 50-year-old woman with low back and right leg pain was scheduled for epidural steroid injection .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "low back and right leg pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Complications were observed in two patients : one had a left homonymous hemianopsia after pallidotomy and another one developed left hemiballistic movements 3 days after subthalamotomy which partly improved within 1 month with Valproate 1000 mg/day .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "homonymous hemianopsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Valproate", "type": "ChemicalEntity"}]}

Input:
Sentence: This patient presented with a complaint of epigastric pain and watery diarrhea over the past 3 months , and had undergone subtotal parathyroidectomy and enucleation of pancreatic islet cell tumor about 10 yr before .

## Item biored:test:350
Example input:
Sentence: Her mother was heterozygous for the Asn45Ser mutation , and her father , for the nine-nucleotide deletion .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: The genetic basis of the other forms remain unknown , including the early-onset , recessive form with Mallory body-like inclusions ( MB-DRMs ) , first described in five related German patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : We have confirmed the localization of the congenital microcoria locus ( MCOR ) to 13q31-q32 in a large Asian Indian family and conclude that current information suggests this is a single locus disorder and genetically homogeneous .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : By clinical examination , the patients and the pedigrees were divided into the following three groups : AN , coloboma of iris and choroids , and the anterior segment malformations including peters anomaly .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coloboma of iris and choroids", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anterior segment malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "peters anomaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The patient , her twin sister , and her mother also presented with cerebral cavernous malformations .

## Item biored:test:366
Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: Another is the 3A/4A polymorphism ( -134delA ) located in the 5'-untranslated region .

Example answer:
{"entities": [{"text": "-134delA", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : In the Czechs , all three SNPs were in a tight linkage disequlibrium , while in the Azeri , the linkage disequlibrium was limited to between the promoter and 3'-UTR polymorphism , D ' ( -1123 , +2740 ) =0.99 , r ( 2 ) =0.72 .

Example answer:
{"entities": []}

Example input:
Sentence: There was also a statistically significant p-value of the ( 2 ) test for the trend observed in the XRCC1 Arg399Gln polymorphism ( ptrend=0.0048 ) .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}]}

Example input:
Sentence: The polymorphism did not show any association with FHCM .

Example answer:
{"entities": [{"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Association and Hardy-Weinberg equilibrium checking were assessed by Chi-square test and Mann-Whitney U test .

Example answer:
{"entities": []}

Example input:
Sentence: No Hardy Weinberg disequilibrium and no significant difference in allele frequencies between patients and controls were observed for any variation .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: RESULTS : The polymorphism was in Hardy-Weinberg equilibrium .

## Item biored:test:190
Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Status epilepticus ( P45 ) rats failed to acquire either sound-source location or sound-silence discriminations .

Example answer:
{"entities": [{"text": "Status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : The data show that CCR2 and CCL2 are up-regulated in the hippocampus after pilocarpine-induced SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work CCR2 and CCL2 expression were examined following status epilepticus ( SE ) induced by pilocarpine injection .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chemokine CCL2 and its receptor CCR2 are increased in the hippocampus following pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: To investigate how GAP43 expression ( GAP43-ir ) correlates with MFS , we assessed the intensity ( densitometry ) and extension ( width ) of GAP43-ir in the inner molecular layer of the dentate gyrus ( IML ) of rats subject to status epilepticus induced by pilocarpine ( Pilo ) , previously injected or not with cycloheximide ( CHX ) , which has been shown to inhibit MFS .

## Item biored:test:309
Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Estrogen replacement ( 17beta-estradiol subcutaneous pellet , 14.2 microg/day , 12 wk ) of Ovx rats restored the hemodynamic and locomotor effects of alpha-methyldopa to sham-operated levels .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: In Alzheimer 's disease groups , rats were injected with STZ-icv bilaterally ( 3 mg/kg ) in first day and 3 days later , a similar STZ-icv application was repeated .

Example answer:
{"entities": [{"text": "Alzheimer 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ-icv", "type": "ChemicalEntity"}]}

Example input:
Sentence: At puberty ( P40 ) , half the PCPA-treated rats and half the saline-treated rats began treatment with testosterone ( T , 5 mg/kg , 5 days/week ) .

Example answer:
{"entities": [{"text": "PCPA-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a prevention study , rats received 4 days of LF treatment followed by Dex and continued during the test period .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Upon pretreatment with mangiferin ( 100 mg/kg body weight suspended in 2 ml of dimethyl sulphoxide ) given intraperitoneally for 28 days to MI rats protected the above-mentioned parameters to fall from the normal levels .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "dimethyl sulphoxide", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: The rat received either alpha-TC ( 20 mg/kg ) intraperitoneally for 3 days and 30 min prior to MA administration or DFO ( 50 mg/kg ) subcutaneously 30 min before MA administration .

## Item biored:test:306
Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further , we show that mice genetically engineered to be deficient in brain DA develop METH neurotoxicity , as long as the thermic effects of METH are preserved .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , we demonstrate that mice genetically engineered to have unilateral brain DA deficits develop METH-induced dopaminergic deficits that are of comparable magnitude on both sides of the brain .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "dopaminergic deficits", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Methamphetamine-induced neurotoxicity and microglial activation are not mediated by fractalkine receptor signaling .

Example answer:
{"entities": [{"text": "Methamphetamine-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

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

Input:
Sentence: Methamphetamine ( MA ) -induced dopaminergic neurotoxicity is believed to be associated with the increased formation of free radicals .

## Item biored:test:283
Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Both GcgR knockout ( Gcgr ( -/- ) ) mice and db/db mice that were administered GcgR monoclonal antibody displayed lower blood glucose levels accompanied by elevated plasma ghrelin levels .

Example answer:
{"entities": [{"text": "GcgR", "type": "GeneOrGeneProduct"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "blood glucose", "type": "ChemicalEntity"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover mRNA levels of LDLr and ERK1/2 as well as protein levels of total and activated forms of ERK1/2 in rat liver were evaluated by Western blotting and quantitative real time polymerase chain reaction analysis .

Example answer:
{"entities": [{"text": "LDLr", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BMP-4 reduced LHbeta mRNA up-regulation in response to GnRH ( +/-activin ) and decreased GnRH receptor expression , which would favour FSH , rather than LH , synthesis and secretion .

Example answer:
{"entities": [{"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "LHbeta", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}, {"text": "GnRH receptor", "type": "GeneOrGeneProduct"}, {"text": "FSH", "type": "GeneOrGeneProduct"}, {"text": "LH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Re-expression of LKB1 or knockdown of VEGF receptor 2 decreased the overproliferation and -migration observed in LKB1 ( endo-/- ) cells .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The greater LV hypertrophy in TGR rats was associated with more pronounced downregulation of beta-AR and upregulation of LV beta-AR kinase-1 mRNA levels compared with those in SD rats .

## Item biored:test:216
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Given VIP 's role as an anti-inflammatory mediator , we hypothesized that VIP ( -/- ) mice would exhibit enhanced inflammatory mediator expression after cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , Wistar Kyoto/spontaneous hypertensive ( WKY/SHR ) rats fed a high-salt diet developed severe proteinuria , resulting from pronounced renal inflammation , fibrosis and tubular epithelial cell apoptosis .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using puromycin aminonucleoside nephrosis ( PAN ) rats , we studied early ultrastructural and permeability changes in relation to the expression of the podocyte-associated molecules nephrin , a-actinin , dendrin , and plekhh2 , the last two of which were only recently discovered in podocytes .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "ChemicalEntity"}, {"text": "nephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "nephrin", "type": "GeneOrGeneProduct"}, {"text": "a-actinin", "type": "GeneOrGeneProduct"}, {"text": "dendrin", "type": "GeneOrGeneProduct"}, {"text": "plekhh2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This shift in balance may contribute to increased bladder dysfunction in VIP ( -/- ) mice with bladder inflammation and altered neurochemical expression in micturition pathways .

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
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Histopathological examination revealed severe renal damage such as proteinaceous casts in tubuli and tubular expansion in the kidney of control rats , while an improvement of the damage was seen in antithrombin-treated rats .

Example answer:
{"entities": [{"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "antithrombin-treated", "type": "ChemicalEntity"}]}

Input:
Sentence: There were a significant dilatation of tubular lumens , extensive epithelial cell vacuolization , atrophy , desquamation , and necrosis in VCM-treated rats more than those of the control and the erdosteine groups .

## Item biored:test:269
Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of chemokines CCL4 and CCL5 in cirrhotic patients indicate the presence of hepatocellular carcinoma .

Example answer:
{"entities": [{"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hepatocellular carcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Liver metastases from colorectal cancer ( CRC ) are a clinically significant problem .

Example answer:
{"entities": [{"text": "Liver metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Most hepatocellular carcinomas ( HCCs ) are diagnosed at an advanced stage .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Most hepatocellular carcinomas ( HCC ) develop as a result of chronic liver inflammation .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic liver inflammation", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Chronic infection with hepatitis C virus ( HCV ) can progress to cirrhosis , hepatocellular carcinoma , and end-stage liver disease .

## Item biored:test:335
Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Women with a deletion allele had a significantly greater risk of preterm delivery [ adjusted odds ratio ( AOR ) : 3.0 ; 95 % CI : 1.0 , 8.8 ; P < 0.05 ] than did those without a deletion allele .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Homozygosity for c.2607C > A was also identified in an unrelated but haplotypically identical patient with an unusually favorable outcome despite severe neonatal-onset GE .

Example answer:
{"entities": [{"text": "c.2607C > A", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Methylation of the 5'CpG island of the p14 gene was not suggested for any case without homozygous deletion .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thus , the same deletion patterns covered the entire p14 gene for all cases except for one case , which suggested the hemizygous deletion of exons 1beta and 2 and homozygous deletion of exon 3 .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Input:
Sentence: A second heterozygotic 14-bp deletion was detected in an unaffected ex-premature girl .

## Item biored:test:377
Example input:
Sentence: At dose levels of ( + ) -propranolol which attenuated the responses to isoprenaline , there was a significant prolongation of the PR interval of the electrocardiogram.3 .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: AIMS : Individuals with both diabetes mellitus ( DM ) and the Haptoglobin ( Hp ) 2-2 genotype are at increased risk of cardiovascular disease .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Haptoglobin", "type": "GeneOrGeneProduct"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "cardiovascular disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The current data showed that pilocarpine significantly delayed onset of arrhythmias , decreased the time course of ventricular tachycardia and fibrillation , reduced arrhythmia score , and increased the survival time of arrhythmic rats and guinea pigs .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventricular tachycardia and fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "guinea pigs", "type": "OrganismTaxon"}]}

Example input:
Sentence: hiPS-CMs using MEA system and FPDc can predict the effects of drug candidates on QT interval .

Example answer:
{"entities": []}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with dyskinesia had lower onset age ( p < 0.001 ) , longer duration of levodopa therapy ( p < 0.001 ) , longer disease duration ( p < 0.001 ) , higher total daily levodopa dose ( p < 0.001 ) , and higher total UPDRS scores ( p = 0.005 ) than patients without dyskinesia .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In these trials , Hp typing of 69 DM individuals and treating those with the Hp 2-2 with vitamin E prevented one myocardial infarct , stroke or cardiovascular death .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "myocardial infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolongation of the QT interval in the ECG of patients with torsade de pointes ( TdP ) has been reported in methadone users .

Example answer:
{"entities": [{"text": "Prolongation of the QT interval", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "torsade de pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Input:
Sentence: dP/dtejc outcome was combined with the ECG results , giving an ECG-enhanced value , and compared to ECG alone .
