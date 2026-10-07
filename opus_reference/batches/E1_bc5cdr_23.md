# Task
You are a biomedical named entity recognition system for the BC5CDR annotation scheme.
Identify every mention of the following entity types in the sentence:
- Chemical: Drug, compound, molecule, medication (e.g., cisplatin, aspirin).
- Disease: Pathological or medical condition (e.g., diabetes, lymphoma).

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

## Item bc5cdr:test:4615
Example input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Similarly , significant improvements in memory scores were observed using passive avoidance apparatus and aged mice .

Example answer:
{"entities": []}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Intracerebroventricular injection of U-II also caused an increase in : food intake at doses of 100 and 1,000 ng/mouse , water intake at doses of 100-10,000 ng/mouse , and horizontal locomotion activity at a dose of 10,000 ng/mouse .

Example answer:
{"entities": [{"text": "U-II", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The protective action of subcutaneously ( SC ) administered antidotes or their combinations in DFP ( 2.0 mg/kg BW ) intoxication was studied in 9-10-weeks-old Han-Wistar male rats .

Example answer:
{"entities": [{"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Input:
Sentence: METHODS : Adult male Wistar rats were intracerebroventricularly ( icv ) infused with STZ ( 750 ug ) on d 1 and d 3 , and a passive avoidance task was assessed 2 weeks after the first injection of STZ .

## Item bc5cdr:test:4767
Example input:
Sentence: Additionally , histopathological alterations mirrored both serum chemistry changes and the pattern of DNA fragmentation .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Uni- and multivariate analyses were used to test the influence of the clinical variables : age , sex , stroke , myocardiopathy ( MP ) , duration of the test , mitral regurgitation ( MR ) and the MZ dose .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "myocardiopathy", "type": "Disease"}, {"text": "MP", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "MR", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: Assay for mitochondrial respiratory function and histopathological examination of heart tissues were performed .

Example answer:
{"entities": []}

Example input:
Sentence: Evaluation of cardiac troponin I and T levels as markers of myocardial damage in doxorubicin-induced cardiomyopathy rats , and their relationship with echocardiographic and histological findings .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Serum hemoglobin , haptoglobin and angiogenesis markers of vascular endothelial growth factor and angiopoetin-2 were investigated before and after therapy .

Example answer:
{"entities": []}

Example input:
Sentence: Myocardial histologic features were analyzed semiquantitatively and results were confirmed by transmission electron microscopy .

Example answer:
{"entities": []}

Example input:
Sentence: These changes in the serum transaminases were associated with corresponding depletions in the cardiac GOT and GPT .

Example answer:
{"entities": []}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: Cardiac marker enzymes and antioxidative parameters in serum and heart tissues were measured .

Example answer:
{"entities": []}

Input:
Sentence: Serum cardiac marker enzyme , histopathological variables and expression of protein levels were analyzed .

## Item bc5cdr:test:4553
Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Electrocardiography has a very low sensitivity in detecting dobutamine-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Although there was a discrepancy between the amount of cTnI and cTnT after DOX , probably due to heterogeneity in cross-reactivities of mAbs to various cTnI and cTnT forms , it is likely that cTnT in rats after DOX indicates cell damage determined by the magnitude of injury induced and that cTnT should be a useful marker for the prediction of experimentally induced cardiotoxicity and possibly for cardioprotective experiments .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin is an effective anticancer chemotherapeutic agent known to cause acute and chronic cardiomyopathy .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: Histological evaluation of hearts from all rats given DOX revealed significant slight degrees of perivascular and interstitial fibrosis .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Input:
Sentence: Children are particularly sensitive to DOX-induced heart failure .

## Item bc5cdr:test:4678
Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: The biopsy specimen showed pathognomonic features , including eosinophilic infiltration of the interstitial compartment .

Example answer:
{"entities": []}

Example input:
Sentence: Biopsies performed in five patients revealed new pathological changes : One membranoproliferative glomerulopathy and interstitial nephritis .

Example answer:
{"entities": [{"text": "membranoproliferative glomerulopathy", "type": "Disease"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: Histopathological examination of kidney , heart and lung sections revealed moderate to massive tissue damage with a variety of morphological aberrations by all the three drugs in the absence of GSPE preexposure than in its presence .

Example answer:
{"entities": [{"text": "tissue damage", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: Nephrotoxicity was assessed by measuring the concentrations of creatinine and urea in the plasma and reduced glutathione ( GSH ) in the kidney cortex , and by light microscopic examination of kidney sections .

Example answer:
{"entities": [{"text": "Nephrotoxicity", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "urea", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}]}

Example input:
Sentence: Renal biopsy revealed severe glomerulonephritis with crescents , electron dense fibrillar deposits and moderate lymphocytic interstitial infiltrate .

Example answer:
{"entities": [{"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: Histologic examination of the renal tissue showed evidence of intravascular coagulation , primarily affecting the small arteries , arterioles , and glomeruli .

Example answer:
{"entities": [{"text": "intravascular coagulation", "type": "Disease"}]}

Example input:
Sentence: The morphological analysis of the kidneys included a semi-quantitative scoring system analysing the degree of striped fibrosis , subcapsular fibrosis and the number of basophilic tubules , plus an additional stereological analysis of the total grade of fibrosis in the cortex stained with Sirius Red .

Example answer:
{"entities": [{"text": "fibrosis", "type": "Disease"}]}

Input:
Sentence: Renal lesions were analyzed in hematoxylin and eosin , periodic acid-Schiff , and Masson 's trichrome stains .

## Item bc5cdr:test:4687
Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Cisplatin has minimal antitumor activity when used as second- or third-line treatment of metastatic breast carcinoma .

Example answer:
{"entities": [{"text": "Cisplatin", "type": "Chemical"}, {"text": "breast carcinoma", "type": "Disease"}]}

Example input:
Sentence: Intravenous hydration and mannitol was administered before and after cisplatin .

Example answer:
{"entities": [{"text": "mannitol", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: METHODS : A Phase II study of the combination of cisplatin plus amifostine was conducted in patients with progressive metastatic breast carcinoma who had received one , but not more than one , chemotherapy regimen for metastatic disease .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "breast carcinoma", "type": "Disease"}]}

Example input:
Sentence: A Phase II trial of cisplatin plus WR-2721 ( amifostine ) for metastatic breast carcinoma : an Eastern Cooperative Oncology Group Study ( E8188 ) .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "WR-2721", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "breast carcinoma", "type": "Disease"}]}

Example input:
Sentence: Early trials of cisplatin and amifostine also suggested that the incidence and severity of cisplatin-induced nephrotoxicity , ototoxicity , and neuropathy were reduced .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Although a dose-response effect has been observed with cisplatin , the dose-limiting toxicities associated with cisplatin ( e.g. , nephrotoxicity , ototoxicity , and neurotoxicity ) have limited its use as a treatment for breast carcinoma .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "toxicities", "type": "Disease"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "breast carcinoma", "type": "Disease"}]}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Therefore , three novel sigma receptor ligands with antagonist activity were evaluated in Swiss Webster mice : BD1018 ( 3S-1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -1,4-diazabicyclo [ 4.3.0 ] nonane ) , BD1063 ( 1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -4-methylpiperazine ) , and LR132 ( 1R,2S- ( + ) -cis-N- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -2- ( 1-pyrrolidinyl ) cyclohexylamine ) .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "3S-1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -1,4-diazabicyclo [ 4.3.0 ] nonane", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -4-methylpiperazine", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}]}

Input:
Sentence: Additionally , WT mice were treated with a B2 receptor antagonist after cisplatin administration .

## Item bc5cdr:test:4573
Example input:
Sentence: The cardiotoxic effects of adriamycin were studied in mammalian myocardial cells in culture as a model system .

Example answer:
{"entities": [{"text": "cardiotoxic", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Effects of acetylsalicylic acid , dipyridamole , and hydrocortisone on epinephrine-induced myocardial injury in dogs .

Example answer:
{"entities": [{"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine-induced", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: A similar bradycardic effect of clonidine was observed in isolated spontaneously beating right atria from alpha2ABC-knockout and wild-type mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Alpha2ABC-/- mice were completely unresponsive to the analgesic and hypnotic effects of clonidine ; however , clonidine significantly lowered heart rate in alpha2ABC-/- mice by up to 150 bpm .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Clonidine-induced bradycardia in conscious alpha2ABC-/- mice was 32.3 % ( 10 microg/kg ) and 26.6 % ( 100 microg/kg ) of the effect in wild-type mice .

Example answer:
{"entities": [{"text": "Clonidine-induced", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Neonatal cardiomyocytes were isolated from Sprague-Dawley rat hearts and randomly divided into controls , an adriamycin-treated group , and a 3MA plus adriamycin-treated group .

Example answer:
{"entities": [{"text": "adriamycin-treated", "type": "Chemical"}, {"text": "3MA", "type": "Chemical"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: A developmental analysis of clonidine 's effects on cardiac rate and ultrasound production in infant rats .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Therefore , in the present experiment , the effects of clonidine administration ( 0.5 mg/kg ) on cardiac rate and ultrasound production were examined in 2- , 8- , 15- , and 20-day-old rats .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Input:
Sentence: To investigate effects of aconitine on myocardial injury , we performed cytotoxicity assay in neonatal rat ventricular myocytes ( NRVMs ) , as well as measured lactate dehydrogenase level in the culture medium of NRVMs and activities of serum cardiac enzymes in rats .

## Item bc5cdr:test:4789
Example input:
Sentence: Improvement was noted with cessation of therapy .

Example answer:
{"entities": []}

Example input:
Sentence: She was treated with heparin , dipyridamole and hemodialysis ; and after more than three months , her urinary output rose above 500 ml ; and six months after the onset of anuria , dialysis treatment was stopped .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}]}

Example input:
Sentence: Her vocal change and weakness began to improve spontaneously about 3 weeks after transfer .

Example answer:
{"entities": []}

Example input:
Sentence: Proximal muscle weakness has developed during her follow-up .

Example answer:
{"entities": [{"text": "muscle weakness", "type": "Disease"}]}

Example input:
Sentence: After her strength returned , repetitive stimulation was normal , but single fiber EMG revealed increased jitter and blocking .

Example answer:
{"entities": []}

Example input:
Sentence: The patient was treated with methylprednisolone and gradually improved .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}]}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: She had a gradual return of motor function and ability of feeling Foley catheter .

Example answer:
{"entities": []}

Example input:
Sentence: Her symptoms totally regressed after drug withdrawal and reappeared when acitretin was reintroduced .

Example answer:
{"entities": [{"text": "acitretin", "type": "Chemical"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Input:
Sentence: Her symptoms improved through physical therapy but persisted to some degree .

## Item bc5cdr:test:4654
Example input:
Sentence: Simvastatin-induced bilateral leg compartment syndrome and myonecrosis associated with hypothyroidism .

Example answer:
{"entities": [{"text": "Simvastatin-induced", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}, {"text": "hypothyroidism", "type": "Disease"}]}

Example input:
Sentence: Simvastatin is metabolized by CYP3A4 .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}]}

Example input:
Sentence: CASE : A 58-year-old man received an intracarotid injection of carboplatin for recurrent glioblastomas in his left temporal lobe .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Example input:
Sentence: The patient 's lipid panel had been maintained with simvastatin for 18 months before the conversion without evidence of hepatotoxicity .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Urgent fasciotomies were performed and the patient made an uneventful recovery with the withdrawal of simvastatin .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Input:
Sentence: The patient also received simvastatin .

## Item bc5cdr:test:4625
Example input:
Sentence: The cataleptogenic effect of THC was significantly reduced in rats treated with 6-OHDA and in rats with lesions of the locus coeruleus but not in rats treated with desipramine and 6-OHDA , as compared with control rats .

Example answer:
{"entities": [{"text": "THC", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Example input:
Sentence: The current work indicates the ability of PG-9 to induce beneficial effects on cognitive processes and stimulate activity of NGF synthesis in astroglial cells .

Example answer:
{"entities": []}

Example input:
Sentence: The present study was carried out to test the effects of L-alpha-glycerylphosphorylcholine ( L-alpha-GFC ) on memory impairment induced by scopolamine in man .

Example answer:
{"entities": [{"text": "L-alpha-glycerylphosphorylcholine", "type": "Chemical"}, {"text": "L-alpha-GFC", "type": "Chemical"}, {"text": "memory impairment", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}]}

Example input:
Sentence: Reduction in GFR was associated with the development of glomerular sclerosis in both treated and untreated rats .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: METH depleted DA , caused microglial activation , and increased body temperature in CX3CR1 knockout mice to the same extent and over the same time course seen in wild-type controls .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Noxious chemical stimulation of rat facial mucosa increases intracranial blood flow through a trigemino-parasympathetic reflex -- an experimental model for vascular dysfunctions in cluster headache .

Example answer:
{"entities": [{"text": "vascular dysfunctions", "type": "Disease"}, {"text": "cluster headache", "type": "Disease"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Input:
Sentence: However , there is no research on GFC effects in the central nervous system of rodents .

## Item bc5cdr:test:4694
Example input:
Sentence: PATIENT ( S ) : A 36-year-old woman referred from the infertility clinic for blurred vision .

Example answer:
{"entities": [{"text": "infertility", "type": "Disease"}, {"text": "blurred vision", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The main pathologic diagnoses ( some overlap ) were acute rejection ( AR ; n = 4 ) , chronic rejection ( CR ; n=5 ) , AR+CR ( n =4 ) , recurrent IgA nephropathy ( n =5 ) , normal findings ( n =2 ) , minimal-type chronic FK506 nephropathy ( n = 9 ) , and mild-type FK506 nephropathy ( n = 11 ) .

Example answer:
{"entities": [{"text": "IgA nephropathy", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Ophthalmological examinations in over 1100 patients treated with one or the other agent have revealed no evidence of significant short term ( up to 2 years ) cataractogenic potential .

Example answer:
{"entities": []}

Example input:
Sentence: All patients had some response to the combined therapy and five of the seven went into complete remission after one or two courses of AraG/VP/CPM .

Example answer:
{"entities": [{"text": "AraG/VP/CPM", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Ophthalmologists at 15 institutions responded , reporting a total of 3,774 indocyanine green angiograms performed on 2,820 patients between June 1984 and September 1992 .

Example answer:
{"entities": [{"text": "indocyanine green", "type": "Chemical"}]}

Example input:
Sentence: Eight glaucomatous patients chronically treated with timolol 0.5 % /12h , suffering from depression diagnosed through DMS-III-R criteria , were included in the study .

Example answer:
{"entities": [{"text": "glaucomatous", "type": "Disease"}, {"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Twenty-four patients with recurrent Grade I to IV astrocytomas , whose resection and irradiation therapy had failed , received two to eight courses of intra-arterial BCNU therapy .

Example answer:
{"entities": [{"text": "astrocytomas", "type": "Disease"}, {"text": "BCNU", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Retrospective review of medical records of 236 patients with hyperthyroidism admitted in our department ( in- or out-patients ) from 1986 to 1992 .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}]}

Example input:
Sentence: RESULT ( S ) : A 36-year-old Chinese woman developed central retinal vein occlusion after eight courses of CC .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Input:
Sentence: METHODS : A retrospective case series involving 11 birdshot retinochoroidopathy patients ( 11 eyes ) .

## Item bc5cdr:test:4408
Example input:
Sentence: Capsaicin-induced muscle pain alters the excitability of the human jaw-stretch reflex .

Example answer:
{"entities": [{"text": "Capsaicin-induced", "type": "Chemical"}, {"text": "muscle pain", "type": "Disease"}]}

Example input:
Sentence: Our findings , showing no interaction between capsaicin treatment and attentional modulation suggest that capsaicin-induced secondary hyperalgesia and attention might affect mechanical pain through independent mechanisms .

Example answer:
{"entities": [{"text": "capsaicin", "type": "Chemical"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Attentional modulation of perceived pain intensity in capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: Capsaicin ( 0.01-1 mm ) applied to oral or nasal mucosa induced increases in dural and cortical blood flow and provoked lacrimation .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}, {"text": "increases in dural and cortical blood flow", "type": "Disease"}]}

Example input:
Sentence: Using functional magnetic resonance imaging ( fMRI ) in normal volunteers , we studied the gabapentin-induced modulation of brain activity in response to nociceptive mechanical stimulation of normal skin and capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "gabapentin-induced", "type": "Chemical"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "secondary hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: We have examined the effect of systemic administration of ketamine and lidocaine on brush-evoked ( dynamic ) pain and punctate-evoked ( static ) hyperalgesia induced by capsaicin .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Capsaicin ( 10 micro g ) was injected into the masseter muscle to induce pain in 11 healthy volunteers .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: In order to address long-term pain memory , nine healthy male volunteers received intradermal injections of three doses of capsaicin ( 0.05 , 1 and 20 microg , separated by 15 min breaks ) , each given three times in a balanced design across three sessions at one week intervals .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Differential effects of systemically administered ketamine and lidocaine on dynamic and static hyperalgesia induced by intradermal capsaicin in humans .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Input:
Sentence: Intradermal glutamate and capsaicin injections : intra- and interindividual variability of provoked hyperalgesia and allodynia .

## Item bc5cdr:test:4421
Example input:
Sentence: Capsaicin ( 10 micro g ) was injected into the masseter muscle to induce pain in 11 healthy volunteers .

Example answer:
{"entities": [{"text": "Capsaicin", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: In order to address long-term pain memory , nine healthy male volunteers received intradermal injections of three doses of capsaicin ( 0.05 , 1 and 20 microg , separated by 15 min breaks ) , each given three times in a balanced design across three sessions at one week intervals .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Capsaicin-induced muscle pain alters the excitability of the human jaw-stretch reflex .

Example answer:
{"entities": [{"text": "Capsaicin-induced", "type": "Chemical"}, {"text": "muscle pain", "type": "Disease"}]}

Example input:
Sentence: Differential effects of systemically administered ketamine and lidocaine on dynamic and static hyperalgesia induced by intradermal capsaicin in humans .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Attentional modulation of perceived pain intensity in capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: Furthermore , it was found that the magnitude of attentional modulation in secondary hyperalgesia is very similar to that of capsaicin-untreated , control condition .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin-untreated", "type": "Chemical"}]}

Example input:
Sentence: Our findings , showing no interaction between capsaicin treatment and attentional modulation suggest that capsaicin-induced secondary hyperalgesia and attention might affect mechanical pain through independent mechanisms .

Example answer:
{"entities": [{"text": "capsaicin", "type": "Chemical"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: We have examined the effect of systemic administration of ketamine and lidocaine on brush-evoked ( dynamic ) pain and punctate-evoked ( static ) hyperalgesia induced by capsaicin .

Example answer:
{"entities": [{"text": "ketamine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: To this end , persistent hyperalgesia was induced by administration of capsaicin in the tail of gonadally intact F344 rats , following which the tail was immersed in a mildly noxious thermal stimulus , and tail-withdrawal latencies measured .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}, {"text": "capsaicin", "type": "Chemical"}]}

Example input:
Sentence: Using functional magnetic resonance imaging ( fMRI ) in normal volunteers , we studied the gabapentin-induced modulation of brain activity in response to nociceptive mechanical stimulation of normal skin and capsaicin-induced secondary hyperalgesia .

Example answer:
{"entities": [{"text": "gabapentin-induced", "type": "Chemical"}, {"text": "capsaicin-induced", "type": "Chemical"}, {"text": "secondary hyperalgesia", "type": "Disease"}]}

Input:
Sentence: In conclusion , glutamate and capsaicin yield reproducible hyperalgesic and allodynic responses , and the present model is well suited for basic research , as well as for assessing the modulation of central phenomena .

## Item bc5cdr:test:4627
Example input:
Sentence: Mature male and female mice from six inbred stains were tested for susceptibility to behavioral seizures induced by a single injection of cocaine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Three hundred fifty-five adult male CSS mice , 58 B6 , and 39 A/J were tested for susceptibility to pilocarpine-induced seizures .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: One hour after the administration of gamma-HCH , the activity of seizure-inducing agents was increased , regardless of their mechanism , while 24 h after gamma-HCH a differential response was observed .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "seizure-inducing", "type": "Disease"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: Thus , FS containing 47.5 mg/ml tAMCA evoked generalized seizures in all tested rats ( n=6 ) while the lowest concentration of tAMCA ( 0.5 mg/ml ) only evoked brief episodes of jerk-correlated convulsive potentials in 1 of 6 rats .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "generalized seizures", "type": "Disease"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: In the absence of caffeine , acetaminophen ( up to 300 mg/kg ) did not modify the seizures induced by maximal electroshock and did not alter the convulsant dose of pentylenetetrezol in mice ( tests performed by the Anticonvulsant Screening Project of NINCDS ) .

Example answer:
{"entities": [{"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "pentylenetetrezol", "type": "Chemical"}]}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: The in vitro data suggest that the site responsible for the decrease in seizure activity 24 h after gamma-HCH may be the GABA-A receptor-linked chloride channel .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "GABA-A", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Input:
Sentence: GFC produced an increased latency to first seizure , at doses 25mg/kg ( 20.12 + 2.20 min ) , 50mg/kg ( 20.95 + 2.21 min ) or 75 mg/kg ( 23.43 + 1.99 min ) when compared with seized mice .

## Item bc5cdr:test:4600
Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: glycopyrrolate and atropine in the prevention of bradycardia and arrhythmias following repeated doses of suxamethonium in children .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "arrhythmias", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: Dose-dependent bradycardia induced by verapamil was potentiated by LNa , LCa , and HCa .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: A metoprolol-terbinafine combination induced bradycardia .

## Item bc5cdr:test:4493
Example input:
Sentence: Here its ability to antagonize the prolonged depletion of dopamine in the striatum by amphetamine in iprindole-treated rats is reported .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "iprindole-treated", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to study the effect of histamine H ( 3 ) -receptor ligands on neuroleptic-induced catalepsy , apomorphine-induced climbing behavior and amphetamine-induced locomotor activities in mice .

Example answer:
{"entities": [{"text": "histamine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "apomorphine-induced", "type": "Chemical"}, {"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: The prolonged depletion of dopamine in the striatum in mice , given multiple injections of methamphetamine , was also antagonized dose-dependently and completely by LY274614 .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: The data strengthen the evidence that the neurotoxic effect of amphetamine and related compounds toward nigrostriatal dopamine neurons involves NMDA receptors and that LY274614 is an NMDA receptor antagonist with long-lasting in vivo effects in rats .

Example answer:
{"entities": [{"text": "neurotoxic", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: The Dbh -/- mice had normal baseline performance in the EPM but were completely resistant to the anxiogenic effects of cocaine .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In this study , we evaluated the performance of dopamine beta-hydroxylase knockout ( Dbh -/- ) mice , which lack norepinephrine ( NE ) , in the elevated plus maze ( EPM ) to examine the contribution of noradrenergic signaling to cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "NE", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}]}

Example input:
Sentence: This study aimed at investigating the potential antipsychotic-like properties of SSR103800 , with a particular focus on models of hyperactivity , involving either drug challenge ( ie , amphetamine and MK-801 ) or transgenic mice ( ie , NMDA Nr1 ( neo-/- ) and DAT ( -/- ) ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "MK-801", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}]}

Example input:
Sentence: dose of ( +/- ) -amphetamine hemisulfate , given to rats pretreated with iprindole , resulted in persistent depletion of dopamine in the striatum 1 week later .

Example answer:
{"entities": [{"text": "iprindole", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: In contrast , SSR103800 failed to affect hyperactivity induced by amphetamine or naturally observed in dopamine transporter ( DAT ( -/- ) ) knockout mice ( 10-30 mg/kg p.o . ) .

Example answer:
{"entities": [{"text": "SSR103800", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Input:
Sentence: Effects of dehydroepiandrosterone in amphetamine-induced schizophrenia models in mice .

## Item bc5cdr:test:4568
Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: ) , while apomorphine ( 1.5 mg/kg s.c. ) and amphetamine ( 2 mg/kg s.c. ) were used for studying climbing behavior and locomotor activities , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Hydrocortisone acetate ( 50 mg ) was given orally every 6 hours for 24 hours after a 5-day fixed-salt diet ( 150 mmol/d ) .

Example answer:
{"entities": [{"text": "Hydrocortisone acetate", "type": "Chemical"}]}

Example input:
Sentence: Tetrandrine ( TET ) and fangchinoline ( FAN ) are two naturally occurring analogues with a bisbenzylisoquinoline structure .

Example answer:
{"entities": [{"text": "Tetrandrine", "type": "Chemical"}, {"text": "TET", "type": "Chemical"}, {"text": "fangchinoline", "type": "Chemical"}, {"text": "FAN", "type": "Chemical"}, {"text": "bisbenzylisoquinoline", "type": "Chemical"}]}

Example input:
Sentence: The ethanolic extract of Daucus carota seeds ( DCE ) was administered orally in three doses ( 100 , 200 , 400 mg/kg ) for seven successive days to different groups of young and aged mice .

Example answer:
{"entities": [{"text": "extract of Daucus carota seeds", "type": "Chemical"}, {"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: However , when the patient was questioned about use of herbal products and supplements , the use of creatine monohydrate was revealed .

Example answer:
{"entities": [{"text": "creatine", "type": "Chemical"}]}

Example input:
Sentence: Coniine , an alkaloid from Conium maculatum ( poison hemlock ) , has been shown to be teratogenic in livestock .

Example answer:
{"entities": [{"text": "Coniine", "type": "Chemical"}]}

Input:
Sentence: Aconitine is a major bioactive diterpenoid alkaloid with high content derived from herbal aconitum plants .

## Item bc5cdr:test:4836
Example input:
Sentence: The initiated hepatocytes in the liver were assayed as the gamma-glutamyltransferase ( gamma-GT ) positive foci formed following a 2-week selection regimen consisting of dietary 0.02 % 2-acetylaminofluorene coupled with a necrogenic dose of CCl4 .

Example answer:
{"entities": [{"text": "2-acetylaminofluorene", "type": "Chemical"}, {"text": "CCl4", "type": "Chemical"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Data from a Transnational case-control study were used to assess the risk of VTE for the latter patterns of use , while accounting for duration of use .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: The study was designed to have a power of greater than 0.90 to detect a slowing to 25 % of the expected rate of progression of weakness at P less than 0.05 .

Example answer:
{"entities": [{"text": "weakness", "type": "Disease"}]}

Example input:
Sentence: The results suggest that hypomethylation of DNA per se may not be sufficient for initiation .

Example answer:
{"entities": []}

Example input:
Sentence: In the absence of the carcinogen , 5-AzC given after a two thirds partial hepatectomy , when its incorporation should be maximum , failed to induce any gamma-GT positive foci .

Example answer:
{"entities": [{"text": "5-AzC", "type": "Chemical"}]}

Example input:
Sentence: At the highest effective doses , PG-9 did not produce any collateral symptoms as revealed by the Irwin test , and it did not modify spontaneous motility and inspection activity , as revealed by the hole-board test .

Example answer:
{"entities": []}

Example input:
Sentence: Improved outcomes among patients with head and neck carcinomas require investigations of new drugs for induction therapy .

Example answer:
{"entities": [{"text": "head and neck carcinomas", "type": "Disease"}]}

Example input:
Sentence: Visual analogue scores ( mean +/- SD ) during induction were lower in Groups L ( 3.3 +/- 2.5 ) and T ( 4.1 +/- 2.7 ) than in Group C ( 5.6 +/- 2.3 ) ; P = 0.0031 .

Example answer:
{"entities": []}

Example input:
Sentence: ) , a positive control , showed only 30 % inhibition .

Example answer:
{"entities": []}

Input:
Sentence: In order to conduct reliable testing in this regard , it is essential that a positive control for induction be available .

## Item bc5cdr:test:4387
Example input:
Sentence: We report the case of a 63-year-old female who was treated with methylphenidate due to hyperactivity and suffered from multiple ischaemic strokes .

Example answer:
{"entities": [{"text": "methylphenidate", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "ischaemic strokes", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy is a rare syndrome that may manifest in otherwise normal epileptic individuals .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "epileptic", "type": "Disease"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: The possible influence of the hepatic damage , mainly hyperammonemia , upon the development of valproate encephalopathy is discussed .

Example answer:
{"entities": [{"text": "hepatic damage", "type": "Disease"}, {"text": "hyperammonemia", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Three yr after transplantation she developed renal Fanconi syndrome with severe metabolic acidosis , hypophosphatemia , glycosuria , and aminoaciduria .

Example answer:
{"entities": [{"text": "renal Fanconi syndrome", "type": "Disease"}, {"text": "metabolic acidosis", "type": "Disease"}, {"text": "hypophosphatemia", "type": "Disease"}, {"text": "glycosuria", "type": "Disease"}, {"text": "aminoaciduria", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Input:
Sentence: Here , we describe the case of a 15-year-old girl who was on a long-term therapy with valproate due to epilepsy and revealed impaired consciousness with hyperammonemia 12 days after renal transplantation .

## Item bc5cdr:test:4657
Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Mean serum creatinine level before conversion was 2.21 mg/dL and thereafter , 4.93 mg/dL ( P = .02 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Minor elevations of creatine kinase levels are reported in about 5 % of patients .

Example answer:
{"entities": [{"text": "creatine", "type": "Chemical"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Serum creatinine values did not change significantly : 1.98 +/- 0.8 mg/dL before SRL therapy and 2.53 +/- 1.9 mg/dL at last follow-up ( P = .14 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Following major intracranial surgery in a 35-year-old man , sodium pentothal was intravenously infused to minimize cerebral ischaemia .

Example answer:
{"entities": [{"text": "sodium pentothal", "type": "Chemical"}, {"text": "cerebral ischaemia", "type": "Disease"}]}

Example input:
Sentence: Laboratory evaluation revealed 66,680 U/L creatine kinase , 93 mg/dL blood urea nitrogen , 4.6 mg/dL creatinine , 1579 U/L aspartate aminotransferase , and 738 U/L alanine aminotransferase .

Example answer:
{"entities": [{"text": "creatine", "type": "Chemical"}, {"text": "blood urea nitrogen", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "alanine", "type": "Chemical"}]}

Example input:
Sentence: Nine days later the patient 's creatine kinase had dropped to 1695 U/L and creatinine was 3.3 mg/dL .

Example answer:
{"entities": [{"text": "creatine", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Input:
Sentence: The creatine kinase peaked at 62,246 IU/L and the patient was treated with intravenous normal saline .

## Item bc5cdr:test:4232
Example input:
Sentence: The purpose of this study was to investigate the influence of calcium channel blockers on bupivacaine-induced acute toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The spinal cords of the animals that received bupivacaine , low pH normal saline ( pH 3.0 ) , or normal saline did not show abnormal findings .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Patients in Group C received 2 ml normal saline , Group L , 2 ml , lidocaine 2 % ( 40 mg ) and Group T , 2 ml thiopentone 2.5 % ( 50 mg ) .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "thiopentone", "type": "Chemical"}]}

Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Two groups of 22 similar patients were studied : one group received 6 mL prilocaine 2 % ; and the other received 3 mL bupivacaine 0.5 % .

Example answer:
{"entities": [{"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: The marked vasodilator and negative inotropic effects of propofol are disadvantages in frail elderly patients .

Example answer:
{"entities": [{"text": "propofol", "type": "Chemical"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: We conclude that lidocaine reduces the incidence and severity of propofol injection pain in ambulatory patients whereas thiopentone only reduces its severity .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "pain", "type": "Disease"}, {"text": "thiopentone", "type": "Chemical"}]}

Input:
Sentence: The cumulative bupivacaine dose given at those time points was higher in Group P. Plasma bupivacaine levels were significantly lower in Group P than in Group C. Bupivacaine levels in the brain and heart were significantly lower in Group P and Group L than in Group C. CONCLUSION : We conclude that pre-treatment with propofol in intralipid , compared with propofol in medialipid or saline , delayed the onset of bupivacaine-induced cardiotoxic effects as well as reduced plasma bupivacaine levels .

## Item bc5cdr:test:4676
Example input:
Sentence: After 12weeks , animals were euthanized , and CaCl ( 2 ) -treated , CaCl ( 2 ) -untreated ( n=12 ) and NaCl-treated aortic segments ( n=12 ) were collected for histological and molecular assessments .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl-treated", "type": "Chemical"}]}

Example input:
Sentence: The patient cohort ( 14 men , 11 women ) was treated with SRL as conversion therapy , due to chronic allograft nephropathy ( CAN ) ( n = 15 ) neoplasia ( n = 8 ) ; Kaposi 's sarcoma , Four skin cancers , One intestinal tumors , One renal cell carsinom ) or BK virus nephropathy ( n = 2 ) .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}, {"text": "chronic allograft nephropathy", "type": "Disease"}, {"text": "CAN", "type": "Disease"}, {"text": "neoplasia", "type": "Disease"}, {"text": "Kaposi 's sarcoma", "type": "Disease"}, {"text": "skin cancers", "type": "Disease"}, {"text": "intestinal tumors", "type": "Disease"}, {"text": "renal cell carsinom", "type": "Disease"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: The animals that had experienced cyclic sucrose and chow were hyperactive in response to amphetamine compared with four control groups ( ad libitum 10 % sucrose and chow followed by amphetamine injection , cyclic chow followed by amphetamine injection , ad libitum chow with amphetamine , or cyclic 10 % sucrose and chow with a saline injection ) .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}, {"text": "hyperactive", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: The semi-quantitative scoring was significantly worst in the group treated with CsA plus SRL ( P < 0.001 compared with controls ) and the analysis of the total grade of fibrosis also showed the highest proportion in the same group and was significantly different from controls ( P < 0.02 ) .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This rat study demonstrated a synergistic nephrotoxic effect of CsA plus SRL , whereas FK506 plus SRL was better tolerated .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "CsA", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}]}

Example input:
Sentence: A further deterioration was seen when CsA was combined with either FK506 or SRL , whereas the GFR remained unchanged in the group treated with FK506 plus SRL when compared with treatment with any of the single substances .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: After a 30-min baseline measure of locomotor activity ( day 0 ) , animals were maintained on a cyclic diet of 12-h deprivation followed by 12-h access to 10 % sucrose solution and chow pellets ( 12 h access starting 4 h after onset of the dark period ) for 21 days .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}]}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Input:
Sentence: Four animal groups ( n = 6 ) were tested during 9 weeks : control , CsA , SRL , and conversion ( CsA for 3 weeks followed by SRL for 6 weeks ) .

## Item bc5cdr:test:4747
Example input:
Sentence: Forty seconds after injection of suxamethonium , bradycardia and cardiac arrest occurred .

Example answer:
{"entities": [{"text": "suxamethonium", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "cardiac arrest", "type": "Disease"}]}

Example input:
Sentence: Apart from the reduction in the patient 's level of consciousness , there were no signs of motor neurone damage or of any of the other known predisposing conditions for hyperkalaemia following the administration of suxamethonium .

Example answer:
{"entities": [{"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: The duration of action may be prolonged in patients with genetic variants of the butyrylcholinesterase enzyme ( BChE ) , the most common being the K- and the A-variants .

Example answer:
{"entities": []}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Suxamethonium induced prolonged apnea in a patient receiving electroconvulsive therapy .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}]}

Example input:
Sentence: Butyrylcholinesterase gene mutations in patients with prolonged apnea after succinylcholine for electroconvulsive therapy .

Example answer:
{"entities": [{"text": "apnea", "type": "Disease"}, {"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: Suxamethonium causes prolonged apnea in patients in whom pseudocholinesterase enzyme gets deactivated by organophosphorus ( OP ) poisons .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}, {"text": "organophosphorus ( OP ) poisons", "type": "Chemical"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: The aim of the study was to assess the clinical significance of genetic variants in butyrylcholinesterase gene ( BCHE ) in patients with a suspected prolonged duration of action of succinylcholine after ECT .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : eleven of 13 patients with a prolonged duration of action of succinylcholine had mutations in BCHE , indicating that this is the possible reason for a prolonged period of apnea .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}]}

Input:
Sentence: Here , we report a case of prolonged neuromuscular block after administration of suxamethonium leading to the discovery of a novel BCHE variant ( c.695T > A , p.Val204Asp ) .

## Item bc5cdr:test:4669
Example input:
Sentence: Six patients ( 12 % ) had World Health Organization Grade 3-4 neutropenia , 2 patients ( 4 % ) had Grade 3-4 thrombocytopenia , and 2 patients ( 4 % ) had Grade 3 neurotoxicity .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Migraine ( 20 % ) was not an uncommon cause of cranial neuropathy although malignancies arising from the reticuloendothelial system or related structures of the head and neck were more frequent ( 26 % ) .

Example answer:
{"entities": [{"text": "Migraine", "type": "Disease"}, {"text": "cranial neuropathy", "type": "Disease"}, {"text": "malignancies", "type": "Disease"}]}

Example input:
Sentence: Guillain-Barr syndrome was the commonest identifiable cause ( 15.6 % ) , accounting for half of the cases with motor neuropathy .

Example answer:
{"entities": [{"text": "Guillain-Barr syndrome", "type": "Disease"}, {"text": "motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: Isolated myelopathy or peripheral neuropathy , or these manifestations occurring together , were infrequent .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: In 26.5 % of all the cases , the aetiology of the neuropathy was undetermined .

Example answer:
{"entities": [{"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Sensori-motor neuropathy was the commonest presentation ( 50 % ) .

Example answer:
{"entities": [{"text": "Sensori-motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy due to nutritional deficiency of thiamine and riboflavin was common ( 10.1 % ) and presented mainly as sensory and sensori-motor neuropathy .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "nutritional deficiency", "type": "Disease"}, {"text": "thiamine", "type": "Chemical"}, {"text": "riboflavin", "type": "Chemical"}, {"text": "sensori-motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: In the remaining cases , a combination of myelopathy , visual disturbance , and peripheral neuropathy was the most common manifestation .

Example answer:
{"entities": [{"text": "myelopathy", "type": "Disease"}, {"text": "visual disturbance", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}]}

Example input:
Sentence: Other side effects were rare , and peripheral neurotoxicity has been minor ( 26 % grade 1 ) .

Example answer:
{"entities": [{"text": "peripheral neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Peripheral neuropathy occurred in 12 patients and pancreatitis in six .

Example answer:
{"entities": [{"text": "Peripheral neuropathy", "type": "Disease"}, {"text": "pancreatitis", "type": "Disease"}]}

Input:
Sentence: Peripheral neuropathy was common ( 63 % ) , but severe grade 3-4 peripheral neuropathy was not observed .

## Item bc5cdr:test:3992
Example input:
Sentence: A single MPEP ( 5 mg/kg ip ) injection reduced the basal extracellular dopamine level in the striatum , as well as dopamine release stimulated either by methamphetamine ( 10 mg/kg sc ) or by intrastriatally administered veratridine ( 100 microM ) .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "veratridine", "type": "Chemical"}]}

Example input:
Sentence: Moreover , systemic lipopolysaccharide pretreatment ( 1 mg/kg ) attenuated local methamphetamine infusion-produced dopamine and 3,4-dihydroxyphenylacetic acid depletions in the striatum , indicating that the protective effect of lipopolysaccharide is less likely due to interrupted peripheral distribution or metabolism of methamphetamine .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Depletion of dopamine in the striatum was also antagonized when LY274614 was given after the injection of amphetamine ; LY274614 protected when given up to 4 hr after but not when given 8 or 24 hr after amphetamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: dose of ( +/- ) -amphetamine hemisulfate , given to rats pretreated with iprindole , resulted in persistent depletion of dopamine in the striatum 1 week later .

Example answer:
{"entities": [{"text": "iprindole", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Such systemic lipopolysaccharide treatment mitigated methamphetamine-induced striatal dopamine and 3,4-dihydroxyphenylacetic acid depletions in a dose-dependent manner .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "METH", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: As the most potent dose ( 1 mg/kg ) of lipopolysaccharide was administered two weeks , one day before or after the methamphetamine dosing regimen , methamphetamine-induced striatal dopamine and 3,4-dihydroxyphenylacetic acid depletions remained unaltered .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: The prolonged depletion of dopamine in the striatum in mice , given multiple injections of methamphetamine , was also antagonized dose-dependently and completely by LY274614 .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: Methamphetamine ( 10 mg/kg sc ) , administered five times , reduced the levels of dopamine and its metabolites in striatal tissue when measured 72 h after the last injection .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Input:
Sentence: This depressive-like profile induced by METH was accompanied by a marked depletion of frontostriatal dopaminergic and serotonergic neurotransmission , indicated by a reduction in the levels of dopamine , DOPAC and HVA , tyrosine hydroxylase and serotonin , observed at both 3 and 49 days post-administration .

## Item bc5cdr:test:4683
Example input:
Sentence: In salt-depleted rats , amphotericin B decreased creatinine clearance linearly with time , with an 85 % reduction by week 3 .

Example answer:
{"entities": [{"text": "amphotericin B", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Calcineurin-inhibitor therapy can lead to renal dysfunction in heart transplantation patients .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}]}

Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: The goal of this study was to determine the role of synthesis/release of bradykinin to activate B2 receptors in disruption of the blood-brain barrier during acute hypertension .

Example answer:
{"entities": [{"text": "bradykinin", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Role of activation of bradykinin B2 receptors in disruption of the blood-brain barrier during acute hypertension .

Example answer:
{"entities": [{"text": "bradykinin", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Early trials of cisplatin and amifostine also suggested that the incidence and severity of cisplatin-induced nephrotoxicity , ototoxicity , and neuropathy were reduced .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "mitochondrial impairment", "type": "Disease"}]}

Input:
Sentence: Kinin B2 receptor deletion and blockage ameliorates cisplatin-induced acute renal injury .

## Item bc5cdr:test:4480
Example input:
Sentence: CASE : A 58-year-old man received an intracarotid injection of carboplatin for recurrent glioblastomas in his left temporal lobe .

Example answer:
{"entities": [{"text": "carboplatin", "type": "Chemical"}, {"text": "glioblastomas", "type": "Disease"}]}

Example input:
Sentence: The risk of venous thromboembolism in women prescribed cyproterone acetate in combination with ethinyl estradiol : a nested cohort analysis and case-control study .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "cyproterone acetate", "type": "Chemical"}, {"text": "ethinyl estradiol", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Correlation of plasma argatroban concentration versus the patient 's coagulation variables and clinical course suggest that prolonged elevated levels of plasma argatroban may have contributed to the patient 's extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: Increased frequency of venous thromboembolism with the combination of docetaxel and thalidomide in patients with metastatic androgen-independent prostate cancer .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: This is the first report to measure plasma argatroban concentration in the context of CPB and extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: STUDY OBJECTIVE : To evaluate the frequency of venous thromboembolism ( VTE ) in patients with advanced androgen-independent prostate cancer who were treated with docetaxel alone or in combination with thalidomide .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "VTE", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}, {"text": "docetaxel", "type": "Chemical"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Input:
Sentence: Use of argatroban and catheter-directed thrombolysis with alteplase in an oncology patient with heparin-induced thrombocytopenia with thrombosis .

## Item bc5cdr:test:4551
Example input:
Sentence: We measured the plasma level of brain natriuretic peptide ( BNP ) to determine whether BNP might serve as a simple diagnostic indicator of anthracycline-induced cardiotoxicity in patients with acute leukemia treated with a daunorubicin ( DNR ) -containing regimen .

Example answer:
{"entities": [{"text": "anthracycline-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "acute leukemia", "type": "Disease"}, {"text": "daunorubicin", "type": "Chemical"}, {"text": "DNR", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Autophagic cardiomyocyte death plays an important role in the pathogenesis of heart failure in rats induced by adriamycin .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: These preliminary results suggest that BNP may be useful as an early and sensitive indicator of anthracycline-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "anthracycline-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Furthermore , adriamycin induced the formation of autophagic vacuoles , and 3MA strongly downregulated the expression of beclin 1 in adriamycin-induced failing heart and inhibited the formation of autophagic vacuoles .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "3MA", "type": "Chemical"}, {"text": "adriamycin-induced", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial injury may be involved in the progression of heart failure caused by adriamycin via the autophagy pathway .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Late , late doxorubicin cardiotoxicity .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Adriamycin-induced autophagic cardiomyocyte death plays a pathogenic role in a rat model of heart failure .

Example answer:
{"entities": [{"text": "Adriamycin-induced", "type": "Chemical"}, {"text": "death", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: Brain natriuretic peptide is a predictor of anthracycline-induced cardiotoxicity .

Example answer:
{"entities": [{"text": "anthracycline-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Anthracyclines are effective antineoplastic drugs , but they frequently cause dose-related cardiotoxicity .

Example answer:
{"entities": [{"text": "Anthracyclines", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Input:
Sentence: P53 inhibition exacerbates late-stage anthracycline cardiotoxicity .

## Item bc5cdr:test:4797
Example input:
Sentence: The cell populations were examined regarding total cell recovery correlated with gland weight , intracellular prolactin ( PRL ) content and subsequent release in primary culture , immunocytochemical PRL staining , density and/or size alterations via separation on Ficoll-Hypaque and by unit gravity sedimentation , and cell cycle analysis , after acriflavine DNA staining , by laser flow cytometry .

Example answer:
{"entities": [{"text": "acriflavine", "type": "Chemical"}]}

Example input:
Sentence: Cells were pretreated with maltolyl p-coumarate , before exposed to amyloid beta peptide ( 1-42 ) , glutamate or H2O2 .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "H2O2", "type": "Chemical"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Example input:
Sentence: Moreover , systemic lipopolysaccharide pretreatment ( 1 mg/kg ) attenuated local methamphetamine infusion-produced dopamine and 3,4-dihydroxyphenylacetic acid depletions in the striatum , indicating that the protective effect of lipopolysaccharide is less likely due to interrupted peripheral distribution or metabolism of methamphetamine .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: An autoradiographic study was performed on male F-344 rats fed diet containing FANFT at a level of 0.2 % and/or aspirin at a level of 0.5 % to evaluate the effect of aspirin on the increased cell proliferation induced by FANFT in the forestomach and bladder .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: We found that maltolyl p-coumarate significantly decreased apoptotic cell death and reduced reactive oxygen species , cytochrome c release , and caspase 3 activation .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}]}

Input:
Sentence: Maleate induced cell damage and reactive oxygen species ( ROS ) production in LLC-PK1 cells in culture .

## Item bc5cdr:test:4205
Example input:
Sentence: Salvage therapy with nelarabine , etoposide , and cyclophosphamide in relapsed/refractory paediatric T-cell lymphoblastic leukaemia and lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Leucovorin rescue was initiated 12 hours after the end of the infusion with a loading dose of 200 mg/m2 followed by 12 mg/m2 every three hours for six doses and then every six hours until the plasma methotrexate level decreased to less than 1 X 10 ( -7 ) mol/L .

Example answer:
{"entities": [{"text": "Leucovorin", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: Central nervous system complications during treatment of acute lymphoblastic leukemia in a single pediatric institution .

Example answer:
{"entities": [{"text": "Central nervous system complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Central nervous system ( CNS ) complications during treatment of childhood acute lymphoblastic leukemia ( ALL ) remain a challenging clinical problem .

Example answer:
{"entities": [{"text": "Central nervous system ( CNS ) complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: Remission induction of meningeal leukemia with high-dose intravenous methotrexate .

Example answer:
{"entities": [{"text": "meningeal leukemia", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: High-dose intravenous methotrexate is an effective treatment for the induction of remission after meningeal relapse in acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Input:
Sentence: Concerns about long-term methotrexate ( MTX ) neurotoxicity in the 1990s led to modifications in intrathecal ( IT ) therapy , leucovorin rescue , and frequency of systemic MTX administration in children with acute lymphoblastic leukemia .

## Item bc5cdr:test:4443
Example input:
Sentence: Raloxifene did not increase risk for cataracts ( RR 0.9 ; 95 % CI 0.8-1.1 ) , gallbladder disease ( RR 1.0 ; 95 % CI 0.7-1.3 ) , endometrial hyperplasia ( RR 1.3 ; 95 % CI 0.4-5.1 ) , or endometrial cancer ( RR 0.9 ; 95 % CI 0.3-2.7 ) .

Example answer:
{"entities": [{"text": "Raloxifene", "type": "Chemical"}, {"text": "cataracts", "type": "Disease"}, {"text": "gallbladder disease", "type": "Disease"}, {"text": "endometrial hyperplasia", "type": "Disease"}, {"text": "endometrial cancer", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: Similarly , pre-test scopolamine partially reversed the scopolamine-induced amnesia , but not significantly ; and pre-test cycloheximide failed to reverse the cycloheximide-induced amnesia .

Example answer:
{"entities": [{"text": "scopolamine", "type": "Chemical"}, {"text": "scopolamine-induced", "type": "Chemical"}, {"text": "amnesia", "type": "Disease"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "cycloheximide-induced", "type": "Chemical"}]}

Example input:
Sentence: Reversal by phenylephrine of the beneficial effects of intravenous nitroglycerin in patients with acute myocardial infarction .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly reversed the disruption of prepulse inhibition ( PPI ) in rats produced by apomorphine .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}]}

Example input:
Sentence: Prompt restoration of renal function followed drug withdrawal , while re-exposure to a single dose of indomethacin caused recurrence of acute reversible oliguria .

Example answer:
{"entities": [{"text": "indomethacin", "type": "Chemical"}, {"text": "oliguria", "type": "Disease"}]}

Example input:
Sentence: In conclusion , although Ro4368554 did not improve a time-related retention deficit , it reversed a cholinergic and a serotonergic memory deficit , suggesting that both mechanisms may be involved in the facilitation of object memory by Ro4368554 and , possibly , other 5-HT ( 6 ) receptor antagonists .

Example answer:
{"entities": [{"text": "memory", "type": "Disease"}]}

Example input:
Sentence: Ginsenoside Rg1 restores the impairment of learning induced by chronic morphine administration in rats .

Example answer:
{"entities": [{"text": "Ginsenoside Rg1", "type": "Chemical"}, {"text": "impairment of learning", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Rg1 , as a ginsenoside extracted from Panax ginseng , could ameliorate spatial learning impairment .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "ginsenoside", "type": "Chemical"}, {"text": "learning impairment", "type": "Disease"}]}

Input:
Sentence: Our data suggested that the ginsenoside Re , but not Rg1 or Rb1 , may contribute toward reversal of OIH .

## Item bc5cdr:test:4603
Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: We studied a 37-year-old man who developed persistent segmental dystonia within 2 months after starting sulpiride therapy .

Example answer:
{"entities": [{"text": "dystonia", "type": "Disease"}, {"text": "sulpiride", "type": "Chemical"}]}

Example input:
Sentence: CASE SUMMARY : A 25-year-old male patient , with a height of 175 cm and weight of 72 kg presented to Marmara University Hospital Emergency Department , Istanbul , Turkey , with 5 days ' history of jaundice , malaise , nausea , and vomiting .

Example answer:
{"entities": [{"text": "jaundice", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}]}

Example input:
Sentence: A 40-year-old man with leukemia and no history of cardiac disease developed recurrent , brief episodes of apparent sinus arrest while receiving continuous-infusion cimetidine 50 mg/hour .

Example answer:
{"entities": [{"text": "leukemia", "type": "Disease"}, {"text": "cardiac disease", "type": "Disease"}, {"text": "sinus arrest", "type": "Disease"}, {"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: For compounds that have shown TDP in the clinic ( terfenadine , terodiline , cisapride ) there is little differentiation between the dog ED50 and the efficacious free plasma concentrations in man ( < 10-fold ) reflecting their limited safety margins .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: These data indicate that the free ED50 in plasma for terfenadine ( 1.9 nM ) , terodiline ( 76 nM ) , cisapride ( 11 nM ) and E4031 ( 1.9 nM ) closely correlate with the free concentration in man causing QT effects .

Example answer:
{"entities": [{"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Input:
Sentence: On the 49th day of terbinafine therapy , he was brought to the emergency room for a decrease of his global health status , confusion and falls .

## Item bc5cdr:test:4441
Example input:
Sentence: together for 30 consecutive days and challenged with ISO on the day 29th and 30th , showed a significant ( P < 0.05 ) decrease in heart weight , serum marker enzymes , lipid peroxidation , Ca+2 ATPase and a significant increase in the body weight , endogenous antioxidants , Na+/K+ ATPase and Mg+2 ATPase when compared with ISO treated group and green tea or vitamin E alone treated groups .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}, {"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: In the antinociceptive and antiamnesic dose range , ( +/- ) -PG-9 did not impair mouse performance evaluated by the rota-rod test and Animex apparatus .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to investigate the effect of Rg1 on learning impairment by chronic morphine administration and the mechanism responsible for this effect .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "learning impairment", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: Previous studies have demonstrated that Rg1 might be a useful agent for the prevention and treatment of the adverse effects of morphine .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: At the highest effective doses , PG-9 did not produce any collateral symptoms as revealed by the Irwin test , and it did not modify spontaneous motility and inspection activity , as revealed by the hole-board test .

Example answer:
{"entities": []}

Example input:
Sentence: Ginsenoside Rg1 restores the impairment of learning induced by chronic morphine administration in rats .

Example answer:
{"entities": [{"text": "Ginsenoside Rg1", "type": "Chemical"}, {"text": "impairment of learning", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Rg1 , as a ginsenoside extracted from Panax ginseng , could ameliorate spatial learning impairment .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "ginsenoside", "type": "Chemical"}, {"text": "learning impairment", "type": "Disease"}]}

Input:
Sentence: However , the Rg1 and Rb1 ginsenosides failed to prevent OIH in either test .

## Item bc5cdr:test:4583
Example input:
Sentence: Angiotensin-converting enzyme inhibitors and angiotensin II receptor-blocking drugs hold promise in atrial fibrillation through cardiac remodelling .

Example answer:
{"entities": [{"text": "Angiotensin-converting", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "cardiac remodelling", "type": "Disease"}]}

Example input:
Sentence: Evaluation of cardiac troponin I and T levels as markers of myocardial damage in doxorubicin-induced cardiomyopathy rats , and their relationship with echocardiographic and histological findings .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: After re-infarction , heart size increased in the placebo group and remained unchanged in the timolol group .

Example answer:
{"entities": [{"text": "timolol", "type": "Chemical"}]}

Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: The present study was done to investigate the protective effect of TCR on experimentally induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: The results show that pretreatment with TCR may be useful in preventing the damage induced by isoproterenol in rat heart .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The effect of long-term timolol treatment on heart size after myocardial infarction was evaluated by X-ray in a double-blind study including 241 patients ( placebo 126 , timolol 115 ) .

Example answer:
{"entities": [{"text": "timolol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: In the present study , the effect of chronic pre-treatment with metformin on cardiac dysfunction and toll-like receptor 4 ( TLR4 ) activities following myocardial infarction and their relation with AMPK were assessed .

## Item bc5cdr:test:4613
Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Example input:
Sentence: In males , estradiol increased the total damage score .

Example answer:
{"entities": [{"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Most of the other low testosterone levels seemed to result from nonorganic hypothalamic dysfunction because of normal serum luteinizing hormone and prolactin and to have only a small role in erectile dysfunction ( definite improvement in only 16 of 44 [ 36 % ] after androgen therapy , normal morning or nocturnal erections in 30 % and definite vasculogenic contributions in 42 % ) .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "hypothalamic dysfunction", "type": "Disease"}, {"text": "erectile dysfunction", "type": "Disease"}]}

Example input:
Sentence: Estrogens protect ovariectomized rats from hippocampal injury induced by kainic acid-induced status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "hippocampal injury", "type": "Disease"}, {"text": "kainic", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Estradiol reduces seizure-induced hippocampal injury in ovariectomized female but not in male rats .

Example answer:
{"entities": [{"text": "Estradiol", "type": "Chemical"}, {"text": "seizure-induced", "type": "Disease"}, {"text": "hippocampal injury", "type": "Disease"}]}

Example input:
Sentence: Testosterone replacement in castrated DS rats increased BP , renal injury , and upregulation of renal angiotensinogen associated with HS diet .

Example answer:
{"entities": [{"text": "Testosterone", "type": "Chemical"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: Testosterone contributes to the development of hypertension and renal injury in male DS rats on HS diet possibly through upregulation of the intrarenal renin-angiotensin system .

Example answer:
{"entities": [{"text": "Testosterone", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "renal injury", "type": "Disease"}]}

Input:
Sentence: Testosterone ameliorates streptozotocin-induced memory impairment in male rats .

## Item bc5cdr:test:4704
Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Rare serious complications may occur in some patients , including haemorrhagic pancreatitis , bone marrow suppression , VPA-induced hepatotoxicity and VPA-induced encephalopathy .

Example answer:
{"entities": [{"text": "pancreatitis", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}, {"text": "VPA-induced", "type": "Chemical"}, {"text": "hepatotoxicity", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Outcomes included venous thromboembolism , cataracts , gallbladder disease , and endometrial hyperplasia or cancer .

Example answer:
{"entities": [{"text": "venous thromboembolism", "type": "Disease"}, {"text": "cataracts", "type": "Disease"}, {"text": "gallbladder disease", "type": "Disease"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Although the intraocular pressure elevation caused by secondary acute angle-closure glaucoma decreased and ocular pain diminished , inexorable papilledema and exudative retinal detachment continued for 3 weeks .

Example answer:
{"entities": [{"text": "glaucoma", "type": "Disease"}, {"text": "ocular pain", "type": "Disease"}, {"text": "papilledema", "type": "Disease"}, {"text": "retinal detachment", "type": "Disease"}]}

Input:
Sentence: Adverse events included increased intraocular pressure ( 54.5 % ) and cataract formation ( 100 % ) .

## Item bc5cdr:test:4721
Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: When comparing all lithium treated versus non-lithium-treated groups , lithium caused a reduction in glomerular filtration rate ( GFR ) without significant changes in effective renal plasma flow ( as determined by a marker secreted into the proximal tubules ) or lithium clearance .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Lithium-associated cognitive and functional deficits reduced by a switch to divalproex sodium : a case series .

Example answer:
{"entities": [{"text": "Lithium-associated", "type": "Chemical"}, {"text": "cognitive and functional deficits", "type": "Disease"}, {"text": "divalproex sodium", "type": "Chemical"}]}

Example input:
Sentence: Although much has been written about the management of the more common adverse effects of lithium , such as polyuria and tremor , more subtle lithium side effects such as cognitive deficits , loss of creativity , and functional impairments remain understudied .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}, {"text": "tremor", "type": "Disease"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "loss of creativity", "type": "Disease"}, {"text": "functional impairments", "type": "Disease"}]}

Example input:
Sentence: In all the experiments , the attenuation of the lithium-induced diabetes-insipidus-like syndrome by amiloride was accompanied by a reduction of the ratio between the lithium concentration in the renal medulla and its levels in the blood and an elevation in the plasma potassium level .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "diabetes-insipidus-like syndrome", "type": "Disease"}, {"text": "amiloride", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: Lithium also caused proteinuria and systolic hypertension in absence of glomerulosclerosis .

Example answer:
{"entities": [{"text": "Lithium", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: The effect of amiloride on lithium-induced polydipsia and polyuria and on the lithium concentration in the plasma , brain , kidney , thyroid and red blood cells was investigated in rats , chronically treated with LiCl .

Example answer:
{"entities": [{"text": "amiloride", "type": "Chemical"}, {"text": "lithium-induced", "type": "Chemical"}, {"text": "polydipsia", "type": "Disease"}, {"text": "polyuria", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}, {"text": "LiCl", "type": "Chemical"}]}

Example input:
Sentence: It is concluded that acute amiloride administration to lithium-treated patients suffering from polydipsia and polyuria might relieve these patients but prolonged amiloride supplementation would result in elevated lithium levels and might be hazardous .

Example answer:
{"entities": [{"text": "amiloride", "type": "Chemical"}, {"text": "lithium-treated", "type": "Chemical"}, {"text": "polydipsia", "type": "Disease"}, {"text": "polyuria", "type": "Disease"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Rats with lithium-induced nephropathy were subjected to high protein ( HP ) feeding , uninephrectomy ( NX ) or a combination of these , in an attempt to induce glomerular hyperfiltration and further progression of renal failure .

Example answer:
{"entities": [{"text": "lithium-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Lithium-induced polyuria seems to be related to extrarenal as well as to renal effects .

Example answer:
{"entities": [{"text": "Lithium-induced", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Input:
Sentence: Targeting an alternative signaling pathway , such as PKC-mediated signaling , may be an effective method of treating lithium-induced polyuria .

## Item bc5cdr:test:4716
Example input:
Sentence: 1 h prior to haloperidol resulted in a dose-dependent increase in the catalepsy times ( P < 0.05 ) .

Example answer:
{"entities": []}

Example input:
Sentence: immediately before the induction of anaesthesia , to prevent arrhythmia and bradycardia following repeated doses of suxamethonium in children , was studied .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: A 10 mg/kg dose of LY274614 was effective in antagonizing the depletion of dopamine in the striatum , when given as long as 8 hr prior to amphetamine but not when given 24 hr prior to amphetamine .

Example answer:
{"entities": [{"text": "LY274614", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : A 50 % reduction in the incidence of akathisia when prochlorperazine was administered by means of 15-minute intravenous infusion versus a 2-minute intravenous push was not detected .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}, {"text": "prochlorperazine", "type": "Chemical"}]}

Example input:
Sentence: This change resulted within 2-4 weeks in the 50-200 % increase in the plasma levels of these neuroleptics and the appearance of extrapyramidal symptoms .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}]}

Example input:
Sentence: The optimal time for the initial dose of carbon tetrachloride was after 14 days on phenobarbitone .

Example answer:
{"entities": [{"text": "carbon tetrachloride", "type": "Chemical"}, {"text": "phenobarbitone", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : patients undergoing electroconvulsive therapy ( ECT ) often receive succinylcholine as part of the anesthetic procedure .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}]}

Example input:
Sentence: Forty seconds after injection of suxamethonium , bradycardia and cardiac arrest occurred .

Example answer:
{"entities": [{"text": "suxamethonium", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "cardiac arrest", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : eleven of 13 patients with a prolonged duration of action of succinylcholine had mutations in BCHE , indicating that this is the possible reason for a prolonged period of apnea .

Example answer:
{"entities": [{"text": "succinylcholine", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}]}

Input:
Sentence: The onset time of succinylcholine was significantly longer with increasing the amount of precurarizing dose of rocuronium ( P < 0.001 ) .

## Item bc5cdr:test:4693
Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: High-dose intravenous methotrexate is an effective treatment for the induction of remission after meningeal relapse in acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Currently accepted intravitreal antibiotic regimens may cause retinal toxicity and macular ischaemia .

Example answer:
{"entities": [{"text": "retinal toxicity", "type": "Disease"}, {"text": "ischaemia", "type": "Disease"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Twenty-four patients with recurrent Grade I to IV astrocytomas , whose resection and irradiation therapy had failed , received two to eight courses of intra-arterial BCNU therapy .

Example answer:
{"entities": [{"text": "astrocytomas", "type": "Disease"}, {"text": "BCNU", "type": "Chemical"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: The ocular myasthenia associated with combination therapy of pegylated IFN alpha-2b and ribavirin for CHC is very rarely reported ; therefore , we present this case with a review of the various eye complications of IFN therapy .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "CHC", "type": "Disease"}, {"text": "IFN", "type": "Chemical"}]}

Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Input:
Sentence: PURPOSE : To report the treatment outcomes of the fluocinolone acetonide intravitreal implant ( 0.59 mg ) in patients with birdshot retinochoroidopathy whose disease is refractory or intolerant to conventional immunomodulatory therapy .

## Item bc5cdr:test:4814
Example input:
Sentence: The low incidence of cerebral haemorrhage as a cause of death in patients with Parkinson 's disease may reflect the hypotensive effect of levodopa and a hypotensive mechanism due to reduced noradrenaline levels in the parkinsonian brain .

Example answer:
{"entities": [{"text": "cerebral haemorrhage", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "hypotensive", "type": "Disease"}, {"text": "levodopa", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}, {"text": "parkinsonian", "type": "Disease"}]}

Example input:
Sentence: in the rat haloperidol-induced catalepsy model for Parkinson 's disease .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: In recent years , evidence from animal models of Parkinson 's disease has provided important information to understand the effect of specific receptor and post-receptor molecular mechanisms underlying the development of dyskinetic movements .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "dyskinetic movements", "type": "Disease"}]}

Example input:
Sentence: Causes of death , with special reference to cerebral haemorrhage , among 240 patients with pathologically verified Parkinson 's disease were investigated using the Annuals of the Pathological Autopsy Cases in Japan from 1981 to 1985 .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}, {"text": "cerebral haemorrhage", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Example input:
Sentence: In the present study , we investigated the changes occurring at the protein level in striatal samples obtained from the unilaterally 6-hydroxydopamine-lesion rat model of PD treated with saline , L-DOPA or bromocriptine using two-dimensional difference gel electrophoresis and mass spectrometry ( MS ) .

Example answer:
{"entities": [{"text": "6-hydroxydopamine-lesion", "type": "Chemical"}, {"text": "PD", "type": "Disease"}, {"text": "L-DOPA", "type": "Chemical"}, {"text": "bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: In multivariate analysis , a significant correlation between DBP reduction and worsening of the neurological score was found for the high-dose group ( beta=0.49 , P=0 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: Drug-induced parkinsonism was observed in subjects treated with risperidone ( 42 % ) and haloperidol ( 29 % ) and was observed at occupancy levels above 60 % .

Example answer:
{"entities": [{"text": "Drug-induced parkinsonism", "type": "Disease"}, {"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Depression is a major clinical feature of Parkinson 's disease .

Example answer:
{"entities": [{"text": "Depression", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}]}

Input:
Sentence: METHODS : We used logistic regression to determine the associations of these pollutants with self-reported , doctor-diagnosed Parkinson 's disease .

## Item bc5cdr:test:4522
Example input:
Sentence: Lack of teratogenicity was found in piroxicam and DFU-exposed groups .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}, {"text": "DFU-exposed", "type": "Chemical"}]}

Example input:
Sentence: The dose-limiting toxic effect was transient noncumulative granulocytopenia .

Example answer:
{"entities": [{"text": "granulocytopenia", "type": "Disease"}]}

Example input:
Sentence: Unlike general toxicity data , their prenatal toxic effects were not extensively studied before .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Less frequent toxic effects included thrombocytopenia , anemia , nausea , mild alopecia , phlebitis , and mucositis .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "alopecia", "type": "Disease"}, {"text": "phlebitis", "type": "Disease"}, {"text": "mucositis", "type": "Disease"}]}

Example input:
Sentence: Auditory toxicity was characterized by a mid- to high-frequency neurosensorial hearing loss and the lesion was of the cochlear type .

Example answer:
{"entities": [{"text": "Auditory toxicity", "type": "Disease"}, {"text": "neurosensorial hearing loss", "type": "Disease"}]}

Example input:
Sentence: Major toxicities were cardiotoxicity and leukopenia .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "leukopenia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Maternal toxicity , intrauterine growth retardation , and increase of external and skeletal variations were found in rats treated with the highest dose of piroxicam .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "intrauterine growth retardation", "type": "Disease"}, {"text": "increase of external and skeletal variations", "type": "Disease"}, {"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: Decrease of fetal length was the only signs of the DFU developmental toxicity observed in pups exposed to the highest compound dose .

Example answer:
{"entities": [{"text": "DFU", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: The major teratogenic outcome is arthrogryposis , presumably due to nicotinic receptor blockade .

Example answer:
{"entities": [{"text": "arthrogryposis", "type": "Disease"}]}

Example input:
Sentence: Visual toxicity was of retinal origin and was characterized by a tritan-type dyschromatopsy , sometimes associated with a loss of visual acuity and pigmentary retinal deposits .

Example answer:
{"entities": [{"text": "Visual toxicity", "type": "Disease"}, {"text": "dyschromatopsy", "type": "Disease"}, {"text": "a loss of visual acuity", "type": "Disease"}, {"text": "pigmentary retinal deposits", "type": "Disease"}]}

Input:
Sentence: Toxicity included embryolethality , teratogenicity , and growth retardation .
