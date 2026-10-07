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

## Item biored:test:932
Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Attenuated expression of LDHA by siRNA or inhibition of LDHA activities by FX11 inhibited cell proliferation , migration , invasion , and promoted cell apoptosis of PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Methadone , an agonist of OPRM1 , enhances the sensitivity of parental leukemic cells , but not OPRM1-depleted cells , to L-asparaginase treatment , indicating that OPRM1 is required for the synergistic action of L-asparaginase and methadone , and that OPRM1 loss promotes leukemic cell survival likely through downregulation of the OPRM1-mediated apoptotic pathway .

Example answer:
{"entities": [{"text": "Methadone", "type": "ChemicalEntity"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "methadone", "type": "ChemicalEntity"}, {"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Treatment of WT with clodronate liposomes suppressed liver metastasis by diminishing TGF-b1 ( + ) F4/80 ( + ) cells accumulation .

Example answer:
{"entities": [{"text": "clodronate", "type": "ChemicalEntity"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "F4/80", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Input:
Sentence: Our data underscore the major role of PPARa in regulation of hepatic lipid and xenobiotic metabolism in human liver and reveal a marked immuno-suppressive/anti-inflammatory effect of PPARa in human liver slices that may be therapeutically relevant for non-alcoholic fatty liver disease .

## Item biored:test:810
Example input:
Sentence: Coenzyme Q10 significantly compensated deficits in the antioxidant defense mechanisms ( reduced glutathione level and superoxide dismutase activity ) , suppressed lipid peroxidation , decreased the elevations of tumor necrosis factor-alpha , nitric oxide and platinum ion concentration , and attenuated the reductions of selenium and zinc ions in renal tissue resulted from cisplatin administration .

Example answer:
{"entities": [{"text": "Coenzyme Q10", "type": "ChemicalEntity"}, {"text": "glutathione", "type": "ChemicalEntity"}, {"text": "superoxide dismutase", "type": "GeneOrGeneProduct"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "tumor necrosis factor-alpha", "type": "GeneOrGeneProduct"}, {"text": "nitric oxide", "type": "ChemicalEntity"}, {"text": "platinum", "type": "ChemicalEntity"}, {"text": "selenium", "type": "ChemicalEntity"}, {"text": "zinc", "type": "ChemicalEntity"}, {"text": "cisplatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: FASN activity was measured by monitoring oxidation of nicotinamide adenine dinucleotide phosphate at a wavelength of 340 nm , and intracellular free fatty acid levels were detected using a Free Fatty Acid Quantification kit .

Example answer:
{"entities": [{"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "nicotinamide adenine dinucleotide phosphate", "type": "ChemicalEntity"}, {"text": "free fatty acid", "type": "ChemicalEntity"}, {"text": "Free Fatty Acid", "type": "ChemicalEntity"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Valproic acid I : time course of lipid peroxidation biomarkers , liver toxicity , and valproic acid metabolite levels in rats .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "liver toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "valproic acid", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: The expression of NEK2 , phospho-AKT and MMP-2 was evaluated by immunohistochemistry in 63 cases of HCC and matched adjacent non-tumorous liver tissues .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A repeat work-up revealed further elevations in aminotransferase levels , and liver biopsy revealed evidence of moderate-to-severe drug toxicity .

Example answer:
{"entities": [{"text": "aminotransferase", "type": "ChemicalEntity"}, {"text": "drug toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Histological analyses of apoptosis , proliferation , angiogenesis and infarct zone assessments were performed using terminal deoxynucleotidyltransferase-mediated dUTP nick-end labelling ( TUNEL ) staining , BrdU immunostaining , a-smooth muscle actin ( a-SMA ) /CD31 immunostaining and Masson 's trichrome staining , respectively .

Example answer:
{"entities": [{"text": "infarct", "type": "DiseaseOrPhenotypicFeature"}, {"text": "terminal", "type": "GeneOrGeneProduct"}, {"text": "dUTP", "type": "ChemicalEntity"}, {"text": "a-smooth muscle actin", "type": "GeneOrGeneProduct"}, {"text": "a-SMA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Liver toxicity was evaluated based on serum levels of alpha-glutathione S-transferase ( alpha-GST ) and by histology .

Example answer:
{"entities": [{"text": "Liver toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alpha-glutathione S-transferase", "type": "GeneOrGeneProduct"}, {"text": "alpha-GST", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Oxidative stress was assessed by determining plasma and liver levels of 15-F ( 2t ) -IsoP , lipid hydroperoxides ( LPO ) , and thiobarbituric acid reactive substances ( TBARs ) .

Example answer:
{"entities": [{"text": "15-F ( 2t ) -IsoP", "type": "ChemicalEntity"}, {"text": "lipid hydroperoxides", "type": "ChemicalEntity"}, {"text": "LPO", "type": "ChemicalEntity"}, {"text": "thiobarbituric acid reactive substances", "type": "ChemicalEntity"}, {"text": "TBARs", "type": "ChemicalEntity"}]}

Input:
Sentence: The lipid peroxidation indicators including antisuperoxideanion ( ASAFR ) , hydroxyl free radical ( .OH ) , superoxide dismutase ( SOD ) , malondialdehyde and glutathione S-transferase ( GST ) were determined with kits , and matrix metalloproteinase-2 and 9 ( MMP-2/9 ) activities in liver were analyzed with gelatin zymography and in situ fluorescent zymography respectively .

## Item biored:test:978
Example input:
Sentence: In this work the effect of CAA on human proximal tubule cells in primary culture ( hRPTEC ) was investigated .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "hRPTEC", "type": "CellLine"}]}

Example input:
Sentence: The effects of CAA on cysteine protease activities and thiols could be reproduced in cell lysate .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "cysteine protease", "type": "GeneOrGeneProduct"}, {"text": "thiols", "type": "ChemicalEntity"}]}

Example input:
Sentence: GADD45A-expressing HSCs failed to long-term reconstitute the blood of recipients by inducing multilineage differentiation in vivo .

Example answer:
{"entities": [{"text": "GADD45A-expressing", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Growth arrest and DNA-damage-inducible 45 alpha ( GADD45A ) is induced by genotoxic stress in HSCs .

Example answer:
{"entities": [{"text": "Growth arrest and DNA-damage-inducible 45 alpha", "type": "GeneOrGeneProduct"}, {"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Notably , following treatment with Hsp27 siRNA or pcDNA3.1-Hsp27 , it was found that iopamidol enhanced or weakened the upregulation of Bax/caspase-3 and downregulation of Bcl-2 in the HK2 cells , respectively .

Example answer:
{"entities": [{"text": "Hsp27", "type": "GeneOrGeneProduct"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "Bax/caspase-3", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Acidification , which slowed the reaction of CAA with thiol donors , could also attenuate effects of CAA on necrosis markers , thiol depletion and cysteine protease inhibition in living cells .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "thiol", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cysteine protease", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These data indicate that genotoxic stress-induced GADD45A expression in HSCs prevents their fatal transformation by directing them into differentiation and thereby clearing them from the system .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further study revealed that the effect of Sal on renal interstitial fibrosis is associated with the lower expression of TLR4 , p-IkappaBalpha , p-NF-kappaB and mitogen-activated protein kinases ( MAPK ) , both in vivo and in vitro .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinases", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CAA reduced hRPTEC cell number and protein , induced a loss in free intracellular thiols and an increase in necrosis markers .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "hRPTEC", "type": "CellLine"}, {"text": "thiols", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In this study , we determined the effects of SAA on hepatic stellate cells ( HSCs ) , the main fibrogenic cell type of the liver .

## Item biored:test:963
Example input:
Sentence: The signal transduction target upon interleukin 1 beta ( IL1beta ) stimulation , the nuclear factor of kappa B ( NFkappaB ) activation , supports cancer development , signal transduction in which is mediated by FS-7 cell-associated cell surface antigen ( FAS ) signaling .

Example answer:
{"entities": [{"text": "interleukin 1 beta", "type": "GeneOrGeneProduct"}, {"text": "IL1beta", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor of kappa B", "type": "GeneOrGeneProduct"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "FS-7 cell-associated cell surface antigen", "type": "GeneOrGeneProduct"}, {"text": "FAS", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further studies indicated that the CSF-1/CSF-1R axis contributed significantly to IL-3-induced CD11c+ cell generation through enhancing c-Fos-associated monopoiesis .

Example answer:
{"entities": [{"text": "CSF-1/CSF-1R", "type": "GeneOrGeneProduct"}, {"text": "IL-3-induced", "type": "GeneOrGeneProduct"}, {"text": "CD11c+", "type": "GeneOrGeneProduct"}, {"text": "c-Fos-associated", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Coincidentally , cdk inhibitors p27Kip1 and p57Kip2 were upregulated in the Ras transgenic lenses but not in the corneas .

Example answer:
{"entities": [{"text": "cdk", "type": "GeneOrGeneProduct"}, {"text": "p27Kip1", "type": "GeneOrGeneProduct"}, {"text": "p57Kip2", "type": "GeneOrGeneProduct"}, {"text": "Ras", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Semiquantitative assessment of the density of NOX4 colabeling with lectin-stained retinal ECs was determined by immunolabeling of retinal cryosections from P18 pups in OIR or in RA .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "lectin-stained", "type": "GeneOrGeneProduct"}, {"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Collectively , these findings reveal a role for CSF-1 in mediating the IL-3 hematopoietic pathway through monopoiesis , which regulates expansion of CD11c+ macrophages .

Example answer:
{"entities": [{"text": "CSF-1", "type": "GeneOrGeneProduct"}, {"text": "IL-3", "type": "GeneOrGeneProduct"}, {"text": "CD11c+", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Endothelial NADPH oxidase 4 mediates vascular endothelial growth factor receptor 2-induced intravitreal neovascularization in a rat model of retinopathy of prematurity .

Example answer:
{"entities": [{"text": "NADPH oxidase 4", "type": "GeneOrGeneProduct"}, {"text": "vascular endothelial growth factor receptor", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "retinopathy of prematurity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Activation of the fibroblast growth factor ( FGF ) signaling pathway induces the corneal epithelial cells to proliferate and the lens epithelial cells to exit the cell cycle .

Example answer:
{"entities": [{"text": "fibroblast growth factor", "type": "GeneOrGeneProduct"}, {"text": "FGF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Association study of complement factor H , C2 , CFB , and C3 and age-related macular degeneration in a Han Chinese population .

Example answer:
{"entities": [{"text": "complement factor H", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}, {"text": "age-related macular degeneration", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : Genes in the complement pathway , including complement factor H ( CFH ) , C2/BF , and C3 , have been reported to be associated with age-related macular degeneration ( AMD ) .

Example answer:
{"entities": [{"text": "complement factor H", "type": "GeneOrGeneProduct"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2/BF", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}, {"text": "age-related macular degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: PURPOSE : Complement factor I ( CFI ) plays an important role in complement activation pathways and is known to affect the development of uveitis .

## Item biored:test:1006
Example input:
Sentence: B cells overexpressing Myc displayed constitutively higher levels of activated CD79a , Btk , Plcg2 and Erk1/2 .

Example answer:
{"entities": [{"text": "Myc", "type": "GeneOrGeneProduct"}, {"text": "CD79a", "type": "GeneOrGeneProduct"}, {"text": "Btk", "type": "GeneOrGeneProduct"}, {"text": "Plcg2", "type": "GeneOrGeneProduct"}, {"text": "Erk1/2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , accumulated F4/80 ( + ) cells in the liver metastasis were not BM-derived F4/80 ( + ) cells , but mainly resident hepatic F4/80 ( + ) cells , and these resident hepatic F4/80 ( + ) cells were positive for TGF-b1 .

Example answer:
{"entities": [{"text": "F4/80", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results suggested that resident hepatic macrophages induced liver metastasis formation by induction of TGF-b1 through AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In response to IL-2 , these CD25 ( + ) Tfh cells increased expression of costimulatory molecules ICOS or OX40 , upregulated transcription factor cMaf , produced cytokines IL-21 , IL-17 , and IL-10 , and raised the levels of antiapoptotic protein Bcl2 .

Example answer:
{"entities": [{"text": "IL-2", "type": "GeneOrGeneProduct"}, {"text": "CD25", "type": "GeneOrGeneProduct"}, {"text": "ICOS", "type": "GeneOrGeneProduct"}, {"text": "OX40", "type": "GeneOrGeneProduct"}, {"text": "cMaf", "type": "GeneOrGeneProduct"}, {"text": "IL-21", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "Bcl2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of NEK2 , phospho-AKT and MMP-2 was evaluated by immunohistochemistry in 63 cases of HCC and matched adjacent non-tumorous liver tissues .

Example answer:
{"entities": [{"text": "NEK2", "type": "GeneOrGeneProduct"}, {"text": "MMP-2", "type": "GeneOrGeneProduct"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Input:
Sentence: This was endorsed by elevated hepatic expression of key immune cell and inflammatory markers .

## Item biored:test:1025
Example input:
Sentence: Both polymorphisms were in strong linkage disequilibrium ( D ' = 0.71 , P < .001 ) , and the 3R/-6 base pair ( bp ) haplotype showed a significant overall survival benefit compared with the most prevalent haplotype 2R/+6bp ( HR = 0.42 ; 95 % CI , 0.20 to 0.85 ; P = .017 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The identification of around 7 % of homozygotes for the frameshift mutation in our Caucasian population suggests the existence of an interindividual variation of the CYP2F1 activity and , consequently , the possibility of interindividual differences in the toxic response to some pneumotoxicants and in the susceptibility to certain chemically induced diseases .

Example answer:
{"entities": [{"text": "CYP2F1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A common single nucleotide polymorphism ( SNP ) , G472A , codes for a Val158Met substitution and results in a fourfold down regulation of enzyme activity .

Example answer:
{"entities": [{"text": "G472A", "type": "SequenceVariant"}, {"text": "Val158Met", "type": "SequenceVariant"}]}

Example input:
Sentence: A detailed analysis of the DNA breakpoints in the two genes , previously characterized by other groups , validated the observation that Alu-mediated unequal recombination is the main type of deletion in MSH2 ( n=34 ) , but not in MLH1 ( n=21 ) ( P < 0.0001 ) .

Example answer:
{"entities": [{"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "MLH1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The AS isoform lacks exon 8 , and is deduced to contain 49 amino acid changes in the membrane-distal portion of the extracellular domain , where considerable amino acid changes are known in CD72 ( c ) allele associated with murine SLE .

Example answer:
{"entities": [{"text": "CD72", "type": "GeneOrGeneProduct"}, {"text": "murine", "type": "OrganismTaxon"}, {"text": "SLE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These studies have produced intriguing but inconsistent results , potentially because the known functional variants : ADRB1 Arg389Gly and Gly49Ser , ADRB2 Arg16Gly and Gln27Glu , and ADRB3 Arg64Trp provided an incomplete picture of the total functional diversity at these genes .

Example answer:
{"entities": [{"text": "ADRB1", "type": "GeneOrGeneProduct"}, {"text": "Arg389Gly", "type": "SequenceVariant"}, {"text": "Gly49Ser", "type": "SequenceVariant"}, {"text": "ADRB2", "type": "GeneOrGeneProduct"}, {"text": "Arg16Gly", "type": "SequenceVariant"}, {"text": "Gln27Glu", "type": "SequenceVariant"}, {"text": "ADRB3", "type": "GeneOrGeneProduct"}, {"text": "Arg64Trp", "type": "SequenceVariant"}]}

Example input:
Sentence: Linkage disequilibrium analysis indicates that D90A homozygotes and heterozygotes share a rare haplotype and are all descended from a single ancient founder ( alpha 0.974 ) c.895 generations ago .

Example answer:
{"entities": [{"text": "D90A", "type": "SequenceVariant"}]}

Example input:
Sentence: We investigated the mechanisms responsible for the functional disparity on B cells between a wild-type p17 ( refp17 ) and a vp17 named S75X .

Example answer:
{"entities": [{"text": "p17", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}]}

Example input:
Sentence: The ratio of AS/common isoforms was strikingly increased in individuals with * 2/ * 2 genotype when compared with * 1/ * 1 ( P=0.000038 ) or * 1/ * 2 ( P=0.0085 ) genotypes .

Example answer:
{"entities": []}

Example input:
Sentence: A pathogenic implication of this substitution , which is conserved in primates and rodents , can not be ruled out completely .

Example answer:
{"entities": []}

Input:
Sentence: Despite common mechanistic similarities between the isoforms , the extent of their redundancy is unclear .

## Item biored:test:971
Example input:
Sentence: The MLH1 -93 variant allele was also over-represented in t-AML cases when compared to de novo AML cases ( 36.9 % , n = 420 ) and healthy controls ( 36.3 % , n = 952 ) , and was associated with a significantly increased risk of developing t-AML ( odds ratio 5.31 , 95 % confidence interval 1.40 to 20.15 ) , but only in patients previously treated with a methylating agent .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "AML", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Additionally , when PSA genotype was cross classified with CAG repeat , significantly more cases than both BPH and population controls were observed to have a short ( < 22 ) CAG/GG genotype ( P = 0.006 ) .

Example answer:
{"entities": [{"text": "PSA", "type": "GeneOrGeneProduct"}, {"text": "CAG repeat", "type": "SequenceVariant"}, {"text": "BPH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Significantly lower frequency of the A-C-C-G with higher frequency of A-C-A-G haplotypes was also noticed in subjects with DS ( P value =0.02089 and 0.00588 respectively ) .

Example answer:
{"entities": [{"text": "DS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A relatively high frequency of germ-line genomic rearrangements in MLH1 and MSH2 has been reported among Lynch Syndrome ( HNPCC ) patients from different ethnic populations .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "MSH2", "type": "GeneOrGeneProduct"}, {"text": "Lynch Syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HNPCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: RESULTS : Carrier frequency of the MLH1 -93 variant was higher in patients who developed therapy related acute myeloid leukaemia ( t-AML ) ( 75.0 % , n = 12 ) or breast cancer ( 53.3 % .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "acute myeloid leukaemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "breast cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Homozygosity for c.2607C > A was also identified in an unrelated but haplotypically identical patient with an unusually favorable outcome despite severe neonatal-onset GE .

Example answer:
{"entities": [{"text": "c.2607C > A", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "GE", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We found the frequency of the three different genotypes of GSTP1 Ile105Val in our ethnic Kashmir population , i.e. , Ile/Ile , Ile/Val and Val/Val , to be 52.4 , 33.3 and 14.3 % among prostate cancer cases , 48.5 , 37.5 and 14 % among benign prostate hyperplasia cases and 73.8 , 21.3 and 5 % in the control population , respectively .

Example answer:
{"entities": [{"text": "GSTP1", "type": "GeneOrGeneProduct"}, {"text": "Ile105Val", "type": "SequenceVariant"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "benign prostate hyperplasia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , patients with recurrent VKH syndrome had lower frequencies of the G allele and GG homozygosity in CFI-rs7356506 when compared to the controls ( p=0.016 , odds ratio [ OR ] =0.429 , 95 % confidence interval [ CI ] =0.212-0.871 ; p=0.014 , OR=0.364 , 95 % CI=0.158-0.837 , respectively ) .

## Item biored:test:1021
Example input:
Sentence: There was a smaller excess of MB in antiplatelet users vs nonusers with ICH ( OR , 1.7 ; 95 % CI , 1.3-2.3 ; P < 0.001 ) , but findings were similar for antiplatelet users with IS/TIA ( OR , 1.4 ; 95 % CI , 1.2-1.7 ; P < 0.001 ; P difference=0.25 ) .

Example answer:
{"entities": [{"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The subjects were metabolically characterized by oral glucose tolerance test with glucose , insulin , proinsulin , and C-peptide measurements .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "proinsulin", "type": "ChemicalEntity"}, {"text": "C-peptide", "type": "ChemicalEntity"}]}

Example input:
Sentence: Moreover , in studies of 238 middle-aged glucose tolerant subjects , of 226 glucose tolerant offspring of Type II diabetic patients and of 367 young healthy subjects , the carriers of the polymorphism did not differ from non-carriers in glucose induced serum insulin or C-peptide responses .

Example answer:
{"entities": [{"text": "II diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "and", "type": "OrganismTaxon"}, {"text": "or", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : LAT and HAT groups were matched in age , obesity , insulin , and glucose , and had similar expression of insulin-related genes ( InsR , IRS-1 ) .

Example answer:
{"entities": [{"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "glucose", "type": "ChemicalEntity"}, {"text": "insulin-related", "type": "GeneOrGeneProduct"}, {"text": "InsR", "type": "GeneOrGeneProduct"}, {"text": "IRS-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : In a pooled analysis of 1460 ICH and 3817 IS/TIA , MB were more frequent in ICH vs IS/TIA in all treatment groups , but the excess increased from 2.8 ( odds ratio ; range , 2.3-3.5 ) in nonantithrombotic users to 5.7 ( range , 3.4-9.7 ) in antiplatelet users and 8.0 ( range , 3.5-17.8 ) in warfarin users ( P difference=0.01 ) .

Example answer:
{"entities": [{"text": "ICH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IS/TIA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "MB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Based on fasting plasma analysis , obese subjects were grouped as Low Acylation Stimulating protein ( ASP ) and Triglyceride ( TG ) ( LAT ) vs High ASP and TG ( HAT ) .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Acylation Stimulating protein", "type": "GeneOrGeneProduct"}, {"text": "ASP", "type": "GeneOrGeneProduct"}, {"text": "Triglyceride", "type": "ChemicalEntity"}, {"text": "TG", "type": "ChemicalEntity"}]}

Example input:
Sentence: The homeostasis model assessment of insulin resistance also differed significantly among groups ( F ( 33 ) = 4.92 ; P = .01 ) ( clozapine > olanzapine > risperidone ) ( clozapine vs risperidone , t ( 33 ) = 2.94 ; P = .006 ; olanzapine vs risperidone , t ( 33 ) = 2.42 ; P = .02 ) .

Example answer:
{"entities": [{"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: There was a significant difference in insulin sensitivity index among groups ( F ( 33 ) = 10.66 ; P < .001 ) ( clozapine < olanzapine < risperidone ) , with subjects who received clozapine and olanzapine exhibiting significant insulin resistance compared with subjects who were treated with risperidone ( clozapine vs risperidone , t ( 33 ) = -4.29 ; P < .001 ; olanzapine vs risperidone , t ( 33 ) = -3.62 ; P = .001 [ P < .001 ] ) .

Example answer:
{"entities": [{"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}, {"text": "insulin resistance", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Fasting serum insulin concentrations differed among groups ( F ( 33 ) = 3.35 ; P = .047 ) ( clozapine > olanzapine > risperidone ) with significant differences between clozapine and risperidone ( t ( 33 ) = 2.32 ; P = .03 ) and olanzapine and risperidone ( t ( 33 ) = 2.15 ; P = .04 ) .

Example answer:
{"entities": [{"text": "insulin", "type": "ChemicalEntity"}, {"text": "clozapine", "type": "ChemicalEntity"}, {"text": "olanzapine", "type": "ChemicalEntity"}, {"text": "risperidone", "type": "ChemicalEntity"}]}

Example input:
Sentence: Insulin secretion was not affected by the variants ( different secretion parameters , all p > or= 0.08 ) .

Example answer:
{"entities": [{"text": "Insulin", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Plasma insulin did not differ between groups .

## Item biored:test:983
Example input:
Sentence: A sublethal dose of Smac mimetic BV6 induces cIAP1 and cIAP2 degradation to increase tumor cell sensitivity to radiation-induced cell death in vitro and to enhance radiation-mediated suppression of STS xenografts in vivo .

Example answer:
{"entities": [{"text": "Smac", "type": "GeneOrGeneProduct"}, {"text": "BV6", "type": "ChemicalEntity"}, {"text": "cIAP1", "type": "GeneOrGeneProduct"}, {"text": "cIAP2", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "STS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Inhibition of caspases , RIP1 , or RIP3 blocks radiation/TNFa-induced cell death , whereas inhibition of RIP1 blocks TNFa-induced caspase activation , suggesting that caspases and RIP1 act sequentially to mediate the non-compensatory cell death pathways .

Example answer:
{"entities": [{"text": "caspases", "type": "GeneOrGeneProduct"}, {"text": "RIP1", "type": "GeneOrGeneProduct"}, {"text": "RIP3", "type": "GeneOrGeneProduct"}, {"text": "TNFa-induced", "type": "GeneOrGeneProduct"}, {"text": "caspase", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the present study , we demonstrate that NF-kappaB , whether activated by recombinant human tumor necrosis factor ( TNF ) -alpha or by ectopic expression of the p65 subunit , is involved in extracellular matrix adhesion and invasion of osteotropic PC-3 and C4-2B , but not LNCaP , cells .

Example answer:
{"entities": [{"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tumor necrosis factor ( TNF ) -alpha", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "PC-3", "type": "CellLine"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "LNCaP", "type": "CellLine"}]}

Example input:
Sentence: Furthermore , Sal treatment significantly decreases the release of inflammatory cytokines and inhibits the TLR4/NF-kappaB and MAPK signaling pathways .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4/NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CAA reduced hRPTEC cell number and protein , induced a loss in free intracellular thiols and an increase in necrosis markers .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "hRPTEC", "type": "CellLine"}, {"text": "thiols", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Finally , we found that Sag deletion inactivates Kras ( G12D ) activity and block the MAPK signaling pathway , together with accumulated p16 , to induce senescence .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Input:
Sentence: In primary hepatocytes , SAA also activated MAP kinases , but did not induce relevant cell death after NF-kappaB inhibition .

## Item biored:test:910
Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Whole-Organism Developmental Expression Profiling Identifies RAB-28 as a Novel Ciliary GTPase Associated with the BBSome and Intraflagellar Transport .

Example answer:
{"entities": [{"text": "RAB-28", "type": "GeneOrGeneProduct"}, {"text": "GTPase", "type": "GeneOrGeneProduct"}, {"text": "BBSome", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Our recent study showed that SAG/RBX2 E3 ubiquitin ligase regulates apoptosis and vasculogenesis by promoting degradation of NOXA and NF1 , and co-operates with Kras to promote lung tumorigenesis by activating NFkappaB and mTOR pathways via targeted degradation of tumor suppressive substrates including IkappaB , DEPTOR , p21 and p27 .

Example answer:
{"entities": [{"text": "SAG/RBX2", "type": "GeneOrGeneProduct"}, {"text": "E3 ubiquitin ligase", "type": "GeneOrGeneProduct"}, {"text": "NOXA", "type": "GeneOrGeneProduct"}, {"text": "NF1", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "lung tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "IkappaB", "type": "GeneOrGeneProduct"}, {"text": "DEPTOR", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The expression of bone morphogenetic protein ( Bmp ) genes , such as Bmp4 and Bmp7 , was also ectopically induced in the epithelia of the URS in the b-catenin GOF mutants .

Example answer:
{"entities": [{"text": "bone morphogenetic protein", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}, {"text": "Bmp4", "type": "GeneOrGeneProduct"}, {"text": "Bmp7", "type": "GeneOrGeneProduct"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both baseline and NRG-1 beta-induced migration were erbB-dependent and required the action of MEK 1/2 , SAPK/JNK , PI-3 kinase , Src family kinases and ROCK-I/II .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB-dependent", "type": "GeneOrGeneProduct"}, {"text": "MEK 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "PI-3 kinase", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "ROCK-I/II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here we investigated the role of Sag/Rbx2 E3 ligase in cellular senescence and immortalization of mouse embryonic fibroblasts ( MEFs ) and report that Sag is required for proper cell proliferation and Kras ( G12D ) -induced immortalization .

Example answer:
{"entities": [{"text": "Sag/Rbx2", "type": "GeneOrGeneProduct"}, {"text": "E3 ligase", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "SequenceVariant"}]}

Example input:
Sentence: Recombinant OGT bearing the p.Arg284Pro mutation was prone to unfolding and exhibited reduced glycosylation activity against a complex array of glycosylation substrates and proteolytic processing of the transcription factor host cell factor 1 , which is also encoded by an XLID-associated gene .

Example answer:
{"entities": [{"text": "OGT", "type": "GeneOrGeneProduct"}, {"text": "p.Arg284Pro", "type": "SequenceVariant"}, {"text": "host cell factor 1", "type": "GeneOrGeneProduct"}, {"text": "XLID-associated", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The differentiation induction by GADD45A was transmitted by activating p38 Mitogen-activated protein kinase ( MAPK ) signaling and allowed the generation of megakaryocytic-erythroid , myeloid , and lymphoid lineages .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}, {"text": "p38 Mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We have shown that MPNSTs express neuregulin-1 ( NRG-1 ) beta isoforms , which promote Schwann cell migration during development , and NRG-1 alpha isoforms , whose effects on Schwann cells are poorly understood .

Example answer:
{"entities": [{"text": "MPNSTs", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuregulin-1 ( NRG-1 ) beta", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Embryos homozygous for a GBT insertion within neuregulin 2a ( nrg2a ) revealed a novel requirement for a Neuregulin 2a ( Nrg2a ) -ErbB2/3-AKT signaling pathway governing the apicobasal organization of a subset of epidermal cells during median fin fold ( MFF ) morphogenesis .

## Item biored:test:930
Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: CONCLUSIONS : Hypomorphic MKS3/TMEM67 mutations cause NPHP with liver fibrosis ( NPHP11 ) .

Example answer:
{"entities": [{"text": "MKS3/TMEM67", "type": "GeneOrGeneProduct"}, {"text": "NPHP with liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NPHP11", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In IEC-6 crypt cells and jejunum enteroids quantitative RT-PCR showed a time- and dose-dependent upregulation of lpa2 in response to gamma-irradiation that was abolished by mutation of the NF-kappaB site in the lpa2 promoter or by inhibition of ATM/ATR kinases with CGK-733 , suggesting that lpa2 is a DNA damage response gene upregulated by ATM via NF-kappaB .

Example answer:
{"entities": [{"text": "IEC-6", "type": "CellLine"}, {"text": "lpa2", "type": "GeneOrGeneProduct"}, {"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "ATM/ATR kinases", "type": "GeneOrGeneProduct"}, {"text": "CGK-733", "type": "ChemicalEntity"}, {"text": "ATM", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CCK and other GI-hormones/neurotransmitters/growth-factors activate PAK2 via small GTPases ( CDC42/Rac1 ) , PKC and SFK but not cytosolic calcium or PI3K .

Example answer:
{"entities": [{"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "GI-hormones/neurotransmitters/growth-factors", "type": "ChemicalEntity"}, {"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "small GTPases", "type": "GeneOrGeneProduct"}, {"text": "CDC42/Rac1", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "SFK", "type": "GeneOrGeneProduct"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "PI3K", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A model of liver metastasis was developed by intrasplenic injection of mouse colon cancer ( CMT-93 ) into AT1a knockout mice ( AT1aKO ) and wild-type ( C57BL/6 ) mice ( WT ) .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mouse", "type": "OrganismTaxon"}, {"text": "colon cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CMT-93", "type": "CellLine"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "AT1aKO", "type": "GeneOrGeneProduct"}, {"text": "C57BL/6", "type": "CellLine"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAK2 was activated by some pancreatic growth-factors [ EGF , PDGF , bFGF ] , by secretagogues activating phospholipase-C ( PLC ) [ CCK , carbachol , bombesin ] and by post-receptor stimulants activating PKC [ TPA ] , but not agents only mobilizing cellular calcium or increasing cyclic AMP .

Example answer:
{"entities": [{"text": "PAK2", "type": "GeneOrGeneProduct"}, {"text": "pancreatic growth-factors", "type": "GeneOrGeneProduct"}, {"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "PDGF", "type": "GeneOrGeneProduct"}, {"text": "bFGF", "type": "GeneOrGeneProduct"}, {"text": "phospholipase-C", "type": "GeneOrGeneProduct"}, {"text": "PLC", "type": "GeneOrGeneProduct"}, {"text": "CCK", "type": "GeneOrGeneProduct"}, {"text": "carbachol", "type": "ChemicalEntity"}, {"text": "bombesin", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "TPA", "type": "ChemicalEntity"}, {"text": "calcium", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We integrated chromatin-immunoprecipitation-coupled sequencing and microarray expression profiling in TMPRSS2-ERG gene rearrangement positive DUCaP cells with the GWAS PCa risk SNPs catalog to identify disease susceptibility SNPs localized within functional androgen receptor-binding sites ( ARBSs ) .

Example answer:
{"entities": [{"text": "TMPRSS2-ERG", "type": "GeneOrGeneProduct"}, {"text": "DUCaP", "type": "CellLine"}, {"text": "PCa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "androgen", "type": "GeneOrGeneProduct"}, {"text": "ARBSs", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Finally , several putative new target genes of PPARa were identified that were commonly induced by PPARa activation in the two human liver model systems , including TSKU , RHOF , CA12 and VSIG10L .

## Item biored:test:990
Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Bach1 siRNA attenuates bleomycin-induced pulmonary fibrosis by modulating oxidative stress in mice .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "bleomycin-induced", "type": "ChemicalEntity"}, {"text": "pulmonary fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Molecular dynamic simulations of structural changes induced by L1503R indicated that the mean value of all-atom root-mean-squared-deviation was shifted from those with wild type or another mutation L1503Q that has been reported to be a group II mutation , which is susceptible to ADAMTS13 proteolysis .

Example answer:
{"entities": [{"text": "L1503R", "type": "SequenceVariant"}, {"text": "L1503Q", "type": "SequenceVariant"}, {"text": "ADAMTS13", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: VDAC1 regulates mitochondrial uptake across the outer membrane and mitochondrial outer membrane permeabilization ( MOMP ) .

Example answer:
{"entities": [{"text": "VDAC1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Specific knockdown of OPRM1 confers L-asparaginase resistance , validating our genome-wide retroviral shRNA library screening data .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}]}

Example input:
Sentence: CBMCs were stimulated with innate ( Lipid A , LpA ; Peptidoglycan , Ppg ) , adaptive stimuli ( house dust mite Dermatophagoides pteronyssinus 1 , Derp1 ) or mitogen ( phytohemagglutinin , PHA ) .

Example answer:
{"entities": [{"text": "Lipid A", "type": "ChemicalEntity"}, {"text": "LpA", "type": "ChemicalEntity"}, {"text": "Peptidoglycan", "type": "ChemicalEntity"}, {"text": "Ppg", "type": "ChemicalEntity"}, {"text": "Dermatophagoides pteronyssinus 1", "type": "GeneOrGeneProduct"}, {"text": "Derp1", "type": "GeneOrGeneProduct"}, {"text": "phytohemagglutinin", "type": "ChemicalEntity"}, {"text": "PHA", "type": "ChemicalEntity"}]}

Example input:
Sentence: Consistent with this premise , patient leukemic cells with relatively high levels of OPRM1 are more sensitive to L-asparaginase treatment compared to OPRM1-depleted leukemic cells , further indicating that OPRM1 loss has a crucial role in L-asparaginase resistance in leukemic patients .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Here we show that the LRR-RLK MOL1 is necessary for cambium homeostasis in Arabidopsis thaliana .

## Item biored:test:974
Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : Genes in the complement pathway , including complement factor H ( CFH ) , C2/BF , and C3 , have been reported to be associated with age-related macular degeneration ( AMD ) .

Example answer:
{"entities": [{"text": "complement factor H", "type": "GeneOrGeneProduct"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2/BF", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}, {"text": "age-related macular degeneration", "type": "DiseaseOrPhenotypicFeature"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Our findings further confirmed that different kind of mutations might cause different ocular phenotype , and clearly clinical phenotype classification might increase the mutation detection rate of the PAX6 gene .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We identified such a mechanism as the origin of the mild to asymptomatic phenotype observed in cystic fibrosis patients homozygous for the E831X mutation ( 2623G > T ) in the CFTR gene .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "E831X", "type": "SequenceVariant"}, {"text": "2623G > T", "type": "SequenceVariant"}, {"text": "CFTR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Input:
Sentence: CONCLUSIONS : Our results indicate that CFI polymorphisms are not significantly associated with VKH syndrome ; nevertheless , we identified a trend for the association of CFI-7356506 with VKH syndrome that depends on the recurrent status and the complicated cataract status but not on the steroid-sensitive status .

## Item biored:test:988
Example input:
Sentence: This sole substitution was sufficient to confer constitutive activity to the receptor variant ( PrlR ( I146L ) ) , as assessed in three reconstituted cell models ( Ba/F3 , HEK293 and MCF-7 cells ) by Prl-independent ( i ) PrlR tyrosine phosphorylation , ( ii ) activation of signal transducer and activator of transcription 5 ( STAT5 ) signaling , ( iii ) transcriptional activity toward a Prl-responsive reporter gene , and ( iv ) cell proliferation and protection from cell death .

Example answer:
{"entities": [{"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "I146L", "type": "SequenceVariant"}, {"text": "Ba/F3", "type": "CellLine"}, {"text": "HEK293", "type": "CellLine"}, {"text": "MCF-7", "type": "CellLine"}, {"text": "Prl-independent", "type": "GeneOrGeneProduct"}, {"text": "signal transducer and activator of transcription 5", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "Prl-responsive", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Drosophila ovarian germline stem cells ( GSCs ) are maintained by Dpp signaling and the Pumilio ( Pum ) and Nanos ( Nos ) translational repressors .

Example answer:
{"entities": [{"text": "Drosophila", "type": "OrganismTaxon"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Pumilio", "type": "GeneOrGeneProduct"}, {"text": "Pum", "type": "GeneOrGeneProduct"}, {"text": "Nanos", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: At p18 OIR , semiquantitative assessment of the density of lectin and NOX4 colabeling in retinal vascular ECs was greater in retinal cryosections and activated STAT3 was greater in retinal lysates when compared to the RA-raised pups .

Example answer:
{"entities": [{"text": "OIR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lectin", "type": "GeneOrGeneProduct"}, {"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Re-expression of LKB1 or knockdown of VEGF receptor 2 decreased the overproliferation and -migration observed in LKB1 ( endo-/- ) cells .

Example answer:
{"entities": [{"text": "LKB1", "type": "GeneOrGeneProduct"}, {"text": "VEGF receptor 2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: LPA2 transcripts in Lin ( - ) Sca-1 ( + ) c-Kit ( + ) enriched for bone marrow stem cells were 27- and 5-fold higher than in common myeloid or lymphoid progenitors , respectively .

Example answer:
{"entities": [{"text": "LPA2", "type": "GeneOrGeneProduct"}, {"text": "Lin", "type": "GeneOrGeneProduct"}, {"text": "Sca-1", "type": "GeneOrGeneProduct"}, {"text": "c-Kit", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Following knockdown of PKCalpha , Mz-ChA-1 cells were stimulated with RAMH before evaluating cell growth and extracellular signal-regulated kinase ( ERK ) -1/2 phosphorylation .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "extracellular signal-regulated kinase ( ERK ) -1/2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Here , we show that a single Arginine ( R ) to Glycine ( G ) mutation at position 76 in the refp17 backbone ( p17R76G ) , as in the S75X variant , is per se sufficient to confer a B-cell clonogenic potential to the viral protein and modulate , through activation of the PTEN/PI3K/Akt signaling pathway , different molecules involved in apoptosis inhibition ( CASP-9 , CASP-7 , DFF-45 , NPM , YWHAZ , Src , PAX2 , MAPK8 ) , cell cycle promotion and cancer progression ( CDK1 , CDK2 , CDK8 , CHEK1 , CHEK2 , GSK-3 beta , NPM , PAK1 , PP2C-alpha ) .

Example answer:
{"entities": [{"text": "Arginine ( R ) to Glycine ( G ) mutation at position 76", "type": "SequenceVariant"}, {"text": "p17R76G", "type": "GeneOrGeneProduct"}, {"text": "S75X", "type": "SequenceVariant"}, {"text": "PTEN/PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "CASP-9", "type": "GeneOrGeneProduct"}, {"text": "CASP-7", "type": "GeneOrGeneProduct"}, {"text": "DFF-45", "type": "GeneOrGeneProduct"}, {"text": "NPM", "type": "GeneOrGeneProduct"}, {"text": "YWHAZ", "type": "GeneOrGeneProduct"}, {"text": "Src", "type": "GeneOrGeneProduct"}, {"text": "PAX2", "type": "GeneOrGeneProduct"}, {"text": "MAPK8", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CDK1", "type": "GeneOrGeneProduct"}, {"text": "CDK2", "type": "GeneOrGeneProduct"}, {"text": "CDK8", "type": "GeneOrGeneProduct"}, {"text": "CHEK1", "type": "GeneOrGeneProduct"}, {"text": "CHEK2", "type": "GeneOrGeneProduct"}, {"text": "GSK-3 beta", "type": "GeneOrGeneProduct"}, {"text": "PAK1", "type": "GeneOrGeneProduct"}, {"text": "PP2C-alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Regulation of both targets simultaneously lowers cellular responsiveness to Dpp signaling , forcing the cell to become refractory to the self-renewal signal .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Stem cell homeostasis in shoot and root tips depends on negative regulation by ligand-receptor pairs of the CLE peptide and leucine-rich repeat receptor-like kinase ( LRR-RLK ) families .

## Item biored:test:991
Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : These data support the hypothesis that the common polymorphism at position -93 in the core promoter of MLH1 defines a risk allele for the development of cancer after methylating chemotherapy for Hodgkin lymphoma .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hodgkin lymphoma", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: STUDY DESIGN : Wild-type ( WT ) and superoxide dismutase 1 ( SOD1 ) -overexpressing day 8.75 embryos from nondiabetic WT control with SOD1 transgenic male and diabetic WT female with SOD1 transgenic male were analyzed for ER stress markers : C/EBP-homologous protein ( CHOP ) , calnexin , eukaryotic initiation factor 2a ( eIF2a ) , protein kinase ribonucleic acid ( RNA ) -like ER kinase ( PERK ) , binding immunoglobulin protein , protein disulfide isomerase family A member 3 , kinases inositol-requiring protein-1a ( IRE1a ) , and the X-box binding protein ( XBP1 ) messenger RNA ( mRNA ) splicing .

Example answer:
{"entities": [{"text": "superoxide dismutase 1", "type": "GeneOrGeneProduct"}, {"text": "SOD1", "type": "GeneOrGeneProduct"}, {"text": "diabetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "C/EBP-homologous protein", "type": "GeneOrGeneProduct"}, {"text": "CHOP", "type": "GeneOrGeneProduct"}, {"text": "calnexin", "type": "GeneOrGeneProduct"}, {"text": "eukaryotic initiation factor 2a", "type": "GeneOrGeneProduct"}, {"text": "eIF2a", "type": "GeneOrGeneProduct"}, {"text": "protein kinase ribonucleic acid ( RNA ) -like ER kinase", "type": "GeneOrGeneProduct"}, {"text": "PERK", "type": "GeneOrGeneProduct"}, {"text": "binding immunoglobulin protein", "type": "GeneOrGeneProduct"}, {"text": "protein disulfide isomerase family A member 3", "type": "GeneOrGeneProduct"}, {"text": "kinases inositol-requiring protein-1a", "type": "GeneOrGeneProduct"}, {"text": "IRE1a", "type": "GeneOrGeneProduct"}, {"text": "X-box binding protein", "type": "GeneOrGeneProduct"}, {"text": "XBP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Homozygous carriers of HLX1 promoter SNP rs3806325 showed increased IL-13 and IL-6 ( unstimulated , p < 0.03 ) .

Example answer:
{"entities": [{"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs3806325", "type": "SequenceVariant"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We hypothesised that a common substitution in the basal promoter of MLH1 ( position -93 , rs1800734 ) modifies the risk of cancer after methylating chemotherapy .

Example answer:
{"entities": [{"text": "MLH1", "type": "GeneOrGeneProduct"}, {"text": "rs1800734", "type": "SequenceVariant"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: By unbiased genome-wide RNAi screening , we found that among 10 resistant ALL clones , six hits were for opioid receptor mu 1 ( oprm1 ) , two hits were for carbonic anhydrase 1 ( ca1 ) and another two hits were for ubiquitin-conjugating enzyme E2C ( ube2c ) .

Example answer:
{"entities": [{"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "opioid receptor mu 1", "type": "GeneOrGeneProduct"}, {"text": "oprm1", "type": "GeneOrGeneProduct"}, {"text": "carbonic anhydrase 1", "type": "GeneOrGeneProduct"}, {"text": "ca1", "type": "GeneOrGeneProduct"}, {"text": "ubiquitin-conjugating enzyme E2C", "type": "GeneOrGeneProduct"}, {"text": "ube2c", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Of these , rs11891426 : T > G in an intron of the melanophilin gene ( MLPH ) was within a novel putative auxiliary AR-binding motif , which is enriched in the neighborhood of canonical androgen-responsive elements .

Example answer:
{"entities": [{"text": "rs11891426", "type": "SequenceVariant"}, {"text": "T > G", "type": "SequenceVariant"}, {"text": "melanophilin", "type": "GeneOrGeneProduct"}, {"text": "MLPH", "type": "GeneOrGeneProduct"}, {"text": "AR-binding", "type": "GeneOrGeneProduct"}, {"text": "androgen-responsive", "type": "ChemicalEntity"}]}

Example input:
Sentence: The dual-luciferase reporter assay revealed that the -395A carrier of a 498-bp DNA fragment ( containing the G-395A site ) upstream of the Klotho gene has higher relative luciferase activity than the -395G carrier .

Example answer:
{"entities": [{"text": "-395A", "type": "SequenceVariant"}, {"text": "G-395A", "type": "SequenceVariant"}, {"text": "Klotho", "type": "GeneOrGeneProduct"}, {"text": "-395G", "type": "SequenceVariant"}]}

Example input:
Sentence: Carriers of TBX21 promoter SNP rs17250932 and HLX1 promoter SNP rs2738751 showed reduced or trendwise reduced ( p < 0.07 ) IL-5 , IL-13 and TNF-a secretion after LpA-stimulation .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "rs17250932", "type": "SequenceVariant"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "rs2738751", "type": "SequenceVariant"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "TNF-a", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Input:
Sentence: By employing promoter reporter lines , we reveal that MOL1 is active in a domain that is distinct from the domain of the positively acting CLE41/PXY signaling module .

## Item biored:test:970
Example input:
Sentence: We identified such a mechanism as the origin of the mild to asymptomatic phenotype observed in cystic fibrosis patients homozygous for the E831X mutation ( 2623G > T ) in the CFTR gene .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "E831X", "type": "SequenceVariant"}, {"text": "2623G > T", "type": "SequenceVariant"}, {"text": "CFTR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The non-synonymous SNP rs2230912 ( resulting in amino-acid polymorphism Q460R ) showed the strongest association and has been postulated to be pathogenically relevant .

Example answer:
{"entities": [{"text": "rs2230912", "type": "SequenceVariant"}, {"text": "Q460R", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSION : This study showed that SNPs rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , but not rs7535263 , rs1410996 , or rs2274700 , in CFH were significantly associated with wet AMD in a mainland Han Chinese population .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "rs7535263", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "rs2274700", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: RESULTS : No significant association was found between CFI-rs7356506 polymorphisms and VKH syndrome .

## Item biored:test:1012
Example input:
Sentence: Intracerebroventricular injection of U-II also caused an increase in : food intake at doses of 100 and 1,000 ng/mouse , water intake at doses of 100-10,000 ng/mouse , and horizontal locomotion activity at a dose of 10,000 ng/mouse .

Example answer:
{"entities": [{"text": "U-II", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "STZ", "type": "ChemicalEntity"}]}

Example input:
Sentence: Male Wistar rats were treated by Dex ( 30 u g/kg/day subcutaneously ) or saline for 14 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Dex", "type": "ChemicalEntity"}]}

Example input:
Sentence: Ninety-six Swiss-Webster mice ( 30-35 g , 6-8 wk ) , were randomized into 6 groups 1 ) saline ( control ) , 2 ) NTG immediately after learning , 3 ) NTG 3 h after learning , 4 ) NTG and NIMO , 5 ) vehicle , and 6 ) NIMO alone .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "NTG", "type": "ChemicalEntity"}, {"text": "NIMO", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mice were treated with saline or RAMH for 44 days and tumor volume was measured .

Example answer:
{"entities": [{"text": "Mice", "type": "OrganismTaxon"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Male CD-1 mice were treated with warfarin ( 2 mg/kg over 24 h ) , resulting in a mean ( +/-s.d . )

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "warfarin", "type": "ChemicalEntity"}]}

Example input:
Sentence: The ethanolic extract of Daucus carota seeds ( DCE ) was administered orally in three doses ( 100 , 200 , 400 mg/kg ) for seven successive days to different groups of young and aged mice .

Example answer:
{"entities": [{"text": "extract of Daucus carota seeds", "type": "ChemicalEntity"}, {"text": "DCE", "type": "ChemicalEntity"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "Ato", "type": "ChemicalEntity"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/ K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}]}

Example input:
Sentence: A total of 60 male Wistar albino rats were randomly divided into four groups ( 15/group ) : The control group injected with single doses of normal saline ( i.c.v ) followed 24 h later by BCNU solvent ( i.v ) .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "BCNU", "type": "ChemicalEntity"}]}

Input:
Sentence: METHODS : Adult male mice were provided an alcohol-containing liquid diet for 24 weeks or an isonitrogenous isocaloric control diet .

## Item biored:test:992
Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: Our results reveal that dominant mutations in BICD2 hyperactivate DDB motility and suggest that an imbalance of minus versus plus end-directed microtubule motility in neurons may underlie spinal muscular atrophy .

Example answer:
{"entities": [{"text": "BICD2", "type": "GeneOrGeneProduct"}, {"text": "DDB", "type": "GeneOrGeneProduct"}, {"text": "spinal muscular atrophy", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results indicate that some ARM phenotypes in the b-catenin GOF mutants were caused by abnormal Bmp signaling .

Example answer:
{"entities": [{"text": "ARM", "type": "DiseaseOrPhenotypicFeature"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "Bmp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Bach1 is an important transcriptional repressor that acts by modulating oxidative stress and represents a potential target in the treatment of pulmonary fibrosis ( PF ) .

Example answer:
{"entities": [{"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "pulmonary fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: All these patients had mutations in a catalytic domain in both POLG1 alleles , in either the polymerase or exonuclease domain or both .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "POLG1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CBMCs were stimulated with innate ( Lipid A , LpA ; Peptidoglycan , Ppg ) , adaptive stimuli ( house dust mite Dermatophagoides pteronyssinus 1 , Derp1 ) or mitogen ( phytohemagglutinin , PHA ) .

Example answer:
{"entities": [{"text": "Lipid A", "type": "ChemicalEntity"}, {"text": "LpA", "type": "ChemicalEntity"}, {"text": "Peptidoglycan", "type": "ChemicalEntity"}, {"text": "Ppg", "type": "ChemicalEntity"}, {"text": "Dermatophagoides pteronyssinus 1", "type": "GeneOrGeneProduct"}, {"text": "Derp1", "type": "GeneOrGeneProduct"}, {"text": "phytohemagglutinin", "type": "ChemicalEntity"}, {"text": "PHA", "type": "ChemicalEntity"}]}

Example input:
Sentence: RAMH induced a shift in the localization of PKCalpha expression from the cytosolic domain into the membrane region of Mz-ChA-1 cells .

Example answer:
{"entities": [{"text": "RAMH", "type": "ChemicalEntity"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Mz-ChA-1", "type": "CellLine"}]}

Example input:
Sentence: Chl , like Chd , dorsalizes embryos upon overexpression and is cleaved by BMP1 , which antagonizes this activity .

Example answer:
{"entities": [{"text": "Chl", "type": "GeneOrGeneProduct"}, {"text": "Chd", "type": "GeneOrGeneProduct"}, {"text": "BMP1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Expression of mutated caveolin-1 in caveolin-1-null mouse fibroblasts failed to induce formation of caveolae due to retention of the mutated protein in the endoplasmic reticulum .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "caveolin-1-null", "type": "GeneOrGeneProduct"}, {"text": "mouse", "type": "OrganismTaxon"}]}

Example input:
Sentence: We also demonstrate that the A118D SEA domain mutation causes an intra-molecular structural imbalance that impairs matriptase-2 activation .

Example answer:
{"entities": [{"text": "A118D", "type": "SequenceVariant"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: In particular , we show that MOL1 acts in an opposing manner to the CLE41/PXY module and that changing the domain or level of MOL1 expression both result in disturbed cambium organization .

## Item biored:test:962
Example input:
Sentence: Seven SNPs in CFH and two SNPs in C2 , CFB ' , and C3 were genotyped using the ABI SNaPshot method .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In five patients p.R246Q missense mutation was detected , of which four were homozygous and one was compound heterozygous : g.80_87delT CGCGAAG ( p.A27fsX132 ) and p.R246Q .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "p.R246Q", "type": "SequenceVariant"}, {"text": "g.80_87delT CGCGAAG", "type": "SequenceVariant"}, {"text": "p.A27fsX132", "type": "SequenceVariant"}]}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In this work , we studied the proband in a small nuclear family of Chinese and Dutch/German descent and identified two novel mutations in the type VII collagen gene leading to recessive dystrophic epidermolysis bullosa , Hallopeau-Siemens variant ( HS-RDEB ) .

Example answer:
{"entities": [{"text": "VII collagen", "type": "GeneOrGeneProduct"}, {"text": "recessive dystrophic epidermolysis bullosa", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Hallopeau-Siemens", "type": "DiseaseOrPhenotypicFeature"}, {"text": "HS-RDEB", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The genetic polymorphism rs1052133 , which leads to substitution of the amino acid at codon 326 from Ser to Cys , shows functional differences , namely a decrease in enzyme activity in hOGG1-Cys326 .

Example answer:
{"entities": [{"text": "rs1052133", "type": "SequenceVariant"}, {"text": "326 from Ser to Cys", "type": "SequenceVariant"}, {"text": "hOGG1-Cys326", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: After restricting the candidate region in chromosome 16q22.1 by haplotype analysis , we found that all patients from 52 unrelated Japanese families harbor a heterozygous C -- > T single-nucleotide substitution , 16 nt upstream of the putative translation initiation site of the gene for a hypothetical protein DKFZP434I216 , which we have called `` puratrophin-1 '' ( Purkinje cell atrophy associated protein-1 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "C -- > T", "type": "SequenceVariant"}, {"text": "DKFZP434I216", "type": "GeneOrGeneProduct"}, {"text": "puratrophin-1", "type": "GeneOrGeneProduct"}, {"text": "Purkinje cell atrophy associated protein-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSION : This study showed that SNPs rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , but not rs7535263 , rs1410996 , or rs2274700 , in CFH were significantly associated with wet AMD in a mainland Han Chinese population .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "rs7535263", "type": "SequenceVariant"}, {"text": "rs1410996", "type": "SequenceVariant"}, {"text": "rs2274700", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Identification of a novel WFS1 mutation ( AFF344-345ins ) in Japanese patients with Wolfram syndrome .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Wolfram syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: CFI-rs7356506 polymorphisms associated with Vogt-Koyanagi-Harada syndrome .

## Item biored:test:994
Example input:
Sentence: A heterozygous caveolin-1 c.474delA mutation has been identified in a family with heritable pulmonary arterial hypertension ( PAH ) .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "pulmonary arterial hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the functional aspect , overexpression of FLNBv4 led to upregulation of RANKL , OCN , OPG and RUNX2 , which are closely related to GCT cell survival and differentiation .

Example answer:
{"entities": [{"text": "FLNBv4", "type": "GeneOrGeneProduct"}, {"text": "RANKL", "type": "GeneOrGeneProduct"}, {"text": "OCN", "type": "GeneOrGeneProduct"}, {"text": "OPG", "type": "GeneOrGeneProduct"}, {"text": "RUNX2", "type": "GeneOrGeneProduct"}, {"text": "GCT", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A mouse model of BLM-induced PF was established , and Bach1 siRNA ( 1x109 pfu ) was administered to the mice via the tail vein .

Example answer:
{"entities": [{"text": "mouse", "type": "OrganismTaxon"}, {"text": "BLM-induced", "type": "ChemicalEntity"}, {"text": "PF", "type": "DiseaseOrPhenotypicFeature"}, {"text": "Bach1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: In cultured hRMVECs , knockdown of NOX4 by siRNA transfection inhibited VEGF-induced ROS generation .

Example answer:
{"entities": [{"text": "NOX4", "type": "GeneOrGeneProduct"}, {"text": "VEGF-induced", "type": "GeneOrGeneProduct"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Immunoperoxidase brightfield- and laser-scanning confocal fluorescence microscopy demonstrated increased targeting of alpha-ENaC , beta-ENaC , and gamma-ENaC subunits to the apical plasma membrane in the distal convoluted tubule ( DCT2 ) , connecting tubule , and cortical and medullary collecting duct segments .

Example answer:
{"entities": [{"text": "alpha-ENaC", "type": "GeneOrGeneProduct"}, {"text": "beta-ENaC", "type": "GeneOrGeneProduct"}, {"text": "gamma-ENaC", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The Shh ( CreERT2/+ ) ; b-catenin ( flox ( ex3 ) /+ ) ; BmprIA ( flox/- ) mutants displayed partial restoration of URS elongation compared with the b-catenin GOF mutants .

Example answer:
{"entities": [{"text": "Shh", "type": "GeneOrGeneProduct"}, {"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "BmprIA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Both b-catenin loss- and gain-of-function ( LOF and GOF ) mutants displayed abnormal clefts in the perineal region and hypoplastic elongation of the URS .

Example answer:
{"entities": [{"text": "b-catenin", "type": "GeneOrGeneProduct"}, {"text": "hypoplastic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In LPA2-reconstituted MEF cells lacking LPA1 ' 3 the levels of gamma-H2AX decreased rapidly , whereas in Vector MEF were high and remained sustained .

Example answer:
{"entities": [{"text": "LPA2-reconstituted", "type": "GeneOrGeneProduct"}, {"text": "MEF", "type": "CellLine"}, {"text": "LPA1 ' 3", "type": "GeneOrGeneProduct"}, {"text": "gamma-H2AX", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Chl , like Chd , dorsalizes embryos upon overexpression and is cleaved by BMP1 , which antagonizes this activity .

Example answer:
{"entities": [{"text": "Chl", "type": "GeneOrGeneProduct"}, {"text": "Chd", "type": "GeneOrGeneProduct"}, {"text": "BMP1", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Furthermore , MOL1 but not PXY is able to rescue CLV1 deficiency in the shoot apical meristem .

## Item biored:test:812
Example input:
Sentence: Attenuated expression of LDHA by siRNA or inhibition of LDHA activities by FX11 inhibited cell proliferation , migration , invasion , and promoted cell apoptosis of PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Meanwhile apoptosis related proteins bax and ATF2 were involved in desminopathy patients and desminopathy rat model , but not bcl-2 , bcl-xl or HK2.VDAC1 and desmin are closely relevant in the tissue splices of deminopathies patients and rats with desminopathy at protein lever .

Example answer:
{"entities": [{"text": "bax", "type": "GeneOrGeneProduct"}, {"text": "ATF2", "type": "GeneOrGeneProduct"}, {"text": "desminopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "bcl-2", "type": "GeneOrGeneProduct"}, {"text": "bcl-xl", "type": "GeneOrGeneProduct"}, {"text": "HK2.VDAC1", "type": "GeneOrGeneProduct"}, {"text": "desmin", "type": "GeneOrGeneProduct"}, {"text": "rats", "type": "OrganismTaxon"}]}

Example input:
Sentence: In this study , we found that mice with a genetic deletion of VIPR2 , encoding the VPAC2 receptor , exhibited exacerbated ( MOG35-55 ) -induced EAE compared to wild type mice , characterized by enhanced clinical and histopathological features , increased proinflammatory cytokines ( TNF-alpha , IL-6 , IFN-gamma ( Th1 ) , and IL-17 ( Th17 ) ) and reduced anti-inflammatory cytokines ( IL-10 , TGFbeta , and IL-4 ( Th2 ) ) in the CNS and lymph nodes .

Example answer:
{"entities": [{"text": "mice", "type": "OrganismTaxon"}, {"text": "VIPR2", "type": "GeneOrGeneProduct"}, {"text": "VPAC2 receptor", "type": "GeneOrGeneProduct"}, {"text": "MOG35-55", "type": "GeneOrGeneProduct"}, {"text": "EAE", "type": "DiseaseOrPhenotypicFeature"}, {"text": "proinflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "IFN-gamma", "type": "GeneOrGeneProduct"}, {"text": "IL-17", "type": "GeneOrGeneProduct"}, {"text": "anti-inflammatory cytokines", "type": "GeneOrGeneProduct"}, {"text": "IL-10", "type": "GeneOrGeneProduct"}, {"text": "TGFbeta", "type": "GeneOrGeneProduct"}, {"text": "IL-4", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We postulate that the mechanism of the simvastatinezetimibe-induced hepatotoxicity is the increased simvastatin exposure by ezetimibe inhibition of UGT enzymes .

Example answer:
{"entities": [{"text": "simvastatinezetimibe-induced", "type": "ChemicalEntity"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "simvastatin", "type": "ChemicalEntity"}, {"text": "ezetimibe", "type": "ChemicalEntity"}, {"text": "UGT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , atorvastatin reduced the iopamidol-induced activity of B cell lymphoma-2 ( Bcl-2 ) -associated X protein ( Bax ) /caspase-3 and increased the expression of Bcl-2 in vivo and in vitro .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "B cell lymphoma-2 ( Bcl-2 ) -associated X protein", "type": "GeneOrGeneProduct"}, {"text": "Bax", "type": "GeneOrGeneProduct"}, {"text": "Bcl-2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Compared to that in the normal control , more severe liver inflammation and hepatocyte apoptosis , worse hepatic lipid peroxidation demonstrated by the increased ASAFR , .OH and MDA , but decreased SOD and GST , increased MMP-2/9 activities and VCAM-1 , ICAM-1 and vWF expressions , which revealed obvious LSEC injury and scaffold structure broken , were shown in the model control .

## Item biored:test:993
Example input:
Sentence: Our transient expression study indicates that the Lys198Asn polymorphism may not directly affect ET-1 and big ET-1 production .

Example answer:
{"entities": [{"text": "Lys198Asn", "type": "SequenceVariant"}, {"text": "ET-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further , expression of miRNA biosynthetic machinery including Dicer , Exportin-5 , TRKRA , and TARBP2 were downregulated , while DGCR8 and Ago2 were upregulated in KC mice .

Example answer:
{"entities": [{"text": "Dicer", "type": "GeneOrGeneProduct"}, {"text": "Exportin-5", "type": "GeneOrGeneProduct"}, {"text": "TRKRA", "type": "GeneOrGeneProduct"}, {"text": "TARBP2", "type": "GeneOrGeneProduct"}, {"text": "DGCR8", "type": "GeneOrGeneProduct"}, {"text": "Ago2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Specific knockdown of OPRM1 confers L-asparaginase resistance , validating our genome-wide retroviral shRNA library screening data .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}]}

Example input:
Sentence: CONCLUSIONS : Polymorphisms in TBX21 and HLX1 influenced primarily IL-5 and IL-13 secretion after LpA-stimulation in cord blood suggesting that genetic variations in the transcription factors essential for the T ( H ) 1-pathway may contribute to modified T ( H ) 2-immune responses already early in life .

Example answer:
{"entities": [{"text": "TBX21", "type": "GeneOrGeneProduct"}, {"text": "HLX1", "type": "GeneOrGeneProduct"}, {"text": "IL-5", "type": "GeneOrGeneProduct"}, {"text": "IL-13", "type": "GeneOrGeneProduct"}, {"text": "LpA-stimulation", "type": "ChemicalEntity"}]}

Example input:
Sentence: Collectively , these results extend the pattern of TMPRSS6 mutations associated with IRIDA and functionally demonstrate that mutations affecting protease regions other than the catalytic domain may have a profound impact in the regulatory role of matriptase-2 during iron deficiency .

Example answer:
{"entities": [{"text": "TMPRSS6", "type": "GeneOrGeneProduct"}, {"text": "IRIDA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "matriptase-2", "type": "GeneOrGeneProduct"}, {"text": "iron deficiency", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Thus , our study demonstrates for the first time , a novel OPRM1-mediated mechanism for L-asparaginase resistance in ALL , and identifies OPRM1 as a functional biomarker for defining high-risk subpopulations and for the detection of evolving resistant clones .

Example answer:
{"entities": [{"text": "OPRM1-mediated", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "ALL", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistent with this premise , patient leukemic cells with relatively high levels of OPRM1 are more sensitive to L-asparaginase treatment compared to OPRM1-depleted leukemic cells , further indicating that OPRM1 loss has a crucial role in L-asparaginase resistance in leukemic patients .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "L-asparaginase", "type": "ChemicalEntity"}, {"text": "OPRM1-depleted", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: We also found that OPRM1 is expressed in all leukemic cells tested .

Example answer:
{"entities": [{"text": "OPRM1", "type": "GeneOrGeneProduct"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This sole substitution was sufficient to confer constitutive activity to the receptor variant ( PrlR ( I146L ) ) , as assessed in three reconstituted cell models ( Ba/F3 , HEK293 and MCF-7 cells ) by Prl-independent ( i ) PrlR tyrosine phosphorylation , ( ii ) activation of signal transducer and activator of transcription 5 ( STAT5 ) signaling , ( iii ) transcriptional activity toward a Prl-responsive reporter gene , and ( iv ) cell proliferation and protection from cell death .

Example answer:
{"entities": [{"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "I146L", "type": "SequenceVariant"}, {"text": "Ba/F3", "type": "CellLine"}, {"text": "HEK293", "type": "CellLine"}, {"text": "MCF-7", "type": "CellLine"}, {"text": "Prl-independent", "type": "GeneOrGeneProduct"}, {"text": "signal transducer and activator of transcription 5", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "Prl-responsive", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In a prospective study involving 74 MFA patients and 170 control subjects , we identified four patients harboring a heterozygous single nucleotide polymorphism in exon 6 of the PrlR gene , encoding Ile ( 146 ) -- > Leu substitution in its extracellular domain .

Example answer:
{"entities": [{"text": "MFA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PrlR", "type": "GeneOrGeneProduct"}, {"text": "Ile ( 146 ) -- > Leu", "type": "SequenceVariant"}]}

Input:
Sentence: Underlining discrete roles of MOL1 and PXY , both LRR-RLKs are not able to replace each other when their expression domains are interchanged .

## Item biored:test:1023
Example input:
Sentence: Despite the absence of functional phosphatase and tensin homolog ( PTEN ) protein in Ishikawa cells , PKCalpha knockdown reduced Akt phosphorylation at serine 473 and concomitantly inhibited phosphorylation of the Akt target , glycogen synthase kinase-3beta ( GSK-3beta ) .

Example answer:
{"entities": [{"text": "phosphatase and tensin homolog", "type": "GeneOrGeneProduct"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "glycogen synthase kinase-3beta", "type": "GeneOrGeneProduct"}, {"text": "GSK-3beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Ishikawa cells depleted of PKCalpha protein grew slower , formed fewer colonies in anchorage-independent growth assays and exhibited impaired xenograft tumor formation in nude mice .

Example answer:
{"entities": [{"text": "Ishikawa", "type": "CellLine"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Aberrant caveolin-1-mediated Smad signaling and proliferation identified by analysis of adenine 474 deletion mutation ( c.474delA ) in patient fibroblasts : a new perspective on the mechanism of pulmonary hypertension .

Example answer:
{"entities": [{"text": "caveolin-1-mediated", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "adenine 474 deletion", "type": "SequenceVariant"}, {"text": "c.474delA", "type": "SequenceVariant"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pulmonary hypertension", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: Myotonic dystrophy protein kinase is involved in the modulation of the Ca2+ homeostasis in skeletal muscle cells .

Example answer:
{"entities": [{"text": "Myotonic dystrophy protein kinase", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The NRG-1 receptors erbB3 and erbB4 were present in MPNST invadopodia ( processes mediating invasion ) , partially colocalized with focal adhesion kinase and the laminin receptor beta ( 1 ) -integrin and coimmunoprecipitated with beta ( 1 ) -integrin .

Example answer:
{"entities": [{"text": "NRG-1", "type": "GeneOrGeneProduct"}, {"text": "erbB3", "type": "GeneOrGeneProduct"}, {"text": "erbB4", "type": "GeneOrGeneProduct"}, {"text": "MPNST", "type": "DiseaseOrPhenotypicFeature"}, {"text": "focal adhesion kinase", "type": "GeneOrGeneProduct"}, {"text": "laminin receptor", "type": "GeneOrGeneProduct"}, {"text": "beta ( 1 ) -integrin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The d-myo-inositol 1,4,5-trisphosphate ( IP ( 3 ) ) /Ca ( 2+ ) /protein kinase C ( PKC ) /mitogen-activated protein kinase pathway regulates cholangiocarcinoma growth .

Example answer:
{"entities": [{"text": "d-myo-inositol 1,4,5-trisphosphate", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "( 2+ )", "type": "ChemicalEntity"}, {"text": "kinase C", "type": "GeneOrGeneProduct"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "protein kinase", "type": "GeneOrGeneProduct"}, {"text": "cholangiocarcinoma", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Phosphatidylinositol 4-kinase IIb negatively regulates invadopodia formation and suppresses an invasive cellular phenotype .

## Item biored:test:964
Example input:
Sentence: Identification of a novel WFS1 mutation ( AFF344-345ins ) in Japanese patients with Wolfram syndrome .

Example answer:
{"entities": [{"text": "WFS1", "type": "GeneOrGeneProduct"}, {"text": "AFF344-345ins", "type": "SequenceVariant"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Wolfram syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The single base pair guanine insertion/deletion polymorphism ( 4G/5G ) within the promoter region of the PAI-1 gene influences PAI-1 synthesis and may modulate hepatic fibrogenesis .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "hepatic fibrogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: OBJECTIVES : To investigate the molecular basis of FDH in a 2-year-old Thai girl who presented at birth with depressed , pale linear scars on the trunk and limbs , sparse brittle hair , syndactyly of the right middle and ring fingers , dental caries and radiological features of osteopathia striata .

Example answer:
{"entities": [{"text": "FDH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "depressed", "type": "DiseaseOrPhenotypicFeature"}, {"text": "dental caries", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: The present study was performed to investigate the existence of an association between CFI genetic polymorphisms and Vogt-Koyanagi-Harada ( VKH ) syndrome .

## Item biored:test:973
Example input:
Sentence: The CFHR1 and CFHR3 deletion was not polymorphic in the Chinese population and was not associated with wet AMD or drusen .

Example answer:
{"entities": [{"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "drusen", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In both sets , no genotyped polymorphisms were significantly associated with RA susceptibility , but rs729302 was significantly associated .

Example answer:
{"entities": [{"text": "RA", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rs729302", "type": "SequenceVariant"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSION : Such a weak association and the lack of families with simple dominant Mendelian inheritance suggest that missense changes of uroplakin genes can not play a dominant role in causing VUR in humans , although they may be weak risk factors contributing to a complex polygenic disease .

Example answer:
{"entities": [{"text": "uroplakin", "type": "GeneOrGeneProduct"}, {"text": "VUR", "type": "DiseaseOrPhenotypicFeature"}, {"text": "humans", "type": "OrganismTaxon"}]}

Example input:
Sentence: We identified such a mechanism as the origin of the mild to asymptomatic phenotype observed in cystic fibrosis patients homozygous for the E831X mutation ( 2623G > T ) in the CFTR gene .

Example answer:
{"entities": [{"text": "cystic fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "E831X", "type": "SequenceVariant"}, {"text": "2623G > T", "type": "SequenceVariant"}, {"text": "CFTR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Of them , two patients carrying E359K mutation were from two generations in one family with ventricular septal defect ( VSD ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "E359K", "type": "SequenceVariant"}, {"text": "ventricular septal defect", "type": "DiseaseOrPhenotypicFeature"}, {"text": "VSD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: RESULTS : Four SNPs , including rs3753394 ( P = 0.0276 ) , rs800292 ( P = 0.0266 ) , rs1061170 ( P = 0.00514 ) , and rs1329428 ( P = 0.0089 ) , in CFH showed a significant association with wet AMD in the cohort of this study .

Example answer:
{"entities": [{"text": "rs3753394", "type": "SequenceVariant"}, {"text": "rs800292", "type": "SequenceVariant"}, {"text": "rs1061170", "type": "SequenceVariant"}, {"text": "rs1329428", "type": "SequenceVariant"}, {"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PURPOSE : The aim of the study was to evaluate the renin-angiotensin system and serotonin transporter gene polymorphisms in relation to hemodynamic parameters and heart rate variability during a head-up tilt test ( HUT ) in patients with vasovagal syncope .

Example answer:
{"entities": [{"text": "renin-angiotensin", "type": "GeneOrGeneProduct"}, {"text": "serotonin transporter", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "vasovagal syncope", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: This study showed that CFH was more likely to be AMD susceptibility gene at Chr.1q31 based on the finding that the CFHR1 and CFHR3 deletion was not polymorphic in the cohort of this study , and none of the SNPs that were significantly associated with AMD in a white population in C2 , CFB , and C3 genes showed a significant association with AMD .

Example answer:
{"entities": [{"text": "CFH", "type": "GeneOrGeneProduct"}, {"text": "AMD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "CFHR1", "type": "GeneOrGeneProduct"}, {"text": "CFHR3", "type": "GeneOrGeneProduct"}, {"text": "C2", "type": "GeneOrGeneProduct"}, {"text": "CFB", "type": "GeneOrGeneProduct"}, {"text": "C3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Nevertheless , no significant association with patients with VKH syndrome in steroid-sensitive statuses was detected for CFI-rs7356506 polymorphisms .

## Item biored:test:1043
Example input:
Sentence: The p53 mutation spectrum , presenting a high level of CC to TT mutations , shows that the UV component of sunlight is the major risk factor and modulated DNA repair by immunosuppressive drug treatment may be significant in the skin carcinogenesis of RTRs .

Example answer:
{"entities": [{"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "CC to TT", "type": "SequenceVariant"}, {"text": "skin carcinogenesis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: We have analyzed skin lesions from RTRs with aggressive tumors for p53 gene modifications , the presence of Human Papillomas Virus ( HPV ) DNA in relation to the p53 codon 72 genotype and polymorphisms of the XPD repair gene .

Example answer:
{"entities": [{"text": "skin lesions", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "p53", "type": "GeneOrGeneProduct"}, {"text": "Human Papillomas Virus", "type": "OrganismTaxon"}, {"text": "HPV", "type": "OrganismTaxon"}, {"text": "XPD", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: TS genotyping methods were polymerase chain reaction ( PCR ) for VNTR and PCR , followed by restriction length fragment polymorphism ( PCR-RFLP ) for SNP and ins/del 6 bp .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "ins/del 6 bp", "type": "SequenceVariant"}]}

Example input:
Sentence: Serum samples were PCR amplified with HBV reverse transcriptase ( RT ) primers , followed by direct sequencing across the tyrosine-methionine-aspartate-aspartate ( YMDD ) motif of the major catalytic region in the C domain of the HBV RT enzyme .

Example answer:
{"entities": [{"text": "HBV", "type": "OrganismTaxon"}]}

Example input:
Sentence: DNA from peripheral nuclear blood cells was genotyped for 5-HTTLPR using standard polymerase chain reaction methods.A significant group effect was observed only on memory function tasks ( p = 0.04 ) but not on reaction times ( p = 0.61 ) or attention/executive functioning ( p = 0.59 ) .

Example answer:
{"entities": [{"text": "5-HTTLPR", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Expression analysis on a cDNA panel from 17 different normal tissues by reverse transcription-PCR ( RT-PCR ) revealed tissue restricted mRNA expression of 2 of the 27 unknown antigens .

Example answer:
{"entities": []}

Example input:
Sentence: RT-PCR analysis of the c.610-2A > G transition demonstrated that the change altered splicing , leading to the production of two distinct aberrantly spliced forms , viz .

Example answer:
{"entities": [{"text": "c.610-2A > G", "type": "SequenceVariant"}]}

Example input:
Sentence: RT-PCR analysis , performed on a patient homozygous for the intronic deletion ( c.609+28_610-16del ) , failed to detect any GNPTG RNA transcripts .

Example answer:
{"entities": [{"text": "patient", "type": "OrganismTaxon"}, {"text": "c.609+28_610-16del", "type": "SequenceVariant"}, {"text": "GNPTG", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Polymerase chain reaction ( PCR ) showed EGFR amplification in 25 of 77 ( 32 % ) cases and p16 homozygous deletion in 32 of 77 ( 42 % ) cases .

Example answer:
{"entities": [{"text": "EGFR", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RT-PCR identified a novel alternatively spliced ( AS ) transcript that was expressed at the protein level in COS-7 transfectants .

Example answer:
{"entities": [{"text": "COS-7", "type": "CellLine"}]}

Input:
Sentence: Some of these findings were validated by RT-PCR .

## Item biored:test:985
Example input:
Sentence: Sag inactivation by genetic deletion remarkably suppresses cell proliferation by inducing senescence , which is associated with accumulation of p16 , but not p53 .

Example answer:
{"entities": [{"text": "Sag", "type": "GeneOrGeneProduct"}, {"text": "p16", "type": "GeneOrGeneProduct"}, {"text": "p53", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Growth arrest and DNA-damage-inducible 45 alpha ( GADD45A ) is induced by genotoxic stress in HSCs .

Example answer:
{"entities": [{"text": "Growth arrest and DNA-damage-inducible 45 alpha", "type": "GeneOrGeneProduct"}, {"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: GADD45A-expressing HSCs failed to long-term reconstitute the blood of recipients by inducing multilineage differentiation in vivo .

Example answer:
{"entities": [{"text": "GADD45A-expressing", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In contrast to other cellular systems , GADD45A expression did not cause a cell cycle arrest or an alteration in the decision between cell survival and apoptosis in HSCs .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Further study revealed that the effect of Sal on renal interstitial fibrosis is associated with the lower expression of TLR4 , p-IkappaBalpha , p-NF-kappaB and mitogen-activated protein kinases ( MAPK ) , both in vivo and in vitro .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "renal interstitial fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TLR4", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinases", "type": "GeneOrGeneProduct"}, {"text": "MAPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Thus , CAA directly reacts with cellular protein and non-protein thiols , mediating its toxicity on hRPTEC .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "thiols", "type": "ChemicalEntity"}, {"text": "toxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hRPTEC", "type": "CellLine"}]}

Example input:
Sentence: Acidification , which slowed the reaction of CAA with thiol donors , could also attenuate effects of CAA on necrosis markers , thiol depletion and cysteine protease inhibition in living cells .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "thiol", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cysteine protease", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: These data indicate that genotoxic stress-induced GADD45A expression in HSCs prevents their fatal transformation by directing them into differentiation and thereby clearing them from the system .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , Sal administration significantly suppresses epithelial-mesenchymal transition ( EMT ) , as evidenced by a decreased expression of alpha-SMA , vimentin , TGF-beta1 , snail , slug , and a largely restored expression of E-cadherin .

Example answer:
{"entities": [{"text": "Sal", "type": "ChemicalEntity"}, {"text": "alpha-SMA", "type": "GeneOrGeneProduct"}, {"text": "vimentin", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta1", "type": "GeneOrGeneProduct"}, {"text": "snail", "type": "GeneOrGeneProduct"}, {"text": "slug", "type": "GeneOrGeneProduct"}, {"text": "E-cadherin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CAA reduced hRPTEC cell number and protein , induced a loss in free intracellular thiols and an increase in necrosis markers .

Example answer:
{"entities": [{"text": "CAA", "type": "ChemicalEntity"}, {"text": "hRPTEC", "type": "CellLine"}, {"text": "thiols", "type": "ChemicalEntity"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: In conclusion , SAA may modulate fibrogenic responses in the liver in a positive and negative fashion by inducing inflammation , proliferation and cell death in HSCs .

## Item biored:test:999
Example input:
Sentence: Although treatment with the pancreatic b-cell toxin streptozotocin induced hyperglycemia and raised plasma ghrelin levels in wild-type mice , hyperglycemia was averted in similarly treated Gcgr ( -/- ) mice and the plasma ghrelin level was further increased .

Example answer:
{"entities": [{"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "hyperglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In conclusion , administration of isoproterenol to rats results in primary loss of dystrophin , the most sensitive among the structural proteins that form the DGC that connects the extracellular matrix and the cytoskeleton in cardiomyocyte .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "ChemicalEntity"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "dystrophin", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: CONCLUSIONS : Dexamethasone treatment is effective in controlling the premature pubarche , hypoglycemia , hypertension , and hypokalemia in this child case , wherein arginine 714 plays a key role in the proper formation of the ligand-binding pocket and the AF-2 surface of the GR alpha LBD .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "premature pubarche", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypertension", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypokalemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "arginine 714", "type": "SequenceVariant"}, {"text": "GR alpha", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aldosterone-sensitive serum- and glucocorticoid-inducible kinase SGK1 has been shown to participate in the stimulation of ENaC and to mediate renal fibrosis following mineralocorticoid and salt excess .

Example answer:
{"entities": [{"text": "aldosterone-sensitive", "type": "ChemicalEntity"}, {"text": "serum- and glucocorticoid-inducible kinase", "type": "GeneOrGeneProduct"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mineralocorticoid", "type": "ChemicalEntity"}, {"text": "salt", "type": "ChemicalEntity"}]}

Example input:
Sentence: In conclusion , HFD-induced obese rats are highly sensitized to doxorubicin-induced cardiotoxicity by substantially downregulating cardiac mitochondrial ATP generation , increasing oxidative stress and downregulating the JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Dexamethasone significantly increased SBP and plasma H2O2 level and decreased thymus and body weights .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "ChemicalEntity"}, {"text": "H2O2", "type": "ChemicalEntity"}]}

Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Male Wistar rats were challenged intragastrically once daily for 9 days with 1.0 ml/kg of corn oil containing vitamin D2 and cholesterol to induce atherosclerosis .

Example answer:
{"entities": [{"text": "rats", "type": "OrganismTaxon"}, {"text": "corn oil", "type": "ChemicalEntity"}, {"text": "vitamin D2", "type": "ChemicalEntity"}, {"text": "cholesterol", "type": "ChemicalEntity"}, {"text": "atherosclerosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the current study , we investigated whether a physiological intervention by feeding 40 % high fat diet ( HFD ) , which induces obesity in male Sprague-Dawley rats ( 250-275 g ) , sensitizes to doxorubicin-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "fat", "type": "ChemicalEntity"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Crocin improves lipid dysregulation in subacute diazinon exposure through ERK1/2 pathway in rat liver .

Example answer:
{"entities": [{"text": "Crocin", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "diazinon", "type": "ChemicalEntity"}, {"text": "ERK1/2", "type": "GeneOrGeneProduct"}, {"text": "rat", "type": "OrganismTaxon"}]}

Input:
Sentence: Glucocorticoids can promote steatosis by stimulating lipolysis within adipose tissue , free fatty acid delivery to liver and hepatic de novo lipogenesis .

## Item biored:test:1001
Example input:
Sentence: OBJECTIVE : This study determined the antihyperalgesic effect of CNSB002 , a sodium channel blocker with antioxidant properties given alone and in combinations with morphine in rat models of inflammatory and neuropathic pain .

Example answer:
{"entities": [{"text": "CNSB002", "type": "ChemicalEntity"}, {"text": "sodium channel blocker", "type": "ChemicalEntity"}, {"text": "morphine", "type": "ChemicalEntity"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "neuropathic pain", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Meanwhile , Co-IP results demonstrated that Hsp90beta could interact with and stabilize TAK1 , AMPKalpha , IKKalpha/beta , HIF-1alpha and Raptor , whereas Hsp90beta inhibition disrupted this process .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "TAK1", "type": "GeneOrGeneProduct"}, {"text": "AMPKalpha", "type": "GeneOrGeneProduct"}, {"text": "IKKalpha/beta", "type": "GeneOrGeneProduct"}, {"text": "HIF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "Raptor", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In vitro , the HK2 cells were treated with iopamidol in the presence or absence of atorvastatin , heat shock protein ( Hsp ) 27 small interfering ( si ) RNA or pcDNA3.1-Hsp27 .

Example answer:
{"entities": [{"text": "HK2", "type": "CellLine"}, {"text": "iopamidol", "type": "ChemicalEntity"}, {"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "heat shock protein ( Hsp ) 27", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Instead , oral administration of S-1 ( a derivative of 5-FU ) , at 200 mg/day twice a week , was instituted , because S-1 has a strong inhibitory effect on dihydropyrimidine dehydrogenase , which catalyzes the degradative of 5-FU into FBAL .

Example answer:
{"entities": [{"text": "S-1", "type": "ChemicalEntity"}, {"text": "5-FU", "type": "ChemicalEntity"}, {"text": "dihydropyrimidine", "type": "ChemicalEntity"}, {"text": "FBAL", "type": "ChemicalEntity"}]}

Example input:
Sentence: OBJECTIVES : SLCO1B1 * 5 and SLCO1B1 * 15 have been reported to reduce the clearance of pravastatin in healthy volunteers .

Example answer:
{"entities": [{"text": "SLCO1B1", "type": "GeneOrGeneProduct"}, {"text": "pravastatin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Emodin markedly inhibited the proliferation of HCT116 cells and a higher protein level of FASN was expressed , compared with that in SW480 , SNU-C2A or SNU-C5 cells .

Example answer:
{"entities": [{"text": "Emodin", "type": "ChemicalEntity"}, {"text": "HCT116", "type": "CellLine"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "SW480", "type": "CellLine"}, {"text": "SNU-C2A", "type": "CellLine"}, {"text": "SNU-C5", "type": "CellLine"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: RAD001 , an oral inhibitor of the mammalian target of rapamycin ( mTOR ) , has shown phase I efficacy in NSCLC .

Example answer:
{"entities": [{"text": "RAD001", "type": "ChemicalEntity"}, {"text": "mammalian target of rapamycin", "type": "GeneOrGeneProduct"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "NSCLC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Inhibition of type I TGFb receptors ALK1/2/3/6 responsible for phosphorylation of Smad1/5/8 reduced the hyperproliferation seen in c.474delA fibroblasts .

Example answer:
{"entities": [{"text": "type I TGFb receptors", "type": "GeneOrGeneProduct"}, {"text": "ALK1/2/3/6", "type": "GeneOrGeneProduct"}, {"text": "Smad1/5/8", "type": "GeneOrGeneProduct"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Input:
Sentence: Inhibition of 11b-HSD1 has been suggested as a potential treatment for NAFLD .

## Item biored:test:1002
Example input:
Sentence: RESULTS : HAT adipose tissue demonstrated increased lipid related genes for storage ( CD36 , DGAT1 , DGAT2 , SCD1 , FASN , and LPL ) , lipolysis ( HSL , CES1 , perilipin ) , fatty acid binding proteins ( FABP1 , FABP3 ) and adipocyte differentiation markers ( CEBPalpha , CEBPbeta , PPARgamma ) .

Example answer:
{"entities": [{"text": "lipid", "type": "ChemicalEntity"}, {"text": "CD36", "type": "GeneOrGeneProduct"}, {"text": "DGAT1", "type": "GeneOrGeneProduct"}, {"text": "DGAT2", "type": "GeneOrGeneProduct"}, {"text": "SCD1", "type": "GeneOrGeneProduct"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "LPL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CES1", "type": "GeneOrGeneProduct"}, {"text": "perilipin", "type": "GeneOrGeneProduct"}, {"text": "fatty acid binding proteins", "type": "GeneOrGeneProduct"}, {"text": "FABP1", "type": "GeneOrGeneProduct"}, {"text": "FABP3", "type": "GeneOrGeneProduct"}, {"text": "CEBPalpha", "type": "GeneOrGeneProduct"}, {"text": "CEBPbeta", "type": "GeneOrGeneProduct"}, {"text": "PPARgamma", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Resequencing of IRS2 reveals rare variants for obesity but not fasting glucose homeostasis in Hispanic children .

Example answer:
{"entities": [{"text": "IRS2", "type": "GeneOrGeneProduct"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "glucose", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: ADAM12 knockdown also diminished ALDEFLUOR ( + ) and CD44 ( hi ) /CD24 ( -/lo ) CSC-enriched populations in vitro and reduced tumorigenesis in mice in vivo .

Example answer:
{"entities": [{"text": "ADAM12", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "tumorigenesis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Object of the present study was to study the influence of SLCO1B1 * 5 , * 15 and * 15+C1007G , a novel haplotype found in a patient with pravastatin-induced myopathy , on the functional properties of OATP1B1 by transient expression systems of HEK293 and HeLa cells using endogenous conjugates and statins as substrates .

Example answer:
{"entities": [{"text": "SLCO1B1", "type": "GeneOrGeneProduct"}, {"text": "patient", "type": "OrganismTaxon"}, {"text": "pravastatin-induced", "type": "ChemicalEntity"}, {"text": "myopathy", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OATP1B1", "type": "GeneOrGeneProduct"}, {"text": "HEK293", "type": "CellLine"}, {"text": "HeLa", "type": "CellLine"}]}

Example input:
Sentence: Tak1 ( col2 ) mice displayed severe chondrodysplasia with runting , impaired formation of secondary centres of ossification , and joint abnormalities including elbow dislocation and tarsal fusion .

Example answer:
{"entities": [{"text": "Tak1", "type": "GeneOrGeneProduct"}, {"text": "col2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "chondrodysplasia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "joint abnormalities", "type": "DiseaseOrPhenotypicFeature"}, {"text": "elbow dislocation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tarsal fusion", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In conclusion , HFD-induced obese rats are highly sensitized to doxorubicin-induced cardiotoxicity by substantially downregulating cardiac mitochondrial ATP generation , increasing oxidative stress and downregulating the JAK/STAT3 pathway .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ATP", "type": "ChemicalEntity"}, {"text": "JAK/STAT3", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: A LD ( 10 ) dose ( 8 mg doxorubicin/kg , ip ) administered on day 43 of the HFD feeding regimen led to higher cardiotoxicity , cardiac dysfunction , lipid peroxidation , and 80 % mortality in the obese ( OB ) rats in the absence of any significant renal or hepatic toxicity .

Example answer:
{"entities": [{"text": "doxorubicin/kg", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cardiac dysfunction", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "OB", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "renal or hepatic toxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In the current study , we investigated whether a physiological intervention by feeding 40 % high fat diet ( HFD ) , which induces obesity in male Sprague-Dawley rats ( 250-275 g ) , sensitizes to doxorubicin-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "fat", "type": "ChemicalEntity"}, {"text": "obesity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "doxorubicin-induced", "type": "ChemicalEntity"}, {"text": "cardiotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: AIM : To evaluate the influence of PAI-1 serum levels and 4G/5G polymorphism on the risk of liver fibrosis associated to non-alcoholic fatty liver disease ( NAFLD ) in morbidly obese patients .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "non-alcoholic fatty liver disease", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NAFLD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: To test this , male mice with global ( 11b-HSD1 knockout [ KO ] ) and liver-specific ( LKO ) 11b-HSD1 loss of function were fed the American Lifestyle Induced Obesity Syndrome ( ALIOS ) diet , known to recapitulate the spectrum of NAFLD , and metabolic and liver phenotypes assessed .

## Item biored:test:1049
Example input:
Sentence: Upon division , Dpp signaling is extinguished , and Nos is downregulated in one daughter cell , causing it to switch to a differentiating cystoblast ( CB ) .

Example answer:
{"entities": [{"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mathematical modeling elucidates bistability of cell fate in the Brat-mediated system , revealing how autoregulation of GSC number can arise from Brat coupling extracellular Dpp regulation to intracellular interpretation .

Example answer:
{"entities": [{"text": "Brat-mediated", "type": "GeneOrGeneProduct"}, {"text": "Brat", "type": "GeneOrGeneProduct"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The cytokine leukemia inhibitory factor ( LIF ) is essential for rendering the uterus receptive for blastocyst implantation .

Example answer:
{"entities": [{"text": "leukemia inhibitory factor", "type": "GeneOrGeneProduct"}, {"text": "LIF", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mouse embryonic fibroblasts exhibiting disruption or overexpression of IGF-1R ( R- cells and R+ cells ) were used to examine the level of apoptosis , autophagy , and production of reactive oxygen species ( ROS ) .

Example answer:
{"entities": [{"text": "Mouse", "type": "OrganismTaxon"}, {"text": "IGF-1R", "type": "GeneOrGeneProduct"}, {"text": "reactive oxygen species", "type": "ChemicalEntity"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Genetic investigation of four meiotic genes in women with premature ovarian failure .

Example answer:
{"entities": [{"text": "women", "type": "OrganismTaxon"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Drosophila ovarian germline stem cells ( GSCs ) are maintained by Dpp signaling and the Pumilio ( Pum ) and Nanos ( Nos ) translational repressors .

Example answer:
{"entities": [{"text": "Drosophila", "type": "OrganismTaxon"}, {"text": "Dpp", "type": "GeneOrGeneProduct"}, {"text": "Pumilio", "type": "GeneOrGeneProduct"}, {"text": "Pum", "type": "GeneOrGeneProduct"}, {"text": "Nanos", "type": "GeneOrGeneProduct"}, {"text": "Nos", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: BACKGROUND : Folate is critical for cell division , a major feature of in utero development .

Example answer:
{"entities": [{"text": "Folate", "type": "ChemicalEntity"}]}

Example input:
Sentence: Here , we show that simultaneous overexpression of the mitotic checkpoint protein Mad2 with Kras ( G12D ) or Her2 in mammary glands of adult mice results in mitotic checkpoint overactivation and a delay in tumor onset .

Example answer:
{"entities": [{"text": "Mad2", "type": "GeneOrGeneProduct"}, {"text": "Kras", "type": "GeneOrGeneProduct"}, {"text": "G12D", "type": "GeneOrGeneProduct"}, {"text": "Her2", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: OBJECTIVE : The goal of this study was to determine whether mutations of meiotic genes , such as disrupted meiotic cDNA ( DMC1 ) , MutS homolog ( MSH4 ) , MSH5 , and S. cerevisiae homolog ( SPO11 ) , were associated with premature ovarian failure ( POF ) .

Example answer:
{"entities": [{"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "MutS", "type": "GeneOrGeneProduct"}, {"text": "MSH4", "type": "GeneOrGeneProduct"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}, {"text": "S. cerevisiae", "type": "OrganismTaxon"}, {"text": "SPO11", "type": "GeneOrGeneProduct"}, {"text": "premature ovarian failure", "type": "DiseaseOrPhenotypicFeature"}, {"text": "POF", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : The symptoms of infertility observed in the DMC1 homozygote mutation carrier and in both patients with a heterozygous substitution in exon 2 of the MSH5 gene provide indirect evidence of the role of genes involved in meiotic recombination in the regulation of ovarian function .

Example answer:
{"entities": [{"text": "infertility", "type": "DiseaseOrPhenotypicFeature"}, {"text": "DMC1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "MSH5", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Meiotic resumption ( G2/M transition ) and progression through meiosis I ( MI ) are two key stages for producing fertilization-competent eggs .

## Item biored:test:982
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Although treatment with the pancreatic b-cell toxin streptozotocin induced hyperglycemia and raised plasma ghrelin levels in wild-type mice , hyperglycemia was averted in similarly treated Gcgr ( -/- ) mice and the plasma ghrelin level was further increased .

Example answer:
{"entities": [{"text": "streptozotocin", "type": "ChemicalEntity"}, {"text": "hyperglycemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ghrelin", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "Gcgr", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: While NRG-1 beta potently and persistently activated Erk 1/2 , SAPK/JNK , Akt and Src family kinases , NRG-1 alpha did not activate Akt and activated these other kinases with kinetics distinct from those evident in NRG-1 beta-stimulated cells .

Example answer:
{"entities": [{"text": "NRG-1 beta", "type": "GeneOrGeneProduct"}, {"text": "Erk 1/2", "type": "GeneOrGeneProduct"}, {"text": "SAPK/JNK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "Src family kinases", "type": "GeneOrGeneProduct"}, {"text": "NRG-1 alpha", "type": "GeneOrGeneProduct"}, {"text": "NRG-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Gene deletion or pharmacological blockade of KCa3.1 protected against SOCE-induced Ca2+ overload and ER stress via the protein kinase B ( AKT ) signaling pathway in astrocytes .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Ca2+", "type": "ChemicalEntity"}, {"text": "protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "AKT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The aldosterone-sensitive serum- and glucocorticoid-inducible kinase SGK1 has been shown to participate in the stimulation of ENaC and to mediate renal fibrosis following mineralocorticoid and salt excess .

Example answer:
{"entities": [{"text": "aldosterone-sensitive", "type": "ChemicalEntity"}, {"text": "serum- and glucocorticoid-inducible kinase", "type": "GeneOrGeneProduct"}, {"text": "SGK1", "type": "GeneOrGeneProduct"}, {"text": "renal fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "mineralocorticoid", "type": "ChemicalEntity"}, {"text": "salt", "type": "ChemicalEntity"}]}

Example input:
Sentence: A new and highly specific antibody ( A82 , Amgen ) was used to evaluate the presence of Epo-R by western blot analysis in addition to Epo-R signaling proteins ( Akt , STAT5 , p70s6k , LYN , and p38MAPK ) , activation of lipolytic pathways ( ATGL , HSL , CGI-58 , G0S2 , Perilipin , Cidea , Cidec , AMPK , and ACC ) , and mitochondrial biogenesis ( VDAC , HSP90 , PDH , and SDHA ) .

Example answer:
{"entities": [{"text": "Epo-R", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "STAT5", "type": "GeneOrGeneProduct"}, {"text": "p70s6k", "type": "GeneOrGeneProduct"}, {"text": "LYN", "type": "GeneOrGeneProduct"}, {"text": "p38MAPK", "type": "GeneOrGeneProduct"}, {"text": "ATGL", "type": "GeneOrGeneProduct"}, {"text": "HSL", "type": "GeneOrGeneProduct"}, {"text": "CGI-58", "type": "GeneOrGeneProduct"}, {"text": "G0S2", "type": "GeneOrGeneProduct"}, {"text": "Perilipin", "type": "GeneOrGeneProduct"}, {"text": "Cidea", "type": "GeneOrGeneProduct"}, {"text": "Cidec", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}, {"text": "ACC", "type": "GeneOrGeneProduct"}, {"text": "VDAC", "type": "GeneOrGeneProduct"}, {"text": "HSP90", "type": "GeneOrGeneProduct"}, {"text": "PDH", "type": "GeneOrGeneProduct"}, {"text": "SDHA", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Growth arrest and DNA-damage-inducible 45 alpha ( GADD45A ) is induced by genotoxic stress in HSCs .

Example answer:
{"entities": [{"text": "Growth arrest and DNA-damage-inducible 45 alpha", "type": "GeneOrGeneProduct"}, {"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In Mz-ChA-1 cells stimulated with ( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide ( RAMH ) , we measured ( a ) cell growth , ( b ) IP ( 3 ) and cyclic AMP levels , and ( c ) phosphorylation of PKC and mitogen-activated protein kinase isoforms .

Example answer:
{"entities": [{"text": "Mz-ChA-1", "type": "CellLine"}, {"text": "( R ) - ( alpha ) - ( - ) -methylhistamine dihydrobromide", "type": "ChemicalEntity"}, {"text": "RAMH", "type": "ChemicalEntity"}, {"text": "IP ( 3 )", "type": "ChemicalEntity"}, {"text": "cyclic AMP", "type": "ChemicalEntity"}, {"text": "PKC", "type": "GeneOrGeneProduct"}, {"text": "mitogen-activated protein kinase", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: Serum amyloid A induced HSC proliferation , which depended on JNK , Erk and Akt activity .

## Item biored:test:1032
Example input:
Sentence: Based on recent papers describing the prognostic roles of the polymorphisms and the NFkappaB functions on cancer development , we sought to determine if Japanese gastric cancer patients were affected by the IL1B -31/-511 and FAS-670 polymorphisms .

Example answer:
{"entities": [{"text": "NFkappaB", "type": "GeneOrGeneProduct"}, {"text": "cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gastric cancer", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "IL1B", "type": "GeneOrGeneProduct"}, {"text": "FAS-670", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: MCF7/AdrR cells expressing the exogenous Rab6c exhibited less resistance to several anti-cancer drugs , such as doxorubicin ( DOX ) , taxol , vinblastine , and vincristine , than the control cells containing the empty vector .

Example answer:
{"entities": [{"text": "MCF7/AdrR", "type": "CellLine"}, {"text": "Rab6c", "type": "GeneOrGeneProduct"}, {"text": "doxorubicin", "type": "ChemicalEntity"}, {"text": "DOX", "type": "ChemicalEntity"}, {"text": "taxol", "type": "ChemicalEntity"}, {"text": "vinblastine", "type": "ChemicalEntity"}, {"text": "vincristine", "type": "ChemicalEntity"}]}

Example input:
Sentence: We recently reported that phosphoinositide 3-kinase ( PI3K ) /protein kinase B ( Akt ) mediates transcriptional regulation and activation of bone morphogenetic protein ( BMP ) -2 signaling by nuclear factor ( NF ) -kappaB in bone metastatic prostate cancer cells .

Example answer:
{"entities": [{"text": "phosphoinositide 3-kinase ( PI3K ) /protein kinase B", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "bone morphogenetic protein ( BMP ) -2", "type": "GeneOrGeneProduct"}, {"text": "nuclear factor ( NF ) -kappaB", "type": "GeneOrGeneProduct"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In addition , BMP-2 mediates TNF-alpha-induced invasion of C4-2B cells in a NF-kappaB-dependent fashion .

Example answer:
{"entities": [{"text": "BMP-2", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha-induced", "type": "GeneOrGeneProduct"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "NF-kappaB-dependent", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: It was partially reduced by PKC- or Src-inhibition , but not with PI3K-inhibitors ( wortmannin , LY294002 ) or thapsigargin .

Example answer:
{"entities": [{"text": "PKC-", "type": "GeneOrGeneProduct"}, {"text": "Src-inhibition", "type": "GeneOrGeneProduct"}, {"text": "PI3K-inhibitors", "type": "GeneOrGeneProduct"}, {"text": "wortmannin", "type": "ChemicalEntity"}, {"text": "LY294002", "type": "ChemicalEntity"}, {"text": "thapsigargin", "type": "ChemicalEntity"}]}

Example input:
Sentence: Consistent with impaired growth , PKCalpha knockdown increased levels of the cyclin-dependent kinase ( CDK ) inhibitors p21 ( Cip1/WAF1 ) ( p21 ) and p27 ( Kip1 ) ( p27 ) .

Example answer:
{"entities": [{"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "cyclin-dependent kinase", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}, {"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "Cip1/WAF1", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Kip1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: p21 and p27 expression was not increased by treatment of Ishikawa cells with ERK and Akt inhibitors , suggesting that PKCalpha regulates CDK expression independently of Akt and ERK .

Example answer:
{"entities": [{"text": "p21", "type": "GeneOrGeneProduct"}, {"text": "p27", "type": "GeneOrGeneProduct"}, {"text": "Ishikawa", "type": "CellLine"}, {"text": "ERK", "type": "GeneOrGeneProduct"}, {"text": "Akt", "type": "GeneOrGeneProduct"}, {"text": "PKCalpha", "type": "GeneOrGeneProduct"}, {"text": "CDK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Furthermore , incubation of cells with exogenously added EGF prevented the downregulation of CD44 ( hi ) /CD24 ( -/lo ) cell population by ADAM12 knockdown .

Example answer:
{"entities": [{"text": "EGF", "type": "GeneOrGeneProduct"}, {"text": "CD44", "type": "GeneOrGeneProduct"}, {"text": "ADAM12", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In the present study , we demonstrate that NF-kappaB , whether activated by recombinant human tumor necrosis factor ( TNF ) -alpha or by ectopic expression of the p65 subunit , is involved in extracellular matrix adhesion and invasion of osteotropic PC-3 and C4-2B , but not LNCaP , cells .

Example answer:
{"entities": [{"text": "NF-kappaB", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "tumor necrosis factor ( TNF ) -alpha", "type": "GeneOrGeneProduct"}, {"text": "p65", "type": "GeneOrGeneProduct"}, {"text": "PC-3", "type": "CellLine"}, {"text": "C4-2B", "type": "CellLine"}, {"text": "LNCaP", "type": "CellLine"}]}

Example input:
Sentence: Furthermore , PI3K/Akt pathway signaling was also increased in Eu-myc B cells , and this increase was partially suppressed with ibrutinib .

Example answer:
{"entities": [{"text": "PI3K/Akt", "type": "GeneOrGeneProduct"}, {"text": "ibrutinib", "type": "ChemicalEntity"}]}

Input:
Sentence: This finding supports the cell data and suggests that PI4KIIb may be a clinically significant suppressor of invasion .

## Item biored:test:943
Example input:
Sentence: Both minor alleles , adjusted for sex , age , BMI and insulin sensitivity were associated with elevated AUCproinsulin and AUCproinsulin/AUCinsulin ( rs6235 : p ( additive ) model < or= 0.009 , effect sizes 8/8 % , rs6232 : pdominant model < or= 0.01 , effect sizes 10/21 % ) .

Example answer:
{"entities": [{"text": "insulin", "type": "GeneOrGeneProduct"}, {"text": "rs6235", "type": "SequenceVariant"}, {"text": "rs6232", "type": "SequenceVariant"}]}

Example input:
Sentence: In Canadian patients , Cys 23 Ser was associated with minimum lifetime BMI ( p=0.046 ) , with lowest values in Ser/Ser carriers .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: ( CCTTT ) 14 , which has been reported to have a higher activity in a reporter-construct , was significantly more abundant in POAG patients , while ( CCTTT ) 10 and ( CCTTT ) 13 were less common .

Example answer:
{"entities": [{"text": "( CCTTT ) 14", "type": "SequenceVariant"}, {"text": "POAG", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "( CCTTT ) 10", "type": "SequenceVariant"}, {"text": "( CCTTT ) 13", "type": "SequenceVariant"}]}

Example input:
Sentence: CONCLUSIONS : High serum levels of inflammatory chemokines such as CCL4 and CCL5 in the serum of cirrhotic patients indicate the presence of HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: CONCLUSIONS : Morbidly obese patients had significantly lower PAI-1 serum levels with similar PAI-1 4G/5G genotypes frequencies compared to non-obese subjects .

Example answer:
{"entities": [{"text": "obese", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "PAI-1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum concentrations of CRP , neopterin and IL-6 as markers of inflammation and thrombopoietin ( TPO ) , GCSF , FGF basic and VEGF , HMGB1 , CK-18 ( M65 ) and CK18 fragment ( M30 ) and a panel of proinflammatory chemokines ( CCL2 , CCL3 , CCL4 , CCL5 , CXCL5 and IL-8 ) were measured .

Example answer:
{"entities": [{"text": "CRP", "type": "GeneOrGeneProduct"}, {"text": "neopterin", "type": "ChemicalEntity"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "thrombopoietin", "type": "GeneOrGeneProduct"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "GCSF", "type": "GeneOrGeneProduct"}, {"text": "FGF basic", "type": "GeneOrGeneProduct"}, {"text": "VEGF", "type": "GeneOrGeneProduct"}, {"text": "HMGB1", "type": "GeneOrGeneProduct"}, {"text": "CK-18", "type": "GeneOrGeneProduct"}, {"text": "CK18", "type": "GeneOrGeneProduct"}, {"text": "proinflammatory chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "CCL3", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "IL-8", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : Patients with HCC had higher serum TPO and chemokines ( P < 0.001 for TPO , CCL4 , CCL5 and CXCL5 ) and lower CCL2 ( P=0.008 ) levels than cirrhotic patients without HCC .

Example answer:
{"entities": [{"text": "Patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "CCL4", "type": "GeneOrGeneProduct"}, {"text": "CCL5", "type": "GeneOrGeneProduct"}, {"text": "CXCL5", "type": "GeneOrGeneProduct"}, {"text": "CCL2", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Example input:
Sentence: Serum levels of TPO and chemokines were lower , whereas M30 was significantly higher in cirrhotic patients than in HCs .

Example answer:
{"entities": [{"text": "TPO", "type": "GeneOrGeneProduct"}, {"text": "chemokines", "type": "GeneOrGeneProduct"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}]}

Input:
Sentence: By contrast , no significant correlation was detected between the protein levels and patient age , histological type , or serum CA125 , CA199 , CA724 , NSE , CEA , and b-HCG levels .

## Item biored:test:1022
Example input:
Sentence: Emodin significantly downregulated the protein expression of FASN in HCT116 cells , which was caused by protein degradation due to elevated protein ubiquitination .

Example answer:
{"entities": [{"text": "Emodin", "type": "ChemicalEntity"}, {"text": "FASN", "type": "GeneOrGeneProduct"}, {"text": "HCT116", "type": "CellLine"}]}

Example input:
Sentence: p16ink4a , the inducer of terminal senescence , underwent autophagic sequestration in the cytoplasm of ETO-treated cells , allowing alternative cell fates .

Example answer:
{"entities": [{"text": "p16ink4a", "type": "GeneOrGeneProduct"}, {"text": "ETO-treated", "type": "ChemicalEntity"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: Together , these findings imply that OCT4A induction following DNA damage in PA-1 cells , performs a cell stress , rather than self-renewal , function by moderating the expression of p21Cip1 , which alongside AMPK helps to then regulate autophagy .

Example answer:
{"entities": [{"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "PA-1", "type": "CellLine"}, {"text": "p21Cip1", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The results demonstrated that hypoxia induced apoptosis , increased ROS production , and promoted autophagy in a time-dependent manner relative to that observed under normoxia .

Example answer:
{"entities": [{"text": "hypoxia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Accordingly , failure of autophagy was accompanied by an accumulation of p16ink4a , nuclear disintegration , and loss of cell recovery .

Example answer:
{"entities": [{"text": "p16ink4a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: In addition , inhibition of autophagy led to increased ROS production and a higher percentage of apoptotic cells in the two cell types .

Example answer:
{"entities": [{"text": "ROS", "type": "ChemicalEntity"}]}

Example input:
Sentence: Instead , ETO-induced OCT4A was concomitant with activation of AMPK , a key component of metabolic stress and autophagy regulation .

Example answer:
{"entities": [{"text": "ETO-induced", "type": "ChemicalEntity"}, {"text": "OCT4A", "type": "GeneOrGeneProduct"}, {"text": "AMPK", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: CONCLUSIONS : These results demonstrate that the alcohol-induced decrease in whole-body fat mass resulted in part from activation of autophagy in eWAT as protein synthesis was increased and mediated by the specific increase in the activity of S6K1 .

## Item biored:test:975
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "ChemicalEntity"}, {"text": "proteinuria", "type": "DiseaseOrPhenotypicFeature"}, {"text": "crea", "type": "ChemicalEntity"}, {"text": "sgk1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}, {"text": "nephrotic syndrome", "type": "DiseaseOrPhenotypicFeature"}, {"text": "ascites", "type": "DiseaseOrPhenotypicFeature"}, {"text": "lipidemia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hypoalbuminemia", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: These results demonstrate the critical role of the final 20 amino acids of caveolin-1 in modulating fibroblast proliferation by dampening Smad signaling and suggest that augmented Smad signaling and fibroblast hyperproliferation are contributing factors in the pathogenesis of PAH in patients with caveolin-1 c.474delA mutation .

Example answer:
{"entities": [{"text": "caveolin-1", "type": "GeneOrGeneProduct"}, {"text": "Smad", "type": "GeneOrGeneProduct"}, {"text": "PAH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "c.474delA", "type": "SequenceVariant"}]}

Example input:
Sentence: We also observed apoptotic cell death in TD as demonstrated by PI/Annexin V staining , TUNEL assay , and Cell Death ELISA .

Example answer:
{"entities": [{"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "V", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: RESULTS : KCa3.1 expression was markedly associated with endoplasmic reticulum ( ER ) stress and unfolded protein response ( UPR ) in both Abeta-stimulated primary astrocytes and brain lysates of AD patients and APP/PS1 AD mice .

Example answer:
{"entities": [{"text": "KCa3.1", "type": "GeneOrGeneProduct"}, {"text": "Abeta-stimulated", "type": "GeneOrGeneProduct"}, {"text": "AD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "APP/PS1", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: The aim of our study is to evaluate the diagnostic value of serum growth factors , apoptotic and inflammatory mediators of cirrhotic patients with and without HCC .

Example answer:
{"entities": [{"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "cirrhotic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "HCC", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Angiotensin II subtype 1a receptor signaling in resident hepatic macrophages induces liver metastasis formation .

Example answer:
{"entities": [{"text": "Angiotensin II subtype 1a receptor", "type": "GeneOrGeneProduct"}, {"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: It hydrolyzes plasma asparagine into aspartate and NH3 , causing asparagine deficit and inhibition of protein synthesis and eventually , leukemic cell death .

Example answer:
{"entities": [{"text": "asparagine", "type": "ChemicalEntity"}, {"text": "aspartate", "type": "ChemicalEntity"}, {"text": "NH3", "type": "ChemicalEntity"}, {"text": "asparagine deficit", "type": "DiseaseOrPhenotypicFeature"}, {"text": "leukemic", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: To determine whether atorvastatin attenuated CIN , the inflammatory response and apoptosis in vivo and in vitro , a rat model of iopamidol-induced CIN was used , and human embryonic proximal tubule ( HK2 ) cell damage was assessed .

Example answer:
{"entities": [{"text": "atorvastatin", "type": "ChemicalEntity"}, {"text": "CIN", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammatory", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rat", "type": "OrganismTaxon"}, {"text": "iopamidol-induced", "type": "ChemicalEntity"}, {"text": "human", "type": "OrganismTaxon"}, {"text": "HK2", "type": "CellLine"}]}

Example input:
Sentence: These results suggested that resident hepatic macrophages induced liver metastasis formation by induction of TGF-b1 through AT1a signaling .

Example answer:
{"entities": [{"text": "liver metastasis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TGF-b1", "type": "GeneOrGeneProduct"}, {"text": "AT1a", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: Serum Amyloid A Induces Inflammation , Proliferation and Cell Death in Activated Hepatic Stellate Cells .

## Item biored:test:1014
Example input:
Sentence: Women were significantly more likely to experience lactic acidosis , while men were significantly more likely to experience immune reconstitution syndrome ( p < 0.05 ) .

Example answer:
{"entities": [{"text": "Women", "type": "OrganismTaxon"}, {"text": "lactic acidosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "men", "type": "OrganismTaxon"}, {"text": "immune reconstitution syndrome", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "ChemicalEntity"}, {"text": "lipid", "type": "ChemicalEntity"}, {"text": "Ca+2 ATPase", "type": "ChemicalEntity"}, {"text": "antioxidants", "type": "ChemicalEntity"}, {"text": "Na+/K+ ATPase", "type": "ChemicalEntity"}, {"text": "Mg+2 ATPase", "type": "ChemicalEntity"}, {"text": "green tea", "type": "ChemicalEntity"}, {"text": "vitamin E", "type": "ChemicalEntity"}]}

Example input:
Sentence: In Austrians , genotype distribution differed between patients and controls ( p=0.044 ) and Cys 23 Ser was associated with weight ( p=0.039 ) , body mass index ( BMI ; p=0.038 ) , and seasonal appetite change ( p=0.031 ) .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "Cys 23 Ser", "type": "SequenceVariant"}]}

Example input:
Sentence: Because intensity of alcohol consumption is associated with poorer fetal outcomes , separate analyses were conducted for the heavy ( average of > or=5 drinks per drinking day ) alcohol consumers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}]}

Example input:
Sentence: We found little evidence that variants in alcohol metabolising genes were associated with prostate cancer diagnosis .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "prostate cancer", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Sepsis in adult male rats decreased basal protein synthesis in gastrocnemius , associated with a reduction in mTOR activation as indicated by decreased 4E-BP1 and S6K1 phosphorylation .

Example answer:
{"entities": [{"text": "Sepsis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "rats", "type": "OrganismTaxon"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "4E-BP1", "type": "GeneOrGeneProduct"}, {"text": "S6K1", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mechanistically , decreased Warburg effect as demonstrated by reduced glucose consumption and lactate secretion and reduced expression of MMP-9 , PLAU , and cathepsin B were found after LDHA knockdown or FX11 treatment in PC-3 and DU145 cells .

Example answer:
{"entities": [{"text": "glucose", "type": "ChemicalEntity"}, {"text": "lactate", "type": "ChemicalEntity"}, {"text": "MMP-9", "type": "GeneOrGeneProduct"}, {"text": "PLAU", "type": "GeneOrGeneProduct"}, {"text": "cathepsin B", "type": "GeneOrGeneProduct"}, {"text": "LDHA", "type": "GeneOrGeneProduct"}, {"text": "FX11", "type": "ChemicalEntity"}, {"text": "PC-3", "type": "CellLine"}, {"text": "DU145", "type": "CellLine"}]}

Example input:
Sentence: In developed countries , thiamine deficiency ( TD ) is most often manifested following chronic alcohol consumption leading to impaired mitochondrial function , oxidative stress , inflammation and excitotoxicity .

Example answer:
{"entities": [{"text": "thiamine deficiency", "type": "DiseaseOrPhenotypicFeature"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "alcohol", "type": "ChemicalEntity"}, {"text": "impaired mitochondrial function", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "excitotoxicity", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The ability of oral Leu to increase protein synthesis and mTOR kinase after 1 h was largely prevented in sepsis .

Example answer:
{"entities": [{"text": "Leu", "type": "ChemicalEntity"}, {"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "sepsis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Any alcohol consumption postpregnancy recognition among the heavy drinkers resulted in reduced cerebellar growth as well as decreased cranial to body growth in comparison with women who either quit drinking or who were nondrinkers .

Example answer:
{"entities": [{"text": "alcohol", "type": "ChemicalEntity"}, {"text": "reduced cerebellar growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "decreased cranial to body growth", "type": "DiseaseOrPhenotypicFeature"}, {"text": "women", "type": "OrganismTaxon"}]}

Input:
Sentence: RESULTS : While chronic alcohol feeding decreased whole-body and eWAT mass , this was associated with a discordant increase in protein synthesis in eWAT .

## Item biored:test:1008
Example input:
Sentence: We revealed the changes in murine HSC fate control orchestrated by the expression of GADD45A at single cell resolution .

Example answer:
{"entities": [{"text": "murine", "type": "OrganismTaxon"}, {"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Hsp90beta , TGF-beta , HIF-1alpha , TNF-alpha , IL-6 and MCP-1 were shown to be highly expressed in response to salt loading .

Example answer:
{"entities": [{"text": "Hsp90beta", "type": "GeneOrGeneProduct"}, {"text": "TGF-beta ,", "type": "GeneOrGeneProduct"}, {"text": "HIF-1alpha", "type": "GeneOrGeneProduct"}, {"text": "TNF-alpha", "type": "GeneOrGeneProduct"}, {"text": "IL-6", "type": "GeneOrGeneProduct"}, {"text": "MCP-1", "type": "GeneOrGeneProduct"}, {"text": "salt", "type": "ChemicalEntity"}]}

Example input:
Sentence: These data indicate that genotoxic stress-induced GADD45A expression in HSCs prevents their fatal transformation by directing them into differentiation and thereby clearing them from the system .

Example answer:
{"entities": [{"text": "GADD45A", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: We observed a time-dependent increase in mRNA and protein expression of the pro-apoptotic and pro-inflammatory HIF-1a target genes MCP1 , BNIP3 , Nix and Noxa during TD .

Example answer:
{"entities": [{"text": "HIF-1a", "type": "GeneOrGeneProduct"}, {"text": "MCP1", "type": "GeneOrGeneProduct"}, {"text": "BNIP3", "type": "GeneOrGeneProduct"}, {"text": "Nix", "type": "GeneOrGeneProduct"}, {"text": "Noxa", "type": "GeneOrGeneProduct"}, {"text": "TD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Among NASH patients , body mass index was significantly lower ( p < 0.05 ) , and non-obese patients were significantly more frequent ( p < 0.001 ) in carriers of Val175Met variant than in homozygotes of wild type PEMT .

Example answer:
{"entities": [{"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "Val175Met", "type": "SequenceVariant"}, {"text": "PEMT", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Chronic inflammation enhances gankyrin expression in the human liver .

Example answer:
{"entities": [{"text": "Chronic inflammation", "type": "DiseaseOrPhenotypicFeature"}, {"text": "gankyrin", "type": "GeneOrGeneProduct"}, {"text": "human", "type": "OrganismTaxon"}]}

Example input:
Sentence: The phosphatidylethanolamine N-methyltransferase gene V175M single nucleotide polymorphism confers the susceptibility to NASH in Japanese population .

Example answer:
{"entities": [{"text": "phosphatidylethanolamine N-methyltransferase", "type": "GeneOrGeneProduct"}, {"text": "V175M", "type": "SequenceVariant"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Serum alpha-GST levels were significantly elevated by day 4 , which corresponded to hepatotoxicity as shown by the increasing incidence of inflammation of the liver capsule , necrosis , and steatosis throughout the study .

Example answer:
{"entities": [{"text": "alpha-GST", "type": "GeneOrGeneProduct"}, {"text": "hepatotoxicity", "type": "DiseaseOrPhenotypicFeature"}, {"text": "inflammation of the liver capsule", "type": "DiseaseOrPhenotypicFeature"}, {"text": "necrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "steatosis", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: PAI-1 4G/5G promoter genotypes frequencies were similar in patients with or without liver fibrosis associated to NASH ( p = 0.6 ) .

Example answer:
{"entities": [{"text": "PAI-1", "type": "GeneOrGeneProduct"}, {"text": "patients", "type": "OrganismTaxon"}, {"text": "liver fibrosis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: BACKGROUND/AIMS : The genetic predisposition on the development of nonalcoholic steatohepatitis ( NASH ) has been poorly understood .

Example answer:
{"entities": [{"text": "nonalcoholic steatohepatitis", "type": "DiseaseOrPhenotypicFeature"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Input:
Sentence: However , global deficiency of 11b-HSD1 did increase markers of hepatic inflammation and suggests a critical role for 11b-HSD1 in restraining the transition to NASH .

## Item biored:test:1059
Example input:
Sentence: METHODS : Blood samples of 107 patients with biopsy-proven NASH and of 150 healthy volunteers were analyzed by the polymerase chain reaction ( PCR ) and restriction fragment length polymorphism .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "NASH", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: DESIGN : Genomic DNA was analysed for mutations in the AIP gene , by PCR amplification and direct sequencing .

Example answer:
{"entities": [{"text": "AIP", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Direct sequencing was used for mutation analysis .

Example answer:
{"entities": []}

Example input:
Sentence: Analyses of markers associated with the mTOR pathway were carried out on archival tumor from a subgroup using immunohistochemistry ( IHC ) and direct mutation sequencing .

Example answer:
{"entities": [{"text": "mTOR", "type": "GeneOrGeneProduct"}, {"text": "tumor", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The entire coding region of BRCA1 and BRCA2 was screened for the presence of germline mutations , by use of SSCP followed by direct sequencing of observed variants .

Example answer:
{"entities": [{"text": "BRCA1", "type": "GeneOrGeneProduct"}, {"text": "BRCA2", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutation screening of all exons of the PAX6 gene was performed by direct sequencing of PCR-amplified DNA fragments .

Example answer:
{"entities": [{"text": "PAX6", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Mutation analysis enabled prenatal diagnosis of three unaffected and one affected pregnancies .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Mutations were identified in 14 of 18 patients with LCD and in all 19 patients with GCD .

Example answer:
{"entities": [{"text": "patients", "type": "OrganismTaxon"}, {"text": "LCD", "type": "DiseaseOrPhenotypicFeature"}, {"text": "GCD", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Mutational analyses of TS and allelic imbalances were studied in all primary tumors and in 18 additional metachronic metastases .

Example answer:
{"entities": [{"text": "TS", "type": "GeneOrGeneProduct"}, {"text": "tumors", "type": "DiseaseOrPhenotypicFeature"}, {"text": "metastases", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: SSCP followed by DNA sequencing revealed TP53 mutations in 16 of 73 ( 22 % ) glioblastomas and PTEN mutations in 13 of 63 ( 21 % ) cases analyzed .

Example answer:
{"entities": [{"text": "TP53", "type": "GeneOrGeneProduct"}, {"text": "glioblastomas", "type": "DiseaseOrPhenotypicFeature"}, {"text": "PTEN", "type": "GeneOrGeneProduct"}]}

Input:
Sentence: RESULTS : Mutation analyses were successfully performed for both endoscopic biopsy and surgically resected specimens in all the cases .

## Item biored:test:1028
Example input:
Sentence: The exon 4 sequence of TGFBI of the proband exhibits the heterozygous single-nucleotide mutation , C417T , leading to amino acid substitution ( R124C ) in the encoded TGF-induced protein .

Example answer:
{"entities": [{"text": "TGFBI", "type": "GeneOrGeneProduct"}, {"text": "C417T", "type": "SequenceVariant"}, {"text": "R124C", "type": "SequenceVariant"}, {"text": "TGF-induced protein", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: The rs4704559 G allele was associated with a lower prevalence of dyskinesia ( prevalence ratio ( PR ) =0.615 , 95 % confidence interval ( CI ) 0.426-0.887 , P=0.009 ) and visual hallucinations ( PR=0.515 , 95 % CI 0.295-0.899 , P=0.020 ) .

Example answer:
{"entities": [{"text": "rs4704559", "type": "SequenceVariant"}, {"text": "dyskinesia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "visual hallucinations", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: The severe phenotype with seriously impaired intellectual development , hyperkinetic behaviour , tachycardia , hearing and visual impairment is probably due to the dominant negative effect of the I280S mutant protein and the absence of any functional TR-beta .

Example answer:
{"entities": [{"text": "impaired intellectual development", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hyperkinetic", "type": "DiseaseOrPhenotypicFeature"}, {"text": "tachycardia", "type": "DiseaseOrPhenotypicFeature"}, {"text": "hearing and visual impairment", "type": "DiseaseOrPhenotypicFeature"}, {"text": "I280S", "type": "SequenceVariant"}, {"text": "TR-beta", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Quantitative real-time PCR and GNPTG western blot analysis confirmed that the homozygous microdeletion p.G204VfsX17 had elicited NMD resulting in failure to synthesize GNPTG protein .

Example answer:
{"entities": [{"text": "GNPTG", "type": "GeneOrGeneProduct"}, {"text": "p.G204VfsX17", "type": "SequenceVariant"}]}

Example input:
Sentence: Our interpretation is that Ent3p mediates the transport of alpha-syn to the vacuole for proteolytic degradation .

Example answer:
{"entities": [{"text": "Ent3p", "type": "GeneOrGeneProduct"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Lastly , overexpression of Ent3p , which is a clathrin adapter protein involved in protein transport between the Golgi and the vacuole , causes alpha-syn to redistribute from the plasma membrane into cytoplasmic vesicular structures .

Example answer:
{"entities": [{"text": "Ent3p", "type": "GeneOrGeneProduct"}, {"text": "clathrin", "type": "ChemicalEntity"}, {"text": "alpha-syn", "type": "GeneOrGeneProduct"}]}

Example input:
Sentence: Additionally , the fetal TCRg chain repertoire is altered , and peripheral Vg4 gd T cells are mostly restricted to the IFNg-producing phenotype in HEB-deficient mice .

Example answer:
{"entities": [{"text": "TCRg", "type": "GeneOrGeneProduct"}, {"text": "Vg4", "type": "GeneOrGeneProduct"}, {"text": "IFNg-producing", "type": "GeneOrGeneProduct"}, {"text": "HEB-deficient", "type": "GeneOrGeneProduct"}, {"text": "mice", "type": "OrganismTaxon"}]}

Example input:
Sentence: Molecular dynamic ( MD ) simulations showed that the overall effect of the mutation p.Val204Asp is disruption of hydrogen bonding between Gln223 and Glu441 , leading Ser198 and His438 to move away from each other with subsequent disruption of the catalytic triad functionality regardless of the type of substrate .

Example answer:
{"entities": [{"text": "p.Val204Asp", "type": "SequenceVariant"}]}

Example input:
Sentence: We propose that the alteration in the replication/nuclear location pattern of the non-deleted TDR22 indicates an altered gene regulation hence an altered transcritpion in DGS/VCFS .

Example answer:
{"entities": [{"text": "DGS/VCFS", "type": "DiseaseOrPhenotypicFeature"}]}

Example input:
Sentence: Proband 's DNA analysis revealed a homozygous four-base-pair deletion ( TGAG ) , starting from the last base of the codon for Ser39 , leading to a coding frame shift with a new termination codon after 11 novel amino acids .

Example answer:
{"entities": [{"text": "deletion ( TGAG )", "type": "SequenceVariant"}]}

Input:
Sentence: Depletion of PI4KII isoforms also differentially affected trans-Golgi network ( TGN ) pools of PI ( 4 ) P and post-TGN traffic .
