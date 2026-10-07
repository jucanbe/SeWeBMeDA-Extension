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

## Item biored:test:359
Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: XRCC1 Arg399Gln gene polymorphism and the risk of systemic lupus erythematosus in the Polish population .

Example answer:
{"entities": [{"text": "XRCC1", "type": "GeneOrGeneProduct"}, {"text": "Arg399Gln", "type": "SequenceVariant"}, {"text": "systemic lupus erythematosus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Two single nucleotide polymorphisms in the ET-1 gene ( EDN1 ) have been reported to be associated with blood pressure ( BP ) .

Example answer:
{"entities": [{"text": "ET-1", "type": "GeneOrGeneProduct"}, {"text": "EDN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA polymorphisms at CYP11B2/B1 locus may confer susceptibility to postoperative hypertension of patients with APA .

Example answer:
{"entities": [{"text": "CYP11B2/B1", "type": "GeneOrGeneProduct"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Specifically , the rs4539 ( AA ) polymorphism was associated with persistent postoperative hypertension ( P = .002 ) .

Example answer:
{"entities": [{"text": "rs4539", "type": "SequenceVariant"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We hypothesised that the G-395A polymorphism in the promoter region of the human Klotho gene may contribute to the prevalence of Essential Hypertension ( EH ) .

Example answer:
{"entities": [{"text": "G-395A", "type": "SequenceVariant"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "Essential Hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential regulatory single nucleotide polymorphism in the promoter of the Klotho gene may be associated with essential hypertension in the Chinese Han population .

Example answer:
{"entities": [{"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "essential hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Association between an endoglin gene polymorphism and systemic sclerosis-related pulmonary arterial hypertension .

## Item biored:test:386
Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To date , the nature of the parasites remains unknown ; however , zoonoses could be incriminated .

Example answer:
{"entities": []}

Example input:
Sentence: Most carrier females have mild mental retardation and subtle facial changes .

Example answer:
{"entities": [{"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Whereas female patients had a higher predisposition to erysipelas , male patients were prone to having a facial localization of the infection .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "erysipelas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The neurologic evaluation revealed loss of sensation in the saddle area and medial aspect of her right leg .

Example answer:
{"entities": [{"text": "loss of sensation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She had profound insulin resistance , diabetes , severe hypertriglyceridemia and relapsing pancreatitis , while her pre-pubescent daughter had normal fat distribution but elevated plasma triglycerides and C-peptide and depressed high-density lipoprotein cholesterol .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertriglyceridemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}, {"text": "high-density lipoprotein cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The mutation was identified in a 22-year-old French woman coming to medical attention because of an increasing overweight .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "overweight", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: She was unable to urinate .

Example answer:
{"entities": []}

Example input:
Sentence: Three hours later , she complained of perineal numbness and lower extremity weakness .

Example answer:
{"entities": [{"text": "numbness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lower extremity weakness", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: She complained of seeing parasites and the larvae of fleas in her stools .

## Item biored:test:384
Example input:
Sentence: Thus , immunosuppression has increased the risk of infections by HPVs , predominantly epidermodysplasia verruciformis , speculated to play a role in skin cancer development .

Example answer:
{"entities": [{"text": "infections", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HPVs", "type": "OrganismTaxon"}, {"text": "epidermodysplasia verruciformis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although only limited subjects were investigated , our results suggested that a genetic polymorphism in ABCG2 might alter the transport activity for the drug and elevate the systemic circulation level of irinotecan , leading to severe myelosuppression .

Example answer:
{"entities": [{"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "irinotecan", "type": "ChemicalEntity"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , utilizing IFN-g-yellow fluorescent protein ( YFP ) and IL-10-GFP dual reporter mice , we show that primary malaria infection-induced CD4 ( + ) YFP ( + ) GFP ( + ) T cells have limited memory potential , do not stably express IL-10 , and are disproportionately lost from the Ag-experienced CD4 ( + ) T cell memory population during the maintenance phase postinfection .

Example answer:
{"entities": [{"text": "IFN-g-yellow", "type": "GeneOrGeneProduct"}, {"text": "IL-10-GFP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "malaria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rhabdomyolysis in a hepatitis C virus infected patient treated with telaprevir and simvastatin .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hepatitis C virus infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "telaprevir", "type": "ChemicalEntity"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Viruses were evaluated for replication in SCID mice transplanted with human hepatoma cells ( SCID-HuH-7 mice ) , in mosquitoes , and in rhesus monkeys .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hepatoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCID-HuH-7", "type": "CellLine"}, {"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: One month after starting the antiviral therapy , the patient was admitted to the hospital because he developed rhabdomyolysis .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "rhabdomyolysis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 46-year old man with a chronic hepatitis C virus infection received triple therapy with ribavirin , pegylated interferon and telaprevir .

Example answer:
{"entities": [{"text": "man", "type": "OrganismTaxon"}, {"text": "hepatitis C virus infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ribavirin", "type": "ChemicalEntity"}, {"text": "pegylated interferon", "type": "ChemicalEntity"}, {"text": "telaprevir", "type": "ChemicalEntity"}]}

Example input:
Sentence: Because human immunodeficiency virus type 1 ( HIV-1 ) Tat protein causes depressive-like behavior in mice , we investigated its ability to activate IDO in organotypic hippocampal slice cultures ( OHSCs ) derived from neonatal C57BL/6 mice .

Example answer:
{"entities": [{"text": "human immunodeficiency virus type 1", "type": "OrganismTaxon"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "depressive-like", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "paclitaxel", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Input:
Sentence: To the best of our knowledge , no cases of psychogenic parasitosis occurring during interferon therapy have been described in the literature .

## Item biored:test:336
Example input:
Sentence: We screened affected family members for homozygosity at short-tandem repeats flanking known autosomal recessive ( DFNB ) deafness loci , followed by TMC1 sequence analysis in families segregating deafness linked to DFNB7/B11 .

Example answer:
{"entities": [{"text": "autosomal recessive ( DFNB ) deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Overall , 9 different TMC1 mutations account for deafness in 19 ( 3.4 % ) of the 557 Pakistani families .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We previously reported that mutations of transmembrane channel-like gene 1 ( TMC1 ) cause non-syndromic recessive deafness at the DFNB7/B11 locus on chromosome 9q13-q21 in nine Pakistani families .

Example answer:
{"entities": [{"text": "transmembrane channel-like gene 1", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "non-syndromic recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DFNB7/B11", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We identified 10 new families segregating DFNB7/B11 deafness and TMC1 mutations , including three novel alleles .

Example answer:
{"entities": [{"text": "DFNB7/B11 deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We also detected p.R34X among normal control samples of African-American and northern European origins , raising the possibility that p.R34X and other mutations of TMC1 are prevalent contributors to the genetic load of deafness across a variety of populations and continents .

Example answer:
{"entities": [{"text": "p.R34X", "type": "SequenceVariant"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This report describes a patient with mild language delay and mental retardation , who was found to have nonketotic hyperglycinemia following her presentation with acute encephalopathy and chorea shortly after initiation of valproate therapy .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "language delay", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nonketotic hyperglycinemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chorea", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproate", "type": "ChemicalEntity"}]}

Example input:
Sentence: A large proportion of non-syndromic autosomal recessive deafness ( NSARD ) in many populations is caused by variants of the GJB2 gene .

Example answer:
{"entities": [{"text": "non-syndromic autosomal recessive deafness", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NSARD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GJB2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The slower progression of hearing loss associated with p.D572H , in comparison with that caused by p.D572N , may reflect a correlation of DFNA36 phenotype with TMC1 genotype .

Example answer:
{"entities": [{"text": "hearing loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.D572H", "type": "SequenceVariant"}, {"text": "p.D572N", "type": "SequenceVariant"}, {"text": "DFNA36", "type": "GeneOrGeneProduct"}, {"text": "TMC1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Only two of the 13 Norrie-FEVR index cases had the full features of Norrie disease with deafness and mental retardation .

## Item biored:test:421
Example input:
Sentence: METHODS : Genomic DNA was extracted from peripheral blood and used for PCR amplification of the GJB2 gene .

Example answer:
{"entities": [{"text": "GJB2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA was extracted from blood and PSA/ARE promoter region amplified by PCR .

Example answer:
{"entities": [{"text": "PSA/ARE", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Genomic DNA was extracted from blood samples , and DNA fragments containing the site of polymorphism were amplified by PCR .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA extracted from peripheral blood was amplified by polymerase chain reaction ( PCR ) method and the exons of all candidate genes were sequenced .

Example answer:
{"entities": []}

Example input:
Sentence: After informed consent was obtained , genomic DNA was extracted from the venous blood of all participants .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was isolated from peripheral blood and genotyping was performed with PCR-based methods .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : DNA was extracted from peripheral blood and tumors of 54 RB patients and their relatives .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Peripheral blood samples were collected and genomic DNA was extracted from the leukocytes .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was extracted from whole blood samples collected with informed consent .

Example answer:
{"entities": []}

Input:
Sentence: Blood samples were collected for DNA extraction .

## Item biored:test:370
Example input:
Sentence: In conclusion , our findings reveal a potent protective role of BDNF against Dox-induced cardiotoxicity by activating Akt signalling , which may facilitate the safe use of Dox in cancer treatment .

Example answer:
{"entities": []}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Example input:
Sentence: The protective role of mangiferin was analyzed by triphenyl tetrazolium chloride ( TTC ) test used for macroscopic enzyme mapping assay of the ischemic myocardium .

Example answer:
{"entities": [{"text": "mangiferin", "type": "ChemicalEntity"}, {"text": "triphenyl tetrazolium chloride", "type": "ChemicalEntity"}, {"text": "TTC", "type": "ChemicalEntity"}, {"text": "ischemic myocardium", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Brain-derived neurotrophic factor attenuates doxorubicin-induced cardiac dysfunction through activating Akt signalling in rats .

Example answer:
{"entities": [{"text": "Brain-derived neurotrophic factor", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: Brain-derived neurotrophic factor significantly inhibited Dox-induced cardiomyocyte apoptosis , oxidative stress and cardiac dysfunction in rats .

Example answer:
{"entities": [{"text": "cardiac", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Doxorubicin toxicokinetics studies revealed no change in accumulation of doxorubicin and doxorubicinol ( toxic metabolite ) in the normal diet-fed ( ND ) and OB hearts .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicinol", "type": "ChemicalEntity"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subcutaneous injection of ISPH ( 200 mg/kg body weight in 1 ml saline ) to rats for 2 consecutive days caused myocardial damage in rat heart , which was determined by the increased activity of serum lactate dehydrogenase ( LDH ) and creatine phosphokinase isoenzymes ( CK-MB ) , increased uric acid level and reduced plasma iron binding capacity .

Example answer:
{"entities": [{"text": "ISPH", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "myocardial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "lactate dehydrogenase", "type": "GeneOrGeneProduct"}, {"text": "LDH", "type": "GeneOrGeneProduct"}, {"text": "creatine phosphokinase isoenzymes", "type": "GeneOrGeneProduct"}, {"text": "CK-MB", "type": "GeneOrGeneProduct"}, {"text": "uric acid", "type": "ChemicalEntity"}, {"text": "iron", "type": "ChemicalEntity"}]}

Example input:
Sentence: The clinical application of doxorubicin ( Dox ) is limited by its adverse effect of cardiotoxicity .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "Dox", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Assessment of a new non-invasive index of cardiac performance for detection of dobutamine-induced myocardial ischemia .

## Item biored:test:371
Example input:
Sentence: The cardiac toxicity intrinsically associated with the aggressive chemotherapy employed could function as a triggering factor for the arrhythmia in the predisposed myocardium of this patient .

Example answer:
{"entities": [{"text": "cardiac toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arrhythmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of this study is to show that FPD from MEA ( Multielectrode array ) of hiPS-CMs can detect QT prolongation induced by multichannel blockers .

Example answer:
{"entities": [{"text": "QT prolongation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clonidine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "ChemicalEntity"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "drowsiness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Field potential duration ( FPD ) in human-induced pluripotent stem cell-derived cardiomyocytes ( hiPS-CMs ) , which can express QT interval in an electrocardiogram , is reported to be a useful tool to predict K ( + ) channel and Ca ( 2+ ) channel blocker effects on QT interval .

Example answer:
{"entities": [{"text": "human-induced", "type": "OrganismTaxon"}, {"text": "K ( + ) channel and Ca ( 2+ ) channel blocker", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mechanistic studies revealed that OB rats are sensitized due to : ( 1 ) higher oxyradical stress leading to upregulation of uncoupling proteins 2 and 3 , ( 2 ) downregulation of cardiac peroxisome proliferators activated receptor-alpha , ( 3 ) decreased plasma adiponectin levels , ( 4 ) decreased cardiac fatty-acid oxidation ( 666.9+/-14.0 nmol/min/g heart in ND versus 400.2+/-11.8 nmol/min/g heart in OB ) , ( 5 ) decreased mitochondrial AMP-alpha2 protein kinase , and ( 6 ) 86 % drop in cardiac ATP levels accompanied by decreased ATP/ADP ratio after doxorubicin administration .

Example answer:
{"entities": [{"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "uncoupling proteins 2 and 3", "type": "GeneOrGeneProduct"}, {"text": "peroxisome proliferators activated receptor-alpha", "type": "GeneOrGeneProduct"}, {"text": "adiponectin", "type": "GeneOrGeneProduct"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "AMP-alpha2 protein kinase", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "ATP/ADP", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fatal carbamazepine induced fulminant eosinophilic ( hypersensitivity ) myocarditis : emphasis on anatomical and histological characteristics , mechanisms and genetics of drug hypersensitivity and differential diagnosis .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "ChemicalEntity"}, {"text": "hypersensitivity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocarditis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drug hypersensitivity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "epinephrine", "type": "ChemicalEntity"}, {"text": "myocardial stunning", "type": "DiseaseOrPhenotypicFeature"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report a case of 54-year-old woman with medical history of mitral valve prolapse and migraines , who was admitted to the hospital for substernal chest pain and electrocardiogram demonstrated 1/2 mm ST-segment elevation in leads II , III , aVF , V5 , and V6 and positive troponin I. Emergent coronary angiogram revealed normal coronary arteries with moderately reduced left ventricular ejection fraction with wall motion abnormalities consistent with TS .

Example answer:
{"entities": [{"text": "woman", "type": "OrganismTaxon"}, {"text": "mitral valve prolapse", "type": "DiseaseOrPhenotypicFeature"}, {"text": "migraines", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chest pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "motion abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The clinical application of doxorubicin ( Dox ) is limited by its adverse effect of cardiotoxicity .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "Dox", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND : Electrocardiography has a very low sensitivity in detecting dobutamine-induced myocardial ischemia .

## Item biored:test:376
Example input:
Sentence: In spontaneously hypertensive , stroke-prone rats , microinjection of methyldopa into the area of the midline B3 serotonin cell group in the ventral medulla caused a potent hypotension of 30-40 mm Hg , which was maximal 2-3 h after administration and was abolished by the serotonin neurotoxin 5,7-dihydroxytryptamine ( 5,7-DHT ) injected intracerebroventricularly .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke-prone", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5,7-dihydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5,7-DHT", "type": "ChemicalEntity"}]}

Example input:
Sentence: In these trials , Hp typing of 69 DM individuals and treating those with the Hp 2-2 with vitamin E prevented one myocardial infarct , stroke or cardiovascular death .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}, {"text": "myocardial infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiovascular death", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: After admission , the patient received a continuous intravenous infusion of 5-FU ( 1000 mg/day ) , during which precordial pain with right bundle branch block occurred concomitantly with a high serum FBAL concentration of 1955 ng/ml .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "right bundle branch block", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , there is convincing clinical evidence that monotherapy with continuous subcutaneous apomorphine infusions is associated with marked reductions of preexisting levodopa-induced dyskinesias .

Example answer:
{"entities": [{"text": "apomorphine", "type": "ChemicalEntity"}, {"text": "levodopa-induced", "type": "ChemicalEntity"}, {"text": "dyskinesias", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Isoproterenol alone decreased left ventricular systolic pressure and myocardial contractility indexed as LVdp/dtmax and LVdp/dtmin .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Further , 5,7-DHT lesion of serotonin nerves travelling in the median forebrain bundle , one of the main ascending pathways from the B3 serotonin cells , did not affect the fall in blood pressure associated with a midline B3 serotonin methyldopa injection .

Example answer:
{"entities": [{"text": "5,7-DHT", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "methyldopa", "type": "ChemicalEntity"}]}

Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Flow cytometry experiments confirmed that the transfectants ' diminished resistance to DOX was caused by increased drug accumulation induced by the exogenous Rab6c .

Example answer:
{"entities": [{"text": "DOX", "type": "ChemicalEntity"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The increase in dP/dtejc during infusion of dobutamine in this group was severely impaired as compared to the non-ischemic group .

## Item biored:test:423
Example input:
Sentence: Genomic DNA extracted from peripheral blood was amplified by polymerase chain reaction ( PCR ) method and the exons of all candidate genes were sequenced .

Example answer:
{"entities": []}

Example input:
Sentence: DNA was extracted from the blood drawn from 399 prostate cancer patients , 150 BPH patients and 294 healthy community controls .

Example answer:
{"entities": [{"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Peripheral blood samples were collected and genomic DNA was extracted from the leukocytes .

Example answer:
{"entities": []}

Example input:
Sentence: Genomic DNA of eastern Indian probands with DS ( N=132 ) , their parents ( N=209 ) and ethnically matched controls ( N=149 ) was subjected to PCR-based analyses of functionally important SNPs followed by statistical analyses .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : DNA obtained from leukocytes and tumor cells was amplified by polymerase chain reaction regarding five exons of PTCH1 and PTCH2 and neighboring microsatellites .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTCH1", "type": "GeneOrGeneProduct"}, {"text": "PTCH2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: EXPERIMENTAL DESIGN : Genomic DNA was purified from peripheral blood mononuclear cells or tissue specimens .

Example answer:
{"entities": []}

Example input:
Sentence: Germline DNA was extracted from paraffin-embedded unaffected lymph nodes .

Example answer:
{"entities": [{"text": "paraffin-embedded", "type": "ChemicalEntity"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Example input:
Sentence: Cheek swab samples were obtained for DNA analysis from 116 case/parent trios .

Example answer:
{"entities": []}

Example input:
Sentence: METHOD : Serum and DNA samples from the proband and his parents were analyzed .

Example answer:
{"entities": []}

Input:
Sentence: Additionally , samples of hair follicles and buccal cells from the mother of the proband were acquired for DNA extraction and molecular analysis .

## Item biored:test:355
Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Long-term oral galactose treatment prevents cognitive deficits in male Wistar rats treated intracerebroventricularly with streptozotocin .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "streptozotocin", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Short-term losartan treatment , besides antihypertensive effect , improved glomerular filtration rate and ameliorated glomerulosclerosis resulting in decreased proteinuria .

Example answer:
{"entities": [{"text": "losartan", "type": "ChemicalEntity"}, {"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Oral galactose exposure might have beneficial effects on learning and memory ability and could be worth investigating for improvement of cognitive deficits associated with glucose hypometabolism in AD .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose hypometabolism", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Prolonged treatment with losartan showed further reduction of glomerulosclerosis associated with reduced progression of tubular atrophy and interstitial fibrosis , thus preventing heavy proteinuria and chronic renal failure .

Example answer:
{"entities": [{"text": "losartan", "type": "ChemicalEntity"}, {"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have investigated the effects of continuous daily oral galactose ( 200 mg/kg/day ) treatment on cognitive deficits in streptozotocin-induced ( STZ-icv ) rat model of sAD , tested by Morris Water Maze and Passive Avoidance test , respectively .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}, {"text": "cognitive deficits", "type": "DiseaseOrPhenotypicFeature"}, {"text": "streptozotocin-induced", "type": "ChemicalEntity"}, {"text": "STZ-icv", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "sAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Amphetamine abuse was predictive of larger cranial to body growth ratios .

Example answer:
{"entities": [{"text": "Amphetamine", "type": "ChemicalEntity"}]}

Input:
Sentence: Supplementation with potassium and magnesium improved clinical symptoms and resulted in catch-up growth , but vision remained impaired .

## Item biored:test:367
Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the haplotype analysis , 1 haplotype carrying the variant allele from both +3100 T/G and +8365 C/T , with a population frequency of 3 % , was also significantly associated with decreased risk of prostate cancer ( p=0.036 , global simulated p-value=0.046 ) .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: When the patients were stratified by the SE , the rs729302 A allele was found to confer increased risk to RA in patients that were SE negative ( OR 1.50 , 95 % CI 1.17 to 1.92 , p = 0.001 ) as compared with patients carrying the SE ( OR 1.11 , 95 % CI 0.93 to 1.33 , p = 0.24 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Significant differences were detected in genotypic distribution ( p = 0.04 ) as well as the allelic frequency ( p = 0.003 ) between the SHCM patients and controls .

Example answer:
{"entities": [{"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: A statistically significant difference in allele frequency between cases and controls was observed for 2 of the SNPs ( +3100 T/G and +8365 C/T ) , with an odds ratio of 0.78 ( 95 % CI=0.64-0.96 ) and 0.65 ( 95 % CI=0.45-0.94 ) respectively .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: We concluded that the CASP8 -652 6N del variant allele may contribute to the risk of developing SCCHN in non-Hispanic white populations .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CASP8 -652 6N del variant genotypes or haplotypes were inversely associated with SCCHN risk ( adjusted OR , 0.70 ; 95 % CI , 0.57-0.85 for the ins/del + del/del genotypes compared with the ins/ins genotype ; adjusted OR , 0.73 ; 95 % CI , 0.55-0.97 for the del-D haplotype compared with the ins-D haplotype ) .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: We observed a significant lower frequency of 6bINS allele in SSc patients with associated PAH compared with controls [ 10.3 vs 23.9 % , P = 0.01 ; odds ratio ( OR ) 0.37 , 95 % confidence interval ( CI ) 0.15-0.89 ] , and a trend in comparison with SSc patients without PAH ( 10.3 vs 20.3 % , P = 0.05 ; OR : 0.45 , 95 % CI : 0.19-1.08 ) .

## Item biored:test:338
Example input:
Sentence: OBJECTIVE : We aimed to determine whether a common , recently discovered deletion polymorphism in the DHFR gene is a risk factor for preterm delivery or low birth weight .

Example answer:
{"entities": [{"text": "DHFR", "type": "GeneOrGeneProduct"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: An intronic SNP , rs2622604 , in ABCG2 showed P ( Fisher ) =0.0419 in the second stage and indicated a significant association with severe myelosuppression in the combined study ( P ( Fisher ) =0.000237 ; P ( Corrected ) =0.036 ) .

Example answer:
{"entities": [{"text": "rs2622604", "type": "SequenceVariant"}, {"text": "ABCG2", "type": "GeneOrGeneProduct"}, {"text": "myelosuppression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Women with both a DHFR deletion allele and low folate intake ( < 400 microg/d from diet plus supplements ) had a significantly greater risk of preterm delivery ( AOR : 5.5 ; 95 % CI : 1.5 , 20.4 ; P = 0.01 ) and a significantly greater risk of having an infant with a low birth weight ( AOR : 8.3 ; 95 % CI : 1.8 , 38.6 ; P = 0.01 ) than did women without a deletion allele and with a folate intake > /=400 microg/d .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "DHFR", "type": "GeneOrGeneProduct"}, {"text": "folate", "type": "ChemicalEntity"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: A two base pair deletion in the PQBP1 gene is associated with microphthalmia , microcephaly , and mental retardation .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mental retardation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The Typically Deleted Region in the 22q11.21 subband ( here called TDR22 ) is very gene-dense , and the extent of the deletion has been defined precisely in several studies .

Example answer:
{"entities": []}

Example input:
Sentence: An RT-PCR fragment retaining 43 bp of intron 8 was consistently detected suggesting that the 33-bp genomic deletion had elicited NMD .

Example answer:
{"entities": [{"text": "33-bp genomic deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We used high-resolution karyotyping to confirm a deletion ( 10-12Mb ) [ del ( 1 ) ( p31.2p32.3 ) ] and found no structural abnormalities in the father , suggesting a de novo event .

Example answer:
{"entities": [{"text": "deletion ( 10-12Mb )", "type": "SequenceVariant"}, {"text": "del ( 1 ) ( p31.2p32.3 )", "type": "SequenceVariant"}]}

Example input:
Sentence: All affected children were homozygous for a four-basepair deletion in exon 3 , which created a premature translational stop codon .

Example answer:
{"entities": [{"text": "four-basepair deletion", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Women with a deletion allele had a significantly greater risk of preterm delivery [ adjusted odds ratio ( AOR ) : 3.0 ; 95 % CI : 1.0 , 8.8 ; P < 0.05 ] than did those without a deletion allele .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "preterm delivery", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A deletion within the non-coding region was associated with only mild-regressed ROP , despite the presence of low birthweight , prematurity and exposure to oxygen .

## Item biored:test:424
Example input:
Sentence: MATERIALS AND METHODS : The patients were examined using standard ophthalmic techniques .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: PURPOSE : To report the clinical , ophthalmic , and genetic characteristics for lattice corneal dystrophy type I ( LCDI ) in a Chilean family .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCDI", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : To identify mutations in the TGFBI gene in Indian patients with lattice corneal dystrophy ( LCD ) or granular corneal dystrophy ( GCD ) and to look for genotype-phenotype correlations .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "lattice corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "granular corneal dystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: His apoE phenotype was apoE3/2 and he had mild dyslipidemia with a mid-band on polyacrylamide gel electrophoresis .

Example answer:
{"entities": [{"text": "apoE", "type": "GeneOrGeneProduct"}, {"text": "apoE3/2", "type": "GeneOrGeneProduct"}, {"text": "dyslipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "polyacrylamide", "type": "ChemicalEntity"}]}

Example input:
Sentence: In addition , eight individuals who had both microcoria and glaucoma were screened for glaucoma genes : myocilin ( MYOC ) , optineurin ( OPTN ) and CYP1B1 .

Example answer:
{"entities": [{"text": "microcoria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocilin", "type": "GeneOrGeneProduct"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "optineurin", "type": "GeneOrGeneProduct"}, {"text": "OPTN", "type": "GeneOrGeneProduct"}, {"text": "CYP1B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CDSRR phenotype was associated with reduced visual acuity of variable degree and color vision defects .

Example answer:
{"entities": [{"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "color vision defects", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Our findings further confirmed that different kind of mutations might cause different ocular phenotype , and clearly clinical phenotype classification might increase the mutation detection rate of the PAX6 gene .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Six affected family members were examined clinically including visual acuity , color cornea photography , applanation tonography , and fundoscopy .

Example answer:
{"entities": []}

Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Phenotype was characterized with routine ophthalmic examination , Goldmann perimetry , electroretinography , and color fundus photography .

## Item biored:test:429
Example input:
Sentence: The D2267 residue is predicted to coordinate binding of a calcium ion , which influences the conformational binding loops of the C-type lectin domain that mediate interactions with tenascins and other extracellular-matrix proteins .

Example answer:
{"entities": [{"text": "D2267", "type": "SequenceVariant"}, {"text": "calcium", "type": "ChemicalEntity"}]}

Example input:
Sentence: We identified two silent and one missense ( Pro75 Ala ) variant .

Example answer:
{"entities": [{"text": "Ala )", "type": "SequenceVariant"}]}

Example input:
Sentence: Optimal control of the absences was achieved with sodium valproate , lamotrigine , or ethosuximide alone or in combination .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "ChemicalEntity"}, {"text": "lamotrigine", "type": "ChemicalEntity"}, {"text": "ethosuximide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Structure-function studies and in silico analyses provided the first experimental evidence of an indel of a stop codon by alternative splicing at a NAGNAG acceptor site .

Example answer:
{"entities": []}

Example input:
Sentence: Clinical evaluation included the use of the Unified Parkinson 's Disease Rating Scale ( UPDRS ) , Hoehn_Yahr score and Schwab England activities of daily living ( ADL ) score in 'on'- and 'off'-drug conditions before surgery and 6 months after surgery .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: L-asparaginase is a critical chemotherapeutic agent for acute lymphoblastic leukemia ( ALL ) .

Example answer:
{"entities": [{"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "acute lymphoblastic leukemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: LIF , secreted from the endometrial glands ( GEs ) , binds to the LIFR , activating the Janus kinase-signal transducer and activation of transcription ( STAT ) 3 ( Jak-Stat3 ) signaling pathway in the LE .

Example answer:
{"entities": [{"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "LIFR", "type": "GeneOrGeneProduct"}, {"text": "Janus", "type": "GeneOrGeneProduct"}, {"text": "transducer and activation of transcription ( STAT ) 3", "type": "GeneOrGeneProduct"}, {"text": "Jak-Stat3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : The authors obtained a significant maximum parametric LOD ( logarithm of odds ) score of Z ( max ) = 3.72 on chromosome 8q22 and identified a homozygous missense mutation in the gene MKS3/TMEM67 .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Homozygous mutations in PLCE1 ( also known as KIAA1516 , PLCE , or NPHS3 ) were identified following genome-wide mapping of single-nucleotide polymorphisms .

Example answer:
{"entities": [{"text": "PLCE1", "type": "GeneOrGeneProduct"}, {"text": "KIAA1516", "type": "GeneOrGeneProduct"}, {"text": "PLCE", "type": "GeneOrGeneProduct"}, {"text": "NPHS3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: FLSs proliferation was detected by BrdU incorporation .

Example answer:
{"entities": []}

Input:
Sentence: ( c ) 2007 Wiley-Liss , Inc .

## Item biored:test:348
Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Mild glycine encephalopathy ( NKH ) in a large kindred due to a silent exonic GLDC splice mutation .

Example answer:
{"entities": [{"text": "glycine encephalopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NKH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We also found that the c.463-6T > G mutation leads to aberrant mRNA splicing , but no stable truncated protein was detected in the corresponding patient-derived fibroblasts .

Example answer:
{"entities": [{"text": "c.463-6T > G", "type": "SequenceVariant"}, {"text": "patient-derived", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mutations in N-acetylglucosamine ( O-GlcNAc ) transferase in patients with X-linked intellectual disability .

Example answer:
{"entities": [{"text": "N-acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutation of the a-tubulin isotype TUBA1A is associated with cortical malformations in humans .

Example answer:
{"entities": [{"text": "a-tubulin", "type": "GeneOrGeneProduct"}, {"text": "TUBA1A", "type": "GeneOrGeneProduct"}, {"text": "cortical malformations", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Minigene assays demonstrated that the 13-nucleotide repeat and 4 bp deletion within the same haplotype of intron 8 could regulate alternative splicing .

Example answer:
{"entities": []}

Example input:
Sentence: Notably , the same mutation is associated with the Hamel cerebropalatocardiac syndrome , another form of S-XLMR .

Example answer:
{"entities": [{"text": "Hamel cerebropalatocardiac syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: A novel splicing mutation in SLC12A3 associated with Gitelman syndrome and idiopathic intracranial hypertension .

## Item biored:test:390
Example input:
Sentence: AIMS : This study sought to assess the risk of developing coronary artery disease ( CAD ) associated with initial treatment of type 2 diabetes with different sulphonylureas .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sulphonylureas", "type": "ChemicalEntity"}]}

Example input:
Sentence: To evaluate amikacin-associated nephrotoxicity in an adult hematology/oncology population , a prospective , randomized , open-label trial was conducted at a university-affiliated medical center .

Example answer:
{"entities": [{"text": "amikacin-associated", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MATERIALS AND METHODS : Our study included patients who were administered 30-60 mL of iodinated contrast agent for percutaneous coronary angiography ( PCAG ) , all with creatinine values between 1.1 and 3.1 mg/dL .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "contrast", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Reduced progression of adriamycin nephropathy in spontaneously hypertensive rats treated by losartan .

Example answer:
{"entities": [{"text": "adriamycin", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "losartan", "type": "ChemicalEntity"}]}

Example input:
Sentence: Doxorubicin-induced nephropathy leads to epithelial sodium channel ( ENaC ) -dependent volume retention and renal fibrosis .

Example answer:
{"entities": [{"text": "Doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sodium", "type": "ChemicalEntity"}, {"text": "volume retention", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : The aim of the study was to investigate the antihypertensive effects of angiotensin II type-1 receptor blocker , losartan , and its potential in slowing down renal disease progression in spontaneously hypertensive rats ( SHR ) with adriamycin ( ADR ) nephropathy .

Example answer:
{"entities": [{"text": "angiotensin II type-1 receptor", "type": "GeneOrGeneProduct"}, {"text": "losartan", "type": "ChemicalEntity"}, {"text": "renal disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "adriamycin", "type": "ChemicalEntity"}, {"text": "ADR", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Atorvastatin protects against contrast-induced nephropathy via anti-apoptosis by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "Atorvastatin", "type": "ChemicalEntity"}, {"text": "contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Among a total of 60 patients included in the study , 16 patients developed acute renal failure ( ARF ) on the second day after contrast material was injected ( 26.6 % ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: Contrast-induced nephropathy ( CIN ) is an iatrogenic acute renal failure occurring following the intravascular injection of iodinated radiographic contrast medium .

Example answer:
{"entities": [{"text": "Contrast-induced nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: INTRODUCTION AND OBJECTIVE : Contrast-induced nephropathy ( CIN ) significantly increases the morbidity and mortality of patients .

Example answer:
{"entities": [{"text": "Contrast-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Cardiac Angiography in Renally Impaired Patients ( CARE ) study : a randomized double-blind trial of contrast-induced nephropathy in patients with chronic kidney disease .

## Item biored:test:393
Example input:
Sentence: Nine days later the patient 's creatine kinase had dropped to 1695 U/L and creatinine was 3.3 mg/dL .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: However , an increase of serum creatinine at various times postoperatively is more predictive of the development of CRF or ESRD .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fourteen days after hospitalization , creatine kinase level had returned to 230 IU/L and the patient was discharged .

Example answer:
{"entities": [{"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: All of the patients ' plasma blood urea nitrogen ( BUN ) and creatinine levels were measured on the second and seventh day after the administration of intravenous contrast material .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "BUN", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Urinary volume and serum creatinine levels recovered to the normal range , with urinary protein disappearing completely within 40 days .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Serum creatinine ( SCr ) levels and estimated glomerular filtration rate were assessed at baseline and 2 to 5 days after receiving medications .

## Item biored:test:399
Example input:
Sentence: Patients with dyskinesia had lower onset age ( p < 0.001 ) , longer duration of levodopa therapy ( p < 0.001 ) , longer disease duration ( p < 0.001 ) , higher total daily levodopa dose ( p < 0.001 ) , and higher total UPDRS scores ( p = 0.005 ) than patients without dyskinesia .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "levodopa", "type": "ChemicalEntity"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Fasting serum insulin concentrations differed among groups ( F ( 33 ) = 3.35 ; P = .047 ) ( clozapine > olanzapine > risperidone ) with significant differences between clozapine and risperidone ( t ( 33 ) = 2.32 ; P = .03 ) and olanzapine and risperidone ( t ( 33 ) = 2.15 ; P = .04 ) .

Example answer:
{"entities": [{"text": "insulin", "type": "ChemicalEntity"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In mutant type group , resistin ( 4.15 1.7 ng/ml vs. 3.90 2.1 ng/ml : P < 0.05 ) , leptin ( 78.4 69 ng/ml vs 66.2 32 ng/ml : P < 0.05 ) and IL-6 ( 1.40 1.9 pg/ml vs 0.81 1.5 pg/ml : P < 0.05 ) levels decreased after dietary treatment .

Example answer:
{"entities": [{"text": "resistin", "type": "GeneOrGeneProduct"}, {"text": "leptin", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The homeostasis model assessment of insulin resistance also differed significantly among groups ( F ( 33 ) = 4.92 ; P = .01 ) ( clozapine > olanzapine > risperidone ) ( clozapine vs risperidone , t ( 33 ) = 2.94 ; P = .006 ; olanzapine vs risperidone , t ( 33 ) = 2.42 ; P = .02 ) .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

## Item biored:test:408
Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : We observed that genes of the metallothionein-1 ( MT1 ) family are induced in the HCC cell line Huh7 exposed to sorafenib .

Example answer:
{"entities": [{"text": "metallothionein-1", "type": "GeneOrGeneProduct"}, {"text": "MT1", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Huh7", "type": "CellLine"}, {"text": "sorafenib", "type": "ChemicalEntity"}]}

Example input:
Sentence: We hypothesized that Thra1 ( PV/+ ) mice could be used to predict the skeletal outcome of human THRA mutations and determine whether prolonged treatment with a supraphysiological dose of T4 ameliorates the skeletal abnormalities .

Example answer:
{"entities": [{"text": "Thra1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "THRA", "type": "GeneOrGeneProduct"}, {"text": "T4", "type": "ChemicalEntity"}, {"text": "skeletal abnormalities", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thra1 ( PV/+ ) mice express a similar potent dominant-negative mutant TRa1 to affected individuals , and thus represent an excellent disease model .

Example answer:
{"entities": [{"text": "Thra1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "TRa1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS AND FINDINGS : Cord blood mononuclear cells ( CBMCs ) of 200 neonates were genotyped for two TBX21 and three HLX1 SNPs .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Collectively , these findings reveal a role for CSF-1 in mediating the IL-3 hematopoietic pathway through monopoiesis , which regulates expansion of CD11c+ macrophages .

Example answer:
{"entities": [{"text": "CSF-1", "type": "GeneOrGeneProduct"}, {"text": "IL-3", "type": "GeneOrGeneProduct"}, {"text": "CD11c+", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whole cell recordings from non-transfected HEK cells and cells expressing human TRPV6 revealed the presence of a basal inward current in both types of cells when the internal solution contained 0.1 mm EGTA and 100 nm ( i ) or if the cytosolic Ca ( 2+ ) buffering remained undisturbed in perforated patch-clamp experiments .

Example answer:
{"entities": [{"text": "HEK", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "TRPV6", "type": "GeneOrGeneProduct"}, {"text": "EGTA", "type": "ChemicalEntity"}, {"text": "Ca ( 2+ )", "type": "ChemicalEntity"}]}

Example input:
Sentence: TSPO was up-regulated in Iba1 ( + ) cells from brains of patients with ICH and in CD11b ( + ) CD45 ( int ) cells from mice subjected to collagenase-induced ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "Iba1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD11b", "type": "GeneOrGeneProduct"}, {"text": "CD45", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "collagenase-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We have utilized the human monocyte cell line , THP-1 as a model to address this question .

## Item biored:test:414
Example input:
Sentence: Recent studies found that TIPE2 was involved in cancer development .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: RESULTS : Increased CCR2 was observed in the hippocampus after SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SOX2 and NANOG expression did not change following ETO treatment suggesting a dissociation of OCT4A from its pluripotency function .

Example answer:
{"entities": [{"text": "SOX2", "type": "GeneOrGeneProduct"}, {"text": "NANOG", "type": "GeneOrGeneProduct"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sepsis increased CAT1 , LAT2 and SNAT2 mRNA content two- to fourfold , but only the protein content for CAT1 ( 20 % decrease ) differed significantly .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CAT1", "type": "GeneOrGeneProduct"}, {"text": "LAT2", "type": "GeneOrGeneProduct"}, {"text": "SNAT2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , bupivacaine significantly increased COX-2 gene expression at 48 h as compared with the lidocaine/placebo group .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "lidocaine/placebo", "type": "ChemicalEntity"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Increased numbers of neurons that expressed CCR2 was observed following SE .

Example answer:
{"entities": [{"text": "CCR2", "type": "GeneOrGeneProduct"}, {"text": "SE", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Treatment with E2 , however , failed to prevent these increases at the mRNA level .

## Item biored:test:388
Example input:
Sentence: The most relevant adverse event was peripheral neuropathy , which occurred in 78 % of the patients ( grade II , 38 % ; grade III , 21 % ) and led to treatment discontinuation in 6 % .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: Follow-up MRIs were performed on 5 patients from third to 14th days after discontinuation of metronidazole administration .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "metronidazole", "type": "ChemicalEntity"}]}

Example input:
Sentence: Finally , the IKr blockers , Terfenadine and Citalopram , which are reported to cause Torsade de Pointes ( TdP ) in clinical practice , produced early afterdepolarization ( EAD ) .

Example answer:
{"entities": [{"text": "Terfenadine", "type": "ChemicalEntity"}, {"text": "Citalopram", "type": "ChemicalEntity"}, {"text": "Torsade de Pointes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TdP", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fourteen days after hospitalization , creatine kinase level had returned to 230 IU/L and the patient was discharged .

Example answer:
{"entities": [{"text": "creatine kinase", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Plasma and liver 15-F ( 2t ) -IsoP were elevated and reached a plateau after day 2 of VPA treatment compared to control .

Example answer:
{"entities": [{"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}, {"text": "VPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: The cumulative discontinuation rate due to GI AEs was significantly lower with etoricoxib than diclofenac ( 5.2 vs 8.5 events per 100 patient-years , respectively ; hazard ratio 0.62 ( 95 % CI : 0.47 , 0.81 ; p < or=0.001 ) ) .

Example answer:
{"entities": [{"text": "GI AEs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "etoricoxib", "type": "ChemicalEntity"}, {"text": "diclofenac", "type": "ChemicalEntity"}, {"text": "patient-years", "type": "OrganismTaxon"}]}

Example input:
Sentence: We briefly describe two patients suffering from recent-onset atrial fibrillation , who experienced an acute devastating low back pain a few minutes after initiation of intravenous amiodarone loading .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "atrial fibrillation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "low back pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amiodarone", "type": "ChemicalEntity"}]}

Example input:
Sentence: At admission simvastatin and all antiviral drugs were discontinued because toxicity due to a drug-drug interaction was suspected .

Example answer:
{"entities": [{"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "antiviral drugs", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both the precordial pain and the electrocardiographic changes disappeared spontaneously after the discontinuation of 5-FU .

Example answer:
{"entities": [{"text": "precordial pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5-FU", "type": "ChemicalEntity"}]}

Input:
Sentence: All the complaints disappeared after stopping pegylated interferon alpha-2b and reappeared after restarting it .

## Item biored:test:391
Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: Among a total of 60 patients included in the study , 16 patients developed acute renal failure ( ARF ) on the second day after contrast material was injected ( 26.6 % ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "acute renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "contrast", "type": "ChemicalEntity"}]}

Example input:
Sentence: The observed effect of NIMO may have been attributable to the preservation of calcium homeostasis during hypotension , because there were no differences in the PbtO ( 2 ) indices among groups .

Example answer:
{"entities": [{"text": "NIMO", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : There was no significant difference between isotonic sodium chloride , sodium bicarbonate and isotonic sodium chloride with diltiazem application in prevention of CIN .

Example answer:
{"entities": [{"text": "sodium chloride", "type": "ChemicalEntity"}, {"text": "sodium bicarbonate", "type": "ChemicalEntity"}, {"text": "diltiazem", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study is to investigate and compare the protective effects of isotonic sodium chloride with sodium bicarbonate infusion and isotonic sodium chloride infusion with diltiazem , a calcium channel blocker , in preventing CIN .

Example answer:
{"entities": [{"text": "sodium chloride", "type": "ChemicalEntity"}, {"text": "sodium bicarbonate", "type": "ChemicalEntity"}, {"text": "diltiazem", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: MATERIALS AND METHODS : Our study included patients who were administered 30-60 mL of iodinated contrast agent for percutaneous coronary angiography ( PCAG ) , all with creatinine values between 1.1 and 3.1 mg/dL .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "contrast", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Example input:
Sentence: Comparison of effects of isotonic sodium chloride with diltiazem in prevention of contrast-induced nephropathy .

Example answer:
{"entities": [{"text": "sodium chloride", "type": "ChemicalEntity"}, {"text": "diltiazem", "type": "ChemicalEntity"}, {"text": "contrast-induced", "type": "ChemicalEntity"}, {"text": "nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND : No direct comparisons exist of the renal tolerability of the low-osmolality contrast medium iopamidol with that of the iso-osmolality contrast medium iodixanol in high-risk patients .

## Item biored:test:417
Example input:
Sentence: Among the family members , patients with the homozygous SLURP1 ( previously known as ARS component B ) mutation are prone to melanoma and viral infection , which might link to defective T-cell function as well as a derangement of epidermal homeostasis .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "melanoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "viral infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A patient of Chinese origin with ambiguous genitalia at 14 months , a 46 , XY karyotype , and normal T secretion under human chorionic gonadotropin ( hCG ) stimulation underwent a gonadectomy at 20 months .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "human chorionic gonadotropin", "type": "ChemicalEntity"}, {"text": "hCG", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report on two hemizygous mutations in OGT in individuals with X-linked intellectual disability ( XLID ) and dysmorphic features : one missense mutation ( p.Arg284Pro ) and one mutation leading to a splicing defect ( c.463-6T > G ) .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "XLID", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "c.463-6T > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Defects in these organelles cause inherited human disorders ( ciliopathies ) such as retinitis pigmentosa and Bardet-Biedl syndrome ( BBS ) , frequently affecting many physiological and developmental processes across multiple organs .

Example answer:
{"entities": [{"text": "inherited human disorders", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ciliopathies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinitis pigmentosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bardet-Biedl syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "BBS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutations in N-acetylglucosamine ( O-GlcNAc ) transferase in patients with X-linked intellectual disability .

Example answer:
{"entities": [{"text": "N-acetylglucosamine ( O-GlcNAc ) transferase", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "X-linked intellectual disability", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: X-linked mental retardation has been traditionally divided into syndromic ( S-XLMR ) and non-syndromic forms ( NS-XLMR ) , although the borderlines between these phenotypes begin to vanish and mutations in a single gene , for example PQBP1 , can cause S-XLMR as well as NS-XLMR .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PQBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutations of the steroid 5alpha-reductase type 2 ( SRD5A2 ) gene in 46 , XY subjects cause masculinization defects of varying degrees , due to reduced or impaired enzymatic activity .

Example answer:
{"entities": [{"text": "steroid 5alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We report here a new family with X-linked mental retardation due to mutation in OPHN1 and present unpublished data about two families previously reported , concerning the facial and psychological phenotype of affected males and carrier females .

Example answer:
{"entities": [{"text": "X-linked mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPHN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Somatic and gonadal mosaicism in X-linked retinitis pigmentosa .

## Item biored:test:422
Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A single nucleotide polymorphism at position 388 of the FGFR4 amino-acid sequence results in the substitution of glycine ( Gly ) with arginine ( Arg ) and higher frequency of the ArgArg genotype was previously found in prostate cancer patients .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}, {"text": "glycine ( Gly ) with arginine ( Arg )", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We screened germline mutations in the coding exons and the flanking intron sequences of the GATA4 gene in 486 CHD patients by denaturing high-performance liquid chromatography ( DHPLC ) , and confirmed the mutations by sequencing .

Example answer:
{"entities": [{"text": "GATA4", "type": "GeneOrGeneProduct"}, {"text": "CHD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To investigate the GSTP1 Ile105Val genotype frequency in prostate cancer cases in the Kashmiri population , we designed a case-control study , in which 50 prostate cancer cases and 45 benign prostate hyperplasia cases were studied for GSTP1 Ile105Val polymorphism , compared to 80 controls taken from the general population , employing the PCR-RFLP technique .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Haplotype analysis and mutational screening on the RPGR gene were performed .

## Item biored:test:404
Example input:
Sentence: Chronic pre-treatment with metformin reduces post-myocardial infarction cardiac dysfunction and suppresses inflammatory responses , possibly through inhibition of TLR4 activities .

Example answer:
{"entities": [{"text": "metformin", "type": "ChemicalEntity"}, {"text": "infarction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This cardioprotection is accompanied by decreased cardiac oxidative stress and triglycerides and increased cardiac fatty-acid oxidation , ATP synthesis , and upregulated JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "fatty-acid", "type": "ChemicalEntity"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: AIMS : This study sought to assess the risk of developing coronary artery disease ( CAD ) associated with initial treatment of type 2 diabetes with different sulphonylureas .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sulphonylureas", "type": "ChemicalEntity"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "hepatorenal syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prolonged PFS and OS were observed in patients achieving CR and receiving bort-dex a single line of prior therapy .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "bort-dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Patients who are more than 10 years post-OLTX have CRF and ESRD at a high rate .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She also had hypertension and premature pubarche , whereas dexamethasone effectively suppressed these clinical manifestations .

Example answer:
{"entities": [{"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSION : The rate of major hemorrhage was high in this old , frail group , but excluding fatalities , resulted in no long-term sequelae , and the stroke rate on warfarin was low , demonstrating how effective warfarin treatment is .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adverse cardiovascular effects occurred mainly , but not exclusively , in patients with concomitant risk factors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: These results suggest that , despite a known association with increased weight , long-term sulfonylurea therapy may reduce the risk of coronary heart disease .

Example answer:
{"entities": [{"text": "sulfonylurea", "type": "ChemicalEntity"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Many patients , however , develop negative long-term side effects such as premature atherosclerosis .

## Item biored:test:307
Example input:
Sentence: In collagenase-induced ICH mice , the protection of etifoxine was associated with reduced leukocyte infiltration into the brain and microglial production of IL-6 and TNF-a .

Example answer:
{"entities": [{"text": "collagenase-induced", "type": "ChemicalEntity"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "etifoxine", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid prevents mitochondrial damage and neurotoxicity in experimental chemotherapy neuropathy .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The study investigates if alpha-lipoic acid is neuroprotective against chemotherapy induced neurotoxicity , if mitochondrial damage plays a critical role in toxic neurodegenerative cascade , and if neuroprotective effects of alpha-lipoic acid depend on mitochondria protection .

Example answer:
{"entities": [{"text": "alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "toxic neurodegenerative cascade", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "MPTP", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "METH-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: In this study , we determined the impact of a TSPO ligand , etifoxine , on brain injury and inflammation in 2 mouse models of ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "etifoxine", "type": "ChemicalEntity"}, {"text": "brain injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alpha-lipoic acid exerts neuroprotective effects against chemotherapy induced neurotoxicity in sensory neurons : it rescues the mitochondrial toxicity and induces the expression of frataxin , an essential mitochondrial protein with anti-oxidant and chaperone properties .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mitochondrial toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "frataxin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This study examined the effect of alpha-tocopherol ( alpha-TC ) , a scavenger of reactive oxygen species , and deferoxamine ( DFO ) , an iron chelator , on the MA-induced neurotoxicity .

## Item biored:test:310
Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: and metrifonate ( 10 mg/kg , p.o. , respectively ) reversed memory deficits induced by scopolamine and TRP depletion ( 10 mg/kg , i.p. , and 3 mg/kg , p.o. , respectively ) .

Example answer:
{"entities": [{"text": "memory", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , these findings demonstrate that DA is not essential for the development of METH-induced dopaminergic neurotoxicity and suggest that mechanisms independent of DA warrant more intense investigation .

Example answer:
{"entities": [{"text": "DA", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rilmenidine", "type": "ChemicalEntity"}, {"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In aspartate , glutamine and glutamate levels detected a decrease of 5.21 % , 13.55 % and 21.80 % , respectively in mice hippocampus treated with GFC75 plus P400 when compared with seized mice .

Example answer:
{"entities": [{"text": "aspartate", "type": "ChemicalEntity"}, {"text": "glutamine", "type": "ChemicalEntity"}, {"text": "glutamate", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "GFC75", "type": "ChemicalEntity"}, {"text": "P400", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chronic T treatment significantly decreased 5-HT and 5-HIAA in certain brain areas , but to a much lesser extent than PCPA .

Example answer:
{"entities": [{"text": "T", "type": "ChemicalEntity"}, {"text": "5-HT", "type": "ChemicalEntity"}, {"text": "5-HIAA", "type": "ChemicalEntity"}, {"text": "PCPA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In spontaneously hypertensive , stroke-prone rats , microinjection of methyldopa into the area of the midline B3 serotonin cell group in the ventral medulla caused a potent hypotension of 30-40 mm Hg , which was maximal 2-3 h after administration and was abolished by the serotonin neurotoxin 5,7-dihydroxytryptamine ( 5,7-DHT ) injected intracerebroventricularly .

Example answer:
{"entities": [{"text": "hypertensive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "stroke-prone", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "methyldopa", "type": "ChemicalEntity"}, {"text": "serotonin", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5,7-dihydroxytryptamine", "type": "ChemicalEntity"}, {"text": "5,7-DHT", "type": "ChemicalEntity"}]}

Example input:
Sentence: It is widely believed that dopamine ( DA ) mediates methamphetamine ( METH ) -induced toxicity to brain dopaminergic neurons , because drugs that interfere with DA neurotransmission decrease toxicity , whereas drugs that increase DA neurotransmission enhance toxicity .

Example answer:
{"entities": [{"text": "dopamine", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "methamphetamine", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here we show that the recently reported ability of L-dihydroxyphenylalanine to reverse the protective effect of alpha-methyl-para-tyrosine on METH-induced DA neurotoxicity is also confounded by drug effects on body temperature .

Example answer:
{"entities": [{"text": "L-dihydroxyphenylalanine", "type": "ChemicalEntity"}, {"text": "alpha-methyl-para-tyrosine", "type": "ChemicalEntity"}, {"text": "METH-induced", "type": "ChemicalEntity"}, {"text": "DA", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "a reduced locomotor activity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The concentrations of dopamine ( DA ) , serotonin and their metabolites decreased significantly after MA administration , which was inhibited by the alpha-TC and DFO pretreatment .

## Item biored:test:368
Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Seven SNPs in CFH and two SNPs in C2 , CFB ' , and C3 were genotyped using the ABI SNaPshot method .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Genetic analysis identified a novel V876E mutation in all HypoPP patients in the family , but not in normal family members or 160 control people .

Example answer:
{"entities": [{"text": "V876E", "type": "SequenceVariant"}, {"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: C_6+/6+ and G_6+/6+ combined genotypes were respectively associated to the best and worst PFS ( P=0.03 when compared with each other ) , while combinations carrying the allele 6- determined an intermediate evolution that might be indicative of a variable response to chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: Additionally , when PSA genotype was cross classified with CAG repeat , significantly more cases than both BPH and population controls were observed to have a short ( < 22 ) CAG/GG genotype ( P = 0.006 ) .

Example answer:
{"entities": [{"text": "PSA", "type": "GeneOrGeneProduct"}, {"text": "CAG repeat", "type": "SequenceVariant"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The minor allele of SNP rs6232 was additionally associated with 15 % higher OGTT-derived and 19 % higher clamp-derived insulin sensitivity ( pdom < or= 0.0047 ) , 4.5 % lower HOMAIR ( pdom = 0.02 ) and 3.5 % lower 120-min glucose ( pdom = 0.0003 ) independently of BMI and proinsulin conversion .

Example answer:
{"entities": [{"text": "rs6232", "type": "SequenceVariant"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "proinsulin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The CASP8 -652 6N del variant genotypes or haplotypes were inversely associated with SCCHN risk ( adjusted OR , 0.70 ; 95 % CI , 0.57-0.85 for the ins/del + del/del genotypes compared with the ins/ins genotype ; adjusted OR , 0.73 ; 95 % CI , 0.55-0.97 for the del-D haplotype compared with the ins-D haplotype ) .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We concluded that the CASP8 -652 6N del variant allele may contribute to the risk of developing SCCHN in non-Hispanic white populations .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Genotypes carrying allele 6bINS were also less frequent in SSc patients with PAH than in controls ( 20.7 vs 42.9 % , P = 0.02 ) .

## Item biored:test:392
Example input:
Sentence: AIMS : This study sought to assess the risk of developing coronary artery disease ( CAD ) associated with initial treatment of type 2 diabetes with different sulphonylureas .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sulphonylureas", "type": "ChemicalEntity"}]}

Example input:
Sentence: Salidroside Ameliorates Renal Interstitial Fibrosis by Inhibiting the TLR4/NF-kappaB and MAPK Signaling Pathways .

Example answer:
{"entities": [{"text": "Salidroside", "type": "ChemicalEntity"}, {"text": "Renal Interstitial Fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4/NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "ChemicalEntity"}, {"text": "amiodarone", "type": "ChemicalEntity"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "human immunodeficiency virus", "type": "OrganismTaxon"}]}

Example input:
Sentence: This retrospective study examines the incidence and treatment of ESRD and chronic renal failure ( CRF ) in OLTX patients .

Example answer:
{"entities": [{"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chronic renal failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Short-term losartan treatment , besides antihypertensive effect , improved glomerular filtration rate and ameliorated glomerulosclerosis resulting in decreased proteinuria .

Example answer:
{"entities": [{"text": "losartan", "type": "ChemicalEntity"}, {"text": "glomerulosclerosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: MATERIALS AND METHODS : Our study included patients who were administered 30-60 mL of iodinated contrast agent for percutaneous coronary angiography ( PCAG ) , all with creatinine values between 1.1 and 3.1 mg/dL .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "contrast", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}]}

Input:
Sentence: METHODS AND RESULTS : The present study is a multicenter , randomized , double-blind comparison of iopamidol and iodixanol in patients with chronic kidney disease ( estimated glomerular filtration rate , 20 to 59 mL/min ) who underwent cardiac angiography or percutaneous coronary interventions .

## Item biored:test:445
Example input:
Sentence: p38 MAPK phosphorylation was analyzed by western blot .

Example answer:
{"entities": [{"text": "p38 MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The surface expression of GPIbalpha was practically undetectable by flow-cytometry and western blot in the patient and was reduced in the father .

Example answer:
{"entities": [{"text": "GPIbalpha", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: The expression of the Msx2 gene and phosphorylated-Smad1/5/8 , possible readouts of Bmp signaling , was also increased in the mutants .

Example answer:
{"entities": [{"text": "Msx2", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: GLDC expression in lymphoblasts was studied by Northern blot and reverse transcriptase PCR analysis .

Example answer:
{"entities": [{"text": "GLDC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemistry and western blotting are used to determine the mechanisms of Sal against RIF .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "RIF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Co-transfection experiment of both wild-type and mutant plasmids indicated the dominant-negative mechanism of disease development ; as more of mutant DNA was transfected , VWF secretion was impaired in the media , whereas more of VWF was stored in the cell lysates .

Example answer:
{"entities": [{"text": "VWF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The 293T cells transfected with the full-coding cDNA inserted in the expression vector produced a new 80 kDa protein , as detected by Western blot .

Example answer:
{"entities": [{"text": "293T", "type": "CellLine"}]}

Example input:
Sentence: Western blot analysis and reverse transcription-polymerase chain reaction were used to detect target gene and protein expression .

Example answer:
{"entities": []}

Input:
Sentence: The greater gene expression was also supported by Western blotting .

## Item biored:test:328
Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: Anticipation in familial lattice corneal dystrophy type I with R124C mutation in the TGFBI ( BIGH3 ) gene .

Example answer:
{"entities": [{"text": "lattice corneal dystrophy type I", "type": "DiseaseOrPhenotypicFeature"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "BIGH3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Endothelial NADPH oxidase 4 mediates vascular endothelial growth factor receptor 2-induced intravitreal neovascularization in a rat model of retinopathy of prematurity .

Example answer:
{"entities": [{"text": "NADPH oxidase 4", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor receptor", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The molecular basis of FDH involves mutations in the PORCN gene , which encodes an enzyme that allows membrane targeting and secretion of several Wnt proteins critical for normal tissue development .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Identification of this new de novo nonsense mutation confirms the diagnosis of FDH in this child and highlights the clinical importance of PORCN and Wnt signalling pathways in embryogenesis .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PORCN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A missense mutation in BCOR was described in a family with Lenz microphthalmia syndrome , a phenotype showing substantial overlapping features with that described in the two cousins .

Example answer:
{"entities": [{"text": "BCOR", "type": "GeneOrGeneProduct"}, {"text": "Lenz microphthalmia syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: NPHP can be associated with retinal degeneration ( Senior-Loken syndrome ) , brainstem and cerebellar anomalies ( Joubert syndrome ) , or liver fibrosis .

Example answer:
{"entities": [{"text": "NPHP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "retinal degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Senior-Loken syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cerebellar anomalies", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Joubert syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The phenotype of cone dystrophy with supernormal rod response is tightly linked with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cone dystrophy with supernormal rod response is strictly associated with mutations in KCNV2 .

Example answer:
{"entities": [{"text": "Cone dystrophy with supernormal rod response", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Mutations in the NDP gene : contribution to Norrie disease , familial exudative vitreoretinopathy and retinopathy of prematurity .

## Item biored:test:419
Example input:
Sentence: Genetic analysis identified a novel V876E mutation in all HypoPP patients in the family , but not in normal family members or 160 control people .

Example answer:
{"entities": [{"text": "V876E", "type": "SequenceVariant"}, {"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Ten subjects with OPMD ( 6 symptomatic and 4 asymptomatic ) within the Taiwanese family carried a novel mutation in the PABPN1 gene .

Example answer:
{"entities": [{"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PABPN1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the current study , a three generation Asian Indian family with 15 congenital microcoria ( pupils with a diameter < 2 mm ) affected members was studied for linkage to candidate microsatellite markers at the 13q31-q32 locus .

Example answer:
{"entities": [{"text": "congenital microcoria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our data indicate that the 5-HTTLPR polymorphic element within the SLC6A4 promoter may govern the genetic risk of PD in Italians .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}, {"text": "SLC6A4", "type": "GeneOrGeneProduct"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Familial partial lipodystrophy ( Dunnigan ) type 3 ( FPLD3 , Mendelian Inheritance in Man [ MIM ] 604367 ) results from heterozygous mutations in PPARG encoding peroxisomal proliferator-activated receptor-gamma .

Example answer:
{"entities": [{"text": "Familial partial lipodystrophy ( Dunnigan ) type 3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FPLD3", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Mendelian Inheritance in Man [ MIM ] 604367", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PPARG", "type": "GeneOrGeneProduct"}, {"text": "peroxisomal proliferator-activated receptor-gamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : To identify the genetic basis of recessive inheritance of high hyperopia and Leber congenital amaurosis ( LCA ) in a family of Middle Eastern origin .

Example answer:
{"entities": [{"text": "high hyperopia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leber congenital amaurosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LCA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The goal of this study was to define the identities , origins and frequencies of TMC1 mutations in an expanded cohort of 557 large Pakistani families segregating recessive deafness .

Example answer:
{"entities": [{"text": "TMC1", "type": "GeneOrGeneProduct"}, {"text": "recessive deafness", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In summary , our findings demonstrate for the first time that mutations in PQBP1 are associated with an S-XLMR phenotype including microphthalmia , thereby further extending the clinical spectrum of phenotypes associated with PQBP1 mutations .

Example answer:
{"entities": [{"text": "PQBP1", "type": "GeneOrGeneProduct"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we report two maternal cousins with an apparently X-linked phenotype of mental retardation ( MR ) , microphthalmia , choroid coloboma , microcephaly , renal hypoplasia , and spastic paraplegia .

Example answer:
{"entities": [{"text": "X-linked phenotype of mental retardation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microphthalmia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "choroid coloboma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal hypoplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "spastic paraplegia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Haplotype analysis suggests a germline mosaicism of the 2-bp deletion in the maternal grandmother of both affected individuals .

Example answer:
{"entities": []}

Input:
Sentence: The objective of this study was to investigate the possibility of mosaicism in an XLRP family .

## Item biored:test:420
Example input:
Sentence: We characterized a four-generation South American family with HypoPP .

Example answer:
{"entities": [{"text": "HypoPP", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The second objective was to employ RB1 molecular deletion and microsatellite-based linkage analysis as laboratory tools , while counseling families with a history of retinoblastoma ( RB ) .

Example answer:
{"entities": [{"text": "RB1", "type": "GeneOrGeneProduct"}, {"text": "retinoblastoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "RB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using PCR-RFLP , we confirmed the heterozygous mutation in six affected family members and excluded it in three healthy members .

Example answer:
{"entities": []}

Example input:
Sentence: The rats were assigned into four groups ( n=10 per group ) , as follows : Control rats ; rats+atorvastatin ; rats + iopamidol ; rats+iopamidol+atorvastatin .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "rats+atorvastatin", "type": "OrganismTaxon"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "rats+iopamidol+atorvastatin", "type": "OrganismTaxon"}]}

Example input:
Sentence: PATIENTS AND METHODS : Six unrelated families and 10 sporadic patients were examined clinically .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: 480 subjects were studied : 240 patients with premature CAD , 240 age and sex matched blood donors .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: PATIENTS : The five patients derived from four families living in Shandong Province , China .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We collected 837 independent subjects ( 393 PD , 444 controls ) .

Example answer:
{"entities": [{"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Eight subjects in the RP family were recruited .

## Item biored:test:449
Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The findings of this study suggest that lesions of the unilateral STN and GPi are equally effective treatment for patients with advanced PD refractory to medical treatment .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "PD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The differential effects of bupivacaine and lidocaine on prostaglandin E2 release , cyclooxygenase gene expression and pain in a clinical pain model .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "prostaglandin E2", "type": "GeneOrGeneProduct"}, {"text": "cyclooxygenase", "type": "GeneOrGeneProduct"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The homeostasis model assessment of insulin resistance also differed significantly among groups ( F ( 33 ) = 4.92 ; P = .01 ) ( clozapine > olanzapine > risperidone ) ( clozapine vs risperidone , t ( 33 ) = 2.94 ; P = .006 ; olanzapine vs risperidone , t ( 33 ) = 2.42 ; P = .02 ) .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Administration of salvianolic acid A for a period of 8 days significantly attenuated isoproterenol-induced cardiac dysfunction and myocardial injury and improved mitochondrial respiratory function .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "ChemicalEntity"}, {"text": "isoproterenol-induced", "type": "ChemicalEntity"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myocardial injury", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Moreover , bupivacaine significantly increased COX-2 gene expression at 48 h as compared with the lidocaine/placebo group .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "lidocaine/placebo", "type": "ChemicalEntity"}]}

Example input:
Sentence: In blocking the positive inotropic and chronotropic responses to isoprenaline , ( + ) -propranolol had less than one hundredth the potency of ( - ) -propranolol .

Example answer:
{"entities": [{"text": "isoprenaline", "type": "ChemicalEntity"}]}

Example input:
Sentence: Post hoc analyses indicated that efficacy was similar with asenapine and haloperidol ; greater contrasts were seen in AEs , especially extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}, {"text": "extrapyramidal symptoms", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Clinical comparison of cardiorespiratory effects during unilateral and conventional spinal anaesthesia .

## Item biored:test:361
Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Endothelial NADPH oxidase 4 mediates vascular endothelial growth factor receptor 2-induced intravitreal neovascularization in a rat model of retinopathy of prematurity .

Example answer:
{"entities": [{"text": "NADPH oxidase 4", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor receptor", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Tumors implanted in LKB1 ( endo-/- ) mice but not macrophage-specific LKB1-knockout mice grew faster and showed enhanced vascular permeability and increased angiogenesis as compared with those implanted in wild-type mice .

Example answer:
{"entities": [{"text": "Tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "LKB1-knockout", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Endothelial LKB1 may regulate endothelial angiogenesis and tumor growth by modulating Sp1-mediated VEGF expression .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Sp1-mediated", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our results demonstrated that the absence of TIEG1 prevented cardiomyocytes from undergoing apoptosis and promoted higher proliferation ; it stimulated the proliferation of endothelial cells in vitro and in vivo .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One of the responding genes was X-chromosomal tenomodulin ( TNMD ) , a putative angiogenesis inhibitor .

Example answer:
{"entities": [{"text": "tenomodulin", "type": "GeneOrGeneProduct"}, {"text": "TNMD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: The transforming growth factor ( TGF ) -b-inducible early gene-1 ( TIEG1 ) plays a crucial role in modulating cell apoptosis and proliferation in a number of diseases , including pancreatic cancer , leukaemia and osteoporosis .

Example answer:
{"entities": [{"text": "transforming growth factor ( TGF ) -b-inducible early gene-1", "type": "GeneOrGeneProduct"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "osteoporosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Vascular endothelial growth factor ( VEGF ) level was highly co-stained in endothelial cells but not in macrophages in LKB1 ( endo-/- ) mice .

Example answer:
{"entities": [{"text": "Vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Endoglin gene ( ENG ) encodes a transmembrane glycoprotein which acts as an accessory receptor for the transforming growth factor-beta ( TGF-beta ) superfamily , and is crucial for maintaining vascular integrity .

## Item biored:test:397
Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Moreover , bupivacaine significantly increased COX-2 gene expression at 48 h as compared with the lidocaine/placebo group .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "lidocaine/placebo", "type": "ChemicalEntity"}]}

Example input:
Sentence: The hazard of developing CAD ( 95 % CI ) associated with initial treatment increased by 2.4-fold ( 1.3-4.3 , P=0.004 ) with glibenclamide ; 2-fold ( 0.9-4.6 , P=0.099 ) with glipizide ; 2.9-fold ( 1.6-5.1 , P=0.000 ) with either , and was unchanged with metformin .

Example answer:
{"entities": [{"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glibenclamide", "type": "ChemicalEntity"}, {"text": "glipizide", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "ChemicalEntity"}, {"text": "haloperidol", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

## Item biored:test:398
Example input:
Sentence: The hazard of developing CAD ( 95 % CI ) associated with initial treatment increased by 2.4-fold ( 1.3-4.3 , P=0.004 ) with glibenclamide ; 2-fold ( 0.9-4.6 , P=0.099 ) with glipizide ; 2.9-fold ( 1.6-5.1 , P=0.000 ) with either , and was unchanged with metformin .

Example answer:
{"entities": [{"text": "CAD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glibenclamide", "type": "ChemicalEntity"}, {"text": "glipizide", "type": "ChemicalEntity"}, {"text": "metformin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Fasting serum insulin concentrations differed among groups ( F ( 33 ) = 3.35 ; P = .047 ) ( clozapine > olanzapine > risperidone ) with significant differences between clozapine and risperidone ( t ( 33 ) = 2.32 ; P = .03 ) and olanzapine and risperidone ( t ( 33 ) = 2.15 ; P = .04 ) .

Example answer:
{"entities": [{"text": "insulin", "type": "ChemicalEntity"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: IFNAR1 deficiency significantly delayed the onset and frequency of diabetes and greatly reduced the intensity of insulitis after poly I : C treatment .

Example answer:
{"entities": [{"text": "IFNAR1", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "poly I : C", "type": "ChemicalEntity"}]}

Example input:
Sentence: The homeostasis model assessment of insulin resistance also differed significantly among groups ( F ( 33 ) = 4.92 ; P = .01 ) ( clozapine > olanzapine > risperidone ) ( clozapine vs risperidone , t ( 33 ) = 2.94 ; P = .006 ; olanzapine vs risperidone , t ( 33 ) = 2.42 ; P = .02 ) .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : While the incidence of new-onset diabetes mellitus may be increasing in patients with schizophrenia treated with certain atypical antipsychotic agents , it remains unclear whether atypical agents are directly affecting glucose metabolism or simply increasing known risk factors for diabetes .

Example answer:
{"entities": [{"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "schizophrenia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "antipsychotic agents", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "ChemicalEntity"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Input:
Sentence: In patients with diabetes , SCr increases > or = 0.5 mg/dL were 5.1 % ( 4 of 78 patients ) with iopamidol and 13.0 % ( 12 of 92 patients ) with iodixanol ( P=0.11 ) , whereas SCr increases > or = 25 % were 10.3 % and 15.2 % , respectively ( P=0.37 ) .

## Item biored:test:451
Example input:
Sentence: Here , we describe a case of severe masseter muscle rigidity ( jaw of steel ) after succinylcholine ( Sch ) administration during general anesthetic management for rigid bronchoscopic removal of a tracheal foreign body .

Example answer:
{"entities": [{"text": "masseter muscle rigidity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "jaw of steel", "type": "DiseaseOrPhenotypicFeature"}, {"text": "succinylcholine", "type": "ChemicalEntity"}, {"text": "Sch", "type": "ChemicalEntity"}]}

Example input:
Sentence: Cauda equina syndrome is a rare complication of epidural anesthesia .

Example answer:
{"entities": [{"text": "Cauda equina syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Prehospital care providers who are managing any patient with a syncopal episode that fails to recover within a reasonable time frame should consider the Bezold-Jarisch reflex as the cause and manage the patient accordingly .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "syncopal episode", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : The bupivacaine/rofecoxib group reported significantly less pain , as assessed by a visual analog scale , compared with the other three treatment groups over the first 4 h. However , the bupivacaine/placebo group reported significantly more pain at 24 h and PGE2 levels during the first 4 h were significantly higher than the other three treatment groups .

Example answer:
{"entities": [{"text": "bupivacaine/rofecoxib", "type": "ChemicalEntity"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bupivacaine/placebo", "type": "ChemicalEntity"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "ChemicalEntity"}, {"text": "convulsive", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lidocaine", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depression", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The data indicate that phenylephrine-induced hypertension instituted 2 h after MCAO does not aggravate edema in the ischemic core , that it improves edema in the periphery of the ischemic territory , and that it reduces the area of histochemical neuronal dysfunction .

Example answer:
{"entities": [{"text": "phenylephrine-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCAO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "edema", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ischemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuronal dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These results suggest that bupivacaine stimulates COX-2 gene expression after tissue injury , which is associated with higher PGE2 production and pain after the local anesthetic effect dissipates .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "ChemicalEntity"}, {"text": "COX-2", "type": "GeneOrGeneProduct"}, {"text": "tissue injury", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE2", "type": "GeneOrGeneProduct"}, {"text": "pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We tested the hypothesis that nimodipine ( NIMO ) administered at the onset of nitroglycerin ( NTG ) -induced hypotension would preserve long-term associative memory .

Example answer:
{"entities": [{"text": "nimodipine", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}, {"text": "nitroglycerin", "type": "ChemicalEntity"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Carotid arteries and vena cava were removed for measurement of isometric contraction .

Example answer:
{"entities": []}

Example input:
Sentence: Fentanyl did reduce minor intraoperative movement but had no sevoflurane-sparing effect and increased respiratory depression , hypotension and bradycardia .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "ChemicalEntity"}, {"text": "sevoflurane-sparing", "type": "ChemicalEntity"}, {"text": "respiratory depression", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "bradycardia", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Efforts must therefore continue to be made to obviate this setback OBJECTIVE : To evaluate the cardiovascular and respiratory changes during unilateral and conventional spinal anaesthesia .

## Item biored:test:406
Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Methadone , an agonist of OPRM1 , enhances the sensitivity of parental leukemic cells , but not OPRM1-depleted cells , to L-asparaginase treatment , indicating that OPRM1 is required for the synergistic action of L-asparaginase and methadone , and that OPRM1 loss promotes leukemic cell survival likely through downregulation of the OPRM1-mediated apoptotic pathway .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: According to annexin V binding , erythrocytes from patients indeed showed a significant increase of PS exposure within 1 week of treatment with azathioprine .

Example answer:
{"entities": [{"text": "annexin V", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PS", "type": "ChemicalEntity"}, {"text": "azathioprine", "type": "ChemicalEntity"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Exposure to azathioprine ( > or =2 microg/mL ) for 48 hours increased cytosolic Ca2+ activity and annexin V binding and decreased forward scatter .

Example answer:
{"entities": [{"text": "azathioprine", "type": "ChemicalEntity"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "annexin V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Human peripheral blood mononuclear cells ( PBMCs ) were isolated from a Taiwanese MDM family bearing the G to A substitution in nucleotide 256 in the SLURP1 gene , corresponding to a glycine to arginine substitution at amino acid 86 ( G86R ) in the SLURP-1 protein .

Example answer:
{"entities": [{"text": "Human", "type": "OrganismTaxon"}, {"text": "MDM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "G to A substitution in nucleotide 256", "type": "SequenceVariant"}, {"text": "SLURP1", "type": "GeneOrGeneProduct"}, {"text": "glycine to arginine substitution at amino acid 86", "type": "SequenceVariant"}, {"text": "G86R", "type": "SequenceVariant"}, {"text": "SLURP-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Input:
Sentence: Furthermore , peripheral blood monocytes isolated from ritonavir-treated females had less cholesteryl ester accumulation .

## Item biored:test:426
Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A single heterozygous missense mutation , substitution of a cytosine residue with thymidine in exon 2 of MSH5 , was found in two Caucasian women in whom POF developed at 18 and 36 years of age .

Example answer:
{"entities": [{"text": "cytosine residue with thymidine", "type": "SequenceVariant"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "women", "type": "OrganismTaxon"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Eleven subjects presented SRD5A2 homozygous single-base mutations ( two first cousins and four unrelated patients with G183S , two with R246W , one with del642T , one with G196S , and one with 217_218insC plus the A49T variant in heterozygosis ) , whereas four were compound heterozygotes ( one with Q126R/IVS3+1G > A , one with Q126R/del418T , and two brothers with Q126R/G158R ) .

Example answer:
{"entities": [{"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "G183S", "type": "SequenceVariant"}, {"text": "R246W", "type": "SequenceVariant"}, {"text": "del642T", "type": "SequenceVariant"}, {"text": "G196S", "type": "SequenceVariant"}, {"text": "217_218insC", "type": "SequenceVariant"}, {"text": "A49T", "type": "SequenceVariant"}, {"text": "Q126R/IVS3+1G > A", "type": "SequenceVariant"}, {"text": "Q126R/del418T", "type": "SequenceVariant"}, {"text": "Q126R/G158R", "type": "SequenceVariant"}]}

Example input:
Sentence: Her cells accumulated lipid-linked oligosaccharides lacking three glucose residues , and sequencing of the ALG6 gene showed what initially appeared to be a homozygous novel point mutation ( 338G > A ) .

Example answer:
{"entities": [{"text": "lipid-linked oligosaccharides", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "ALG6", "type": "GeneOrGeneProduct"}, {"text": "338G > A", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : A heterozygous in-frame deletion Y248del ( c.742_744delTAC ) was identified in one GH-secreting adenoma patient .

Example answer:
{"entities": [{"text": "Y248del", "type": "SequenceVariant"}, {"text": "c.742_744delTAC", "type": "SequenceVariant"}, {"text": "GH-secreting adenoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Sequence analysis of aggrecan complementary DNA from an affected individual revealed homozygosity for a missense mutation ( c.6799G -- > A ) that predicts a p.D2267N amino acid substitution in the C-type lectin domain within the G3 domain of aggrecan .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "c.6799G -- > A", "type": "SequenceVariant"}, {"text": "p.D2267N", "type": "SequenceVariant"}]}

Example input:
Sentence: Using a combination of homozygosity mapping and candidate gene approach , we have identified a homozygous single base pair deletion ( c.1052delA ) in SP7/Osterix ( OSX ) in an Egyptian child with recessive osteogenesis imperfecta .

Example answer:
{"entities": [{"text": "single base pair deletion", "type": "SequenceVariant"}, {"text": "c.1052delA", "type": "SequenceVariant"}, {"text": "SP7/Osterix", "type": "GeneOrGeneProduct"}, {"text": "OSX", "type": "GeneOrGeneProduct"}, {"text": "recessive osteogenesis imperfecta", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All nine patients were homozygous and their parents heterozygous for a novel , translationally silent GLDC exon 22 transversion c.2607C > A .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "GLDC", "type": "GeneOrGeneProduct"}, {"text": "c.2607C > A", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA samples of 760 anonymous AJ subjects were submitted for analysis , subsequently detecting six individuals heterozygous for the GALT deletion mutation , giving a carrier frequency of 1 in 127 ( 0.79 % ) .

Example answer:
{"entities": [{"text": "GALT", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: A first-generation female , who was considered to be an obligate carrier , demonstrated a normal phenotype as well as a normal genotype in lymphocytic DNA , indicating the gonadal mosaicism ; however , a heterozygous AG-deletion at nucleotide 652 and 653 was identified in the genomic DNA of hair follicles , hair shaft , and buccal cells , indicating that the mutation is somatic .
