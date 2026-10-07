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

## Item biored:test:21
Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Molecular diagnosis of 46 , XY DSD and identification of a novel 8 nucleotide deletion in exon 1 of the SRD5A2 gene .

Example answer:
{"entities": [{"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "8 nucleotide deletion", "type": "SequenceVariant"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Four out of 12 patients exhibited a progressive , mosaic pattern of mtDNA depletion in cultured fibroblasts .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: We used high-resolution karyotyping to confirm a deletion ( 10-12Mb ) [ del ( 1 ) ( p31.2p32.3 ) ] and found no structural abnormalities in the father , suggesting a de novo event .

Example answer:
{"entities": [{"text": "deletion ( 10-12Mb )", "type": "SequenceVariant"}, {"text": "del ( 1 ) ( p31.2p32.3 )", "type": "SequenceVariant"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether c.609+28_610-16del allele-derived transcripts were subject to nonsense-mediated mRNA decay ( NMD ) , patient fibroblasts were incubated with the protein synthesis inhibitor anisomycin .

Example answer:
{"entities": [{"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "anisomycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Input:
Sentence: Of these , eight BMD patients and one intermediate patient had gene deletions predicted to leave the reading frame intact , while 21 DMD patients , 7 intermediate patients , and 1 BMD patient had gene deletions predicted to disrupt the reading frame .

## Item biored:test:100
Example input:
Sentence: We hypothesized that activin and/or GnRH pathways may be modulated by BMP-4 , but neither the activin-stimulated phosphorylation of Smad2/3 nor the GnRH-induced ERK1/2 or cAMP response element-binding phosphorylation were modified .

Example answer:
{"entities": [{"text": "activin", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "activin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "Smad2/3", "type": "GeneOrGeneProduct"}, {"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because members of the synaptotagmin family of proteins function as sensors that link changes in calcium levels with a variety of biological processes , including neurotransmission and hormone-responsiveness , SYT14 is an intriguing candidate gene for the abnormal development in this child .

Example answer:
{"entities": [{"text": "synaptotagmin", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Smad1/5 phosphorylation induced by BMP-4 , indicating activation of BMP signalling , was the same whether BMP-4 was used alone or combined with activin+/-GnRH .

Example answer:
{"entities": [{"text": "Smad1/5", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}, {"text": "activin+/-GnRH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TAK1 is an essential regulator of BMP signalling in cartilage .

Example answer:
{"entities": [{"text": "TAK1", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the absence of functional phosphatase and tensin homolog ( PTEN ) protein in Ishikawa cells , PKCalpha knockdown reduced Akt phosphorylation at serine 473 and concomitantly inhibited phosphorylation of the Akt target , glycogen synthase kinase-3beta ( GSK-3beta ) .

Example answer:
{"entities": [{"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "glycogen synthase kinase-3beta", "type": "GeneOrGeneProduct"}, {"text": "GSK-3beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunofluorescent staining revealed that dystrophin is the most sensitive among the structures connecting the actin in the cardiomyocyte cytoskeleton and the extracellular matrix .

Example answer:
{"entities": [{"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "actin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TAK1 mediates Smad1 phosphorylation at C-terminal serine residues .

Example answer:
{"entities": [{"text": "TAK1", "type": "GeneOrGeneProduct"}, {"text": "Smad1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Glutathione-S-transferase P1 ( GSTP1 ) is a critical enzyme of the phase II detoxification pathway .

Example answer:
{"entities": [{"text": "Glutathione-S-transferase P1", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gankyrin binds to Src homology 2 domain-containing protein tyrosine phosphatase-1 ( SHP-1 ) , mainly expressed in liver non-parenchymal cells , resulting in phosphorylation and activation of signal transducer and activator of transcription 3 ( STAT3 ) .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "Src homology 2 domain-containing protein tyrosine phosphatase-1", "type": "GeneOrGeneProduct"}, {"text": "SHP-1", "type": "GeneOrGeneProduct"}, {"text": "signal transducer and activator of transcription 3", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The full-length puratrophin-1 mRNA had an open reading frame of 3,576 nt , predicted to contain important domains , including the spectrin repeat and the guanine-nucleotide exchange factor ( GEF ) for Rho GTPases , followed by the Dbl-homologous domain , which indicates the role of puratrophin-1 in intracellular signaling and actin dynamics at the Golgi apparatus .

Example answer:
{"entities": [{"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "guanine-nucleotide exchange factor", "type": "GeneOrGeneProduct"}, {"text": "GEF", "type": "GeneOrGeneProduct"}, {"text": "Rho GTPases", "type": "GeneOrGeneProduct"}, {"text": "actin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: SSH1 encodes a phosphatase that plays a pivotal role in actin dynamics .

## Item biored:test:137
Example input:
Sentence: Among a total of 60 patients included in the study , 16 patients developed acute renal failure ( ARF ) on the second day after contrast material was injected ( 26.6 % ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: MD also showed that the enzyme volume is increased , suggesting a pre-denaturation state .

Example answer:
{"entities": []}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients who received the same anesthetic procedure were selected : 2 minutes after intravenous injections of the pretreatment drugs , anesthesia is induced with 0.3 mg.kg-1 etomidate injected intravenously over a period of 20-30 seconds .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "etomidate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One week later , they received repeatedly vehicles ( saline , DMSO , saline+DMSO ) , scopolamine ( 2 microg/0.5 microl saline/side ; 30 min before training ) , ritanserin ( 2 , 4 and 8 microg/0.5 microl DMSO/side ; 20 min before training ) and scopolamine ( 2 microg/0.5 microl ; 30 min before ritanserin injection ) +ritanserin ( 4 microg/0.5 microl DMSO ) through cannulae each day .

Example answer:
{"entities": [{"text": "DMSO", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "DMSO/side", "type": "ChemicalEntity"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After extraction , a microdialysis probe was placed at the surgical site for PGE2 and thromboxane B2 ( TXB2 ) measurements .

Example answer:
{"entities": [{"text": "PGE2", "type": "GeneOrGeneProduct"}, {"text": "thromboxane B2", "type": "ChemicalEntity"}, {"text": "TXB2", "type": "ChemicalEntity"}]}

Input:
Sentence: Microdialysis samples were collected preischemia , before IT injection , and at 2 , 4 , 8 , 24 , and 48 h of reperfusion ( after IT injection ) .

## Item biored:test:140
Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Among 167 methadone maintenance patients , the prevalence of QTc prolongation to 0.50 second ( ( 1/2 ) ) or longer was 16.2 % compared with 0 % in 80 control subjects .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "QTc prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Lifelong administration of vitamin E to Hp 2-2 DM individuals in the Kaiser population would increase their life expectancy by 3 years .

Example answer:
{"entities": [{"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A cell proliferation assay was performed after 7 days of incubation under normoxic conditions .

Example answer:
{"entities": []}

Example input:
Sentence: Addition of Tat ( 40 ng/slice ) to the medium of OHSCs induced IDO steady-state mRNA that peaked at 6 h. This effect was potentiated by pretreatment with IFNg .

Example answer:
{"entities": [{"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "IFNg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All patients were observed for 6 hours after each challenge , and controlled again after 24 hours to exclude delayed reactions .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The patient 's symptoms improved slightly over the next few hours .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Extended follow-up studies of up to 8 years have demonstrated long-term persistence of apomorphine efficacy .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: TGF-betaRII mRNA expression was increased after 48 and 72 h respectively .

Example answer:
{"entities": [{"text": "TGF-betaRII", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Liver and plasma TBARs were not increased until 14 days ( 2-fold vs. control , p < 0.05 ) .

Example answer:
{"entities": [{"text": "TBARs", "type": "ChemicalEntity"}]}

Input:
Sentence: This increase persisted for 8 hrs .

## Item biored:test:50
Example input:
Sentence: Recent reports have demonstrated that mutations in the OPHN1 gene were responsible for a syndromic rather than non-specific mental retardation .

Example answer:
{"entities": [{"text": "OPHN1", "type": "GeneOrGeneProduct"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Identification of a novel WFS1 mutation ( AFF344-345ins ) in Japanese patients with Wolfram syndrome .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Wolfram syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that primary glioblastomas in Japan show genetic alterations similar to those in Switzerland , suggesting a similar molecular basis in caucasians and Asians , despite different genetic backgrounds , including different status of a polymorphism in the EGFR gene .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient showed an R227Q mutation that has been described in an Asian population and MPH patients , along with a novel frameshift mutation , Tdel219 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "R227Q", "type": "SequenceVariant"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Tdel219", "type": "SequenceVariant"}]}

Example input:
Sentence: Two novel mutations , L490R and V561X , of the transferrin receptor 2 gene in Japanese patients with hemochromatosis .

Example answer:
{"entities": [{"text": "L490R", "type": "SequenceVariant"}, {"text": "V561X", "type": "SequenceVariant"}, {"text": "transferrin receptor 2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND AND OBJECTIVES : The low prevalence of the C282Y mutation of the HFE gene in Japan means that the genetic background of hemochromatosis in Japanese patients remains unclear .

Example answer:
{"entities": [{"text": "C282Y", "type": "SequenceVariant"}, {"text": "HFE", "type": "GeneOrGeneProduct"}, {"text": "hemochromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: X-linked mental retardation has been traditionally divided into syndromic ( S-XLMR ) and non-syndromic forms ( NS-XLMR ) , although the borderlines between these phenotypes begin to vanish and mutations in a single gene , for example PQBP1 , can cause S-XLMR as well as NS-XLMR .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PQBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: After restricting the candidate region in chromosome 16q22.1 by haplotype analysis , we found that all patients from 52 unrelated Japanese families harbor a heterozygous C -- > T single-nucleotide substitution , 16 nt upstream of the putative translation initiation site of the gene for a hypothetical protein DKFZP434I216 , which we have called `` puratrophin-1 '' ( Purkinje cell atrophy associated protein-1 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "C -- > T", "type": "SequenceVariant"}, {"text": "DKFZP434I216", "type": "GeneOrGeneProduct"}, {"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "Purkinje cell atrophy associated protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Although uncommon , point mutations in the FMR1 gene may be a cause of autism and mental retardation in Japanese patients .

## Item biored:test:43
Example input:
Sentence: In addition , affected males display facial similarities that can help the diagnosis .

Example answer:
{"entities": []}

Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutations in N-acetylglucosamine ( O-GlcNAc ) transferase in patients with X-linked intellectual disability .

Example answer:
{"entities": [{"text": "N-acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recent reports have demonstrated that mutations in the OPHN1 gene were responsible for a syndromic rather than non-specific mental retardation .

Example answer:
{"entities": [{"text": "OPHN1", "type": "GeneOrGeneProduct"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Most carrier females have mild mental retardation and subtle facial changes .

Example answer:
{"entities": [{"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: ARX mutations cause a diverse spectrum of human disorders , ranging from severe brain and genital malformations to non-syndromic intellectual disability ( ID ) .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "brain and genital malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ID", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: X-linked mental retardation has been traditionally divided into syndromic ( S-XLMR ) and non-syndromic forms ( NS-XLMR ) , although the borderlines between these phenotypes begin to vanish and mutations in a single gene , for example PQBP1 , can cause S-XLMR as well as NS-XLMR .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PQBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Fragile X syndrome is one of the most common causes of mental retardation in males , and patients with fragile X syndrome occasionally develop autism .

## Item biored:test:77
Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The purpose of this study was to analyze the value of germline and tumor thymidylate synthase ( TS ) genotyping as a prognostic marker in a series of colorectal cancer patients receiving adjuvant fluorouracil ( FU ) -based treatment .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil", "type": "ChemicalEntity"}, {"text": "FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Example input:
Sentence: This study supports the hypothesis that inflammation is involved in prostate carcinogenesis and that sequence variation within the COX-2 gene influence the risk of prostate cancer .

Example answer:
{"entities": [{"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that GSTP1 Ile/Val polymorphism is involved in the risk of prostate cancer development in our population .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ubiquitin carboxyl-terminal esterase L1 ( UCHL1 ) is associated with stem-like cancer cell functions in pediatric high-grade glioma .

Example answer:
{"entities": [{"text": "Ubiquitin carboxyl-terminal esterase L1", "type": "GeneOrGeneProduct"}, {"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Curcumin also decreased bladder tumor growth in athymic nude mice bearing KU7 cells as xenografts and this was accompanied by decreased Sp1 , Sp3 , and Sp4 protein levels in tumors .

Example answer:
{"entities": [{"text": "Curcumin", "type": "ChemicalEntity"}, {"text": "bladder tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "KU7", "type": "CellLine"}, {"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Urinary bladder cancer in Wegener 's granulomatosis : risks and relation to cyclophosphamide .

## Item biored:test:120
Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: The Shh ( CreERT2/+ ) ; b-catenin ( flox ( ex3 ) /+ ) ; BmprIA ( flox/- ) mutants displayed partial restoration of URS elongation compared with the b-catenin GOF mutants .

Example answer:
{"entities": [{"text": "Shh", "type": "GeneOrGeneProduct"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "BmprIA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also demonstrate that the A118D SEA domain mutation causes an intra-molecular structural imbalance that impairs matriptase-2 activation .

Example answer:
{"entities": [{"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The R47W mutation dramatically reduced DNA binding suggesting that the mutant protein with consequent haploinsufficiency results in a clinical phenotype .

Example answer:
{"entities": [{"text": "R47W", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Characterization of a novel BCHE `` silent '' allele : point mutation ( p.Val204Asp ) causes loss of activity and prolonged apnea with suxamethonium .

Example answer:
{"entities": [{"text": "BCHE", "type": "GeneOrGeneProduct"}, {"text": "p.Val204Asp", "type": "SequenceVariant"}, {"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "suxamethonium", "type": "ChemicalEntity"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation is at the same nucleotide and amino acid position as the only other reported DFNA36 mutation , p.D572N ( c.G1714A ) .

Example answer:
{"entities": [{"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "p.D572N", "type": "SequenceVariant"}, {"text": "c.G1714A", "type": "SequenceVariant"}]}

Example input:
Sentence: This generates a conformational shift in the p17 R76G mutant which enables a functional epitope ( s ) , masked in refp17 , to elicit B-cell growth-promoting signals after its interaction with a still unknown receptor ( s ) .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "R76G", "type": "SequenceVariant"}]}

Input:
Sentence: But , the other neighboring I1762A mutant had no persistent current and was still associated with a positive shift of inactivation .

## Item biored:test:56
Example input:
Sentence: Control rats received corn oil only .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "corn oil", "type": "ChemicalEntity"}]}

Example input:
Sentence: The rats were assigned into four groups ( n=10 per group ) , as follows : Control rats ; rats+atorvastatin ; rats + iopamidol ; rats+iopamidol+atorvastatin .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rats+atorvastatin", "type": "OrganismTaxon"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "rats+iopamidol+atorvastatin", "type": "OrganismTaxon"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Sprague-Dawley rats were injected with saline on postnatal day ( P ) 20 , or a convulsant dose of pilocarpine on P20 or P45 .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "Ato-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "allopurinol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Control ( saline P20 ) rats acquired both discriminations immediately .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Control rats were injected with saline instead of pilocarpine .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Input:
Sentence: The control rats received atropine sulfate , but also saline and olive oil instead of other antidotes and DFP , respectively .

## Item biored:test:119
Example input:
Sentence: RESULTS : Val175Met variant allele of the PEMT gene was significantly more frequent in NASH patients than in healthy volunteers ( p < 0.001 ) , and carriers of Val175Met variant were significantly more frequent in NASH patients than in healthy volunteers ( p < 0.01 ) .

Example answer:
{"entities": [{"text": "Val175Met", "type": "SequenceVariant"}, {"text": "PEMT", "type": "GeneOrGeneProduct"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Atypical clinical features for LCD were noted in patients with the Gly594Val and Val624-Val625del mutations .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: The aim of this study was to investigate whether the carriers of Val175Met variant impaired in PEMT activity are more susceptible to NASH .

Example answer:
{"entities": [{"text": "Val175Met", "type": "SequenceVariant"}, {"text": "PEMT", "type": "GeneOrGeneProduct"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation at the DFNA36 hearing loss locus reveals a critical function and potential genotype-phenotype correlation for amino acid-572 of TMC1 .

Example answer:
{"entities": [{"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In LCD , three novel heterozygous mutations found were glycine-594-valine ( Gly594Val ) in 2 of 18 patients , valine-539-aspartic acid ( Val539Asp ) in 1 patient , and deletion of valine 624 , valine 625 ( Val624-Val625del ) in 1 patient .

Example answer:
{"entities": [{"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glycine-594-valine", "type": "SequenceVariant"}, {"text": "Gly594Val", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "valine-539-aspartic acid", "type": "SequenceVariant"}, {"text": "Val539Asp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion of valine 624 , valine 625", "type": "SequenceVariant"}, {"text": "Val624-Val625del", "type": "SequenceVariant"}]}

Example input:
Sentence: This generates a conformational shift in the p17 R76G mutant which enables a functional epitope ( s ) , masked in refp17 , to elicit B-cell growth-promoting signals after its interaction with a still unknown receptor ( s ) .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "R76G", "type": "SequenceVariant"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Input:
Sentence: We also found a similar electrophysiological profile for the neighboring V1764M mutant .

## Item biored:test:94
Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The mechanism of isoproterenol-induced myocardial damage is unknown , but a mismatch of oxygen supply vs. demand following coronary hypotension and myocardial hyperactivity is the best explanation for the complex morphological alterations observed .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial hyperactivity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol ( 100mg/kg ) was injected subcutaneously on the 13th and 14th days to induce acute myocardial infarction .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "acute myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Isoproterenol induces primary loss of dystrophin in rat hearts : correlation with myocardial injury .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The results show that pretreatment with TCR may be useful in preventing the damage induced by isoproterenol in rat heart .

## Item biored:test:125
Example input:
Sentence: All but one of the mutations were detected within the BRCA1 gene .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: SEREX screening of cDNA expression libraries derived from 3 breast cancer patients identified a total of 88 positive clones ( bcg-1 to bcg-88 ) , including 27 hitherto unknown sequences .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The study group consisted of 66 Polish families with cancer who have at least three related females affected with breast or ovarian cancer and who had cancer diagnosed , in at least one of the three affected females , at age < 50 years .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast or ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have undertaken a hospital-based study , to identify possible BRCA1 and BRCA2 founder mutations in the Polish population .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Founder mutations in the BRCA1 gene in Polish families with breast-ovarian cancer .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The study includes 778 women carrying a BRCA1 germ-line mutation belonging to 403 families .

## Item biored:test:20
Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interestingly , a nucleotide insertion of c.1146+25insA in exon 6 was detected in five VSD patients , but not in 486 normal healthy controls .

Example answer:
{"entities": [{"text": "c.1146+25insA", "type": "SequenceVariant"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: Molecular diagnosis of 46 , XY DSD and identification of a novel 8 nucleotide deletion in exon 1 of the SRD5A2 gene .

Example answer:
{"entities": [{"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "8 nucleotide deletion", "type": "SequenceVariant"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Input:
Sentence: Thirty-eight independent patients were old enough to be classified as DMD , BMD , or intermediate phenotype and had deletions of exons with sequenced intron/exon boundaries .

## Item biored:test:90
Example input:
Sentence: The protective role of mangiferin was analyzed by triphenyl tetrazolium chloride ( TTC ) test used for macroscopic enzyme mapping assay of the ischemic myocardium .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "triphenyl tetrazolium chloride", "type": "ChemicalEntity"}, {"text": "TTC", "type": "ChemicalEntity"}, {"text": "ischemic myocardium", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Protective effects of antithrombin on puromycin aminonucleoside nephrosis in rats .

Example answer:
{"entities": [{"text": "antithrombin", "type": "ChemicalEntity"}, {"text": "puromycin aminonucleoside", "type": "ChemicalEntity"}, {"text": "nephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: Acute treatment with metformin has a protective effect in myocardial infarction by suppression of inflammatory responses due to activation of AMP-activated protein kinase ( AMPK ) .

Example answer:
{"entities": [{"text": "metformin", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AMP-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: For in vivo experiments , a model of myocardial infarction ( MI ) was established using both TIEG1 KO and WT mice .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cardioprotective effect of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings indicate the synergistic protective effect of green tea and vitamin E during ISO induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: The present study was done to investigate the protective effect of TCR on experimentally induced myocardial infarction in rats .

## Item biored:test:93
Example input:
Sentence: These changes , related to ischaemic injury , explain the severe alterations in the structural integrity of the sarcolemma of cardiomyocytes and hence severe and irreversible injury induced by isoproterenol .

Example answer:
{"entities": [{"text": "ischaemic injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Severe alterations in the structural integrity of the sarcolemma of cardiomyocytes have been demonstrated to be caused by isoproterenol .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The mechanism of isoproterenol-induced myocardial damage is unknown , but a mismatch of oxygen supply vs. demand following coronary hypotension and myocardial hyperactivity is the best explanation for the complex morphological alterations observed .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial hyperactivity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Isoproterenol induces primary loss of dystrophin in rat hearts : correlation with myocardial injury .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: TCR protected against pathological changes induced by isoproterenol in rat heart .

## Item biored:test:27
Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , crocin in the mentioned dose could significantly attenuated learning and memory impairment in treated STZ-injected group in passive avoidance test .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "learning and memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STZ-injected", "type": "ChemicalEntity"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "ChemicalEntity"}, {"text": "scopolamine-", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Nefiracetam ( DM-9384 ) reverses apomorphine-induced amnesia of a passive avoidance response : delayed emergence of the memory retention effects .

## Item biored:test:126
Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: All but one of the mutations were detected within the BRCA1 gene .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genotyping was performed by kinetic polymerase chain-reaction or TaqMan assays .

Example answer:
{"entities": []}

Example input:
Sentence: The -930A > G polymorphism was genotyped using the TaqMan - Pre-designed SNP Genotyping Assay ( Applied Biosystems ) .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We genotyped the SNPs using TaqMan assays .

Example answer:
{"entities": []}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Patients were genotyped for rs4704559 , rs10942891 and rs4704560 by allelic discrimination with Taqman assays .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "rs4704559", "type": "SequenceVariant"}, {"text": "rs10942891", "type": "SequenceVariant"}, {"text": "rs4704560", "type": "SequenceVariant"}]}

Input:
Sentence: The two BRCA2 variants were analyzed by the TaqMan allelic discrimination technique .

## Item biored:test:157
Example input:
Sentence: Only subsets of genes located within given cytogenetic anomaly-intervals showed a concomitant change in mRNA expression level .

Example answer:
{"entities": []}

Example input:
Sentence: T > G exchange attenuated the transcriptional activity of the ARBS in an AR reporter gene assay .

Example answer:
{"entities": [{"text": "T > G", "type": "SequenceVariant"}, {"text": "ARBS", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Expression analysis on a cDNA panel from 17 different normal tissues by reverse transcription-PCR ( RT-PCR ) revealed tissue restricted mRNA expression of 2 of the 27 unknown antigens .

Example answer:
{"entities": []}

Example input:
Sentence: Co-transfection experiment of both wild-type and mutant plasmids indicated the dominant-negative mechanism of disease development ; as more of mutant DNA was transfected , VWF secretion was impaired in the media , whereas more of VWF was stored in the cell lysates .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The genes that showed consistent correlation between DNA copy number and RNA expression levels are likely to be important in MCL pathology .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: RNA sequencing was performed to identify global gene expression changes after ADAM12 knockdown .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also tested whether a G/A substitution at the G-395A site affected the transcription level in vitro through the dual-luciferase reporter assay .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "G-395A", "type": "SequenceVariant"}]}

Input:
Sentence: The effects of specific variants on expression of common markers were evaluated by in vitro transcription/translation .

## Item biored:test:136
Example input:
Sentence: After extraction , a microdialysis probe was placed at the surgical site for PGE2 and thromboxane B2 ( TXB2 ) measurements .

Example answer:
{"entities": [{"text": "PGE2", "type": "GeneOrGeneProduct"}, {"text": "thromboxane B2", "type": "ChemicalEntity"}, {"text": "TXB2", "type": "ChemicalEntity"}]}

Example input:
Sentence: restored the amplitude of PS that was attenuated by morphine injection .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: DESIGN : Dose response curves for nonsedating doses of morphine and CNSB002 given intraperitoneally alone and together in combinations were constructed for antihyperalgesic effect using paw withdrawal from noxious heat in two rat pain models : carrageenan-induced paw inflammation and streptozotocin ( STZ ) -induced diabetic neuropathy .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan-induced", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "STZ", "type": "ChemicalEntity"}, {"text": "diabetic neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The ED50 values for morphine when given in combination with CNSB002 ( 5 mg/kg ) were less than the maximum nonsedating dose : 0.56 ( 1.55 ) in the carrageenan model and 1.37 ( 1.23 ) in the neuropathy model ( mg/kg ; mean , SEM ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "carrageenan", "type": "ChemicalEntity"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Example input:
Sentence: The second group administered ZnSO ( 4 ) ( 0.1 micromol/10 microl normal saline , i.c.v , once ) then BCNU solvent ( i.v ) after 24 h. Third group received BCNU ( 20 mg/kg , i.v , once ) 24 h after injection with normal saline ( i.c.v ) .

Example answer:
{"entities": [{"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Example input:
Sentence: One week later , they received repeatedly vehicles ( saline , DMSO , saline+DMSO ) , scopolamine ( 2 microg/0.5 microl saline/side ; 30 min before training ) , ritanserin ( 2 , 4 and 8 microg/0.5 microl DMSO/side ; 20 min before training ) and scopolamine ( 2 microg/0.5 microl ; 30 min before ritanserin injection ) +ritanserin ( 4 microg/0.5 microl DMSO ) through cannulae each day .

Example answer:
{"entities": [{"text": "DMSO", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "DMSO/side", "type": "ChemicalEntity"}]}

Input:
Sentence: In a microdialysis study , 10 muL of saline ( group C ; n = 8 ) or 30 mug of morphine ( group M ; n = 8 ) was injected intrathecally ( IT ) 0.5 h after reflow , and 30 mug of morphine ( group SM ; n = 8 ) or 10 muL of saline ( group SC ; n = 8 ) was injected IT 0.5 h after sham operation .

## Item biored:test:14
Example input:
Sentence: Our results reveal that dominant mutations in BICD2 hyperactivate DDB motility and suggest that an imbalance of minus versus plus end-directed microtubule motility in neurons may underlie spinal muscular atrophy .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "spinal muscular atrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MC is clinically distinct from other multiple exostosis or multiple enchondromatosis syndromes and is unlinked to EXT1 and EXT2 , the genes responsible for autosomal dominant multiple osteochondromas ( MO ) .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple exostosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple enchondromatosis syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EXT1", "type": "GeneOrGeneProduct"}, {"text": "EXT2", "type": "GeneOrGeneProduct"}, {"text": "multiple osteochondromas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Point mutations in the BICD2 gene have been identified in patients with a dominant form of spinal muscular atrophy , but how these mutations cause disease is unknown .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "spinal muscular atrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in the desmin and the alpha-B crystallin genes account for approximately one third of the DRM cases .

Example answer:
{"entities": [{"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "alpha-B crystallin", "type": "GeneOrGeneProduct"}, {"text": "DRM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genetic basis of the other forms remain unknown , including the early-onset , recessive form with Mallory body-like inclusions ( MB-DRMs ) , first described in five related German patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Oculopharyngeal muscular dystrophy ( OPMD ) is a late onset autosomal dominant muscle disorder .

Example answer:
{"entities": [{"text": "Oculopharyngeal muscular dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant muscle disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the original MB-DRM German family , we demonstrated a linkage of the disease to the SEPN1 locus ( 1p36 ) , and subsequently a homozygous SEPN1 deletion ( del 92 nucleotide -19/+73 ) in the affected patients .

Example answer:
{"entities": [{"text": "SEPN1", "type": "GeneOrGeneProduct"}, {"text": "del 92 nucleotide -19/+73", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Myotonic dystrophy ( DM ) , the most prevalent muscular disorder in adults , is caused by ( CTG ) n-repeat expansion in a gene encoding a protein kinase ( DM protein kinase ; DMPK ) and involves changes in cytoarchitecture and ion homeostasis .

Example answer:
{"entities": [{"text": "Myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM protein kinase", "type": "GeneOrGeneProduct"}, {"text": "DMPK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Eighty unrelated individuals with Duchenne muscular dystrophy ( DMD ) or Becker muscular dystrophy ( BMD ) were found to have deletions in the major deletion-rich region of the DMD locus .

## Item biored:test:29
Example input:
Sentence: Nimodipine prevents memory impairment caused by nitroglycerin-induced hypotension in adult mice .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nitroglycerin-induced", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , crocin in the mentioned dose could significantly attenuated learning and memory impairment in treated STZ-injected group in passive avoidance test .

Example answer:
{"entities": [{"text": "crocin", "type": "ChemicalEntity"}, {"text": "learning and memory impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STZ-injected", "type": "ChemicalEntity"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Our findings show that microinjection of ritanserin into the CA1 region of the hippocampus improves the scopolamine-induced amnesia .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effect of ritanserin ( 5-HT2 antagonist ) on scopolamine ( muscarinic cholinergic antagonist ) -induced amnesia in Morris water maze ( MWM ) was investigated .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "5-HT2", "type": "GeneOrGeneProduct"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "muscarinic cholinergic", "type": "GeneOrGeneProduct"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Microinjection of ritanserin into the CA1 region of hippocampus improves scopolamine-induced amnesia in adult male rats .

Example answer:
{"entities": [{"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Given that apomorphine inhibits passive avoidance retention when given during training or in a defined 10-12h post-training period , we evaluated the ability of nefiracetam to attenuate amnesia induced by dopaminergic agonism .

## Item biored:test:95
Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , gene-targeted mice lacking SGK1 showed blunted volume retention , yet were not protected against renal fibrosis during experimental nephrotic syndrome .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "volume retention", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymorphism in manganese superoxide dismutase gene ( Mn-SOD ) is a new approach to identify its probable association with urolithiasis .

Example answer:
{"entities": [{"text": "manganese superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "Mn-SOD", "type": "GeneOrGeneProduct"}, {"text": "urolithiasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Puratrophin-1 -- normally expressed in a wide range of cells , including epithelial hair cells in the cochlea -- was aggregated in Purkinje cells of the chromosome 16q22.1-linked ADCA brains .

Example answer:
{"entities": [{"text": "Puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "ADCA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recent studies indicate that genetic ablation of mouse uroplakin ( UP ) III gene , which encodes a 47 kD urothelial-specific integral membrane protein forming urothelial plaques , causes VUR and hydronephrosis .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "uroplakin ( UP ) III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Hypomorphic mutations in meckelin ( MKS3/TMEM67 ) cause nephronophthisis with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "meckelin", "type": "GeneOrGeneProduct"}, {"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "nephronophthisis with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found 8 p53 mutations in 7/17 ( 41 % ) precancerous actinic keratosis ( AK ) , suggesting that p53 mutations are early events in RTR skin carcinogenesis .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "actinic keratosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After restricting the candidate region in chromosome 16q22.1 by haplotype analysis , we found that all patients from 52 unrelated Japanese families harbor a heterozygous C -- > T single-nucleotide substitution , 16 nt upstream of the putative translation initiation site of the gene for a hypothetical protein DKFZP434I216 , which we have called `` puratrophin-1 '' ( Purkinje cell atrophy associated protein-1 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "C -- > T", "type": "SequenceVariant"}, {"text": "DKFZP434I216", "type": "GeneOrGeneProduct"}, {"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "Purkinje cell atrophy associated protein-1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Fine mapping and identification of a candidate gene SSH1 in disseminated superficial actinic porokeratosis .

## Item biored:test:135
Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These changes , related to ischaemic injury , explain the severe alterations in the structural integrity of the sarcolemma of cardiomyocytes and hence severe and irreversible injury induced by isoproterenol .

Example answer:
{"entities": [{"text": "ischaemic injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Under isoflurane anesthesia , the MCA of 14 spontaneously hypertensive rats was occluded .

Example answer:
{"entities": [{"text": "isoflurane", "type": "ChemicalEntity"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , intraspinal injection of 5,7-DHT to produce a more selective lesion of only descending serotonin projections in the spinal cord did not affect this hypotension .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The brains were sectioned along coronal planes spanning the distribution of ischemia produced by MCAO .

Example answer:
{"entities": [{"text": "ischemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effect of induced hypertension instituted after a 2-h delay following middle cerebral artery occlusion ( MCAO ) on brain edema formation and histochemical injury was studied .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "middle cerebral artery occlusion", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "brain edema", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Spinal cord ischemia was induced by aortic occlusion for 6 min with a balloon catheter .

## Item biored:test:91
Example input:
Sentence: Male Wistar rats were challenged intragastrically once daily for 9 days with 1.0 ml/kg of corn oil containing vitamin D2 and cholesterol to induce atherosclerosis .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "corn oil", "type": "ChemicalEntity"}, {"text": "vitamin D2", "type": "ChemicalEntity"}, {"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "atherosclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At puberty ( P40 ) , half the PCPA-treated rats and half the saline-treated rats began treatment with testosterone ( T , 5 mg/kg , 5 days/week ) .

Example answer:
{"entities": [{"text": "PCPA-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol ( 100mg/kg ) was injected subcutaneously on the 13th and 14th days to induce acute myocardial infarction .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "acute myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Male Wistar rats were randomly assigned to one of 5 groups ( n=6 ) : normal control and groups were injected isoproterenol after chronic pre-treatment with 0 , 25 , 50 , or 100mg/kg of metformin twice daily for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

## Item biored:test:59
Example input:
Sentence: Serotonin was depleted beginning on postnatal day 26 with parachlorophenylalanine ( PCPA 100 mg/kg , every other day ) ; controls received saline .

Example answer:
{"entities": [{"text": "Serotonin", "type": "ChemicalEntity"}, {"text": "parachlorophenylalanine", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results showed that intracollicular microinjection of MK-801 and AP7 previous to systemic injections of haloperidol significantly attenuated the catalepsy , as indicated by a reduced latency to step down from a horizontal bar .

Example answer:
{"entities": [{"text": "MK-801", "type": "ChemicalEntity"}, {"text": "AP7", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The patient received bromocriptine and diazepam to treat his symptoms .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "bromocriptine", "type": "ChemicalEntity"}, {"text": "diazepam", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "ChemicalEntity"}, {"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "impairment of learning and memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Diazepam- , scopolamine- and ageing-induced amnesia served as the interoceptive behavioral models .

Example answer:
{"entities": [{"text": "Diazepam-", "type": "ChemicalEntity"}, {"text": "scopolamine-", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: According to annexin V binding , erythrocytes from patients indeed showed a significant increase of PS exposure within 1 week of treatment with azathioprine .

Example answer:
{"entities": [{"text": "annexin V", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PS", "type": "ChemicalEntity"}, {"text": "azathioprine", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The authors report here a depressed patient comorbid with postprandial dyspepsia who developed RLS after mirtazapine had been added to his domperidone therapy .

Example answer:
{"entities": [{"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "postprandial dyspepsia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RLS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mirtazapine", "type": "ChemicalEntity"}, {"text": "domperidone", "type": "ChemicalEntity"}]}

Input:
Sentence: When CPA , diazepam or 2PAM was given immediately after DFP-atropine , these treatments prevented , delayed or shortened the occurrence of serious signs of poisoning .

## Item biored:test:89
Example input:
Sentence: Dexrazoxane ( ICRF-187 ) is recommended for protection against anthracycline-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "Dexrazoxane", "type": "ChemicalEntity"}, {"text": "ICRF-187", "type": "ChemicalEntity"}, {"text": "anthracycline-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These findings indicate the synergistic protective effect of green tea and vitamin E during ISO induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "ChemicalEntity"}, {"text": "AraG", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "VP", "type": "ChemicalEntity"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CPM", "type": "ChemicalEntity"}, {"text": "T-cell leukaemia or lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Pharmacological evidence for the potential of Daucus carota in the management of cognitive dysfunctions .

Example answer:
{"entities": [{"text": "Daucus carota", "type": "OrganismTaxon"}, {"text": "cognitive dysfunctions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Photochemoprevention has been appreciated as a viable approach to reduce the occurrence of skin cancer and in recent years , the use of agents , especially botanical antioxidants , present in the common diet and beverages consumed by human population have gained considerable attention as photochemopreventive agents for human use .

Example answer:
{"entities": [{"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : 24 Rats were divided into 4 groups and received following treatments for 4 weeks ; Corn oil ( control ) , diazinon ( 15mg/kg per day , orally ) and crocin ( 12.5 and 25mg/kg per day , intraperitoneally ) in combination with diazinon ( 15 mg/kg ) .

Example answer:
{"entities": [{"text": "Rats", "type": "OrganismTaxon"}, {"text": "Corn oil", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "crocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: It is widely used in folk medicine to treat skin diseases in both humans and animals as well as the seed decoction has been used to treat diarrheas and inflammatory diseases .

Example answer:
{"entities": [{"text": "skin diseases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "diarrheas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory diseases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The ethanolic extract of Daucus carota seeds ( DCE ) was administered orally in three doses ( 100 , 200 , 400 mg/kg ) for seven successive days to different groups of young and aged mice .

Example answer:
{"entities": [{"text": "extract of Daucus carota seeds", "type": "ChemicalEntity"}, {"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Tincture of Crataegus ( TCR ) , an alcoholic extract of the berries of hawthorn ( Crataegus oxycantha ) , is used in herbal and homeopathic medicine .

## Item biored:test:33
Example input:
Sentence: However , scopolamine and ritanserin co-administration resulted in a significant decrease in escape latencies and traveled distances as compared to the scopolamine-treated rats .

Example answer:
{"entities": [{"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "ritanserin", "type": "ChemicalEntity"}, {"text": "scopolamine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: NDP-MSH time- and dose-dependently inhibited IRS-1 ( ser307 ) phosphorylation , effects also reversed by a specific melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: We suggest that trazodone ( 5 , 10 and 20 mg/kg ) , by blocking the 5-HT 2C receptors , releases the nigrostriatal DAergic neurons from tonic inhibition caused by 5-HT , and thereby potentiates dexamphetamine stereotypy and antagonizes haloperidol catalepsy .

Example answer:
{"entities": [{"text": "5-HT 2C", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "ChemicalEntity"}, {"text": "anxiety", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Dbh", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "disulfiram", "type": "ChemicalEntity"}, {"text": "dopamine beta-hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "DBH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Daily administration of desipramine , an inhibitor of the NET , for 5 days decreased [ ( 3 ) H ] norepinephrine uptake in the P2 fractions of hippocampus but not cortex , striatum or amygdalae .

Example answer:
{"entities": [{"text": "desipramine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}, {"text": "[ ( 3 ) H ] norepinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: These effects were not mediated by a dopaminergic mechanism as nefiracetam , at millimolar concentrations , failed to displace either [ 3H ] SCH 23390 or [ 3H ] spiperone binding from D1 or D2 dopamine receptor subtypes , respectively .

## Item biored:test:88
Example input:
Sentence: TIEG1 deficiency confers enhanced myocardial protection in the infarcted heart by mediating the Pten/Akt signalling pathway .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "infarcted heart", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Pten/Akt", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Isoproterenol induces primary loss of dystrophin in rat hearts : correlation with myocardial injury .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol ( 100mg/kg ) was injected subcutaneously on the 13th and 14th days to induce acute myocardial infarction .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "acute myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study was aimed to investigate the combined effects of green tea and vitamin E on heart weight , body weight , serum marker enzymes , lipid peroxidation , endogenous antioxidants and membrane bound ATPases in isoproterenol ( ISO ) -induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Cardioprotective effect of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings indicate the synergistic protective effect of green tea and vitamin E during ISO induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: ( Anacardiaceae ) , on isoproterenol ( ISPH ) -induced myocardial infarction ( MI ) in rats through its antioxidative mechanism .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "ISPH", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MI", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: Cardioprotective effect of tincture of Crataegus on isoproterenol-induced myocardial infarction in rats .

## Item biored:test:110
Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "ChemicalEntity"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV and HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A polymorphism of C-to-T substitution at -31 IL1B is associated with the risk of advanced gastric adenocarcinoma in a Japanese population .

Example answer:
{"entities": [{"text": "C-to-T substitution at -31", "type": "SequenceVariant"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "gastric adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Carriers of HLX1 SNP rs2738751 had lower IL-13 levels following Ppg-stimulation ( p = 0.08 ) .

Example answer:
{"entities": [{"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "Ppg-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Input:
Sentence: No association of IL12B polymorphisms and self-limited HCV infection could be demonstrated .

## Item biored:test:109
Example input:
Sentence: ADAM12 knockdown also diminished ALDEFLUOR ( + ) and CD44 ( hi ) /CD24 ( -/lo ) CSC-enriched populations in vitro and reduced tumorigenesis in mice in vivo .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although the sP120T substitution also impaired HBsAg secretion , it did not enhance the replication of LAM-resistant clones .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: In all clones with combined immune escape and LAM resistance mutations , the nucleotide analogues adefovir and tenofovir remained effective in suppressing viral replication in vitro .

Example answer:
{"entities": [{"text": "LAM", "type": "ChemicalEntity"}, {"text": "adefovir", "type": "ChemicalEntity"}, {"text": "tenofovir", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The minor allele ( A ) in IL10 rs1800872 , known to produce less interleukin-10 ( IL-10 ) , was associated with a higher risk of recurrence ( OR = 1.76 , 95 % CI : 1.00-3.10 ) , and the minor allele ( G ) in rs1800896 , known to produce more IL-10 , was associated with a lower risk of recurrence ( OR = 0.66 , 95 % CI : 0.48-0.91 ) .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "rs1800872", "type": "SequenceVariant"}, {"text": "interleukin-10", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "rs1800896", "type": "SequenceVariant"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Input:
Sentence: CONCLUSIONS : IL12B 3'-UTR 1188-C-allele carriers appear to be capable of responding more efficiently to antiviral combination therapy as a consequence of a reduced relapse rate .

## Item biored:test:128
Example input:
Sentence: Genetic polymorphism of the glutathione-S-transferase P1 gene ( GSTP1 ) and susceptibility to prostate cancer in the Kashmiri population .

Example answer:
{"entities": [{"text": "glutathione-S-transferase P1", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All but one of the mutations were detected within the BRCA1 gene .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Founder mutations in the BRCA1 gene in Polish families with breast-ovarian cancer .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We found no evidence of a significant modification of breast cancer penetrance in BRCA1 mutation carriers by either polymorphism .

## Item biored:test:139
Example input:
Sentence: Chemokine CCL2 and its receptor CCR2 are increased in the hippocampus following pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The increase of galactose concentration in the cerebrospinal fluid was several times lower after oral than after parenteral administration of the same galactose dose .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}]}

Example input:
Sentence: The ED50 values for morphine when given in combination with CNSB002 ( 5 mg/kg ) were less than the maximum nonsedating dose : 0.56 ( 1.55 ) in the carrageenan model and 1.37 ( 1.23 ) in the neuropathy model ( mg/kg ; mean , SEM ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "carrageenan", "type": "ChemicalEntity"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we investigated the effects of CCK-8 on long-term potentiation ( LTP ) in the lateral perforant path ( LPP ) -granule cell synapse of rat dentate gyrus ( DG ) in acute saline or morphine-treated rats .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "morphine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The present results demonstrate that CCK-8 attenuates the effect of morphine on hippocampal LTP through CCK2 receptors and suggest an ameliorative function of CCK-8 on morphine-induced memory impairment .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK2 receptors", "type": "GeneOrGeneProduct"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "memory impairment", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Cholecystokinin-octapeptide restored morphine-induced hippocampal long-term potentiation impairment in rats .

Example answer:
{"entities": [{"text": "Cholecystokinin-octapeptide", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The antinociception after morphine ( 3.2 mg/kg ) was increased by co-administration with CNSB002 from 28.0 and 31.7 % to 114.6 and 56.9 % reversal of hyperalgesia in the inflammatory and neuropathic models , respectively ( P < 0.01 ; one-way analysis of variance-significantly greater than either drug given alone ) .

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Acute morphine ( 30mg/kg , s.c. ) treatment significantly attenuated hippocampal LTP and CCK-8 ( 1ug , i.c.v . )

Example answer:
{"entities": [{"text": "morphine", "type": "ChemicalEntity"}, {"text": "CCK-8", "type": "ChemicalEntity"}]}

Example input:
Sentence: We have previously reported that CCK-8 significantly alleviated morphine-induced amnesia and reversed spine density decreases in the CA1 region of the hippocampus in morphine-treated animals .

Example answer:
{"entities": [{"text": "CCK-8", "type": "ChemicalEntity"}, {"text": "morphine-induced", "type": "ChemicalEntity"}, {"text": "amnesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "morphine-treated", "type": "ChemicalEntity"}]}

Input:
Sentence: After IT morphine , the cerebrospinal fluid ( CSF ) glutamate concentration was increased in group M relative to both baseline and group C ( P < 0.05 ) .

## Item biored:test:118
Example input:
Sentence: Carriers of TBX21 promoter SNP rs17250932 and HLX1 promoter SNP rs2738751 showed reduced or trendwise reduced ( p < 0.07 ) IL-5 , IL-13 and TNF-a secretion after LpA-stimulation .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "rs17250932", "type": "SequenceVariant"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Molecular analysis revealed that the mutant receptor had significantly impaired transactivation activity with a 2-fold reduction in affinity to ligand .

Example answer:
{"entities": []}

Example input:
Sentence: Like human TRPV6 , the truncated human TRPV6 ( Delta695-725 ) , which lacks the C-terminal domain required for Ca ( 2+ ) -calmodulin binding , does not form constitutive active channels , whereas the human TRPV6 ( D542A ) , carrying a point mutation in the presumed pore region , does not function as a channel .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "TRPV6", "type": "GeneOrGeneProduct"}, {"text": "Delta695-725", "type": "SequenceVariant"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}, {"text": "D542A", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we report a novel natural RTH mutation ( E333D ) located in the large carboxy-terminal ligand binding domain of TRbeta .

Example answer:
{"entities": [{"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , a dominant inhibition of the wild-type TRbeta counterpart transactivation function was observed on both a positive ( F2-TRE ) and a negative ( TSHalpha ) promoter .

Example answer:
{"entities": [{"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "TSHalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations T71N and A190T in hippocalcin did not affect stability , calcium-binding affinity or translocation to cellular membranes ( Ca2+/myristoyl switch ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "Ca2+/myristoyl", "type": "ChemicalEntity"}]}

Example input:
Sentence: In contrast , dialyzing 0.5 mm EGTA into TRPV6-expressing cells readily activated Ca ( 2+ ) inward currents , which were undetectable in non-transfected cells .

Example answer:
{"entities": [{"text": "EGTA", "type": "ChemicalEntity"}, {"text": "TRPV6-expressing", "type": "GeneOrGeneProduct"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , in transient transfection assays , the E333D TRbeta mutant exhibited impaired transcriptional regulation on two distinct positively regulated thyroid response elements ( F2- and DR4-TREs ) as well as on the negatively regulated human TSHalpha promoter .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "TSHalpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Expression of this mutant channel in tsA201 mammalian cells by site-directed mutagenesis revealed a persistent tetrodotoxin-sensitive but lidocaine-resistant current that was associated with a positive shift of the steady-state inactivation curve , steeper activation curve and faster recovery from inactivation .

## Item biored:test:170
Example input:
Sentence: A case-control study was conducted on incident gastric adenocarcinoma patients ( n=271 ) and age-gender frequency-matched control subjects ( n=271 ) .

Example answer:
{"entities": [{"text": "gastric adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: MATERIAL AND METHODS : This study was performed based on anesthesia records .

Example answer:
{"entities": []}

Example input:
Sentence: MATERIALS AND METHODS : The patients were examined using standard ophthalmic techniques .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : The passive avoidance ( PA ) paradigm was used to assess memory retention .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : All individuals in the study underwent a full clinical examination and the details of history were collected .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : In type 2 diabetic patients , cases who developed CAD were compared retrospectively with controls that did not .

Example answer:
{"entities": [{"text": "type 2 diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Further validation by population-based case-control studies and rigorous mechanistic studies is warranted .

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

Example input:
Sentence: DESIGN : Case-control study .

Example answer:
{"entities": []}

Input:
Sentence: DESIGN AND METHODS : The present analysis was a case control study .

## Item biored:test:112
Example input:
Sentence: In the classical form it presents as neonatal apnea , intractable seizures , and hypotonia , followed by significant psychomotor retardation .

Example answer:
{"entities": [{"text": "apnea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Drug-induced long QT syndrome is a serious adverse drug reaction .

Example answer:
{"entities": [{"text": "long QT syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Approximately 30 % of alleles causing genetic disorders generate premature termination codons ( PTCs ) , which are usually associated with severe phenotypes .

Example answer:
{"entities": []}

Example input:
Sentence: Recently , a lethal phenotype characterized by sudden infant death with dysgenesis of the testes syndrome ( SIDDT ) was identified to be caused by loss of function mutations in the TSPYL1 gene .

Example answer:
{"entities": [{"text": "sudden infant death with dysgenesis of the testes syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SIDDT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSPYL1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Women with a deletion allele had a significantly greater risk of preterm delivery [ adjusted odds ratio ( AOR ) : 3.0 ; 95 % CI : 1.0 , 8.8 ; P < 0.05 ] than did those without a deletion allele .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition to methadone dose , 15 demographic , biological , and pharmacological variables were considered as potential risk factors for QT prolongation .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Included were 5,128 CL/P cases , 1,745 CPO cases , and 3,712 controls ( like-sexed , non-malformed liveborn infant , born immediately after a malformed one , in the same hospital ) , over 4,199,630 consecutive births .

Example answer:
{"entities": [{"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Example input:
Sentence: Long QT syndrome can occur with low doses of methadone .

Example answer:
{"entities": [{"text": "Long QT syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Input:
Sentence: OBJECTIVE : Congenital long QT syndrome ( LQTS ) with in utero onset of the rhythm disturbances is associated with a poor prognosis .

## Item biored:test:87
Example input:
Sentence: IMPACT : This study supports that genetic variation in immune response and oxidation influence prostate cancer recurrence risk and suggests genetic variation in these pathways may inform prognosis .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study supports the hypothesis that inflammation is involved in prostate carcinogenesis and that sequence variation within the COX-2 gene influence the risk of prostate cancer .

Example answer:
{"entities": [{"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The purpose of this study was to analyze the value of germline and tumor thymidylate synthase ( TS ) genotyping as a prognostic marker in a series of colorectal cancer patients receiving adjuvant fluorouracil ( FU ) -based treatment .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil", "type": "ChemicalEntity"}, {"text": "FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The hazard of developing CAD ( 95 % CI ) associated with initial treatment increased by 2.4-fold ( 1.3-4.3 , P=0.004 ) with glibenclamide ; 2-fold ( 0.9-4.6 , P=0.099 ) with glipizide ; 2.9-fold ( 1.6-5.1 , P=0.000 ) with either , and was unchanged with metformin .

Example answer:
{"entities": [{"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glibenclamide", "type": "ChemicalEntity"}, {"text": "glipizide", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VIP ( -/- ) mice exhibit altered bladder function and neurochemical properties in micturition pathways after cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The cumulative discontinuation rate due to GI AEs was significantly lower with etoricoxib than diclofenac ( 5.2 vs 8.5 events per 100 patient-years , respectively ; hazard ratio 0.62 ( 95 % CI : 0.47 , 0.81 ; p < or=0.001 ) ) .

Example answer:
{"entities": [{"text": "GI AEs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "patient-years", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : We found a significantly higher PSA/GG distribution in PC ( 30 % ) than either benign prostatic hyperplasia ( BPH ) ( 18 % ) or population controls ( 16 % ) ( P = 0.025 ) .

Example answer:
{"entities": [{"text": "PSA/GG", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostatic hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSION : The results indicate a dose-response relationship between cyclophosphamide and the risk of bladder cancer , high cumulative risks in the entire cohort , and also the possibility of risk factors operating even before Wegener 's granulomatosis .

## Item biored:test:92
Example input:
Sentence: The present study was aimed to investigate the combined effects of green tea and vitamin E on heart weight , body weight , serum marker enzymes , lipid peroxidation , endogenous antioxidants and membrane bound ATPases in isoproterenol ( ISO ) -induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Metfromin markedly lowered isoproterenol-induced elevation in the levels of TLR4 mRNA , myeloid differentiation protein 88 ( MyD88 ) , tumor necrosis factor-alpha ( TNF-a ) , and interleukin 6 ( IL-6 ) in the heart tissues .

Example answer:
{"entities": [{"text": "Metfromin", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "myeloid differentiation protein 88", "type": "GeneOrGeneProduct"}, {"text": "MyD88", "type": "GeneOrGeneProduct"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "interleukin 6", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The mechanism of isoproterenol-induced myocardial damage is unknown , but a mismatch of oxygen supply vs. demand following coronary hypotension and myocardial hyperactivity is the best explanation for the complex morphological alterations observed .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "oxygen", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial hyperactivity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol induces primary loss of dystrophin in rat hearts : correlation with myocardial injury .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "aspartate transaminase", "type": "GeneOrGeneProduct"}, {"text": "creatine kinase", "type": "GeneOrGeneProduct"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "catalase", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "mitochondrial respiratory dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADP/O", "type": "ChemicalEntity"}, {"text": "isoproterenol-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

## Item biored:test:102
Example input:
Sentence: Carriers of HLX1 SNP rs2738751 had lower IL-13 levels following Ppg-stimulation ( p = 0.08 ) .

Example answer:
{"entities": [{"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "Ppg-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The minor allele ( A ) in IL10 rs1800872 , known to produce less interleukin-10 ( IL-10 ) , was associated with a higher risk of recurrence ( OR = 1.76 , 95 % CI : 1.00-3.10 ) , and the minor allele ( G ) in rs1800896 , known to produce more IL-10 , was associated with a lower risk of recurrence ( OR = 0.66 , 95 % CI : 0.48-0.91 ) .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "rs1800872", "type": "SequenceVariant"}, {"text": "interleukin-10", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "rs1800896", "type": "SequenceVariant"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Polymorphisms in TBX21 and HLX1 influenced primarily IL-5 and IL-13 secretion after LpA-stimulation in cord blood suggesting that genetic variations in the transcription factors essential for the T ( H ) 1-pathway may contribute to modified T ( H ) 2-immune responses already early in life .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Input:
Sentence: Influence of interleukin 12B ( IL12B ) polymorphisms on spontaneous and treatment-induced recovery from hepatitis C virus infection .

## Item biored:test:104
Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Homozygous carriers of HLX1 promoter SNP rs3806325 showed increased IL-13 and IL-6 ( unstimulated , p < 0.03 ) .

Example answer:
{"entities": [{"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs3806325", "type": "SequenceVariant"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Input:
Sentence: We investigated whether the IL12B polymorphisms within the promoter region ( 4 bp insertion/deletion ) and the 3'-UTR ( 1188-A/C ) , which have been reported to influence IL-12 synthesis , are associated with the outcome of HCV infection .

## Item biored:test:122
Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have undertaken a hospital-based study , to identify possible BRCA1 and BRCA2 founder mutations in the Polish population .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations of TP53 and dysfunction of the Brca1 and/or Brca2 tumor-suppressor proteins have been implicated in the molecular pathogenesis of a large fraction of OSCs , but frequent somatic mutations in other well-established tumor-suppressor genes have not been identified .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "Brca1", "type": "GeneOrGeneProduct"}, {"text": "Brca2", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Founder mutations in the BRCA1 gene in Polish families with breast-ovarian cancer .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The single family with a BRCA2 mutation had the breast-ovarian cancer syndrome .

Example answer:
{"entities": [{"text": "BRCA2", "type": "GeneOrGeneProduct"}, {"text": "breast-ovarian cancer syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Common BRCA2 variants and modification of breast and ovarian cancer risk in BRCA1 mutation carriers .
