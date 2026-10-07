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

## Item biored:test:507
Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: Common germline genetic variation in antioxidant defense genes and survival after diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : ADAM12 expression was downregulated in representative claudin-low breast cancer cell lines , SUM159PT and Hs578T , using siRNA transfection or inducible shRNA expression .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SUM159PT", "type": "CellLine"}, {"text": "Hs578T", "type": "CellLine"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Elevated expression of the C6orf49 transcript was associated with breast cancer survival , adding biological interest to the finding .

## Item biored:test:467
Example input:
Sentence: In both types , purinoceptor desensitization with alpha , beta-methylene adenosine-5'-triphosphate ( alpha , beta-meATP ) caused further reductions at low frequencies ( < 10 Hz ) .

Example answer:
{"entities": [{"text": "alpha , beta-methylene adenosine-5'-triphosphate", "type": "ChemicalEntity"}, {"text": "alpha , beta-meATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Plasma and liver 15-F ( 2t ) -IsoP were elevated and reached a plateau after day 2 of VPA treatment compared to control .

Example answer:
{"entities": [{"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study aimed to evaluate the GFC effects at doses of 25 , 50 or 75 mg/kg on seizure parameters to determine their anticonvulsant activity and its effects on amino acid ( r-aminobutyric acid ( GABA ) , glutamine , aspartate and glutathione ) levels as well as on acetylcholinesterase ( AChE ) activity in mice hippocampus after seizures .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "r-aminobutyric acid", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Overall , these findings indicate that VPA treatment results in oxidative stress , as measured by levels of 15-F ( 2t ) -IsoP , which precedes the onset of necrosis , steatosis , and elevated levels of serum alpha-GST .

Example answer:
{"entities": [{"text": "VPA", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-GST", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Input:
Sentence: Pretreatment with either VPU ( 50 and 100 mg/kg ) or VPA ( 300 and 600 mg/kg ) completely abolished pilocarpine-evoked increases in extracellular glutamate and aspartate .

## Item biored:test:496
Example input:
Sentence: Addition of Tat ( 40 ng/slice ) to the medium of OHSCs induced IDO steady-state mRNA that peaked at 6 h. This effect was potentiated by pretreatment with IFNg .

Example answer:
{"entities": [{"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "IFNg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There was statistically significant improvement in all contralateral major parkinsonian motor signs in all patients followed for 6 months .

Example answer:
{"entities": [{"text": "parkinsonian", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among the subjects treated with methadone , 28 % men and 32 % women had prolonged QTc interval .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "prolonged QTc interval", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , a 38 % remission rate has been recently reported in refractory MCL treated with temsirolimus , a mTOR inhibitor.Here we had the opportunity to study a case of refractory MCL who had tumor regression two months after temsirolimus treatment , and a progression-free survival of 10 months .

Example answer:
{"entities": [{"text": "MCL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "temsirolimus", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : In a PA retention paradigm , the injection of NTG immediately after learning produced a significant impairment of long-term associative memory in mice , whereas delayed induced hypotension had no effect .

Example answer:
{"entities": [{"text": "NTG", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolongation of the QT interval in the ECG of patients with torsade de pointes ( TdP ) has been reported in methadone users .

Example answer:
{"entities": [{"text": "Prolongation of the QT interval", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "torsade de pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "methadone", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : Among 167 methadone maintenance patients , the prevalence of QTc prolongation to 0.50 second ( ( 1/2 ) ) or longer was 16.2 % compared with 0 % in 80 control subjects .

Example answer:
{"entities": [{"text": "methadone", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "QTc prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Three months of raloxifene treatment was associated with a significant decrease in the plasma TAFI antigen concentrations ( 16 % change , P < 0.01 ) , and a significant increase in tPA antigen concentrations ( 25 % change , P < 0.05 ) .

Example answer:
{"entities": [{"text": "raloxifene", "type": "ChemicalEntity"}, {"text": "TAFI", "type": "GeneOrGeneProduct"}, {"text": "tPA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Symptoms persisted for three months despite TAC dose reduction , administration of IVIG and four doses of methylprednisolone pulse therapy .

## Item biored:test:466
Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: These findings suggest that glutamate-mediated mechanisms in the neural circuits at the IC level influence haloperidol-induced catalepsy and participate in the regulation of motor activity .

Example answer:
{"entities": [{"text": "glutamate-mediated", "type": "ChemicalEntity"}, {"text": "haloperidol-induced", "type": "ChemicalEntity"}, {"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study was designed to evaluate the effects of pilocarpine and explore the underlying ionic mechanism , using both aconitine-induced rat and ouabain-induced guinea pig arrhythmia models .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "aconitine-induced", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "ouabain-induced", "type": "ChemicalEntity"}, {"text": "guinea pig", "type": "OrganismTaxon"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Behavioral and neurochemical studies in mice pretreated with garcinielliptone FC in pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "garcinielliptone FC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chemokine CCL2 and its receptor CCR2 are increased in the hippocampus following pilocarpine-induced status epilepticus .

Example answer:
{"entities": [{"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , our data suggest that GFC may influence in epileptogenesis and promote anticonvulsant actions in pilocarpine model by modulating the GABA and glutamate contents and of AChE activity in seized mice hippocampus .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : The data show that CCR2 and CCL2 are up-regulated in the hippocampus after pilocarpine-induced SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

## Item biored:test:435
Example input:
Sentence: Compound heterozygosity for a novel nine-nucleotide deletion and the Asn45Ser missense mutation in the glycoprotein IX gene in a patient with Bernard-Soulier syndrome .

Example answer:
{"entities": [{"text": "Asn45Ser", "type": "SequenceVariant"}, {"text": "glycoprotein IX", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "Bernard-Soulier syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In GCD , 18 patients with GCD type I had a mutation of arginine 555-to-tryptophan ( Arg555Trp ) and 1 patient with GCD type III ( Reis-Bucklers dystrophy ) , had the Arg124Leu mutation .

Example answer:
{"entities": [{"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "GCD type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 555-to-tryptophan", "type": "SequenceVariant"}, {"text": "Arg555Trp", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GCD type III", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Reis-Bucklers dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Arg124Leu", "type": "SequenceVariant"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation was responsible for the familial disorder through the substitution of a highly conserved arginine to tryptophan at codon 198 ( p.R198W ) .

Example answer:
{"entities": [{"text": "arginine to tryptophan at codon 198", "type": "SequenceVariant"}, {"text": "p.R198W", "type": "SequenceVariant"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: No CHRNA1 , CHRNB1 , or CHRND mutations were detected , but a homozygous RAPSN frameshift mutation , c.1177-1178delAA , was identified in a family with three children affected with lethal fetal akinesia sequence .

## Item biored:test:478
Example input:
Sentence: In conclusion , our findings reveal a potent protective role of BDNF against Dox-induced cardiotoxicity by activating Akt signalling , which may facilitate the safe use of Dox in cancer treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Brain-derived neurotrophic factor attenuates doxorubicin-induced cardiac dysfunction through activating Akt signalling in rats .

Example answer:
{"entities": [{"text": "Brain-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In conclusion , HFD-induced obese rats are highly sensitized to doxorubicin-induced cardiotoxicity by substantially downregulating cardiac mitochondrial ATP generation , increasing oxidative stress and downregulating the JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cardiotoxicity is a rare complication occurring during 5-fluorouracil ( 5-FU ) treatment for malignancies .

Example answer:
{"entities": [{"text": "Cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-fluorouracil", "type": "ChemicalEntity"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "malignancies", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Dexrazoxane ( ICRF-187 ) is recommended for protection against anthracycline-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "Dexrazoxane", "type": "ChemicalEntity"}, {"text": "ICRF-187", "type": "ChemicalEntity"}, {"text": "anthracycline-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Randomised clinical trials and observational studies have shown an increased risk of myocardial infarction , stroke , hypertension and heart failure during treatment with cyclooxygenase inhibitors .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heart failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cyclooxygenase inhibitors", "type": "ChemicalEntity"}]}

Example input:
Sentence: PURPOSE : The anthracyclines daunorubicin and doxorubicin and the epipodophyllotoxin etoposide are potent DNA cleavage-enhancing drugs that are widely used in clinical oncology ; however , myelosuppression and cardiac toxicity limit their use .

Example answer:
{"entities": [{"text": "anthracyclines", "type": "ChemicalEntity"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "epipodophyllotoxin", "type": "ChemicalEntity"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atrial fibrillation or other cardiac arrhythmias are unusual complications in patients treated with chemotherapy .

Example answer:
{"entities": [{"text": "Atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac arrhythmias", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Often , chemotherapy by doxorubicin ( Adriamycin ) is limited due to life threatening cardiotoxicity in patients during and posttherapy .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "Adriamycin", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The cardiac toxicity intrinsically associated with the aggressive chemotherapy employed could function as a triggering factor for the arrhythmia in the predisposed myocardium of this patient .

Example answer:
{"entities": [{"text": "cardiac toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Input:
Sentence: BACKGROUND : Exposure to anthracyclines as part of cancer therapy has been associated with the development of congestive heart failure ( CHF ) .

## Item biored:test:465
Example input:
Sentence: An experimental group of rats was treated with puromycin aminonucleoside ( PAN ; 180 mg/kg iv ) , whereas the control group received only vehicle .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "puromycin aminonucleoside", "type": "ChemicalEntity"}, {"text": "PAN", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study examined the influence of excitatory amino acid-mediated mechanisms in the IC on the catalepsy induced by the dopamine receptor blocker haloperidol administered systemically ( 1 or 0.5 mg/kg ) in rats .

Example answer:
{"entities": [{"text": "catalepsy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dopamine receptor", "type": "GeneOrGeneProduct"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: GFC produced an increased latency to first seizure , at doses 25mg/kg ( 20.12 + 2.20 min ) , 50mg/kg ( 20.95 + 2.21 min ) or 75 mg/kg ( 23.43 + 1.99 min ) when compared with seized mice .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The results indicate that GFC can exert anticonvulsant activity and reduce the frequency of installation of pilocarpine-induced status epilepticus , as demonstrated by increase in latency to first seizure and decrease in mortality rate of animals .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "pilocarpine-induced", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Male Sprague-Dawley rats were injected with saline on postnatal day ( P ) 20 , or a convulsant dose of pilocarpine on P20 or P45 .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "pilocarpine", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study aimed to evaluate the GFC effects at doses of 25 , 50 or 75 mg/kg on seizure parameters to determine their anticonvulsant activity and its effects on amino acid ( r-aminobutyric acid ( GABA ) , glutamine , aspartate and glutathione ) levels as well as on acetylcholinesterase ( AChE ) activity in mice hippocampus after seizures .

Example answer:
{"entities": [{"text": "GFC", "type": "ChemicalEntity"}, {"text": "seizure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "r-aminobutyric acid", "type": "ChemicalEntity"}, {"text": "GABA", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "AChE", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Pre-treatment with a dose of 30 mg/kg 2h before picrotoxin microperfusion prevented seizures in the 75 % of the rats .

Example answer:
{"entities": [{"text": "picrotoxin", "type": "ChemicalEntity"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Pilocarpine on either day induced status epilepticus ; status epilepticus at P45 resulted in CA3 cell loss and spontaneous seizures , whereas P20 rats had no cell loss or spontaneous seizures .

Example answer:
{"entities": [{"text": "Pilocarpine", "type": "ChemicalEntity"}, {"text": "status epilepticus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CA3", "type": "CellLine"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: To determine whether there was a temporal relationship between VPA-associated oxidative stress and hepatotoxicity , adult male Sprague-Dawley rats were treated ip with VPA ( 500 mg/kg ) or 0.9 % saline ( vehicle ) once daily for 2 , 4 , 7 , 10 , or 14 days .

Example answer:
{"entities": [{"text": "VPA-associated", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: A single dose of valproic acid ( VPA ) , which is a widely used antiepileptic drug , is associated with oxidative stress in rats , as recently demonstrated by elevated levels of 15-F ( 2t ) -isoprostane ( 15-F ( 2t ) -IsoP ) .

Example answer:
{"entities": [{"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}, {"text": "antiepileptic drug", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "15-F ( 2t ) -isoprostane", "type": "ChemicalEntity"}, {"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}]}

Input:
Sentence: VPU was more potent than VPA , exhibiting the median effective dose ( ED ( 50 ) ) of 49 mg/kg in protecting rats against pilocarpine-induced seizure whereas the corresponding value for VPA was 322 mg/kg .

## Item biored:test:316
Example input:
Sentence: Mutations leading to abrogation of matriptase-2 proteolytic activity in humans are associated with an iron-refractory iron deficiency anemia ( IRIDA ) due to elevated hepcidin levels .

Example answer:
{"entities": [{"text": "matriptase-2", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "iron-refractory iron deficiency anemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IRIDA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepcidin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hypokalaemic periodic paralysis ( HypoPP ) is an autosomal dominant disorder , which is characterized by periodic attacks of muscle weakness associated with a decrease in the serum potassium level .

Example answer:
{"entities": [{"text": "Hypokalaemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscle weakness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "potassium", "type": "ChemicalEntity"}]}

Example input:
Sentence: The FH mutation database : an online database of fumarate hydratase mutations involved in the MCUL ( HLRCC ) tumor syndrome and congenital fumarase deficiency .

Example answer:
{"entities": [{"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "fumarate hydratase", "type": "GeneOrGeneProduct"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HLRCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fumarase deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: One-hundred and fifty HCM ( 90 sporadic hypertrophic cardiomyopathy [ SHCM ] and 60 familial hypertrophic cardiomyopathy [ FHCM ] ) patients and 165 age- and sex-matched normal healthy controls without known hypertension and left ventricular hypertrophy were included in the study .

Example answer:
{"entities": [{"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sporadic hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "familial hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular hypertrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A major disease-causing gene for HypoPP has been identified as CACNA1S , which encodes the skeletal muscle calcium channel alpha-subunit with four transmembrane domains ( I-IV ) , each with six transmembrane segments ( S1-S6 ) .

Example answer:
{"entities": [{"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "skeletal muscle calcium channel alpha-subunit", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : 17alpha-Hydroxylase deficiency is a rare form of congenital adrenal hyperplasia caused by CYP17 gene mutations .

Example answer:
{"entities": [{"text": "17alpha-Hydroxylase deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "congenital adrenal hyperplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CYP17", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Nephronophthisis ( NPHP ) , a rare recessive cystic kidney disease , is the most frequent genetic cause of chronic renal failure in children and young adults .

Example answer:
{"entities": [{"text": "Nephronophthisis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystic kidney disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: INTRODUCTION : Hypertrophic cardiomyopathy ( HCM ) is a complex disorder and genetically transmitted cardiac disease with a diverse clinical course .

Example answer:
{"entities": [{"text": "Hypertrophic cardiomyopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONTEXT : Hereditary hypophosphatemic rickets with hypercalciuria ( HHRH ) is a rare metabolic disorder , characterized by hypophosphatemia and rickets/osteomalacia with increased serum 1,25-dihydroxyvitamin D [ 1,25- ( OH ) ( 2 ) D ] resulting in hypercalciuria .

## Item biored:test:485
Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The -930A > G polymorphism of the CYBA gene is associated with premature coronary artery disease .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}, {"text": "CYBA", "type": "GeneOrGeneProduct"}, {"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A meta-analysis of previous and our present study revealed that this polymorphism is positively associated with adenocarcinoma , although suggestive associations were also found for squamous- and small-cell lung cancers .

Example answer:
{"entities": [{"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "squamous- and small-cell lung cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We analyzed the nucleotidic sequence of the CYP2F1 gene in DNA samples from 90 French Caucasians consisting in 44 patients with lung cancer and 46 control individuals , using single-strand conformation polymorphism analysis of PCR products ( PCR-SSCP ) .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Two coding polymorphisms , 55M/L and 192Q/R , and a promoter variant , -107C/T , has been extensively studied with respect to susceptibility to CHD .

Example answer:
{"entities": [{"text": "55M/L", "type": "SequenceVariant"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "-107C/T", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , our preliminary results did not show any evidence that the CYP2F1 genetic polymorphism has implications in the pathogenesis of lung cancer .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}, {"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using self-reported data on ischemic heart disease to evaluate the impact of the PON 192Q/R polymorphism on susceptibility to CHD , we found only a nonsignificant trend of 192RR homozygosity in women being a risk factor .

Example answer:
{"entities": [{"text": "ischemic heart disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PON", "type": "GeneOrGeneProduct"}, {"text": "192Q/R", "type": "SequenceVariant"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "192RR", "type": "SequenceVariant"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Analyses indicated no association between the NQO1 * 2 polymorphism and the risk of anthracycline-related CHF ( odds ratio [ OR ] , 1.04 ; P=.97 ) .

## Item biored:test:433
Example input:
Sentence: We describe in a BSS patient the first case of homozygous four bases deletion ( TGAG ) in the gpIbalpha gene coding sequence , leading to a premature stop codon .

Example answer:
{"entities": [{"text": "BSS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "deletion ( TGAG )", "type": "SequenceVariant"}, {"text": "gpIbalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We investigated clinical and cellular phenotypes of 24 children with mutations in the catalytic ( alpha ) subunit of the mitochondrial DNA ( mtDNA ) gamma polymerase ( POLG1 ) .

Example answer:
{"entities": [{"text": "mitochondrial DNA ( mtDNA ) gamma polymerase", "type": "GeneOrGeneProduct"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: With the advent of next-generation sequencing technologies , the homozygous mutations T71N and A190T in the neuronal calcium sensor ( NCS ) hippocalcin were identified as the genetic cause of primary isolated dystonia ( DYT2 dystonia ) .

Example answer:
{"entities": [{"text": "T71N", "type": "SequenceVariant"}, {"text": "A190T", "type": "SequenceVariant"}, {"text": "neuronal calcium sensor", "type": "GeneOrGeneProduct"}, {"text": "NCS", "type": "GeneOrGeneProduct"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "primary isolated dystonia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DYT2", "type": "GeneOrGeneProduct"}, {"text": "dystonia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Previously , we and others reported that recessive mutations in the embryonal acetylcholine receptor g subunit ( CHRNG ) can cause both lethal and nonlethal MPS , thus demonstrating that pterygia resulted from fetal akinesia .

## Item biored:test:545
Example input:
Sentence: The polymorphism did not show any association with FHCM .

Example answer:
{"entities": [{"text": "FHCM", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Other regions , such as the transactivation domain , seem to be slightly more polymorphic in the human population and the impact on functionality should be further examined .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Seven novel single-nucleotide polymorphisms ( SNPs ) were also found , of which a change of leucine 269 to phenylalanine ( Leu269Phe ) was found in 12 of 18 patients with the Arg555Trp mutation .

Example answer:
{"entities": [{"text": "leucine 269 to phenylalanine", "type": "SequenceVariant"}, {"text": "Leu269Phe", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Arg555Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: The result of PCR associated with restriction fragment length polymorphism analysis also suggested that this mutation is heterozygous .

Example answer:
{"entities": []}

Example input:
Sentence: Whereas we confirmed lack of direct correlation between the clinical phenotype and the genotype , we also found that the so-called 'common mutation ' ( p.R50X ) accounted for about 43 % of alleles in our cohort and that no population-related mutations are clearly identified in Italian patients .

Example answer:
{"entities": [{"text": "p.R50X", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Similarly , NF1 alterations including homozygous deletions and splicing mutations were identified in 9 ( 22 % ) of 41 primary OSCs .

Example answer:
{"entities": [{"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: None of the studied polymorphisms alone affected overall or progression-free survival ( PFS ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Eighteen single nucleotide polymorphisms ( SNPs ) were identified , seven of which were missense , with no truncation or frame shift mutations .

Example answer:
{"entities": []}

Input:
Sentence: In conclusion , the majority of the detected sequence alterations were polymorphisms without obvious functional relevance .

## Item biored:test:522
Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : The G-395A polymorphism of the human Klotho gene is associated with EH and may be a potential regulatory site .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The aim of this study was to test if the IGF-1 gene polymorphisms are associated with the GH-dose of GH-deficient adults .

## Item biored:test:548
Example input:
Sentence: ETV6 proteins with mutations outside of amino acids 332-452 localize to the nucleus , whereas proteins with mutations within amino acids 332-452 remain in the cytoplasm .

Example answer:
{"entities": [{"text": "ETV6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This mutation consists of two consecutive substitutions ( 735-6 TG > AT ) that cause two nonsense mutations ( Y245X , G246X ) , inherited in an autosomal dominant fashion , on one parental chromosome .

Example answer:
{"entities": [{"text": "735-6 TG > AT", "type": "SequenceVariant"}, {"text": "Y245X", "type": "SequenceVariant"}, {"text": "G246X", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation caused protein truncation , and represents a novel case of consecutive nonsense mutations in human disease .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Both mutations reside in the tetratricopeptide repeats of OGT that are essential for substrate recognition .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In this family , a heterozygous cytosine insertion in exon 10 ( c.1546_1547insC ) inducing a frame shift mutation of MEN1 was found in the proband and the other two suffering members of his family .

Example answer:
{"entities": [{"text": "cytosine insertion", "type": "SequenceVariant"}, {"text": "c.1546_1547insC", "type": "SequenceVariant"}, {"text": "MEN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The first is the frameshift mutation ( P686fs ) caused by the insertion of the four nucleotides CCCC in exon 16 ( 2172_2173insCCCC ) that is predicted to terminate translation before the catalytic serine .

Example answer:
{"entities": [{"text": "P686fs", "type": "SequenceVariant"}, {"text": "insertion of the four nucleotides CCCC", "type": "SequenceVariant"}, {"text": "2172_2173insCCCC", "type": "SequenceVariant"}]}

Example input:
Sentence: This is the first known constitutional rearrangement of SYT14 , and further systematic genetic analysis and clinical studies of DGAP128 may offer unique insights into the role of SYT14 in neurodevelopment .

Example answer:
{"entities": [{"text": "SYT14", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The two transversions resulted in the substitution of a stop codon for glutamine at codon 298 ( p.Q298X ) and a missense mutation at codon 358 , tyrosine to histidine ( p.Y358H ) .

Example answer:
{"entities": [{"text": "stop codon for glutamine at codon 298", "type": "SequenceVariant"}, {"text": "p.Q298X", "type": "SequenceVariant"}, {"text": "codon 358 , tyrosine to histidine", "type": "SequenceVariant"}, {"text": "p.Y358H", "type": "SequenceVariant"}]}

Example input:
Sentence: ETV6 , or Translocation-Ets-Leukemia ( TEL ) , is an ETS family transcriptional repressor that is essential for establishing hematopoiesis in neonatal bone marrow , and is frequently a target of chromosomal translocations in human cancer .

Example answer:
{"entities": [{"text": "ETV6", "type": "GeneOrGeneProduct"}, {"text": "Translocation-Ets-Leukemia", "type": "GeneOrGeneProduct"}, {"text": "TEL", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We propose that the alteration in the replication/nuclear location pattern of the non-deleted TDR22 indicates an altered gene regulation hence an altered transcritpion in DGS/VCFS .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Insertional translocations ( IT ) are rare structural rearrangements .

## Item biored:test:550
Example input:
Sentence: Haplotype analysis suggests a germline mosaicism of the 2-bp deletion in the maternal grandmother of both affected individuals .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Two additional loci displayed an evidence of linkage ( LOD > 3 ) and included a locus on 16p13 , proximal to the gene encoding NDE1 , which has been shown to biologically interact with DISC1 .

Example answer:
{"entities": [{"text": "NDE1", "type": "GeneOrGeneProduct"}, {"text": "DISC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : We have confirmed the localization of the congenital microcoria locus ( MCOR ) to 13q31-q32 in a large Asian Indian family and conclude that current information suggests this is a single locus disorder and genetically homogeneous .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Multipoint analysis revealed a 4 cM region encompassing D13S1300 to D13S1280 where the LOD remains just over 6.0 Thus we confirm localization of the congenital microcoria locus to chromosomal locus 13q31-q32 .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The mutations concordantly segregate in all available families according a recessive mode of inheritance .

Example answer:
{"entities": []}

Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A disease co-segregating haplotype was detected in two hereditary autosomal dominant cases .

Example answer:
{"entities": []}

Example input:
Sentence: Linkage to the chromosomal locus 13q31-q32 has previously been reported in a large French family .

Example answer:
{"entities": []}

Input:
Sentence: We describe an IT between chromosomes 3 and 13 segregating in a three-generation pedigree .

## Item biored:test:511
Example input:
Sentence: We conclude that the SNPs of SLC2A2 predict the conversion to diabetes in obese subjects with IGT .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that TNMD polymorphisms are associated with adiposity and also with glucose metabolism and conversion from IGT to T2D in men .

Example answer:
{"entities": [{"text": "TNMD", "type": "GeneOrGeneProduct"}, {"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}]}

Example input:
Sentence: None of the SNPs or indels were associated with diabetes-related traits or accounted for a previously identified quantitative trait locus on chromosome 13 for fasting serum glucose .

Example answer:
{"entities": [{"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Measured genotype analysis tested associations between SNPs and obesity and diabetes-related traits .

Example answer:
{"entities": [{"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our aim was to study the associations of individual single nucleotide polymorphisms and haplotypes with adiposity , glucose metabolism , and the risk of type 2 diabetes ( T2D ) .

Example answer:
{"entities": [{"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: According to recent genome-wide association studies , a number of single nucleotide polymorphisms ( SNPs ) are reported to be associated with type 2 diabetes mellitus ( T2DM ) .

## Item biored:test:515
Example input:
Sentence: In overall analysis , the homozygous Cys/Cys genotype showed a significant association with lung cancer compared to Ser allele carrier status ( odds ratio ( OR ) =1.31 , 95 % confidence interval ( CI ) =1.02-1.69 ) .

Example answer:
{"entities": [{"text": "lung cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We also observed associations for candidate SNPs in CRP , GSTP1 , and IL1B .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Conditional haplotype analysis revealed three other SNPs , rs204890 ( OR = 1.86 , p = 1.2 10 ( -4 ) ) , rs2071349 ( OR = 1.53 , p = 1.0 10 ( -3 ) ) , and rs2844580 ( OR = 1.43 , p = 1.3 10 ( -3 ) ) , to be associated with SLE independent of the rs9271366 SNP .

Example answer:
{"entities": [{"text": "rs204890", "type": "SequenceVariant"}, {"text": "rs2071349", "type": "SequenceVariant"}, {"text": "rs2844580", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Using the two Asian cohorts , significant association of FCGR2B-232Thr/Thr with SLE was observed only in the presence of CD72- * 1/ * 1 genotype ( OR 4.63 , 95 % CI 1.47-14.6 , P=0.009 versus FCGR2B-232Ile/Ile plus CD72- * 2/ * 2 ) .

Example answer:
{"entities": [{"text": "FCGR2B-232Thr/Thr", "type": "GeneOrGeneProduct"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD72-", "type": "GeneOrGeneProduct"}, {"text": "FCGR2B-232Ile/Ile", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our strongest signal , the rs9271366 SNP , was also associated with higher risk of SLE in a previous Chinese genome-wide association study ( GWAS ) .

Example answer:
{"entities": [{"text": "rs9271366", "type": "SequenceVariant"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A significant association of the rs729302 A allele with RA susceptibility was found in both sets ( odds ratio ( OR ) 1.22 , 95 % CI 1.09 to 1.35 , p < 0.001 in the combined analysis ) .

Example answer:
{"entities": [{"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: The most strongly associated SNP with SLE was the rs9271366 ( odds ratio , OR = 1.70 , p = 5.6 10 ( -5 ) ) near the HLA-DRB1 gene .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs9271366", "type": "SequenceVariant"}, {"text": "HLA-DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : We found that the presence of the -1021T allele was associated with AD : odds ratio = 1.2 ( 95 % confidence interval : 1.06-1.4 , p = 0.005 ) .

Example answer:
{"entities": [{"text": "-1021T", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The strongest association was found in a variant of CDKAL1 [ rs7754840 , odds ratio ( OR ) = 1.77 , 95 % CI = 1.50-2.10 , p = 5.0 x 10 ( -11 ) ] .

## Item biored:test:551
Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: In order to explain the reduced genetic heterogeneity detected by Alu insertions among Basque subpopulations , values of the Wright 's F ( ST ) statistic were estimated for both Alu markers and a set of short tandem repeats ( STRs ) in terms of two geographical scales : ( 1 ) the Basque Country , ( 2 ) Europe ( including Basques ) .

Example answer:
{"entities": []}

Example input:
Sentence: Microsatellite markers at 13q31-q32 were PCR amplified and run on an ABI Prism 310 genetic analyzer and genotyped with the GeneScan analysis .

Example answer:
{"entities": []}

Example input:
Sentence: By multipoint linkage analysis with markers spanning the entire X-chromosome we mapped the disease locus to a 28-Mb interval between Xp11.4 and Xq12 , including the BCOR gene .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: An 18 kb genomic clone hybridizing with the h mu OR1 cDNA contains 63 and 489 bp exonic sequences flanked by splice donor/acceptor sequences .

Example answer:
{"entities": [{"text": "h mu OR1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Analysis of hybridization to DNA prepared from human rodent hybrid cell lines and chromosomal in situ hybridization studies indicate localization to 6q24-25 .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Exonic and intronic segments , 5 ' and 3 ' flanking regions of IRS2 ( 14.5 kb ) , were bidirectionally sequenced for single nucleotide polymorphism ( SNP ) discovery in 934 Hispanic children using 3730XL DNA Sequencers .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : DNA sequencing disclosed a heterozygous G > T substitution at nucleotide c.898 within exon 10 ( NM_203475.1 ) , converting a glutamic acid residue ( GAA ) to a premature termination codon ( TAA ) .

Example answer:
{"entities": [{"text": "G > T substitution at nucleotide c.898", "type": "SequenceVariant"}, {"text": "glutamic acid residue ( GAA ) to a premature termination codon ( TAA )", "type": "SequenceVariant"}]}

Example input:
Sentence: The phenotype co-segregates with short-tandem repeat markers flanking the TMC1 gene at the DFNA36 locus on chromosome 9q31-q21 .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 28 bp variable number of tandem repeats ( VNTR ) , a G/C single nucleotide polymorphism ( SNP ) , and a deletion of 6 bp at position 1494 were studied .

Example answer:
{"entities": [{"text": "28 bp variable number of tandem repeats", "type": "SequenceVariant"}, {"text": "G/C", "type": "SequenceVariant"}, {"text": "deletion of 6 bp at position 1494", "type": "SequenceVariant"}]}

Input:
Sentence: Short tandem repeat ( STR ) segregation analysis and array-comparative genomic hybridization were used to define the IT as a 25.1 Mb segment spanning 13q21.2-q31.1 .

## Item biored:test:520
Example input:
Sentence: Genome-wide association studies have identified genomic loci , whose single-nucleotide polymorphisms ( SNPs ) predispose to prostate cancer ( PCa ) .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Two microsatellites , 1 insertion/deletion , and 8 single nucleotide polymorphisms ( SNPs ) in the regulatory region of iNOS were genotyped in 200 POAG patients and 200 age-matched controls .

Example answer:
{"entities": [{"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We investigated the association between chronic ITP and the frequency of the single-nucleotide polymorphism rs763780 ( 7488T/C ) , which causes a His-to-Arg substitution at amino acid 161 .

Example answer:
{"entities": [{"text": "chronic ITP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs763780", "type": "SequenceVariant"}, {"text": "7488T/C", "type": "SequenceVariant"}, {"text": "His-to-Arg substitution at amino acid 161", "type": "SequenceVariant"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: None of the SNPs or indels were associated with diabetes-related traits or accounted for a previously identified quantitative trait locus on chromosome 13 for fasting serum glucose .

Example answer:
{"entities": [{"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Plasminogen activator inhibitor type 1 serum levels and 4G/5G gene polymorphism in morbidly obese Hispanic patients with non-alcoholic fatty liver disease .

Example answer:
{"entities": [{"text": "Plasminogen activator inhibitor type 1", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential regulatory single nucleotide polymorphism in the promoter of the Klotho gene may be associated with essential hypertension in the Chinese Han population .

Example answer:
{"entities": [{"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Common single nucleotide polymorphisms ( SNPs ) within this gene , rs6232 and rs6235 , are associated with obesity .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: AIMS : Several SNPs and a microsatellite cytosine-adenine repeat promoter polymorphism of the IGF-1 gene have been reported to be associated with circulating IGF-1 serum concentrations .

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

## Item biored:test:528
Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genetic Variation at the Sulfonylurea Receptor , Type 2 Diabetes , and Coronary Heart Disease .

Example answer:
{"entities": [{"text": "Sulfonylurea Receptor", "type": "GeneOrGeneProduct"}, {"text": "Type 2 Diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Coronary Heart Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutant receptor hGRalphaD401H enhances the transcriptional activity of glucocorticoid-responsive genes .

Example answer:
{"entities": [{"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid-responsive genes", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Treatment with recombinant DNA-derived IGF-I resulted in growth acceleration .

Example answer:
{"entities": [{"text": "IGF-I", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Therefore , genetic variations of the IGF-1 gene seem not to be major influencing factors of the GH-IGF-axis causing variable response to exogenous GH-treatment .

## Item biored:test:441
Example input:
Sentence: SRD5A2 gene analysis revealed 2 consecutive mutations in exon 4 , each located in a different allele : 1 ) a T nucleotide deletion , which predicts a frameshift mutation from codon 219 , and 2 ) a missense mutation at codon 227 , where the substitution of guanine ( CGA ) by adenine ( CAA ) predicts a glutamine replacement of arginine ( R227Q ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "T nucleotide deletion , which predicts a frameshift mutation from codon 219", "type": "SequenceVariant"}, {"text": "guanine ( CGA ) by adenine ( CAA )", "type": "SequenceVariant"}, {"text": "glutamine replacement of arginine", "type": "SequenceVariant"}, {"text": "R227Q", "type": "SequenceVariant"}]}

Example input:
Sentence: Four patients harbor yet non-described SRD5A2 gene mutations : a single nucleotide deletion ( del642T ) , a G158R amino acid substitution , a splice junction mutation ( IVS3+1G > A ) , and the insertion of a cytosine ( 217_218insC ) occurring at a CCCC motif .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G158R", "type": "SequenceVariant"}, {"text": "IVS3+1G > A", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}]}

Example input:
Sentence: Sequencing of the GJB2 gene showed that the child was heterozygous for a novel nucleotide change , c.263C > T , in exon 2 , leading to a substitution of alanine for valine at position 88 ( p.Ala88Val ) .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}, {"text": "c.263C > T", "type": "SequenceVariant"}, {"text": "alanine for valine at position 88", "type": "SequenceVariant"}, {"text": "p.Ala88Val", "type": "SequenceVariant"}]}

Example input:
Sentence: Whereas no mutations were detected in the PDE6H gene , mutations in KCNV2 were identified in all patients , in either the homozygous or compound heterozygous state .

Example answer:
{"entities": [{"text": "PDE6H", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We detected a novel , single , heterozygous nucleotide ( G -- > C ) substitution at position 1201 ( exon 2 ) of the hGR gene , which resulted in aspartic acid to histidine substitution at amino acid position 401 in the amino-terminal domain of the hGRalpha .

Example answer:
{"entities": [{"text": "( G -- > C ) substitution at position 1201", "type": "SequenceVariant"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "aspartic acid to histidine substitution at amino acid position 401", "type": "SequenceVariant"}, {"text": "hGRalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Another POF patient of African origin showed a homozygous nucleotide change in the tenth of DMC1 gene that led to an alteration of the amino acid composition of the protein ( M200V ) .

Example answer:
{"entities": [{"text": "POF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "M200V", "type": "SequenceVariant"}]}

Example input:
Sentence: This mutation resulted in replacement of a non-polar amino acid ( proline ) with a polar amino acid ( serine ) at position 29 ( P29S ) .

Example answer:
{"entities": [{"text": "( proline ) with a polar amino acid ( serine ) at position 29", "type": "SequenceVariant"}, {"text": "P29S", "type": "SequenceVariant"}]}

Example input:
Sentence: Mutation analysis of the plakophilin 1 gene PKP1 revealed a homozygous deletion of C at nucleotide 888 within exon 5 .

Example answer:
{"entities": [{"text": "plakophilin 1", "type": "GeneOrGeneProduct"}, {"text": "PKP1", "type": "GeneOrGeneProduct"}, {"text": "deletion of C at nucleotide 888", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this report the distribution of the exonic G/A single nucleotide polymorphism ( SNP ) in purine nucleoside phosphorylase ( PNP ) gene , resulting in the amino acid substitution serine to glycine at position 51 ( G51S ) , was investigated in a large population of AD patients ( n=321 ) and non-demented control ( n=208 ) .

Example answer:
{"entities": [{"text": "G/A", "type": "SequenceVariant"}, {"text": "purine nucleoside phosphorylase", "type": "GeneOrGeneProduct"}, {"text": "PNP", "type": "GeneOrGeneProduct"}, {"text": "serine to glycine at position 51", "type": "SequenceVariant"}, {"text": "G51S", "type": "SequenceVariant"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: RESULTS : We identified a patient homozygous for a nucleotide change c.1445T > G , resulting in a novel homozygous substitution of the non-polar hydrophobic phenylalanine to the polar hydrophilic cysteine in exon 6 at codon 482 ( p.F482C ) of the PKD2 gene and a de-novo PKD1 splice-site variant IVS21-2delAG .

## Item biored:test:536
Example input:
Sentence: Disruption of the temporally regulated cloaca endodermal b-catenin signaling causes anorectal malformations .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "anorectal malformations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Testis morphology showed that , during early infancy , the 5-alpha-reductase enzyme deficiency may not have affected interstitial or tubular development .

Example answer:
{"entities": [{"text": "5-alpha-reductase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Also known as Goltz syndrome , FDH presents with characteristic linear streaks of hypoplastic dermis and variable abnormalities of bone , nails , hair , limbs , teeth and eyes .

Example answer:
{"entities": [{"text": "Goltz syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoplastic dermis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although congenital malformations , such as anorectal malformations ( ARMs ) , are frequently observed during this process , the underlying pathogenic mechanisms remain unclear .

Example answer:
{"entities": [{"text": "congenital malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "anorectal malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARMs", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A patient of Chinese origin with ambiguous genitalia at 14 months , a 46 , XY karyotype , and normal T secretion under human chorionic gonadotropin ( hCG ) stimulation underwent a gonadectomy at 20 months .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "human chorionic gonadotropin", "type": "ChemicalEntity"}, {"text": "hCG", "type": "ChemicalEntity"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Defect in androgen action on the target tissues or production of active metabolite share common morphological features .

Example answer:
{"entities": []}

Example input:
Sentence: Defects in these organelles cause inherited human disorders ( ciliopathies ) such as retinitis pigmentosa and Bardet-Biedl syndrome ( BBS ) , frequently affecting many physiological and developmental processes across multiple organs .

Example answer:
{"entities": [{"text": "inherited human disorders", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ciliopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinitis pigmentosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bardet-Biedl syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BBS", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In contrast to disorders of sexual differentiation caused by lack of androgen production or inhibited androgen action , defects affecting development of the bipotent genital anlagen have rarely been investigated in humans .

## Item biored:test:508
Example input:
Sentence: SEREX screening of cDNA expression libraries derived from 3 breast cancer patients identified a total of 88 positive clones ( bcg-1 to bcg-88 ) , including 27 hitherto unknown sequences .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : We identified in ACC CD133-positive CSC that expressed NOTCH1 and SOX10 , formed spheroids , and initiated tumors in nude mice .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133-positive", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Tumor TS 1494del6 genotype may be a prognostic factor in FU-based adjuvant treatment of colorectal cancer patients .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "FU-based", "type": "ChemicalEntity"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : These data provide strong support for the hypothesis that common variation in GPX4 is associated with prognosis after a diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined associations between 54 polymorphisms that tag the known common variants ( minor allele frequency > 0.05 ) in 10 genes involved in oxidative damage repair ( CAT , SOD1 , SOD2 , GPX1 , GPX4 , GSR , TXN , TXN2 , TXNRD1 , and TXNRD2 ) and survival in 4,470 women with breast cancer .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "GPX1", "type": "GeneOrGeneProduct"}, {"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "GSR", "type": "GeneOrGeneProduct"}, {"text": "TXN", "type": "GeneOrGeneProduct"}, {"text": "TXN2", "type": "GeneOrGeneProduct"}, {"text": "TXNRD1", "type": "GeneOrGeneProduct"}, {"text": "TXNRD2", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CONCLUSION : It is possible that CCND3 rs2479717 , or another variant it tags , is associated with prognosis after a diagnosis of breast cancer .

## Item biored:test:519
Example input:
Sentence: Treatment with recombinant DNA-derived IGF-I resulted in growth acceleration .

Example answer:
{"entities": [{"text": "IGF-I", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONTEXT : Interindividual variations in glucocorticoid sensitivity have been associated with manifestations of cortisol excess or deficiency and may be partly explained by polymorphisms in the human glucocorticoid receptor ( hGR ) gene .

Example answer:
{"entities": [{"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "cortisol", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The G-395A polymorphism of the human Klotho gene is associated with EH and may be a potential regulatory site .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Differences in the genotype distributions of the G-395A polymorphism between the EH and non-hypertension groups are statistically significant ( P=0.032 ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There are differential effects of age , gender and smoking status on the association of the G-395A polymorphism with EH ; the G-395A polymorphism is significantly associated with EH in subjects over 60years old , in females and in nonsmokers .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : We investigate whether the G-395A polymorphism of Klotho is associated with EH in a population consisting of 215 patients with EH and 220 non-hypertensive subjects .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Mutations affecting the intracellular domain of the GHR can result in GH insensitivity and IGF deficiency , despite normal serum concentrations of GHBP .

Example answer:
{"entities": [{"text": "GHR", "type": "GeneOrGeneProduct"}, {"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GHBP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Atypical GH insensitivity syndrome and severe insulin-like growth factor-I deficiency resulting from compound heterozygous mutations of the GH receptor , including a novel frameshift mutation affecting the intracellular domain .

Example answer:
{"entities": [{"text": "GH insensitivity syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin-like growth factor-I deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND/AIMS : GH insensitivity and IGF deficiency may result from aberrations of the GH receptor ( GHR ) .

Example answer:
{"entities": [{"text": "GH insensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGF deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GH receptor", "type": "GeneOrGeneProduct"}, {"text": "GHR", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Growth hormone dose in growth hormone-deficient adults is not associated with IGF-1 gene polymorphisms .

## Item biored:test:431
Example input:
Sentence: In addition to hyperthyroidism , ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers were consistently found in all affected individuals .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Twenty-one had Alpers syndrome , the commonest severe POLG1 autosomal recessive phenotype , comprising hepatoencephalopathy and often mtDNA depletion .

Example answer:
{"entities": [{"text": "Alpers syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}, {"text": "hepatoencephalopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Myotonic dystrophy ( DM ) , the most prevalent muscular disorder in adults , is caused by ( CTG ) n-repeat expansion in a gene encoding a protein kinase ( DM protein kinase ; DMPK ) and involves changes in cytoarchitecture and ion homeostasis .

Example answer:
{"entities": [{"text": "Myotonic dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "muscular disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DM protein kinase", "type": "GeneOrGeneProduct"}, {"text": "DMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Loss-of-function mutations in PTPN11 cause metachondromatosis , but not Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "metachondromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Ventriculomegaly and bilateral shortening of the fifth metacarpal bones and the middle phalanges of the fifth fingers might be characteristic features of NAH because of an activating TSHR germline mutation .

Example answer:
{"entities": [{"text": "Ventriculomegaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TSHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Oculopharyngeal muscular dystrophy ( OPMD ) is a late onset autosomal dominant muscle disorder .

Example answer:
{"entities": [{"text": "Oculopharyngeal muscular dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "autosomal dominant muscle disorder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metachondromatosis ( MC ) is a rare , autosomal dominant , incompletely penetrant combined exostosis and enchondromatosis tumor syndrome .

Example answer:
{"entities": [{"text": "Metachondromatosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "exostosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "enchondromatosis tumor syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Analysis of a nuclear family with three affected offspring identified an autosomal-recessive form of spondyloepimetaphyseal dysplasia characterized by severe short stature and a unique constellation of radiographic findings .

Example answer:
{"entities": [{"text": "spondyloepimetaphyseal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "short stature", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MC is clinically distinct from other multiple exostosis or multiple enchondromatosis syndromes and is unlinked to EXT1 and EXT2 , the genes responsible for autosomal dominant multiple osteochondromas ( MO ) .

Example answer:
{"entities": [{"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple exostosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "multiple enchondromatosis syndromes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EXT1", "type": "GeneOrGeneProduct"}, {"text": "EXT2", "type": "GeneOrGeneProduct"}, {"text": "multiple osteochondromas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MO", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Multiple pterygium syndromes ( MPS ) comprise a group of multiple congenital anomaly disorders characterized by webbing ( pterygia ) of the neck , elbows , and/or knees and joint contractures ( arthrogryposis ) .

## Item biored:test:574
Example input:
Sentence: Genomic DNA was extracted from blood samples , and DNA fragments containing the site of polymorphism were amplified by PCR .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA extracted from peripheral blood was amplified by polymerase chain reaction ( PCR ) method and the exons of all candidate genes were sequenced .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: EXPERIMENTAL DESIGN : Genomic DNA was purified from peripheral blood mononuclear cells or tissue specimens .

Example answer:
{"entities": []}

Example input:
Sentence: After informed consent was obtained , genomic DNA was extracted from the venous blood of all participants .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was isolated from the leukocytes and genotyping was performed using the Sequenom platform .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was isolated from peripheral blood and genotyping was performed with PCR-based methods .

Example answer:
{"entities": []}

Example input:
Sentence: Peripheral blood samples were collected and genomic DNA was extracted from the leukocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA was isolated from the venous blood leukocytes of 322 unrelated patients with schizophrenia , 156 patients with depression , 300 patients with heroin addiction , and 300 healthy unrelated individuals .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "heroin addiction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genomic DNA was isolated from the white blood cells of all family members of the affected case following standard established protocols .

Example answer:
{"entities": []}

Input:
Sentence: Blood samples were obtained from all patients and genomic DNA was isolated .

## Item biored:test:434
Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conclude that heterozygous loss-of-function mutations in PTPN11 are a frequent cause of MC , that lesions in patients with MC appear to arise following a `` second hit , '' that MC may be locus heterogeneous since 1 familial and 5 sporadically occurring cases lacked obvious disease-causing PTPN11 mutations , and that PTPN11 mutations are not a common cause of Ollier disease or Maffucci syndrome .

Example answer:
{"entities": [{"text": "PTPN11", "type": "GeneOrGeneProduct"}, {"text": "MC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Ollier disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Maffucci syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Novel CACNA1S mutation causes autosomal dominant hypokalemic periodic paralysis in a South American family .

Example answer:
{"entities": [{"text": "CACNA1S", "type": "GeneOrGeneProduct"}, {"text": "hypokalemic periodic paralysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Recent reports have demonstrated that mutations in the OPHN1 gene were responsible for a syndromic rather than non-specific mental retardation .

Example answer:
{"entities": [{"text": "OPHN1", "type": "GeneOrGeneProduct"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The mother and daughter were each heterozygous for PPARG nonsense mutation Y355X , whose protein product in vitro was transcriptionally inactive with no dominant-negative activity against the wild-type receptor .

Example answer:
{"entities": [{"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "Y355X", "type": "SequenceVariant"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The fact that no truncation or frame shift mutations have been found in any of the VUR patients , coupled with our recent finding that some breeding pairs of UP III knockout mice yield litters that show not only VUR , but also severe hydronephrosis and neonatal death , raises the possibility that major uroplakin mutations could be embryonically or postnatally lethal in humans .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "UP III", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "hydronephrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neonatal death", "type": "DiseaseOrPhenotypicFeature"}, {"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "humans", "type": "OrganismTaxon"}]}

Input:
Sentence: We hypothesized that mutations in acetylcholine receptor-related genes might also result in a MPS/fetal akinesia phenotype and so we analyzed 15 cases of lethal MPS/fetal akinesia without CHRNG mutations for mutations in the CHRNA1 , CHRNB1 , CHRND , and rapsyn ( RAPSN ) genes .

## Item biored:test:576
Example input:
Sentence: Moderate or severe adverse events were more common in subjects on clonidine ( 79.4 % versus 49.2 % ; p =.0006 ) but not associated with higher rates of early study withdrawal .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Eighty-one percent of patients with dyskinesia had clinical fluctuations .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: We therefore examined the associations with AD of the DBH -1021T allele and of the above interactions in the Epistasis Project , with 1757 cases of AD and 6294 elderly controls .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "-1021T", "type": "SequenceVariant"}]}

Example input:
Sentence: A statistically significant difference in allele frequency between cases and controls was observed for 2 of the SNPs ( +3100 T/G and +8365 C/T ) , with an odds ratio of 0.78 ( 95 % CI=0.64-0.96 ) and 0.65 ( 95 % CI=0.45-0.94 ) respectively .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Study results showed that myoclonus incidence was 85 % , 40 % , 70 % , and 25 % in Group NP , Group F , Group M , and Group FM , respectively , and were significantly lower in Group F and Group FM .

Example answer:
{"entities": [{"text": "myoclonus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have investigated this gene in a large UK case-control sample ( bipolar I disorder N = 687 , unipolar recurrent major depression N = 1,036 , controls N = 1,204 ) .

Example answer:
{"entities": [{"text": "bipolar I disorder", "type": "DiseaseOrPhenotypicFeature"}, {"text": "unipolar recurrent major depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: D allelic was significantly associated with DDD ( p value = 0.027 , odds ratio = 1.41 with 95 % CI = 1.04-1.90 ) while Genotypic association on the presence of D allele was also significantly associated with DDD ( p value = 0.046 , odds ratio = 1.50 with 95 % CI = 1.01-2.24 ) .

Example answer:
{"entities": [{"text": "DDD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Twenty-four of 113 ( 21 % ) gastric cancer patients had the II , 57 ( 51 % ) the ID , and 32 ( 28 % ) the DD genotype .

Example answer:
{"entities": [{"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: In the control subjects , the frequency of DD was 18.8 % ( n = 18 ) , ID was 50 % ( n = 48 ) and II was 31.3 % ( n = 30 ) .

## Item biored:test:531
Example input:
Sentence: The boy developed intraventricular and intracerebral haemorrhage , leading to hydrocephalus .

Example answer:
{"entities": [{"text": "intraventricular and intracerebral haemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hydrocephalus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A TSPO ligand attenuates brain injury after intracerebral hemorrhage .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged hypothermia as a bridge to recovery for cerebral edema and intracranial hypertension associated with fulminant hepatic failure .

Example answer:
{"entities": [{"text": "hypothermia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracranial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fulminant hepatic failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Twenty-one of the 24 patients did not have evidence of new cerebral ischemic injury , but seizures were likely due to ischemic brain injury in 3 patients .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cerebral ischemic injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic brain injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : The rate of major hemorrhage was high in this old , frail group , but excluding fatalities , resulted in no long-term sequelae , and the stroke rate on warfarin was low , demonstrating how effective warfarin treatment is .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND AND PURPOSE : Cerebral microbleeds ( MB ) are potential risk factors for intracerebral hemorrhage ( ICH ) , but it is unclear if they are a contraindication to using antithrombotic drugs .

Example answer:
{"entities": [{"text": "Cerebral microbleeds", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antithrombotic drugs", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHOD : Case-based observations from a medical intensive care unit ( MICU ) in a tertiary care facility in a 27-year-old female with FHF from acetaminophen and resultant cerebral edema .

Example answer:
{"entities": [{"text": "FHF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acetaminophen", "type": "ChemicalEntity"}, {"text": "cerebral edema", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Warfarin-associated intracerebral hemorrhage ( W-ICH ) is a severe type of stroke .

Example answer:
{"entities": [{"text": "Warfarin-associated", "type": "ChemicalEntity"}, {"text": "intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "W-ICH", "type": "ChemicalEntity"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Intracerebral hemorrhage ( ICH ) is a devastating disease without effective treatment .

Example answer:
{"entities": [{"text": "Intracerebral hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Intracranial hemorrhage has been reported in a small number of OI patients .

## Item biored:test:540
Example input:
Sentence: In this study , DNA sequencing of the 12 exons of the PCSK9 gene has been performed in 51 Norwegian subjects with a clinical diagnosis of familial hypercholesterolemia where mutations in the low-density lipoprotein receptor gene and mutation R3500Q in the apolipoprotein B-100 gene had been excluded .

Example answer:
{"entities": [{"text": "PCSK9", "type": "GeneOrGeneProduct"}, {"text": "familial hypercholesterolemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low-density lipoprotein receptor", "type": "GeneOrGeneProduct"}, {"text": "R3500Q", "type": "SequenceVariant"}, {"text": "apolipoprotein B-100", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Nine distinct mutations including one small deletion mutation ( 46delS ) , two small insertion mutations ( 118-119insA and 125-126insAA ) , and six non-synonymous mutations ( A6V , P163S , E359K , P407Q , S429T and A442V ) were identified in 12 of the 486 patients ( nine with ventricular septal defect , two with Tetralogy of Fallot , and one with endocardial cushion defect ) .

Example answer:
{"entities": [{"text": "46delS", "type": "SequenceVariant"}, {"text": "118-119insA", "type": "SequenceVariant"}, {"text": "125-126insAA", "type": "SequenceVariant"}, {"text": "A6V", "type": "SequenceVariant"}, {"text": "P163S", "type": "SequenceVariant"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "P407Q", "type": "SequenceVariant"}, {"text": "S429T", "type": "SequenceVariant"}, {"text": "A442V", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Tetralogy of Fallot", "type": "DiseaseOrPhenotypicFeature"}, {"text": "endocardial cushion defect", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Included were 5,128 CL/P cases , 1,745 CPO cases , and 3,712 controls ( like-sexed , non-malformed liveborn infant , born immediately after a malformed one , in the same hospital ) , over 4,199,630 consecutive births .

Example answer:
{"entities": [{"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Seven hundred fifty three subjects , corresponding to 251 full trios of childhood-onset SLE families , were genotyped and analyzed using transmission disequilibrium testing ( TDT ) and multitest corrections .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Non-predefined geographical areas with significantly unusual cleft BPRs were identified with Kulldorf and Nagarwalla 's spatial scan statistic , employing number of cases and births , and exact location of each hospital .

Example answer:
{"entities": []}

Example input:
Sentence: The aim of this work was to search for unequal birth prevalence rates ( BPRs ) of cleft lip +/- cleft palate ( CL/P ) , and cleft palate only ( CPO ) , among different geographic areas in South America , and to analyze phenotypic characteristics and associated risk factors in each identified cluster .

Example answer:
{"entities": [{"text": "cleft lip", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cleft palate", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CL/P", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CPO", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Eighteen children with DSD and cleft palate were identified in the L beck DSD database ( about 1,500 entries ) .
