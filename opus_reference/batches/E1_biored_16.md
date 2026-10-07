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

## Item biored:test:596
Example input:
Sentence: The androgen receptor ( AR ) gene has polymorphic regions containing variable length glutamine and glycine repeats and these are believed to be associated with PC risk .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A common missense variant in the gene encoding a component of the sulfonylurea receptor ( ABCC8 p.A1369S ) promotes closure of the target channel of sulfonylurea therapy and is associated with increased insulin secretion , thus mimicking the effects of sulfonylurea therapy .

Example answer:
{"entities": [{"text": "sulfonylurea receptor", "type": "GeneOrGeneProduct"}, {"text": "ABCC8", "type": "GeneOrGeneProduct"}, {"text": "p.A1369S", "type": "SequenceVariant"}, {"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Autosomal dominant cerebellar ataxia ( ADCA ) is a group of heterogeneous neurodegenerative disorders .

Example answer:
{"entities": [{"text": "Autosomal dominant cerebellar ataxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ADCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurodegenerative disorders", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our findings suggest that the G51S PNP polymorphism is associated with a faster rate of cognitive decline in AD patients , highlighting the important role of purine metabolism in the progression of this neurodegenerative disorder .

Example answer:
{"entities": [{"text": "G51S", "type": "SequenceVariant"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "neurodegenerative disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Aryl hydrocarbon receptor interacting protein ( AIP ) gene mutation analysis in children and adolescents with sporadic pituitary adenomas .

Example answer:
{"entities": [{"text": "Aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}, {"text": "pituitary adenomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast to alleles that cause early-onset MLD , the arginine84 to glutamine substitution is associated with some residual ARSA activity .

Example answer:
{"entities": [{"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine84 to glutamine", "type": "SequenceVariant"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Renal angiotensin II receptor type 2 ( AT2R ) gene expression in adult offspring was reduced by PCE , whereas the renal angiotensin II receptor type 1a ( AT1aR ) /AT2R expression ratio was increased .

Example answer:
{"entities": [{"text": "angiotensin II receptor type 2", "type": "GeneOrGeneProduct"}, {"text": "AT2R", "type": "GeneOrGeneProduct"}, {"text": "angiotensin II receptor type 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1aR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Adenosine A ( 2A ) receptor gene ( ADORA2A ) variants may increase autistic symptoms and anxiety in autism spectrum disorder .

## Item biored:test:654
Example input:
Sentence: Initial testing in a time-dependent forgetting task employing a 24-h delay between training and testing showed that metrifonate improved object recognition ( at 10 and 30 mg/kg , p.o .

Example answer:
{"entities": [{"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Group ADR+LOS ( 6 ) received losartan ( 10 mg/kg/b.w./day by gavages ) for 6 weeks and group ADR+LOS ( 12 ) for 12 weeks after second injection of ADR .

Example answer:
{"entities": [{"text": "ADR+LOS", "type": "ChemicalEntity"}, {"text": "losartan", "type": "ChemicalEntity"}, {"text": "ADR", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Mean ( SD ; maximum ) duration of treatment was 19.3 ( 10.3 ; 32.9 ) and 19.1 ( 10.4 ; 33.1 ) months in the etoricoxib and diclofenac groups , respectively .

Example answer:
{"entities": [{"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}]}

Example input:
Sentence: The median disease duration was 6 ( 7 ) years .

Example answer:
{"entities": []}

Example input:
Sentence: hiPS-CMs were seeded onto MEA and FPD was measured for 2min every 10min for 30min after drug exposure for the vehicle and each drug concentration .

Example answer:
{"entities": []}

Example input:
Sentence: Total follow-up on warfarin was 530 years ( mean 28 months ) .

Example answer:
{"entities": [{"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: In a prevention study , rats received 4 days of LF treatment followed by Dex and continued during the test period .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Patients who are more than 10 years post-OLTX have CRF and ESRD at a high rate .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ten consecutive patients ( mean age , 58.4 +/- 6.8 years ; 7 men , 3 women ) with similar characteristics at the duration of disease ( mean disease time , 8.4 +/- 3.5 years ) , disabling motor fluctuations ( Hoehn _ Yahr stage 3-5 in off-drug phases ) and levodopa-induced dyskinesias were selected .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The length of exposure to LAM and TDF varied from 4 to 216 months .

## Item biored:test:634
Example input:
Sentence: However , in transient transfection assays , the E333D TRbeta mutant exhibited impaired transcriptional regulation on two distinct positively regulated thyroid response elements ( F2- and DR4-TREs ) as well as on the negatively regulated human TSHalpha promoter .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "TSHalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Importantly , 35 % ( 6/17 ) are tandem mutations , including 4 UV signature CC to TT transitions possibly linked to modulated DNA repair caused by the immunosuppressive drug cyclosporin A ( CsA ) .

Example answer:
{"entities": [{"text": "CC to TT", "type": "SequenceVariant"}, {"text": "cyclosporin A", "type": "ChemicalEntity"}, {"text": "CsA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The C139T mutation , predicted to result in the substitution of an arginine by a tryptophan ( R47W ) in the N-terminal subdomain , affected conserved residues in the PAX9 paired domain .

Example answer:
{"entities": [{"text": "C139T", "type": "SequenceVariant"}, {"text": "arginine by a tryptophan", "type": "SequenceVariant"}, {"text": "R47W", "type": "SequenceVariant"}, {"text": "PAX9", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A heterozygous germline T to C transition in exon 10 of the TSHR gene ( c.1358T -- > C ) resulting in the substitution of methionine ( ATG ) by threonine ( ACG ) at codon 453 ( p.M453T ) was identified in the father and his two children .

Example answer:
{"entities": [{"text": "T to C", "type": "SequenceVariant"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}, {"text": "c.1358T -- > C", "type": "SequenceVariant"}, {"text": "methionine ( ATG ) by threonine ( ACG ) at codon 453", "type": "SequenceVariant"}, {"text": "p.M453T", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thyroid hormone receptor a mutation causes a severe and thyroxine-resistant skeletal dysplasia in female mice .

Example answer:
{"entities": [{"text": "Thyroid hormone receptor a", "type": "GeneOrGeneProduct"}, {"text": "thyroxine-resistant", "type": "ChemicalEntity"}, {"text": "skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Affected individuals are usually heterozygous for mutations in the thyroid hormone receptor beta gene ( TR-beta ) .

Example answer:
{"entities": [{"text": "thyroid hormone receptor beta", "type": "GeneOrGeneProduct"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel mutation ( E333D ) in the thyroid hormone beta receptor causing resistance to thyroid hormone syndrome .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "thyroid hormone beta receptor", "type": "GeneOrGeneProduct"}, {"text": "resistance to thyroid hormone syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: OBJECTIVE : Our objective was to report the molecular consequences of a novel splice-junction mutation and a novel missense mutation in the TSH-beta subunit gene found in two patients with congenital central hypothyroidism and conventional treatment-resistant anemia .

## Item biored:test:670
Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: A case-control study was conducted on incident gastric adenocarcinoma patients ( n=271 ) and age-gender frequency-matched control subjects ( n=271 ) .

Example answer:
{"entities": [{"text": "gastric adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: No effect of 5-HTTLPR or gender on memory function or MDMA use was observed .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Age-matched controls ( n = 14 ) were given only calcium .

Example answer:
{"entities": [{"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: Amphetamine abuse was predictive of larger cranial to body growth ratios .

Example answer:
{"entities": [{"text": "Amphetamine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Further analysis of G472A genotypes in Hispanic subjects with data stratified by gender identified a point-wise significant ( P = 0.049 ) association of G/A and A/A genotypes with opiate addiction in women , but not men .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: Ten consecutive patients ( mean age , 58.4 +/- 6.8 years ; 7 men , 3 women ) with similar characteristics at the duration of disease ( mean disease time , 8.4 +/- 3.5 years ) , disabling motor fluctuations ( Hoehn _ Yahr stage 3-5 in off-drug phases ) and levodopa-induced dyskinesias were selected .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Among the subjects treated with methadone , 28 % men and 32 % women had prolonged QTc interval .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "prolonged QTc interval", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The age and sex of the control subjects did not differ from those of the methamphetamine dependence patients .

## Item biored:test:609
Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ecstasy-specific hypoactivity was evident in the right dorsal anterior cingulated cortex ( ACC ) and left posterior cingulated cortex .

Example answer:
{"entities": [{"text": "Ecstasy-specific", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results provide evidence for a possible mechanistic role of oxidative and nitrosative stress and NFkappaB in the alterations induced by cocaine .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Repeated administration of cocaine induces up-regulation of hippocampal NET function .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}, {"text": "NET", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Severe reversible left ventricular systolic and diastolic dysfunction due to accidental iatrogenic epinephrine overdose .

Example answer:
{"entities": [{"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "epinephrine", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : In patients with FHF and cerebral edema from acetaminophen overdose , prolonged therapeutic hypothermia could potentially be used as a life saving therapy and a bridge to hepatic and neurological recovery .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged hypothermia as a bridge to recovery for cerebral edema and intracranial hypertension associated with fulminant hepatic failure .

Example answer:
{"entities": [{"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Progressive abstinence from cocaine was associated with worsening of all measured polysomnographic sleep outcomes .

Example answer:
{"entities": [{"text": "cocaine", "type": "ChemicalEntity"}]}

Example input:
Sentence: As heroin addicts sometimes faint while using illicit drugs , doctors might attribute too many episodes of syncope to illicit drug use and thereby underestimate the incidence of TdP in this special population , and the high mortality in this population may , in part , be caused by the proarrhythmic effect of methadone .

Example answer:
{"entities": [{"text": "heroin addicts", "type": "DiseaseOrPhenotypicFeature"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Input:
Sentence: In our patient , transient cardiac arrhythmia or respiratory dysfunction related to cocaine and/or ethanol use were the most likely causes of cerebral hypoperfusion .

## Item biored:test:681
Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotyping was determined by the polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) technique .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: A single nucleotide polymorphism at position 388 of the FGFR4 amino-acid sequence results in the substitution of glycine ( Gly ) with arginine ( Arg ) and higher frequency of the ArgArg genotype was previously found in prostate cancer patients .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "glycine ( Gly ) with arginine ( Arg )", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Our tetra-primer PCR assay is sensitive , low-cost , and easy to use method for FGFR3 p.G380R genotyping , which could be used even in `` low-tech '' laboratories .

Example answer:
{"entities": [{"text": "FGFR3", "type": "GeneOrGeneProduct"}, {"text": "p.G380R", "type": "SequenceVariant"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Patients were genotyped for rs4704559 , rs10942891 and rs4704560 by allelic discrimination with Taqman assays .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "rs4704559", "type": "SequenceVariant"}, {"text": "rs10942891", "type": "SequenceVariant"}, {"text": "rs4704560", "type": "SequenceVariant"}]}

Example input:
Sentence: Genotyping was performed by kinetic polymerase chain-reaction or TaqMan assays .

Example answer:
{"entities": []}

Example input:
Sentence: The -930A > G polymorphism was genotyped using the TaqMan - Pre-designed SNP Genotyping Assay ( Applied Biosystems ) .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: We genotyped the SNPs using TaqMan assays .

Example answer:
{"entities": []}

Input:
Sentence: FGG genotypes were determined by exonuclease ( TaqMan ) assays .

## Item biored:test:617
Example input:
Sentence: A multiple logistic regression analysis indicated that the odds ratio for EH in the -395A allele carriers as compared with the control group was 0.593 ( P=0.024 ) after adjusting for current traditional risk factors .

Example answer:
{"entities": [{"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-395A", "type": "SequenceVariant"}]}

Example input:
Sentence: L1503R is a member of group I mutation and has dominant-negative effect on secretion of full-length VWF multimers : an analysis of two patients with type 2A von Willebrand disease .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "VWF", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "type 2A von Willebrand disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Studies of additional cases yielded a second set of data that , in combination with the first set , confirmed a weak association of UP III SNP7 in VUR ( P= 0.036 adjusted for both subsets of cases vs. controls ) .

Example answer:
{"entities": [{"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VNTR and ins/del 6 bp genotypes varied with tumour anatomical site : 2R/2R genotype was rare in left-sided tumours ( 7.0 % vs. 26.3 % of right-sided and 24.1 % of rectal cancers ; P < 0.01 ) , where the variant allele 6- was very frequent ( 69.0 % ) .

Example answer:
{"entities": [{"text": "ins/del 6 bp", "type": "SequenceVariant"}, {"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumours", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rectal cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , SNP1 of UP Ia gene affecting a C to T conversion and an Ala7Val change , and SNP7 of UP III affecting a C to G conversion and a Pro154Ala change , were marginally associated with VUR ( both P= 0.08 ) .

Example answer:
{"entities": [{"text": "UP Ia", "type": "GeneOrGeneProduct"}, {"text": "C to T", "type": "SequenceVariant"}, {"text": "Ala7Val", "type": "SequenceVariant"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "C to G", "type": "SequenceVariant"}, {"text": "Pro154Ala", "type": "SequenceVariant"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Input:
Sentence: VDR overexpression was significantly associated with KRAS mutation ( odds ratio , 1.55 ; 95 % confidence interval , 1.11-2.16 ) and PIK3CA mutation ( odds ratio , 2.17 ; 95 % confidence interval , 1.36-3.47 ) , both of which persisted in multivariate logistic regression analysis .

## Item biored:test:625
Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "enflurane", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The doses calculated to cause 50 % reversal of hyperalgesia ( ED50 ) were 7.54 ( 1.81 ) and 4.83 ( 1.54 ) in the carrageenan model and 44.18 ( 1.37 ) and 9.14 ( 1.24 ) in the STZ-induced neuropathy model for CNSB002 and morphine , respectively ( mg/kg ; mean , SEM ) .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "carrageenan", "type": "ChemicalEntity"}, {"text": "STZ-induced", "type": "ChemicalEntity"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients with essential hypertension ( mean sitting diastolic BP [ MSDBP ] , > or =95 mm Hg and < 110 mm Hg ) were randomized to 1 of 8 treatment groups : VAL 160 or 320 mg ; HCTZ 12.5 or 25 mg ; VAL/HCTZ 160/12.5 , 320/12.5 , or 320/25 mg ; or placebo .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Omission of fentanyl did not reduce the overall incidence of postoperative nausea and vomiting , but did reduce the incidence of vomiting and/or moderate to severe nausea prior to discharge from 20 % and 17 % with fentanyl and fentanyl-dexamethasone , respectively , to 5 % ( P = 0.013 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "ChemicalEntity"}, {"text": "postoperative nausea and vomiting", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vomiting", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nausea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fentanyl-dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combining the two fentanyl groups revealed further significant benefits from the avoidance of opioids , reducing postoperative nausea and vomiting and nausea prior to discharge from 35 % and 33 % to 22 % and 19 % ( P = 0.049 and P = 0.035 ) , respectively , while nausea in the first 24 h was decreased from 42 % to 27 % ( P = 0.034 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "ChemicalEntity"}, {"text": "postoperative nausea and vomiting", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nausea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients who received the same anesthetic procedure were selected : 2 minutes after intravenous injections of the pretreatment drugs , anesthesia is induced with 0.3 mg.kg-1 etomidate injected intravenously over a period of 20-30 seconds .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "etomidate", "type": "ChemicalEntity"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Depending on the drugs that would be given before the induction of anesthesia with etomidate , the patients were separated into 4 groups : no pretreatment ( Group NP ) , fentanyl 1 ug.kg-1 ( Group F ) , midazolam 0.03 mg.kg-1 ( Group M ) , and midazolam 0.015 mg.kg-1 + fentanyl 0.5 ug.kg-1 ( Group FM ) .

Example answer:
{"entities": [{"text": "etomidate", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fentanyl", "type": "ChemicalEntity"}, {"text": "midazolam", "type": "ChemicalEntity"}]}

Input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

## Item biored:test:621
Example input:
Sentence: This heterozygous phenotype illustrates that subtle changes in receptor tyrosine kinase signalling can have significant effects , perhaps providing an explanation for the numerous changes seen in cancer .

Example answer:
{"entities": [{"text": "receptor tyrosine kinase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found 8 p53 mutations in 7/17 ( 41 % ) precancerous actinic keratosis ( AK ) , suggesting that p53 mutations are early events in RTR skin carcinogenesis .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "actinic keratosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Mammalian Ras genes regulate diverse cellular processes including proliferation and differentiation and are frequently mutated in human cancers .

Example answer:
{"entities": [{"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesized that Thra1 ( PV/+ ) mice could be used to predict the skeletal outcome of human THRA mutations and determine whether prolonged treatment with a supraphysiological dose of T4 ameliorates the skeletal abnormalities .

Example answer:
{"entities": [{"text": "Thra1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "THRA", "type": "GeneOrGeneProduct"}, {"text": "T4", "type": "ChemicalEntity"}, {"text": "skeletal abnormalities", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As expected , tumors and cell lines with NF1 defects lacked mutations in KRAS or BRAF but showed Ras pathway activation based on immunohistochemical detection of phosphorylated MAPK ( primary tumors ) or increased levels of GTP-bound Ras ( cell lines ) .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "KRAS", "type": "GeneOrGeneProduct"}, {"text": "BRAF", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "GTP-bound", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , PI3K/Akt pathway signaling was also increased in Eu-myc B cells , and this increase was partially suppressed with ibrutinib .

Example answer:
{"entities": [{"text": "PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "ibrutinib", "type": "ChemicalEntity"}]}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential downstream signaling pathway involving phosphatidylinositol 3-kinase ( PI3K ) /threonine protein kinase B ( Akt ) /mammalian target of rapamycin ( mTOR ) was identifiedby western blot analysis .

Example answer:
{"entities": [{"text": "phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "target of rapamycin", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Our data support potential interactions between the VDR , RAS-MAPK and PI3K-AKT pathways , and possible influence by KRAS or PIK3CA mutation on therapy or chemoprevention targeting VDR .

## Item biored:test:660
Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-containing", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In all clones with combined immune escape and LAM resistance mutations , the nucleotide analogues adefovir and tenofovir remained effective in suppressing viral replication in vitro .

Example answer:
{"entities": [{"text": "LAM", "type": "ChemicalEntity"}, {"text": "adefovir", "type": "ChemicalEntity"}, {"text": "tenofovir", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: Immune escape variants of the hepatitis B virus ( HBV ) represent an emerging clinical challenge , because they can be associated with vaccine escape , HBV reactivation , and failure of diagnostic tests .

Example answer:
{"entities": [{"text": "hepatitis B virus", "type": "OrganismTaxon"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: Although the sP120T substitution also impaired HBsAg secretion , it did not enhance the replication of LAM-resistant clones .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: These findings reveal the differential impact of immune escape variants on the replication and drug susceptibility of complex HBV mutants , supporting the need of close surveillance and treatment adjustment in response to the selection of distinct mutational patterns .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Input:
Sentence: The data suggest that prolonged LAM use is associated with the emergence of particular changes in the HBV genome , including substitutions that may elicit a vaccine escape phenotype .

## Item biored:test:620
Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PCR-amplified VLCAD cDNAs were sequenced in cultured fibroblasts from two VLCAD-deficient patients .

Example answer:
{"entities": [{"text": "VLCAD", "type": "GeneOrGeneProduct"}, {"text": "VLCAD-deficient", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: However , SNP1 of UP Ia gene affecting a C to T conversion and an Ala7Val change , and SNP7 of UP III affecting a C to G conversion and a Pro154Ala change , were marginally associated with VUR ( both P= 0.08 ) .

Example answer:
{"entities": [{"text": "UP Ia", "type": "GeneOrGeneProduct"}, {"text": "C to T", "type": "SequenceVariant"}, {"text": "Ala7Val", "type": "SequenceVariant"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "C to G", "type": "SequenceVariant"}, {"text": "Pro154Ala", "type": "SequenceVariant"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: VNTR and ins/del 6 bp genotypes varied with tumour anatomical site : 2R/2R genotype was rare in left-sided tumours ( 7.0 % vs. 26.3 % of right-sided and 24.1 % of rectal cancers ; P < 0.01 ) , where the variant allele 6- was very frequent ( 69.0 % ) .

Example answer:
{"entities": [{"text": "ins/del 6 bp", "type": "SequenceVariant"}, {"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumours", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rectal cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Input:
Sentence: In conclusion , VDR overexpression in colorectal cancer is independently associated with PIK3CA and KRAS mutations .

## Item biored:test:585
Example input:
Sentence: In a double-blind 6-week trial , 458 patients with acute schizophrenia were randomly assigned to fixed-dose treatment with asenapine at 5 mg twice daily ( BID ) , asenapine at 10 mg BID , placebo , or haloperidol at 4 mg BID ( to verify assay sensitivity ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Twenty-five women were given raloxifene hydrochloride ( 60 mg/day ) plus calcium ( 500 mg/day ) .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "raloxifene hydrochloride", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Short- and intermediate-term treatment with therapeutic ( 10 or 20 mg daily ) and supratherapeutic ( 40 or 80 mg daily ) valdecoxib doses was not associated with an increased incidence of thrombotic events relative to nonselective NSAIDs or placebo in osteoarthritis and rheumatoid arthritis patients in controlled clinical trials .

Example answer:
{"entities": [{"text": "valdecoxib", "type": "ChemicalEntity"}, {"text": "thrombotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NSAIDs", "type": "ChemicalEntity"}, {"text": "osteoarthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rheumatoid arthritis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: PATIENTS AND METHODS : A total of 4086 patients ( mean age 60.8 years ) diagnosed with RA were enrolled and received etoricoxib 90 mg daily ( n = 2032 ) or diclofenac 75 mg twice daily ( n = 2054 ) .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the 10th day of paroxetine and alprazolam treatment , the patient exhibited marked psychomotor retardation , disorientation , and severe muscle rigidity with tremors .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "psychomotor retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tremors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Medical treatment was initiated at a daily dose of 20 mg paroxetine and 1.2 mg alprazolam .

Example answer:
{"entities": [{"text": "paroxetine", "type": "ChemicalEntity"}, {"text": "alprazolam", "type": "ChemicalEntity"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "atazanavir", "type": "ChemicalEntity"}]}

Input:
Sentence: On admission the patient was taking carvedilol 12 mg twice daily , warfarin 2 mg/day , folic acid 1 mg/day , levothyroxine 100 microg/day , pantoprazole 40 mg/day , paroxetine 40 mg/day , and flecainide 100 mg twice daily .

## Item biored:test:639
Example input:
Sentence: Sequencing of the GJB2 gene showed that the child was heterozygous for a novel nucleotide change , c.263C > T , in exon 2 , leading to a substitution of alanine for valine at position 88 ( p.Ala88Val ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "alanine for valine at position 88", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Direct sequencing of the encoding regions of the candidate genes revealed a heterozygous mutation c.592C -- > T in exon 2 of the gap junction protein , alpha 8 ( GJA8 ) gene .

Example answer:
{"entities": [{"text": "c.592C -- > T", "type": "SequenceVariant"}, {"text": "gap junction protein , alpha 8", "type": "GeneOrGeneProduct"}, {"text": "GJA8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The second mutation is the di-nucleotide substitution c.467C > A and c.468C > T in exon 3 that causes the missense mutation A118D in the SEA domain of the extracellular stem region of matriptase-2 .

Example answer:
{"entities": [{"text": "c.467C > A", "type": "SequenceVariant"}, {"text": "c.468C > T", "type": "SequenceVariant"}, {"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Molecular characterization by DNA sequencing analysis and multiplex ligation-dependent probe amplification of the MLYCD gene revealed a heterozygous mutation ( c.920T > G , p.Leu307Arg ) in the patient and his father and a heterozygous deletion comprising exon 1 in the patient and his mother .

Example answer:
{"entities": [{"text": "MLYCD", "type": "GeneOrGeneProduct"}, {"text": "c.920T > G", "type": "SequenceVariant"}, {"text": "p.Leu307Arg", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: The single nucleotide substitution I280S ( 1123T -- > G ) was present either on both alleles or in a hemizygous form with complete deletion of the second allele .

Example answer:
{"entities": [{"text": "I280S", "type": "SequenceVariant"}, {"text": "1123T -- > G", "type": "SequenceVariant"}]}

Example input:
Sentence: The compound heterozygous mutations , c.892C > T and c.1072T > C , were identified in exon 3 of CHST6 in three patients .

Example answer:
{"entities": [{"text": "c.892C > T", "type": "SequenceVariant"}, {"text": "c.1072T > C", "type": "SequenceVariant"}, {"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The I280S mutation was recently reported in a heterozygous patient .

Example answer:
{"entities": [{"text": "I280S", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Input:
Sentence: In patient 2 , sequence analysis revealed a compound heterozygosis for the already reported 313delT ( C105Vfs114X ) mutation and for a second novel mutation in exon 3 , substituting G for A at cDNA nucleotide position 323 , resulting in a C88Y change .

## Item biored:test:640
Example input:
Sentence: In its regulatory subunit , p85alpha , there is a common amino acid substitution ( the Met326Ile polymorphism ) , and this amino acid may be crucial for the function of the p85alpha regulatory subunit and PI3-kinase .

Example answer:
{"entities": [{"text": "p85alpha", "type": "GeneOrGeneProduct"}, {"text": "Met326Ile", "type": "SequenceVariant"}, {"text": "PI3-kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In that allele arginine84 , a residue that is highly conserved in the arylsulfatase gene family , is replaced by glutamine .

Example answer:
{"entities": [{"text": "arginine84", "type": "SequenceVariant"}, {"text": "arylsulfatase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Pituitary adenoma predisposition ( PAP ) has been recently associated with germline mutations in the aryl hydrocarbon receptor interacting protein ( AIP ) gene .

Example answer:
{"entities": [{"text": "Pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have shown previously that , in sheep primary pituitary cells , bone morphogenetic proteins ( BMP ) -4 inhibits FSHbeta mRNA expression and FSH release .

Example answer:
{"entities": [{"text": "sheep", "type": "OrganismTaxon"}, {"text": "bone morphogenetic proteins ( BMP ) -4", "type": "GeneOrGeneProduct"}, {"text": "FSHbeta", "type": "GeneOrGeneProduct"}, {"text": "FSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: cDNA sequence and chromosomal localization of the remaining three human nuclear encoded iron sulphur protein ( IP ) subunits of complex I : the human IP fraction is completed .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "nuclear encoded iron sulphur protein ( IP ) subunits of complex I", "type": "GeneOrGeneProduct"}, {"text": "IP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The androgen receptor ( AR ) gene has polymorphic regions containing variable length glutamine and glycine repeats and these are believed to be associated with PC risk .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The D2267 residue is predicted to coordinate binding of a calcium ion , which influences the conformational binding loops of the C-type lectin domain that mediate interactions with tenascins and other extracellular-matrix proteins .

Example answer:
{"entities": [{"text": "D2267", "type": "SequenceVariant"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: The full-length puratrophin-1 mRNA had an open reading frame of 3,576 nt , predicted to contain important domains , including the spectrin repeat and the guanine-nucleotide exchange factor ( GEF ) for Rho GTPases , followed by the Dbl-homologous domain , which indicates the role of puratrophin-1 in intracellular signaling and actin dynamics at the Golgi apparatus .

Example answer:
{"entities": [{"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "guanine-nucleotide exchange factor", "type": "GeneOrGeneProduct"}, {"text": "GEF", "type": "GeneOrGeneProduct"}, {"text": "Rho GTPases", "type": "GeneOrGeneProduct"}, {"text": "actin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This cysteine residue is conserved among all dimeric pituitary and placental glycoprotein hormone-beta subunits .

## Item biored:test:653
Example input:
Sentence: Eighty-seven percent of the patients had received immunomodulatory drugs included in some line of therapy before bort-dex .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Bort-dex was an effective salvage treatment for MM patients , particularly for those in first relapse .

Example answer:
{"entities": [{"text": "Bort-dex", "type": "ChemicalEntity"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : One hundred and fifty-eight patients with wet AMD , 80 patients with soft drusen , and 220 matched control subjects were recruited among Han Chinese in mainland China .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This retrospective study examines the incidence and treatment of ESRD and chronic renal failure ( CRF ) in OLTX patients .

Example answer:
{"entities": [{"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Chronic administration of LF strongly reduced the blood pressure and production of ROS and improved antioxidant capacity in Dex-induced hypertension , suggesting the role of inhibition of oxidative stress as another mechanism of antihypertensive action of LF .

Example answer:
{"entities": [{"text": "LF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "Dex-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: However , a 38 % remission rate has been recently reported in refractory MCL treated with temsirolimus , a mTOR inhibitor.Here we had the opportunity to study a case of refractory MCL who had tumor regression two months after temsirolimus treatment , and a progression-free survival of 10 months .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "temsirolimus", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This retrospective study investigated the combination of bort ( 1.3 mg/m ( 2 ) on days 1 , 4 , 8 , and 11 every 3 weeks ) and dex ( 20 mg on the day of and the day after bort ) as salvage treatment in 85 patients with R/R MM after prior autologous stem cell transplantation or conventional chemotherapy .

Example answer:
{"entities": [{"text": "bort", "type": "ChemicalEntity"}, {"text": "dex", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : One hundred twenty-nine colorectal cancer patients homogeneously treated with FU plus levamisole or leucovorin in the adjuvant setting were included .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "FU", "type": "ChemicalEntity"}, {"text": "levamisole", "type": "ChemicalEntity"}, {"text": "leucovorin", "type": "ChemicalEntity"}]}

Input:
Sentence: Eighteen patients were treated with LAM and six patients were treated with LAM plus TDF .

## Item biored:test:693
Example input:
Sentence: A 14-year-old girl is reported with recurrent , azithromycin-induced , acute interstitial nephritis .

Example answer:
{"entities": [{"text": "azithromycin-induced", "type": "ChemicalEntity"}, {"text": "interstitial nephritis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we establish the unilateral ureteric obstruction ( UUO ) or folic acid ( FA ) -induced mice renal interstitial fibrosis in vivo and the transforming growth factor ( TGF ) -beta1-stimulated human proximal tubular epithelial cell ( HK-2 ) model in vitro .

Example answer:
{"entities": [{"text": "unilateral ureteric obstruction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "UUO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "folic acid", "type": "ChemicalEntity"}, {"text": "FA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor ( TGF )", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: Histopathological examination revealed severe renal damage such as proteinaceous casts in tubuli and tubular expansion in the kidney of control rats , while an improvement of the damage was seen in antithrombin-treated rats .

Example answer:
{"entities": [{"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "antithrombin-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: These results demonstrated that PCE could induce dysplasia of fetal kidneys as well as glomerulosclerosis of adult offspring , and the low functional programming of renal AT2R might mediate the developmental origin of adult glomerulosclerosis .

Example answer:
{"entities": [{"text": "dysplasia of fetal kidneys", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AT2R", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results revealed that the adult offspring kidneys in the PCE group exhibited glomerulosclerosis as well as interstitial fibrosis , accompanied by elevated levels of serum creatinine and urine protein .

Example answer:
{"entities": [{"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fetal kidneys in the PCE group displayed an enlarged Bowman 's space and a shrunken glomerular tuft , accompanied by a reduced cortex width and an increase in the nephrogenic zone/cortical zone ratio .

Example answer:
{"entities": []}

Example input:
Sentence: Patients developing ESRD had a 6-year survival after onset of ESRD of 27 % for the patients receiving hemodialysis versus 71.4 % for the patients developing ESRD who subsequently received kidney transplants .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: About 1 year later , abdominal computed tomography revealed enlargement of kidneys .

## Item biored:test:700
Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Homozygous mutations in PLCE1 ( also known as KIAA1516 , PLCE , or NPHS3 ) were identified following genome-wide mapping of single-nucleotide polymorphisms .

Example answer:
{"entities": [{"text": "PLCE1", "type": "GeneOrGeneProduct"}, {"text": "KIAA1516", "type": "GeneOrGeneProduct"}, {"text": "PLCE", "type": "GeneOrGeneProduct"}, {"text": "NPHS3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We established a hrMCA method to screen for COL3A1 mutations using genomic DNA .

## Item biored:test:680
Example input:
Sentence: We analysed data from 23,868 men with prostate cancer and 23,051 controls from 25 studies within the international PRACTICAL Consortium .

Example answer:
{"entities": [{"text": "men", "type": "OrganismTaxon"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : This study included 133 patients with AVSD and 200 healthy controls .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : One hundred PC patients and an age matched cohort of 79 benign prostate hyperplasia and 67 population controls were entered in this study .

Example answer:
{"entities": [{"text": "PC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We therefore conducted a case-control study with 515 incident lung cancer cases and 1030 age- and sex-matched controls without cancer , and further conducted a meta-analysis .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A case-control study was conducted on incident gastric adenocarcinoma patients ( n=271 ) and age-gender frequency-matched control subjects ( n=271 ) .

Example answer:
{"entities": [{"text": "gastric adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: METHODS : A case-control study was carried out in Chinese Han population , including 368 cases of migraine and 517 controls .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We analyzed a large population-based case-control study , cancer prostate in Sweden ( CAPS ) consisting of 1,378 cases and 782 controls .

Example answer:
{"entities": [{"text": "cancer prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Input:
Sentence: The study was designed as case-control study including 891 patients with documented PAD and 777 control subjects .

## Item biored:test:696
Example input:
Sentence: Identification of novel type VII collagen gene mutations resulting in severe recessive dystrophic epidermolysis bullosa .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genomic DNA was extracted from peripheral leukocytes from six affected and three unaffected members of a family with lattice corneal dystrophy type I. Exon 4 of the transforming growth factor-induced gene ( TGFBI ) was screened for the most frequent mutation , R124C , in the proband by sequencing .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor-induced gene", "type": "GeneOrGeneProduct"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "R124C", "type": "SequenceVariant"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Genomic DNA was screened for GLDC , AMT , and GCSH gene mutations .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "AMT", "type": "GeneOrGeneProduct"}, {"text": "GCSH", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: A novel mutation screening system for Ehlers-Danlos Syndrome , vascular type by high-resolution melting curve analysis in combination with small amplicon genotyping using genomic DNA .

## Item biored:test:650
Example input:
Sentence: HBV viral load was performed with Amplicor HBV Monitor test v2.0 ( Roche Diagnostics , Penzberg , Germany ) .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings reveal the differential impact of immune escape variants on the replication and drug susceptibility of complex HBV mutants , supporting the need of close surveillance and treatment adjustment in response to the selection of distinct mutational patterns .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "ChemicalEntity"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV and HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum samples were PCR amplified with HBV reverse transcriptase ( RT ) primers , followed by direct sequencing across the tyrosine-methionine-aspartate-aspartate ( YMDD ) motif of the major catalytic region in the C domain of the HBV RT enzyme .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: However , the concomitant occurrence of HBeAg negativity ( PC/BCP ) , sP120T , and LAM resistance resulted in the restoration of replication to levels of wild-type HBV .

Example answer:
{"entities": [{"text": "HBeAg", "type": "ChemicalEntity"}, {"text": "PC/BCP", "type": "GeneOrGeneProduct"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: HBV genotypes/subgenotypes , antiviral resistance , basal core promoter ( BCP ) , and precore mutations were detected by DNA sequencing .

## Item biored:test:701
Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , p53 codon 72 or frequencies of three XPD genotypes of RTRs are comparable with control populations .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "XPD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: Three aberrantly spliced cDNA species were identified : exon 22 and exon 22 to 23 skipping , and insertion of an 87-base pair cryptic exon .

Example answer:
{"entities": []}

Example input:
Sentence: Specific PRC primers were designed to amplify all 14 exons of the HGD gene with the flanking intronic sequences including the splice site sequences .

Example answer:
{"entities": [{"text": "HGD", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: PCR primers pairs for COL3A1 ( 52 amplicons ) were designed to cover all coding regions of the 52 exons , including the splicing sites .

## Item biored:test:698
Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: HPV DNA was detected in 78 % of skin lesions ( 60 % Basal Cell Carcinomas , 82 % AK and 79 % SCCs ) .

Example answer:
{"entities": [{"text": "HPV", "type": "OrganismTaxon"}, {"text": "skin lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Basal Cell Carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have analyzed skin lesions from RTRs with aggressive tumors for p53 gene modifications , the presence of Human Papillomas Virus ( HPV ) DNA in relation to the p53 codon 72 genotype and polymorphisms of the XPD repair gene .

Example answer:
{"entities": [{"text": "skin lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "Human Papillomas Virus", "type": "OrganismTaxon"}, {"text": "HPV", "type": "OrganismTaxon"}, {"text": "XPD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Skin biopsy revealed widening of intercellular spaces in the epidermis and a reduced number of small , poorly formed desmosomes .

Example answer:
{"entities": []}

Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transmission electron microscopy showed that fibroblasts carrying the c.474delA mutation form typical caveolae .

Example answer:
{"entities": [{"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: We found 8 p53 mutations in 7/17 ( 41 % ) precancerous actinic keratosis ( AK ) , suggesting that p53 mutations are early events in RTR skin carcinogenesis .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "actinic keratosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Input:
Sentence: Most COL3A1 mutations are detected by using total RNA from patient-derived fibroblasts , which requires an invasive skin biopsy .

## Item biored:test:666
Example input:
Sentence: Compound 1 is a potent A ( 2A ) /A ( 1 ) receptor antagonist in vitro ( A ( 2A ) K ( i ) = 4.1 nM ; A ( 1 ) K ( i ) = 17.0 nM ) that has excellent activity , after oral administration , across a number of animal models of Parkinson 's disease including mouse and rat models of haloperidol-induced catalepsy , mouse model of reserpine-induced akinesia , rat 6-hydroxydopamine ( 6-OHDA ) lesion model of drug-induced rotation , and MPTP-treated non-human primate model .

Example answer:
{"entities": [{"text": "A ( 2A ) /A ( 1 ) receptor antagonist", "type": "ChemicalEntity"}, {"text": "Parkinson 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "reserpine-induced", "type": "ChemicalEntity"}, {"text": "akinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "6-hydroxydopamine", "type": "ChemicalEntity"}, {"text": "6-OHDA", "type": "ChemicalEntity"}, {"text": "MPTP-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although 3,4-methylenedioxymethamphetamine ( MDMA or ecstasy ) has been shown to damage brain serotonin ( 5-HT ) neurons in animals and possibly humans , little is known about the long-term consequences of MDMA-induced 5-HT neurotoxic lesions on functions in which 5-HT is involved , such as cognitive function .

Example answer:
{"entities": [{"text": "3,4-methylenedioxymethamphetamine", "type": "ChemicalEntity"}, {"text": "MDMA", "type": "ChemicalEntity"}, {"text": "ecstasy", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "MDMA-induced", "type": "ChemicalEntity"}, {"text": "neurotoxic lesions", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: Glucose metabolism in patients with schizophrenia treated with atypical antipsychotic agents : a frequently sampled intravenous glucose tolerance test and minimal model analysis .

Example answer:
{"entities": [{"text": "Glucose", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antipsychotic agents", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Several studies have suggested that the regulator of G-protein signaling 4 ( RGS4 ) may be a positional and functional candidate gene for schizophrenia .

Example answer:
{"entities": [{"text": "regulator of G-protein signaling 4", "type": "GeneOrGeneProduct"}, {"text": "RGS4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because 5-HT transporters play a key element in the regulation of synaptic 5-HT transmission it may be important to control for the potential covariance effect of a polymorphism in the 5-HT transporter promoter gene region ( 5-HTTLPR ) when studying the effects of MDMA as well as cognitive functioning .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HT transporter promoter gene region", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "5-HT6 receptor", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "serotonergic", "type": "ChemicalEntity"}, {"text": "memory deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Antagonists at serotonin type 6 ( 5-HT ( 6 ) ) receptors show activity in models of learning and memory .

Example answer:
{"entities": [{"text": "serotonin type 6 ( 5-HT ( 6 ) ) receptors", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: These animal models were considered to reflect the positive symptoms of schizophrenia , and the above evidence suggests that altered 5-HT6 receptors are involved in the pathophysiology of psychotic disorders .

## Item biored:test:671
Example input:
Sentence: Association study of polymorphisms in the promoter region of DRD4 with schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study investigated the possible association between three functional polymorphisms in the promoter region of the dopamine D4 receptor ( DRD4 ) gene and schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "dopamine D4 receptor", "type": "GeneOrGeneProduct"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , these three SNP markers were genotyped in 218 schizophrenia pedigrees of Taiwan ( 864 individuals ) for association analysis .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neither rs2230912 nor any of 8 other SNPs genotyped across P2RX7 was found to be associated with mood disorder in general , nor specifically with bipolar or unipolar disorder .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "P2RX7", "type": "GeneOrGeneProduct"}, {"text": "mood disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bipolar or unipolar disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Results of this analysis indicated that there is a strong finding of -120 bp duplication allele frequencies with schizophrenia ( p=0.008 ) and weak finding with -1240 L/S and for paranoid schizophrenia ( p=0.022 ) .

Example answer:
{"entities": [{"text": "-120 bp duplication", "type": "SequenceVariant"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-1240 L/S", "type": "SequenceVariant"}, {"text": "paranoid schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among these three SNPs , neither SNP4 , SNP7 , SNP18 has shown significant association with schizophrenia in single locus association analysis , nor any compositions of the three SNP haplotypes has shown significantly associations with the DSM-IV diagnosed schizophrenia .

Example answer:
{"entities": [{"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although none of the observed linkages remained significant after multiple test correction through simulation , further analysis of NDE1 revealed an association between a tag-haplotype and schizophrenia ( P = 0.00046 ) specific to females , which proved to be significant ( P = 0.011 ) after multiple test correction .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These observations strongly suggest that the -120-bp duplication polymorphism of DRD4 is associated with schizophrenia and that the -521 C/T polymorphism is associated with heroin addiction .

Example answer:
{"entities": [{"text": "-120-bp duplication", "type": "SequenceVariant"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-521 C/T", "type": "SequenceVariant"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS : rs6693503 was associated with METH-induced psychosis patients in the allele/genotype-wise analysis .

## Item biored:test:722
Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: RT-PCR analysis , performed on a patient homozygous for the intronic deletion ( c.609+28_610-16del ) , failed to detect any GNPTG RNA transcripts .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: For this purpose we developed a high-throughput methodology to genotype both normal and deleted alleles using a chip-based matrix-assisted laser desorption-time-of-flight ( MALDI-TOF ) mass spectrometer and Multiplex PCR .

Example answer:
{"entities": []}

Example input:
Sentence: Large deletions involving RB1 were observed , and a disease co-segregating haplotype was used for indirect genetic testing .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In Southern blot analysis , from the signal densities of the hybridized bands and their similarities to those of exons 2 and 3 in our previous quantitative study , we found that exon 1beta was homozygously deleted in four cases , hemizygously deleted in five cases and not deleted in one case .

Example answer:
{"entities": []}

Example input:
Sentence: A deletion of 84,682 base pairs covering the CFHR1 and CFHR3 genes was detected by direct polymerase chain reaction and gel electrophoresis .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The Typically Deleted Region in the 22q11.21 subband ( here called TDR22 ) is very gene-dense , and the extent of the deletion has been defined precisely in several studies .

Example answer:
{"entities": []}

Example input:
Sentence: A detailed analysis of the DNA breakpoints in the two genes , previously characterized by other groups , validated the observation that Alu-mediated unequal recombination is the main type of deletion in MSH2 ( n=34 ) , but not in MLH1 ( n=21 ) ( P < 0.0001 ) .

Example answer:
{"entities": [{"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used high-resolution karyotyping to confirm a deletion ( 10-12Mb ) [ del ( 1 ) ( p31.2p32.3 ) ] and found no structural abnormalities in the father , suggesting a de novo event .

Example answer:
{"entities": [{"text": "deletion ( 10-12Mb )", "type": "SequenceVariant"}, {"text": "del ( 1 ) ( p31.2p32.3 )", "type": "SequenceVariant"}]}

Input:
Sentence: The deletions were defined using long distance inverse PCR and microarray-based comparative genomic hybridization .

## Item biored:test:679
Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: An association between the 5-HTTLPR polymorphism and risk of PD ( S/S genotype OR [ 95 % CI ] : 1.7 [ 1.2-2.5 ] , p = 0.002 ) was found .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The following gene polymorphisms were determined in genomic DNA : angiotensin-converting enzyme insertion/deletion polymorphism ( I/D ACE ) , angiotensinogen gene polymorphism ( M 235 ) , angiotensin II receptor type 1 ( ATR1 ) polymorphism ( A 11666C ) , and polymorphism of serotonin transporter gene ( 5HTTLPR ) .Heart rate variability during HUT was assessed in 5-minute intervals by low frequency , high frequency , standard deviation of the normal-to-normal ( SDNN ) , and root mean square successive difference parameters .

Example answer:
{"entities": [{"text": "angiotensin-converting enzyme", "type": "GeneOrGeneProduct"}, {"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "M 235", "type": "SequenceVariant"}, {"text": "angiotensin II receptor type 1", "type": "GeneOrGeneProduct"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "A 11666C", "type": "SequenceVariant"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "5HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The M235T polymorphism of the angiotensinogen gene in South Indian patients of hypertrophic cardiomyopathy .

Example answer:
{"entities": [{"text": "M235T", "type": "SequenceVariant"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conducted an association study assessing how PD risk in Italy was influenced by the serotonin transporter gene ( SLC6A4 ) polymorphic region 5-HTTLPR , consisting of an insertion/deletion ( long allele-L/short allele-S ) of 43 bp in the SLC6A4 promoter region .

Example answer:
{"entities": [{"text": "PD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "insertion/deletion ( long allele-L/short allele-S ) of 43 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : AA genotype of A 1166C polymorphism was associated with lower minimal systolic blood pressure ( SBP ) and diastolic blood pressure ( DBP ) during HUT compared with other genotypes ( minimal SBP : AA 59.6+/-21,8 , AC 79.9+/-22.7 , CC 65.4+/-22.7 mmHg , P=0.007 ) , ( minimal DBP : AA 36.4+/-22.7 , AC 52.3+/-22.9 , CC 45.4+/-19.5 mmHg , P=0.007 ) .AA genotype was also associated with higher SDNN compared to other genotypes in the early phase of HUT ( SDNN in 5 minutes of tilt : AA 59.7+/-24.6 , AC 50.6+/-20.6 , CC 46.0+/-13.2 , P=0.01 ) and at syncope occurrence ( SDNN : AA 71.0+/-20.9 , AC 58.2+/-17.9 , CC 58+/-10 , P=0.04 ) CONCLUSION : AA genotype of A 1166C polymorphism in the ATR1 gene may be associated with hypotension and decline in sympathetic tone during HUT .

Example answer:
{"entities": [{"text": "A 1166C", "type": "SequenceVariant"}, {"text": "syncope", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATR1", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DNA polymorphisms at CYP11B2/B1 locus may confer susceptibility to postoperative hypertension of patients with APA .

Example answer:
{"entities": [{"text": "CYP11B2/B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Specifically , the rs4539 ( AA ) polymorphism was associated with persistent postoperative hypertension ( P = .002 ) .

Example answer:
{"entities": [{"text": "rs4539", "type": "SequenceVariant"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Aim of the present study was to analyze the role of this polymorphism in peripheral arterial disease ( PAD ) .

## Item biored:test:703
Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition to these new mutations , this investigation reveals the prevalence of G183S substitution among a subset of African-Brazilian patients and presents evidences of the recurrence of already known mutations .

Example answer:
{"entities": [{"text": "G183S", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results strongly suggest that the E333D TRbeta mutation is responsible for the RTH phenotype in the proposita 's family .

Example answer:
{"entities": [{"text": "E333D", "type": "SequenceVariant"}, {"text": "TRbeta", "type": "GeneOrGeneProduct"}, {"text": "RTH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Homozygous mutations in PLCE1 ( also known as KIAA1516 , PLCE , or NPHS3 ) were identified following genome-wide mapping of single-nucleotide polymorphisms .

Example answer:
{"entities": [{"text": "PLCE1", "type": "GeneOrGeneProduct"}, {"text": "KIAA1516", "type": "GeneOrGeneProduct"}, {"text": "PLCE", "type": "GeneOrGeneProduct"}, {"text": "NPHS3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Input:
Sentence: The eight known COL3A1 mutations in validation samples were all successfully detected by the hrMCA .

## Item biored:test:713
Example input:
Sentence: We also designed a rapid polymerase chain reaction-restriction fragment length polymorphism ( PCR-RFLP ) method to analyze the same mutation , amplifying exon 4 and digesting with PstI restriction enzyme .

Example answer:
{"entities": [{"text": "PstI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Exons and flanking intron sequences of the TGFBI gene were amplified by PCR with specific primers .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutation screening of all exons of the PAX6 gene was performed by direct sequencing of PCR-amplified DNA fragments .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: DNA analysis revealed compound heterozygosity for mutations of GHR , including a previously reported R211H mutation and a novel duplication of a nucleotide in exon 9 ( 899dupC ) , the latter resulting in a frameshift and a premature stop codon .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "R211H", "type": "SequenceVariant"}, {"text": "899dupC", "type": "SequenceVariant"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA was isolated from peripheral leukocytes and the region of interest in the AGT gene bearing a missense mutation methionine to threonine substitution at codon 235 ( M235T ) of exon 2 , was amplified by polymerase chain reaction ( PCR ) .

Example answer:
{"entities": [{"text": "AGT", "type": "GeneOrGeneProduct"}, {"text": "methionine to threonine substitution at codon 235", "type": "SequenceVariant"}, {"text": "M235T", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Mutation analysis of all coding exons of the GUCA1B gene was performed by polymerase chain reaction amplification of genomic DNA and subsequent DNA sequencing .

## Item biored:test:676
Example input:
Sentence: These results indicated that IGF-1R may increase cell viability under hypoxic conditions by promoting autophagy and scavenging ROS production , which is closed with PI3K/Akt/mTOR signaling pathway .

Example answer:
{"entities": [{"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "hypoxic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "PI3K/Akt/mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TIEG1 deficiency confers enhanced myocardial protection in the infarcted heart by mediating the Pten/Akt signalling pathway .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "infarcted heart", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Pten/Akt", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Example input:
Sentence: BACKGROUND : The plasminogen activator inhibitor type-1 ( PAI-1 ) has been implicated in the regulation of fibrinolysis and extracellular matrix components .

Example answer:
{"entities": [{"text": "plasminogen activator inhibitor type-1", "type": "GeneOrGeneProduct"}, {"text": "PAI-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Oxidative stress plays an essential role in inflammation and fibrosis .

Example answer:
{"entities": [{"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taking into account that the sarcolemmal integrity is stabilized by the dystrophin-glycoprotein complex ( DGC ) that connects actin and laminin in contractile machinery and extracellular matrix and by integrins , this study tests the hypothesis that isoproterenol affects sarcolemmal stability through changes in the DGC and integrins .

Example answer:
{"entities": [{"text": "dystrophin-glycoprotein", "type": "GeneOrGeneProduct"}, {"text": "actin", "type": "GeneOrGeneProduct"}, {"text": "laminin", "type": "GeneOrGeneProduct"}, {"text": "isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rapid reversal of anticoagulation reduces hemorrhage volume in a mouse model of warfarin-associated intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "warfarin-associated", "type": "ChemicalEntity"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a mouse model , we tested whether the rapid reversal of anticoagulation using human prothrombin complex concentrate ( PCC ) can reduce hemorrhagic blood volume .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "prothrombin complex concentrate", "type": "ChemicalEntity"}, {"text": "PCC", "type": "ChemicalEntity"}]}

Input:
Sentence: Conversion of fibrinogen to fibrin plays an essential role in hemostasis and results in stabilization of the fibrin clot .

## Item biored:test:707
Example input:
Sentence: In our study the combination of high TS expression genotypes G_6+/6+ identifies a group of high risk within CRC patients treated with 5FU .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: Further analysis of G472A genotypes in Hispanic subjects with data stratified by gender identified a point-wise significant ( P = 0.049 ) association of G/A and A/A genotypes with opiate addiction in women , but not men .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: An increased representation of the PNP AA genotype was observed in AD patients with fast cognitive deterioration in comparison with that from patients with slow deterioration rate .

Example answer:
{"entities": [{"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive deterioration", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Elimination of KCa3.1 in KCa3.1-/-/APP/PS1 mice corrected these abnormal responses .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "KCa3.1-/-/APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The estimated relative risk was significantly high for individuals with w1/m1 genotype at 3'UTR of CYP1A1 gene ( OR-4.64 ; 95 % CI = 1.51-14.86 ; P < 0.01 ) whereas the CYP1A1 Ile/Val genotype ( w2/m2 ) on exon 7 was found to be associated with a decreased risk for prostate cancer ( OR-0.17 ; 95 % CI = 0.02-0.89 ; P=0.03 ) .

Example answer:
{"entities": [{"text": "CYP1A1", "type": "GeneOrGeneProduct"}, {"text": "Ile/Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A Stratified analysis of the genotypes with age of onset and tumor grade showed the w1/m1 genotype to be significantly associated with an early age of onset ; however the tumor grades did not have significant association with the variant genotypes .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Taken together with previous studies of human PPARG mutations , these findings suggest that PPAR-gamma deficiency due either to haploinsufficiency or to substantial activity loss due to dominant negative interference of the normal allele product 's function can each contribute to the FPLD3 phenotype .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "PPAR-gamma", "type": "GeneOrGeneProduct"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a genotype test , we found a trend to point-wise association ( P = 0.053 ) of the G472A SNP in Hispanic subjects with opiate addiction .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "opiate addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: 3R G > C SNP genotyping did not add prognostic information .

Example answer:
{"entities": [{"text": "G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A better understanding of the genotype-phenotype correlation in COL3A1 using this method will lead to improve in diagnosis and treatment .

## Item biored:test:658
Example input:
Sentence: Pituitary adenoma predisposition ( PAP ) has been recently associated with germline mutations in the aryl hydrocarbon receptor interacting protein ( AIP ) gene .

Example answer:
{"entities": [{"text": "Pituitary adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aryl hydrocarbon receptor interacting protein", "type": "GeneOrGeneProduct"}, {"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in PDE6H and in KCNV2 have been described in CDSRR .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations found in the PTCH1 gene and neighboring repetitive sequences may have contributed to the development of the studied BCCs .

Example answer:
{"entities": [{"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "BCCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One sporadic BCC presented the mutation g.2885G > C in exon 17 of PTCH1 , which predicts the substitution p.R962T in an external domain of the protein .

Example answer:
{"entities": [{"text": "BCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "g.2885G > C", "type": "SequenceVariant"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "p.R962T", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Input:
Sentence: Mutations in the BCP region ( A1762T , G1764A ) and in the precore region ( G1896A , G1899A ) were also found .

## Item biored:test:692
Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Clinically , death was due to cardiogenic shock .

Example answer:
{"entities": [{"text": "death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiogenic shock", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : A 72-year-old white man with underlying human immunodeficiency virus , atrial fibrillation , coronary artery disease , and hyperlipidemia presented with generalized pain , fatigue , and dark orange urine for 3 days .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperlipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fatigue", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The clinical findings from this patient include recurrent fractures , mild bone deformities , delayed tooth eruption , normal hearing , and white sclera .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "fractures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bone deformities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tooth eruption", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thereafter , no cardiac symptoms were observed .

Example answer:
{"entities": [{"text": "cardiac symptoms", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Echocardiography was performed at 3 and 28 days post-MI , whereas the haemodynamics test was performed 28 days post-MI .

Example answer:
{"entities": []}

Example input:
Sentence: We herein report the case of a 70-year-old man with 5-FU-induced cardiotoxicity , in whom a high serum level of alpha-fluoro-beta-alanine ( FBAL ) was observed .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "5-FU-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fluoro-beta-alanine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: However , echocardiography indicated no sign of cardiomyopathy and he showed no distinct intellectual impairment that interfered with daily life .

## Item biored:test:716
Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The A49T variant was also detected in heterozygosis in the second case without other sequencing abnormalities .

Example answer:
{"entities": [{"text": "A49T", "type": "SequenceVariant"}]}

Example input:
Sentence: The I280S mutation was recently reported in a heterozygous patient .

Example answer:
{"entities": [{"text": "I280S", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Since the first molecular characterization of an FH mutation by Bourgeron et al in 1994 , a series of reports of both FH deficiency patients and patients with MCUL/HLRRC have described 107 variants , of which 93 are thought to be pathogenic .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "FH deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MCUL/HLRRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The MLH1 -93 variant allele was also over-represented in t-AML cases when compared to de novo AML cases ( 36.9 % , n = 420 ) and healthy controls ( 36.3 % , n = 952 ) , and was associated with a significantly increased risk of developing t-AML ( odds ratio 5.31 , 95 % confidence interval 1.40 to 20.15 ) , but only in patients previously treated with a methylating agent .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "AML", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: With the exception of g.3318-34C > T and g.3352delG , all variants occurred heterozygously .

Example answer:
{"entities": [{"text": "g.3318-34C > T", "type": "SequenceVariant"}, {"text": "g.3352delG", "type": "SequenceVariant"}]}

Example input:
Sentence: This sequence variant has previously been reported as a compound heterozygote in one sporadic LCA patient .

Example answer:
{"entities": [{"text": "LCA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Input:
Sentence: All sequence variants were previously reported in healthy subjects .

## Item biored:test:631
Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the present study , we investigated whether 50 mg/kg per day , p.o. , Ato could prevent endothelial NO synthase ( eNOS ) downregulation and the increase in O2- in Sprague-Dawley ( SD ) rats , thereby reducing blood pressure .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "endothelial NO synthase", "type": "GeneOrGeneProduct"}, {"text": "eNOS", "type": "GeneOrGeneProduct"}, {"text": "O2-", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have recently shown that estrogen negatively modulates the hypotensive effect of clonidine ( mixed alpha2-/I1-receptor agonist ) in female rats and implicates the cardiovascular autonomic control in this interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "hypotensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}, {"text": "alpha2-/I1-receptor", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: This , together with our previous findings that allopurinol failed to prevent adrenocorticotrophic hormone induced hypertension , suggests that XO activity is not a major determinant of GC-HT in the rat .

Example answer:
{"entities": [{"text": "allopurinol", "type": "ChemicalEntity"}, {"text": "adrenocorticotrophic hormone", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XO", "type": "ChemicalEntity"}, {"text": "GC-HT", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: The extent of hypotension and changes in brain tissue oxygenation ( PbtO ( 2 ) ) and in cerebral blood flow were studied in a separate group of animals .

Example answer:
{"entities": [{"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: Down-regulation of norepinephrine transporter function induced by chronic administration of desipramine linking to the alteration of sensitivity of local-anesthetics-induced convulsions and the counteraction by co-administration with local anesthetics .

Example answer:
{"entities": [{"text": "norepinephrine transporter", "type": "GeneOrGeneProduct"}, {"text": "desipramine", "type": "ChemicalEntity"}, {"text": "convulsions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anesthetics", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

## Item biored:test:675
Example input:
Sentence: Several studies have reported that , compared with wild-type individuals , CYP2C19 variant allele carriers exhibit a significantly lower capacity to metabolize clopidogrel into its active metabolite and inhibit platelet activation , and are therefore at significantly higher risk of adverse cardiovascular events .

Example answer:
{"entities": [{"text": "CYP2C19", "type": "GeneOrGeneProduct"}, {"text": "clopidogrel", "type": "ChemicalEntity"}]}

Example input:
Sentence: Specifically , the rs4539 ( AA ) polymorphism was associated with persistent postoperative hypertension ( P = .002 ) .

Example answer:
{"entities": [{"text": "rs4539", "type": "SequenceVariant"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: No independent role of the -1123 G > C and+2740 A > G variants in the association of PTPN22 with type 1 diabetes and juvenile idiopathic arthritis in two Caucasian populations .

Example answer:
{"entities": [{"text": "-1123 G > C", "type": "SequenceVariant"}, {"text": "A > G", "type": "SequenceVariant"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "juvenile idiopathic arthritis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : In two different Caucasian populations , the Czechs and the Azeri , no independent contribution can be detected either of the -1123 promoter SNP or the +2740 3'-UTR SNP , and only the minor allele at PTPN22 codon 620 contributes to the risk of autoimmunity .

Example answer:
{"entities": [{"text": "PTPN22", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The M235T polymorphism of the angiotensinogen gene in South Indian patients of hypertrophic cardiomyopathy .

Example answer:
{"entities": [{"text": "M235T", "type": "SequenceVariant"}, {"text": "angiotensinogen", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: The fibrinogen gamma 10034C > T polymorphism is not associated with Peripheral Arterial Disease .

## Item biored:test:613
Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The differentiation induction by GADD45A was transmitted by activating p38 Mitogen-activated protein kinase ( MAPK ) signaling and allowed the generation of megakaryocytic-erythroid , myeloid , and lymphoid lineages .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}, {"text": "p38 Mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Investigations of the underlying mechanisms revealed that BDNF activated Akt and preserved phosphorylation of mammalian target of rapamycin and Bad without affecting p38 mitogen-activated protein kinase and extracellular regulated protein kinase pathways .

Example answer:
{"entities": [{"text": "mammalian target of", "type": "GeneOrGeneProduct"}, {"text": "p38 mitogen-activated protein", "type": "GeneOrGeneProduct"}, {"text": "extracellular regulated protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , PI3K/Akt pathway signaling was also increased in Eu-myc B cells , and this increase was partially suppressed with ibrutinib .

Example answer:
{"entities": [{"text": "PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "ibrutinib", "type": "ChemicalEntity"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , IGF-1R is related with PI3K/Akt/mTOR signaling pathway and enhanced autophagy-associated protein expression , which was verified following treatment with the PI3K inhibitor LY294002 .

Example answer:
{"entities": [{"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "PI3K/Akt/mTOR", "type": "GeneOrGeneProduct"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}, {"text": "LY294002", "type": "ChemicalEntity"}]}

Example input:
Sentence: A potential downstream signaling pathway involving phosphatidylinositol 3-kinase ( PI3K ) /threonine protein kinase B ( Akt ) /mammalian target of rapamycin ( mTOR ) was identifiedby western blot analysis .

Example answer:
{"entities": [{"text": "phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "target of rapamycin", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: A link between VDR and the RAS-mitogen-activated protein kinase ( MAPK ) or phosphatidylinositol 3-kinase ( PI3K ) -AKT pathway has been suggested .

## Item biored:test:668
Example input:
Sentence: The aim of the study was to investigate the effects of moderate and heavy MDMA use on cognitive function , as well as the effects of long-term abstention from MDMA , in subjects genotyped for 5-HTTLPR .

Example answer:
{"entities": [{"text": "MDMA", "type": "ChemicalEntity"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These observations strongly suggest that the -120-bp duplication polymorphism of DRD4 is associated with schizophrenia and that the -521 C/T polymorphism is associated with heroin addiction .

Example answer:
{"entities": [{"text": "-120-bp duplication", "type": "SequenceVariant"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-521 C/T", "type": "SequenceVariant"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "5-HT6 receptor", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "serotonergic", "type": "ChemicalEntity"}, {"text": "memory deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: This study investigated the possible association between three functional polymorphisms in the promoter region of the dopamine D4 receptor ( DRD4 ) gene and schizophrenia , depression , and heroin addiction .

Example answer:
{"entities": [{"text": "dopamine D4 receptor", "type": "GeneOrGeneProduct"}, {"text": "DRD4", "type": "GeneOrGeneProduct"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because 5-HT transporters play a key element in the regulation of synaptic 5-HT transmission it may be important to control for the potential covariance effect of a polymorphism in the 5-HT transporter promoter gene region ( 5-HTTLPR ) when studying the effects of MDMA as well as cognitive functioning .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HT transporter promoter gene region", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Therefore , we conducted an analysis of the association of the 5-HT6 gene ( HTR6 ) with METH-induced psychosis .

## Item biored:test:718
Example input:
Sentence: Using a genome-wide screen of DNA copy number alterations in 36 primary OSCs , we identified two tumors with apparent homozygous deletions of the NF1 gene .

Example answer:
{"entities": [{"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conducted a screening of the MHC region for 1,536 single nucleotide polymorphisms ( SNPs ) and the deletion of the C4A gene in a SLE case-control study ( 380 cases , 765 age-matched controls ) nested within the prospective Black Women 's Health Study .

Example answer:
{"entities": [{"text": "MHC", "type": "GeneOrGeneProduct"}, {"text": "C4A", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Deletion 22q11.2 syndrome is the most frequent known microdeletion syndrome and is associated with a highly variable phenotype , including DiGeorge and Shprintzen ( velocardiofacial ) syndromes .

Example answer:
{"entities": [{"text": "Deletion 22q11.2 syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DiGeorge and Shprintzen ( velocardiofacial ) syndromes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Through MLPA analysis , a large deletion including the whole PAX6 gene and DKFZ p686k1684 gene was detected in one sporadic patient from the AN group .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}, {"text": "DKFZ p686k1684", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "AN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A case of Bernard-Soulier Syndrome due to a homozygous four bases deletion ( TGAG ) of GPIbalpha gene : lack of GPIbalpha but absence of bleeding .

Example answer:
{"entities": [{"text": "Bernard-Soulier Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "GPIbalpha", "type": "GeneOrGeneProduct"}, {"text": "bleeding", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in the PCSK9 gene in Norwegian subjects with autosomal dominant hypercholesterolemia .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "autosomal dominant hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Large contiguous gene deletions in Sjogren-Larsson syndrome .

## Item biored:test:645
Example input:
Sentence: Replication-competent HBV strains with sG145R or sP120T and LAM resistance ( rtM204I or rtL180M/rtM204V ) were generated on an HBeAg-positive and an HBeAg-negative background with precore ( PC ) and basal core promoter ( BCP ) mutants .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg-positive", "type": "ChemicalEntity"}, {"text": "HBeAg-negative", "type": "ChemicalEntity"}, {"text": "precore", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "ChemicalEntity"}, {"text": "LAM", "type": "ChemicalEntity"}, {"text": "HBeAg", "type": "ChemicalEntity"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "G145R", "type": "SequenceVariant"}, {"text": "P120T", "type": "SequenceVariant"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus e", "type": "ChemicalEntity"}]}

Example input:
Sentence: To the best of our knowledge , this constitutes the first report of HBV lamivudine-resistant strains in therapy-na ve HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thirty-five lamivudine-na ve HBV infected patients with or without HIV co-infection were studied : 15 chronic HBV mono-infected patients and 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "HBV infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV mono-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It remains to be seen whether such pre-existing antiviral mutations could result in widespread emergence of HBV resistant strains when lamivudine-containing highly active antiretroviral ( ARV ) treatment ( HAART ) regimens become widely applied in South Africa , as this is likely to have potential implications in the management of HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-containing", "type": "ChemicalEntity"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: This was an exploratory study to investigate lamivudine-resistant hepatitis B virus ( HBV ) strains in selected lamivudine-na ve HBV carriers with and without human immunodeficiency virus ( HIV ) co-infection in South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B virus", "type": "OrganismTaxon"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-na", "type": "ChemicalEntity"}, {"text": "human immunodeficiency virus ( HIV ) co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}, {"text": "lamivudine-resistant", "type": "ChemicalEntity"}, {"text": "hepatitis B", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HBV-HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "ChemicalEntity"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HIV co-infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HBV and HIV co-infected", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: High frequency of lamivudine resistance mutations in Brazilian patients co-infected with HIV and hepatitis B .

## Item biored:test:674
Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , it appears that striatal-resident microglia respond to METH with an activation cascade and then return to a surveying state without undergoing apoptosis or migration .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}]}

Example input:
Sentence: Antagonists at serotonin type 6 ( 5-HT ( 6 ) ) receptors show activity in models of learning and memory .

Example answer:
{"entities": [{"text": "serotonin type 6 ( 5-HT ( 6 ) ) receptors", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study sought to characterize the cognitive-enhancing effects of the 5-HT ( 6 ) antagonist Ro4368554 ( 3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole ) in a rat object recognition task employing a cholinergic ( scopolamine pretreatment ) and a serotonergic- ( tryptophan ( TRP ) depletion ) deficient model , and compared its pattern of action with that of the acetylcholinesterase inhibitor metrifonate .

Example answer:
{"entities": [{"text": "5-HT ( 6 )", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "3-benzenesulfonyl-7- ( 4-methyl-piperazin-1-yl ) 1H-indole", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "scopolamine", "type": "ChemicalEntity"}, {"text": "serotonergic-", "type": "ChemicalEntity"}, {"text": "tryptophan", "type": "ChemicalEntity"}, {"text": "TRP", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "metrifonate", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-HT ( 6 ) receptor", "type": "ChemicalEntity"}]}

Example input:
Sentence: With few genetic studies investigating biosynthetic and metabolic enzymes governing the rate of 5-HT activity and their relationship to migraine , it was the objective of this study to assess genetic variants within the human tryptophan hydroxylase ( TPH ) , amino acid decarboxylase ( AADC ) and monoamine oxidase A ( MAOA ) genes in migraine susceptibility .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tryptophan hydroxylase", "type": "GeneOrGeneProduct"}, {"text": "TPH", "type": "GeneOrGeneProduct"}, {"text": "amino acid decarboxylase", "type": "GeneOrGeneProduct"}, {"text": "AADC", "type": "GeneOrGeneProduct"}, {"text": "monoamine oxidase A", "type": "GeneOrGeneProduct"}, {"text": "MAOA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because 5-HT transporters play a key element in the regulation of synaptic 5-HT transmission it may be important to control for the potential covariance effect of a polymorphism in the 5-HT transporter promoter gene region ( 5-HTTLPR ) when studying the effects of MDMA as well as cognitive functioning .

Example answer:
{"entities": [{"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HT transporter promoter gene region", "type": "GeneOrGeneProduct"}, {"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "MDMA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: The selective 5-HT6 receptor antagonist Ro4368554 restores memory performance in cholinergic and serotonergic models of memory deficiency in the rat .

Example answer:
{"entities": [{"text": "5-HT6 receptor", "type": "GeneOrGeneProduct"}, {"text": "Ro4368554", "type": "ChemicalEntity"}, {"text": "cholinergic", "type": "ChemicalEntity"}, {"text": "serotonergic", "type": "ChemicalEntity"}, {"text": "memory deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}]}

Input:
Sentence: CONCLUSION : HTR6 may play an important role in the pathophysiology of METH-induced psychosis in the Japanese population .
