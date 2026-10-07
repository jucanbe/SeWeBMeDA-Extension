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

## Item biored:test:921
Example input:
Sentence: This sole substitution was sufficient to confer constitutive activity to the receptor variant ( PrlR ( I146L ) ) , as assessed in three reconstituted cell models ( Ba/F3 , HEK293 and MCF-7 cells ) by Prl-independent ( i ) PrlR tyrosine phosphorylation , ( ii ) activation of signal transducer and activator of transcription 5 ( STAT5 ) signaling , ( iii ) transcriptional activity toward a Prl-responsive reporter gene , and ( iv ) cell proliferation and protection from cell death .

Example answer:
{"entities": [{"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "I146L", "type": "SequenceVariant"}, {"text": "Ba/F3", "type": "CellLine"}, {"text": "HEK293", "type": "CellLine"}, {"text": "MCF-7", "type": "CellLine"}, {"text": "Prl-independent", "type": "GeneOrGeneProduct"}, {"text": "signal transducer and activator of transcription 5", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "Prl-responsive", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: The coding sequences and flanking intron/UTR sequences of PDE6C and KCNV2 were screened for mutations by means of DHPLC and direct DNA sequencing of PCR-amplified genomic DNA .

Example answer:
{"entities": [{"text": "PDE6C", "type": "GeneOrGeneProduct"}, {"text": "KCNV2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: RESULTS : Quantitative PCR indicated that PPARa is well expressed in human liver and human liver slices and that the classical PPARa targets PLIN2 , VLDLR , ANGPTL4 , CPT1A and PDK4 are robustly induced by PPARa activation .

## Item biored:test:984
Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: PURPOSE : Genes in the complement pathway , including complement factor H ( CFH ) , C2/BF , and C3 , have been reported to be associated with age-related macular degeneration ( AMD ) .

Example answer:
{"entities": [{"text": "complement factor H", "type": "GeneOrGeneProduct"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2/BF", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}, {"text": "age-related macular degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: Serum levels of chemokines CCL4 and CCL5 in cirrhotic patients indicate the presence of hepatocellular carcinoma .

Example answer:
{"entities": [{"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "hepatocellular carcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Input:
Sentence: In two models of hepatic fibrogenesis , CCl4 treatment and bile duct ligation , hepatic mRNA levels of SAA1 and SAA3 were strongly increased .

## Item biored:test:1017
Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The melanocortin agonist melanotan II increased insulin-stimulated AKT phosphorylation in the rat hypothalamus in vivo .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "melanotan II", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: Furthermore , EPZ015666 restrained the phosphorylation of IkB kinaseb and IkBa , as well as nucleus transsituation of p65 as well as AKT in FLSs .

Example answer:
{"entities": [{"text": "EPZ015666", "type": "ChemicalEntity"}, {"text": "IkB kinaseb", "type": "GeneOrGeneProduct"}, {"text": "IkBa", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PKCalpha knockdown also resulted in decreased basal ERK phosphorylation and attenuated ERK activation following EGF stimulation .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Acidification , which slowed the reaction of CAA with thiol donors , could also attenuate effects of CAA on necrosis markers , thiol depletion and cysteine protease inhibition in living cells .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "thiol", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cysteine protease", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TIPE2 inhibited the phosphorylation of Akt , while promoting the phosphorylation of P38 , but had no effect on IkBa and ERK pathway .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "P38", "type": "GeneOrGeneProduct"}, {"text": "IkBa", "type": "GeneOrGeneProduct"}, {"text": "ERK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Focused transcriptomics revealed that myocyte-specific enhancer factor 2C ( MEF2C ) and myogenic factor 5 ( MYF5 ) expression was inhibited by high glucose levels , and endoribonuclease-prepared small interfering RNA-mediated combined inhibition of those transcription factors phenocopied the glycolytic shift that was observed in high glucose conditions .

Example answer:
{"entities": [{"text": "myocyte-specific enhancer factor 2C", "type": "GeneOrGeneProduct"}, {"text": "MEF2C", "type": "GeneOrGeneProduct"}, {"text": "myogenic factor 5", "type": "GeneOrGeneProduct"}, {"text": "MYF5", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Input:
Sentence: Alcohol also increased eEF2K phosphorylation and decreased eEF2 phosphorylation consistent with increased translation elongation .

## Item biored:test:923
Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: HAT subjects had increased anti-inflammatory genes TGFB1 , TIMP1 , TIMP3 , and TIMP4 while proinflammatory PIG7 and MMP2 were also significantly increased ; all genes , p < 0.025 .

Example answer:
{"entities": [{"text": "TGFB1", "type": "GeneOrGeneProduct"}, {"text": "TIMP1", "type": "GeneOrGeneProduct"}, {"text": "TIMP3", "type": "GeneOrGeneProduct"}, {"text": "TIMP4", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PIG7", "type": "GeneOrGeneProduct"}, {"text": "MMP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Polymorphisms in TBX21 and HLX1 influenced primarily IL-5 and IL-13 secretion after LpA-stimulation in cord blood suggesting that genetic variations in the transcription factors essential for the T ( H ) 1-pathway may contribute to modified T ( H ) 2-immune responses already early in life .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Many genes induced by PPARa activation were involved in lipid metabolism ( ACSL5 , AGPAT9 , FADS1 , SLC27A4 ) , xenobiotic metabolism ( POR , ABCC2 , CYP3A5 ) or the unfolded protein response , whereas most of the downregulated genes were involved in immune-related pathways .

## Item biored:test:1061
Example input:
Sentence: In univariate analysis , the OR for the C4A deletion was 1.38 , p = 0.075 , but after simultaneous adjustment for the other four SNPs the odds ratio was 1.01 , p = 0.98 .

Example answer:
{"entities": [{"text": "C4A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further age stratification showed significant genotypic as well as allelic association in the group of over 40 years ( genotypic : p value = 0.035 , odds ratio = 1.617 with 95 % CI = 1.033-2.529 ; allelic : p value = 0.033 , odds ratio = 1.445 with 95 % CI = 1.029-2.029 ) .

Example answer:
{"entities": []}

Example input:
Sentence: On an intention-to-treat basis , 55 % of the patients achieved at least partial response , including 19 % CR and 35 % achieved at least very good partial response .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Peak two point LOD scores of 3.5 , 4.7 , and 5.3 were found co-incident with consecutive markers D13S154 , DCT , and D13S1280 .

Example answer:
{"entities": [{"text": "DCT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Odds ratios and 95 % confidence intervals for cancer risk by MLH1 -93 polymorphism status , and stratified by previous exposure to methylating chemotherapy , were calculated using unconditional logistic regression .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We used conditional logistic regression to estimate OR and 95 % confidence intervals ( CI ) .

Example answer:
{"entities": []}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: These 2 SNPs had a false discovery rate for multitest correction of < 0.05 , and therefore a > 95 % probability of being considered as proven .

Example answer:
{"entities": []}

Example input:
Sentence: We have observed complete concordance between methods .

Example answer:
{"entities": []}

Input:
Sentence: The overall concordance rate , positive predictive value , and negative predictive value were 98.3 % ( 178/181 ) , 90.9 % ( 10/11 ) , and 98.8 % ( 168/170 ) , respectively .

## Item biored:test:1005
Example input:
Sentence: RESULTS : We identified in ACC CD133-positive CSC that expressed NOTCH1 and SOX10 , formed spheroids , and initiated tumors in nude mice .

Example answer:
{"entities": [{"text": "ACC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD133-positive", "type": "GeneOrGeneProduct"}, {"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The phosphatidylethanolamine N-methyltransferase gene V175M single nucleotide polymorphism confers the susceptibility to NASH in Japanese population .

Example answer:
{"entities": [{"text": "phosphatidylethanolamine N-methyltransferase", "type": "GeneOrGeneProduct"}, {"text": "V175M", "type": "SequenceVariant"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among NASH patients , body mass index was significantly lower ( p < 0.05 ) , and non-obese patients were significantly more frequent ( p < 0.001 ) in carriers of Val175Met variant than in homozygotes of wild type PEMT .

Example answer:
{"entities": [{"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Val175Met", "type": "SequenceVariant"}, {"text": "PEMT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: To determine the pathogenic importance of CB depletions in AD models , we crossed 5 familial AD mutations ( 5XFAD ; Tg ) mice with CB knock-out ( CBKO ) mice and generated a novel line CBKO.5XFAD ( CBKOTg ) mice .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "CBKO", "type": "GeneOrGeneProduct"}, {"text": "CBKO.5XFAD", "type": "GeneOrGeneProduct"}, {"text": "CBKOTg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , the abundance and proliferative index of lymph node , thymus and CNS CD4 ( + ) CD25 ( + ) FoxP3 ( + ) Tregs were strikingly reduced in VPAC2-deficient mice with EAE .

Example answer:
{"entities": [{"text": "CD4", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "FoxP3", "type": "GeneOrGeneProduct"}, {"text": "VPAC2-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: TSPO was up-regulated in Iba1 ( + ) cells from brains of patients with ICH and in CD11b ( + ) CD45 ( int ) cells from mice subjected to collagenase-induced ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "Iba1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD11b", "type": "GeneOrGeneProduct"}, {"text": "CD45", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "collagenase-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: We revealed the changes in murine HSC fate control orchestrated by the expression of GADD45A at single cell resolution .

Example answer:
{"entities": [{"text": "murine", "type": "OrganismTaxon"}, {"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND/AIMS : The genetic predisposition on the development of nonalcoholic steatohepatitis ( NASH ) has been poorly understood .

Example answer:
{"entities": [{"text": "nonalcoholic steatohepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Unexpectedly , histological analysis revealed significantly increased levels of immune foci present in livers of 11b-HSD1KO but not LKO or control mice , suggestive of a transition to NASH .

## Item biored:test:959
Example input:
Sentence: The MLH1 -93 variant allele was also over-represented in t-AML cases when compared to de novo AML cases ( 36.9 % , n = 420 ) and healthy controls ( 36.3 % , n = 952 ) , and was associated with a significantly increased risk of developing t-AML ( odds ratio 5.31 , 95 % confidence interval 1.40 to 20.15 ) , but only in patients previously treated with a methylating agent .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "AML", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Importantly , fibroblasts carrying the mutation showed twofold increase in proliferation rate associated with hyperphosphorylation of Smad1/5/8 .

Example answer:
{"entities": [{"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Dex increased SBP ( 110 +/- 2-126 +/- 3 mmHg ; P < 0.001 ) and decreased thymus ( P < 0.001 ) and bodyweights ( P '' < 0.01 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: These findings suggest that NRG-1 beta enhances MPNST migration and that NRG-1 beta and NRG-1 alpha differentially modulate this process .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "ChemicalEntity"}, {"text": "LAM-resistant", "type": "ChemicalEntity"}, {"text": "HBV", "type": "OrganismTaxon"}, {"text": "PC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Input:
Sentence: Changes included increases in HOOK1 , SDCCAG8 , ENAH/Mena , and TNS1 and decreases in EMB , BCL11B , and PTPRD .

## Item biored:test:980
Example input:
Sentence: Also , BCNU administration increased serum tumor necrosis factor-alpha ( TNFalpha ) , hippocampal MT and malondialdehyde ( MDA ) contents as well as caspase-3 activity in addition to histological alterations .

Example answer:
{"entities": [{"text": "BCNU", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , using RNA interference with small inhibitory RNAs for Sp1 , Sp3 , and Sp4 , we observed that curcumin-dependent inhibition of nuclear factor kappaB ( NF-kappaB ) -dependent genes , such as bcl-2 , survivin , and cyclin D1 , was also due , in part , to loss of Sp proteins .

Example answer:
{"entities": [{"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "curcumin-dependent", "type": "ChemicalEntity"}, {"text": "nuclear factor kappaB", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "survivin", "type": "GeneOrGeneProduct"}, {"text": "cyclin D1", "type": "GeneOrGeneProduct"}, {"text": "Sp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: 9 ( 2006 ) , 917 ] recently identified the microglial-specific fractalkine receptor ( CX3CR1 ) as an important mediator of MPTP-induced neurodegeneration of DA neurons .

Example answer:
{"entities": [{"text": "fractalkine receptor", "type": "GeneOrGeneProduct"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "MPTP-induced", "type": "ChemicalEntity"}, {"text": "neurodegeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DA", "type": "ChemicalEntity"}]}

Example input:
Sentence: In Mz-ChA-1 cells stimulated with ( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide ( RAMH ) , we measured ( a ) cell growth , ( b ) IP ( 3 ) and cyclic AMP levels , and ( c ) phosphorylation of PKC and mitogen-activated protein kinase isoforms .

Example answer:
{"entities": [{"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide", "type": "ChemicalEntity"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistent with these in vitro data , expression levels of the ER stress markers 78-kDa glucose-regulated protein and CCAAT/enhancer-binding protein homologous protein , as well as that of the RA marker glial fibrillary acidic protein were increased in APP/PS1 AD mouse model .

Example answer:
{"entities": [{"text": "78-kDa glucose-regulated protein", "type": "GeneOrGeneProduct"}, {"text": "CCAAT/enhancer-binding protein homologous protein", "type": "GeneOrGeneProduct"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Importantly , this is the first experimental evidence that removal of CB from amyloid precursor protein/presenilin transgenic mice aggravates AD pathogenesis , suggesting that CB has a critical role in AD pathogenesis .

Example answer:
{"entities": [{"text": "CB", "type": "GeneOrGeneProduct"}, {"text": "amyloid precursor", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Furthermore , the MLFs infected with Bach1 siRNA exhibited increased mRNA and protein expression levels of heme oxygenase-1 and glutathione peroxidase 1 , but decreased levels of TGF-b1 and interleukin-6 in the cell supernatants compared with the cells exposed to TGF-b1 alone .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "heme oxygenase-1", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase 1", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "interleukin-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Serum amyloid A induced the transcription of MCP-1 , RANTES and MMP9 in an NF-kappaB- and JNK-dependent manner .

## Item biored:test:1000
Example input:
Sentence: The mutant receptor hGRalphaD401H did not exert a dominant positive or negative effect upon the wild-type receptor , it preserved its ability to bind to glucocorticoid response elements , and displayed a normal interaction with the glucocorticoid receptor-interacting protein 1 coactivator .

Example answer:
{"entities": [{"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid", "type": "ChemicalEntity"}, {"text": "glucocorticoid receptor-interacting protein 1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: His liver was cirrhotic with parenchymal iron deposits and the result of a glucose tolerance test was compatible with diabetes mellitus .

Example answer:
{"entities": [{"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "iron", "type": "ChemicalEntity"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "diabetes mellitus", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: METHODS-RESULTS : Compared with the wild-type hGRalpha , the mutant receptor hGRalphaD401H demonstrated a 2.4-fold increase in its ability to transactivate the glucocorticoid-inducible mouse mammary tumor virus promoter in response to dexamethasone but had similar affinity for the ligand ( dissociation constant = 6.2 +/- 0.6 vs. 6.1 +/- 0.6 nm ) and time to nuclear translocation ( 14.75 +/- 0.25 vs. 14.25 +/- 1.13 min ) .

Example answer:
{"entities": [{"text": "hGRalpha", "type": "GeneOrGeneProduct"}, {"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid-inducible", "type": "ChemicalEntity"}, {"text": "mouse mammary tumor virus", "type": "OrganismTaxon"}, {"text": "dexamethasone", "type": "ChemicalEntity"}]}

Example input:
Sentence: A novel point mutation in the amino terminal domain of the human glucocorticoid receptor ( hGR ) gene enhancing hGR-mediated gene expression .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "hGR", "type": "GeneOrGeneProduct"}, {"text": "hGR-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Glucocorticoid-induced hypertension ( GC-HT ) in the rat is associated with nitric oxide-redox imbalance .

Example answer:
{"entities": [{"text": "Glucocorticoid-induced", "type": "ChemicalEntity"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GC-HT", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "nitric", "type": "ChemicalEntity"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cocaine", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "glutathione peroxidase", "type": "GeneOrGeneProduct"}, {"text": "nNOS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: A novel point mutation in helix 10 of the human glucocorticoid receptor causes generalized glucocorticoid resistance by disrupting the structure of the ligand-binding domain .

Example answer:
{"entities": [{"text": "human", "type": "OrganismTaxon"}, {"text": "glucocorticoid receptor", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid resistance", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The mutant receptor hGRalphaD401H enhances the transcriptional activity of glucocorticoid-responsive genes .

Example answer:
{"entities": [{"text": "hGRalphaD401H", "type": "GeneOrGeneProduct"}, {"text": "glucocorticoid-responsive genes", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Glucocorticoids can be reactivated in liver through 11b-hydroxysteroid dehydrogenase type 1 ( 11b-HSD1 ) enzyme activity .

## Item biored:test:1026
Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In vitro , the Vps2/Vps24 subunits of ESCRT-III formed side-by-side filaments with Snf7 and inhibited further polymerization , but the growth inhibition was alleviated by the addition of Vps4 and ATP .

Example answer:
{"entities": [{"text": "Vps2/Vps24", "type": "GeneOrGeneProduct"}, {"text": "ESCRT-III", "type": "GeneOrGeneProduct"}, {"text": "Snf7", "type": "GeneOrGeneProduct"}, {"text": "Vps4", "type": "GeneOrGeneProduct"}, {"text": "ATP", "type": "ChemicalEntity"}]}

Example input:
Sentence: Silencing OCT4A suppresses p21Cip1 , changes cell cycle regulation and subsequently suppresses terminal senescence ; p21Cip1-silencing did not affect OCT4A expression or cellular phenotype .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1-silencing", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Moreover , using RNA interference with small inhibitory RNAs for Sp1 , Sp3 , and Sp4 , we observed that curcumin-dependent inhibition of nuclear factor kappaB ( NF-kappaB ) -dependent genes , such as bcl-2 , survivin , and cyclin D1 , was also due , in part , to loss of Sp proteins .

Example answer:
{"entities": [{"text": "Sp1", "type": "GeneOrGeneProduct"}, {"text": "Sp3", "type": "GeneOrGeneProduct"}, {"text": "Sp4", "type": "GeneOrGeneProduct"}, {"text": "curcumin-dependent", "type": "ChemicalEntity"}, {"text": "nuclear factor kappaB", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "survivin", "type": "GeneOrGeneProduct"}, {"text": "cyclin D1", "type": "GeneOrGeneProduct"}, {"text": "Sp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , LKB1 deletion enhanced mouse retinal and cell angiogenesis , and knockdown of VEGF by small-interfering RNA decreased endothelial cell proliferation and migration .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: In this study , we knocked down Bach1 using adenovirus-mediated small interfering RNA ( siRNA ) to determine whether the use of Bach1 siRNA is an effective therapeutic strategy in mice with bleomycin ( BLM ) -induced PF .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "bleomycin", "type": "ChemicalEntity"}, {"text": "BLM", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the absence of functional phosphatase and tensin homolog ( PTEN ) protein in Ishikawa cells , PKCalpha knockdown reduced Akt phosphorylation at serine 473 and concomitantly inhibited phosphorylation of the Akt target , glycogen synthase kinase-3beta ( GSK-3beta ) .

Example answer:
{"entities": [{"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "glycogen synthase kinase-3beta", "type": "GeneOrGeneProduct"}, {"text": "GSK-3beta", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We found that depletion of PI4KIIa and PI4KIIb using small interfering RNA led to actin remodeling .

## Item biored:test:1036
Example input:
Sentence: Thus , metabolic symbiosis is established in the face of angiogenesis inhibition , whereby hypoxic cancer cells import glucose and export lactate , while normoxic cells import and catabolize lactate .

Example answer:
{"entities": [{"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Top canonical pathways identified by Ingenuity Pathway Analysis ( IPA ) included `` Clathrin-mediated Endocytosis Signaling '' ( p = 5.14x10-4 ) , `` Virus Entry via Endocytic Pathways '' ( p = 6.15x 10-4 ) , and `` High Mobility Group-Box 1 ( HMGB1 ) Signaling '' ( p = 6.15x10-4 ) .

Example answer:
{"entities": [{"text": "Clathrin-mediated", "type": "GeneOrGeneProduct"}, {"text": "High Mobility Group-Box 1", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There is considerable interest in identifying the molecular mechanisms that relate early-life iAs exposure to the development of these latent diseases , particularly in relationship to cancer .

Example answer:
{"entities": [{"text": "iAs", "type": "ChemicalEntity"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Defect in androgen action on the target tissues or production of active metabolite share common morphological features .

Example answer:
{"entities": []}

Example input:
Sentence: This molecular study reveals a naturally occurring mechanism where the effect of either modifier genes or epigenetic factors could be suspected .

Example answer:
{"entities": []}

Example input:
Sentence: We hypothesized that activin and/or GnRH pathways may be modulated by BMP-4 , but neither the activin-stimulated phosphorylation of Smad2/3 nor the GnRH-induced ERK1/2 or cAMP response element-binding phosphorylation were modified .

Example answer:
{"entities": [{"text": "activin", "type": "GeneOrGeneProduct"}, {"text": "GnRH", "type": "GeneOrGeneProduct"}, {"text": "BMP-4", "type": "GeneOrGeneProduct"}, {"text": "activin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "Smad2/3", "type": "GeneOrGeneProduct"}, {"text": "GnRH-induced", "type": "GeneOrGeneProduct"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The present study investigated whether this effect of estrogen involves interaction with alpha2- and/or I1-receptors .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "alpha2- and/or I1-receptors", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These findings suggest that estrogen downregulates alpha2- but not I1-receptor-mediated hypotension and highlight a role for the cardiac autonomic control in alpha-methyldopa-estrogen interaction .

Example answer:
{"entities": [{"text": "estrogen", "type": "ChemicalEntity"}, {"text": "alpha2- but not", "type": "GeneOrGeneProduct"}, {"text": "hypotension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-methyldopa-estrogen", "type": "ChemicalEntity"}]}

Example input:
Sentence: Although the underlying mechanism ( s ) are not well understood , these effects may involve an increase in acetylcholine ( ACh ) levels .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "ChemicalEntity"}, {"text": "ACh", "type": "ChemicalEntity"}]}

Input:
Sentence: Little is known regarding the mechanism , although it is assumed that acetaldehyde or estrogen mediated pathways play a role .

## Item biored:test:1053
Example input:
Sentence: Knockdown of either NOX4 or STAT3 inhibited VEGF-induced EC proliferation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Knockdowns of NOTCH1 , SOX10 , and their common effector FABP7 had negative effects on each other , inhibited spheroidogenesis , and induced cell death pointing at their essential roles in CSC maintenance .

Example answer:
{"entities": [{"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "FABP7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: NDP-MSH time- and dose-dependently inhibited IRS-1 ( ser307 ) phosphorylation , effects also reversed by a specific melanocortin receptor antagonist .

Example answer:
{"entities": [{"text": "NDP-MSH", "type": "ChemicalEntity"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}, {"text": "melanocortin receptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Silencing of PKCalpha prevented RAMH inhibition of Mz-ChA-1 cell growth and ablated RAMH effects on ERK1/2 phosphorylation .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Immunohistochemistry showed that CBKOTg mice had significant neuronal loss in the subiculum area without changing the magnitude ( number ) of amyloid b-peptide ( Ab ) plaques deposition and elicited significant apoptotic features and mitochondrial dysfunction compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "neuronal loss", "type": "DiseaseOrPhenotypicFeature"}, {"text": "amyloid b-peptide", "type": "GeneOrGeneProduct"}, {"text": "Ab", "type": "GeneOrGeneProduct"}, {"text": "mitochondrial dysfunction", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunohistochemical analysis revealed that coenzyme Q10 significantly decreased the cisplatin-induced overexpression of inducible nitric oxide synthase , nuclear factor-kappaB , caspase-3 and p53 in renal tissue .

Example answer:
{"entities": [{"text": "coenzyme Q10", "type": "ChemicalEntity"}, {"text": "cisplatin-induced", "type": "ChemicalEntity"}, {"text": "nitric oxide synthase", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor-kappaB", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Upon division , Dpp signaling is extinguished , and Nos is downregulated in one daughter cell , causing it to switch to a differentiating cystoblast ( CB ) .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Unexpectedly , blocking CenpH did not affect spindle organization and meiotic cell cycle progression after germinal vesicle breakdown .

## Item biored:test:981
Example input:
Sentence: Knockdowns of NOTCH1 , SOX10 , and their common effector FABP7 had negative effects on each other , inhibited spheroidogenesis , and induced cell death pointing at their essential roles in CSC maintenance .

Example answer:
{"entities": [{"text": "NOTCH1", "type": "GeneOrGeneProduct"}, {"text": "SOX10", "type": "GeneOrGeneProduct"}, {"text": "FABP7", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: ZnSO ( 4 ) pretreatment counteracted BCNU-induced inhibition of GR and depletion of GSH and resulted in significant reduction in the levels of MDA and TNFalpha as well as the activity of caspase-3 .

Example answer:
{"entities": [{"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}, {"text": "BCNU-induced", "type": "ChemicalEntity"}, {"text": "GR", "type": "GeneOrGeneProduct"}, {"text": "GSH", "type": "ChemicalEntity"}, {"text": "MDA", "type": "ChemicalEntity"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A sublethal dose of Smac mimetic BV6 induces cIAP1 and cIAP2 degradation to increase tumor cell sensitivity to radiation-induced cell death in vitro and to enhance radiation-mediated suppression of STS xenografts in vivo .

Example answer:
{"entities": [{"text": "Smac", "type": "GeneOrGeneProduct"}, {"text": "BV6", "type": "ChemicalEntity"}, {"text": "cIAP1", "type": "GeneOrGeneProduct"}, {"text": "cIAP2", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal treatment significantly decreases the release of inflammatory cytokines and inhibits the TLR4/NF-kappaB and MAPK signaling pathways .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4/NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These data indicate that genotoxic stress-induced GADD45A expression in HSCs prevents their fatal transformation by directing them into differentiation and thereby clearing them from the system .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Growth arrest and DNA-damage-inducible 45 alpha ( GADD45A ) is induced by genotoxic stress in HSCs .

Example answer:
{"entities": [{"text": "Growth arrest and DNA-damage-inducible 45 alpha", "type": "GeneOrGeneProduct"}, {"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast to other cellular systems , GADD45A expression did not cause a cell cycle arrest or an alteration in the decision between cell survival and apoptosis in HSCs .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Blockade of NF-kappaB revealed cytotoxic effects of SAA in primary HSCs with signs of apoptosis such as caspase 3 and PARP cleavage and Annexin V staining .

## Item biored:test:1035
Example input:
Sentence: BACKGROUND : ADAM12 is upregulated in human breast cancers and is a predictor of chemoresistance in estrogen receptor-negative tumors .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "breast cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "estrogen", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Study-specific associations of 68 single nucleotide polymorphisms ( SNPs ) in 8 alcohol-metabolising genes ( Alcohol Dehydrogenases ( ADHs ) and Aldehyde Dehydrogenases ( ALDHs ) ) with prostate cancer diagnosis and prostate cancer-specific mortality , by grade , were assessed using logistic and Cox regression models , respectively .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "Alcohol Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ADHs", "type": "GeneOrGeneProduct"}, {"text": "Aldehyde Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ALDHs", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we investigated the associations of genetic variants in alcohol-metabolising genes with prostate cancer incidence and survival .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Because intensity of alcohol consumption is associated with poorer fetal outcomes , separate analyses were conducted for the heavy ( average of > or=5 drinks per drinking day ) alcohol consumers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Breast cancer accounts for 30-40 % of all deaths from cancers in females .

Example answer:
{"entities": [{"text": "Breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effects of alcohol consumption on prostate cancer incidence and survival remain unclear , potentially due to methodological limitations of observational studies .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that alcohol consumption is unlikely to affect prostate cancer incidence , but it may influence disease progression .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alcohol consumption and prostate cancer incidence and progression : A Mendelian randomisation study .

Example answer:
{"entities": [{"text": "Alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Alcohol consumption is a risk factor for breast cancer .

## Item biored:test:1009
Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: In developed countries , thiamine deficiency ( TD ) is most often manifested following chronic alcohol consumption leading to impaired mitochondrial function , oxidative stress , inflammation and excitotoxicity .

Example answer:
{"entities": [{"text": "thiamine deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alcohol", "type": "ChemicalEntity"}, {"text": "impaired mitochondrial function", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "excitotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : Erythropoietin ( Epo ) exerts direct effects on white adipose tissue ( WAT ) in mice in addition to its erythropoietic effects , and in humans Epo increases resting energy expenditure and affect serum lipid levels , but direct effects of Epo in human WAT have not been documented .

Example answer:
{"entities": [{"text": "Erythropoietin", "type": "GeneOrGeneProduct"}, {"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Taken together , the profile of C5L2 receptor , ASP gene expression and metabolic factors in adipose tissue from morbidly obese HAT subjects suggests a compensatory response associated with the increased plasma ASP and TG .

Example answer:
{"entities": [{"text": "C5L2", "type": "GeneOrGeneProduct"}, {"text": "ASP", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TG", "type": "ChemicalEntity"}]}

Example input:
Sentence: Instead , ETO-induced OCT4A was concomitant with activation of AMPK , a key component of metabolic stress and autophagy regulation .

Example answer:
{"entities": [{"text": "ETO-induced", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Decreased Whole-Body Fat Mass Produced by Chronic Alcohol Consumption is Associated with Activation of S6K1-Mediated Protein Synthesis and Increased Autophagy in Epididymal White Adipose Tissue .

## Item biored:test:881
Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Taken together , our results demonstrated that Sag is a Kras ( G12D ) -cooperating oncogene required for Kras ( G12D ) -induced immortalization and transformation , and targeting SAG-SCF E3 ligase may , therefore , have therapeutic value for senescence-based cancer treatment .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "SAG-SCF", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In hRMVECs transfected with NOX4 siRNA and treated with VEGF or control , 1 ) ROS generation was measured using the 5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester fluorescence assay and 2 ) phosphorylated VEGF receptor 2 and STAT3 , and total VEGFR2 and STAT3 were measured in western blot analyses .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}, {"text": "5- ( and-6 ) -chloromethyl-2',7'-dichlorodihydrofluorescein diacetate , acetyl ester", "type": "ChemicalEntity"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}, {"text": "VEGFR2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SB 202190 significantly decreased IDO expression induced by Tat , and this effect was accompanied by a reduction of Tat-induced expression of TNFa , IL-6 , iNOS and SERT .

Example answer:
{"entities": [{"text": "SB 202190", "type": "ChemicalEntity"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "Tat-induced", "type": "GeneOrGeneProduct"}, {"text": "TNFa", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "iNOS", "type": "GeneOrGeneProduct"}, {"text": "SERT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : SELP and IRAK1 were identified as novel SLE-associated genes with a high degree of significance , suggesting new directions in understanding the pathogenesis of SLE .

Example answer:
{"entities": [{"text": "SELP", "type": "GeneOrGeneProduct"}, {"text": "IRAK1", "type": "GeneOrGeneProduct"}, {"text": "SLE-associated", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CSF-1 significantly promoted IL-3-driven CD11c+ cell expansion and dampened basophil and mast cell generation from C57BL/6 bone marrow .

Example answer:
{"entities": [{"text": "CSF-1", "type": "GeneOrGeneProduct"}, {"text": "IL-3-driven", "type": "GeneOrGeneProduct"}, {"text": "CD11c+", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: When the patients were stratified by the SE , the rs729302 A allele was found to confer increased risk to RA in patients that were SE negative ( OR 1.50 , 95 % CI 1.17 to 1.92 , p = 0.001 ) as compared with patients carrying the SE ( OR 1.11 , 95 % CI 0.93 to 1.33 , p = 0.24 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "rs729302", "type": "SequenceVariant"}, {"text": "RA", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS AND DISCUSSION : RSV-infected A549 and SAE cells release a network of cytokines , including newly identified RSV-inducible cytokines LIF , migration inhibitory factor ( MIF ) , stem cell factor ( SCF ) , CCL27 , CXCL12 and stem cell growth factor beta ( SCGF-b ) .

## Item biored:test:1015
Example input:
Sentence: The melanocortin agonist melanotan II increased insulin-stimulated AKT phosphorylation in the rat hypothalamus in vivo .

Example answer:
{"entities": [{"text": "melanocortin", "type": "GeneOrGeneProduct"}, {"text": "melanotan II", "type": "ChemicalEntity"}, {"text": "insulin-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Example input:
Sentence: Furthermore , EPZ015666 restrained the phosphorylation of IkB kinaseb and IkBa , as well as nucleus transsituation of p65 as well as AKT in FLSs .

Example answer:
{"entities": [{"text": "EPZ015666", "type": "ChemicalEntity"}, {"text": "IkB kinaseb", "type": "GeneOrGeneProduct"}, {"text": "IkBa", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PA-1 cells treated with ETO display highly heterogeneous increases in OCT4A and p21Cip1 indicative of dis-adaptation catastrophe .

Example answer:
{"entities": [{"text": "PA-1", "type": "CellLine"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Certain concepts concerning EPO/EPOR action modes have been challenged by in vivo studies : Bcl-x levels are elevated in maturing erythroblasts , but not in their progenitors ; truncated EPOR alleles that lack a major p85/PI3K recruitment site nonetheless promote polycythemia ; and Erk1 disruption unexpectedly bolsters erythropoiesis .

Example answer:
{"entities": [{"text": "EPO/EPOR", "type": "GeneOrGeneProduct"}, {"text": "Bcl-x", "type": "GeneOrGeneProduct"}, {"text": "EPOR", "type": "GeneOrGeneProduct"}, {"text": "p85/PI3K", "type": "GeneOrGeneProduct"}, {"text": "polycythemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Erk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Despite the absence of functional phosphatase and tensin homolog ( PTEN ) protein in Ishikawa cells , PKCalpha knockdown reduced Akt phosphorylation at serine 473 and concomitantly inhibited phosphorylation of the Akt target , glycogen synthase kinase-3beta ( GSK-3beta ) .

Example answer:
{"entities": [{"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "glycogen synthase kinase-3beta", "type": "GeneOrGeneProduct"}, {"text": "GSK-3beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TIPE2 inhibited the phosphorylation of Akt , while promoting the phosphorylation of P38 , but had no effect on IkBa and ERK pathway .

Example answer:
{"entities": [{"text": "TIPE2", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "P38", "type": "GeneOrGeneProduct"}, {"text": "IkBa", "type": "GeneOrGeneProduct"}, {"text": "ERK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The binding of mTOR , PRAS40 and RagC to raptor did not differ for control and septic muscle in the basal condition ; however , the Leu-induced decrease in PRAS40 raptor and increase in RagC raptor seen in control muscle was absent in sepsis .

Example answer:
{"entities": [{"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "PRAS40", "type": "GeneOrGeneProduct"}, {"text": "RagC", "type": "GeneOrGeneProduct"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "Leu-induced", "type": "ChemicalEntity"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A potential downstream signaling pathway involving phosphatidylinositol 3-kinase ( PI3K ) /threonine protein kinase B ( Akt ) /mammalian target of rapamycin ( mTOR ) was identifiedby western blot analysis .

Example answer:
{"entities": [{"text": "phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "target of rapamycin", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Importantly , fibroblasts carrying the mutation showed twofold increase in proliferation rate associated with hyperphosphorylation of Smad1/5/8 .

Example answer:
{"entities": [{"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This increase was not associated with a change in mTOR , 4E-BP1 , Akt , or PRAS40 phosphorylation .

## Item biored:test:1027
Example input:
Sentence: Mouse lung fibroblasts ( MLFs ) were incubated with transforming growth factor ( TGF ) -b1 ( 5 ng/ml ) and subsequently infected with recombined adenovirus-like Bach1 siRNA1 and Bach1 siRNA2 , while an empty adenovirus vector was used as the negative control .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "transforming growth factor ( TGF ) -b1", "type": "GeneOrGeneProduct"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To investigate this question , we have developed in vitro motility assays with purified DDB and BICD2 's membrane vesicle partner , the GTPase Rab6a .

Example answer:
{"entities": [{"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "GTPase Rab6a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TSPO was up-regulated in Iba1 ( + ) cells from brains of patients with ICH and in CD11b ( + ) CD45 ( int ) cells from mice subjected to collagenase-induced ICH .

Example answer:
{"entities": [{"text": "TSPO", "type": "GeneOrGeneProduct"}, {"text": "Iba1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CD11b", "type": "GeneOrGeneProduct"}, {"text": "CD45", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "collagenase-induced", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Exaggerated expression of inflammatory mediators in vasoactive intestinal polypeptide knockout ( VIP-/- ) mice with cyclophosphamide ( CYP ) -induced cystitis .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "vasoactive intestinal polypeptide", "type": "GeneOrGeneProduct"}, {"text": "VIP-/-", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "cyclophosphamide", "type": "ChemicalEntity"}, {"text": "CYP", "type": "ChemicalEntity"}, {"text": "cystitis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Matrix metalloproteinases ( MMPs ) are involved in the degradation of the extracellular matrix of the intervertebral disc .

Example answer:
{"entities": [{"text": "Matrix metalloproteinases", "type": "GeneOrGeneProduct"}, {"text": "MMPs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Depletion of PI4KIIb also induced the formation of invadopodia containing membrane type I matrix metalloproteinase ( MT1-MMP ) .

## Item biored:test:1046
Example input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

Example answer:
{"entities": [{"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VAL/HCTZ", "type": "ChemicalEntity"}, {"text": "HCTZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: At pH 9 , a higher rate of etodolac release from ED was observed as compared to aqueous buffer of pH 7.4 and 80 % human plasma ( pH 7.4 ) , following first-order kinetics .

Example answer:
{"entities": [{"text": "etodolac", "type": "ChemicalEntity"}, {"text": "ED", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: The increase of galactose concentration in the cerebrospinal fluid was several times lower after oral than after parenteral administration of the same galactose dose .

Example answer:
{"entities": [{"text": "galactose", "type": "ChemicalEntity"}]}

Example input:
Sentence: BACKGROUND : More than 3 decades after Jones and Smith ( 1973 ) reported on the devastation caused by alcohol exposure on fetal development , the rates of heavy drinking during pregnancy remain relatively unchanged .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: In developed countries , thiamine deficiency ( TD ) is most often manifested following chronic alcohol consumption leading to impaired mitochondrial function , oxidative stress , inflammation and excitotoxicity .

Example answer:
{"entities": [{"text": "thiamine deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alcohol", "type": "ChemicalEntity"}, {"text": "impaired mitochondrial function", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "excitotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : The effects of 2,3,7,8-tetrachlorodibenzo-p-dioxin and related dioxin-like chemicals are mediated through binding-dependent activation of the cytosolic aryl hydrocarbon receptor ( AHR ) .

Example answer:
{"entities": [{"text": "2,3,7,8-tetrachlorodibenzo-p-dioxin", "type": "ChemicalEntity"}, {"text": "dioxin-like", "type": "ChemicalEntity"}, {"text": "aryl hydrocarbon receptor", "type": "GeneOrGeneProduct"}, {"text": "AHR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Although the underlying mechanism ( s ) are not well understood , these effects may involve an increase in acetylcholine ( ACh ) levels .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "ChemicalEntity"}, {"text": "ACh", "type": "ChemicalEntity"}]}

Example input:
Sentence: Chloroacetaldehyde ( CAA ) is a metabolite of the alkylating agent ifosfamide ( IFO ) and putatively responsible for renal damage following anti-tumor therapy with IFO .

Example answer:
{"entities": [{"text": "Chloroacetaldehyde", "type": "ChemicalEntity"}, {"text": "CAA", "type": "ChemicalEntity"}, {"text": "alkylating agent", "type": "ChemicalEntity"}, {"text": "ifosfamide", "type": "ChemicalEntity"}, {"text": "IFO", "type": "ChemicalEntity"}, {"text": "renal damage", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Malondialdehyde level in BCNU-exposed group was higher than those in control groups and melatonin decreased malondialdehyde levels in BCNU group ( P < 0.01 ) , while there were no significant differences in the superoxide dismutase levels between these groups .

Example answer:
{"entities": [{"text": "Malondialdehyde", "type": "ChemicalEntity"}, {"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "melatonin", "type": "ChemicalEntity"}, {"text": "malondialdehyde", "type": "ChemicalEntity"}, {"text": "BCNU", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Early identification of fetal alcohol exposure and maternal abstinence led to better infant outcomes .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Input:
Sentence: Exposure to acetaldehyde resulted in little or no effect comparable to that of ethanol .

## Item biored:test:1041
Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , the MLFs infected with Bach1 siRNA exhibited increased mRNA and protein expression levels of heme oxygenase-1 and glutathione peroxidase 1 , but decreased levels of TGF-b1 and interleukin-6 in the cell supernatants compared with the cells exposed to TGF-b1 alone .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "heme oxygenase-1", "type": "GeneOrGeneProduct"}, {"text": "glutathione peroxidase 1", "type": "GeneOrGeneProduct"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "interleukin-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of the Msx2 gene and phosphorylated-Smad1/5/8 , possible readouts of Bmp signaling , was also increased in the mutants .

Example answer:
{"entities": [{"text": "Msx2", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Loss of MLH1 , a major component of DNA MMR , results in tolerance to the cytotoxic effects of methylating agents and persistence of mutagenised cells at high risk of malignant transformation .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cytotoxic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : These findings indicate that MT1 constitute a biomarker adapted for exploring the impact of sorafenib on the redox metabolism of cancer cells .

Example answer:
{"entities": [{"text": "MT1", "type": "GeneOrGeneProduct"}, {"text": "sorafenib", "type": "ChemicalEntity"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Metallothionein induction reduces caspase-3 activity and TNFalpha levels with preservation of cognitive function and intact hippocampal neurons in carmustine-treated rats .

Example answer:
{"entities": [{"text": "Metallothionein", "type": "ChemicalEntity"}, {"text": "caspase-3", "type": "GeneOrGeneProduct"}, {"text": "TNFalpha", "type": "GeneOrGeneProduct"}, {"text": "carmustine-treated", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: On the other hand , induction of metallothionein ( MT ) by ZnSO ( 4 ) and its role in neuroprotection has been documented .

Example answer:
{"entities": [{"text": "metallothionein", "type": "ChemicalEntity"}, {"text": "MT", "type": "ChemicalEntity"}, {"text": "ZnSO ( 4 )", "type": "ChemicalEntity"}]}

Example input:
Sentence: Metallothionein-1 as a biomarker of altered redox metabolism in hepatocellular carcinoma cells exposed to sorafenib .

Example answer:
{"entities": [{"text": "Metallothionein-1", "type": "GeneOrGeneProduct"}, {"text": "hepatocellular carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "sorafenib", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : We observed that genes of the metallothionein-1 ( MT1 ) family are induced in the HCC cell line Huh7 exposed to sorafenib .

Example answer:
{"entities": [{"text": "metallothionein-1", "type": "GeneOrGeneProduct"}, {"text": "MT1", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Huh7", "type": "CellLine"}, {"text": "sorafenib", "type": "ChemicalEntity"}]}

Input:
Sentence: DNA microarray analysis in cells exposed for 1 week showed upregulated expression of metallothionein genes , particularly MT1X .

## Item biored:test:1010
Example input:
Sentence: We report on a new allele at the arylsulfatase A ( ARSA ) locus causing late-onset metachromatic leukodystrophy ( MLD ) .

Example answer:
{"entities": [{"text": "arylsulfatase A", "type": "GeneOrGeneProduct"}, {"text": "ARSA", "type": "GeneOrGeneProduct"}, {"text": "metachromatic leukodystrophy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MLD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: She had profound insulin resistance , diabetes , severe hypertriglyceridemia and relapsing pancreatitis , while her pre-pubescent daughter had normal fat distribution but elevated plasma triglycerides and C-peptide and depressed high-density lipoprotein cholesterol .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertriglyceridemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "pancreatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "triglycerides", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}, {"text": "high-density lipoprotein cholesterol", "type": "ChemicalEntity"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Taken together , the profile of C5L2 receptor , ASP gene expression and metabolic factors in adipose tissue from morbidly obese HAT subjects suggests a compensatory response associated with the increased plasma ASP and TG .

Example answer:
{"entities": [{"text": "C5L2", "type": "GeneOrGeneProduct"}, {"text": "ASP", "type": "GeneOrGeneProduct"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TG", "type": "ChemicalEntity"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: BACKGROUND : Erythropoietin ( Epo ) exerts direct effects on white adipose tissue ( WAT ) in mice in addition to its erythropoietic effects , and in humans Epo increases resting energy expenditure and affect serum lipid levels , but direct effects of Epo in human WAT have not been documented .

Example answer:
{"entities": [{"text": "Erythropoietin", "type": "GeneOrGeneProduct"}, {"text": "Epo", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "humans", "type": "OrganismTaxon"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: We recently showed that long-term weight reduction changes the gene expression profile of adipose tissue in overweight individuals with impaired glucose tolerance ( IGT ) .

Example answer:
{"entities": [{"text": "overweight", "type": "DiseaseOrPhenotypicFeature"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In developed countries , thiamine deficiency ( TD ) is most often manifested following chronic alcohol consumption leading to impaired mitochondrial function , oxidative stress , inflammation and excitotoxicity .

Example answer:
{"entities": [{"text": "thiamine deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alcohol", "type": "ChemicalEntity"}, {"text": "impaired mitochondrial function", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "excitotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: BACKGROUND : Chronic alcohol consumption leads to a loss of white adipose tissue ( WAT ) but the underlying mechanisms for this lipodystrophy are not fully elucidated .

## Item biored:test:972
Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Homozygosity for c.2607C > A was also identified in an unrelated but haplotypically identical patient with an unusually favorable outcome despite severe neonatal-onset GE .

Example answer:
{"entities": [{"text": "c.2607C > A", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In agreement with the expectation that this mutation alters the LYAR binding activity , we found that the Ag ( +25 G- > A ) and Gg-globin-XmnI polymorphisms are associated with high HbF in erythroid precursor cells isolated from b ( 0 ) 39/b ( 0 ) 39 thalassemia patients .

Example answer:
{"entities": [{"text": "LYAR", "type": "GeneOrGeneProduct"}, {"text": "Ag", "type": "GeneOrGeneProduct"}, {"text": "+25 G- > A", "type": "SequenceVariant"}, {"text": "Gg-globin-XmnI", "type": "GeneOrGeneProduct"}, {"text": "HbF", "type": "GeneOrGeneProduct"}, {"text": "b ( 0 ) 39/b ( 0 ) 39 thalassemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: The allele frequencies of polymorphisms at codon 787 CAG/CAA ( Gln/Gln ) in glioblastomas in Japan were G/G ( 82.4 % ) , G/A ( 10.8 % ) , A/A ( 6.8 % ) , corresponding to G 0.878 versus A 0.122 , significantly different from those in glioblastomas in Switzerland : G/G ( 27.2 % ) , G/A ( 28.4 % ) , A/A ( 44.4 % ) , corresponding to G 0.414 versus A 0.586 ( p < 0.0001 ) .

Example answer:
{"entities": [{"text": "codon 787 CAG/CAA", "type": "SequenceVariant"}, {"text": "Gln/Gln", "type": "SequenceVariant"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: Using direct sequencing a point mutation ( 144 G > A ) resulting in a Q48H substitution in exon 1 of the MYOC gene was observed in five of the eight glaucoma patients , but not in unaffected family members and 100 unrelated controls .

Example answer:
{"entities": [{"text": "144 G > A", "type": "SequenceVariant"}, {"text": "Q48H", "type": "SequenceVariant"}, {"text": "MYOC", "type": "GeneOrGeneProduct"}, {"text": "glaucoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: The result expands the mutation spectrum of GJA8 in associated with congenital cataract and microcornea , and implies that this gene has direct involvement with the development of the lens as well as the other anterior segment of the eye .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract", "type": "DiseaseOrPhenotypicFeature"}, {"text": "microcornea", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A novel mutation in GJA8 causing congenital cataract-microcornea syndrome in a Chinese pedigree .

Example answer:
{"entities": [{"text": "GJA8", "type": "GeneOrGeneProduct"}, {"text": "cataract-microcornea syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Furthermore , there were significant decreases in the frequencies of the G allele and GG homozygosity in CFI-rs7356506 in patients with VKH syndrome with complicated cataract compared to the controls ( p < 0.001 , OR=0.357 , 95 % CI=0.197-0.648 ; p < 0.001 , OR=0.273 , 95 % CI=0.135-0.551 , respectively ) .

## Item biored:test:909
Example input:
Sentence: Five of the forty genes -- ENT3 , IDP3 , JEM1 , ARG2 and HSP82 -- ranked highest in their ability to block alpha-syn-induced reactive oxygen species accumulation , and these five genes were characterized in more detail .

Example answer:
{"entities": [{"text": "ENT3", "type": "GeneOrGeneProduct"}, {"text": "IDP3", "type": "GeneOrGeneProduct"}, {"text": "JEM1", "type": "GeneOrGeneProduct"}, {"text": "ARG2", "type": "GeneOrGeneProduct"}, {"text": "HSP82", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn-induced", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}]}

Example input:
Sentence: These genes were assessed and ranked by cartilage selectivity with whole-genome microarray data , revealing only two genes , encoding aggrecan and chondroitin sulfate proteoglycan 4 , that were selectively expressed in cartilage .

Example answer:
{"entities": [{"text": "aggrecan", "type": "GeneOrGeneProduct"}, {"text": "chondroitin sulfate proteoglycan 4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Two tumors harbored FGFR1 gene fusions ( FGFR1-HOOK3 , FGFR1-TACC1 ) and one harbored an ETV6-NTRK3 fusion that responded to TRK inhibition .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "FGFR1-HOOK3", "type": "GeneOrGeneProduct"}, {"text": "FGFR1-TACC1", "type": "GeneOrGeneProduct"}, {"text": "ETV6-NTRK3", "type": "GeneOrGeneProduct"}, {"text": "TRK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ectodermal dysplasia-skin fragility syndrome resulting from a new homozygous mutation , 888delC , in the desmosomal protein plakophilin 1 .

Example answer:
{"entities": [{"text": "Ectodermal dysplasia-skin fragility syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "888delC", "type": "SequenceVariant"}, {"text": "plakophilin 1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Transcriptome comparisons of UCHL1 KDs versus vector control identified a list of 306 differentially expressed genes ( at least 2-fold change ; p < 0.05 ) which included genes known to be involved in cancer like ACTA2 , POSTN , LIF , FBXL7 , FBXW11 , GDF15 , HEY2 , but also potential novel genes such us IGLL5 , ABCA4 , AQP3 , AQP4 , CALB1 , and ALK .

Example answer:
{"entities": [{"text": "UCHL1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ACTA2", "type": "GeneOrGeneProduct"}, {"text": "POSTN", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}, {"text": "FBXL7", "type": "GeneOrGeneProduct"}, {"text": "FBXW11", "type": "GeneOrGeneProduct"}, {"text": "GDF15", "type": "GeneOrGeneProduct"}, {"text": "HEY2", "type": "GeneOrGeneProduct"}, {"text": "IGLL5", "type": "GeneOrGeneProduct"}, {"text": "ABCA4", "type": "GeneOrGeneProduct"}, {"text": "AQP3", "type": "GeneOrGeneProduct"}, {"text": "AQP4", "type": "GeneOrGeneProduct"}, {"text": "CALB1", "type": "GeneOrGeneProduct"}, {"text": "ALK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These 24 GIST were more commonly mutated at 7 genes : ARID1B , ATR , FGFR1 , LTK , SUFU , PARK2 and ZNF217 .

Example answer:
{"entities": [{"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ARID1B", "type": "GeneOrGeneProduct"}, {"text": "ATR", "type": "GeneOrGeneProduct"}, {"text": "FGFR1", "type": "GeneOrGeneProduct"}, {"text": "LTK", "type": "GeneOrGeneProduct"}, {"text": "SUFU", "type": "GeneOrGeneProduct"}, {"text": "PARK2", "type": "GeneOrGeneProduct"}, {"text": "ZNF217", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: HAT subjects had increased anti-inflammatory genes TGFB1 , TIMP1 , TIMP3 , and TIMP4 while proinflammatory PIG7 and MMP2 were also significantly increased ; all genes , p < 0.025 .

Example answer:
{"entities": [{"text": "TGFB1", "type": "GeneOrGeneProduct"}, {"text": "TIMP1", "type": "GeneOrGeneProduct"}, {"text": "TIMP3", "type": "GeneOrGeneProduct"}, {"text": "TIMP4", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PIG7", "type": "GeneOrGeneProduct"}, {"text": "MMP2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Of these , rs11891426 : T > G in an intron of the melanophilin gene ( MLPH ) was within a novel putative auxiliary AR-binding motif , which is enriched in the neighborhood of canonical androgen-responsive elements .

Example answer:
{"entities": [{"text": "rs11891426", "type": "SequenceVariant"}, {"text": "T > G", "type": "SequenceVariant"}, {"text": "melanophilin", "type": "GeneOrGeneProduct"}, {"text": "MLPH", "type": "GeneOrGeneProduct"}, {"text": "AR-binding", "type": "GeneOrGeneProduct"}, {"text": "androgen-responsive", "type": "ChemicalEntity"}]}

Input:
Sentence: Eight genes -- fras1 , grip1 , hmcn1 , msxc , col4a4 , ahnak , capn12 , and nrg2a -- had been described in an integumentary context to varying degrees , while arhgef25b , fkbp10b , and megf6a emerged as novel skin genes .

## Item biored:test:1030
Example input:
Sentence: In the present study , we demonstrate that NF-kappaB , whether activated by recombinant human tumor necrosis factor ( TNF ) -alpha or by ectopic expression of the p65 subunit , is involved in extracellular matrix adhesion and invasion of osteotropic PC-3 and C4-2B , but not LNCaP , cells .

Example answer:
{"entities": [{"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tumor necrosis factor ( TNF ) -alpha", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "PC-3", "type": "CellLine"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "LNCaP", "type": "CellLine"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Finally , the inflammatory infiltration of alveolar and interstitial cells and the destruction of lung structure were significantly attenuated in the mide administered Bach1 siRNA compared with those in the BLM group .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "BLM", "type": "ChemicalEntity"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Rab6c was found to be under-expressed in MCF7/AdrR and MES-SA/Dx5 ( a human MDR uterine sarcoma cell line ) compared with their non-MDR parental cell lines .

Example answer:
{"entities": [{"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "MES-SA/Dx5", "type": "CellLine"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "uterine sarcoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Furthermore , PI3K/Akt pathway signaling was also increased in Eu-myc B cells , and this increase was partially suppressed with ibrutinib .

Example answer:
{"entities": [{"text": "PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "ibrutinib", "type": "ChemicalEntity"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Input:
Sentence: Depletion of PI4KIIb was sufficient to confer an aggressive invasive phenotype on minimally invasive HeLa and MCF-7 cell lines .

## Item biored:test:1003
Example input:
Sentence: In conclusion , gene-targeted mice lacking SGK1 showed blunted volume retention , yet were not protected against renal fibrosis during experimental nephrotic syndrome .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "volume retention", "type": "DiseaseOrPhenotypicFeature"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Both GcgR knockout ( Gcgr ( -/- ) ) mice and db/db mice that were administered GcgR monoclonal antibody displayed lower blood glucose levels accompanied by elevated plasma ghrelin levels .

Example answer:
{"entities": [{"text": "GcgR", "type": "GeneOrGeneProduct"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "blood glucose", "type": "ChemicalEntity"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Superoxide dismutase 1 overexpression in mice abolishes maternal diabetes-induced endoplasmic reticulum stress in diabetic embryopathy .

Example answer:
{"entities": [{"text": "Superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "maternal", "type": "DiseaseOrPhenotypicFeature"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "embryopathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Resequencing of IRS2 reveals rare variants for obesity but not fasting glucose homeostasis in Hispanic children .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: SNP rs6235 was not associated with parameters of glucose metabolism .

Example answer:
{"entities": [{"text": "rs6235", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Subcutaneous ( SC ) and omental ( OM ) adipose tissues ( n = 21 ) were analysed by microarray , and biologic pathways in lipid metabolism and inflammation were specifically examined .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Collectively , these results demonstrate that GLUT4 is not necessary for overload-induced muscle glucose uptake or hypertrophic growth and suggest that GLUT1 , GLUT3 , GLUT6 , and/or GLUT10 mediate overload-induced glucose uptake .

Example answer:
{"entities": [{"text": "GLUT4", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "GLUT1", "type": "GeneOrGeneProduct"}, {"text": "GLUT3", "type": "GeneOrGeneProduct"}, {"text": "GLUT6", "type": "GeneOrGeneProduct"}, {"text": "GLUT10", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: GLUT4 Is Not Necessary for Overload-Induced Glucose Uptake or Hypertrophic Growth in Mouse Skeletal Muscle .

Example answer:
{"entities": [{"text": "GLUT4", "type": "GeneOrGeneProduct"}, {"text": "Glucose", "type": "ChemicalEntity"}, {"text": "Mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: Overload-induced muscle glucose uptake and hypertrophic growth were not impaired in muscle-specific GLUT4 knockout mice , demonstrating that GLUT4 is not necessary for these processes .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "GLUT4", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Input:
Sentence: Body weight , muscle and adipose tissue masses , and parameters of glucose homeostasis showed that 11b-HSD1KO and LKO mice were not protected from systemic metabolic disease .

## Item biored:test:1057
Example input:
Sentence: Mutational analyses of TS and allelic imbalances were studied in all primary tumors and in 18 additional metachronic metastases .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemical analysis of Grade 1 endometrioid adenocarcinoma revealed aberrant PKCalpha expression , with foci of elevated PKCalpha staining , not observed in normal endometrium .

Example answer:
{"entities": [{"text": "endometrioid adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We detected 24 p53 mutations in 15/25 ( 60 % ) NMSCs , 1 deletion and 23 base substitutions , the majority ( 78 % ) being UV-specific C to T transitions at bipyrimidine sites .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "NMSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C to T", "type": "SequenceVariant"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found 8 p53 mutations in 7/17 ( 41 % ) precancerous actinic keratosis ( AK ) , suggesting that p53 mutations are early events in RTR skin carcinogenesis .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "actinic keratosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We aimed to clarify the concordance between PIK3CA mutations detected in endoscopic biopsy specimens and corresponding surgically resected specimens .

## Item biored:test:1011
Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: The binding of mTOR , PRAS40 and RagC to raptor did not differ for control and septic muscle in the basal condition ; however , the Leu-induced decrease in PRAS40 raptor and increase in RagC raptor seen in control muscle was absent in sepsis .

Example answer:
{"entities": [{"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "PRAS40", "type": "GeneOrGeneProduct"}, {"text": "RagC", "type": "GeneOrGeneProduct"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "Leu-induced", "type": "ChemicalEntity"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Importantly , gene deletion or blockade of KCa3.1 restored AKT/mechanistic target of rapamycin signaling both in vivo and in vitro .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "AKT/mechanistic target of rapamycin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hence , while alterations in select amino acid transporters are not associated with development of sepsis-induced Leu resistance , the Leu-stimulated binding of raptor with RagC and the recruitment of mTOR/raptor to the endosome-lysosomal compartment may partially explain the inability of Leu to fully activate mTOR and muscle protein synthesis .

Example answer:
{"entities": [{"text": "amino acid transporters", "type": "GeneOrGeneProduct"}, {"text": "sepsis-induced", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leu", "type": "ChemicalEntity"}, {"text": "Leu-stimulated", "type": "ChemicalEntity"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "RagC", "type": "GeneOrGeneProduct"}, {"text": "mTOR/raptor", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: There was no sepsis or Leu effect on the protein content for RagA-D , LAMTOR-1 and -2 , raptor , Rheb or mTOR in muscle .

Example answer:
{"entities": [{"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Leu", "type": "ChemicalEntity"}, {"text": "RagA-D", "type": "GeneOrGeneProduct"}, {"text": "LAMTOR-1 and -2", "type": "GeneOrGeneProduct"}, {"text": "raptor", "type": "GeneOrGeneProduct"}, {"text": "Rheb", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A potential downstream signaling pathway involving phosphatidylinositol 3-kinase ( PI3K ) /threonine protein kinase B ( Akt ) /mammalian target of rapamycin ( mTOR ) was identifiedby western blot analysis .

Example answer:
{"entities": [{"text": "phosphatidylinositol 3-kinase", "type": "GeneOrGeneProduct"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "target of rapamycin", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Massive urinary protein excretion has been observed after conversion from calcineurin inhibitors to mammalian target of rapamycin ( mToR ) inhibitors , especially sirolimus , in renal transplant recipients with chronic allograft nephropathy .

Example answer:
{"entities": [{"text": "calcineurin inhibitors", "type": "ChemicalEntity"}, {"text": "mammalian target of rapamycin ( mToR ) inhibitors", "type": "ChemicalEntity"}, {"text": "sirolimus", "type": "ChemicalEntity"}, {"text": "chronic allograft nephropathy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: This study tested the hypothesis that the reduction in WAT mass in chronic alcohol-fed mice is associated with a decreased protein synthesis specifically related to impaired function of mammalian target of rapamycin ( mTOR ) .

## Item biored:test:1060
Example input:
Sentence: A novel missense mutation c.643T > C ( p.S216P ) was detected in the anterior segment malformation group .

Example answer:
{"entities": [{"text": "c.643T > C", "type": "SequenceVariant"}, {"text": "p.S216P", "type": "SequenceVariant"}, {"text": "anterior segment malformation", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found 8 p53 mutations in 7/17 ( 41 % ) precancerous actinic keratosis ( AK ) , suggesting that p53 mutations are early events in RTR skin carcinogenesis .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "actinic keratosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : When compared with Crohn 's disease patients without CARD15 mutations , the presence of at least one CARD15 variant in Crohn 's disease patients more frequently led to gASCA positivity ( 66.1 % versus 51.5 % , p < 0.0001 ) and ALCA positivity ( 43.3 % versus 34.9 % , p = 0.018 ) and higher gASCA titers ( 85.7 versus 51.8 ELISA units , p < 0.0001 ) , independent of ileal involvement .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CARD15", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We detected 24 p53 mutations in 15/25 ( 60 % ) NMSCs , 1 deletion and 23 base substitutions , the majority ( 78 % ) being UV-specific C to T transitions at bipyrimidine sites .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "NMSCs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C to T", "type": "SequenceVariant"}]}

Example input:
Sentence: We have developed a sensitive single tube tetra-primer PCR assay to detect both the c.1138G > A and c.1138G > C mutations and can successfully distinguish DNA samples that are homozygous and heterozygous for the c.1138G > A mutation .

Example answer:
{"entities": [{"text": "c.1138G > A", "type": "SequenceVariant"}, {"text": "c.1138G > C", "type": "SequenceVariant"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Input:
Sentence: A PIK3CA mutation was detected in either type of specimen in 13 cases ( 7.2 % , 95 % confidence interval : 3.9-12.0 ) .

## Item biored:test:1050
Example input:
Sentence: Moreover , CBKOTg mice reduced levels of phosphorylated mitogen-activated protein kinase ( extracellular signal-regulated kinase ) 1/2 and cAMP response element-binding protein at Ser-133 and synaptic molecules such as N-methyl-D-aspartate receptor 1 ( NMDA receptor 1 ) , NMDA receptor 2A , PSD-95 and synaptophysin in the subiculum compared with Tg mice .

Example answer:
{"entities": [{"text": "CBKOTg", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "extracellular signal-regulated kinase ) 1/2", "type": "GeneOrGeneProduct"}, {"text": "cAMP response element-binding protein", "type": "GeneOrGeneProduct"}, {"text": "N-methyl-D-aspartate receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 1", "type": "GeneOrGeneProduct"}, {"text": "NMDA receptor 2A", "type": "GeneOrGeneProduct"}, {"text": "PSD-95", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Distinct patterns of germ-line deletions in MLH1 and MSH2 : the implication of Alu repetitive element in the genetic etiology of Lynch syndrome ( HNPCC ) .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mouse embryonic fibroblasts exhibiting disruption or overexpression of IGF-1R ( R- cells and R+ cells ) were used to examine the level of apoptosis , autophagy , and production of reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Upon division , Dpp signaling is extinguished , and Nos is downregulated in one daughter cell , causing it to switch to a differentiating cystoblast ( CB ) .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Drosophila ovarian germline stem cells ( GSCs ) are maintained by Dpp signaling and the Pumilio ( Pum ) and Nanos ( Nos ) translational repressors .

Example answer:
{"entities": [{"text": "Drosophila", "type": "OrganismTaxon"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Pumilio", "type": "GeneOrGeneProduct"}, {"text": "Pum", "type": "GeneOrGeneProduct"}, {"text": "Nanos", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Here , we report that CenpH , a component of the kinetochore inner plate , is responsible for G2/M transition in meiotic mouse oocytes .

## Item biored:test:1063
Example input:
Sentence: In addition , although exon 1beta mutation is rare in various tumors , we detected a missense mutation ( L50R ) in one case with a hemizygous deletion .

Example answer:
{"entities": [{"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "L50R", "type": "SequenceVariant"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Example input:
Sentence: In an independent sample set , we identified 5 GIST cases lacking alterations in the KIT/PDGFRA/SDHx/RAS pathways , including two additional cases with FGFR1-TACC1 and ETV6-NTRK3 fusions .

Example answer:
{"entities": [{"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KIT/PDGFRA/SDHx/RAS", "type": "GeneOrGeneProduct"}, {"text": "FGFR1-TACC1", "type": "GeneOrGeneProduct"}, {"text": "ETV6-NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: One patient with a severe cellular and clinical phenotype was a compound heterozygote with POLG1 mutations in the polymerase and exonuclease domain intrans .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutational analyses of TS and allelic imbalances were studied in all primary tumors and in 18 additional metachronic metastases .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , mutation analysis for MKS3/TMEM67 in 120 patients with JBTS yielded seven different ( four novel ) mutations in five patients , four of whom also presented with congenital liver fibrosis .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "JBTS", "type": "DiseaseOrPhenotypicFeature"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In 2002 , the Multiple Leiomyoma Consortium identified heterozygous germline mutations of FH in patients with multiple cutaneous and uterine leiomyomas , ( MCUL : OMIM 150800 ) .

Example answer:
{"entities": [{"text": "Leiomyoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FH", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "multiple cutaneous and uterine leiomyomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MCUL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OMIM 150800", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: VNTR and ins/del 6 bp genotypes varied with tumour anatomical site : 2R/2R genotype was rare in left-sided tumours ( 7.0 % vs. 26.3 % of right-sided and 24.1 % of rectal cancers ; P < 0.01 ) , where the variant allele 6- was very frequent ( 69.0 % ) .

Example answer:
{"entities": [{"text": "ins/del 6 bp", "type": "SequenceVariant"}, {"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumours", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rectal cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: There were three cases with a discordant mutation status between the types of specimens ( PIK3CA mutation in surgically resected specimen and wild-type in biopsy specimen in two cases , and the opposite pattern in one case ) , suggesting possible intratumoral heterogeneity in the PIK3CA mutation status .

## Item biored:test:1033
Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: To investigate this question , we have developed in vitro motility assays with purified DDB and BICD2 's membrane vesicle partner , the GTPase Rab6a .

Example answer:
{"entities": [{"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "GTPase Rab6a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our interpretation is that Ent3p mediates the transport of alpha-syn to the vacuole for proteolytic degradation .

Example answer:
{"entities": [{"text": "Ent3p", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Rab6a-GTP , either in solution or bound to artificial liposomes , released BICD2 from an autoinhibited state and promoted robust dynein-dynactin transport .

Example answer:
{"entities": [{"text": "Rab6a-GTP", "type": "GeneOrGeneProduct"}, {"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "dynein-dynactin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: We propose that PI4KIIb synthesizes a pool of PI ( 4 ) P that maintains MT1-MMP traffic in the degradative pathway and suppresses the formation of invadopodia .

## Item biored:test:1039
Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : More than 3 decades after Jones and Smith ( 1973 ) reported on the devastation caused by alcohol exposure on fetal development , the rates of heavy drinking during pregnancy remain relatively unchanged .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: There was a marked increase in the number of TUNEL positive cells and nestin positive cells in BCNU-exposed group , but a decreased immunoreactivity to glial fibrillary acidic protein , synaptophysin and transforming growth factor beta1 was observed , indicating a delayed maturation , and melatonin significantly reversed these changes .

Example answer:
{"entities": [{"text": "BCNU-exposed", "type": "ChemicalEntity"}, {"text": "glial fibrillary acidic protein", "type": "GeneOrGeneProduct"}, {"text": "synaptophysin", "type": "GeneOrGeneProduct"}, {"text": "transforming growth factor beta1", "type": "GeneOrGeneProduct"}, {"text": "melatonin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Impact of alcohol exposure after pregnancy recognition on ultrasonographic fetal growth measures .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: Addition of Tat ( 40 ng/slice ) to the medium of OHSCs induced IDO steady-state mRNA that peaked at 6 h. This effect was potentiated by pretreatment with IFNg .

Example answer:
{"entities": [{"text": "Tat", "type": "GeneOrGeneProduct"}, {"text": "IDO", "type": "GeneOrGeneProduct"}, {"text": "IFNg", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A cell proliferation assay was performed after 7 days of incubation under normoxic conditions .

Example answer:
{"entities": []}

Example input:
Sentence: SOX2 and NANOG expression did not change following ETO treatment suggesting a dissociation of OCT4A from its pluripotency function .

Example answer:
{"entities": [{"text": "SOX2", "type": "GeneOrGeneProduct"}, {"text": "NANOG", "type": "GeneOrGeneProduct"}, {"text": "ETO", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Short-term ( 1-week ) incubation to ethanol at as low as 1-5 mM ( corresponding to blood alcohol concentration of ~0.0048-0.024 % ) upregulated the stem cell related proteins Oct4 and Nanog , but they were reduced after exposure at 25 mM .

## Item biored:test:1016
Example input:
Sentence: Furthermore , EPZ015666 restrained the phosphorylation of IkB kinaseb and IkBa , as well as nucleus transsituation of p65 as well as AKT in FLSs .

Example answer:
{"entities": [{"text": "EPZ015666", "type": "ChemicalEntity"}, {"text": "IkB kinaseb", "type": "GeneOrGeneProduct"}, {"text": "IkBa", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The data suggest that in VIP ( -/- ) mice with bladder inflammation , inflammatory mediators are increased above that observed in WT with CYP .

Example answer:
{"entities": [{"text": "bladder", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Likewise , in vivo , B6D2F1 mice were treated with etoposide , daunorubicin , and doxorubicin , with or without dexrazoxane over a wide range of doses : posttreatment , a full hematologic evaluation was done .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "etoposide", "type": "ChemicalEntity"}, {"text": "daunorubicin", "type": "ChemicalEntity"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "dexrazoxane", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In collagenase-induced ICH mice , the protection of etifoxine was associated with reduced leukocyte infiltration into the brain and microglial production of IL-6 and TNF-a .

Example answer:
{"entities": [{"text": "collagenase-induced", "type": "ChemicalEntity"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "etifoxine", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Improved cardiac function and less scar formation were observed in TIEG1 KO mice , and we also observed the altered expression of phosphatase and tensin homolog ( Pten ) , Akt and Bcl-2/Bax , as well as vascular endothelial growth factor ( VEGF ) .

Example answer:
{"entities": [{"text": "TIEG1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "Pten", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2/Bax", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Those novel compound heterozygous mutations were thought to contribute to the loss of CHST6 function , which induced the abnormal metabolism of keratan sulfate ( KS ) that deposited in the corneal stroma .

Example answer:
{"entities": [{"text": "CHST6", "type": "GeneOrGeneProduct"}, {"text": "keratan sulfate", "type": "ChemicalEntity"}, {"text": "KS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "CX3CR1", "type": "GeneOrGeneProduct"}, {"text": "enhanced green fluorescent protein", "type": "ChemicalEntity"}, {"text": "eGFP", "type": "ChemicalEntity"}, {"text": "METH", "type": "ChemicalEntity"}, {"text": "neurotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Instead , a selective increase in phosphorylation of S6K1 and its downstream substrates , S6 and eIF4B was detected in alcohol-fed mice .

## Item biored:test:1019
Example input:
Sentence: Instead , ETO-induced OCT4A was concomitant with activation of AMPK , a key component of metabolic stress and autophagy regulation .

Example answer:
{"entities": [{"text": "ETO-induced", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consequently , ADAM12 knockdown lowered the basal activation level of EGFR , and this effect was abolished by batimastat , a metalloproteinase inhibitor .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "batimastat", "type": "ChemicalEntity"}, {"text": "metalloproteinase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Maternal diabetes significantly increased the levels of CHOP , calnexin , phosphorylated ( p ) -eIF2a , p-PERK , and p-IRE1a ; triggered XBP1 mRNA splicing ; and enhanced ER chaperone gene expression in WT embryos .

Example answer:
{"entities": [{"text": "Maternal diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Lipolytic enzymes ( ATGL and HSL phosphorylation ) were increased and lipogenic regulators ( PPARgamma and C/EBPalpha ) were decreased in eWAT by alcohol .

## Item biored:test:1004
Example input:
Sentence: reduced significantly the brain acetylcholinesterase activity and cholesterol levels in young and aged mice .

Example answer:
{"entities": [{"text": "acetylcholinesterase", "type": "GeneOrGeneProduct"}, {"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: BACKGROUND/AIMS : The genetic predisposition on the development of nonalcoholic steatohepatitis ( NASH ) has been poorly understood .

Example answer:
{"entities": [{"text": "nonalcoholic steatohepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Object of the present study was to study the influence of SLCO1B1 * 5 , * 15 and * 15+C1007G , a novel haplotype found in a patient with pravastatin-induced myopathy , on the functional properties of OATP1B1 by transient expression systems of HEK293 and HeLa cells using endogenous conjugates and statins as substrates .

Example answer:
{"entities": [{"text": "SLCO1B1", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pravastatin-induced", "type": "ChemicalEntity"}, {"text": "myopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OATP1B1", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "HeLa", "type": "CellLine"}]}

Example input:
Sentence: Consistently , LKB1 ( endo-/- ) mouse tissues including the lung , skin , kidney and liver showed increased vascular permeability .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: RESULTS : The transporting activities of cells expressing SLCO1B1 * 5 , * 15 and * 15+C1007G decreased significantly but those of SLCO1B1 * 1b , * 1a+C1007G and * 1b+C1007G were not altered for all of the substrates tested except for simvastatin .

Example answer:
{"entities": [{"text": "SLCO1B1", "type": "GeneOrGeneProduct"}, {"text": "simvastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Tak1 ( col2 ) mice displayed severe chondrodysplasia with runting , impaired formation of secondary centres of ossification , and joint abnormalities including elbow dislocation and tarsal fusion .

Example answer:
{"entities": [{"text": "Tak1", "type": "GeneOrGeneProduct"}, {"text": "col2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "chondrodysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "joint abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "elbow dislocation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tarsal fusion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Compared with WT mice , the liver weight and liver metastatic rate were significantly lower in AT1aKO .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "liver metastatic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Evaluation of hepatic histology , triglyceride content , and blinded NAFLD activity score assessment indicated that levels of steatosis were similar between 11b-HSD1KO , LKO , and control mice .

## Item biored:test:1055
Example input:
Sentence: Mutation analysis in a Chinese family with multiple endocrine neoplasia type 1 .

Example answer:
{"entities": [{"text": "multiple endocrine neoplasia type 1", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In an independent sample set , we identified 5 GIST cases lacking alterations in the KIT/PDGFRA/SDHx/RAS pathways , including two additional cases with FGFR1-TACC1 and ETV6-NTRK3 fusions .

Example answer:
{"entities": [{"text": "GIST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "KIT/PDGFRA/SDHx/RAS", "type": "GeneOrGeneProduct"}, {"text": "FGFR1-TACC1", "type": "GeneOrGeneProduct"}, {"text": "ETV6-NTRK3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: As previously observed for glioblastomas in Europe , there was a positive association between EGFR amplification and p16 deletion ( p=0.009 ) , whereas there was an inverse association between TP53 mutations and p16 deletion ( p=0.049 ) in glioblastomas in Japan .

Example answer:
{"entities": [{"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "TP53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a hospital-based study of non-Hispanic whites , we genotyped CASP8 -652 6N del and 302H variants in 1,023 patients with squamous cell carcinoma of the head and neck ( SCCHN ) and 1,052 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "squamous cell carcinoma of the head and neck", "type": "DiseaseOrPhenotypicFeature"}, {"text": "SCCHN", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analyses of TS and allelic imbalances were studied in all primary tumors and in 18 additional metachronic metastases .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemical analysis of Grade 1 endometrioid adenocarcinoma revealed aberrant PKCalpha expression , with foci of elevated PKCalpha staining , not observed in normal endometrium .

Example answer:
{"entities": [{"text": "endometrioid adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We found 8 p53 mutations in 7/17 ( 41 % ) precancerous actinic keratosis ( AK ) , suggesting that p53 mutations are early events in RTR skin carcinogenesis .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "precancerous", "type": "DiseaseOrPhenotypicFeature"}, {"text": "actinic keratosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AK", "type": "DiseaseOrPhenotypicFeature"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing of the kinase domain ( exons 18-21 ) of the EGFR gene revealed mutations in 2 ou of 69 ( 3 % ) glioblastomas in Japan and in 4 of 81 ( 5 % ) glioblastomas in Switzerland .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Concordance between PIK3CA mutations in endoscopic biopsy and surgically resected specimens of esophageal squamous cell carcinoma .

## Item biored:test:941
Example input:
Sentence: However , the ACE genotypes correlated with the number of lymph node metastases and the Unio Internationale Contra Cancrum ( UICC ) tumor stage .

Example answer:
{"entities": [{"text": "ACE", "type": "GeneOrGeneProduct"}, {"text": "lymph node metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Patients with the II genotype had a highly significantly smaller number of lymph node metastases ( P < 0.001 ) and a significantly lower UICC tumor stage ( P = 0.01 ) than patients with the DD genotype .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "lymph node metastases", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: By histology-based analysis , the Cys/Cys genotype showed a significantly positive association with small-cell carcinoma ( OR=2.40 , 95 % CI=1.32-4.49 ) and marginally significant association with adenocarcinoma ( OR=1.32 , 95 % CI=0.98-1.77 ) .

Example answer:
{"entities": [{"text": "small-cell carcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Immunohistochemical analysis of Grade 1 endometrioid adenocarcinoma revealed aberrant PKCalpha expression , with foci of elevated PKCalpha staining , not observed in normal endometrium .

Example answer:
{"entities": [{"text": "endometrioid adenocarcinoma", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , the number of the CASP8 -652 6N del ( but not 302H ) variant allele tended to correlate with increased levels of camptothecin-induced p53-mediated apoptosis in T lymphocytes from 170 cancer-free controls .

Example answer:
{"entities": [{"text": "CASP8", "type": "GeneOrGeneProduct"}, {"text": "-652 6N del", "type": "SequenceVariant"}, {"text": "302H", "type": "SequenceVariant"}, {"text": "camptothecin-induced", "type": "ChemicalEntity"}, {"text": "p53-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSION : Variation in IL10 , CRP , GSTP1 , IL1B , and NOS2 was associated with prostate cancer recurrence independent of pathologic prognostic factors .

Example answer:
{"entities": [{"text": "IL10", "type": "GeneOrGeneProduct"}, {"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "NOS2", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum concentrations of CRP , neopterin and IL-6 as markers of inflammation and thrombopoietin ( TPO ) , GCSF , FGF basic and VEGF , HMGB1 , CK-18 ( M65 ) and CK18 fragment ( M30 ) and a panel of proinflammatory chemokines ( CCL2 , CCL3 , CCL4 , CCL5 , CXCL5 and IL-8 ) were measured .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "neopterin", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombopoietin", "type": "GeneOrGeneProduct"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "GCSF", "type": "GeneOrGeneProduct"}, {"text": "FGF basic", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}, {"text": "CK-18", "type": "GeneOrGeneProduct"}, {"text": "CK18", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL3", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The prognostic value of serum tumour markers alpha-fetoprotein ( AFP ) and des-gamma-carboxy prothrombin ( DCP ) is limited .

Example answer:
{"entities": [{"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-fetoprotein", "type": "GeneOrGeneProduct"}, {"text": "AFP", "type": "GeneOrGeneProduct"}, {"text": "des-gamma-carboxy prothrombin", "type": "GeneOrGeneProduct"}, {"text": "DCP", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In the 213 EOC samples , CEP55 protein levels were positively correlated with clinical stage ( P < 0.001 ) , lymph node metastasis ( P < 0.001 ) , intraperitoneal metastasis ( P < 0.001 ) , tumor recurrence ( P < 0.001 ) , differentiation grade ( P < 0.001 ) , residual tumor size ( P < 0.001 ) , ascites see tumor cells ( P = 0.020 ) , and serum CA153 level ( P < 0.001 ) .

## Item biored:test:1047
Example input:
Sentence: In breast cancer patients , high levels of Star-PAP correlated with an improved prognosis .

Example answer:
{"entities": [{"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Star-PAP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Example input:
Sentence: ADAM12 is induced during epithelial-to-mesenchymal transition , a feature associated with claudin-low breast tumors , which are enriched in cancer stem cell ( CSC ) markers .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "claudin-low", "type": "GeneOrGeneProduct"}, {"text": "breast tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND : ADAM12 is upregulated in human breast cancers and is a predictor of chemoresistance in estrogen receptor-negative tumors .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "breast cancers", "type": "DiseaseOrPhenotypicFeature"}, {"text": "estrogen", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Study-specific associations of 68 single nucleotide polymorphisms ( SNPs ) in 8 alcohol-metabolising genes ( Alcohol Dehydrogenases ( ADHs ) and Aldehyde Dehydrogenases ( ALDHs ) ) with prostate cancer diagnosis and prostate cancer-specific mortality , by grade , were assessed using logistic and Cox regression models , respectively .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "Alcohol Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ADHs", "type": "GeneOrGeneProduct"}, {"text": "Aldehyde Dehydrogenases", "type": "GeneOrGeneProduct"}, {"text": "ALDHs", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "prostate", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this study , we investigated the associations of genetic variants in alcohol-metabolising genes with prostate cancer incidence and survival .

Example answer:
{"entities": [{"text": "alcohol-metabolising", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The effects of alcohol consumption on prostate cancer incidence and survival remain unclear , potentially due to methodological limitations of observational studies .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggest that alcohol consumption is unlikely to affect prostate cancer incidence , but it may influence disease progression .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Alcohol consumption and prostate cancer incidence and progression : A Mendelian randomisation study .

Example answer:
{"entities": [{"text": "Alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The previously shown alcohol induction of oncogenic transformation of normal breast cells is now complemented by the current results suggesting alcohol 's potential involvement in malignant progression of breast cancer .

## Item biored:test:1075
Example input:
Sentence: A recent addition to the list of widely confirmed type 1 diabetes risk loci is the PTPN22 gene encoding a lymphoid-specific phosphatase ( Lyp ) .

Example answer:
{"entities": [{"text": "type 1 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTPN22", "type": "GeneOrGeneProduct"}, {"text": "lymphoid-specific phosphatase", "type": "GeneOrGeneProduct"}, {"text": "Lyp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We conclude that the SNPs of SLC2A2 predict the conversion to diabetes in obese subjects with IGT .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We then examined them on genomic DNA in six MODY probands without mutations in the MODY1 , MODY3 and MODY4 genes and in 54 patients with late-onset Type II diabetes by combined single strand conformational polymorphism-heteroduplex analysis followed by direct sequencing of identified variants .

Example answer:
{"entities": [{"text": ",", "type": "GeneOrGeneProduct"}, {"text": "II diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: None of the SNPs or indels were associated with diabetes-related traits or accounted for a previously identified quantitative trait locus on chromosome 13 for fasting serum glucose .

Example answer:
{"entities": [{"text": "diabetes-related", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: With the exception of SLC2A2 , other genes were not associated with the risk of type 2 diabetes .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our aim was to study the associations of individual single nucleotide polymorphisms and haplotypes with adiposity , glucose metabolism , and the risk of type 2 diabetes ( T2D ) .

Example answer:
{"entities": [{"text": "adiposity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "T2D", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Polymorphisms in the SLC2A2 ( GLUT2 ) gene are associated with the conversion from impaired glucose tolerance to type 2 diabetes : the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Using individual-level data from 120,286 participants in the UK Biobank and summary association results from four large-scale genome-wide association studies , we examined the impact of this variant on cardiometabolic traits , type 2 diabetes , and coronary heart disease .

Example answer:
{"entities": [{"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "coronary heart disease", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All four SNPs of SLC2A2 predicted the conversion to diabetes , and rs5393 ( AA genotype ) increased the risk of type 2 diabetes in the entire study population by threefold ( odds ratio 3.04 , 95 % CI 1.34-6.88 , P = 0.008 ) .

Example answer:
{"entities": [{"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs5393", "type": "SequenceVariant"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The aim of this study was to investigate whether single nucleotide polymorphisms ( SNPs ) in the genes regulating insulin secretion ( SLC2A2 [ encoding GLUT2 ] , GCK , TCF1 [ encoding HNF-1alpha ] , HNF4A , GIP , and GLP1R ) are associated with the conversion from impaired glucose tolerance ( IGT ) to type 2 diabetes in participants of the Finnish Diabetes Prevention Study .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "SLC2A2", "type": "GeneOrGeneProduct"}, {"text": "GLUT2", "type": "GeneOrGeneProduct"}, {"text": "GCK", "type": "GeneOrGeneProduct"}, {"text": "TCF1", "type": "GeneOrGeneProduct"}, {"text": "HNF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "HNF4A", "type": "GeneOrGeneProduct"}, {"text": "GIP", "type": "GeneOrGeneProduct"}, {"text": "GLP1R", "type": "GeneOrGeneProduct"}, {"text": "impaired glucose tolerance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IGT", "type": "DiseaseOrPhenotypicFeature"}, {"text": "type 2 diabetes", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Diabetes", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Molecular mechanisms remain unknown for most type 2 diabetes genome-wide association study identified loci .

## Item biored:test:1062
Example input:
Sentence: VNTR and ins/del 6 bp genotypes varied with tumour anatomical site : 2R/2R genotype was rare in left-sided tumours ( 7.0 % vs. 26.3 % of right-sided and 24.1 % of rectal cancers ; P < 0.01 ) , where the variant allele 6- was very frequent ( 69.0 % ) .

Example answer:
{"entities": [{"text": "ins/del 6 bp", "type": "SequenceVariant"}, {"text": "tumour", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumours", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rectal cancers", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : When compared with Crohn 's disease patients without CARD15 mutations , the presence of at least one CARD15 variant in Crohn 's disease patients more frequently led to gASCA positivity ( 66.1 % versus 51.5 % , p < 0.0001 ) and ALCA positivity ( 43.3 % versus 34.9 % , p = 0.018 ) and higher gASCA titers ( 85.7 versus 51.8 ELISA units , p < 0.0001 ) , independent of ileal involvement .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "CARD15", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Five hundred samples without pA1 or pA2 mutations had the entire ARX ORF screened by single stranded polymorphism conformation ( SSCP ) and/or denaturing high pressure liquid chromatography ( dHPLC ) analysis .

Example answer:
{"entities": [{"text": "ARX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: Three BRCA1 abnormalities - 5382insC , C61G , and 4153delA - accounted for 51 % , 20 % , and 11 % of the identified mutations , respectively ..

Example answer:
{"entities": [{"text": "BRCA1 abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "5382insC", "type": "SequenceVariant"}, {"text": "C61G", "type": "SequenceVariant"}, {"text": "4153delA", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Additionally , when PSA genotype was cross classified with CAG repeat , significantly more cases than both BPH and population controls were observed to have a short ( < 22 ) CAG/GG genotype ( P = 0.006 ) .

Example answer:
{"entities": [{"text": "PSA", "type": "GeneOrGeneProduct"}, {"text": "CAG repeat", "type": "SequenceVariant"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Tumor genotyping ( frequency of allelic loss , 26 % ) showed that the 3R/3R genotype was associated with a better outcome ( hazard ratio [ HR ] = 0.38 ; 95 % CI , 0.16 to 0.93 ; P = .020 for the recessive model ) .

Example answer:
{"entities": [{"text": "Tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Results : Forty seven patients ( 50 % ) had the genotype G1359G ( wild type group ) and 47 ( 50 % ) patients G1359A ( 41 patients , 43.6 % ) or A1359A ( 6 patients , 6.4 % ) ( mutant type group ) had the genotype .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "G1359G", "type": "SequenceVariant"}, {"text": "G1359A", "type": "SequenceVariant"}, {"text": "A1359A", "type": "SequenceVariant"}]}

Input:
Sentence: Among patients with a PIK3CA mutation detected in both types of specimens , the concordance between PIK3CA mutation genotypes was 100 % .
