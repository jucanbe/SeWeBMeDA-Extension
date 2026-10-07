# Task
You are a biomedical named entity recognition system for the MedMentions annotation scheme.
Identify every mention of the following entity types in the sentence:
- AnatomicalStructure: Specific parts of the body or anatomical regions (e.g., left ventricle, femoral artery).
- Bacterium: Bacterial organisms mentioned in the text (e.g., Escherichia coli, Staphylococcus aureus).
- BiologicFunction: Biological or physiological processes and functions (e.g., immune response, hemostasis).
- BiomedicalOccupationOrDiscipline: Biomedical roles or disciplines (e.g., cardiologist, oncology, radiology).
- BodySubstance: Substances originating from the body (e.g., blood, plasma, cerebrospinal fluid).
- BodySystem: Functional body systems (e.g., cardiovascular system, respiratory system).
- Chemical: Chemical substances and compounds (e.g., ethanol, sodium chloride).
- ClinicalAttribute: Clinical characteristics or attributes (e.g., severity, stage II, BMI).
- Eukaryote: Eukaryotic organisms such as parasites or fungi (e.g., Plasmodium falciparum, Candida albicans).
- Finding: Clinical findings or observations (e.g., fever, rash, wheezing, elevated creatinine).
- Food: Food items or nutrients (e.g., milk, gluten, high-fat diet).
- HealthCareActivity: Healthcare-related activities not primarily procedures (e.g., nursing care, follow-up visit).
- InjuryOrPoisoning: Injuries, poisonings, and related conditions (e.g., blunt trauma, acetaminophen overdose).
- IntellectualProduct: Guidelines, questionnaires, reports, and other intellectual artifacts (e.g., clinical guideline, survey form).
- MedicalDevice: Medical instruments or devices (e.g., pacemaker, ventilator, stent).
- Organization: Institutions or organizations (e.g., hospital, research institute, WHO).
- PopulationGroup: Groups of people or patient populations (e.g., elderly patients, pediatric population).
- ProfessionalOrOccupationalGroup: Professional groups or categories (e.g., nurses, surgeons, laboratory technicians).
- ResearchActivity: Research-related activities or study types (e.g., randomized controlled trial, cohort study).
- SpatialConcept: Spatial or locational concepts relevant to medicine (e.g., upper quadrant, distal segment).
- Virus: Viral agents (e.g., influenza virus, SARS-CoV-2).

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

## Item MedMentions:test:4272
Input:
Sentence: Moreover , targeting of a single bioenergetic protein , phosphoglycerate kinase 1 ( Pgk1 ) , was found to modulate motor neuron vulnerability in vivo .

## Item MedMentions:test:4282
Input:
Sentence: These rats would be assessed from the neurological perspective based on their grades of performance in a sequence of tests 24 hours before and 12 hours after brain injury .

## Item MedMentions:test:4374
Input:
Sentence: 32 years , SD = .48 , at Wave 3 ) who participated in Waves 3 - 5

## Item MedMentions:test:4247
Input:
Sentence: Our results suggest for the first time the therapeutic potential of AS in a model of septic arthritis by mechanisms involving microbicidal effects , anti - inflammatory actions and reduction of disease severity .

## Item MedMentions:test:4579
Input:
Sentence: The dataset reviews small mammal communities from the Atlantic forest of South America , one of the regions with the highest diversity of small mammals and a global biodiversity hotspot , though currently covering less than 12 % of its original area due to anthropogenic pressures .

## Item MedMentions:test:4590
Input:
Sentence: 5 x 14 . 0 x 10 .

## Item MedMentions:test:4432
Input:
Sentence: Except for the slick hair gene , there are no other genes for which variants have been clearly associated with HT .

## Item MedMentions:test:4612
Input:
Sentence: The most highly cleaved sequence was 5 ' - TCGT * AT and , in fact , the seven most highly cleaved sequences conformed to the consensus sequence 5 ' - YYGT * AW .

## Item MedMentions:test:3921
Input:
Sentence: the nutrient uptake from litter , the resorption , or the storage of nutrients in the biomass ) , may strongly control forest structure and dynamics .

## Item MedMentions:test:4405
Input:
Sentence: Bivariate comparison showed increased prevalence of coronary artery disease in the OP group ( 32 % vs .

## Item MedMentions:test:4324
Input:
Sentence: For belted occupants , the highest risk for brainstem injury was in side impacts at 0 .

## Item MedMentions:test:4401
Input:
Sentence: Fifty - six children ( 26 boys , mean age 10 .

## Item MedMentions:test:4627
Input:
Sentence: A modified subgradient extragradient method for solving monotone variational inequalities In the setting of Hilbert space , a modified subgradient extragradient method is proposed for solving Lipschitz - continuous and monotone variational inequalities defined on a level set of a convex function .

## Item MedMentions:test:4149
Input:
Sentence: Anecdotal evidence of health improvement was supported by the quantitative analyses , which revealed statistically significant improvements in body mass index , blood pressure , dietary habits , exercise levels , alcohol intake , self - rated health and self - efficacy amongst those who completed the intervention .

## Item MedMentions:test:4633
Input:
Sentence: We found that queenright subcolonies outperformed their queenless counterparts in nearly all collective behaviors .

## Item MedMentions:test:4325
Input:
Sentence: Importantly , TCRP1 was able to directly interact with PDK1 , and 93 - 107 amino - acid and 109 - 124 amino - acid sites of TCRP1 were the common binding domain of PDK1 .

## Item MedMentions:test:4260
Input:
Sentence: This study highlights how cell lines with different lineages may present different virosomes and therefore no general conclusions can be drawn across Sf9 cells from different laboratories .

## Item MedMentions:test:3911
Input:
Sentence: In this retrospective observational study , diabetic patients who underwent pancreas transplantation in a single medical center and developed symptomatic acute macular edema and peripapillary soft exudate within 3 months after the operation were enrolled .

## Item MedMentions:test:4575
Input:
Sentence: 4 , p < 0 . 05 ) and Latina ( β = 3 .

## Item MedMentions:test:4331
Input:
Sentence: Elevated UACR , even at high - normal levels , was significantly associated with greater diastolic dysfunction .

## Item MedMentions:test:4340
Input:
Sentence: T2DM was ascertained by glycated haemoglobin level , self - report , hypoglycaemic medication use and clinical records .

## Item MedMentions:test:4280
Input:
Sentence: In the High - BNP patients , peak oxygen uptake ( V̇O2 ) was significantly increased by 8 .

## Item MedMentions:test:4619
Input:
Sentence: injuries ) and long - term negative consequences ( e . g .

## Item MedMentions:test:4342
Input:
Sentence: Work - related psychosocial stress may increase the risk of T2DM only amongst women in their early 60s .

## Item MedMentions:test:4715
Input:
Sentence: The sum of gaseous and particle concentrations ( ∑OPE ) ranged from 35 to 343 pg / m3 .

## Item MedMentions:test:4610
Input:
Sentence: 6 % of the patients , respectively ( P < 0 . 001 ) .

## Item MedMentions:test:4643
Input:
Sentence: While stakeholders generally see fingerprint -based background checks for personal care workers as potentially effective and as a net benefit , they also point to a variety of contingencies .

## Item MedMentions:test:4646
Input:
Sentence: Mean Cognitive Performance Scale score was 4 .

## Item MedMentions:test:4118
Input:
Sentence: Gastrointestinal disorders in Curry - Jones syndrome : Clinical and molecular insights from an affected newborn Curry - Jones syndrome ( CJS ) is a pattern of malformation that includes craniosynostosis , pre - axial polysyndactyly , agenesis of the corpus callosum , cutaneous and gastrointestinal abnormalities .

## Item MedMentions:test:4742
Input:
Sentence: 1 mm in the rough group and 2 . 28 ± 0 .

## Item MedMentions:test:4753
Input:
Sentence: 05 , for 89 . 8 - 100 % of samples .

## Item MedMentions:test:4192
Input:
Sentence: However , although deciliation was significantly induced by IgM and was inhibited by d - mannose or a specific Ab against fugu IgM , other lectins had no effect , and IgM without d - mannose affinity induced deciliation to a limited degree .

## Item MedMentions:test:4665
Input:
Sentence: Both remained elevated for nearly 48 h after exposure with the effect gradually decreasing .

## Item MedMentions:test:4348
Input:
Sentence: Uncoupling protein 1 ( UCP1 ) is responsible for the non - shivering thermogenesis in the BAT .

## Item MedMentions:test:4758
Input:
Sentence: To date , these methods have included ( 1 ) a simple ratiometric method that is relatively insensitive to noise in the data but has accuracy that is dependent on the staining protocol and the characteristics of the sample ; and ( 2 ) a complex paired - agent kinetic modeling method that is more accurate but is more noise - sensitive and requires a precise serial rinsing protocol .

## Item MedMentions:test:4616
Input:
Sentence: 0181 % nucleotide sequence divergence across the entire mitogenome , implying little intraspecific mtDNA genetic variation .

## Item MedMentions:test:4270
Input:
Sentence: Teens and parents completed validated measures of treatment adherence , diabetes -specific self - efficacy , quality of life , and diabetes -specific family conflict .

## Item MedMentions:test:4279
Input:
Sentence: In this study , kiss1 cDNA was cloned from the hypothalamus of Brandt 's voles and kiss1 mRNA levels were investigated in different tissues , and at different developmental stages , using high - throughput real - time PCR .

## Item MedMentions:test:4680
Input:
Sentence: This study aimed to expand the biological activities of Ts19 Frag - II through in vivo investigation .

## Item MedMentions:test:3233
Input:
Sentence: The antibiotic s used inappropriately included azithromycin enteric - coated capsules , compound cefaclor tablets and nifuratel nysfungin vaginal soft capsules in primary hospitals , amoxicillin and clavulanate potassium dispersible tablets ( 7 : 1 ) and cefonicid sodium for injection in secondary hospitals , cefminox sodium for injection and amoxicillin sodium and sulbactam sodium for injection in tertiary hospitals .

## Item MedMentions:test:4766
Input:
Sentence: After exposure to 35 ° C , the reduction in grain number was highly significant for both genotypes .

## Item MedMentions:test:3917
Input:
Sentence: In this study we aimed to evaluate the effects of dilutional anemia resulting from cardiopulmonary bypass ( CPB ) and its correction with red blood cell ( RBC ) transfusion on tissue oxygenation and renal function in diabetic patients undergoing coronary artery bypass grafting ( CABG ) .

## Item MedMentions:test:4524
Input:
Sentence: Starch content correlated positively with the amylase activity of C .

## Item MedMentions:test:4373
Input:
Sentence: We conducted a multicenter , retrospective review of 13 946 patients across 21 centers who received cervical spine surgery ( levels C2 to C7 ) between January 1 , 2005 , and December 31 , 2011 , inclusive .

## Item MedMentions:test:4762
Input:
Sentence: 1 μA cm ( - 2 ) with Michaelis - Menten constant ( Km ) of 0 .

## Item MedMentions:test:4338
Input:
Sentence: The number of excised lymph nodes of pN + BCP neither correlates with RFS nor with OAS .

## Item MedMentions:test:4514
Input:
Sentence: The mean value for the samples of Osijek - Baranja County was 19 . 63 μg / kg ( median = 15 . 8 μg / kg ) , while for Vukovar - Srijem County the mean value of citrinin was 14 , 6 μg / kg ( median = 1 . 23 μg / kg ) .

## Item MedMentions:test:4716
Input:
Sentence: The three chlorinated OPEs accounted for 88 ± 5 % of the ∑OPE .

## Item MedMentions:test:4372
Input:
Sentence: Using a combination of molecular - scale and real - time imaging , spectroscopy and spectrometry approaches , we introduce a structural motif with a universal insertion mode in reconstituted membranes and live bacteria .

## Item MedMentions:test:4474
Input:
Sentence: Relationship between interpersonal trauma exposure and addictive behaviors : a systematic review The aim of this study was to systematically summarize knowledge on the association between exposure to interpersonal trauma and addictive behaviors .

## Item MedMentions:test:4647
Input:
Sentence: There were no significant changes in cognition or ability to perform activities of daily living .

## Item MedMentions:test:4508
Input:
Sentence: Thirty - five participants with obesity were randomized to lose a similar weight rapidly ( 4 weeks ) or gradually ( 8 weeks ) , and afterwards to maintain it ( 4 weeks ) .

## Item MedMentions:test:4209
Input:
Sentence: The biofilm inhibition activities of four derivatives ( H5 - 32 , H5 - 33 , H5 - 34 , and H5 - 35 ) were further investigated under shearing forces , they all led to significant decreases in the biofilm formation of S .

## Item MedMentions:test:4412
Input:
Sentence: S100 protein level was similar in both groups at 1 h after the procedure and then decreased in the T - ICD group compared to the S - ICD group ( P = 0 . 04 ) .

## Item MedMentions:test:4615
Input:
Sentence: latos individuals collected from introduced populations at Spring Mountain Ranch State Park and Shoshone Ponds Natural Area , Nevada , USA , while a single mitogenome of 16 , 537bp was sequenced for C .

## Item MedMentions:test:4618
Input:
Sentence: Binge drinking : Health impact , prevalence , correlates and interventions Binge drinking ( also called heavy episodic drinking , risky single - occasion drinking etc . ) is a major public health problem .

## Item MedMentions:test:4224
Input:
Sentence: Our group identified the cellular prion protein ( PrP ( C ) ) and its partner , the co - chaperone Hsp70 / 90 organizing protein ( HOP ) , as potential target candidates due to their role in GBM tumorigenesis and in neural stem cell maintenance .

## Item MedMentions:test:4264
Input:
Sentence: Interestingly , instead of directly acetylating NFAT , Gcn5 catalyzes histone H3 lysine H9 acetylation to promote IL - 2 production .

## Item MedMentions:test:4669
Input:
Sentence: On a subset of example FLASHE items across these domains , responses of parents and adolescents within the same dyads were positively and significantly correlated ( r = 0 .

## Item MedMentions:test:4520
Input:
Sentence: We showed that MALDI - TOF MS is an useful technique for rapid identification of the causative agents of endophthalmitis from vitreous humor - inoculated BCBs with a simple protocol .

## Item MedMentions:test:4445
Input:
Sentence: Statistical analysis showed a correlation between BMI > 50 Kg / m2 , presence of metabolic syndrome , presence of diabetes , gastric pouch volume greater than 60 ml and failure of weight loss outcome .

## Item MedMentions:test:4529
Input:
Sentence: Our results suggest that ERK activation in the spinal dorsal horn plays a vital role in NP - evoked hyperalgesia .

## Item MedMentions:test:4768
Input:
Sentence: Bone sounding was most accurate , whereas intra - oral radiographs were least accurate .

## Item MedMentions:test:4164
Input:
Sentence: Here , using quantitative in vitro binding assays , we show that the IQ domain of IQGAP1 is both necessary and sufficient for binding to ERK1 and ERK2 , as well as to the MAPK kinases MEK1 and MEK2 .

## Item MedMentions:test:4172
Input:
Sentence: We used the GBD 2013 results for Years of Life Lost ( YLLs ) and Years Lived with Disability ( YLDs ) to calculate Disability Adjusted Life Years ( DALYs ) for PD in China .

## Item MedMentions:test:4730
Input:
Sentence: In 77 patients the mean Dermatology Life Quality Index ( DLQI ) was 12 .

## Item MedMentions:test:4559
Input:
Sentence: This trial aims to evaluate the effect of participation in an online education programme , compared with a wait - list control group , on allied health professionals ' knowledge about evidence - based CFS interventions and their levels of confidence to engage in the dissemination of these interventions .

## Item MedMentions:test:4519
Input:
Sentence: Prevalence of malnutrition was 5 % in household contacts and healthy controls , and 51 % in patients with TB .

## Item MedMentions:test:4608
Input:
Sentence: We compared the present patient series with that of our previous report statistically , and found that patients undergoing gastrostomy required significantly fewer discontinuations of tube feeding than those who did not .

## Item MedMentions:test:4614
Input:
Sentence: Whether generalist herbivores always have significantly higher GOX activities than their specialist counterparts at any comparable stage or conditions and how this is realized remain unknown .

## Item MedMentions:test:4516
Input:
Sentence: Consequently , we emphasize the need for systematic analysis of larger amount of samples , from both large grains and small grains , especially in the area of Brod - Posavina County , in order to obtain more realistic notion of citrinin contamination of grains and to asses the health risk in humans .

## Item MedMentions:test:4650
Input:
Sentence: As part of the assessment , all were given a full - length Food Frequency Questionnaire ( FFQ ) and MEDAS at baseline and after 3 months .

## Item MedMentions:test:4429
Input:
Sentence: A greater ( < 0 . 05 ) AID and SID of CP and most AA was observed in SBM from the U .

## Item MedMentions:test:4525
Input:
Sentence: The calculated correlations between the objective parameter , which was the resistance to the flow of air through the nasal cavity , and the subjective feelings of respondents expressed in the survey SNOT - 20 were generally weak , and statistical significance was achieved with respect to the first question survey ( the severity of the nose obstruction ) for all components of resistance flow .

## Item MedMentions:test:4757
Input:
Sentence: The two prophylactic drugs with the best evidence for efficacy in chronic migraine are topiramate and onabotulinumtoxinA .

## Item MedMentions:test:4376
Input:
Sentence: Unplanned readmissions within 30 days after discharge : improving quality through easy prediction To propose an easy predictive model for the risk of rehospitalization , built from hospital administrative data , in order to prevent repeated admissions and to improve transitional care .

## Item MedMentions:test:4500
Input:
Sentence: The analysis of diadochokinesis showed that MG patients had a higher mean duration of the silent interval between a series of repetitive /pa / syllables ( P < 0 . 05 ) , of the sound /t / ( P = 0 .

## Item MedMentions:test:4424
Input:
Sentence: Recovery of orthographic processing after stroke : A longitudinal fMRI study An intact orthographic processing system is critical for normal reading and spelling .

## Item MedMentions:test:3948
Input:
Sentence: in this work , we investigate cell viability , migration and tubulogenesis on human EC derived from two different tumors , breast and renal carcinoma ( BTEC and RTEC ) , compared to normal microvascular endothelium ( HMEC ) under oxidative stress , hypoxia and treatment with exogenous H2S .

## Item MedMentions:test:4486
Input:
Sentence: An additional separate group of gingivitis ( n = 21 ) and part of periodontitis patients ( n = 11 ) were subjected to non - surgical periodontal treatment whereupon changes in salivary CSF - 1 , IL - 34 , and MMP - 8 levels were determined and related to periodontal outcome .

## Item MedMentions:test:4043
Input:
Sentence: Transparent nanostructured cellulose acetate films based on the self assembly of PEO - b - PPO - b - PEO block copolymer In this study fabrication and characterization of transparent nanostructured composite films based on cellulose triacetate ( CTA ) and poly ( ethylene oxide ) - b - poly ( propylene oxide ) - b - poly ( ethylene oxide ) ( EPE ) triblock copolymer were presented .

## Item MedMentions:test:4763
Input:
Sentence: There was a good correlation between sera H2O2 values obtained by standard enzymic colourimetric method and the present biosensor ( R ( 2 ) = 0 . 99 ) .

## Item MedMentions:test:4367
Input:
Sentence: RATIONAL DESIGN OF NANOBODY80 LOOP PEPTIDOMIMETICS : TOWARDS BIASED β2 ADRENERGIC RECEPTOR LIGANDS G protein - coupled receptors ( GPCRs ) play an important role for many cellular responses , and as such their mechanism of action is of utmost interest .

## Item MedMentions:test:4522
Input:
Sentence: maculatus homogenate was observed when the insects fed on grain from the interaction of the cultivar Tapaihum inoculated with BR 3262 diazotrophs .

## Item MedMentions:test:4134
Input:
Sentence: Inhibition of p70 S6 kinase ( S6K1 ) activity by A77 1726 , the active metabolite of leflunomide , induces autophagy through TAK1 -mediated AMPK and JNK activation mTOR activation suppresses autophagy by phosphorylating ULK1 at S757 and suppressing its enzymatic activity .

## Item MedMentions:test:4692
Input:
Sentence: Gamma Knife Radiosurgery for Idiopathic Trigeminal Neuralgia ; does the status of offending vessels influence on pain control or side effects ?

## Item MedMentions:test:4765
Input:
Sentence: A temperature - sensitive period was defined , lasting from premeiotic interphase to late leptotene , during which heat can prevent PMCs from progressing through meiosis .

## Item MedMentions:test:4585
Input:
Sentence: After 2 years ' follow - up , safety was maintained in this large group of patients with BRAF ( V600 ) mutation - positive metastatic melanoma who are more representative of routine clinical practice than typical clinical trial populations .

## Item MedMentions:test:4636
Input:
Sentence: In a single breath - hold of less than 9 seconds , 30 transient state IR - ufSSFP images were acquired , yielding longitudinal ( T1 ) and transversal ( T2 ) relaxometry parameter maps using voxel -wise nonlinear fitting .

## Item MedMentions:test:4409
Input:
Sentence: Aim of the study was to compare time to therapy and to investigate cardiac , cerebral and systemic injuries of S - ICD and T - ICD shocks delivered after ventricular fibrillation ( VF ) induction .

## Item MedMentions:test:4700
Input:
Sentence: For flexibility in generating stable cell lines the sgRNAs have been cloned in a lentivirus backbone containing PiggyBac transposase recognition elements together with fluorescent and drug selection markers .

## Item MedMentions:test:4396
Input:
Sentence: We previously reported that the mRNAs of ADH7 and BDH2 , which encode putative NADPH - and NADH - dependent alcohol dehydrogenases , respectively , were efficiently translated even with translation repression in response to severe vanillin stress .

## Item MedMentions:test:4449
Input:
Sentence: Association of leukemia inhibitory factor gene polymorphism and in vitro fertilization outcome in a population in northern Iran Several studies have been demonstrated that endometrial leukemia inhibitory factor ( LIF ) is important in embryo implantation .

## Item MedMentions:test:4736
Input:
Sentence: The added value of cardiac index and pulse pressure variation monitoring to mean arterial pressure - guided volume therapy in moderate - risk abdominal surgery ( COGUIDE ) : a pragmatic multicentre randomised controlled trial There is disagreement regarding the benefits of goal - directed therapy in moderate - risk abdominal surgery .

## Item MedMentions:test:4308
Input:
Sentence: Therefore , our goal was to characterize sublingual and intestinal ( mucosal and serosal ) microvascular injury after blood resuscitation in hemorrhagic shock and its relation with O2 and CO2 metabolism .

## Item MedMentions:test:4237
Input:
Sentence: This study aimed to compare the clinical and radiographic outcomes of bilateral decompression via a unilateral approach ( BDUA ) with transforaminal lumbar interbody fusion ( TLIF ) and laminectomy with PLIF in the treatment of degenerative lumbar spondylolisthesis ( DLS ) with stenosis .

## Item MedMentions:test:4759
Input:
Sentence: Socio - demographic characteristics may influence perception of satisfaction with food consumed and potentially influence the success of public health efforts to offer nutrition guidance for families satisfied with diets that may or may not be comprised of healthy food and beverages .

## Item MedMentions:test:4327
Input:
Sentence: Based on the wzi gene DNA sequences and wzc PCR , these 56 strains were classified as capsular type wzi47 - K47 ( n = 37 ) , wzi64 - K64 ( n = 8 ) , wzi8 - K8 ( n = 4 ) , wzi37 - K37 ( n = 4 ) , wzi53 - K53 ( n = 1 ) , wzi125 - K2 ( n = 1 ) , and wzi1 - K1 ( n = 1 ) .

## Item MedMentions:test:4540
Input:
Sentence: By using 17 bacteria and 1 fungi , which include Bacillus , Candida , Enterobacter , Enterococcus , Escherichia , Klebsiella , Listeria , Pseudomonas , Salmonella and Staphylococcus genera , the activity of A .

## Item MedMentions:test:4739
Input:
Sentence: Sensitivity and Specificity of Plasma ALT , ALP , and Bile Acids for Hepatitis in Labrador Retrievers Biochemical indicators for diagnosing liver disease are plasma alanine aminotransferase activity ( ALT ) , alkaline phosphatase activity ( ALP ) , and bile acid concentration ( BA ) .
