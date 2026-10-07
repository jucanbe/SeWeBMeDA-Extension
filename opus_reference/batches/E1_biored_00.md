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
Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: Four ultraconserved regions distal to ARX ( uc466-469 ) were also screened in a subset of 94 patients , with three unique nucleotide changes identified in two ( uc466 , uc467 ) .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: The 3 ' untranslated regions ( UTR ) are complete in all three cDNAs .

Example answer:
{"entities": []}

Example input:
Sentence: The AS isoform lacks exon 8 , and is deduced to contain 49 amino acid changes in the membrane-distal portion of the extracellular domain , where considerable amino acid changes are known in CD72 ( c ) allele associated with murine SLE .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three microdeletions were also identified , two of which ( c.611delG and c.640_667del28 ) were located within the coding region whereas one ( c.609+28_610-16del ) was located entirely within intron 8 .

Example answer:
{"entities": [{"text": "c.611delG", "type": "SequenceVariant"}, {"text": "c.640_667del28", "type": "SequenceVariant"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}]}

Example input:
Sentence: the skipping of exon 9 ( p.G204_K247del ) or the retention of introns 8 and 9 ( p.G204VfsX28 ) .

Example answer:
{"entities": [{"text": "p.G204_K247del", "type": "SequenceVariant"}, {"text": "p.G204VfsX28", "type": "SequenceVariant"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Three aberrantly spliced cDNA species were identified : exon 22 and exon 22 to 23 skipping , and insertion of an 87-base pair cryptic exon .

Example answer:
{"entities": []}

Example input:
Sentence: Exons 1-8 of the AR gene and exons 1-5 of the SRD5A2 gene were sequenced from peripheral blood DNA .

Example answer:
{"entities": [{"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This region includes the last five exons detected by cDNA5b-7 , all exons detected by cDNA8 , and the first two exons detected by cDNA9 .

## Item biored:test:12
Example input:
Sentence: the skipping of exon 9 ( p.G204_K247del ) or the retention of introns 8 and 9 ( p.G204VfsX28 ) .

Example answer:
{"entities": [{"text": "p.G204_K247del", "type": "SequenceVariant"}, {"text": "p.G204VfsX28", "type": "SequenceVariant"}]}

Example input:
Sentence: An 18 kb genomic clone hybridizing with the h mu OR1 cDNA contains 63 and 489 bp exonic sequences flanked by splice donor/acceptor sequences .

Example answer:
{"entities": [{"text": "h mu OR1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Structure-function studies and in silico analyses provided the first experimental evidence of an indel of a stop codon by alternative splicing at a NAGNAG acceptor site .

Example answer:
{"entities": []}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Input:
Sentence: ( ABSTRACT TRUNCATED AT 250 WORDS )

## Item biored:test:22
Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Similarly , NF1 alterations including homozygous deletions and splicing mutations were identified in 9 ( 22 % ) of 41 primary OSCs .

Example answer:
{"entities": [{"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: This frameshift mutation leads to a caveolin-1 protein that contains all known functional domains but has a change in only the final 20 amino acids of the C-terminus .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The most common type of mutation is missense ( 57 % ) , followed by frameshifts & nonsense ( 27 % ) , and diverse deletions , insertions and duplications .

Example answer:
{"entities": []}

Example input:
Sentence: The identification of around 7 % of homozygotes for the frameshift mutation in our Caucasian population suggests the existence of an interindividual variation of the CYP2F1 activity and , consequently , the possibility of interindividual differences in the toxic response to some pneumotoxicants and in the susceptibility to certain chemically induced diseases .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: We found a single nucleotide deletion c.342delA , located in exon 3 , which resulted in a frameshift at amino acid position 58 ( p.Arg58fs or p.R58fs ) .

Example answer:
{"entities": [{"text": "c.342delA", "type": "SequenceVariant"}, {"text": "p.Arg58fs", "type": "SequenceVariant"}, {"text": "p.R58fs", "type": "SequenceVariant"}]}

Example input:
Sentence: The frameshift caused by the c.1052delA deletion removes the last 81 amino acids of the protein , including the third zinc-finger motif .

Example answer:
{"entities": [{"text": "c.1052delA", "type": "SequenceVariant"}]}

Input:
Sentence: Thus , with two exceptions , frameshift deletions of the gene resulted in more severe phenotype than did in-frame deletions .

## Item biored:test:24
Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A Kruskal-Wallis 1-way analysis of variance indicated a significant difference among the 4 treatment groups ( H = 15.34 ; P < 0.001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SOX2 and NANOG expression did not change following ETO treatment suggesting a dissociation of OCT4A from its pluripotency function .

Example answer:
{"entities": [{"text": "SOX2", "type": "GeneOrGeneProduct"}, {"text": "NANOG", "type": "GeneOrGeneProduct"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: For in vitro experiments , cardiomyocytes were isolated from both TIEG1 knockout ( KO ) and wile-type ( WT ) mice , and the apoptotic ratios were evaluated after a 48-h ischaemic insult .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cardona et al .

Example answer:
{"entities": []}

Example input:
Sentence: In addition to contributing to proteome plasticity , alternative splicing at a NAGNAG tandem site can thus remove a disease-causing UAG stop codon .

Example answer:
{"entities": []}

Input:
Sentence: and Koenig et al .

## Item biored:test:25
Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , affected males display facial similarities that can help the diagnosis .

Example answer:
{"entities": []}

Example input:
Sentence: In contrast , such extensive lesions were never found in the PCC group .

Example answer:
{"entities": [{"text": "PCC", "type": "ChemicalEntity"}]}

Example input:
Sentence: It could be proved by the observation of a positive stain reaction and the enlarged collagen fibers as well as hyperplastic fibroblasts under microscopes .

Example answer:
{"entities": [{"text": "collagen", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Studies of additional cases yielded a second set of data that , in combination with the first set , confirmed a weak association of UP III SNP7 in VUR ( P= 0.036 adjusted for both subsets of cases vs. controls ) .

Example answer:
{"entities": [{"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast to controls , methoctramine increased -- instead of decreased -- the tonic responses at high frequencies .

Example answer:
{"entities": [{"text": "methoctramine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Hallmarks of constitutive activity were all reversed by a specific PrlR antagonist , which opens potential therapeutic approaches for MFA , or any other disease that could be associated with this mutation in future .

Example answer:
{"entities": [{"text": "PrlR antagonist", "type": "ChemicalEntity"}, {"text": "MFA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This observation is in contrast with results from two previous studies conducted in the USA and Japan .

Example answer:
{"entities": []}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Input:
Sentence: but is in contrast to findings , by Malhotra et al .

## Item biored:test:26
Example input:
Sentence: Genomic DNA was extracted from peripheral blood of 11 family members , and the coding region of CHST6 was amplified by the polymerase chain reaction ( PCR ) method .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: We found a single nucleotide deletion c.342delA , located in exon 3 , which resulted in a frameshift at amino acid position 58 ( p.Arg58fs or p.R58fs ) .

Example answer:
{"entities": [{"text": "c.342delA", "type": "SequenceVariant"}, {"text": "p.Arg58fs", "type": "SequenceVariant"}, {"text": "p.R58fs", "type": "SequenceVariant"}]}

Example input:
Sentence: The genes presented represent ( 1 ) greater than 1.5-fold change in either direction and ( 2 ) the p value is less than 0.05 for the comparison being made .

Example answer:
{"entities": []}

Example input:
Sentence: Recombination has reduced the region shared by recessive kindreds to 97-265 kb around SOD1 , excluding all neighbouring genes .

Example answer:
{"entities": [{"text": "SOD1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: The paternal mutation is a G -- > A transition located at the 5 ' donor splice site within intron 51 , designated IVS51 + 1G -- > A .

Example answer:
{"entities": [{"text": "G -- > A", "type": "SequenceVariant"}, {"text": "IVS51 + 1G -- > A", "type": "SequenceVariant"}]}

Example input:
Sentence: Exons 1-8 of the AR gene and exons 1-5 of the SRD5A2 gene were sequenced from peripheral blood DNA .

Example answer:
{"entities": [{"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: at the 5 ' end of the gene .

## Item biored:test:23
Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Also , this effect was nullified by Noggin .

Example answer:
{"entities": [{"text": "Noggin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : LOH was found in conjunction with tumor formation in 72.9 % of RB patients ( 39/54 patients ; p=0.001 ; 95 % CI 0.6028 , 0.8417 ) ; however , we could not associate various other clinical parameters of RB patients with the presence or absence of RB1 LOH .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "RB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The fixed effects also correct for nonindependence of data between populations and results in even further shrinkage of individual patient estimates .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Studies of additional cases yielded a second set of data that , in combination with the first set , confirmed a weak association of UP III SNP7 in VUR ( P= 0.036 adjusted for both subsets of cases vs. controls ) .

Example answer:
{"entities": [{"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

Example answer:
{"entities": []}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: This is in agreement with recent findings by Baumbach et al .

## Item biored:test:49
Example input:
Sentence: Expression analysis on a cDNA panel from 17 different normal tissues by reverse transcription-PCR ( RT-PCR ) revealed tissue restricted mRNA expression of 2 of the 27 unknown antigens .

Example answer:
{"entities": []}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Approximately 30 % of alleles causing genetic disorders generate premature termination codons ( PTCs ) , which are usually associated with severe phenotypes .

Example answer:
{"entities": []}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: RT-PCR identified a novel alternatively spliced ( AS ) transcript that was expressed at the protein level in COS-7 transfectants .

Example answer:
{"entities": [{"text": "COS-7", "type": "CellLine"}]}

Example input:
Sentence: Analysis of PTPN22 transcripts from a subject heterozygous for this variant indicated that it interfered with normal mRNA splicing , resulting in a premature termination codon after exon 17 .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This mutation leads to the activation of a cryptic splice site , 32 bp downstream of the mutation site and to subsequent aberrant out-of-frame splicing , resulting in two alternative mRNA transcripts and a downstream PTC .

Example answer:
{"entities": []}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Input:
Sentence: Reverse transcription-PCR revealed that a large proportion of the mutant transcripts were spliced aberrantly , causing premature termination of the protein synthesis .

## Item biored:test:48
Example input:
Sentence: The reported mutation associated with SIDDT ( 457_458insG ) was not detectable in our cohort .

Example answer:
{"entities": [{"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "457_458insG", "type": "SequenceVariant"}]}

Example input:
Sentence: The R47W mutation dramatically reduced DNA binding suggesting that the mutant protein with consequent haploinsufficiency results in a clinical phenotype .

Example answer:
{"entities": [{"text": "R47W", "type": "SequenceVariant"}]}

Example input:
Sentence: In addition , mutation of arginine 124-to-cysteine ( Arg124Cys ) was found in 8 of 18 patients and histidine 626-to-arginine ( His626Arg ) in 2 of 18 patients .

Example answer:
{"entities": [{"text": "arginine 124-to-cysteine", "type": "SequenceVariant"}, {"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "histidine 626-to-arginine", "type": "SequenceVariant"}, {"text": "His626Arg", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutations were found in 35 ( 53 % ) of the 66 families studied .

Example answer:
{"entities": []}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We detected 24 p53 mutations in 15/25 ( 60 % ) NMSCs , 1 deletion and 23 base substitutions , the majority ( 78 % ) being UV-specific C to T transitions at bipyrimidine sites .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "NMSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C to T", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation , designated p.E300X , was not detected in DNA from either parent or in 100 control chromosomes .

Example answer:
{"entities": [{"text": "p.E300X", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutations were confirmed by screening at least 100 unrelated normal control subjects .

Example answer:
{"entities": []}

Example input:
Sentence: The missense mutation ( c.920T > G ) was not found in 100 healthy controls and has not been reported previously .

Example answer:
{"entities": [{"text": "c.920T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: These two mutations were not detected in any of the 100 control subjects .

Example answer:
{"entities": []}

Input:
Sentence: This mutation was not found in 50 controls .

## Item biored:test:64
Example input:
Sentence: METHODS : Six affected family members were examined clinically including visual acuity , color cornea photography , applanation tonography , and fundoscopy .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : Serum and DNA samples from the proband and his parents were analyzed .

Example answer:
{"entities": []}

Example input:
Sentence: MATERIALS AND METHODS : The patients were examined using standard ophthalmic techniques .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Data were adjusted for sex , age , migraine history and family history , and analyzed using a logistic regression model .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : Six unrelated families and 10 sporadic patients were examined clinically .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Twenty-four members of the family were clinically examined and genomic DNA was extracted .

Example answer:
{"entities": []}

Example input:
Sentence: MATERIAL AND METHODS : This study was performed based on anesthesia records .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Blood sampling , karyotype , hormonal dosage , ultrasound , and ovarian biopsy were carried out on most patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The clinical diagnoses were based on chart review , and developmental and treatment history was obtained from the medical record .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : All individuals in the study underwent a full clinical examination and the details of history were collected .

Example answer:
{"entities": []}

Input:
Sentence: METHODS : Family history and clinical data were recorded .

## Item biored:test:68
Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutation screening of all exons of the PAX6 gene was performed by direct sequencing of PCR-amplified DNA fragments .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: GENETIC ANALYSIS : Genomic DNA was extracted from peripheral blood leukocytes and mutation analysis of the entire coding sequence of the TSHR gene was performed in both children and their parents by direct DNA sequencing .

Example answer:
{"entities": [{"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA samples were obtained and genetic linkage was carried out using polymorphic markers flanking the known genes and loci for LCA .

Example answer:
{"entities": [{"text": "LCA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Direct sequencing was used for mutation analysis .

Example answer:
{"entities": []}

Example input:
Sentence: To identify a gene for MC , we performed linkage analysis with high-density SNP arrays in a single family , used a targeted array to capture exons and promoter sequences from the linked interval in 16 participants from 11 MC families , and sequenced the captured DNA using high-throughput parallel sequencing technologies .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Linkage analysis was performed , and candidate genes were PCR amplified and screened for mutations on both strands using direct sequencing .

## Item biored:test:65
Example input:
Sentence: The R47W mutation dramatically reduced DNA binding suggesting that the mutant protein with consequent haploinsufficiency results in a clinical phenotype .

Example answer:
{"entities": [{"text": "R47W", "type": "SequenceVariant"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In summary , our findings demonstrate for the first time that mutations in PQBP1 are associated with an S-XLMR phenotype including microphthalmia , thereby further extending the clinical spectrum of phenotypes associated with PQBP1 mutations .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Our findings further confirmed that different kind of mutations might cause different ocular phenotype , and clearly clinical phenotype classification might increase the mutation detection rate of the PAX6 gene .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The phenotype was documented by both slit lamp and Scheimpflug photography .

## Item biored:test:66
Example input:
Sentence: Immunoelectron microscopy further revealed an increased labeling of alpha-ENaC in the apical plasma membrane of cortical collecting duct principal cells of PAN-treated rats , indicating enhanced apical targeting of alpha-ENaC subunits .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "PAN-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The murine lens and cornea have a common embryonic origin and arise from adjacent regions of the surface ectoderm .

Example answer:
{"entities": [{"text": "murine", "type": "OrganismTaxon"}]}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Six affected family members were examined clinically including visual acuity , color cornea photography , applanation tonography , and fundoscopy .

Example answer:
{"entities": []}

Example input:
Sentence: OBJECTIVE : This is to present reversible inferior colliculus lesions in metronidazole-induced encephalopathy , to focus on the diffusion-weighted imaging ( DWI ) and fluid attenuated inversion recovery ( FLAIR ) imaging .

Example answer:
{"entities": [{"text": "inferior colliculus lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metronidazole-induced", "type": "ChemicalEntity"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The positive reaction to colloidal iron stain ( extracellular blue accumulations in the stroma ) was detected under light microscopy .

Example answer:
{"entities": [{"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immuno/histochemistry and electron microscopy were carried out on the offspring cerebellum , and levels of malondialdehyde and superoxide dismutase were determined .

Example answer:
{"entities": [{"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Transmission electron microscopy revealed the enlargement of smooth endoplasmic reticulum and the presence of intracytoplasmic vacuoles .

Example answer:
{"entities": []}

Input:
Sentence: One cortical lens was evaluated by electron microscopy after cataract extraction .

## Item biored:test:67
Example input:
Sentence: Despite the application of this high-throughput genotyping method , negative results from the two-stage DNA pooling design used to screen loci within the TPH , AADC and MAOA genes did not support their role in migraine susceptibility .

Example answer:
{"entities": [{"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: We then examined them on genomic DNA in six MODY probands without mutations in the MODY1 , MODY3 and MODY4 genes and in 54 patients with late-onset Type II diabetes by combined single strand conformational polymorphism-heteroduplex analysis followed by direct sequencing of identified variants .

Example answer:
{"entities": [{"text": ",", "type": "GeneOrGeneProduct"}, {"text": "II diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: For this purpose we developed a high-throughput methodology to genotype both normal and deleted alleles using a chip-based matrix-assisted laser desorption-time-of-flight ( MALDI-TOF ) mass spectrometer and Multiplex PCR .

Example answer:
{"entities": []}

Example input:
Sentence: Genotyping was performed by kinetic polymerase chain-reaction or TaqMan assays .

Example answer:
{"entities": []}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The phenotype co-segregates with short-tandem repeat markers flanking the TMC1 gene at the DFNA36 locus on chromosome 9q31-q21 .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotyping was determined by the polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) technique .

Example answer:
{"entities": []}

Input:
Sentence: Lenticular phenotyping and genotyping were performed independently with short tandem repeat polymorphism .

## Item biored:test:70
Example input:
Sentence: We observed strong linkage disequilibrium between the T allele at -511 and the C allele at -31 and between the C allele at -511 and the T allele at -31 in IL1B in both the cases and controls ( R ( 2 ) =0.94 ) .

Example answer:
{"entities": [{"text": "T allele at -511", "type": "SequenceVariant"}, {"text": "C allele at -31", "type": "SequenceVariant"}, {"text": "C allele at -511", "type": "SequenceVariant"}, {"text": "T allele at -31", "type": "SequenceVariant"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction performed with DNA isolated from somatic human-rodent cell hybrids containing defined human chromosomes as template gave a human-specific signal which mapped the NDUFS2 and NDUFS3 subunits to chromosomes 1 and 11 , respectively .

Example answer:
{"entities": [{"text": "human-rodent", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "human-specific", "type": "OrganismTaxon"}, {"text": "NDUFS2", "type": "GeneOrGeneProduct"}, {"text": "NDUFS3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A homozygous deletion of the DOCK8 ( dedicator of cytokinesis 8 ) locus at chromosome 9p24 was found in a lung cancer cell line by array-CGH analysis .

Example answer:
{"entities": [{"text": "DOCK8", "type": "GeneOrGeneProduct"}, {"text": "dedicator of cytokinesis 8", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The phenotype co-segregates with short-tandem repeat markers flanking the TMC1 gene at the DFNA36 locus on chromosome 9q31-q21 .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , sequencing of our two chromosome 12-linked bipolar-Darier families showed no evidence of rare variants at P2RX7 that could explain the linkage .

Example answer:
{"entities": [{"text": "P2RX7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Multipoint analysis revealed a 4 cM region encompassing D13S1300 to D13S1280 where the LOD remains just over 6.0 Thus we confirm localization of the congenital microcoria locus to chromosomal locus 13q31-q32 .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Linkage disequilibrium analysis indicates that D90A homozygotes and heterozygotes share a rare haplotype and are all descended from a single ancient founder ( alpha 0.974 ) c.895 generations ago .

Example answer:
{"entities": [{"text": "D90A", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Two additional loci displayed an evidence of linkage ( LOD > 3 ) and included a locus on 16p13 , proximal to the gene encoding NDE1 , which has been shown to biologically interact with DISC1 .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "DISC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Linkage was obtained to 1q31.3 with a maximal LOD score of 5.20 and a mutation found in exon 9 of the CRB1 gene , causing a G1103R substitution at a highly conserved site in the protein .

Example answer:
{"entities": [{"text": "CRB1", "type": "GeneOrGeneProduct"}, {"text": "G1103R", "type": "SequenceVariant"}]}

Input:
Sentence: Linkage was observed on chromosome 17 for DNA marker D17S1857 ( lod score : 3.44 at theta = 0 ) .

## Item biored:test:73
Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The positive reaction to colloidal iron stain ( extracellular blue accumulations in the stroma ) was detected under light microscopy .

Example answer:
{"entities": [{"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Striatal microglia expressing eGFP constitutively show morphological changes after METH that are characteristic of activation .

Example answer:
{"entities": [{"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}]}

Example input:
Sentence: Transmission electron microscopy showed that fibroblasts carrying the c.474delA mutation form typical caveolae .

Example answer:
{"entities": [{"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: The murine lens and cornea have a common embryonic origin and arise from adjacent regions of the surface ectoderm .

Example answer:
{"entities": [{"text": "murine", "type": "OrganismTaxon"}]}

Example input:
Sentence: It could be proved by the observation of a positive stain reaction and the enlarged collagen fibers as well as hyperplastic fibroblasts under microscopes .

Example answer:
{"entities": [{"text": "collagen", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immuno/histochemistry and electron microscopy were carried out on the offspring cerebellum , and levels of malondialdehyde and superoxide dismutase were determined .

Example answer:
{"entities": [{"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Histopathologically , typical findings were observed in the cerebella from the control groups , but the findings consistent with early embryonic development were noted in BCNU-exposed cortical dysplasia group .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "cortical dysplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transmission electron microscopy revealed the enlargement of smooth endoplasmic reticulum and the presence of intracytoplasmic vacuoles .

Example answer:
{"entities": []}

Input:
Sentence: Electron microscopy showed that cortical lens fiber morphology was normal .

## Item biored:test:76
Example input:
Sentence: RESULTS : Direct sequencing of the encoding regions of the candidate genes revealed a heterozygous mutation c.592C -- > T in exon 2 of the gap junction protein , alpha 8 ( GJA8 ) gene .

Example answer:
{"entities": [{"text": "c.592C -- > T", "type": "SequenceVariant"}, {"text": "gap junction protein , alpha 8", "type": "GeneOrGeneProduct"}, {"text": "GJA8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Subgroup analysis shows a higher incidence of the heterozygous ArgGly genotype in cancer cases than in the combined group of BPH and controls ( P < 0.05 ) ; this difference is statistically significant between cancer and BPH patients but not between cancer cases and community controls .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The demonstration of mutations giving rise to a slightly milder phenotype in A-T raises the interesting question of what range of phenotypes might occur in individuals in whom both mutations are milder .

Example answer:
{"entities": [{"text": "A-T", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We therefore conclude that TBX1 gain-of-function mutations can result in the same phenotypic spectrum as haploinsufficiency caused by loss-of-function mutations or deletions .

Example answer:
{"entities": [{"text": "TBX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Our findings further confirmed that different kind of mutations might cause different ocular phenotype , and clearly clinical phenotype classification might increase the mutation detection rate of the PAX6 gene .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using PCR-RFLP , we confirmed the heterozygous mutation in six affected family members and excluded it in three healthy members .

Example answer:
{"entities": []}

Example input:
Sentence: This heterozygous phenotype illustrates that subtle changes in receptor tyrosine kinase signalling can have significant effects , perhaps providing an explanation for the numerous changes seen in cancer .

Example answer:
{"entities": [{"text": "receptor tyrosine kinase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Similarly , protein mislocalization of the homeodomain mutations also correlated with clinical severity , suggesting an emerging genotype vs cellular phenotype correlation .

Example answer:
{"entities": []}

Example input:
Sentence: These findings extend the body of evidence for compound heterozygous mutations leading to HS-RDEB and provide the basis for prenatal diagnosis in this family .

Example answer:
{"entities": [{"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The result of PCR associated with restriction fragment length polymorphism analysis also suggested that this mutation is heterozygous .

Example answer:
{"entities": []}

Input:
Sentence: These results indicate phenotypic heterogeneity related to mutations in this gene .

## Item biored:test:7
Example input:
Sentence: Serotonin was depleted beginning on postnatal day 26 with parachlorophenylalanine ( PCPA 100 mg/kg , every other day ) ; controls received saline .

Example answer:
{"entities": [{"text": "Serotonin", "type": "ChemicalEntity"}, {"text": "parachlorophenylalanine", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Instead , oral administration of S-1 ( a derivative of 5-FU ) , at 200 mg/day twice a week , was instituted , because S-1 has a strong inhibitory effect on dihydropyrimidine dehydrogenase , which catalyzes the degradative of 5-FU into FBAL .

Example answer:
{"entities": [{"text": "S-1", "type": "ChemicalEntity"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "dihydropyrimidine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: Severe cardiovascular complications occurred in eight of 160 patients treated with terbutaline for preterm labor .

Example answer:
{"entities": [{"text": "cardiovascular complications", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "terbutaline", "type": "ChemicalEntity"}, {"text": "preterm labor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Methadone dose was associated with longer QT interval of 0.140 ms/mg ( p = 0.002 ) .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "longer QT interval", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}]}

Example input:
Sentence: All active treatments were associated with significantly reduced MSSBP and MSDBP during the core 8-week study , with each monotherapy significantly contributing to the overall effect of combination therapy ( VAL and HCTZ , P < 0.001 ) .

Example answer:
{"entities": [{"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: hiPS-CMs were seeded onto MEA and FPD was measured for 2min every 10min for 30min after drug exposure for the vehicle and each drug concentration .

Example answer:
{"entities": []}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Input:
Sentence: Five PMs were studied according to the same protocol , except for a higher terbutaline dose ( 0.75 mg ) on day 2 .

## Item biored:test:19
Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinical phenotype shows considerable variation between individuals , such as bleeding , platelet count and the percentage of large platelets .

Example answer:
{"entities": [{"text": "bleeding", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We show that the less severe phenotype in these patients is caused by some degree of normal splicing , which occurs as an alternative product from the insertion-containing allele .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: A Stratified analysis of the genotypes with age of onset and tumor grade showed the w1/m1 genotype to be significantly associated with an early age of onset ; however the tumor grades did not have significant association with the variant genotypes .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: C_6+/6+ and G_6+/6+ combined genotypes were respectively associated to the best and worst PFS ( P=0.03 when compared with each other ) , while combinations carrying the allele 6- determined an intermediate evolution that might be indicative of a variable response to chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: Similarly , protein mislocalization of the homeodomain mutations also correlated with clinical severity , suggesting an emerging genotype vs cellular phenotype correlation .

Example answer:
{"entities": []}

Example input:
Sentence: An increased representation of the PNP AA genotype was observed in AD patients with fast cognitive deterioration in comparison with that from patients with slow deterioration rate .

Example answer:
{"entities": [{"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive deterioration", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings are useful in understanding the prevalence of GATA4 mutations and the correlation between the GATA4 genotype and the CHD phenotype in Chinese patients .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Clinical findings are presented for all 80 patients allowing a correlation of phenotypic severity with the genotype .

## Item biored:test:34
Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Memory retrieval of experiences acquired prior to cocaine administration was impaired and negatively correlated with NFkappaB activity in the frontal cortex .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Therefore NFkappaB activity , oxidative stress , neuronal nitric oxide synthase ( nNOS ) activity , spatial learning and memory as well as the effect of topiramate , a previously proposed therapy for cocaine addiction , were evaluated in an experimental model of cocaine administration in rats .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "neuronal nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}, {"text": "topiramate", "type": "ChemicalEntity"}, {"text": "cocaine addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NIMO attenuated the disruption in consolidation of long-term memory caused by NTG but did not improve latency in the absence of hypotension .

Example answer:
{"entities": [{"text": "NIMO", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: It is suggested that nefiracetam augments molecular processes in the early stages of events which ultimately lead to consolidation of memory .

## Item biored:test:46
Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : There were no mutations in the HFE gene .

Example answer:
{"entities": [{"text": "HFE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The mutation was identified in a 22-year-old French woman coming to medical attention because of an increasing overweight .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "overweight", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , mutation of arginine 124-to-cysteine ( Arg124Cys ) was found in 8 of 18 patients and histidine 626-to-arginine ( His626Arg ) in 2 of 18 patients .

Example answer:
{"entities": [{"text": "arginine 124-to-cysteine", "type": "SequenceVariant"}, {"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "histidine 626-to-arginine", "type": "SequenceVariant"}, {"text": "His626Arg", "type": "SequenceVariant"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : While mutations were absent in non-GH-secreting adenoma patients , germline AIP mutations can be found in children and adolescents with GH-secreting tumours , even in the absence of family history .

Example answer:
{"entities": [{"text": "adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "GH-secreting tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: No mutations were found in 76 male patients .

## Item biored:test:37
Example input:
Sentence: The purpose of this review was to perform a retrospective analysis to examine whether there was a relation between TXA usage and seizures after cardiac surgery .

Example answer:
{"entities": [{"text": "TXA", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : In 2 separate centers , we observed a notable increase in the incidence of postoperative convulsive seizures from 1.3 % to 3.8 % in patients having undergone major cardiac surgical procedures .

Example answer:
{"entities": [{"text": "convulsive seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Convulsive seizures are a serious postoperative complication after cardiac surgery .

Example answer:
{"entities": [{"text": "Convulsive seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "postoperative complication", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All 24 patients with seizures received high doses of TXA intraoperatively ranging from 61 to 259 mg/kg , had a mean age of 69.9 years , and 21 of 24 had undergone open chamber rather than coronary bypass procedures .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TXA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Independent predictors of postoperative seizures included age , female sex , redo cardiac surgery , calcification of ascending aorta , congestive heart failure , deep hypothermic circulatory arrest , duration of aortic cross-clamp and tranexamic acid .

Example answer:
{"entities": [{"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "calcification of ascending aorta", "type": "DiseaseOrPhenotypicFeature"}, {"text": "congestive heart failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypothermic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tranexamic acid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because of a lack of contemporary data regarding seizures after cardiac surgery , we undertook a retrospective analysis of prospectively collected data from 11 529 patients in whom cardiopulmonary bypass was used from January 2004 to December 2010 .

Example answer:
{"entities": [{"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : An in-depth chart review was undertaken in all 24 patients who developed perioperative seizures .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A total of 100 ( 0.9 % ) patients developed postoperative convulsive seizures .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "convulsive seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The median ( IQR [ range ] ) time after surgery when the seizure occurred was 7 ( 6-12 [ 1-216 ] ) h and 8 ( 6-11 [ 4-18 ] ) h , respectively .

Example answer:
{"entities": [{"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Twenty-three h postoperatively he developed a brief self-limited seizure .

## Item biored:test:39
Example input:
Sentence: The most common adverse events and median CD4 at time of event were rash ( 15.2 % ; CD4 , 285 cells/microL ) and peripheral neuropathy ( 9.0 % and 348 cells/microL ) .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "rash", "type": "DiseaseOrPhenotypicFeature"}, {"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The most relevant adverse event was peripheral neuropathy , which occurred in 78 % of the patients ( grade II , 38 % ; grade III , 21 % ) and led to treatment discontinuation in 6 % .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND AND PURPOSE : Cerebral microbleeds ( MB ) are potential risk factors for intracerebral hemorrhage ( ICH ) , but it is unclear if they are a contraindication to using antithrombotic drugs .

Example answer:
{"entities": [{"text": "Cerebral microbleeds", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antithrombotic drugs", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude from these studies that CX3CR1 signaling does not modulate METH neurotoxicity or microglial activation .

Example answer:
{"entities": [{"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Input:
Sentence: No other risk factors for CNS toxicity were identified .

## Item biored:test:85
Example input:
Sentence: After adjusting for potential confounders , we found that the risk of HIV seroconversion among participants who were daily smokers of crack cocaine increased over time ( period 1 : hazard ratio [ HR ] 1.03 , 95 % confidence interval [ CI ] 0.57-1.85 ; period 2 : HR 1.68 , 95 % CI 1.01-2.80 ; and period 3 : HR 2.74 , 95 % CI 1.06-7.11 ) .

Example answer:
{"entities": [{"text": "HIV seroconversion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crack cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Lifelong administration of vitamin E to Hp 2-2 DM individuals in the Kaiser population would increase their life expectancy by 3 years .

Example answer:
{"entities": [{"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With a median follow up of 22 months , median time to progression , progression-free survival ( PFS ) and overall survival ( OS ) were 8.9 , 8.7 , and 22 months , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The mean +/- SD duration of treatment with the identified atypical antipsychotic agent was 68.3 +/- 28.9 months ( clozapine ) , 29.5 +/- 17.5 months ( olanzapine ) , and 40.9 +/- 33.7 ( risperidone ) .

Example answer:
{"entities": [{"text": "antipsychotic agent", "type": "ChemicalEntity"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Extended follow-up studies of up to 8 years have demonstrated long-term persistence of apomorphine efficacy .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The hazard of developing CAD ( 95 % CI ) associated with initial treatment increased by 2.4-fold ( 1.3-4.3 , P=0.004 ) with glibenclamide ; 2-fold ( 0.9-4.6 , P=0.099 ) with glipizide ; 2.9-fold ( 1.6-5.1 , P=0.000 ) with either , and was unchanged with metformin .

Example answer:
{"entities": [{"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glibenclamide", "type": "ChemicalEntity"}, {"text": "glipizide", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Median durations of response , time to next therapy and treatment-free interval were 8 , 11.2 , and 5.1 months , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: These results suggest that , despite a known association with increased weight , long-term sulfonylurea therapy may reduce the risk of coronary heart disease .

Example answer:
{"entities": [{"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The median disease duration was 6 ( 7 ) years .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Mean ( SD ; maximum ) duration of treatment was 19.3 ( 10.3 ; 32.9 ) and 19.1 ( 10.4 ; 33.1 ) months in the etoricoxib and diclofenac groups , respectively .

Example answer:
{"entities": [{"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}]}

Input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

## Item biored:test:72
Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA sequencing analysis showed the patient to be a compound heterozygote for two mutations in the GPIX gene , a novel nine-nucleotide deletion starting at position 1952 of the gene that changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline ) and a previously reported point mutation that changes the codon asparagine ( AAC ) for serine ( AGC ) at residue 45 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "nine-nucleotide deletion starting at position 1952", "type": "SequenceVariant"}, {"text": "changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline )", "type": "SequenceVariant"}, {"text": "asparagine ( AAC ) for serine ( AGC ) at residue 45", "type": "SequenceVariant"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mild glycine encephalopathy ( NKH ) in a large kindred due to a silent exonic GLDC splice mutation .

Example answer:
{"entities": [{"text": "glycine encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NKH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : The mutation in this kindred led to missplicing and reduced GLDC ( glycine decarboxylase ) expression .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "glycine decarboxylase", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This mutation involved a deletion of glycine-91 , cosegregated in all affected individuals , and was not observed in unaffected individuals or in 250 normal control subjects from the same ethnic background .

## Item biored:test:5
Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: hiPS-CMs were seeded onto MEA and FPD was measured for 2min every 10min for 30min after drug exposure for the vehicle and each drug concentration .

Example answer:
{"entities": []}

Example input:
Sentence: NDP-MSH time- and dose-dependently inhibited IRS-1 ( ser307 ) phosphorylation , effects also reversed by a specific melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: The ED50 values for morphine when given in combination with CNSB002 ( 5 mg/kg ) were less than the maximum nonsedating dose : 0.56 ( 1.55 ) in the carrageenan model and 1.37 ( 1.23 ) in the neuropathy model ( mg/kg ; mean , SEM ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "carrageenan", "type": "ChemicalEntity"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Multivariate regression analysis allowed attribution of 31.8 % of QTc variability to methadone dose , cytochrome P-450 3A4 drug-drug interactions , hypokalemia , and altered liver function .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "cytochrome P-450 3A4", "type": "GeneOrGeneProduct"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Input:
Sentence: By using pharmacokinetic pharmacodynamic modeling the pharmacodynamics of racemic metoprolol and the active S-isomer , were quantitated in EMs and PMs in terms of IC50 values , representing metoprolol plasma concentrations resulting in half-maximum receptor occupancy .

## Item biored:test:69
Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , eight individuals who had both microcoria and glaucoma were screened for glaucoma genes : myocilin ( MYOC ) , optineurin ( OPTN ) and CYP1B1 .

Example answer:
{"entities": [{"text": "microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocilin", "type": "GeneOrGeneProduct"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "optineurin", "type": "GeneOrGeneProduct"}, {"text": "OPTN", "type": "GeneOrGeneProduct"}, {"text": "CYP1B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Six participants demonstrated LCD1 in both eyes , most of whom were symmetric .

Example answer:
{"entities": [{"text": "LCD1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : All four members of this family affected by LCA showed high to extreme hyperopia , with average spherical refractive errors ranging from +5.00 to +10.00 .

Example answer:
{"entities": [{"text": "LCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperopia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Data presented here supports the hypothesis that congenital microcoria is a potential risk factor for glaucoma , although this observation is complicated by the partial segregation of MYOC Q48H ( 1q24.3-q25.2 ) , a mutation known to be associated with glaucoma in India .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "Q48H", "type": "SequenceVariant"}]}

Example input:
Sentence: PURPOSE : To identify the underlying genetic defect in a four-generation family of Chinese origin with autosomal dominant congenital cataract-microcornea syndrome ( CCMC ) .

Example answer:
{"entities": [{"text": "genetic defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCMC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS : Affected individuals had a congenital nuclear lactescent cataract in both eyes .

## Item biored:test:9
Example input:
Sentence: CONCLUSIONS : Methadone is associated with QT prolongation and higher reporting of syncope in a population of heroin addicts .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: All active treatments were associated with significantly reduced MSSBP and MSDBP during the core 8-week study , with each monotherapy significantly contributing to the overall effect of combination therapy ( VAL and HCTZ , P < 0.001 ) .

Example answer:
{"entities": [{"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Methadone dose was associated with longer QT interval of 0.140 ms/mg ( p = 0.002 ) .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "longer QT interval", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: At dose levels of ( + ) -propranolol which attenuated the responses to isoprenaline , there was a significant prolongation of the PR interval of the electrocardiogram.3 .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Among the subjects treated with methadone , 28 % men and 32 % women had prolonged QTc interval .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "prolonged QTc interval", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Prolongation of the QT interval in the ECG of patients with torsade de pointes ( TdP ) has been reported in methadone users .

Example answer:
{"entities": [{"text": "Prolongation of the QT interval", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "torsade de pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Input:
Sentence: In PMs , metoprolol increased the terbutaline area under the plasma concentration vs. time curve ( +67 % ) .

## Item biored:test:16
Example input:
Sentence: A deletion of 84,682 base pairs covering the CFHR1 and CFHR3 genes was detected by direct polymerase chain reaction and gel electrophoresis .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In both patients , a 105-bp deletion encompassing bases 1078-1182 in VLCAD cDNA was identified .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "105-bp deletion encompassing bases 1078-1182", "type": "SequenceVariant"}, {"text": "VLCAD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: After restricting the candidate region in chromosome 16q22.1 by haplotype analysis , we found that all patients from 52 unrelated Japanese families harbor a heterozygous C -- > T single-nucleotide substitution , 16 nt upstream of the putative translation initiation site of the gene for a hypothetical protein DKFZP434I216 , which we have called `` puratrophin-1 '' ( Purkinje cell atrophy associated protein-1 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "C -- > T", "type": "SequenceVariant"}, {"text": "DKFZP434I216", "type": "GeneOrGeneProduct"}, {"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "Purkinje cell atrophy associated protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations in the desmin and the alpha-B crystallin genes account for approximately one third of the DRM cases .

Example answer:
{"entities": [{"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "alpha-B crystallin", "type": "GeneOrGeneProduct"}, {"text": "DRM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Tumor TS 1494del6 allele ( frequency of allelic loss , 36 % ) was protective ( for each allele with the deletion , based on an additive model , HR = 0.42 ; 95 % CI , 0.22 to 0.82 ; P = .0034 ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Seven germline deletions ( 13 % of RB patients ) were identified , and the maternal allele was more frequently lost ( p=0.01 ) .

Example answer:
{"entities": [{"text": "RB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: These 80 individuals account for approximately 75 % of 109 deletions of the gene , detected among 181 patients analyzed with the entire dystrophin cDNA .

## Item biored:test:17
Example input:
Sentence: The D487_S488_F489 deletion had been identified in two previously genotyped Chinese families .

Example answer:
{"entities": [{"text": "D487_S488_F489 deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: A detailed analysis of the DNA breakpoints in the two genes , previously characterized by other groups , validated the observation that Alu-mediated unequal recombination is the main type of deletion in MSH2 ( n=34 ) , but not in MLH1 ( n=21 ) ( P < 0.0001 ) .

Example answer:
{"entities": [{"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Thus , the same deletion patterns covered the entire p14 gene for all cases except for one case , which suggested the hemizygous deletion of exons 1beta and 2 and homozygous deletion of exon 3 .

Example answer:
{"entities": [{"text": "p14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Multiplex ligation-dependent probe amplification ( MLPA ) was performed to detect large deletions .

Example answer:
{"entities": []}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: The Typically Deleted Region in the 22q11.21 subband ( here called TDR22 ) is very gene-dense , and the extent of the deletion has been defined precisely in several studies .

Example answer:
{"entities": []}

Example input:
Sentence: We used high-resolution karyotyping to confirm a deletion ( 10-12Mb ) [ del ( 1 ) ( p31.2p32.3 ) ] and found no structural abnormalities in the father , suggesting a de novo event .

Example answer:
{"entities": [{"text": "deletion ( 10-12Mb )", "type": "SequenceVariant"}, {"text": "del ( 1 ) ( p31.2p32.3 )", "type": "SequenceVariant"}]}

Example input:
Sentence: To investigate the underlying molecular mechanisms , we characterized the DNA breakpoints of 11 germ-line deletions , six for MLH1 and five for MSH2 .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Endpoints for many of these deletions were further characterized using two genomic probes , p20 ( DXS269 ; Wapenaar et al . )

## Item biored:test:30
Example input:
Sentence: However , scopolamine and ritanserin co-administration resulted in a significant decrease in escape latencies and traveled distances as compared to the scopolamine-treated rats .

Example answer:
{"entities": [{"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Elevated plus maze and passive avoidance apparatus served as the exteroceptive behavioral models for testing memory .

Example answer:
{"entities": []}

Example input:
Sentence: Passive avoidance paradigm and elevated plus maze test were used to assess cognitive function .

Example answer:
{"entities": []}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , there is convincing clinical evidence that monotherapy with continuous subcutaneous apomorphine infusions is associated with marked reductions of preexisting levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : The passive avoidance ( PA ) paradigm was used to assess memory retention .

Example answer:
{"entities": []}

Example input:
Sentence: One week later , they received repeatedly vehicles ( saline , DMSO , saline+DMSO ) , scopolamine ( 2 microg/0.5 microl saline/side ; 30 min before training ) , ritanserin ( 2 , 4 and 8 microg/0.5 microl DMSO/side ; 20 min before training ) and scopolamine ( 2 microg/0.5 microl ; 30 min before ritanserin injection ) +ritanserin ( 4 microg/0.5 microl DMSO ) through cannulae each day .

Example answer:
{"entities": [{"text": "DMSO", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "DMSO/side", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , crocin in the mentioned dose could significantly attenuated learning and memory impairment in treated STZ-injected group in passive avoidance test .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "learning and memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STZ-injected", "type": "ChemicalEntity"}]}

Example input:
Sentence: Continuous subcutaneous apomorphine infusions can reduce daily off-time by more than 50 % in this group of patients , which appears to be a stronger effect than that generally seen with add-on therapy with oral dopamine agonists or COMT inhibitors .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "dopamine agonists", "type": "ChemicalEntity"}, {"text": "COMT inhibitors", "type": "ChemicalEntity"}]}

Input:
Sentence: A step-down passive avoidance paradigm was employed and nefiracetam ( 3 mg/kg ) and apomorphine ( 0.5 mg/kg ) were given alone or in combination during training and at the 10-12h post-training period of consolidation .

## Item biored:test:44
Example input:
Sentence: MSH5 and DMC1 mutations may be one explanation for POF , albeit uncommon .

Example answer:
{"entities": [{"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the WFS1 gene of these patients , we identified a novel mutation , a nine nucleotide insertion ( AFF344-345ins ) .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "nine nucleotide insertion", "type": "SequenceVariant"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}]}

Example input:
Sentence: The present study highlights the importance of the 5 ' untranslated region ( UTR ) in identification of genes of human disease , suggests that a single-nucleotide substitution in the 5 ' UTR could be associated with protein aggregation , and indicates that the GEF protein is associated with cerebellar degeneration in humans .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "GEF", "type": "GeneOrGeneProduct"}, {"text": "cerebellar degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient showed an R227Q mutation that has been described in an Asian population and MPH patients , along with a novel frameshift mutation , Tdel219 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "R227Q", "type": "SequenceVariant"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Tdel219", "type": "SequenceVariant"}]}

Example input:
Sentence: Since the first molecular characterization of an FH mutation by Bourgeron et al in 1994 , a series of reports of both FH deficiency patients and patients with MCUL/HLRRC have described 107 variants , of which 93 are thought to be pathogenic .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "FH deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MCUL/HLRRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified such a mechanism as the origin of the mild to asymptomatic phenotype observed in cystic fibrosis patients homozygous for the E831X mutation ( 2623G > T ) in the CFTR gene .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "E831X", "type": "SequenceVariant"}, {"text": "2623G > T", "type": "SequenceVariant"}, {"text": "CFTR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OPMD is caused by a short trinucleotide repeat expansion encoding an expanded polyalanine tract in the polyadenylate binding-protein nuclear 1 ( PABPN1 ) gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyalanine", "type": "ChemicalEntity"}, {"text": "polyadenylate binding-protein nuclear 1", "type": "GeneOrGeneProduct"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In more than 98 % of cases , the disease is associated with a G to A or G to C substitution at nucleotide position 1138 ( p.G380R ) of the fibroblast growth factor receptor 3 ( FGFR3 ) gene .

Example answer:
{"entities": [{"text": "G to A or G to C substitution at nucleotide position 1138", "type": "SequenceVariant"}, {"text": "p.G380R", "type": "SequenceVariant"}, {"text": "fibroblast growth factor receptor 3", "type": "GeneOrGeneProduct"}, {"text": "FGFR3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: It is usually caused by an expansion of the trinucleotide repeat in the 5'-untranslated region of the FMR1 gene , but in a small number of patients deletions and point mutations have been identified .

## Item biored:test:10
Example input:
Sentence: Estrogen replacement ( 17beta-estradiol subcutaneous pellet , 14.2 microg/day , 12 wk ) of Ovx rats restored the hemodynamic and locomotor effects of alpha-methyldopa to sham-operated levels .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "I1- and alpha2-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SDRR was reduced only by alpha-methyldopa .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compared with those carrying at least one variant 326Ile allele , carriers with the Met326Met genotype had higher serum 17-hydroxyprogesterone ( 17-OHP ) { 1.1 [ 95 % confidence interval ( CI ) 1.1-1.3 ] ng/ml in those with the Met326Met genotype versus 0.8 ( 95 % CI 0.7-1.0 ) ng/ml in those with Ile326Ile and Met326Ile genotypes , P = 0.0073 } and free testosterone levels [ 1.2 ( 95 % CI 1.1-1.4 ) pg/ml for Met326Met genotype versus 0.9 ( 95 % CI 0.6-1.3 ) pg/ml for Ile326Ile and Met326Ile genotypes , P = 0.038 ] .

Example answer:
{"entities": [{"text": "326Ile", "type": "SequenceVariant"}, {"text": "Met326Met", "type": "SequenceVariant"}, {"text": "17-hydroxyprogesterone", "type": "ChemicalEntity"}, {"text": "17-OHP", "type": "ChemicalEntity"}, {"text": "Ile326Ile", "type": "SequenceVariant"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "testosterone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Higher metoprolol/alpha-hydroxymetoprolol ratios in PMs were predictive for higher R-/S-isomer ratios of unchanged drug .

## Item biored:test:40
Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: This retrospective study investigated the combination of bort ( 1.3 mg/m ( 2 ) on days 1 , 4 , 8 , and 11 every 3 weeks ) and dex ( 20 mg on the day of and the day after bort ) as salvage treatment in 85 patients with R/R MM after prior autologous stem cell transplantation or conventional chemotherapy .

Example answer:
{"entities": [{"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Daily administration of desipramine , an inhibitor of the NET , for 5 days decreased [ ( 3 ) H ] norepinephrine uptake in the P2 fractions of hippocampus but not cortex , striatum or amygdalae .

Example answer:
{"entities": [{"text": "desipramine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Continuous subcutaneous apomorphine infusions can reduce daily off-time by more than 50 % in this group of patients , which appears to be a stronger effect than that generally seen with add-on therapy with oral dopamine agonists or COMT inhibitors .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "dopamine agonists", "type": "ChemicalEntity"}, {"text": "COMT inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doses were flexibly titrated up to 0.6 mg/day for clonidine and 60 mg/day for methylphenidate ( both with divided dosing ) .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "methylphenidate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Optimal control of the absences was achieved with sodium valproate , lamotrigine , or ethosuximide alone or in combination .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "ChemicalEntity"}, {"text": "lamotrigine", "type": "ChemicalEntity"}, {"text": "ethosuximide", "type": "ChemicalEntity"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One week later , they received repeatedly vehicles ( saline , DMSO , saline+DMSO ) , scopolamine ( 2 microg/0.5 microl saline/side ; 30 min before training ) , ritanserin ( 2 , 4 and 8 microg/0.5 microl DMSO/side ; 20 min before training ) and scopolamine ( 2 microg/0.5 microl ; 30 min before ritanserin injection ) +ritanserin ( 4 microg/0.5 microl DMSO ) through cannulae each day .

Example answer:
{"entities": [{"text": "DMSO", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "DMSO/side", "type": "ChemicalEntity"}]}

Example input:
Sentence: OIH was achieved in mice after subcutaneous administration of morphine for 7 consecutive days three times per day .

Example answer:
{"entities": [{"text": "OIH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "morphine", "type": "ChemicalEntity"}]}

Input:
Sentence: This method allowed frequent self-dosing of pethidine at short time intervals and rapid accumulation of pethidine and norpethidine .

## Item biored:test:57
Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Upon pretreatment with mangiferin ( 100 mg/kg body weight suspended in 2 ml of dimethyl sulphoxide ) given intraperitoneally for 28 days to MI rats protected the above-mentioned parameters to fall from the normal levels .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "dimethyl sulphoxide", "type": "ChemicalEntity"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Four hours after MCAO , the rats were killed and the brains harvested .

Example answer:
{"entities": [{"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Sprague-Dawley rats were injected with saline on postnatal day ( P ) 20 , or a convulsant dose of pilocarpine on P20 or P45 .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a prevention study , rats received 4 days of LF treatment followed by Dex and continued during the test period .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Input:
Sentence: All rats were terminated either 24 h or 3 weeks after the DFP injection .

## Item biored:test:36
Example input:
Sentence: In the present study , we describe the proinflammatory effects of bupivacaine on local prostaglandin E2 ( PGE2 ) production and cyclooxygenase ( COX ) gene expression that increases postoperative pain in human subjects .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "prostaglandin E2", "type": "GeneOrGeneProduct"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}, {"text": "cyclooxygenase", "type": "GeneOrGeneProduct"}, {"text": "COX", "type": "GeneOrGeneProduct"}, {"text": "postoperative pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: A rat model of IUGR was established by PCE , male fetuses and adult offspring at the age of postnatal week 24 were euthanized .

Example answer:
{"entities": [{"text": "rat", "type": "OrganismTaxon"}, {"text": "IUGR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHOD : Medically healthy 7- to 17-year-old males chronically treated , in a naturalistic setting , with risperidone were recruited for this cross-sectional study through child psychiatry outpatient clinics between November 2005 and June 2007 .

Example answer:
{"entities": [{"text": "risperidone", "type": "ChemicalEntity"}, {"text": "outpatient", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Hyperprolactinemia was present in 49 % of 83 boys ( n = 41 ) treated with risperidone for a mean of 2.9 years .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: All 24 patients with seizures received high doses of TXA intraoperatively ranging from 61 to 259 mg/kg , had a mean age of 69.9 years , and 21 of 24 had undergone open chamber rather than coronary bypass procedures .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TXA", "type": "ChemicalEntity"}]}

Example input:
Sentence: At puberty ( P40 ) , half the PCPA-treated rats and half the saline-treated rats began treatment with testosterone ( T , 5 mg/kg , 5 days/week ) .

Example answer:
{"entities": [{"text": "PCPA-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serotonin was depleted beginning on postnatal day 26 with parachlorophenylalanine ( PCPA 100 mg/kg , every other day ) ; controls received saline .

Example answer:
{"entities": [{"text": "Serotonin", "type": "ChemicalEntity"}, {"text": "parachlorophenylalanine", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Input:
Sentence: A healthy 17-year-old male received standard intermittent doses of pethidine via a patient-controlled analgesia ( PCA ) pump for management of postoperative pain control .

## Item biored:test:47
Example input:
Sentence: DNA sequencing analysis showed the patient to be a compound heterozygote for two mutations in the GPIX gene , a novel nine-nucleotide deletion starting at position 1952 of the gene that changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline ) and a previously reported point mutation that changes the codon asparagine ( AAC ) for serine ( AGC ) at residue 45 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GPIX", "type": "GeneOrGeneProduct"}, {"text": "nine-nucleotide deletion starting at position 1952", "type": "SequenceVariant"}, {"text": "changes asparagine 86 for alanine and eliminates amino acids 87 , 88 , and 89 ( arginine , threonine , and proline )", "type": "SequenceVariant"}, {"text": "asparagine ( AAC ) for serine ( AGC ) at residue 45", "type": "SequenceVariant"}]}

Example input:
Sentence: In addition , each affected child was heterozygous for the G1681A mutation in exon 7 that led to an Ala467Thr substitution in POLG , within the linker region of the protein .

Example answer:
{"entities": [{"text": "G1681A", "type": "SequenceVariant"}, {"text": "Ala467Thr", "type": "SequenceVariant"}, {"text": "POLG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : The patient 's GR gene had a heterozygotic mutation ( G -- > A ) at nucleotide position 2141 ( exon 8 ) , which resulted in substitution of arginine by glutamine at amino acid position 714 in the ligand-binding domain ( LBD ) of the GR alpha .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "( G -- > A ) at nucleotide position 2141", "type": "SequenceVariant"}, {"text": "arginine by glutamine at amino acid position 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The patient was a compound heterozygote for SRD5A2 mutations , carrying 2 mutations in exon 4 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: The compound heterozygous mutations , c.892C > T and c.1072T > C , were identified in exon 3 of CHST6 in three patients .

Example answer:
{"entities": [{"text": "c.892C > T", "type": "SequenceVariant"}, {"text": "c.1072T > C", "type": "SequenceVariant"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Her mother was heterozygous for the Asn45Ser mutation , and her father , for the nine-nucleotide deletion .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}]}

Input:
Sentence: However , one female patient was heterozygous for a normal allele and a mutant allele with an A to C substitution at nucleotide 879 in exon 9 .

## Item biored:test:18
Example input:
Sentence: GPX4 rs713041 is located near the selenocysteine insertion sequence element in the GPX4 3 ' untranslated region , and the rare allele of this SNP is associated with an increased risk of death , with a hazard ratio of 1.27 per rare allele carried ( 95 % CI , 1.13 to 11.43 ) .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "rs713041", "type": "SequenceVariant"}, {"text": "selenocysteine", "type": "ChemicalEntity"}, {"text": "death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Two single nucleotide polymorphisms ( SNPs ) in GPX4 ( rs713041 and rs757229 ) were associated with all-cause mortality even after adjusting for multiple hypothesis testing ( adjusted P = .0041 and P = .0035 ) .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "rs713041", "type": "SequenceVariant"}, {"text": "rs757229", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : In contrast to a single GCG expansion in most of OPMD patients in the literature , an insertion of ( GCG ) 4GCA in the PABPN1 gene was found in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of this study was to investigate the association of DNA polymorphisms within steroid synthesis genes ( CYP11B2 , CYP11B1 ) and the postoperative resolution of hypertension in Chinese patients undergoing adrenalectomy for aldosterone-producing adenomas ( APA ) .

Example answer:
{"entities": [{"text": "steroid synthesis genes", "type": "GeneOrGeneProduct"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "aldosterone-producing adenomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Arg124Cys and Arg555Trp appear to be the predominant mutations causing LCD and GCD , respectively , in the population studied .

Example answer:
{"entities": [{"text": "Arg124Cys", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We progressively screened DNA samples from 613 individuals with ID initially for the most frequent ARX mutations ( c.304ins ( GCG ) ( 7 ) 'expansion ' of pA1 and c.429_452dup 'dup24bp ' of pA2 ) .

Example answer:
{"entities": [{"text": "ID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "c.304ins ( GCG ) ( 7 )", "type": "SequenceVariant"}, {"text": "c.429_452dup", "type": "SequenceVariant"}]}

Example input:
Sentence: In addition , the previously described variants g.3352delG ( commonly designated 30delG or 35 delG ) , g.3426G > A [ p.Val37Ile ] , g.3697G > A [ p.Arg127His ] , g.3774G > A [ p.Val153Ile ] , and g.3795G > A [ p.Gly160Ser ] were identified .

Example answer:
{"entities": [{"text": "g.3352delG", "type": "SequenceVariant"}, {"text": "30delG", "type": "SequenceVariant"}, {"text": "35 delG", "type": "SequenceVariant"}, {"text": "g.3426G > A", "type": "SequenceVariant"}, {"text": "p.Val37Ile", "type": "SequenceVariant"}, {"text": "g.3697G > A", "type": "SequenceVariant"}, {"text": "p.Arg127His", "type": "SequenceVariant"}, {"text": "g.3774G > A", "type": "SequenceVariant"}, {"text": "p.Val153Ile", "type": "SequenceVariant"}, {"text": "g.3795G > A", "type": "SequenceVariant"}, {"text": "p.Gly160Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: This is the first known constitutional rearrangement of SYT14 , and further systematic genetic analysis and clinical studies of DGAP128 may offer unique insights into the role of SYT14 in neurodevelopment .

Example answer:
{"entities": [{"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: and GMGX11 ( DXS239 ; present paper ) .

## Item biored:test:83
Example input:
Sentence: However , the lower doses of 25 and 50mg/kg were more effective than 100mg/kg .

Example answer:
{"entities": []}

Example input:
Sentence: injection of cisplatin ( 5 mg/kg ) .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In Canadian patients , Cys 23 Ser was associated with minimum lifetime BMI ( p=0.046 ) , with lowest values in Ser/Ser carriers .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Mean ( SD ; maximum ) duration of treatment was 19.3 ( 10.3 ; 32.9 ) and 19.1 ( 10.4 ; 33.1 ) months in the etoricoxib and diclofenac groups , respectively .

Example answer:
{"entities": [{"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}]}

Example input:
Sentence: The ED50 values for morphine when given in combination with CNSB002 ( 5 mg/kg ) were less than the maximum nonsedating dose : 0.56 ( 1.55 ) in the carrageenan model and 1.37 ( 1.23 ) in the neuropathy model ( mg/kg ; mean , SEM ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "carrageenan", "type": "ChemicalEntity"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The maximum nonsedating doses were : morphine , 3.2 mg/kg ; CNSB002 10.0 mg/kg ; 5.0 mg/kg CNSB002 with morphine 3.2 mg/kg in combination .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Input:
Sentence: RESULTS : The median cumulative doses of cyclophosphamide among cases ( n = 11 ) and controls ( n = 25 ) were 113 g and 25 g , respectively .

## Item biored:test:98
Example input:
Sentence: After restricting the candidate region in chromosome 16q22.1 by haplotype analysis , we found that all patients from 52 unrelated Japanese families harbor a heterozygous C -- > T single-nucleotide substitution , 16 nt upstream of the putative translation initiation site of the gene for a hypothetical protein DKFZP434I216 , which we have called `` puratrophin-1 '' ( Purkinje cell atrophy associated protein-1 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "C -- > T", "type": "SequenceVariant"}, {"text": "DKFZP434I216", "type": "GeneOrGeneProduct"}, {"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "Purkinje cell atrophy associated protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: When combined with the initial linkage paper our haplotype and linkage data map the MCOR locus to a 6-7 cM region between D13S265 and D13S1280 .

Example answer:
{"entities": [{"text": "MCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Multipoint analysis revealed a 4 cM region encompassing D13S1300 to D13S1280 where the LOD remains just over 6.0 Thus we confirm localization of the congenital microcoria locus to chromosomal locus 13q31-q32 .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In our present study , a third Chinese family with this mutation was identified , suggesting that this mutation is a prevalent CYP17 mutation in the Chinese population .

Example answer:
{"entities": [{"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , sequencing of our two chromosome 12-linked bipolar-Darier families showed no evidence of rare variants at P2RX7 that could explain the linkage .

Example answer:
{"entities": [{"text": "P2RX7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The D487_S488_F489 deletion had been identified in two previously genotyped Chinese families .

Example answer:
{"entities": [{"text": "D487_S488_F489 deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: By multipoint linkage analysis with markers spanning the entire X-chromosome we mapped the disease locus to a 28-Mb interval between Xp11.4 and Xq12 , including the BCOR gene .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The chromosomal region 12q24 has been previously implicated by linkage studies of both bipolar disorder and unipolar mood disorder and we have reported two pedigrees segregating both bipolar disorder and Darier 's disease that show linkage across this region .

Example answer:
{"entities": [{"text": "bipolar disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "unipolar mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Darier 's disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Linkage to the chromosomal locus 13q31-q32 has previously been reported in a large French family .

Example answer:
{"entities": []}

Input:
Sentence: In this study , we performed a genome-wide linkage analysis in three Chinese affected families and localized the gene in an 8.0 cM interval defined by D12S330 and D12S354 on chromosome 12 .
