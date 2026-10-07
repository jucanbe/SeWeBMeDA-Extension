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

## Item biored:test:746
Example input:
Sentence: No differences were observed in PAI-1 plasma levels among obese patients with liver fibrosis ( 10.64 4.35 ) compared to patients without liver fibrosis ( 10.61 5.2 ; p = 0.985 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : We decided to investigate the role of the polymorphism ( G1359A ) of CB1 receptor gene on adipocytokines response and weight loss secondary to a lifestyle modification ( Mediterranean hypocaloric diet and exercise ) in obese patients .

Example answer:
{"entities": [{"text": "G1359A", "type": "SequenceVariant"}, {"text": "CB1 receptor", "type": "GeneOrGeneProduct"}, {"text": "weight loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: His apoE phenotype was apoE3/2 and he had mild dyslipidemia with a mid-band on polyacrylamide gel electrophoresis .

Example answer:
{"entities": [{"text": "apoE", "type": "GeneOrGeneProduct"}, {"text": "apoE3/2", "type": "GeneOrGeneProduct"}, {"text": "dyslipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyacrylamide", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: No association was found between PAI-1 serum levels or 4G/5G genotype with liver fibrosis in obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: In particular , serum apoB-100 concentration might be an informative marker for judging changes in HCV-associated intracellular lipoprotein metabolism in patients carrying the rs8099917 responder genotype .

## Item biored:test:688
Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations in PDE6H and in KCNV2 have been described in CDSRR .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Our findings suggest that the additive effects of both mutations in the GPIX gene are responsible for the BSS phenotype of the patient .

Example answer:
{"entities": [{"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: More than 20 DNA mutations with different inheritance pattern have been described in patients with Bernard-Soulier Syndrome ( BSS ) , leading to abnormal or absent synthesis and/or expression of GPIbalpha .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GPIbalpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Mutations in the BSCL2 gene are known to result in CGL2 , a more severe phenotype than CGL1 , with earlier onset , more extensive fat loss and biochemical changes , more severe intellectual impairment , and more severe cardiomyopathy .

## Item biored:test:677
Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: The isoforms TGF-beta1 and TGF-beta2 have profibrotic properties , whereas TGF-beta3 may have antifibrotic functions .

Example answer:
{"entities": [{"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta2", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Remarkably , transfection of Langerin cDNA into fibroblasts created a compact network of membrane structures with typical features of BG .

Example answer:
{"entities": [{"text": "Langerin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In more than 98 % of cases , the disease is associated with a G to A or G to C substitution at nucleotide position 1138 ( p.G380R ) of the fibroblast growth factor receptor 3 ( FGFR3 ) gene .

Example answer:
{"entities": [{"text": "G to A or G to C substitution at nucleotide position 1138", "type": "SequenceVariant"}, {"text": "p.G380R", "type": "SequenceVariant"}, {"text": "fibroblast growth factor receptor 3", "type": "GeneOrGeneProduct"}, {"text": "FGFR3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: The molecular basis of FDH involves mutations in the PORCN gene , which encodes an enzyme that allows membrane targeting and secretion of several Wnt proteins critical for normal tissue development .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A single nucleotide polymorphism at position 388 of the FGFR4 amino-acid sequence results in the substitution of glycine ( Gly ) with arginine ( Arg ) and higher frequency of the ArgArg genotype was previously found in prostate cancer patients .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "glycine ( Gly ) with arginine ( Arg )", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Filamins are actin-binding proteins which contain three family members , filamin A , B and C. They are the products of three different genes , FLNA , FLNB and FLNC , which can generate various transcript variants in different cell types .

Example answer:
{"entities": [{"text": "Filamins", "type": "GeneOrGeneProduct"}, {"text": "actin-binding proteins", "type": "GeneOrGeneProduct"}, {"text": "filamin A , B and", "type": "GeneOrGeneProduct"}, {"text": "FLNA", "type": "GeneOrGeneProduct"}, {"text": "FLNB", "type": "GeneOrGeneProduct"}, {"text": "FLNC", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Fibrinogen consists of three pairs of non-identical polypeptide chains , encoded by different genes ( fibrinogen alpha [ FGA ] , fibrinogen beta [ FGB ] and fibrinogen gamma [ FGG ] ) .

## Item biored:test:755
Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The C139T mutation , predicted to result in the substitution of an arginine by a tryptophan ( R47W ) in the N-terminal subdomain , affected conserved residues in the PAX9 paired domain .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "arginine by a tryptophan", "type": "SequenceVariant"}, {"text": "R47W", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In a patient , a C-to-G transition was identified at nucleotide 857 in exon 8 that resulted in a substitution of alanine for proline at amino acid 286 in the first calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "C-to-G transition was identified at nucleotide 857", "type": "SequenceVariant"}, {"text": "alanine for proline at amino acid 286", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sequencing of the coding region of PTPN22 on these haplotypes revealed a novel variant ( 2250G/C ) predicted to result in a nonsynonymous amino acid substitution .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "2250G/C", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The exon 4 sequence of TGFBI of the proband exhibits the heterozygous single-nucleotide mutation , C417T , leading to amino acid substitution ( R124C ) in the encoded TGF-induced protein .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "C417T", "type": "SequenceVariant"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGF-induced protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation resulted in replacement of a non-polar amino acid ( proline ) with a polar amino acid ( serine ) at position 29 ( P29S ) .

Example answer:
{"entities": [{"text": "( proline ) with a polar amino acid ( serine ) at position 29", "type": "SequenceVariant"}, {"text": "P29S", "type": "SequenceVariant"}]}

Input:
Sentence: RESULTS : A novel heterozygous c.3703T > C change in exon 29 of FBN1 was detected in the proband , which resulted in the substitution of serine by proline at codon 1235 ( p.S1235P ) .

## Item biored:test:782
Example input:
Sentence: In addition , GABA content of mice hippocampus treated with GFC75 plus P400 showed an increase of 46.90 % when compared with seized mice .

Example answer:
{"entities": [{"text": "GABA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Glutamatergic neurotransmission mediated by NMDA receptors in the inferior colliculus can modulate haloperidol-induced catalepsy .

Example answer:
{"entities": [{"text": "NMDA receptors", "type": "GeneOrGeneProduct"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings suggest that the G51S PNP polymorphism is associated with a faster rate of cognitive decline in AD patients , highlighting the important role of purine metabolism in the progression of this neurodegenerative disorder .

Example answer:
{"entities": [{"text": "G51S", "type": "SequenceVariant"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "neurodegenerative disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Increased CCR2 was observed in the hippocampus after SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , glial activation and neuroinflammation were attenuated in the hippocampi of KCa3.1-/-/APP/PS1 mice , as compared with APP/PS1 mice .

Example answer:
{"entities": [{"text": "neuroinflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCa3.1-/-/APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Our results show induction of NP1 in primary hippocampal neurons following OGD exposure ( 4-8 h ) and in the ipsilateral hippocampal CA1 and CA3 regions at 24-48 h post-HI compared to the contralateral side .

## Item biored:test:794
Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "Learning and memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fifteen moderate MDMA users ( < 55 lifetime tablets ) , 22 heavy MDMA+ users ( > 55 lifetime tablets ) , 16 ex-MDMA+ users ( last tablet > 1 year ago ) and 13 controls were compared on a battery of neuropsychological tests .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "MDMA+", "type": "ChemicalEntity"}]}

Example input:
Sentence: It has been consistently shown that ecstasy users display impairments in learning and memory performance .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "impairments in learning and memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: The aim of the study was to investigate the effects of moderate and heavy MDMA use on cognitive function , as well as the effects of long-term abstention from MDMA , in subjects genotyped for 5-HTTLPR .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To address the potential confounding effects of the cannabis use of the ecstasy using group , a second analysis included 14 previously tested cannabis users ( Nestor , L. , Roberts , G. , Garavan , H. , Hester , R. , 2008 .

Example answer:
{"entities": [{"text": "cannabis", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Input:
Sentence: OBJECTIVES : The present study aimed to be the largest to date in sample size and 5HT-related behaviors ; the first to compare present ecstasy users with past users after an abstinence of 4 or more years , and the first to include robust controls for other recreational substances .

## Item biored:test:773
Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The odds ratio ( OR ) for SLE patients with the Gln/Gln versus Gln/Arg or Arg/Arg genotypes was 1.553 ( 95 % confidence interval [ CI ] =0.9573-2.520 ; p=0.0729 ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our studies may confirm that the XRCC1 Arg399Gln polymorphism may increase the risk of incidence of SLE and the occurrence of some SLE manifestations .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The OR for the 399 Gln allele in patients with SLE was 1.406 ( 95 % CI=1.111-1.779 , p=0.0045 ) .

Example answer:
{"entities": [{"text": "399 Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The OR for the STAT4 C allele frequency showed a 1.539-fold increased risk of SLE ( 95 % CI = 1.209-1.959 , p = 0.0004 ) .

## Item biored:test:826
Example input:
Sentence: METHODS : In type 2 diabetic patients , cases who developed CAD were compared retrospectively with controls that did not .

Example answer:
{"entities": [{"text": "type 2 diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The polymorphism distribution was also analyzed in AD patients stratified according to differential progressive rate of cognitive decline during a 2-year follow-up .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Example input:
Sentence: Presence or absence of a CCR5 wt/DD32 genotype and progressive or long-term nonprogressive course of infection stratify the clinical populations in a two-way design .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A case-control study was conducted on incident gastric adenocarcinoma patients ( n=271 ) and age-gender frequency-matched control subjects ( n=271 ) .

Example answer:
{"entities": [{"text": "gastric adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A Retrospective comparative study .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : The first part of this study was an 8-week , multicenter , randomized , double-blind , placebo controlled , parallel-group trial .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN : Case-control study .

Example answer:
{"entities": []}

Example input:
Sentence: DESIGN : A cross-sectional design in stable , treated patients with schizophrenia evaluated using a frequently sampled intravenous glucose tolerance test and the Bergman minimal model analysis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: DESIGN : A retrospective observational cohort study .

Example answer:
{"entities": []}

Input:
Sentence: DESIGN : Multicenter , retrospective , propensity-matched cohort study .

## Item biored:test:827
Example input:
Sentence: Neuroimage 40 , 1328-1339 ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Expected values were cleft BPRs registered for the entire ECLAMC hospital network .

Example answer:
{"entities": []}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Six patients were operated on in the globus pallidus interna ( GPi ) and four in the subthalamic nucleus ( STN ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These results establish in the majority of ACC the presence of a previously uncharacterized population of CD133 ( + ) cells with neural stem properties , which are driven by SOX10 , NOTCH1 , and FABP7 .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "FABP7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: SETTING : Neurocritical care units at two academic medical centers with dedicated neurocritical care teams and board-certified neurointensivists .

## Item biored:test:768
Example input:
Sentence: In conclusion , splicing variants of FLNB are differentially expressed in GCT cells and may play a role in the proliferation and differentiation of tumor cells .

Example answer:
{"entities": [{"text": "FLNB", "type": "GeneOrGeneProduct"}, {"text": "GCT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SLURP1 mutation-impaired T-cell activation in a family with mal de Meleda .

Example answer:
{"entities": [{"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "mal de Meleda", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To test that SLURP-1 is essential for T-cell activation .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The presence of wild-type SLURP-1 is essential for normal T-cell activation .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVES : To investigate the association of the SLURP1 gene mutation with T-cell activation in a Taiwanese family with MDM .

Example answer:
{"entities": [{"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SLURP-1 is an allosteric agonist to the nicotinic acetylcholine receptor ( nAchR ) and it regulates epidermal homeostasis .

Example answer:
{"entities": [{"text": "SLURP-1", "type": "GeneOrGeneProduct"}, {"text": "nicotinic acetylcholine receptor", "type": "GeneOrGeneProduct"}, {"text": "nAchR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: SIGNIFICANCE : The obtained results identified target genes for both NNK and SLURP-1 and shed light on the molecular mechanism of their reciprocal effects on tumorigenic transformation of bronchial and oral epithelial cells .

## Item biored:test:778
Example input:
Sentence: In the classical form it presents as neonatal apnea , intractable seizures , and hypotonia , followed by significant psychomotor retardation .

Example answer:
{"entities": [{"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Histopathologically , typical findings were observed in the cerebella from the control groups , but the findings consistent with early embryonic development were noted in BCNU-exposed cortical dysplasia group .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: `` Angiogenesis and blood vessel development '' , `` neuron differentiation/development '' , cell adhesion '' , and `` cell migration '' also showed significant enrichment in our GO analysis .

Example answer:
{"entities": []}

Example input:
Sentence: Comparable histological injuries in patients with hypoxia/ischemia and TD have been described in the thalamus and mammillary bodies , suggesting a congruency between the cellular responses to these stresses .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "hypoxia/ischemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immuno/histochemistry and electron microscopy were carried out on the offspring cerebellum , and levels of malondialdehyde and superoxide dismutase were determined .

Example answer:
{"entities": [{"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : Hypotension and a resultant decrease in cerebral blood flow have been implicated in the development of cognitive dysfunction .

Example answer:
{"entities": [{"text": "Hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cognitive dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Insulin-like growth factor 1 receptor-mediated cell survival in hypoxia depends on the promotion of autophagy via suppression of the PI3K/Akt/mTOR signaling pathway .

Example answer:
{"entities": [{"text": "Insulin-like growth factor 1", "type": "GeneOrGeneProduct"}, {"text": "hypoxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PI3K/Akt/mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Brain development involves extensive migration of neurons .

Example answer:
{"entities": []}

Example input:
Sentence: Hypoxia is widely accepted as a fundamental biological phenomenon , which is strongly associated with tissue damage and cell viability under stress conditions .

Example answer:
{"entities": [{"text": "Hypoxia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Developing brain is highly susceptible to hypoxic-ischemic ( HI ) injury leading to severe neurological disabilities in surviving infants and children .

## Item biored:test:818
Example input:
Sentence: Overall survival from the time of OLTX was not significantly different among groups , but by year 13 , the survival of the patients who had ESRD was only 28.2 % compared with 54.6 % in the control group .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , we conclude that CE is a reasonably safe alternative to be used in subjects who do not tolerate P and N .

Example answer:
{"entities": [{"text": "CE", "type": "ChemicalEntity"}, {"text": "P", "type": "ChemicalEntity"}, {"text": "N", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results suggest that , despite a known association with increased weight , long-term sulfonylurea therapy may reduce the risk of coronary heart disease .

Example answer:
{"entities": [{"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Our results suggest that use of high-dose TXA in older patients in conjunction with cardiopulmonary bypass and open-chamber cardiac surgery is associated with clinical seizures in susceptible patients .

Example answer:
{"entities": [{"text": "TXA", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Often , chemotherapy by doxorubicin ( Adriamycin ) is limited due to life threatening cardiotoxicity in patients during and posttherapy .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "Adriamycin", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : The rate of major hemorrhage was high in this old , frail group , but excluding fatalities , resulted in no long-term sequelae , and the stroke rate on warfarin was low , demonstrating how effective warfarin treatment is .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: If confirmed , this may be important because most Indian patients receive the cheaper older sulphonylureas , and present guidelines do not distinguish between individual agents .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "sulphonylureas", "type": "ChemicalEntity"}]}

Example input:
Sentence: WHAT THE READER WILL GAIN : The reader will gain better insight into the safety of capecitabine in special populations such as patients with advanced age , renal and kidney disease .

Example answer:
{"entities": [{"text": "capecitabine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "renal and kidney disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Careful therapeutic intervention is necessary in cases involving elderly patients who suffer from depression .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Capecitabine has a well-established safety profile and can be given safely to patients with advanced age , hepatic and renal dysfunctions .

Example answer:
{"entities": [{"text": "Capecitabine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hepatic and renal dysfunctions", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , information is limited concerning the safety of the regimen in elderly patients .

## Item biored:test:815
Example input:
Sentence: BACKGROUND : Matrix metalloproteinases ( MMPs ) are involved in the degradation of the extracellular matrix of the intervertebral disc .

Example answer:
{"entities": [{"text": "Matrix metalloproteinases", "type": "GeneOrGeneProduct"}, {"text": "MMPs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of NEK2 , phospho-AKT and MMP-2 was evaluated by immunohistochemistry in 63 cases of HCC and matched adjacent non-tumorous liver tissues .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Coenzyme Q10 significantly compensated deficits in the antioxidant defense mechanisms ( reduced glutathione level and superoxide dismutase activity ) , suppressed lipid peroxidation , decreased the elevations of tumor necrosis factor-alpha , nitric oxide and platinum ion concentration , and attenuated the reductions of selenium and zinc ions in renal tissue resulted from cisplatin administration .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "nitric oxide", "type": "ChemicalEntity"}, {"text": "platinum", "type": "ChemicalEntity"}, {"text": "selenium", "type": "ChemicalEntity"}, {"text": "zinc", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Hsp90beta inhibition caused the destabilization of upstream mediators in various pathogenic signalling events , thereby effectively ameliorating this nephropathy owing to renal hypoxia and oxidative stress .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoxia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Its action mechanism was associated with the down-regulation of MMP-2/9 activities and inhibition of peroxidation in injured liver .

## Item biored:test:832
Example input:
Sentence: RESULTS : Significant differences were detected in genotypic distribution ( p = 0.04 ) as well as the allelic frequency ( p = 0.003 ) between the SHCM patients and controls .

Example answer:
{"entities": [{"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : The genotype distribution of the Met326Ile polymorphism in the PCOS group was not different from that of the controls ( Met326Met/Met326Ile/Ile326Ile rates were 73.4 % /23.4 % /3.2 % and 70.3 % /26.1 % /3.6 % for the PCOS and control groups , respectively , P = 0.72 ) .

Example answer:
{"entities": [{"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "PCOS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Met326Met/Met326Ile/Ile326Ile", "type": "SequenceVariant"}]}

Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: However , the main outcome measure was the sequencing of genomic DNA from peripheral blood samples of 41 women with POF and 36 fertile women ( controls ) .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further age stratification showed significant genotypic as well as allelic association in the group of over 40 years ( genotypic : p value = 0.035 , odds ratio = 1.617 with 95 % CI = 1.033-2.529 ; allelic : p value = 0.033 , odds ratio = 1.445 with 95 % CI = 1.029-2.029 ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Though FAS-670 polymorphisms did not show any significant difference , the proportion of subjects with IL1B-31TT ( or IL1B-511CC ) increased according to stage ( trend P=0.019 ) .

Example answer:
{"entities": [{"text": "FAS-670", "type": "GeneOrGeneProduct"}, {"text": "IL1B-31TT", "type": "GeneOrGeneProduct"}, {"text": "IL1B-511CC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A statistically significant difference in allele frequency between cases and controls was observed for 2 of the SNPs ( +3100 T/G and +8365 C/T ) , with an odds ratio of 0.78 ( 95 % CI=0.64-0.96 ) and 0.65 ( 95 % CI=0.45-0.94 ) respectively .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}]}

Input:
Sentence: No difference in the primary composite outcome in both the unmatched ( 30 % vs 30 % , p = 0.94 ) or matched cohorts ( 28 % vs 34 % , p = 0.35 ) could be found .

## Item biored:test:742
Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : This study showed that SNPs rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , but not rs7535263 , rs1410996 , or rs2274700 , in CFH were significantly associated with wet AMD in a mainland Han Chinese population .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "rs7535263", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "rs2274700", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: ApoE gene analysis showed a nucleotide substitution of G to C at codon 158 of exon 4 .

Example answer:
{"entities": [{"text": "ApoE", "type": "GeneOrGeneProduct"}, {"text": "G to C at codon 158", "type": "SequenceVariant"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Our results demonstrated that both the aa 70 substitution in the core region of the HCV and the rs8099917 SNP located proximal to the IL28B were independent factors in determining serum apoB-100 and low-density lipoprotein ( LDL ) cholesterol levels .

## Item biored:test:748
Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the WFS1 gene of these patients , we identified a novel mutation , a nine nucleotide insertion ( AFF344-345ins ) .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "nine nucleotide insertion", "type": "SequenceVariant"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}]}

Example input:
Sentence: Hypomorphic mutations in meckelin ( MKS3/TMEM67 ) cause nephronophthisis with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "meckelin", "type": "GeneOrGeneProduct"}, {"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "nephronophthisis with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the carbohydrate sulfotransferase gene ( CHST6 ) for a Chinese family with macular corneal dystrophy ( MCD ) and to investigate the histopathological changes in the affected cornea .

Example answer:
{"entities": [{"text": "carbohydrate sulfotransferase gene", "type": "GeneOrGeneProduct"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "macular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The FH mutation database : an online database of fumarate hydratase mutations involved in the MCUL ( HLRCC ) tumor syndrome and congenital fumarase deficiency .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "fumarate hydratase", "type": "GeneOrGeneProduct"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HLRCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fumarase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified and characterized a PABPN1 mutation in a Taiwanese family with OPMD .

Example answer:
{"entities": [{"text": "PABPN1", "type": "GeneOrGeneProduct"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: PURPOSE : To identify the mutation in the fibrillin-1 gene ( FBN1 ) in a Chinese family with Marfan syndrome ( MFS ) .

## Item biored:test:770
Example input:
Sentence: Promoter insertion/deletion in the IRF5 gene is highly associated with susceptibility to systemic lupus erythematosus in distinct populations , but exerts a modest effect on gene expression in peripheral blood mononuclear cells .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymorphisms in the IRF5 gene have been associated with susceptibility to systemic lupus erythaematosus ( SLE ) in Caucasian and Asian populations , but their involvement in other autoimmune diseases is still uncertain .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythaematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autoimmune diseases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CD72 polymorphisms associated with alternative splicing modify susceptibility to human systemic lupus erythematosus through epistatic interaction with FCGR2B .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These additional genes notably included TNFRSF6 ( Fas ) and IRF5 , supporting previous findings of their association with SLE pathogenesis .

Example answer:
{"entities": [{"text": "TNFRSF6", "type": "GeneOrGeneProduct"}, {"text": "Fas", "type": "GeneOrGeneProduct"}, {"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : SELP and IRAK1 were identified as novel SLE-associated genes with a high degree of significance , suggesting new directions in understanding the pathogenesis of SLE .

Example answer:
{"entities": [{"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}, {"text": "SLE-associated", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The STAT4 has been found to be a susceptible gene in the development of systemic lupus erythematosus ( SLE ) in various populations .

## Item biored:test:767
Example input:
Sentence: Inhibition of caspases , RIP1 , or RIP3 blocks radiation/TNFa-induced cell death , whereas inhibition of RIP1 blocks TNFa-induced caspase activation , suggesting that caspases and RIP1 act sequentially to mediate the non-compensatory cell death pathways .

Example answer:
{"entities": [{"text": "caspases", "type": "GeneOrGeneProduct"}, {"text": "RIP1", "type": "GeneOrGeneProduct"}, {"text": "RIP3", "type": "GeneOrGeneProduct"}, {"text": "TNFa-induced", "type": "GeneOrGeneProduct"}, {"text": "caspase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the functional aspect , overexpression of FLNBv4 led to upregulation of RANKL , OCN , OPG and RUNX2 , which are closely related to GCT cell survival and differentiation .

Example answer:
{"entities": [{"text": "FLNBv4", "type": "GeneOrGeneProduct"}, {"text": "RANKL", "type": "GeneOrGeneProduct"}, {"text": "OCN", "type": "GeneOrGeneProduct"}, {"text": "OPG", "type": "GeneOrGeneProduct"}, {"text": "RUNX2", "type": "GeneOrGeneProduct"}, {"text": "GCT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: Carriers of TBX21 promoter SNP rs17250932 and HLX1 promoter SNP rs2738751 showed reduced or trendwise reduced ( p < 0.07 ) IL-5 , IL-13 and TNF-a secretion after LpA-stimulation .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "rs17250932", "type": "SequenceVariant"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: Inactivation of Sag/Rbx2/Roc2 e3 ubiquitin ligase triggers senescence and inhibits kras-induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2/Roc2", "type": "GeneOrGeneProduct"}, {"text": "e3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "kras-induced", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Carriers of HLX1 exon 1 SNP rs12141189 showed increased IL-5 ( LpA , p = 0.007 ; Ppg , p = 0.10 ) , trendwise increased IL-13 ( LpA ) , higher GM-CSF ( LpA/Ppg , p < 0.05 ) and trendwise decreased IFN-g secretion ( Derp1+LpA-stimulation , p = 0.1 ) .

Example answer:
{"entities": [{"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs12141189", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "LpA", "type": "ChemicalEntity"}, {"text": "Ppg", "type": "ChemicalEntity"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "GM-CSF", "type": "GeneOrGeneProduct"}, {"text": "LpA/Ppg", "type": "ChemicalEntity"}, {"text": "IFN-g", "type": "GeneOrGeneProduct"}, {"text": "Derp1+LpA-stimulation", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: These pro-oncogenic effects of NNK were abolished by rSLURP-1 that also upregulated RUNX3 .

## Item biored:test:776
Example input:
Sentence: We evaluated the frequency of the XRCC1 Arg399Gln substitution in patients with SLE ( n=265 ) and controls ( n=360 ) in a sample of the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results indicated that the presence of CD72- * 2 allele decreases risk for human SLE conferred by FCGR2B-232Thr , possibly by increasing the AS isoform of CD72 .

Example answer:
{"entities": [{"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FCGR2B-232Thr", "type": "GeneOrGeneProduct"}, {"text": "CD72", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our studies may confirm that the XRCC1 Arg399Gln polymorphism may increase the risk of incidence of SLE and the occurrence of some SLE manifestations .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Our studies confirmed an association of the STAT4 C ( rs7582694 ) variant with the development of SLE and occurrence of some clinical manifestations of the disease .

## Item biored:test:806
Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Most hepatocellular carcinomas ( HCC ) develop as a result of chronic liver inflammation .

Example answer:
{"entities": [{"text": "hepatocellular carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic liver inflammation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The positive reaction to colloidal iron stain ( extracellular blue accumulations in the stroma ) was detected under light microscopy .

Example answer:
{"entities": [{"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Immunofluorescent staining revealed that dystrophin is the most sensitive among the structures connecting the actin in the cardiomyocyte cytoskeleton and the extracellular matrix .

Example answer:
{"entities": [{"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "actin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Here we successfully constructed the desminopathy rat model , evaluated with conventional stains , containing hematoxylin and eosin ( HE ) , Gomori Trichrome ( MGT ) , ( PAS ) , red oil ( ORO ) , NADH-TR , SDH staining and immunohistochemistry .

Example answer:
{"entities": [{"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Renal lesions were analyzed in hematoxylin and eosin , periodic acid-Schiff , and Masson 's trichrome stains .

Example answer:
{"entities": [{"text": "Renal lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The inflammation and scaffold structure in liver were stained with hematoxylin and eosin and silver staining respectively .

## Item biored:test:719
Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An antibody against the synthetic C-terminal peptides deduced from the cDNA of the gene responsible for X-linked adrenoleukodystrophy ( ALD ) was produced to characterize the product of the ALD gene .

Example answer:
{"entities": [{"text": "X-linked adrenoleukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The major histocompatibility complex ( MHC ) on chromosome 6p21 is a key contributor to the genetic basis of systemic lupus erythematosus ( SLE ) .

Example answer:
{"entities": [{"text": "major histocompatibility complex", "type": "GeneOrGeneProduct"}, {"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We propose that a cis-acting regulatory polymorphism has arisen close to D90A-SOD1 in the recessive founder , which decreases ALS susceptibility in heterozygotes and slows disease progression .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report on a new allele at the arylsulfatase A ( ARSA ) locus causing late-onset metachromatic leukodystrophy ( MLD ) .

Example answer:
{"entities": [{"text": "arylsulfatase A", "type": "GeneOrGeneProduct"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "metachromatic leukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: D90A-SOD1 mediated amyotrophic lateral sclerosis : a single founder for all cases with evidence for a Cis-acting disease modifier in the recessive haplotype .

Example answer:
{"entities": [{"text": "D90A-SOD1", "type": "SequenceVariant"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: More than 100 different heterozygous mutations in copper/zinc superoxide dismutase ( SOD1 ) have been found in patients with amyotrophic lateral sclerosis ( ALS ) , a fatal neurodegenerative disease .

Example answer:
{"entities": [{"text": "copper/zinc superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "amyotrophic lateral sclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Sjogren-Larsson syndrome ( SLS ) is an autosomal recessive disorder characterized by ichthyosis , mental retardation , spasticity and mutations in the ALDH3A2 gene for fatty aldehyde dehydrogenase , an enzyme that catalyzes the oxidation of fatty aldehyde to fatty acid .

## Item biored:test:824
Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "extrapyramidal symptoms", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ovx significantly enhanced the hypotensive response to alpha-methyldopa , in contrast to no effect on rilmenidine hypotension .

Example answer:
{"entities": [{"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Co-administration of lidocaine , bupivacaine or tricaine with desipramine reversed this effect .

Example answer:
{"entities": [{"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "tricaine", "type": "ChemicalEntity"}, {"text": "desipramine", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : In this study population , combination therapies with VAL/HCTZ were associated with significantly greater BP reductions compared with either monotherapy , were well tolerated , and were associated with less hypokalemia than HCTZ alone .

Example answer:
{"entities": [{"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thromboxane levels were not significantly affected by any of the treatments , indicating that the effects seen were attributable to inhibition of COX-2 , but not COX-1 .

Example answer:
{"entities": [{"text": "Thromboxane", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "COX-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Randomised clinical trials and observational studies have shown an increased risk of myocardial infarction , stroke , hypertension and heart failure during treatment with cyclooxygenase inhibitors .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heart failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cyclooxygenase inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cyclooxygenase inhibitors cause complex changes in renal , vascular and cardiac prostanoid profiles thereby increasing vascular resistance and fluid retention .

Example answer:
{"entities": [{"text": "Cyclooxygenase inhibitors", "type": "ChemicalEntity"}, {"text": "prostanoid", "type": "ChemicalEntity"}]}

Input:
Sentence: However , both agents are associated with significant hemodynamic side effects .

## Item biored:test:779
Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: After restricting the candidate region in chromosome 16q22.1 by haplotype analysis , we found that all patients from 52 unrelated Japanese families harbor a heterozygous C -- > T single-nucleotide substitution , 16 nt upstream of the putative translation initiation site of the gene for a hypothetical protein DKFZP434I216 , which we have called `` puratrophin-1 '' ( Purkinje cell atrophy associated protein-1 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "C -- > T", "type": "SequenceVariant"}, {"text": "DKFZP434I216", "type": "GeneOrGeneProduct"}, {"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "Purkinje cell atrophy associated protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: We have shown that MPNSTs express neuregulin-1 ( NRG-1 ) beta isoforms , which promote Schwann cell migration during development , and NRG-1 alpha isoforms , whose effects on Schwann cells are poorly understood .

Example answer:
{"entities": [{"text": "MPNSTs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuregulin-1 ( NRG-1 ) beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our work shows that Tuba1a plays an essential , noncompensated role in neuronal saltatory migration in vivo and highlights the importance of MT flexibility in N-C coupling and neuronal-branching regulation during neuronal migration .

Example answer:
{"entities": [{"text": "Tuba1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Live imaging of Tuba1a-mutant neurons revealed slowed migration and increased neuronal branching , which correlated with directionality alterations and perturbed nucleus-centrosome ( N-C ) coupling .

Example answer:
{"entities": [{"text": "Tuba1a-mutant", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "MPTP-induced", "type": "ChemicalEntity"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DA", "type": "ChemicalEntity"}]}

Input:
Sentence: Previously , we have reported induction of neuronal pentraxin 1 ( NP1 ) , a novel neuronal protein of long-pentraxin family , following HI neuronal injury .

## Item biored:test:828
Example input:
Sentence: A retrospective study was carried out on paraffin-embedded sections from 113 patients diagnosed of advanced CRC .

Example answer:
{"entities": [{"text": "paraffin-embedded", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients with convulsive seizures had 2.5 times higher in-hospital mortality rates and twice the length of hospital stay compared with patients without convulsive seizures .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "convulsive seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Twenty-one of the 24 patients did not have evidence of new cerebral ischemic injury , but seizures were likely due to ischemic brain injury in 3 patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cerebral ischemic injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic brain injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: The most relevant adverse event was peripheral neuropathy , which occurred in 78 % of the patients ( grade II , 38 % ; grade III , 21 % ) and led to treatment discontinuation in 6 % .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: On an intention-to-treat basis , 55 % of the patients achieved at least partial response , including 19 % CR and 35 % achieved at least very good partial response .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: PATIENTS : Neurocritical care patients admitted between July 2009 and September 2012 were evaluated and then matched 1:1 based on propensity scoring of baseline characteristics .

## Item biored:test:841
Example input:
Sentence: The selected Bach1 siRNA with higher interference efficiency was used for the animal experiments .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : The first part of this study was an 8-week , multicenter , randomized , double-blind , placebo controlled , parallel-group trial .

Example answer:
{"entities": []}

Example input:
Sentence: Animals were tested for four consecutive days ( 4 trial/day ) in MWM during which the position of hidden platform was unchanged .

Example answer:
{"entities": []}

Example input:
Sentence: At the end of study period , serum phenobarbitone and carbamazepine , whole brain malondialdehyde and reduced glutathione levels were estimated .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}]}

Example input:
Sentence: Future research should include animal studies that address mechanistic hypotheses and studies of human populations that integrate early-life exposure , molecular alterations , and latent disease outcomes .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Forty-five minutes later , the animals were randomly treated with PCC ( 100 U/kg ) or saline i.v .

Example answer:
{"entities": [{"text": "PCC", "type": "ChemicalEntity"}]}

Example input:
Sentence: In vivo investigations were performed in animals .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : Data were obtained from two clinical trials : 1 ) acute Epo exposure ( rHuEpo , 400 IU/kg ) followed by WAT biopsies after 1 h and 2 ) 10 weeks treatment with the erythropoiesis-stimulating agent ( ESA ) Darbepoietin-alpha .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "erythropoiesis-stimulating agent", "type": "ChemicalEntity"}, {"text": "ESA", "type": "ChemicalEntity"}, {"text": "Darbepoietin-alpha", "type": "ChemicalEntity"}]}

Example input:
Sentence: ) , on ergometrine-induced wet dog shake ( WDS ) behavior and fluoxetine-induced penile erections was studied in rats .

Example answer:
{"entities": []}

Example input:
Sentence: Four animal groups ( n = 6 ) were tested during 9 weeks : control , CsA , SRL , and conversion ( CsA for 3 weeks followed by SRL for 6 weeks ) .

Example answer:
{"entities": [{"text": "CsA", "type": "ChemicalEntity"}, {"text": "SRL", "type": "ChemicalEntity"}]}

Input:
Sentence: The study was conducted at the Animal Experiment Laboratories , Department of Pharmacology , Medical School , Eskisehir Osmangazi University , Eskisehir , Turkey between March and May 2012 .

## Item biored:test:786
Example input:
Sentence: N-Acetylglucosamine ( O-GlcNAc ) transferase ( OGT ) regulates protein O-GlcNAcylation , an essential and dynamic post-translational modification .

Example answer:
{"entities": [{"text": "N-Acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "O-GlcNAcylation", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OPMD is caused by a short trinucleotide repeat expansion encoding an expanded polyalanine tract in the polyadenylate binding-protein nuclear 1 ( PABPN1 ) gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyalanine", "type": "ChemicalEntity"}, {"text": "polyadenylate binding-protein nuclear 1", "type": "GeneOrGeneProduct"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , apoptotic proteins are also involved in the desminopathies , like bax , ATF2 , but not bcl-2 , bcl-xl or HK2 .

Example answer:
{"entities": [{"text": "desminopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Voltage-Dependent Anion Channel 1 ( VDAC1 ) Participates the Apoptosis of the Mitochondrial Dysfunction in Desminopathy .

Example answer:
{"entities": [{"text": "Voltage-Dependent Anion Channel 1", "type": "GeneOrGeneProduct"}, {"text": "VDAC1", "type": "GeneOrGeneProduct"}, {"text": "Mitochondrial Dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Desminopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that defects in O-GlcNAc homeostasis and host cell factor 1 proteolysis may play roles in mediation of XLID in individuals with OGT mutations .

Example answer:
{"entities": [{"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OGT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Meanwhile apoptosis related proteins bax and ATF2 were involved in desminopathy patients and desminopathy rat model , but not bcl-2 , bcl-xl or HK2.VDAC1 and desmin are closely relevant in the tissue splices of deminopathies patients and rats with desminopathy at protein lever .

Example answer:
{"entities": [{"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2.VDAC1", "type": "GeneOrGeneProduct"}, {"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: NADH : ubiquinone oxidoreductase ( complex I ) of the mitochondrial respiratory chain can be fragmented in a flavoprotein ( FP ) , iron-sulfur protein ( IP ) , and hydrophobic protein ( HP ) subfraction .

Example answer:
{"entities": [{"text": "NADH : ubiquinone oxidoreductase ( complex I )", "type": "GeneOrGeneProduct"}, {"text": "flavoprotein", "type": "GeneOrGeneProduct"}, {"text": "FP", "type": "GeneOrGeneProduct"}, {"text": "iron-sulfur protein", "type": "GeneOrGeneProduct"}, {"text": "IP", "type": "GeneOrGeneProduct"}, {"text": "hydrophobic protein", "type": "GeneOrGeneProduct"}, {"text": "HP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: VDAC1 regulates mitochondrial uptake across the outer membrane and mitochondrial outer membrane permeabilization ( MOMP ) .

Example answer:
{"entities": [{"text": "VDAC1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: NP1 protein was immunoprecipitated with Bad and Bax proteins ; OGD caused increased interactions of NP1 with Bad and Bax , thereby , facilitating their mitochondrial translocation and dissipation of mitochondrial membrane potential ( D ( m ) ) .

## Item biored:test:771
Example input:
Sentence: METHODS : Four IRF5 polymorphisms were genotyped in 1488 SLE patients and 1466 controls .

Example answer:
{"entities": [{"text": "IRF5", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: XRCC1 Arg399Gln gene polymorphism and the risk of systemic lupus erythematosus in the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The OR for the 399 Gln allele in patients with SLE was 1.406 ( 95 % CI=1.111-1.779 , p=0.0045 ) .

Example answer:
{"entities": [{"text": "399 Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We evaluated the frequency of the XRCC1 Arg399Gln substitution in patients with SLE ( n=265 ) and controls ( n=360 ) in a sample of the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: There are evident population differences in the context of clinical manifestations of SLE , therefore we investigated the prevalence of the STAT4 G > C ( rs7582694 ) polymorphism in patients with SLE ( n = 253 ) and controls ( n = 521 ) in a sample of the Polish population .

## Item biored:test:774
Example input:
Sentence: Furthermore , 7 additional SNPs showed q values of < 0.5 , suggesting association with SLE and providing a direction for followup studies .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the meta-analysis of Taiwanese Han Chinese , Brazilian , and Polish populations showed that the Gln/Gln or Gln/Arg genotype and Gln allele were associated with SLE incidence .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We evaluated the frequency of the XRCC1 Arg399Gln substitution in patients with SLE ( n=265 ) and controls ( n=360 ) in a sample of the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The OR for the 399 Gln allele in patients with SLE was 1.406 ( 95 % CI=1.111-1.779 , p=0.0045 ) .

Example answer:
{"entities": [{"text": "399 Gln", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: The odds ratio ( OR ) for SLE patients with the Gln/Gln versus Gln/Arg or Arg/Arg genotypes was 1.553 ( 95 % confidence interval [ CI ] =0.9573-2.520 ; p=0.0729 ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: We also observed an increased frequency of STAT4 C/C and C/G genotypes in SLE patients with renal symptoms OR = 2.259 ( 1.365-3.738 , p = 0.0014 ) , ( p ( corr ) = 0.0238 ) and in SLE patients with neurologic manifestations OR = 2.867 ( 1.467-5.604 , p = 0.0016 ) , ( p ( corr ) = 0.0272 ) .

## Item biored:test:792
Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Memory function and serotonin transporter promoter gene polymorphism in ecstasy ( MDMA ) users .

Example answer:
{"entities": [{"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: It has been consistently shown that ecstasy users display impairments in learning and memory performance .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "impairments in learning and memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "Learning and memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results elucidated ecstasy-related deficits , only some of which might be attributed to cannabis use .

Example answer:
{"entities": [{"text": "ecstasy-related", "type": "ChemicalEntity"}, {"text": "cannabis", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RATIONALE : Ecstasy ( 3,4-methylenedioxymethamphetamine , MDMA ) is a worldwide recreational drug of abuse .

## Item biored:test:784
Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Emodin significantly downregulated the protein expression of FASN in HCT116 cells , which was caused by protein degradation due to elevated protein ubiquitination .

Example answer:
{"entities": [{"text": "Emodin", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "HCT116", "type": "CellLine"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: N-Acetylglucosamine ( O-GlcNAc ) transferase ( OGT ) regulates protein O-GlcNAcylation , an essential and dynamic post-translational modification .

Example answer:
{"entities": [{"text": "N-Acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "O-GlcNAcylation", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed slightly reduced levels of OGT protein and reduced levels of its opposing enzyme O-GlcNAcase in both patient-derived fibroblasts , but global O-GlcNAc levels appeared to be unaffected .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "O-GlcNAcase", "type": "GeneOrGeneProduct"}, {"text": "patient-derived", "type": "OrganismTaxon"}, {"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that defects in O-GlcNAc homeostasis and host cell factor 1 proteolysis may play roles in mediation of XLID in individuals with OGT mutations .

Example answer:
{"entities": [{"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OGT", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: OGD also caused a time-dependent decrease in the phosphorylation of Bad ( Ser136 ) , and Bax protein levels .

## Item biored:test:809
Example input:
Sentence: Sequence analysis of the VWF gene from two unrelated type 2A VWD patients showed an identical , novel , heterozygous T -- > G transversion at nucleotide 4508 , resulting in the substitution of L1503R in the VWF A2 domain .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "type 2A VWD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "T -- > G transversion at nucleotide 4508", "type": "SequenceVariant"}, {"text": "L1503R", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The positive reaction to colloidal iron stain ( extracellular blue accumulations in the stroma ) was detected under light microscopy .

Example answer:
{"entities": [{"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Co-transfection experiment of both wild-type and mutant plasmids indicated the dominant-negative mechanism of disease development ; as more of mutant DNA was transfected , VWF secretion was impaired in the media , whereas more of VWF was stored in the cell lysates .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: L1503R is a member of group I mutation and has dominant-negative effect on secretion of full-length VWF multimers : an analysis of two patients with type 2A von Willebrand disease .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "type 2A von Willebrand disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Vascular endothelial growth factor ( VEGF ) level was highly co-stained in endothelial cells but not in macrophages in LKB1 ( endo-/- ) mice .

Example answer:
{"entities": [{"text": "Vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: This substitution , which was not found in 60 unrelated normal individuals , was introduced into a full-length VWF cDNA and subsequently expressed in 293T cells .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: Immunofluorescence results showed that VDAC1 was accumulated in the desmin highly stained area of muscle fibers of desminopathy patients or desminopathy rat model compared to the normal ones .

Example answer:
{"entities": [{"text": "VDAC1", "type": "GeneOrGeneProduct"}, {"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Only trace amount of the mutant VWF protein was secreted but most of the same was retained in 293T cells .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Type 2A von Willebrand disease ( VWD ) is characterized by decreased platelet-dependent function of von Willebrand factor ( VWF ) ; this in turn is associated with an absence of high-molecular-weight multimers .

Example answer:
{"entities": [{"text": "Type 2A von Willebrand disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VWD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "von Willebrand factor", "type": "GeneOrGeneProduct"}, {"text": "VWF", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Expression of von Willebrand factor ( vWF ) was investigated with immunofluorescence staining .

## Item biored:test:741
Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum concentrations of CRP , neopterin and IL-6 as markers of inflammation and thrombopoietin ( TPO ) , GCSF , FGF basic and VEGF , HMGB1 , CK-18 ( M65 ) and CK18 fragment ( M30 ) and a panel of proinflammatory chemokines ( CCL2 , CCL3 , CCL4 , CCL5 , CXCL5 and IL-8 ) were measured .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "neopterin", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombopoietin", "type": "GeneOrGeneProduct"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "GCSF", "type": "GeneOrGeneProduct"}, {"text": "FGF basic", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}, {"text": "CK-18", "type": "GeneOrGeneProduct"}, {"text": "CK18", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL3", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Finally , we showed that the protein levels of MT1 increase in the serum of some HCC patients receiving sorafenib , and found an association with reduced overall survival .

Example answer:
{"entities": [{"text": "MT1", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "sorafenib", "type": "ChemicalEntity"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: No association was found between PAI-1 serum levels or 4G/5G genotype with liver fibrosis in obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: No differences were observed in PAI-1 plasma levels among obese patients with liver fibrosis ( 10.64 4.35 ) compared to patients without liver fibrosis ( 10.61 5.2 ; p = 0.985 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The aim of this study was to elucidate the relationship between serum lipid and factors that are able to predict the efficacy of PEG-IFN/RB therapy , with specific focus on apolipoprotein B-100 ( apoB-100 ) in 148 subjects with chronic HCV G1b infection .

## Item biored:test:761
Example input:
Sentence: Modulation of PKCalpha by histamine receptors may be important in regulating cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "histamine receptors", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Therefore , radiation-induced NF-kB functions as a molecular link between tumor cells and immune cells in the tumor microenvironment for radiation-mediated tumor suppression .

Example answer:
{"entities": [{"text": "NF-kB", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NRG-1 beta stimulated human and murine MPNST cell migration and invasion in a concentration-dependent manner in three-dimensional migration assays , acting as a chemotactic factor .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study was designed to evaluate the alterations in offspring rat cerebellum induced by maternal exposure to carmustine- [ 1,3-bis ( 2-chloroethyl ) -1-nitrosoure ] ( BCNU ) and to investigate the effects of exogenous melatonin upon cerebellar BCNU-induced cortical dysplasia , using histological and biochemical analyses .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "carmustine-", "type": "ChemicalEntity"}, {"text": "1,3-bis ( 2-chloroethyl ) -1-nitrosoure", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin agonist NDP-MSH dose-dependently inhibited JNK activity in HEK293 cells stably expressing the human MC4R ; effects were reversed by melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "JNK", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "MC4R", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , CBKOTg mice reduced levels of phosphorylated mitogen-activated protein kinase ( extracellular signal-regulated kinase ) 1/2 and cAMP response element-binding protein at Ser-133 and synaptic molecules such as N-methyl-D-aspartate receptor 1 ( NMDA receptor 1 ) , NMDA receptor 2A , PSD-95 and synaptophysin in the subiculum compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "extracellular signal-regulated kinase ) 1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding protein", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-D-aspartate receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 2A", "type": "GeneOrGeneProduct"}, {"text": "PSD-95", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The signal transduction target upon interleukin 1 beta ( IL1beta ) stimulation , the nuclear factor of kappa B ( NFkappaB ) activation , supports cancer development , signal transduction in which is mediated by FS-7 cell-associated cell surface antigen ( FAS ) signaling .

Example answer:
{"entities": [{"text": "interleukin 1 beta", "type": "GeneOrGeneProduct"}, {"text": "IL1beta", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor of kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FS-7 cell-associated cell surface antigen", "type": "GeneOrGeneProduct"}, {"text": "FAS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: 5-Aza-2'-deoxy-cytidine and/or Trichostatin A treatments induced DOCK8 expression in lung cancer cell lines with reduced DOCK8 expression .

Example answer:
{"entities": [{"text": "5-Aza-2'-deoxy-cytidine", "type": "ChemicalEntity"}, {"text": "Trichostatin A", "type": "ChemicalEntity"}, {"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: AIMS : To elucidate how the nicotinic acetylcholine receptors expressed on bronchial and oral epithelial cells targeted by the tobacco nitrosamine ( 4- ( methylnitrosamino ) -1- ( 3-pyridyl ) -1-butanone ) ( NNK ) facilitate carcinogenic transformation .

## Item biored:test:745
Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum levels of chemokines CCL4 and CCL5 in cirrhotic patients indicate the presence of hepatocellular carcinoma .

Example answer:
{"entities": [{"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hepatocellular carcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: Multivariate forward stepwise regression analysis for significant parameters showed that among the studied parameters CCL4 and CCL5 ( P=0.001 ) are diagnostic markers of HCC .

Example answer:
{"entities": [{"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Our results suggest that apoB-100 and LDL cholesterol are markers of impaired cellular lipoprotein pathways and/or host endogenous interferon response to HCV in chronic HCV infection .

## Item biored:test:804
Example input:
Sentence: The rats were assigned into four groups ( n=10 per group ) , as follows : Control rats ; rats+atorvastatin ; rats + iopamidol ; rats+iopamidol+atorvastatin .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rats+atorvastatin", "type": "OrganismTaxon"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "rats+iopamidol+atorvastatin", "type": "OrganismTaxon"}]}

Example input:
Sentence: Utilizing the Eu-myc mouse model , where Myc is overexpressed specifically in B cells , both basal and stimulated BCR signaling were increased in precancerous B lymphocytes from Eu-myc mice compared with wild-type littermates .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "Myc", "type": "GeneOrGeneProduct"}, {"text": "BCR", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: At puberty ( P40 ) , half the PCPA-treated rats and half the saline-treated rats began treatment with testosterone ( T , 5 mg/kg , 5 days/week ) .

Example answer:
{"entities": [{"text": "PCPA-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male CD-1 mice were treated with warfarin ( 2 mg/kg over 24 h ) , resulting in a mean ( +/-s.d . )

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Input:
Sentence: 39 male BABL/c mice were randomly divided into four groups : normal control , model control , CMCS treatment and 1,10-phenanthroline treatment groups .

## Item biored:test:783
Example input:
Sentence: We conclude that defects in O-GlcNAc homeostasis and host cell factor 1 proteolysis may play roles in mediation of XLID in individuals with OGT mutations .

Example answer:
{"entities": [{"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OGT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed slightly reduced levels of OGT protein and reduced levels of its opposing enzyme O-GlcNAcase in both patient-derived fibroblasts , but global O-GlcNAc levels appeared to be unaffected .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "O-GlcNAcase", "type": "GeneOrGeneProduct"}, {"text": "patient-derived", "type": "OrganismTaxon"}, {"text": "O-GlcNAc", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Investigations of the underlying mechanisms revealed that BDNF activated Akt and preserved phosphorylation of mammalian target of rapamycin and Bad without affecting p38 mitogen-activated protein kinase and extracellular regulated protein kinase pathways .

Example answer:
{"entities": [{"text": "mammalian target of", "type": "GeneOrGeneProduct"}, {"text": "p38 mitogen-activated protein", "type": "GeneOrGeneProduct"}, {"text": "extracellular regulated protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: N-Acetylglucosamine ( O-GlcNAc ) transferase ( OGT ) regulates protein O-GlcNAcylation , an essential and dynamic post-translational modification .

Example answer:
{"entities": [{"text": "N-Acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "O-GlcNAcylation", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , EPZ015666 restrained the phosphorylation of IkB kinaseb and IkBa , as well as nucleus transsituation of p65 as well as AKT in FLSs .

Example answer:
{"entities": [{"text": "EPZ015666", "type": "ChemicalEntity"}, {"text": "IkB kinaseb", "type": "GeneOrGeneProduct"}, {"text": "IkBa", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin agonist melanotan II increased insulin-stimulated AKT phosphorylation in the rat hypothalamus in vivo .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "melanotan II", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: NDP-MSH augmented insulin-stimulated AKT phosphorylation in vitro .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the absence of functional phosphatase and tensin homolog ( PTEN ) protein in Ishikawa cells , PKCalpha knockdown reduced Akt phosphorylation at serine 473 and concomitantly inhibited phosphorylation of the Akt target , glycogen synthase kinase-3beta ( GSK-3beta ) .

Example answer:
{"entities": [{"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "glycogen synthase kinase-3beta", "type": "GeneOrGeneProduct"}, {"text": "GSK-3beta", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We also found increased PTEN activity concurrent with OGD time-dependent ( 4-8 h ) dephosphorylation of Akt ( Ser473 ) and GSK-3b ( Ser9 ) .

## Item biored:test:781
Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , GABA content of mice hippocampus treated with GFC75 plus P400 showed an increase of 46.90 % when compared with seized mice .

Example answer:
{"entities": [{"text": "GABA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Superoxide dismutase 1 overexpression in mice abolishes maternal diabetes-induced endoplasmic reticulum stress in diabetic embryopathy .

Example answer:
{"entities": [{"text": "Superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "maternal", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "embryopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hippocampus mice treated with GFC75 plus P400 showed an increase in AChE activity ( 63.30 % ) when compared with seized mice .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , glial activation and neuroinflammation were attenuated in the hippocampi of KCa3.1-/-/APP/PS1 mice , as compared with APP/PS1 mice .

Example answer:
{"entities": [{"text": "neuroinflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCa3.1-/-/APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse embryonic fibroblasts exhibiting disruption or overexpression of IGF-1R ( R- cells and R+ cells ) were used to examine the level of apoptosis , autophagy , and production of reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: For in vivo experiments , a model of myocardial infarction ( MI ) was established using both TIEG1 KO and WT mice .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: For in vitro experiments , cardiomyocytes were isolated from both TIEG1 knockout ( KO ) and wile-type ( WT ) mice , and the apoptotic ratios were evaluated after a 48-h ischaemic insult .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: We used wild-type ( WT ) and NP1 knockout ( NP1-KO ) mouse hippocampal cultures , modeled in vitro following exposure to oxygen glucose deprivation ( OGD ) , and in vivo neonatal ( P9-10 ) mouse model of HI brain injury .

## Item biored:test:739
Example input:
Sentence: A novel apolipoprotein E mutation , ApoE Osaka ( Arg158 Pro ) , in a dyslipidemic patient with lipoprotein glomerulopathy .

Example answer:
{"entities": [{"text": "apolipoprotein E", "type": "GeneOrGeneProduct"}, {"text": "ApoE", "type": "GeneOrGeneProduct"}, {"text": "Arg158 Pro", "type": "SequenceVariant"}, {"text": "dyslipidemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "lipoprotein glomerulopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: His apoE phenotype was apoE3/2 and he had mild dyslipidemia with a mid-band on polyacrylamide gel electrophoresis .

Example answer:
{"entities": [{"text": "apoE", "type": "GeneOrGeneProduct"}, {"text": "apoE3/2", "type": "GeneOrGeneProduct"}, {"text": "dyslipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyacrylamide", "type": "ChemicalEntity"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: No association was found between PAI-1 serum levels or 4G/5G genotype with liver fibrosis in obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The polymorphism rs2234671 at position Ex2+860G > C of the CXCR1 gene causes a conservative amino acid substitution ( S276T ) .

Example answer:
{"entities": [{"text": "rs2234671", "type": "SequenceVariant"}, {"text": "Ex2+860G > C", "type": "SequenceVariant"}, {"text": "CXCR1", "type": "GeneOrGeneProduct"}, {"text": "S276T", "type": "SequenceVariant"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A known variation , 714C- > ( I238M ) , was also found in the patient with L490R .

Example answer:
{"entities": [{"text": "714C-", "type": "SequenceVariant"}, {"text": "I238M", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "L490R", "type": "SequenceVariant"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Genotype rs8099917 near the IL28B gene and amino acid substitution at position 70 in the core region of the hepatitis C virus are determinants of serum apolipoprotein B-100 concentration in chronic hepatitis C. The life cycle of the hepatitis C virus ( HCV ) is closely related to host lipoprotein metabolism .

## Item biored:test:823
Example input:
Sentence: The convulsive threshold ( mean +/- SD ) was 41.4 +/- 6.5 mg. l ( -1 ) with lidocaine infusion ( 6 mg.kg ( -1 ) .min ( -1 ) ) , increasing significantly to 66.6 +/- 10.9 mg. l ( -1 ) when the end-tidal concentration of sevoflurane was 0.8 % .

Example answer:
{"entities": [{"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "sevoflurane", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After verifying the epidural space , bupivacaine and triamcinolone diacetate were injected .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "triamcinolone diacetate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "drowsiness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Anesthesia was continued uneventfully with propofol infusion while all facilities were available to detect and treat malignant hyperthermia .

Example answer:
{"entities": [{"text": "propofol", "type": "ChemicalEntity"}, {"text": "malignant hyperthermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical examination and continued vigilance for neurologic deterioration after epidural steroid injections is important .

Example answer:
{"entities": [{"text": "neurologic deterioration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steroid", "type": "ChemicalEntity"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical trials in patients with brain metastases combining dexrazoxane and high doses of etoposide is ongoing with the aim of improving efficacy without aggravating hematologic toxicity .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "hematologic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: OBJECTIVE : Dexmedetomidine and propofol are commonly used sedatives in neurocritical care as they allow for frequent neurologic examinations .

## Item biored:test:790
Example input:
Sentence: Our findings suggest that the G51S PNP polymorphism is associated with a faster rate of cognitive decline in AD patients , highlighting the important role of purine metabolism in the progression of this neurodegenerative disorder .

Example answer:
{"entities": [{"text": "G51S", "type": "SequenceVariant"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "neurodegenerative disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The study investigates if alpha-lipoic acid is neuroprotective against chemotherapy induced neurotoxicity , if mitochondrial damage plays a critical role in toxic neurodegenerative cascade , and if neuroprotective effects of alpha-lipoic acid depend on mitochondria protection .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "toxic neurodegenerative cascade", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Inhibition of caspases , RIP1 , or RIP3 blocks radiation/TNFa-induced cell death , whereas inhibition of RIP1 blocks TNFa-induced caspase activation , suggesting that caspases and RIP1 act sequentially to mediate the non-compensatory cell death pathways .

Example answer:
{"entities": [{"text": "caspases", "type": "GeneOrGeneProduct"}, {"text": "RIP1", "type": "GeneOrGeneProduct"}, {"text": "RIP3", "type": "GeneOrGeneProduct"}, {"text": "TNFa-induced", "type": "GeneOrGeneProduct"}, {"text": "caspase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our work shows that Tuba1a plays an essential , noncompensated role in neuronal saltatory migration in vivo and highlights the importance of MT flexibility in N-C coupling and neuronal-branching regulation during neuronal migration .

Example answer:
{"entities": [{"text": "Tuba1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Insulin-like growth factor 1 receptor-mediated cell survival in hypoxia depends on the promotion of autophagy via suppression of the PI3K/Akt/mTOR signaling pathway .

Example answer:
{"entities": [{"text": "Insulin-like growth factor 1", "type": "GeneOrGeneProduct"}, {"text": "hypoxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PI3K/Akt/mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we identify Brain Tumor ( Brat ) as a potent differentiation factor and target of Pum-Nos regulation .

Example answer:
{"entities": [{"text": "Brain Tumor", "type": "GeneOrGeneProduct"}, {"text": "Brat", "type": "GeneOrGeneProduct"}, {"text": "Pum-Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate that induction of HIF-1a mediated transcriptional up-regulation of pro-apoptotic/inflammatory signaling contributes to astrocyte cell death during thiamine deficiency .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "thiamine deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Overall , these results suggest that KCa3.1 is involved in the regulation of Ca2+ homeostasis in astrocytes and attenuation of the UPR and ER stress , thus contributing to memory deficits and neuronal loss .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , glial activation and neuroinflammation were attenuated in the hippocampi of KCa3.1-/-/APP/PS1 mice , as compared with APP/PS1 mice .

Example answer:
{"entities": [{"text": "neuroinflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCa3.1-/-/APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , MT induction halts BCNU-induced hippocampal toxicity as it prevented GR inhibition and GSH depletion and counteracted the increased levels of TNFalpha , MDA and caspase-3 activity with subsequent preservation of cognition .

Example answer:
{"entities": [{"text": "MT", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Together our findings demonstrate a novel mechanism by which NP1 regulates mitochondria-driven hippocampal cell death ; suggesting NP1 as a potential therapeutic target against HI brain injury in neonates .
