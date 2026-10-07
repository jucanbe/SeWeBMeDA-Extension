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

## Item biored:test:811
Input:
Sentence: The model mice had much higher serum levels of ALT and AST than the normal mice .

## Item biored:test:783
Input:
Sentence: We also found increased PTEN activity concurrent with OGD time-dependent ( 4-8 h ) dephosphorylation of Akt ( Ser473 ) and GSK-3b ( Ser9 ) .

## Item biored:test:829
Input:
Sentence: INTERVENTIONS : Continuous sedation with dexmedetomidine or propofol .

## Item biored:test:797
Input:
Sentence: RESULTS : While the CAN and PD groups tended to record greater deficits than the non-drug controls , the MDMA and EX-MDMA groups recorded greater deficits than all the control groups on ten of the 13 psychometric measures .

## Item biored:test:842
Input:
Sentence: Statistical analysis was carried out using Kruskal-Wallis test for hyper locomotion , and one-way ANOVA for climbing and catalepsy tests .

## Item biored:test:739
Input:
Sentence: Genotype rs8099917 near the IL28B gene and amino acid substitution at position 70 in the core region of the hepatitis C virus are determinants of serum apolipoprotein B-100 concentration in chronic hepatitis C. The life cycle of the hepatitis C virus ( HCV ) is closely related to host lipoprotein metabolism .

## Item biored:test:857
Input:
Sentence: To confirm the pro-apoptotic effects , we performed flow cytometric detection , cardiac histology , transmission electron microscopy and terminal deoxynucleotidyl transferase-mediated dUTP-biotin nick end labeling assay .

## Item biored:test:719
Input:
Sentence: Sjogren-Larsson syndrome ( SLS ) is an autosomal recessive disorder characterized by ichthyosis , mental retardation , spasticity and mutations in the ALDH3A2 gene for fatty aldehyde dehydrogenase , an enzyme that catalyzes the oxidation of fatty aldehyde to fatty acid .

## Item biored:test:860
Input:
Sentence: The expression analysis of apoptosis-related proteins revealed that pro-apoptotic protein expression was upregulated , and anti-apoptotic protein BCL-2 expression was downregulated .

## Item biored:test:787
Input:
Sentence: This NP1 induction preceded the increased mitochondrial release of cytochrome C ( Cyt C ) into the cytosol , activation of caspase-3 and OGD time-dependent cell death in WT primary hippocampal neurons .

## Item biored:test:806
Input:
Sentence: The inflammation and scaffold structure in liver were stained with hematoxylin and eosin and silver staining respectively .

## Item biored:test:804
Input:
Sentence: 39 male BABL/c mice were randomly divided into four groups : normal control , model control , CMCS treatment and 1,10-phenanthroline treatment groups .

## Item biored:test:844
Input:
Sentence: Both DHEA 50 mg/kg ( p < 0.05 ) , and 100 mg/kg ( p < 0.01 ) significantly decreased all movements compared with the amphetamine-induced locomotion group .

## Item biored:test:821
Input:
Sentence: Physicians should recognise the possibility of fatal bacterial infections related to bortezomib plus high-dose dexamethasone in elderly patients , and we believe this case warrants further investigation .

## Item biored:test:835
Input:
Sentence: Providers should similarly consider the likelihood of hypotension or bradycardia before starting either sedative .

## Item biored:test:859
Input:
Sentence: The expression analysis of Ca ( 2+ ) handling proteins demonstrated that aconitine promoted Ca ( 2+ ) overload through the expression regulation of Ca ( 2+ ) handling proteins .

## Item biored:test:789
Input:
Sentence: Our results indicate a regulatory role of NP1 in Bad/Bax-dependent mitochondrial release of Cyt C and caspase-3 activation .

## Item biored:test:801
Input:
Sentence: Cultured mycelium Cordyceps sinensis protects liver sinusoidal endothelial cells in acute liver injured mice .

## Item biored:test:822
Input:
Sentence: A comparison of severe hemodynamic disturbances between dexmedetomidine and propofol for sedation in neurocritical care patients .

## Item biored:test:845
Input:
Sentence: There was a significant difference between groups in the haloperidol-induced catalepsy test ( p < 0.05 ) .

## Item biored:test:808
Input:
Sentence: The protein expressions of intercellular adhesion molecule-1 ( ICAM-1 ) and vascular cell adhesion molecule-1 ( VCAM-1 ) in liver were analyzed with Western blotting .

## Item biored:test:795
Input:
Sentence: METHODS : A sample of 997 participants ( 52 % male ) was recruited to four control groups ( non-drug ( ND ) , alcohol/nicotine ( AN ) , cannabis/alcohol/nicotine ( CAN ) , non-ecstasy polydrug ( PD ) ) , and two ecstasy polydrug groups ( present ( MDMA ) and past users ( EX-MDMA ) .

## Item biored:test:825
Input:
Sentence: The primary objective of this study is to compare the prevalence of severe hemodynamic effects in neurocritical care patients receiving dexmedetomidine and propofol .

## Item biored:test:858
Input:
Sentence: The results showed that aconitine stimulated apoptosis time-dependently .

## Item biored:test:817
Input:
Sentence: Bortezomib and high-dose dexamethasone-containing regimens are considered to be generally tolerable with few severe bacterial infections in patients with B-cell malignancies .

## Item biored:test:848
Input:
Sentence: We suggest that DHEA displays typical neuroleptic-like effects , and may be used in the treatment of schizophrenia .

## Item biored:test:837
Input:
Sentence: OBJECTIVE : To examine the effects of dehydroepiandrosterone ( DHEA ) on animal models of schizophrenia .

## Item biored:test:871
Input:
Sentence: Animals were also treated with lithium for 6 weeks .

## Item biored:test:870
Input:
Sentence: Similar results were observed with UT-A1 expression .

## Item biored:test:850
Input:
Sentence: Aconitine is a major bioactive diterpenoid alkaloid with high content derived from herbal aconitum plants .

## Item biored:test:761
Input:
Sentence: AIMS : To elucidate how the nicotinic acetylcholine receptors expressed on bronchial and oral epithelial cells targeted by the tobacco nitrosamine ( 4- ( methylnitrosamino ) -1- ( 3-pyridyl ) -1-butanone ) ( NNK ) facilitate carcinogenic transformation .

## Item biored:test:764
Input:
Sentence: Other cancer-related genes whose upregulation by NNK was abolishable by rSLURP-1 were the growth factors EGF in BEP2D cells and HGF in Het-1A cells , and the transcription factors CDKN2A and STAT3 ( Het-1A only ) .

## Item biored:test:782
Input:
Sentence: Our results show induction of NP1 in primary hippocampal neurons following OGD exposure ( 4-8 h ) and in the ipsilateral hippocampal CA1 and CA3 regions at 24-48 h post-HI compared to the contralateral side .

## Item biored:test:762
Input:
Sentence: MAIN METHODS : Since NNK-dependent transformation can be abolished by the nicotinergic secreted mammalian Ly-6/urokinase plasminogen activator receptor related protein-1 ( SLURP-1 ) , we compared effects of NNK and recombinant ( r ) SLURP-1 on the expression of genes related to tumorigenesis in human immortalized bronchial and oral epithelial cell lines BEP2D and Het-1A , respectively .

## Item biored:test:800
Input:
Sentence: CONCLUSIONS : Given this record of impaired memory and clinically significant levels of depression , impulsiveness , and sleep disturbance , the prognosis for the current generation of ecstasy users is a major cause for concern .

## Item biored:test:803
Input:
Sentence: The mice were injected intraperitoneally with lipopolysaccharide ( LPS ) and D-galactosamine ( D-GalN ) .

## Item biored:test:816
Input:
Sentence: Necrotising fasciitis after bortezomib and dexamethasone-containing regimen in an elderly patient of Waldenstrom macroglobulinaemia .

## Item biored:test:814
Input:
Sentence: CMCS could protect LSECs from injury and maintain the microvasculature integration in acute injured liver of mice induced by LPS/D-GalN .

## Item biored:test:834
Input:
Sentence: CONCLUSIONS : Severe hypotension and bradycardia occur at similar prevalence in neurocritical care patients who receive dexmedetomidine or propofol .

## Item biored:test:740
Input:
Sentence: Serum levels of lipid are associated with the response to pegylated interferon plus ribavirin ( PEG-IFN/RBV ) therapy , while single nucleotide polymorphisms ( SNPs ) around the human interleukin 28B ( IL28B ) gene locus and amino acid substitutions in the core region of the HCV have been reported to affect the efficacy of PEG-IFN/RBV therapy in chronic hepatitis with HCV genotype 1b infection .

## Item biored:test:765
Input:
Sentence: NNK also upregulated the anti-apoptotic BCL2 ( Het-1A ) and downregulated the pro-apoptotic TNF ( Het-1A ) , BAX and CASP8 ( BEP2D ) , all of which could be abolished , in part , by rSLURP-1 .

## Item biored:test:836
Input:
Sentence: Effects of dehydroepiandrosterone in amphetamine-induced schizophrenia models in mice .

## Item biored:test:851
Input:
Sentence: Emerging evidence indicates that voltage-dependent Na ( + ) channels have pivotal roles in the cardiotoxicity of aconitine .

## Item biored:test:882
Input:
Sentence: These RSV-inducible cytokines were also observed in the airways of mice during an infection .

## Item biored:test:847
Input:
Sentence: CONCLUSION : We observed that DHEA reduced locomotor activity and increased catalepsy at both doses , while it had no effect on climbing behavior .

## Item biored:test:868
Input:
Sentence: WT mice had increased urine output and lowered urine osmolality after 3 and 5 days of treatment whereas PKCa KO mice had no change in urine output or concentration .

## Item biored:test:766
Input:
Sentence: NNK decreased expression of the CTNNB1 gene encoding the intercellular adhesion molecule beta-catenin ( BEP2D ) , as well as tumor suppressors CDKN3 and FOXD3 in BEP2D cells and SERPINB5 in Het-1A cells .

## Item biored:test:906
Input:
Sentence: A more comprehensive understanding of skin development mechanisms will drive identification of new treatment targets and modalities .

## Item biored:test:838
Input:
Sentence: METHODS : Seventy Swiss albino female mice ( 25-35 g ) were divided into 4 groups : amphetamine-free ( control ) , amphetamine , 50 , and 100 mg/kg DHEA .

## Item biored:test:791
Input:
Sentence: Depression , impulsiveness , sleep , and memory in past and present polydrug users of 3,4-methylenedioxymethamphetamine ( MDMA , ecstasy ) .

## Item biored:test:864
Input:
Sentence: Lithium , an effective antipsychotic , induces nephrogenic diabetes insipidus ( NDI ) in 40 % of patients .

## Item biored:test:802
Input:
Sentence: Cultured mycelium Cordyceps sinensis ( CMCS ) was widely used for a variety of diseases including liver injury , the current study aims to investigate the protective effects of CMCS on liver sinusoidal endothelial cells ( LSECs ) in acute injury liver and related action mechanisms .

## Item biored:test:856
Input:
Sentence: The results showed that aconitine resulted in myocardial injury and reduced NRVMs viability dose-dependently .

## Item biored:test:852
Input:
Sentence: However , no reports are available on the role of Ca ( 2+ ) in aconitine poisoning .

## Item biored:test:853
Input:
Sentence: In this study , we explored the importance of pathological Ca ( 2+ ) signaling in aconitine poisoning in vitro and in vivo .

## Item biored:test:912
Input:
Sentence: Those defects compromised proper ridge cell elongation into a flattened epithelial morphology , resulting in thickened MFF edges .

## Item biored:test:861
Input:
Sentence: Furthermore , increased phosphorylation of MAPK family members , especially the P-P38/P38 ratio was found in cardiac tissues .

## Item biored:test:916
Input:
Sentence: Furthermore , our findings demonstrated that successive , coordinated ridge cell shape changes drive apical MFF development , making MFF ridge cells a valuable model for investigating how the coordinated regulation of cell polarity and cell shape changes serves as a crucial mechanism of epithelial morphogenesis .

## Item biored:test:819
Input:
Sentence: We report a case of a 76-year-old man with Waldenstrom macroglobulinaemia who suffered necrotising fasciitis without neutropenia after the combination treatment with bortezomib , high-dose dexamethasone and rituximab .

## Item biored:test:788
Input:
Sentence: In contrast , in NP1-KO neurons there was no translocation of Bad and Bax from cytosol to the mitochondria , and no evidence of D ( m ) loss , increased Cyt C release and caspase-3 activation following OGD ; which resulted in significantly reduced neuronal death .

## Item biored:test:878
Input:
Sentence: Characterizing the host cytokine response to RSV infection , the regulation of host cytokines and the impact of neutralizing an RSV-inducible cytokine during infection were undertaken in this study .

## Item biored:test:616
Input:
Sentence: We analyzed for PIK3CA and KRAS mutations and LINE-1 methylation by Pyrosequencing , microsatellite instability ( MSI ) , and DNA methylation ( epigenetic changes ) in eight CpG island methylator phenotype ( CIMP ) -specific promoters [ CACNA1G , CDKN2A ( p16 ) , CRABP1 , IGF2 , MLH1 , NEUROG1 , RUNX3 , and SOCS1 ] by MethyLight ( real-time PCR ) .

## Item biored:test:905
Input:
Sentence: Skin disorders are widespread , but available treatments are limited .

## Item biored:test:887
Input:
Sentence: CONCLUSIONS : RSV infection in the epithelium induces a network of immune factors to counter infection , primarily in a RIG-I dependent manner .

## Item biored:test:863
Input:
Sentence: Absence of PKC-alpha attenuates lithium-induced nephrogenic diabetes insipidus .

## Item biored:test:891
Input:
Sentence: We thus attempted to confirm neuroprotective effects of NSP on astrocytes in the ischemic state and then explored the relative mechanisms .

## Item biored:test:866
Input:
Sentence: Targeting an alternative signaling pathway , such as PKC-mediated signaling , may be an effective method of treating lithium-induced polyuria .

## Item biored:test:922
Input:
Sentence: Transcriptomics analysis indicated that 617 genes were upregulated and 665 genes were downregulated by PPARa activation ( q value < 0.05 ) .

## Item biored:test:869
Input:
Sentence: Western blot analysis revealed that AQP2 expression in medullary tissues was lowered after 3 and 5 days in WT mice ; however , AQP2 was unchanged in PKCa KO .

## Item biored:test:924
Input:
Sentence: Among the most highly repressed genes upon PPARa activation were several chemokines ( e.g .

## Item biored:test:898
Input:
Sentence: It also reduced NO/TNF-alpha release .

## Item biored:test:919
Input:
Sentence: However , much less is known about the role of PPARa in human liver .

## Item biored:test:883
Input:
Sentence: To identify the regulation of RSV inducible cytokines , Mavs and Trif deficient animals were infected with RSV .

## Item biored:test:901
Input:
Sentence: Our results thus verified the neuroprotective effects of NSP in ischemic astrocytes .

## Item biored:test:876
Input:
Sentence: Leukemia inhibitory factor protects the lung during respiratory syncytial viral infection .

## Item biored:test:867
Input:
Sentence: PKC-alpha null mice ( PKCa KO ) and strain-matched wild type ( WT ) controls were treated with lithium for 0 , 3 or 5 days .

## Item biored:test:888
Input:
Sentence: Expression of LIF protects the lung from lung injury and enhanced pathology during RSV infection .

## Item biored:test:889
Input:
Sentence: Neuroprotective effect of neuroserpin in oxygen-glucose deprivation- and reoxygenation-treated rat astrocytes in vitro .

## Item biored:test:854
Input:
Sentence: We found that Ca ( 2+ ) overload lead to accelerated beating rhythm in adult rat ventricular myocytes and caused arrhythmia in conscious freely moving rats .

## Item biored:test:872
Input:
Sentence: Lithium-treated WT mice had 19-fold increased urine output whereas treated PKCa KO animals had a 4-fold increase in output .

## Item biored:test:877
Input:
Sentence: BACKGROUND : Respiratory syncytial virus ( RSV ) infects the lung epithelium where it stimulates the production of numerous host cytokines that are associated with disease burden and acute lung injury .

## Item biored:test:890
Input:
Sentence: Neuroserpin ( NSP ) reportedly exerts neuroprotective effects in cerebral ischemic animal models and patients ; however , the mechanism of protection is poorly understood .

## Item biored:test:911
Input:
Sentence: In nrg2a mutant larvae , the basal keratinocytes within the apical MFF , known as ridge cells , displayed reduced pAKT levels as well as reduced apical domains and exaggerated basolateral domains .

## Item biored:test:913
Input:
Sentence: Pharmacological inhibition verified that Nrg2a signals through the ErbB receptor tyrosine kinase network .

## Item biored:test:917
Input:
Sentence: The impact of PPARa activation on whole genome gene expression in human precision cut liver slices .

## Item biored:test:849
Input:
Sentence: Aconitine-induced Ca2+ overload causes arrhythmia and triggers apoptosis through p38 MAPK signaling pathway in rats .

## Item biored:test:914
Input:
Sentence: Moreover , knockdown of the epithelial polarity regulator and tumor suppressor lgl2 ameliorated the nrg2a mutant phenotype .

## Item biored:test:880
Input:
Sentence: Neutralizing anti-leukemia inhibitory factor ( LIF ) IgG or control IgG was administered to a group of wild-type animals prior to RSV infection .

## Item biored:test:937
Input:
Sentence: CEP55 mRNA and protein expression levels were detected by quantitative real-time PCR ( qRT-PCR ) , Western blotting , and immunohistochemistry ( IHC ) .

## Item biored:test:895
Input:
Sentence: The proteins related to the NF-kappaB , ERK1/2 , and PI3K/Akt pathways were investigated by Western blotting .

## Item biored:test:501
Input:
Sentence: METHODS : We examined associations between common germline genetic variation in 13 genes involved in cell cycle control ( CCND1 , CCND2 , CCND3 , CCNE1 , CDK2 [ p33 ] , CDK4 , CDK6 , CDKN1A [ p21 , Cip1 ] , CDKN1B [ p27 , Kip1 ] , CDKN2A [ p16 ] , CDKN2B [ p15 ] , CDKN2C [ p18 ] , and CDKN2D [ p19 ] ) and survival among women diagnosed with invasive breast cancer participating in the SEARCH ( Studies of Epidemiology and Risk factors in Cancer Heredity ) breast cancer study .

## Item biored:test:862
Input:
Sentence: Hence , our results suggest that aconitine significantly aggravates Ca ( 2+ ) overload and causes arrhythmia and finally promotes apoptotic development via phosphorylation of P38 mitogen-activated protein kinase .

## Item biored:test:938
Input:
Sentence: Potential associations of CEP55 expression scores with clinical parameters and patient survival were evaluated .

## Item biored:test:897
Input:
Sentence: We found that NSP significantly increased the cell survival rate and reduced LDH release in OGD/R-treated astrocytes .

## Item biored:test:902
Input:
Sentence: The potential mechanisms include inhibition of the release of NO/TNF-alpha and repression of the NF-kappaB signaling pathways .

## Item biored:test:939
Input:
Sentence: CEP55 function was investigated further using RNA interference , wound healing assay , transwell assay , immunofluorescence analysis , qRT-PCR , and Western blotting .

## Item biored:test:903
Input:
Sentence: Our data also indicated that NSP has little influence on the MAPK and PI3K/Akt pathways .

## Item biored:test:908
Input:
Sentence: In vivo selection for skin-specific expression of gene-break transposon ( GBT ) mutant lines identified eleven new , revertible GBT alleles of genes involved in skin development .

## Item biored:test:927
Input:
Sentence: TLR3 , NOS2 , and LCN2 ) .

## Item biored:test:813
Input:
Sentence: Compared with the model group , CMCS and 1,10-phenanthroline significantly improved serum ALT/AST , attenuated hepatic inflammation and improved peroxidative injury in liver , decreased MMP-2/9 activities in liver tissue , improved integration of scaffold structure , and decreased protein expression of VCAM-1 and ICAM-1 .
