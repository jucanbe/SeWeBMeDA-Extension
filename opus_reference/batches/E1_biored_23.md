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

## Item biored:test:813
Example input:
Sentence: Also , histopathological renal tissue damage mediated by cisplatin was ameliorated by coenzyme Q10 treatment .

Example answer:
{"entities": [{"text": "renal tissue damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "coenzyme Q10", "type": "ChemicalEntity"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Coenzyme Q10 treatment ameliorates acute cisplatin nephrotoxicity in mice .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Also , BCNU administration increased serum tumor necrosis factor-alpha ( TNFalpha ) , hippocampal MT and malondialdehyde ( MDA ) contents as well as caspase-3 activity in addition to histological alterations .

Example answer:
{"entities": [{"text": "BCNU", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Methadone , an agonist of OPRM1 , enhances the sensitivity of parental leukemic cells , but not OPRM1-depleted cells , to L-asparaginase treatment , indicating that OPRM1 is required for the synergistic action of L-asparaginase and methadone , and that OPRM1 loss promotes leukemic cell survival likely through downregulation of the OPRM1-mediated apoptotic pathway .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Coenzyme Q10 significantly reduced blood urea nitrogen and serum creatinine levels which were increased by cisplatin .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "blood urea nitrogen", "type": "ChemicalEntity"}, {"text": "creatinine", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Coenzyme Q10 significantly compensated deficits in the antioxidant defense mechanisms ( reduced glutathione level and superoxide dismutase activity ) , suppressed lipid peroxidation , decreased the elevations of tumor necrosis factor-alpha , nitric oxide and platinum ion concentration , and attenuated the reductions of selenium and zinc ions in renal tissue resulted from cisplatin administration .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "nitric oxide", "type": "ChemicalEntity"}, {"text": "platinum", "type": "ChemicalEntity"}, {"text": "selenium", "type": "ChemicalEntity"}, {"text": "zinc", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Input:
Sentence: Compared with the model group , CMCS and 1,10-phenanthroline significantly improved serum ALT/AST , attenuated hepatic inflammation and improved peroxidative injury in liver , decreased MMP-2/9 activities in liver tissue , improved integration of scaffold structure , and decreased protein expression of VCAM-1 and ICAM-1 .

## Item biored:test:931
Example input:
Sentence: In addition , accumulated F4/80 ( + ) cells in the liver metastasis were not BM-derived F4/80 ( + ) cells , but mainly resident hepatic F4/80 ( + ) cells , and these resident hepatic F4/80 ( + ) cells were positive for TGF-b1 .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This study was designed to evaluate the role of angiotensin II subtype receptor 1a ( AT1a ) in the formation of liver metastasis in CRC .

Example answer:
{"entities": [{"text": "angiotensin II subtype receptor 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Star-PAP , a poly ( A ) polymerase , functions as a tumor suppressor in an orthotopic human breast cancer model .

Example answer:
{"entities": [{"text": "Star-PAP", "type": "GeneOrGeneProduct"}, {"text": "poly ( A ) polymerase", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of NEK2 , phospho-AKT and MMP-2 was evaluated by immunohistochemistry in 63 cases of HCC and matched adjacent non-tumorous liver tissues .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSION : Our paper demonstrates the suitability and superiority of human liver slices over primary hepatocytes for studying the functional role of PPARa in human liver .

## Item biored:test:968
Example input:
Sentence: A multiple logistic regression analysis indicated that the odds ratio for EH in the -395A allele carriers as compared with the control group was 0.593 ( P=0.024 ) after adjusting for current traditional risk factors .

Example answer:
{"entities": [{"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-395A", "type": "SequenceVariant"}]}

Example input:
Sentence: Additionally , when PSA genotype was cross classified with CAG repeat , significantly more cases than both BPH and population controls were observed to have a short ( < 22 ) CAG/GG genotype ( P = 0.006 ) .

Example answer:
{"entities": [{"text": "PSA", "type": "GeneOrGeneProduct"}, {"text": "CAG repeat", "type": "SequenceVariant"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: FINDINGS : Similar distribution of the allelic and genotypic frequencies were observed between the groups ( p > 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Whereas allele frequencies for the other two polymorphisms did not differ significantly between any of the groups , the 111G allele frequency was significantly higher in subjects with extreme morning preference ( 0.14 ) than in subjects with extreme evening preference ( 0.03 ) ( Fisher 's exact test , two-sided P value=0.031 , odds ratio=5.67 ) .

Example answer:
{"entities": [{"text": "111G", "type": "SequenceVariant"}]}

Example input:
Sentence: In the control group the homozygote Ala allele was significantly higher than in the patient group ( P < 0.01 ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: The distribution of Ala/Val and homozygote Val alleles in the patient group was significantly higher than in the control group ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A statistically significant difference in allele frequency between cases and controls was observed for 2 of the SNPs ( +3100 T/G and +8365 C/T ) , with an odds ratio of 0.78 ( 95 % CI=0.64-0.96 ) and 0.65 ( 95 % CI=0.45-0.94 ) respectively .

Example answer:
{"entities": [{"text": "+3100 T/G", "type": "SequenceVariant"}, {"text": "+8365 C/T", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Significant differences were detected in genotypic distribution ( p = 0.04 ) as well as the allelic frequency ( p = 0.003 ) between the SHCM patients and controls .

Example answer:
{"entities": [{"text": "SHCM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Allele and genotype frequencies were compared between patients and controls using a X ( 2 ) test .

## Item biored:test:946
Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The enhanced metastatic potential was associated with transcriptional upregulation of osteopontin , osteocalcin , and collagen IA1 in osteotropic PC cells , suggesting their role in osteomimicry of PC cells .

Example answer:
{"entities": [{"text": "osteopontin", "type": "GeneOrGeneProduct"}, {"text": "osteocalcin", "type": "GeneOrGeneProduct"}, {"text": "collagen IA1", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggested that emodin-regulated cell growth and apoptosis were mediated by inhibiting FASN and provide a molecular basis for colon cancer therapy .

Example answer:
{"entities": [{"text": "emodin-regulated", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These studies demonstrate a critical role for PKCalpha signaling in endometrial tumorigenesis by regulating expression of CDK inhibitors p21 and p27 and activation of Akt and ERK-dependent proliferative pathways .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "ERK-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Additionally , downregulation of CEP55 in ovarian cancer cells remarkably inhibited cellular motility and invasion .

## Item biored:test:969
Example input:
Sentence: Multivariate forward stepwise regression analysis for significant parameters showed that among the studied parameters CCL4 and CCL5 ( P=0.001 ) are diagnostic markers of HCC .

Example answer:
{"entities": [{"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Syndromic and non-syndromic clefts were considered for cluster analysis , and phenotypic characterization , while only non-syndromic for risk factor analysis .

Example answer:
{"entities": [{"text": "clefts", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both lens and corneal differentiation programs were sensitive to Ras activation .

Example answer:
{"entities": [{"text": "Ras", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A combined clinical and genetic study was conducted in a cohort of patients with CDSRR , to substantiate these prior RESULTS : Seventeen patients from 13 families underwent a detailed ophthalmic examination including color vision testing , Goldmann visual fields , fundus photography , Ganzfeld and multifocal ERGs , and optical coherence tomography .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "CDSRR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The goal of this study was to perform 5-alpha-reductase type 2 gene ( SRD5A2 ) analysis in a male pseudohermaphrodite ( MPH ) patient with normal testosterone ( T ) production and normal androgen receptor ( AR ) gene coding sequences .

Example answer:
{"entities": [{"text": "5-alpha-reductase type 2", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "male pseudohermaphrodite", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MPH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "testosterone", "type": "ChemicalEntity"}, {"text": "T", "type": "ChemicalEntity"}, {"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analysis of androgen receptor ( AR ) and SRD5A2 genes was performed in 29 patients with 46 , XY DSD , by PCR-SSCP .

Example answer:
{"entities": [{"text": "androgen receptor", "type": "GeneOrGeneProduct"}, {"text": "AR", "type": "GeneOrGeneProduct"}, {"text": "SRD5A2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "46 , XY DSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : Six affected family members were examined clinically including visual acuity , color cornea photography , applanation tonography , and fundoscopy .

Example answer:
{"entities": []}

Example input:
Sentence: The polymorphism distribution was also analyzed in AD patients stratified according to differential progressive rate of cognitive decline during a 2-year follow-up .

Example answer:
{"entities": [{"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cognitive decline", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The analyses were stratified for recurrent status , complicated cataract status , and steroid-sensitive status .

## Item biored:test:944
Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Consistent with these in vitro data , expression levels of the ER stress markers 78-kDa glucose-regulated protein and CCAAT/enhancer-binding protein homologous protein , as well as that of the RA marker glial fibrillary acidic protein were increased in APP/PS1 AD mouse model .

Example answer:
{"entities": [{"text": "78-kDa glucose-regulated protein", "type": "GeneOrGeneProduct"}, {"text": "CCAAT/enhancer-binding protein homologous protein", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Furthermore , the number of the CASP8 -652 6N del ( but not 302H ) variant allele tended to correlate with increased levels of camptothecin-induced p53-mediated apoptosis in T lymphocytes from 170 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "camptothecin-induced", "type": "ChemicalEntity"}, {"text": "p53-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: Patients with high CEP55 protein expression had shorter overall survival and disease-free survival compared with those with low CEP55 expression .

## Item biored:test:926
Example input:
Sentence: While variations of IL-1beta , IL-7 , IL-8 , IL-17 , CCL5 , and HGF were associated with the SOD2 T2734C SNP , variations of PDFG-BB and CCL2 were associated with the CAT C262T SNP .

Example answer:
{"entities": [{"text": "IL-1beta", "type": "GeneOrGeneProduct"}, {"text": "IL-7", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HGF", "type": "GeneOrGeneProduct"}, {"text": "SOD2", "type": "GeneOrGeneProduct"}, {"text": "T2734C", "type": "SequenceVariant"}, {"text": "PDFG-BB", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CAT", "type": "GeneOrGeneProduct"}, {"text": "C262T", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Family-based TDT showed a significant association of SLE with a N673S polymorphism in the P-selectin gene ( SELP ) ( P = 5.74 x 10 ( -6 ) ) and a C203S polymorphism in the interleukin-1 receptor-associated kinase 1 gene ( IRAK1 ) ( P = 9.58 x 10 ( -6 ) ) .

Example answer:
{"entities": [{"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "N673S", "type": "SequenceVariant"}, {"text": "P-selectin", "type": "GeneOrGeneProduct"}, {"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "C203S", "type": "SequenceVariant"}, {"text": "interleukin-1 receptor-associated kinase 1", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : We genotyped eight single nucleotide polymorphisms ( SNPs ) in the three genes , DBH , IL1A and IL6 .

Example answer:
{"entities": [{"text": "DBH", "type": "GeneOrGeneProduct"}, {"text": "IL1A", "type": "GeneOrGeneProduct"}, {"text": "IL6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Variation in IL10 and other genes involved in the immune response and in oxidation and prostate cancer recurrence .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: mRNA expression of T ( H ) 1/T ( H ) 2-related genes partly correlated with cytokines at protein level .

Example answer:
{"entities": []}

Example input:
Sentence: Essential components of the innate immune antiviral response , including type I interferon ( IFN ) and IFN receptor-mediated signaling pathways , are candidates for determining susceptibility to human type 1 diabetes .

Example answer:
{"entities": [{"text": "type I interferon", "type": "GeneOrGeneProduct"}, {"text": "IFN", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: HAT subjects had increased anti-inflammatory genes TGFB1 , TIMP1 , TIMP3 , and TIMP4 while proinflammatory PIG7 and MMP2 were also significantly increased ; all genes , p < 0.025 .

Example answer:
{"entities": [{"text": "TGFB1", "type": "GeneOrGeneProduct"}, {"text": "TIMP1", "type": "GeneOrGeneProduct"}, {"text": "TIMP3", "type": "GeneOrGeneProduct"}, {"text": "TIMP4", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PIG7", "type": "GeneOrGeneProduct"}, {"text": "MMP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cytokines , T-cells and mRNA expression of T ( H ) 1/T ( H ) 2-related genes were assessed .

Example answer:
{"entities": []}

Example input:
Sentence: The aim of this study was therefore to investigate the influence of mutations in these innate immune receptor genes ( nucleotide oligomerisation domain ( NOD ) 2/caspase recruitment domain ( CARD ) 15 , NOD1/CARD4 , TUCAN/CARDINAL/CARD8 , Toll-like receptor ( TLR ) 4 , TLR2 , TLR1 and TLR6 ) on the development of antimicrobial and antiglycan antibodies in inflammatory bowel disease ( IBD ) .

Example answer:
{"entities": [{"text": "innate immune receptor", "type": "GeneOrGeneProduct"}, {"text": "nucleotide oligomerisation domain ( NOD )", "type": "GeneOrGeneProduct"}, {"text": "recruitment domain ( CARD ) 15", "type": "GeneOrGeneProduct"}, {"text": "NOD1/CARD4", "type": "GeneOrGeneProduct"}, {"text": "TUCAN/CARDINAL/CARD8", "type": "GeneOrGeneProduct"}, {"text": "Toll-like receptor ( TLR ) 4", "type": "GeneOrGeneProduct"}, {"text": "TLR2", "type": "GeneOrGeneProduct"}, {"text": "TLR1", "type": "GeneOrGeneProduct"}, {"text": "TLR6", "type": "GeneOrGeneProduct"}, {"text": "inflammatory bowel disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IBD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Input:
Sentence: IFITM1 , IFIT1 , IFIT2 , IFIT3 ) and numerous other immune-related genes ( e.g .

## Item biored:test:956
Example input:
Sentence: CYP treatment significantly ( p < or = 0.001 ) increased expression of CXCL1 and IL-1beta in the urinary bladder of WT and VIP ( -/- ) mice , but expression in VIP ( -/- ) mice with CYP treatment was significantly ( p < or = 0.001 ) greater ( 4.2- to 13-fold increase ) than that observed in WT urinary bladder ( 3.6- to 5-fold increase ) .

Example answer:
{"entities": []}

Example input:
Sentence: In one such mouse model , potent angiogenesis inhibitors elicit compartmental reorganization of cancer cells around remaining blood vessels .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Overload was induced in mouse plantaris muscle by unilateral synergist ablation .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: A mouse model of BLM-induced PF was established , and Bach1 siRNA ( 1x109 pfu ) was administered to the mice via the tail vein .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "BLM-induced", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The growth of breast cancer xenografts in NOD/SCID mice was also inhibited by the doxycycline-induced Star-PAP overexpression .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "doxycycline-induced", "type": "ChemicalEntity"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Utilizing the Eu-myc mouse model , where Myc is overexpressed specifically in B cells , both basal and stimulated BCR signaling were increased in precancerous B lymphocytes from Eu-myc mice compared with wild-type littermates .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "Myc", "type": "GeneOrGeneProduct"}, {"text": "BCR", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: Tumors implanted in LKB1 ( endo-/- ) mice but not macrophage-specific LKB1-knockout mice grew faster and showed enhanced vascular permeability and increased angiogenesis as compared with those implanted in wild-type mice .

Example answer:
{"entities": [{"text": "Tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "LKB1-knockout", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Overexpression also led to an increase in the number and size of lung metastases in the mouse tail vein injection model .

## Item biored:test:958
Example input:
Sentence: Furthermore , the MLFs infected with Bach1 siRNA exhibited increased mRNA and protein expression levels of heme oxygenase-1 and glutathione peroxidase 1 , but decreased levels of TGF-b1 and interleukin-6 in the cell supernatants compared with the cells exposed to TGF-b1 alone .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "heme oxygenase-1", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase 1", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "interleukin-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We first identified the change of signaling pathways and differentially expressed proteins globally by removing CB in Tg mice using mass spectrometry and antibody microarray .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: HAT subjects had increased anti-inflammatory genes TGFB1 , TIMP1 , TIMP3 , and TIMP4 while proinflammatory PIG7 and MMP2 were also significantly increased ; all genes , p < 0.025 .

Example answer:
{"entities": [{"text": "TGFB1", "type": "GeneOrGeneProduct"}, {"text": "TIMP1", "type": "GeneOrGeneProduct"}, {"text": "TIMP3", "type": "GeneOrGeneProduct"}, {"text": "TIMP4", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PIG7", "type": "GeneOrGeneProduct"}, {"text": "MMP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Bioinformatics gene ontology ( GO ) analysis of these 306 genes revealed significant enrichment in `` signal peptides '' , `` extracellular matrix '' and `` secreted proteins '' GO Terms .

Example answer:
{"entities": []}

Example input:
Sentence: Consistent with these in vitro data , expression levels of the ER stress markers 78-kDa glucose-regulated protein and CCAAT/enhancer-binding protein homologous protein , as well as that of the RA marker glial fibrillary acidic protein were increased in APP/PS1 AD mouse model .

Example answer:
{"entities": [{"text": "78-kDa glucose-regulated protein", "type": "GeneOrGeneProduct"}, {"text": "CCAAT/enhancer-binding protein homologous protein", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Expression of TGF-beta3 mRNA revealed contrary patterns in KFs from different patients while expression of TGF-betaRI was found to be equal during the measurement period .

Example answer:
{"entities": [{"text": "TGF-beta3", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "TGF-betaRI", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Combined analysis of tiling-resolution array-CGH with gene expression profiling on 11 MCL tumours enabled the identification of genomic alterations and their corresponding gene expression profiles .

Example answer:
{"entities": [{"text": "MCL tumours", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A total of 610 differentially expressed genes ( DEGs ) were revealed in the transcriptome comparison , 297 of which were upregulated and 313 were downregulated in HCC .

Example answer:
{"entities": [{"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Investigation of mRNA expression patterns showed that transgelin overexpression altered the levels of approximately 250 other transcripts , with over-representation of genes that affect function of actin or other cytoskeletal proteins .

## Item biored:test:989
Example input:
Sentence: These findings identify an autosomal-recessive skeletal dysplasia and a significant role for the aggrecan C-type lectin domain in regulating endochondral ossification and , thereby , height .

Example answer:
{"entities": [{"text": "autosomal-recessive skeletal dysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "aggrecan", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast , CM of TNF-alpha-stimulate or BMP2-stimulated C4-2B cells induced in vitro mineralization of MC3T3-E1 osteoblast cells in a BMP-2-dependent and NF-kappaB-dependent manner , respectively .

Example answer:
{"entities": [{"text": "TNF-alpha-stimulate", "type": "GeneOrGeneProduct"}, {"text": "BMP2-stimulated", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "MC3T3-E1", "type": "CellLine"}, {"text": "BMP-2-dependent", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tumor cellular senescence induced by genotoxic treatments has recently been found to be paradoxically linked to the induction of `` stemness . ''

Example answer:
{"entities": []}

Example input:
Sentence: Additionally , the fetal TCRg chain repertoire is altered , and peripheral Vg4 gd T cells are mostly restricted to the IFNg-producing phenotype in HEB-deficient mice .

Example answer:
{"entities": [{"text": "TCRg", "type": "GeneOrGeneProduct"}, {"text": "Vg4", "type": "GeneOrGeneProduct"}, {"text": "IFNg-producing", "type": "GeneOrGeneProduct"}, {"text": "HEB-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Zebrafish chordin-like and chordin are functionally redundant in regulating patterning of the dorsoventral axis .

Example answer:
{"entities": [{"text": "Zebrafish", "type": "OrganismTaxon"}, {"text": "chordin-like", "type": "GeneOrGeneProduct"}, {"text": "chordin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These results establish in the majority of ACC the presence of a previously uncharacterized population of CD133 ( + ) cells with neural stem properties , which are driven by SOX10 , NOTCH1 , and FABP7 .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "FABP7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gankyrin deficiency in non-parenchymal cells , but not in parenchymal cells , reduced STAT3 activity , interleukin ( IL ) -6 production , and cancer stem cell marker ( Bmi1 and epithelial cell adhesion molecule [ EpCAM ] ) expression , leading to attenuated tumorigenic potential .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "interleukin ( IL ) -6", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bmi1", "type": "GeneOrGeneProduct"}, {"text": "epithelial cell adhesion molecule", "type": "GeneOrGeneProduct"}, {"text": "EpCAM", "type": "GeneOrGeneProduct"}, {"text": "tumorigenic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Drosophila ovarian germline stem cells ( GSCs ) are maintained by Dpp signaling and the Pumilio ( Pum ) and Nanos ( Nos ) translational repressors .

Example answer:
{"entities": [{"text": "Drosophila", "type": "OrganismTaxon"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Pumilio", "type": "GeneOrGeneProduct"}, {"text": "Pum", "type": "GeneOrGeneProduct"}, {"text": "Nanos", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin system is crucial to regulation of energy homeostasis .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TNF-alpha or conditioned media ( CM ) of TNF-alpha-stimulated C4-2B cells upregulated BMP-2 and BMP-dependent Smad transcripts and inhibited receptor activator of NF-kappaB ligand transcripts in RAW 264.7 preosteoclast cells , respectively , implying that this factor may contribute to suppression of osteoclastogenesis via direct and paracrine mechanisms .

Example answer:
{"entities": [{"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha-stimulated", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "BMP-2", "type": "GeneOrGeneProduct"}, {"text": "BMP-dependent", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "receptor activator of NF-kappaB ligand", "type": "GeneOrGeneProduct"}, {"text": "RAW 264.7", "type": "CellLine"}]}

Input:
Sentence: However , regulation of the cambium , the stem cell niche required for lateral growth of shoots and roots , is poorly characterized .

## Item biored:test:940
Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These studies demonstrate a critical role for PKCalpha signaling in endometrial tumorigenesis by regulating expression of CDK inhibitors p21 and p27 and activation of Akt and ERK-dependent proliferative pathways .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "ERK-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ovarian serous carcinoma ( OSC ) is the most common and lethal histologic type of ovarian epithelial malignancy .

Example answer:
{"entities": [{"text": "Ovarian serous carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian epithelial malignancy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subsequently , 18 ovarian carcinoma-derived cell lines and 41 primary OSCs were evaluated for NF1 alterations .

Example answer:
{"entities": [{"text": "ovarian", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CEP55 was significantly upregulated in ovarian cancer cell lines and lesions compared with normal cells and adjacent noncancerous ovarian tissues .

## Item biored:test:949
Example input:
Sentence: One of the responding genes was X-chromosomal tenomodulin ( TNMD ) , a putative angiogenesis inhibitor .

Example answer:
{"entities": [{"text": "tenomodulin", "type": "GeneOrGeneProduct"}, {"text": "TNMD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The transforming growth factor ( TGF ) -b-inducible early gene-1 ( TIEG1 ) plays a crucial role in modulating cell apoptosis and proliferation in a number of diseases , including pancreatic cancer , leukaemia and osteoporosis .

Example answer:
{"entities": [{"text": "transforming growth factor ( TGF ) -b-inducible early gene-1", "type": "GeneOrGeneProduct"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "osteoporosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: FGFR1 and NTRK3 actionable alterations in `` Wild-Type '' gastrointestinal stromal tumors .

Example answer:
{"entities": [{"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}, {"text": "gastrointestinal stromal tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Using patient demographics , tumor characteristics , and CGP , we show that GIST lacking alterations in canonical genes occur in younger patients , frequently metastasize to lymph nodes , and most contain deleterious genomic alterations , including gene fusions involving FGFR1 and NTRK3 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "metastasize to lymph nodes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results suggested that emodin-regulated cell growth and apoptosis were mediated by inhibiting FASN and provide a molecular basis for colon cancer therapy .

Example answer:
{"entities": [{"text": "emodin-regulated", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The enhanced metastatic potential was associated with transcriptional upregulation of osteopontin , osteocalcin , and collagen IA1 in osteotropic PC cells , suggesting their role in osteomimicry of PC cells .

Example answer:
{"entities": [{"text": "osteopontin", "type": "GeneOrGeneProduct"}, {"text": "osteocalcin", "type": "GeneOrGeneProduct"}, {"text": "collagen IA1", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Transgelin increases metastatic potential of colorectal cancer cells in vivo and alters expression of genes involved in cell motility .

## Item biored:test:948
Example input:
Sentence: Diagnostic markers such as N-terminal pro brain natriuretic peptide ( NT-proBNP ) or high-sensitive C-reactive protein might help in the early identification of patients at risk , thus avoiding the occurrence of serious cardiovascular toxicity .

Example answer:
{"entities": [{"text": "N-terminal pro brain natriuretic peptide", "type": "ChemicalEntity"}, {"text": "NT-proBNP", "type": "ChemicalEntity"}, {"text": "C-reactive protein", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "cardiovascular toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHOD : Data were obtained from two clinical trials : 1 ) acute Epo exposure ( rHuEpo , 400 IU/kg ) followed by WAT biopsies after 1 h and 2 ) 10 weeks treatment with the erythropoiesis-stimulating agent ( ESA ) Darbepoietin-alpha .

Example answer:
{"entities": [{"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "erythropoiesis-stimulating agent", "type": "ChemicalEntity"}, {"text": "ESA", "type": "ChemicalEntity"}, {"text": "Darbepoietin-alpha", "type": "ChemicalEntity"}]}

Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Socs2 , plus five additional targets , further proved to comprise new EPOR/Jak2/Stat5 response genes ( which are important for erythropoiesis during anemia ) .

Example answer:
{"entities": [{"text": "Socs2", "type": "GeneOrGeneProduct"}, {"text": "EPOR/Jak2/Stat5", "type": "GeneOrGeneProduct"}, {"text": "anemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A unique set of EPO-regulated survival factors included Lyl1 , Gas5 , Pim3 , Pim1 , Bim , Trib3 and Serpina 3g .

Example answer:
{"entities": [{"text": "EPO-regulated", "type": "GeneOrGeneProduct"}, {"text": "Lyl1", "type": "GeneOrGeneProduct"}, {"text": "Gas5", "type": "GeneOrGeneProduct"}, {"text": "Pim3", "type": "GeneOrGeneProduct"}, {"text": "Pim1", "type": "GeneOrGeneProduct"}, {"text": "Bim", "type": "GeneOrGeneProduct"}, {"text": "Trib3", "type": "GeneOrGeneProduct"}, {"text": "Serpina 3g", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study aimed to investigate whether atorvastatin protects against CIN via anti-apoptotic effects by the upregulation of Hsp27 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hsp27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Thus , CEP55 may serve as a prognostic marker and therapeutic target for EOC .

## Item biored:test:933
Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis of Grade 1 endometrioid adenocarcinoma revealed aberrant PKCalpha expression , with foci of elevated PKCalpha staining , not observed in normal endometrium .

Example answer:
{"entities": [{"text": "endometrioid adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Ovarian serous carcinoma ( OSC ) is the most common and lethal histologic type of ovarian epithelial malignancy .

Example answer:
{"entities": [{"text": "Ovarian serous carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian epithelial malignancy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These studies demonstrate a critical role for PKCalpha signaling in endometrial tumorigenesis by regulating expression of CDK inhibitors p21 and p27 and activation of Akt and ERK-dependent proliferative pathways .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "ERK-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Upregulation of centrosomal protein 55 is associated with unfavorable prognosis and tumor invasion in epithelial ovarian carcinoma .

## Item biored:test:936
Example input:
Sentence: These results suggested that emodin-regulated cell growth and apoptosis were mediated by inhibiting FASN and provide a molecular basis for colon cancer therapy .

Example answer:
{"entities": [{"text": "emodin-regulated", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Collectively , these findings reveal a role for CSF-1 in mediating the IL-3 hematopoietic pathway through monopoiesis , which regulates expansion of CD11c+ macrophages .

Example answer:
{"entities": [{"text": "CSF-1", "type": "GeneOrGeneProduct"}, {"text": "IL-3", "type": "GeneOrGeneProduct"}, {"text": "CD11c+", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Subsequently , 18 ovarian carcinoma-derived cell lines and 41 primary OSCs were evaluated for NF1 alterations .

Example answer:
{"entities": [{"text": "ovarian", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alteration of NEK2 protein levels may contribute to invasion and metastasis of HCC , which may occur through activation of AKT signaling and promotion of MMP-2 expression .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "metastasis of HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These studies demonstrate a critical role for PKCalpha signaling in endometrial tumorigenesis by regulating expression of CDK inhibitors p21 and p27 and activation of Akt and ERK-dependent proliferative pathways .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "ERK-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The enhanced metastatic potential was associated with transcriptional upregulation of osteopontin , osteocalcin , and collagen IA1 in osteotropic PC cells , suggesting their role in osteomimicry of PC cells .

Example answer:
{"entities": [{"text": "osteopontin", "type": "GeneOrGeneProduct"}, {"text": "osteocalcin", "type": "GeneOrGeneProduct"}, {"text": "collagen IA1", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Therefore , we investigated the expression and clinicopathological significance of CEP55 in patients with EOC and its role in regulating invasion and metastasis of ovarian cell lines .

## Item biored:test:874
Example input:
Sentence: In addition , we observed an increased calcium influx in KCl-depolarised cells expressing mutated hippocalcin , mostly driven by N-type voltage-gated calcium channels .

Example answer:
{"entities": [{"text": "calcium", "type": "ChemicalEntity"}, {"text": "KCl-depolarised", "type": "ChemicalEntity"}, {"text": "hippocalcin", "type": "GeneOrGeneProduct"}, {"text": "N-type voltage-gated calcium channels", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Urinary sodium excretion reached signficantly lower values in sgk1 ( +/+ ) mice ( 15 +/- 5 mumol/mg crea ) than in sgk1 ( -/- ) mice ( 35 +/- 5 mumol/mg crea ) and was associated with a significantly higher body weight gain in sgk1 ( +/+ ) compared with sgk1 ( -/- ) mice ( +6.6 +/- 0.7 vs. +4.1 +/- 0.8 g ) .

Example answer:
{"entities": [{"text": "sodium", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "weight gain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Input:
Sentence: Urinary sodium , potassium and calcium were elevated in lithium-fed WT but not in lithium-fed PKCa KO mice .

## Item biored:test:886
Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tissue-Specific Ablation of the LIF Receptor in the Murine Uterine Epithelium Results in Implantation Failure .

Example answer:
{"entities": [{"text": "LIF Receptor", "type": "GeneOrGeneProduct"}, {"text": "Murine", "type": "OrganismTaxon"}]}

Example input:
Sentence: In rhesus monkeys , rDEN2Delta30 appeared to be slightly attenuated when compared to the parent virus as measured by duration and peak of viremia and neutralizing antibody induction .

Example answer:
{"entities": [{"text": "rhesus monkeys", "type": "OrganismTaxon"}, {"text": "rDEN2Delta30", "type": "OrganismTaxon"}, {"text": "viremia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hence , while alterations in select amino acid transporters are not associated with development of sepsis-induced Leu resistance , the Leu-stimulated binding of raptor with RagC and the recruitment of mTOR/raptor to the endosome-lysosomal compartment may partially explain the inability of Leu to fully activate mTOR and muscle protein synthesis .

Example answer:
{"entities": [{"text": "amino acid transporters", "type": "GeneOrGeneProduct"}, {"text": "sepsis-induced", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leu", "type": "ChemicalEntity"}, {"text": "Leu-stimulated", "type": "ChemicalEntity"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "RagC", "type": "GeneOrGeneProduct"}, {"text": "mTOR/raptor", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Given VIP 's role as an anti-inflammatory mediator , we hypothesized that VIP ( -/- ) mice would exhibit enhanced inflammatory mediator expression after cystitis .

Example answer:
{"entities": [{"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Interestingly , DCs that were co-treated with cisplatin and lipopolysaccharide ( LPS ) exhibited a decreased immunostimulatory capacity for inducing the proliferation of Th1- and Th17-type T cells ; instead , these DCs contributed to Th2-type T cell immunity .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "lipopolysaccharide", "type": "ChemicalEntity"}, {"text": "LPS", "type": "ChemicalEntity"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry and western blotting are used to determine the mechanisms of Sal against RIF .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "RIF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: To evaluate the role of LIF in the airways during RSV infection , animals were treated with neutralizing anti-LIF IgG , which enhanced RSV pathology observed with increased airspace protein content , apoptosis and airway hyperresponsiveness compared to control IgG treatment .

## Item biored:test:996
Example input:
Sentence: Brat promotes stem cell differentiation via control of a bistable switch that restricts BMP signaling .

Example answer:
{"entities": [{"text": "Brat", "type": "GeneOrGeneProduct"}, {"text": "BMP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tumor cellular senescence induced by genotoxic treatments has recently been found to be paradoxically linked to the induction of `` stemness . ''

Example answer:
{"entities": []}

Example input:
Sentence: We hypothesized that activin and/or GnRH pathways may be modulated by BMP-4 , but neither the activin-stimulated phosphorylation of Smad2/3 nor the GnRH-induced ERK1/2 or cAMP response element-binding phosphorylation were modified .

Example answer:
{"entities": [{"text": "activin", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "activin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "Smad2/3", "type": "GeneOrGeneProduct"}, {"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We show that FGFR2 signalling correlates with maintenance of expression of a key transcription factor for basal cell self-renewal and differentiation : SOX2 .

Example answer:
{"entities": [{"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "SOX2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Regulation of both targets simultaneously lowers cellular responsiveness to Dpp signaling , forcing the cell to become refractory to the self-renewal signal .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , metabolic symbiosis is established in the face of angiogenesis inhibition , whereby hypoxic cancer cells import glucose and export lactate , while normoxic cells import and catabolize lactate .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Drosophila ovarian germline stem cells ( GSCs ) are maintained by Dpp signaling and the Pumilio ( Pum ) and Nanos ( Nos ) translational repressors .

Example answer:
{"entities": [{"text": "Drosophila", "type": "OrganismTaxon"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Pumilio", "type": "GeneOrGeneProduct"}, {"text": "Pum", "type": "GeneOrGeneProduct"}, {"text": "Nanos", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hsp90beta was previously proven to regulate the upstream mediators in multiple cellular signalling cascades through stabilizing and maintaining their activities .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Zebrafish chordin-like and chordin are functionally redundant in regulating patterning of the dorsoventral axis .

Example answer:
{"entities": [{"text": "Zebrafish", "type": "OrganismTaxon"}, {"text": "chordin-like", "type": "GeneOrGeneProduct"}, {"text": "chordin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mathematical modeling elucidates bistability of cell fate in the Brat-mediated system , revealing how autoregulation of GSC number can arise from Brat coupling extracellular Dpp regulation to intracellular interpretation .

Example answer:
{"entities": [{"text": "Brat-mediated", "type": "GeneOrGeneProduct"}, {"text": "Brat", "type": "GeneOrGeneProduct"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Our findings provide evidence that common regulatory mechanisms in different plant stem cell niches are adapted to specific niche anatomies and emphasize the importance of a complex spatial organization of intercellular signaling cascades for a strictly bidirectional tissue production .

## Item biored:test:976
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CAA reduced hRPTEC cell number and protein , induced a loss in free intracellular thiols and an increase in necrosis markers .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "hRPTEC", "type": "CellLine"}, {"text": "thiols", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Importantly , this is the first experimental evidence that removal of CB from amyloid precursor protein/presenilin transgenic mice aggravates AD pathogenesis , suggesting that CB has a critical role in AD pathogenesis .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "amyloid precursor", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Consistent with these in vitro data , expression levels of the ER stress markers 78-kDa glucose-regulated protein and CCAAT/enhancer-binding protein homologous protein , as well as that of the RA marker glial fibrillary acidic protein were increased in APP/PS1 AD mouse model .

Example answer:
{"entities": [{"text": "78-kDa glucose-regulated protein", "type": "GeneOrGeneProduct"}, {"text": "CCAAT/enhancer-binding protein homologous protein", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: A haplotype containing these four SNPs ( CATA ) significantly increased protection of wet AMD with a P value of 0.0005 and an odds ratio of 0.29 ( 95 % confidence interval : 0.15-0.60 ) .

Example answer:
{"entities": [{"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Surfactant protein ( SP ) -A and SP-D are pattern-recognition molecules of the respiratory tract that activate inflammatory and phagocytic defences after binding to microbial sugars .

Example answer:
{"entities": [{"text": "Surfactant protein ( SP ) -A", "type": "GeneOrGeneProduct"}, {"text": "SP-D", "type": "GeneOrGeneProduct"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sugars", "type": "ChemicalEntity"}]}

Input:
Sentence: Serum amyloid A ( SAA ) is an evolutionary highly conserved acute phase protein that is predominantly secreted by hepatocytes .

## Item biored:test:942
Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Tumor TS 1494del6 genotype may be a prognostic factor in FU-based adjuvant treatment of colorectal cancer patients .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "1494del6", "type": "SequenceVariant"}, {"text": "FU-based", "type": "ChemicalEntity"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Furthermore , the number of the CASP8 -652 6N del ( but not 302H ) variant allele tended to correlate with increased levels of camptothecin-induced p53-mediated apoptosis in T lymphocytes from 170 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "camptothecin-induced", "type": "ChemicalEntity"}, {"text": "p53-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We report cytogenetic and molecular studies of a de novo , apparently balanced t ( 1 ; 3 ) ( q32.1 ; q25.1 ) identified in a 12-year-old female ( designated DGAP128 ) with cerebral atrophy , macrocephaly seizures , and developmental delay .

Example answer:
{"entities": [{"text": "cerebral atrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "macrocephaly", "type": "DiseaseOrPhenotypicFeature"}, {"text": "seizures", "type": "DiseaseOrPhenotypicFeature"}, {"text": "developmental delay", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It was concluded that coenzyme Q10 represents a potential therapeutic option to protect against acute cisplatin nephrotoxicity commonly encountered in clinical practice .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "nephrotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Moreover , patients with aberrant CEP55 protein expression showed tendencies to receive neoadjuvant chemotherapy ( P < 0.001 ) and cytoreductive surgery ( P = 0.020 ) .

## Item biored:test:967
Example input:
Sentence: For this purpose we developed a high-throughput methodology to genotype both normal and deleted alleles using a chip-based matrix-assisted laser desorption-time-of-flight ( MALDI-TOF ) mass spectrometer and Multiplex PCR .

Example answer:
{"entities": []}

Example input:
Sentence: The -930A > G polymorphism was genotyped using the TaqMan - Pre-designed SNP Genotyping Assay ( Applied Biosystems ) .

Example answer:
{"entities": [{"text": "-930A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: Polymerase chain reaction was carried out and single nucleotide polymorphisms of FGFR4 were identified by restriction enzyme digestion .

Example answer:
{"entities": [{"text": "FGFR4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : This study showed that SNPs rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , but not rs7535263 , rs1410996 , or rs2274700 , in CFH were significantly associated with wet AMD in a mainland Han Chinese population .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "rs7535263", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "rs2274700", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Patients were genotyped for rs4704559 , rs10942891 and rs4704560 by allelic discrimination with Taqman assays .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "rs4704559", "type": "SequenceVariant"}, {"text": "rs10942891", "type": "SequenceVariant"}, {"text": "rs4704560", "type": "SequenceVariant"}]}

Example input:
Sentence: All patients were genotyped for rs1799998 ( C-344 T ) , intron 2 conversion , rs4539 ( A2718G ) within CYP11B2 and rs6410 ( G22 5A ) , rs6387 ( A2803G ) within CYP11B1 .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs1799998", "type": "SequenceVariant"}, {"text": "C-344 T", "type": "SequenceVariant"}, {"text": "rs4539", "type": "SequenceVariant"}, {"text": "A2718G", "type": "SequenceVariant"}, {"text": "CYP11B2", "type": "GeneOrGeneProduct"}, {"text": "rs6410", "type": "SequenceVariant"}, {"text": "G22 5A", "type": "SequenceVariant"}, {"text": "rs6387", "type": "SequenceVariant"}, {"text": "A2803G", "type": "SequenceVariant"}, {"text": "CYP11B1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Seven SNPs in CFH and two SNPs in C2 , CFB ' , and C3 were genotyped using the ABI SNaPshot method .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CFI-rs7356506 polymorphisms were genotyped using Sequenom MassARRAY technology .

## Item biored:test:955
Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: UCHL1 depletion in SF188 and SJ-GBM2 glioma cells was associated with decreased cell proliferation and invasion , along with a reduced ability to grow in soft agar and to form spheres ( i.e .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "SF188", "type": "CellLine"}, {"text": "SJ-GBM2", "type": "CellLine"}, {"text": "glioma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "agar", "type": "ChemicalEntity"}]}

Example input:
Sentence: Re-expression of LKB1 or knockdown of VEGF receptor 2 decreased the overproliferation and -migration observed in LKB1 ( endo-/- ) cells .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tumors implanted in LKB1 ( endo-/- ) mice but not macrophage-specific LKB1-knockout mice grew faster and showed enhanced vascular permeability and increased angiogenesis as compared with those implanted in wild-type mice .

Example answer:
{"entities": [{"text": "Tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "LKB1-knockout", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Ras transgenic lenses and corneal epithelial cells showed increased proliferation with concomitant increases in cyclin D1 and D2 expression .

Example answer:
{"entities": [{"text": "Ras", "type": "GeneOrGeneProduct"}, {"text": "cyclin D1 and D2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: RESULTS : Stable overexpression of transgelin in RKO cells , which have low endogenous levels , led to increased invasiveness , growth at low density , and growth in soft agar .

## Item biored:test:987
Example input:
Sentence: Mathematical modeling elucidates bistability of cell fate in the Brat-mediated system , revealing how autoregulation of GSC number can arise from Brat coupling extracellular Dpp regulation to intracellular interpretation .

Example answer:
{"entities": [{"text": "Brat-mediated", "type": "GeneOrGeneProduct"}, {"text": "Brat", "type": "GeneOrGeneProduct"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: `` Angiogenesis and blood vessel development '' , `` neuron differentiation/development '' , cell adhesion '' , and `` cell migration '' also showed significant enrichment in our GO analysis .

Example answer:
{"entities": []}

Example input:
Sentence: We show that FGFR2 signalling correlates with maintenance of expression of a key transcription factor for basal cell self-renewal and differentiation : SOX2 .

Example answer:
{"entities": [{"text": "FGFR2", "type": "GeneOrGeneProduct"}, {"text": "SOX2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Insulin-like growth factor-1 ( IGF-1 ) is known to protect tissues from multiple types of damage , and protect cells from apoptosis .

Example answer:
{"entities": [{"text": "Insulin-like growth factor-1", "type": "GeneOrGeneProduct"}, {"text": "IGF-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Tumor cellular senescence induced by genotoxic treatments has recently been found to be paradoxically linked to the induction of `` stemness . ''

Example answer:
{"entities": []}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , metabolic symbiosis is established in the face of angiogenesis inhibition , whereby hypoxic cancer cells import glucose and export lactate , while normoxic cells import and catabolize lactate .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Drosophila ovarian germline stem cells ( GSCs ) are maintained by Dpp signaling and the Pumilio ( Pum ) and Nanos ( Nos ) translational repressors .

Example answer:
{"entities": [{"text": "Drosophila", "type": "OrganismTaxon"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Pumilio", "type": "GeneOrGeneProduct"}, {"text": "Pum", "type": "GeneOrGeneProduct"}, {"text": "Nanos", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Airway stem cells slowly self-renew and produce differentiated progeny to maintain homeostasis throughout the lifespan of an individual .

Example answer:
{"entities": []}

Example input:
Sentence: Hematopoietic stem cells ( HSCs ) maintain blood cell production life-long by their unique abilities of self-renewal and differentiation into all blood cell lineages .

Example answer:
{"entities": []}

Input:
Sentence: Plants maintain pools of pluripotent stem cells which allow them to constantly produce new tissues and organs .

## Item biored:test:934
Example input:
Sentence: Moreover , by regulating the expression of BIK ( BCL2-interacting killer ) , Star-PAP induced apoptosis of breast cancer cells through the mitochondrial pathway .

Example answer:
{"entities": [{"text": "BIK", "type": "GeneOrGeneProduct"}, {"text": "BCL2-interacting killer", "type": "GeneOrGeneProduct"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , the number of the CASP8 -652 6N del ( but not 302H ) variant allele tended to correlate with increased levels of camptothecin-induced p53-mediated apoptosis in T lymphocytes from 170 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "camptothecin-induced", "type": "ChemicalEntity"}, {"text": "p53-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The six-nucleotide deletion/insertion variant in the CASP8 promoter region is inversely associated with risk of squamous cell carcinoma of the head and neck .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chromosome instability ( CIN ) is associated with poor survival and therapeutic outcome in a number of malignancies .

Example answer:
{"entities": [{"text": "Chromosome instability", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "malignancies", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These studies demonstrate a critical role for PKCalpha signaling in endometrial tumorigenesis by regulating expression of CDK inhibitors p21 and p27 and activation of Akt and ERK-dependent proliferative pathways .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "ERK-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Centrosomal protein 55 ( CEP55 ) is a cell cycle regulator implicated in development of certain cancers .

## Item biored:test:875
Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A 2-wk administration of LiCl ( 4 mmol.kg ( -1 ) .day ( -1 ) ip ) in mPGES-1 +/+ mice led to a marked polyuria with hyposmotic urine .

Example answer:
{"entities": [{"text": "LiCl", "type": "ChemicalEntity"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In our study , 17-dimethylaminoethylamino-17-demethoxygeldanamycin ( 17-DMAG ) or Hsp90beta knockdown dramatically alleviated the high-salt-diet-induced proteinuria and renal damage without altering blood pressure significantly , when it reversed activations of NF-kappaB , mTOR and p38 signalling cascades .

Example answer:
{"entities": [{"text": "17-dimethylaminoethylamino-17-demethoxygeldanamycin", "type": "ChemicalEntity"}, {"text": "17-DMAG", "type": "ChemicalEntity"}, {"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "p38", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mice lacking mPGES-1 are resistant to lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In contrast , mPGES-1 -/- mice were largely resistant to lithium-induced polyuria and a urine concentrating defect , accompanied by nearly complete blockade of high urine PGE ( 2 ) and cAMP output .

Example answer:
{"entities": [{"text": "mPGES-1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "cAMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Similarly , the total protein abundance of the Na-K-2Cl cotransporter ( NKCC2 ) in the medulla but not in the cortex of the +/+ mice was significantly reduced by lithium treatment .

Example answer:
{"entities": [{"text": "Na-K-2Cl cotransporter", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "lithium", "type": "ChemicalEntity"}]}

Example input:
Sentence: The present study was undertaken to assess lithium-induced polyuria in mice deficient in microsomal prostaglandin E synthase-1 ( mPGES-1 ) .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "microsomal prostaglandin E synthase-1", "type": "GeneOrGeneProduct"}, {"text": "mPGES-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cyclooxygenase-2 activity is required for the development of lithium-induced polyuria .

Example answer:
{"entities": [{"text": "Cyclooxygenase-2", "type": "GeneOrGeneProduct"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We conclude that mPGES-1-derived PGE ( 2 ) mediates lithium-induced polyuria likely via inhibition of AQP2 and NKCC2 expression .

Example answer:
{"entities": [{"text": "mPGES-1-derived", "type": "GeneOrGeneProduct"}, {"text": "PGE ( 2 )", "type": "ChemicalEntity"}, {"text": "lithium-induced", "type": "ChemicalEntity"}, {"text": "polyuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "NKCC2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunoblotting , immunohistochemistry , and quantitative ( q ) RT-PCR consistently detected a significant decrease in aquaporin-2 ( AQP2 ) protein expression in both the renal cortex and medulla of lithium-treated +/+ mice .

Example answer:
{"entities": [{"text": "aquaporin-2", "type": "GeneOrGeneProduct"}, {"text": "AQP2", "type": "GeneOrGeneProduct"}, {"text": "lithium-treated", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Our data show that ablation of PKCa preserves AQP2 and UT-A1 protein expression and localization in lithium-induced NDI , and prevents the development of the severe polyuria associated with lithium therapy .

## Item biored:test:925
Example input:
Sentence: CD4 ( + ) T cells that produce IFN-g are the source of host-protective IL-10 during primary infection with a number of different pathogens , including Plasmodium spp .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "IFN-g", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To clarify the role of CCR5 host genetic background and disease progression on viral evolutionary patterns , we obtain gp120 envelope sequences from clonal HIV-1 variants isolated at multiple time points in the course of infection from populations of HIV-1-infected individuals who only harbored CCR5-using HIV-1 variants at all time points .

Example answer:
{"entities": [{"text": "CCR5", "type": "GeneOrGeneProduct"}, {"text": "gp120", "type": "GeneOrGeneProduct"}, {"text": "HIV-1", "type": "OrganismTaxon"}, {"text": "infection", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HIV-1-infected", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CCR5-using", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: C_6+/6+ and G_6+/6+ combined genotypes were respectively associated to the best and worst PFS ( P=0.03 when compared with each other ) , while combinations carrying the allele 6- determined an intermediate evolution that might be indicative of a variable response to chemotherapy .

Example answer:
{"entities": []}

Example input:
Sentence: Carriers of HLX1 exon 1 SNP rs12141189 showed increased IL-5 ( LpA , p = 0.007 ; Ppg , p = 0.10 ) , trendwise increased IL-13 ( LpA ) , higher GM-CSF ( LpA/Ppg , p < 0.05 ) and trendwise decreased IFN-g secretion ( Derp1+LpA-stimulation , p = 0.1 ) .

Example answer:
{"entities": [{"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs12141189", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "LpA", "type": "ChemicalEntity"}, {"text": "Ppg", "type": "ChemicalEntity"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "GM-CSF", "type": "GeneOrGeneProduct"}, {"text": "LpA/Ppg", "type": "ChemicalEntity"}, {"text": "IFN-g", "type": "GeneOrGeneProduct"}, {"text": "Derp1+LpA-stimulation", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: From a list of 185 candidate ciliary genes , we uncover orthologues of human MAP9 , YAP , CCDC149 , and RAB28 as conserved cilium-associated components .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "MAP9", "type": "GeneOrGeneProduct"}, {"text": "YAP", "type": "GeneOrGeneProduct"}, {"text": "CCDC149", "type": "GeneOrGeneProduct"}, {"text": "RAB28", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The normal ( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG due to an insertion of ( GCG ) 4GCA into the normal allele in the Taiwanese OPMD subjects .

Example answer:
{"entities": [{"text": "( GCG ) 6 ( GCA ) 3GCG sequence was replaced by ( GCG ) 6 ( GCA ) ( GCG ) 4 ( GCA ) 3GCG", "type": "SequenceVariant"}, {"text": "insertion of ( GCG ) 4GCA", "type": "SequenceVariant"}, {"text": "OPMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previous studies of our group found association of haplotypes in the IL8 and in the CXCR2 genes with the multifactorial disease chronic periodontitis .

Example answer:
{"entities": [{"text": "IL8", "type": "GeneOrGeneProduct"}, {"text": "CXCR2", "type": "GeneOrGeneProduct"}, {"text": "chronic periodontitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Several regulated genes were validated using enzyme-linked immunoassays including IL-1beta and CXCL1 .

Example answer:
{"entities": []}

Example input:
Sentence: Variation in the CXCR1 gene ( IL8RA ) is not associated with susceptibility to chronic periodontitis .

Example answer:
{"entities": [{"text": "CXCR1", "type": "GeneOrGeneProduct"}, {"text": "IL8RA", "type": "GeneOrGeneProduct"}, {"text": "chronic periodontitis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CXCL9-11 , CCL8 , CX3CL1 , CXCL6 ) , interferon g-induced genes ( e.g .

## Item biored:test:879
Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we knocked down Bach1 using adenovirus-mediated small interfering RNA ( siRNA ) to determine whether the use of Bach1 siRNA is an effective therapeutic strategy in mice with bleomycin ( BLM ) -induced PF .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "bleomycin", "type": "ChemicalEntity"}, {"text": "BLM", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse model of BLM-induced PF was established , and Bach1 siRNA ( 1x109 pfu ) was administered to the mice via the tail vein .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "BLM-induced", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Viruses were evaluated for replication in SCID mice transplanted with human hepatoma cells ( SCID-HuH-7 mice ) , in mosquitoes , and in rhesus monkeys .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hepatoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCID-HuH-7", "type": "CellLine"}, {"text": "rhesus monkeys", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : A549 , primary human small airway epithelial ( SAE ) cells and wild-type , TIR-domain-containing adapter-inducing interferon-b ( Trif ) and mitochondrial antiviral-signaling protein ( Mavs ) knockout ( KO ) mice were infected with RSV and cytokine responses were investigated by ELISA , multiplex analysis and qPCR .

## Item biored:test:952
Example input:
Sentence: Here , we investigated the effect of cisplatin on the functionality of DCs and the changes in signaling pathways activated upon toll-like receptor ( TLR ) stimulation .

Example answer:
{"entities": [{"text": "cisplatin", "type": "ChemicalEntity"}, {"text": "toll-like receptor", "type": "GeneOrGeneProduct"}, {"text": "TLR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Liver metastases from colorectal cancer ( CRC ) are a clinically significant problem .

Example answer:
{"entities": [{"text": "Liver metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study was designed to evaluate the role of angiotensin II subtype receptor 1a ( AT1a ) in the formation of liver metastasis in CRC .

Example answer:
{"entities": [{"text": "angiotensin II subtype receptor 1a", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that ADAM12 actively supports the CSC phenotype in claudin-low breast cancer cells via modulation of the EGFR pathway .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PURPOSE : The purpose of this study was to analyze the value of germline and tumor thymidylate synthase ( TS ) genotyping as a prognostic marker in a series of colorectal cancer patients receiving adjuvant fluorouracil ( FU ) -based treatment .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil", "type": "ChemicalEntity"}, {"text": "FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: In the present study we explored the effect of three polymorphisms of the TS gene on overall and progression- free survival of colorectal cancer ( CRC ) patients subjected to 5FU chemotherapy .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CRC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "5FU", "type": "ChemicalEntity"}]}

Example input:
Sentence: The enhanced metastatic potential was associated with transcriptional upregulation of osteopontin , osteocalcin , and collagen IA1 in osteotropic PC cells , suggesting their role in osteomimicry of PC cells .

Example answer:
{"entities": [{"text": "osteopontin", "type": "GeneOrGeneProduct"}, {"text": "osteocalcin", "type": "GeneOrGeneProduct"}, {"text": "collagen IA1", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Here we sought to determine the role of transgelin more directly by determining whether experimental manipulation of transgelin levels in colorectal cancer ( CRC ) cells led to changes in metastatic potential in vivo .

## Item biored:test:965
Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PATIENTS AND METHODS : We examined 102 patients ( men/women , 40/62 ; median age , 42 ) diagnosed with chronic ITP and 188 healthy controls ( men/women , 78/110 ; median age , 38 ) .

Example answer:
{"entities": [{"text": "PATIENTS", "type": "OrganismTaxon"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "men/women", "type": "OrganismTaxon"}, {"text": "chronic ITP", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : 133 patients who developed cancer following chemotherapy and/or radiotherapy ( n = 133 ) , 420 patients diagnosed with de novo myeloid leukaemia , 242 patients diagnosed with primary Hodgkin lymphoma , and 1177 healthy controls were genotyped for the MLH1 -93 polymorphism by allelic discrimination polymerase chain reaction ( PCR ) and restriction fragment length polymorphism assay .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "primary Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : A total of 1346 patients were randomized into the 8-week core study ( 734 men , 612 women ; 924 white , 291 black , 23 Asian , 108 other ; mean age , 52.7 years ; mean weight , 92.6 kg ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Since healthy relatives of the VUR probands are not reliable negative controls for VUR , we used a population of 90 race-matched , healthy individuals , unrelated to the VUR patients , as controls to perform an association study .

Example answer:
{"entities": [{"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We performed 2 sets of case-control comparisons using Japanese subjects ( first set : 830 patients with RA and 658 controls ; second set : 1112 patients with RA and 940 controls ) , and then performed a stratified analysis using human leukocyte antigen ( HLA ) -DRB1 shared epitope ( SE ) status .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "leukocyte antigen ( HLA ) -DRB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : A case-control study was carried out in Chinese Han population , including 368 cases of migraine and 517 controls .

Example answer:
{"entities": [{"text": "migraine", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS : This study included 133 patients with AVSD and 200 healthy controls .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "AVSD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: METHODS : A total of 100 patients diagnosed with VKH syndrome and 300 healthy controls were recruited for the study .

## Item biored:test:957
Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The formation of liver metastasis correlated with collagen deposition in the metastatic area , which was dependent on AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "collagen", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results suggested that resident hepatic macrophages induced liver metastasis formation by induction of TGF-b1 through AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Treatment of WT with clodronate liposomes suppressed liver metastasis by diminishing TGF-b1 ( + ) F4/80 ( + ) cells accumulation .

Example answer:
{"entities": [{"text": "clodronate", "type": "ChemicalEntity"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "F4/80", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The enhanced metastatic potential was associated with transcriptional upregulation of osteopontin , osteocalcin , and collagen IA1 in osteotropic PC cells , suggesting their role in osteomimicry of PC cells .

Example answer:
{"entities": [{"text": "osteopontin", "type": "GeneOrGeneProduct"}, {"text": "osteocalcin", "type": "GeneOrGeneProduct"}, {"text": "collagen IA1", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: In addition , accumulated F4/80 ( + ) cells in the liver metastasis were not BM-derived F4/80 ( + ) cells , but mainly resident hepatic F4/80 ( + ) cells , and these resident hepatic F4/80 ( + ) cells were positive for TGF-b1 .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Similarly , attenuation of transgelin expression in HCT116 cells , which have high endogenous levels , decreased metastases in the same model .

## Item biored:test:951
Example input:
Sentence: Recent studies found that TIPE2 was involved in cancer development .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : These data provide strong support for the hypothesis that common variation in GPX4 is associated with prognosis after a diagnosis of breast cancer .

Example answer:
{"entities": [{"text": "GPX4", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Using patient demographics , tumor characteristics , and CGP , we show that GIST lacking alterations in canonical genes occur in younger patients , frequently metastasize to lymph nodes , and most contain deleterious genomic alterations , including gene fusions involving FGFR1 and NTRK3 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "metastasize to lymph nodes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The renin-angiotensin system is involved in tumor growth and metastases .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gankyrin expression in the tumor microenvironment is negatively correlated with progression-free survival in patients undergoing sorafenib treatment for HCC .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "sorafenib", "type": "ChemicalEntity"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Faced with the selective pressure of oncogene withdrawal , Mad2-positive tumors have a higher frequency of developing persistent subclones that avoid remission and continue to grow .

Example answer:
{"entities": [{"text": "Mad2-positive", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The transforming growth factor ( TGF ) -b-inducible early gene-1 ( TIEG1 ) plays a crucial role in modulating cell apoptosis and proliferation in a number of diseases , including pancreatic cancer , leukaemia and osteoporosis .

Example answer:
{"entities": [{"text": "transforming growth factor ( TGF ) -b-inducible early gene-1", "type": "GeneOrGeneProduct"}, {"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "pancreatic cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "osteoporosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The purpose of this study was to analyze the value of germline and tumor thymidylate synthase ( TS ) genotyping as a prognostic marker in a series of colorectal cancer patients receiving adjuvant fluorouracil ( FU ) -based treatment .

Example answer:
{"entities": [{"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thymidylate synthase", "type": "GeneOrGeneProduct"}, {"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "colorectal cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "fluorouracil", "type": "ChemicalEntity"}, {"text": "FU", "type": "ChemicalEntity"}]}

Input:
Sentence: Although the role of transgelin in cancer is controversial , a number of studies have shown that elevated levels correlate with aggressive tumor behavior , advanced stage , and poor prognosis .

## Item biored:test:947
Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ectopic Star-PAP expression inhibited proliferation as well as colony-forming ability of breast cancer cells .

Example answer:
{"entities": [{"text": "Star-PAP", "type": "GeneOrGeneProduct"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These studies demonstrate a critical role for PKCalpha signaling in endometrial tumorigenesis by regulating expression of CDK inhibitors p21 and p27 and activation of Akt and ERK-dependent proliferative pathways .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "ERK-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Subsequently , 18 ovarian carcinoma-derived cell lines and 41 primary OSCs were evaluated for NF1 alterations .

Example answer:
{"entities": [{"text": "ovarian", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Alteration of NEK2 protein levels may contribute to invasion and metastasis of HCC , which may occur through activation of AKT signaling and promotion of MMP-2 expression .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "metastasis of HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Aberrant CEP55 expression may predict unfavorable clinical outcomes in EOC patients and play an important role in regulating invasion in ovarian cancer cells .

## Item biored:test:960
Example input:
Sentence: The formation of liver metastasis correlated with collagen deposition in the metastatic area , which was dependent on AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "collagen", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Our study shows that ACE is expressed locally in gastric cancer and that the gene polymorphism influences metastatic behavior .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Faced with the selective pressure of oncogene withdrawal , Mad2-positive tumors have a higher frequency of developing persistent subclones that avoid remission and continue to grow .

Example answer:
{"entities": [{"text": "Mad2-positive", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gankyrin expression in the tumor microenvironment is negatively correlated with progression-free survival in patients undergoing sorafenib treatment for HCC .

Example answer:
{"entities": [{"text": "Gankyrin", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "sorafenib", "type": "ChemicalEntity"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The renin-angiotensin system is involved in tumor growth and metastases .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sorafenib increased the expression of MT1G mRNA in a panel of human cancer cells , an effect that was not observed with eight other clinically-approved kinase inhibitors .

Example answer:
{"entities": [{"text": "Sorafenib", "type": "ChemicalEntity"}, {"text": "MT1G", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Using patient demographics , tumor characteristics , and CGP , we show that GIST lacking alterations in canonical genes occur in younger patients , frequently metastasize to lymph nodes , and most contain deleterious genomic alterations , including gene fusions involving FGFR1 and NTRK3 .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "metastasize to lymph nodes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The enhanced metastatic potential was associated with transcriptional upregulation of osteopontin , osteocalcin , and collagen IA1 in osteotropic PC cells , suggesting their role in osteomimicry of PC cells .

Example answer:
{"entities": [{"text": "osteopontin", "type": "GeneOrGeneProduct"}, {"text": "osteocalcin", "type": "GeneOrGeneProduct"}, {"text": "collagen IA1", "type": "GeneOrGeneProduct"}, {"text": "PC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSIONS : Increases or decreases in transgelin levels have reciprocal effects on tumor cell behavior , with higher expression promoting metastasis .

## Item biored:test:900
Example input:
Sentence: Protein level of BDNF was reduced in Dox-treated rat ventricles , whereas BDNF and its receptor tropomyosin-related kinase B ( TrkB ) were markedly up-regulated after BDNF administration .

Example answer:
{"entities": [{"text": "tropomyosin-related kinase", "type": "GeneOrGeneProduct"}, {"text": "(", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Investigations of the underlying mechanisms revealed that BDNF activated Akt and preserved phosphorylation of mammalian target of rapamycin and Bad without affecting p38 mitogen-activated protein kinase and extracellular regulated protein kinase pathways .

Example answer:
{"entities": [{"text": "mammalian target of", "type": "GeneOrGeneProduct"}, {"text": "p38 mitogen-activated protein", "type": "GeneOrGeneProduct"}, {"text": "extracellular regulated protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , using RNA interference with small inhibitory RNAs for Sp1 , Sp3 , and Sp4 , we observed that curcumin-dependent inhibition of nuclear factor kappaB ( NF-kappaB ) -dependent genes , such as bcl-2 , survivin , and cyclin D1 , was also due , in part , to loss of Sp proteins .

Example answer:
{"entities": [{"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "curcumin-dependent", "type": "ChemicalEntity"}, {"text": "nuclear factor kappaB", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "survivin", "type": "GeneOrGeneProduct"}, {"text": "cyclin D1", "type": "GeneOrGeneProduct"}, {"text": "Sp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: While NRG-1 beta potently and persistently activated Erk 1/2 , SAPK/JNK , Akt and Src family kinases , NRG-1 alpha did not activate Akt and activated these other kinases with kinetics distinct from those evident in NRG-1 beta-stimulated cells .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "Erk 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "NRG-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Nuclear factor kappa B ( NFkappaB ) is a sensor of oxidative stress and participates in memory formation that could be involved in drug toxicity and addiction mechanisms .

Example answer:
{"entities": [{"text": "Nuclear factor kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: The NSP-induced inhibition could be significantly reversed by administration of the NF-kappaB pathway inhibitor sc3060 , whereas , expressions of p-ERK1 , p-ERK2 , and p-AKT were upregulated by the OGD/R treatment ; however , their levels were unchanged by NSP administration .

## Item biored:test:977
Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: These results suggested that resident hepatic macrophages induced liver metastasis formation by induction of TGF-b1 through AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In this study , we establish the unilateral ureteric obstruction ( UUO ) or folic acid ( FA ) -induced mice renal interstitial fibrosis in vivo and the transforming growth factor ( TGF ) -beta1-stimulated human proximal tubular epithelial cell ( HK-2 ) model in vitro .

Example answer:
{"entities": [{"text": "unilateral ureteric obstruction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "UUO", "type": "DiseaseOrPhenotypicFeature"}, {"text": "folic acid", "type": "ChemicalEntity"}, {"text": "FA", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "transforming growth factor ( TGF )", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK-2", "type": "CellLine"}]}

Example input:
Sentence: In addition , accumulated F4/80 ( + ) cells in the liver metastasis were not BM-derived F4/80 ( + ) cells , but mainly resident hepatic F4/80 ( + ) cells , and these resident hepatic F4/80 ( + ) cells were positive for TGF-b1 .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The formation of liver metastasis correlated with collagen deposition in the metastatic area , which was dependent on AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "collagen", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Further study revealed that the effect of Sal on renal interstitial fibrosis is associated with the lower expression of TLR4 , p-IkappaBalpha , p-NF-kappaB and mitogen-activated protein kinases ( MAPK ) , both in vivo and in vitro .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinases", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Oxidative stress plays an essential role in inflammation and fibrosis .

Example answer:
{"entities": [{"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , its role in liver injury and fibrogenesis has not been elucidated so far .

## Item biored:test:935
Example input:
Sentence: A unique set of EPO-regulated survival factors included Lyl1 , Gas5 , Pim3 , Pim1 , Bim , Trib3 and Serpina 3g .

Example answer:
{"entities": [{"text": "EPO-regulated", "type": "GeneOrGeneProduct"}, {"text": "Lyl1", "type": "GeneOrGeneProduct"}, {"text": "Gas5", "type": "GeneOrGeneProduct"}, {"text": "Pim3", "type": "GeneOrGeneProduct"}, {"text": "Pim1", "type": "GeneOrGeneProduct"}, {"text": "Bim", "type": "GeneOrGeneProduct"}, {"text": "Trib3", "type": "GeneOrGeneProduct"}, {"text": "Serpina 3g", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A CASP8 promoter region six-nucleotide deletion/insertion ( -652 6N ins/del ) variant and a coding region D302H polymorphism are reportedly important in cancer development , but no reported study has assessed the associations of these genetic variations with risk of head and neck cancer .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N ins/del", "type": "SequenceVariant"}, {"text": "D302H", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "head and neck cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BRCA1 abnormalities were identified in all four families with ovarian cancer only , in 67 % of 27 families with both breast and ovarian cancer , and in 34 % of 35 families with breast cancer only .

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast and ovarian cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These studies demonstrate a critical role for PKCalpha signaling in endometrial tumorigenesis by regulating expression of CDK inhibitors p21 and p27 and activation of Akt and ERK-dependent proliferative pathways .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "ERK-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Neurofibromin 1 ( NF1 ) defects are common in human ovarian serous carcinomas and co-occur with TP53 mutations .

Example answer:
{"entities": [{"text": "Neurofibromin 1", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "ovarian serous carcinomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Previously , we showed that following etoposide ( ETO ) treatment embryonal carcinoma PA-1 cells undergo a p53-dependent upregulation of OCT4A and p21Cip1 ( governing self-renewal and regulating cell cycle inhibition and senescence , respectively ) .

Example answer:
{"entities": [{"text": "etoposide", "type": "ChemicalEntity"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "embryonal carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p53-dependent", "type": "GeneOrGeneProduct"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ovarian serous carcinoma ( OSC ) is the most common and lethal histologic type of ovarian epithelial malignancy .

Example answer:
{"entities": [{"text": "Ovarian serous carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ovarian epithelial malignancy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The TP53 tumor-suppressor gene was mutated in all OSCs with documented NF1 mutation , suggesting that the pathways regulated by these two tumor-suppressor proteins often cooperate in the development of ovarian carcinomas with serous differentiation .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "tumor-suppressor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "ovarian carcinomas", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , characteristics of CEP55 expression and its clinical/prognostic significance are unclear in human epithelial ovarian carcinoma ( EOC ) .

## Item biored:test:1013
Example input:
Sentence: To determine whether c.609+28_610-16del allele-derived transcripts were subject to nonsense-mediated mRNA decay ( NMD ) , patient fibroblasts were incubated with the protein synthesis inhibitor anisomycin .

Example answer:
{"entities": [{"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "anisomycin", "type": "ChemicalEntity"}]}

Example input:
Sentence: EPO regulation of signal transduction factors was also interestingly complex .

Example answer:
{"entities": [{"text": "EPO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Emodin significantly downregulated the protein expression of FASN in HCT116 cells , which was caused by protein degradation due to elevated protein ubiquitination .

Example answer:
{"entities": [{"text": "Emodin", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "HCT116", "type": "CellLine"}]}

Example input:
Sentence: This instability possibly resulted in reduced expression levels of differentiation markers , such as keratin 1 and filaggrin , in the perineal epithelia .

Example answer:
{"entities": [{"text": "keratin 1", "type": "GeneOrGeneProduct"}, {"text": "filaggrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The heterozygous c.973G > A transition in exon 9 resulted in a substitution of lysine for glutamic acid at amino acid 325 ( E325K ) in the second calcium-binding EGF domain .

Example answer:
{"entities": [{"text": "c.973G > A", "type": "SequenceVariant"}, {"text": "lysine for glutamic acid at amino acid 325", "type": "SequenceVariant"}, {"text": "E325K", "type": "SequenceVariant"}, {"text": "calcium-binding", "type": "ChemicalEntity"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A mouse inflammatory cytokine and receptor RT2 profiler array was used to determine regulated transcripts in the urinary bladder of wild type ( WT ) and VIP ( -/- ) mice with or without CYP-induced cystitis ( 150 mg/kg ; i.p .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VIP", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CYP-induced", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We first identified the change of signaling pathways and differentially expressed proteins globally by removing CB in Tg mice using mass spectrometry and antibody microarray .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: STUDY DESIGN : Wild-type ( WT ) and superoxide dismutase 1 ( SOD1 ) -overexpressing day 8.75 embryos from nondiabetic WT control with SOD1 transgenic male and diabetic WT female with SOD1 transgenic male were analyzed for ER stress markers : C/EBP-homologous protein ( CHOP ) , calnexin , eukaryotic initiation factor 2a ( eIF2a ) , protein kinase ribonucleic acid ( RNA ) -like ER kinase ( PERK ) , binding immunoglobulin protein , protein disulfide isomerase family A member 3 , kinases inositol-requiring protein-1a ( IRE1a ) , and the X-box binding protein ( XBP1 ) messenger RNA ( mRNA ) splicing .

Example answer:
{"entities": [{"text": "superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C/EBP-homologous protein", "type": "GeneOrGeneProduct"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "eukaryotic initiation factor 2a", "type": "GeneOrGeneProduct"}, {"text": "eIF2a", "type": "GeneOrGeneProduct"}, {"text": "protein kinase ribonucleic acid ( RNA ) -like ER kinase", "type": "GeneOrGeneProduct"}, {"text": "PERK", "type": "GeneOrGeneProduct"}, {"text": "binding immunoglobulin protein", "type": "GeneOrGeneProduct"}, {"text": "protein disulfide isomerase family A member 3", "type": "GeneOrGeneProduct"}, {"text": "kinases inositol-requiring protein-1a", "type": "GeneOrGeneProduct"}, {"text": "IRE1a", "type": "GeneOrGeneProduct"}, {"text": "X-box binding protein", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In vivo protein synthesis was determined at this time and thereafter epididymal WAT ( eWAT ) was excised for analysis of signal transduction pathways central to controling protein synthesis and degradation .

## Item biored:test:953
Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We first identified the change of signaling pathways and differentially expressed proteins globally by removing CB in Tg mice using mass spectrometry and antibody microarray .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : We identified in ACC CD133-positive CSC that expressed NOTCH1 and SOX10 , formed spheroids , and initiated tumors in nude mice .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133-positive", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Double immunofluorescence analysis showed that the number of accumulated F4/80 ( + ) cells expressing TGF-b1 in metastatic areas was higher in WT than in AT1aKO .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: VEGF-stimulated hRMVEC proliferation was measured following transfection with NOX4 siRNA or STAT3 siRNA , or respective controls .

Example answer:
{"entities": [{"text": "VEGF-stimulated", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We modulated the b-catenin gene conditionally in endodermal epithelia by utilizing tamoxifen-inducible Cre driver line ( Shh ( CreERT2 ) ) .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "tamoxifen-inducible", "type": "ChemicalEntity"}, {"text": "Shh", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: EXPERIMENTAL DESIGN : To isolate CSC from ACC and characterize them , we used ROCK inhibitor-supplemented cell culture , immunomagnetic cell sorting , andin vitro/in vivoassays for CSC viability and tumorigenicity .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ROCK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Cell characteristics commonly associated with the CSC phenotype in vitro ( cell migration , invasion , anoikis resistance , mammosphere formation , ALDH activity , and expression of the CD44 and CD24 cell surface markers ) and in vivo ( tumor formation in mice using limiting dilution transplantation assays ) were evaluated .

Example answer:
{"entities": [{"text": "ALDH", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "CD24", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: METHODS : Isogenic CRC cell lines that differ in transgelin expression were characterized using in vitro assays of growth and invasiveness and a mouse tail vein assay of experimental metastasis .

## Item biored:test:986
Example input:
Sentence: To investigate this question , we have developed in vitro motility assays with purified DDB and BICD2 's membrane vesicle partner , the GTPase Rab6a .

Example answer:
{"entities": [{"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "GTPase Rab6a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Bach1 is an important transcriptional repressor that acts by modulating oxidative stress and represents a potential target in the treatment of pulmonary fibrosis ( PF ) .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "pulmonary fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Importantly , this is the first experimental evidence that removal of CB from amyloid precursor protein/presenilin transgenic mice aggravates AD pathogenesis , suggesting that CB has a critical role in AD pathogenesis .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "amyloid precursor", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: Bach1 siRNA attenuates bleomycin-induced pulmonary fibrosis by modulating oxidative stress in mice .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "bleomycin-induced", "type": "ChemicalEntity"}, {"text": "pulmonary fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The melanocortin system is crucial to regulation of energy homeostasis .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CBMCs were stimulated with innate ( Lipid A , LpA ; Peptidoglycan , Ppg ) , adaptive stimuli ( house dust mite Dermatophagoides pteronyssinus 1 , Derp1 ) or mitogen ( phytohemagglutinin , PHA ) .

Example answer:
{"entities": [{"text": "Lipid A", "type": "ChemicalEntity"}, {"text": "LpA", "type": "ChemicalEntity"}, {"text": "Peptidoglycan", "type": "ChemicalEntity"}, {"text": "Ppg", "type": "ChemicalEntity"}, {"text": "Dermatophagoides pteronyssinus 1", "type": "GeneOrGeneProduct"}, {"text": "Derp1", "type": "GeneOrGeneProduct"}, {"text": "phytohemagglutinin", "type": "ChemicalEntity"}, {"text": "PHA", "type": "ChemicalEntity"}]}

Example input:
Sentence: VDAC1 regulates mitochondrial uptake across the outer membrane and mitochondrial outer membrane permeabilization ( MOMP ) .

Example answer:
{"entities": [{"text": "VDAC1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: MOL1 is required for cambium homeostasis in Arabidopsis .

## Item biored:test:945
Example input:
Sentence: A multiple logistic regression analysis indicated that the odds ratio for EH in the -395A allele carriers as compared with the control group was 0.593 ( P=0.024 ) after adjusting for current traditional risk factors .

Example answer:
{"entities": [{"text": "EH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "-395A", "type": "SequenceVariant"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "ChemicalEntity"}, {"text": "CRF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ESRD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Meta-analysis of the two trials demonstrated a significant overall reduction in the composite end point in Hp 2-2 DM individuals with vitamin E ( odds ratio : 0.58 ; 95 % CI : 0.40-0.86 ; p = 0.006 ) .

Example answer:
{"entities": [{"text": "Hp", "type": "GeneOrGeneProduct"}, {"text": "DM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: In breast cancer patients , high levels of Star-PAP correlated with an improved prognosis .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The correlation between survival and NEK2 expression was analyzed in 359 patients with HCC using RNASeqV2 data available from The Cancer Genome Atlas ( TCGA ) website ( https : //tcga-data.nci.nih.gov/tcga/ ) .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A unique set of EPO-regulated survival factors included Lyl1 , Gas5 , Pim3 , Pim1 , Bim , Trib3 and Serpina 3g .

Example answer:
{"entities": [{"text": "EPO-regulated", "type": "GeneOrGeneProduct"}, {"text": "Lyl1", "type": "GeneOrGeneProduct"}, {"text": "Gas5", "type": "GeneOrGeneProduct"}, {"text": "Pim3", "type": "GeneOrGeneProduct"}, {"text": "Pim1", "type": "GeneOrGeneProduct"}, {"text": "Bim", "type": "GeneOrGeneProduct"}, {"text": "Trib3", "type": "GeneOrGeneProduct"}, {"text": "Serpina 3g", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Multivariate forward stepwise regression analysis for significant parameters showed that among the studied parameters CCL4 and CCL5 ( P=0.001 ) are diagnostic markers of HCC .

Example answer:
{"entities": [{"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Multivariate analysis implicated CEP55 as an independent prognostic indicator for EOC patients .
