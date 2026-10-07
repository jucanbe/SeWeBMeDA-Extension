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

## Item bc5cdr:test:2
Example input:
Sentence: This study shows that prolonged analgesic treatment in Fischer 344 rats causes progressive and irreversible damage to the interstitial matrix and type 1 interstitial cells leading to RPN .

Example answer:
{"entities": [{"text": "RPN", "type": "Disease"}]}

Example input:
Sentence: Ginsenoside Rg1 restores the impairment of learning induced by chronic morphine administration in rats .

Example answer:
{"entities": [{"text": "Ginsenoside Rg1", "type": "Chemical"}, {"text": "impairment of learning", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly induced catalepsy in rats , although their effects did not exceed 50 % induction even at the highest dose given .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: In streptozotocin-induced hyperalgesia , inducible NO synthase participates in pronociceptive activity of bradykinin , whereas in vincristine-induced hyperalgesia bradykinin seemed to activate neuronal NO synthase pathway .

Example answer:
{"entities": [{"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "vincristine-induced", "type": "Chemical"}]}

Example input:
Sentence: The results showed that rats treated with Morphine/Rg1 decreased escape latency and increased the time spent in platform quadrant and entering frequency .

Example answer:
{"entities": [{"text": "Morphine/Rg1", "type": "Chemical"}]}

Example input:
Sentence: In males , the non-competitive NMDA antagonist dextromethorphan enhanced the antihyperalgesic effect of low to moderate doses of morphine in a dose-and time-dependent manner .

Example answer:
{"entities": [{"text": "NMDA", "type": "Chemical"}, {"text": "dextromethorphan", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : These results indicate that noradrenergic signaling via beta-adrenergic receptors is required for cocaine-induced anxiety in mice .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}]}

Example input:
Sentence: Antinociceptive effect of morphine was reduced in chronically treated rats ( 39+/-10 vs. 18+/-5 au ) while the combination-induced antinociception was remained similar as an acute treatment ( 298+/-7 vs. 280+/-17 au ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}]}

Input:
Sentence: Noradrenergic influences on the activity of analgesics in rats .

## Item bc5cdr:test:83
Example input:
Sentence: One of 16 patients ( 6 % ) with prior chemotherapy had a complete response ( CR ) of 31 weeks ' duration ( 95 % CI , 0 % to 30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Since it takes three to 12 months to achieve maximal effects , those patients who are unable to continue the drug receive little benefit from it .

Example answer:
{"entities": []}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: After 6 weeks of therapy , glomerular filtration rate was not different among the studied groups .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The rigidity was considerably decreased in both groups after 20 days ' treatment .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Symptoms persisted for three months despite TAC dose reduction , administration of IVIG and four doses of methylprednisolone pulse therapy .

Example answer:
{"entities": [{"text": "TAC", "type": "Chemical"}, {"text": "methylprednisolone", "type": "Chemical"}]}

Example input:
Sentence: 1 patient with squamous cell carcinoma achieved a partial response lasting 5 months .

Example answer:
{"entities": [{"text": "squamous cell carcinoma", "type": "Disease"}]}

Input:
Sentence: Treatment has been continued in 3 individuals for 6-13 months with persistence of the pressor effect , although there appears to have been some decrease in the degree of response with time .

## Item bc5cdr:test:103
Example input:
Sentence: Given alone to any accumbal subregion , GR 55562 ( 0.1-10 microg/side ) or CP 93129 ( 0.1-10 microg/side ) did not change basal locomotor activity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : In exposed neonates , TEOAEs mean response ( across frequency ) and mean amplitude at 4000Hz was significantly lower than in non-exposed neonates .

Example answer:
{"entities": []}

Example input:
Sentence: Visual analogue scores ( mean +/- SD ) during induction were lower in Groups L ( 3.3 +/- 2.5 ) and T ( 4.1 +/- 2.7 ) than in Group C ( 5.6 +/- 2.3 ) ; P = 0.0031 .

Example answer:
{"entities": []}

Example input:
Sentence: During the six-month follow up , depression was quantified through the Beck and Zung-Conde scales every two months .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Three time domain indexes of hemodynamic variability were employed : the standard deviation of mean arterial pressure as a measure of blood pressure variability and the standard deviation of beat-to-beat intervals ( SDRR ) and the root mean square of successive differences in R-wave-to-R-wave intervals as measures of heart rate variability .

Example answer:
{"entities": []}

Example input:
Sentence: The normalized reflex amplitude increased with an increase in velocity at a given displacement , but remained constant with different displacements at a given velocity .

Example answer:
{"entities": []}

Example input:
Sentence: The normalized reflex amplitude was significantly higher during pain , but only at faster stretches in the painful muscle .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "painful muscle", "type": "Disease"}]}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: However , by comparing each subgroup to control group , we found statistically significant decreases of TEOAEs amplitudes at 4000Hz for all three groups .

Example answer:
{"entities": [{"text": "decreases of TEOAEs amplitudes", "type": "Disease"}]}

Input:
Sentence: At the same time , the mean period within each class of amplitudes shortened by 10 -- 20 ms , whereas the mean periods calculated from all oscillations together did not change significantly .

## Item bc5cdr:test:152
Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Terbutaline , a beta2-adrenoceptor agonist used to arrest preterm labor , has been associated with increased concordance for autism in dizygotic twins .

Example answer:
{"entities": [{"text": "Terbutaline", "type": "Chemical"}, {"text": "preterm labor", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: We report twin neonates who were born prematurely at 32 weeks of gestation to a mother with human immunodeficiency virus infection .

Example answer:
{"entities": [{"text": "human immunodeficiency virus infection", "type": "Disease"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reassuringly , penicillins , erythromycins , and cephalosporins , although used commonly by pregnant women , were not associated with many birth defects .

Example answer:
{"entities": [{"text": "penicillins", "type": "Chemical"}, {"text": "erythromycins", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: Three infants , born of two mothers with inflammatory bowel disease who received treatment with sulphasalazine throughout pregnancy , were found to have major congenital anomalies .

Example answer:
{"entities": [{"text": "inflammatory bowel disease", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "congenital anomalies", "type": "Disease"}]}

Example input:
Sentence: The first twin , a female , had a left Potter-type IIa polycystic kidney and a rudimentary left uterine cornu .

Example answer:
{"entities": [{"text": "Potter-type IIa polycystic kidney", "type": "Disease"}, {"text": "rudimentary left uterine cornu", "type": "Disease"}]}

Example input:
Sentence: The second twin , a male , had some features of Potter 's facies , hypoplastic lungs , absent kidneys and ureters , and talipes equinovarus .

Example answer:
{"entities": [{"text": "Potter 's facies", "type": "Disease"}, {"text": "hypoplastic lungs", "type": "Disease"}, {"text": "absent kidneys and ureters", "type": "Disease"}, {"text": "talipes equinovarus", "type": "Disease"}]}

Example input:
Sentence: In the twin pregnancy , the mother had Crohn 's disease .

Example answer:
{"entities": [{"text": "Crohn 's disease", "type": "Disease"}]}

Example input:
Sentence: In the singleton pregnancy , the mother had ulcerative colitis , and the infant , a male , had coarctation of the aorta and a ventricular septal defect .

Example answer:
{"entities": [{"text": "ulcerative colitis", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "ventricular septal defect", "type": "Disease"}]}

Input:
Sentence: The second mother had a male infant by caesarean section .

## Item bc5cdr:test:175
Example input:
Sentence: We conclude that noxious stimulation of facial mucosa increases intracranial blood flow and lacrimation via a trigemino-parasympathetic reflex .

Example answer:
{"entities": []}

Example input:
Sentence: Application of a delayed feedback signal , in the form of a 2-h systemic corticosterone infusion in urethane-anesthetized rats with pharmacological blockade of glucocorticoid synthesis , is without effect on the resting secretion of arginine vasopressin and oxytocin at any corticosterone feedback dose tested .

Example answer:
{"entities": [{"text": "corticosterone", "type": "Chemical"}, {"text": "urethane-anesthetized", "type": "Chemical"}, {"text": "arginine vasopressin", "type": "Chemical"}, {"text": "oxytocin", "type": "Chemical"}]}

Example input:
Sentence: The primary response variable was based on central reading of 24 hour ambulatory electrocardiographic recordings and was defined as the occurrence of 30 or more single premature ventricular complexes in any two consecutive 30 minute blocks or one or more runs of two or more premature ventricular complexes in the entire 24 hour electrocardiographic recording .

Example answer:
{"entities": []}

Example input:
Sentence: Short-latency reflex responses were evoked in the masseter and temporalis muscles by a stretch device with different velocities and displacements before , during , and after the pain .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}]}

Example input:
Sentence: From these data we conclude that the penile pain following intracorporeal injections is most likely due to the acidity of the medication , which can be overcome by elevating the pH to a neutral level .

Example answer:
{"entities": [{"text": "penile pain", "type": "Disease"}]}

Example input:
Sentence: Suppression of irCRF secretion in response to nitroprusside-induced hypotension is observed and occurs at a plasma corticosterone level between 8-12 micrograms/dl .

Example answer:
{"entities": [{"text": "nitroprusside-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "corticosterone", "type": "Chemical"}]}

Example input:
Sentence: Intracavernous epinephrine : a minimally invasive treatment for priapism in the emergency department .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "priapism", "type": "Disease"}]}

Example input:
Sentence: Inhibition of immunoreactive corticotropin-releasing factor secretion into the hypophysial-portal circulation by delayed glucocorticoid feedback .

Example answer:
{"entities": []}

Example input:
Sentence: Intracerebroventricular ( i.c.v . )

Example answer:
{"entities": []}

Example input:
Sentence: Intracranial pressure ( ICP ) was measured during alfentanil-induced rigidity in rats .

Example answer:
{"entities": [{"text": "alfentanil-induced", "type": "Chemical"}, {"text": "rigidity", "type": "Disease"}]}

Input:
Sentence: The pressor response to the intracisternal ( i.c . )

## Item bc5cdr:test:140
Example input:
Sentence: Untreated group 3 rats exhibited a progressive reduction in GFR ( 0.35 +/- 0.08 ml/min at 4 months , 0.27 +/- 0.07 ml/min at 6 months ) .

Example answer:
{"entities": []}

Example input:
Sentence: In Group 1 the rats were trained under the influence of pentobarbital to run to the same shelf as in the normal state .

Example answer:
{"entities": [{"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: Rats were trained to approach a shelf where they received food reinforcement .

Example answer:
{"entities": []}

Example input:
Sentence: Thirty-two healthy young volunteers were randomly allocated to four different groups .

Example answer:
{"entities": []}

Example input:
Sentence: In female rats , only a weak tendency toward aggressiveness was found .

Example answer:
{"entities": [{"text": "aggressiveness", "type": "Disease"}]}

Example input:
Sentence: Rats treated with L-DOPA were allocated to two groups based on the presence or absence of LID .

Example answer:
{"entities": [{"text": "L-DOPA", "type": "Chemical"}, {"text": "LID", "type": "Disease"}]}

Example input:
Sentence: In 7 of the 18 rats , degeneration and myocyte vacuolisation were found .

Example answer:
{"entities": []}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Example input:
Sentence: In Group 2 the rats were trained to approach different shelves in different drug states .

Example answer:
{"entities": []}

Example input:
Sentence: Ten rats received saline as a control group .

Example answer:
{"entities": []}

Input:
Sentence: Ninety-three rats were randomly divided into three groups .

## Item bc5cdr:test:296
Example input:
Sentence: Maximum tolerated dose in good-risk patients was 70 mg/m2 , and in poor-risk patients , 60 mg/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: A starting dose of 1 mg/day with gradual , upward dose titration is recommended .

Example answer:
{"entities": []}

Example input:
Sentence: or theophylline ( 3 mg/kg i.v . ) .

Example answer:
{"entities": [{"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Example input:
Sentence: 5-HTP ( 5 mg/kg i.v . )

Example answer:
{"entities": [{"text": "5-HTP", "type": "Chemical"}]}

Example input:
Sentence: L-Dopa ( 5 mg/kg i.v . )

Example answer:
{"entities": [{"text": "L-Dopa", "type": "Chemical"}]}

Example input:
Sentence: Oral administration of CBZ as an aqueous suspension every 8 h at a dose of 250 mg/kg was continuously protective against HFDE-induced seizures and was minimally toxic as measured by weight gain over 8 weeks of treatment .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "HFDE-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: Two days before admission diltiazem ( 60 mg b.i.d . )

Example answer:
{"entities": [{"text": "diltiazem", "type": "Chemical"}]}

Example input:
Sentence: and then 100 mg b.i.d . )

Example answer:
{"entities": []}

Input:
Sentence: to 5 mg b.d .

## Item bc5cdr:test:297
Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: However , there was no significant difference in the lidocaine concentrations measured when the systolic blood pressure became 70 mmHg .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: On the other hand , BNP did not increase in the patients without heart failure given DNR , even at more than 700 mg/m ( 2 ) .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "DNR", "type": "Chemical"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: In the Ato + Dex group , SBP was increased from 113 +/- 2 to 119 +/- 2 mmHg on Days 4 to 14 , respectively ( P < 0.001 ) , but was significantly lower than SBP in the group treated with Dex alone ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: After 4-week administration of L-NAME , the systolic blood pressure ( SBP ) increased by 36 % .

Example answer:
{"entities": [{"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Input:
Sentence: at 4 weeks in patients with diastolic blood pressure greater than 90 mmHg and their further response was greater than those remaining on 2.5 mg b.d .

## Item bc5cdr:test:310
Example input:
Sentence: Severe distress was noted in the recovery phase in two patients .

Example answer:
{"entities": []}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: A comprehensive examination including her medical history , panoramic radiograph , and intraoral examination revealed 19 carious lesions , which is not very common for a healthy adult .

Example answer:
{"entities": [{"text": "carious lesions", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: METHODS : We conducted a retrospective review of 70 consecutive microvascular decompression operations and studied those patients who received topical papaverine for vasospasm .

Example answer:
{"entities": [{"text": "papaverine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Patients with stage D2-3 disease , abnormal hemoglobin level or renal and liver function tests that were higher than the upper limits were excluded from the study .

Example answer:
{"entities": []}

Example input:
Sentence: In both instances , suspicion of the presence of carcinoma was aroused by the palpation of a small nodule in the vaginal fornix .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}]}

Example input:
Sentence: The surgery and anaesthesia were uneventful , but 3 days after surgery , the patient reported an area of hypoaesthesia over L3-L4 dermatomes of the leg which had been operated on ( loss of pinprick sensation ) without reduction in muscular strength .

Example answer:
{"entities": [{"text": "loss of pinprick sensation", "type": "Disease"}]}

Example input:
Sentence: Decompression and neurolysis were performed with good subsequent recovery of function .

Example answer:
{"entities": []}

Input:
Sentence: A high index of suspicion may lead to a quick diagnostic procedure and successful decompressive surgery .

## Item bc5cdr:test:325
Example input:
Sentence: METHODS : a total of 13 patients were referred to the Danish Cholinesterase Research Unit after ECT during 38 months .

Example answer:
{"entities": []}

Example input:
Sentence: The area under the curve was 537 +/- 149 ng/ml x hours , volume of distribution ( Vd ) 3504 +/- 644 l/m2 , and total clearance ( ClT ) was 204 + 39.3 l/hour/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: It was administered by 15 min infusion to 16 evaluable patients with non-small cell lung cancer ( NSCLC ) ( 7 with no prior treatment , 9 patients in relapse following surgery/radiotherapy ) at a dose ( 648 mg/m2 divided over 3 days , repeated every 3 weeks ) determined by phase I trial .

Example answer:
{"entities": [{"text": "non-small cell lung cancer", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: Pain recall after one week was similarly precise ( magnitude : p < 0.01 , duration : p < 0.05 ) .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}]}

Example input:
Sentence: The t ( 1/2 , z ) of desipramine was longer when desipramine was coadministered with cinacalcet ( 21.0 versus 43.3 hs ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: After completion of the amifostine infusion , cisplatin 120 mg/m2 was administered over 30 minutes .

Example answer:
{"entities": [{"text": "amifostine", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: SigmaST , the sum of ST-segment elevations in 16 precordial leads , decreased ( P less than 0.02 ) with intravenous nitroglycerin .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}]}

Example input:
Sentence: The duration of the examination and the mean ejection fraction ( EF ) were 16.4+/-6.1 minutes and 60+/-9 % , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Pain intensity on a 0 to 10 numerical scale ; nausea and vomiting , drowsiness , confusion , and dry mouth , using a scale from 0 to 3 ( not at all , slight , a lot , awful ) ; Mini-Mental State Examination ( MMSE ) ( 0-30 ) ; and arterial pressure were recorded before administration of drugs ( T0 ) and after 30 minutes ( T30 ) , 60 minutes ( T60 ) , 120 minutes ( T120 ) , and 180 minutes ( T180 ) .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "confusion", "type": "Disease"}, {"text": "dry mouth", "type": "Disease"}]}

Input:
Sentence: ( ABSTRACT TRUNCATED AT 250 WORDS )

## Item bc5cdr:test:380
Example input:
Sentence: Mean follow-up on SRL therapy was 20 +/- 12 ( 6 to 43 ) months .

Example answer:
{"entities": [{"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Long-term follow-up of the patients was not possible .

Example answer:
{"entities": []}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: None of these well validated cases occurred within the first 10 days after treatment .

Example answer:
{"entities": []}

Example input:
Sentence: The median follow-up period was 14 months .

Example answer:
{"entities": []}

Example input:
Sentence: Patients were followed for 8-14 years .

Example answer:
{"entities": []}

Example input:
Sentence: They were followed up during and for 8 weeks after CT .

Example answer:
{"entities": []}

Example input:
Sentence: The follow-up period was 12 months .

Example answer:
{"entities": []}

Example input:
Sentence: Recurrence was studied in 82 evaluable patients after 1 year of follow-up and in 72 patients followed for 2-3 years ( mean 32 months ) .

Example answer:
{"entities": []}

Example input:
Sentence: In each patient who had abnormalities on the initial MR study , a follow-up MR study was performed 1 month later .

Example answer:
{"entities": []}

Input:
Sentence: A follow-up investigation was performed 10-12 months after study onset on the patients who had improved .

## Item bc5cdr:test:91
Example input:
Sentence: Methylergonovine was administered continuously at a rate of 10 micrograms/min up to 50 micrograms .

Example answer:
{"entities": [{"text": "Methylergonovine", "type": "Chemical"}]}

Example input:
Sentence: Median number of courses of MFL regimen given was six and the median cumulative dose of mitoxantrone was 68.35 mg/m2 .

Example answer:
{"entities": [{"text": "MFL regimen", "type": "Chemical"}, {"text": "mitoxantrone", "type": "Chemical"}]}

Example input:
Sentence: Maximum tolerated dose in good-risk patients was 70 mg/m2 , and in poor-risk patients , 60 mg/m2 .

Example answer:
{"entities": []}

Example input:
Sentence: In contrast , dosages of Mipafox ( less than or equal to 5 mg/kg ) which inhibited mean NTE activity in spinal cord less than or equal to 61 % and brain less than or equal to 60 % produced this degree of cord damage in only 9 % of the animals .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "cord damage", "type": "Disease"}]}

Example input:
Sentence: An initial dose of 0.1 microgram.kg-1.min-1 of PGE1 ( 15 patients ) , or 10 micrograms.kg-1.min-1 of TMP ( 15 patients ) was administered intravenously after the dural opening and the dose was adjusted to maintain the mean arterial blood pressure ( MAP ) at about 60 mmHg .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}]}

Example input:
Sentence: Total cumulative doses were 36 or 60 g/m2 of ifosfamide ( six or 10 cycles of ifosfamide , vincristine , and dactinomycin [ IVA ] ) .

Example answer:
{"entities": [{"text": "ifosfamide", "type": "Chemical"}, {"text": "ifosfamide , vincristine , and dactinomycin", "type": "Chemical"}, {"text": "IVA", "type": "Chemical"}]}

Example input:
Sentence: The median dose-intensity ( DI ) was 20 mg/m2/wk .

Example answer:
{"entities": []}

Example input:
Sentence: A dose of 50 mg/kg is recommended in those without audiogram abnormalities .

Example answer:
{"entities": []}

Example input:
Sentence: Doses were flexibly titrated up to 0.6 mg/day for clonidine and 60 mg/day for methylphenidate ( both with divided dosing ) .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}, {"text": "methylphenidate", "type": "Chemical"}]}

Example input:
Sentence: This agent was well tolerated in healthy volunteers at doses up to 100 micrograms/kg/min .

Example answer:
{"entities": []}

Input:
Sentence: A mean overall dose of etomidate 17.4 microgram/kg/min .

## Item bc5cdr:test:97
Example input:
Sentence: Tremor side effects of salbutamol , quantified by a laser pointer technique .

Example answer:
{"entities": [{"text": "Tremor", "type": "Disease"}, {"text": "salbutamol", "type": "Chemical"}]}

Example input:
Sentence: Support of the arm decreased tremor severity , exhaustion increased tremor severity significantly .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Postural tremor showed no significant difference between the first and third session ( P = 0.07 ) .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: There was no agreement between the questionnaire and tremor severity ( r = 0.093 ; P = 0.53 ) .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Tremor was measured simultaneously by two independent observers .

Example answer:
{"entities": [{"text": "Tremor", "type": "Disease"}]}

Example input:
Sentence: In another series of measurements , reproducibility and reference values of the tremor was assessed in 65 healthy subjects in three sessions , at 9 a.m. , 4 p.m. and 9 a.m. , respectively , 1 week later .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Postural tremor was measured with the arm horizontally outstretched rest tremor with the arm supported by an armrest and finally tremor was measured after holding a 2-kg weight until exhaustion .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: DISCUSSION : Quantifying tremor by using an inexpensive laser pointer is , with the exception of children ( < 12 years ) a sensitive and reproducible method .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: METHODS : Tremor was measured using a laser pointer technique .

Example answer:
{"entities": [{"text": "Tremor", "type": "Disease"}]}

Input:
Sentence: A method permitting measurement of finger tremor as a displacement-time curve is described , using a test system with simple amplitude calibration .

## Item bc5cdr:test:102
Example input:
Sentence: Since 18 of the 22 patients were initially receiving deferoxamine doses in excess of the commonly recommended 50 mg/kg per dose , therapy was restarted with lower doses , usually 50 mg/kg per dose or less depending on the degree of auditory abnormality , and with the exception of two cases no further toxicity was demonstrated .

Example answer:
{"entities": [{"text": "deferoxamine", "type": "Chemical"}, {"text": "auditory abnormality", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: GR 55562 ( 0.1-10 microg/side ) , administered intra-accumbens shell prior to cocaine , dose-dependently attenuated the psychostimulant-induced locomotor hyperactivity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: In another series of measurements , reproducibility and reference values of the tremor was assessed in 65 healthy subjects in three sessions , at 9 a.m. , 4 p.m. and 9 a.m. , respectively , 1 week later .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Those dosages ( greater than or equal to 10 mg/kg ) that inhibited mean NTE activity in the spinal cord greater than or equal to 73 % and brain greater than or equal to 67 % of control values produced severe ( greater than or equal to 3 ) cervical cord pathology in 85 % of the rats .

Example answer:
{"entities": []}

Example input:
Sentence: Support of the arm decreased tremor severity , exhaustion increased tremor severity significantly .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: To determine sensitivity we assessed tremor in 44 patients with obstructive lung disease after administration of cumulative doses of salbutamol .

Example answer:
{"entities": [{"text": "tremor", "type": "Disease"}, {"text": "obstructive lung disease", "type": "Disease"}, {"text": "salbutamol", "type": "Chemical"}]}

Example input:
Sentence: 4-DAMP inhibited the tonic contractions in controls more potently than methoctramine and pirenzepine .

Example answer:
{"entities": [{"text": "4-DAMP", "type": "Chemical"}, {"text": "methoctramine", "type": "Chemical"}, {"text": "pirenzepine", "type": "Chemical"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Salbutamol significantly increased tremor severity in patients in a dose-dependent way .

Example answer:
{"entities": [{"text": "Salbutamol", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Input:
Sentence: At therapeutic doses both substances raised the mean tremor amplitude to about three times the control level .

## Item bc5cdr:test:148
Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: A warfarin-drug interaction could have contributed to the haemorrhage in 24 ( 41 % ) of the warfarin patients and in 7 of these ( 12 % ) the bleeding complication was considered being possible to avoid .

Example answer:
{"entities": [{"text": "warfarin-drug", "type": "Chemical"}, {"text": "haemorrhage", "type": "Disease"}, {"text": "warfarin", "type": "Chemical"}, {"text": "bleeding", "type": "Disease"}]}

Example input:
Sentence: We present the case of a 28-year-old man on chronic warfarin therapy who sustained a minor muscle tear and developed increasing pain and a flexure contracture of the right hip .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "muscle tear", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "contracture", "type": "Disease"}]}

Example input:
Sentence: Warfarin-induced iliopsoas hemorrhage with subsequent femoral nerve palsy .

Example answer:
{"entities": [{"text": "Warfarin-induced", "type": "Chemical"}, {"text": "hemorrhage", "type": "Disease"}, {"text": "femoral nerve palsy", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Warfarin-induced cerebral haemorrhages are a major clinical problem with a high fatality rate .

Example answer:
{"entities": [{"text": "Warfarin-induced", "type": "Chemical"}, {"text": "cerebral haemorrhages", "type": "Disease"}]}

Example input:
Sentence: Pregnant rats were administered one of these calcium channel blockers during the period of cardiac morphogenesis and the offspring examined on day 20 of gestation for cardiovascular malformations .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reassuringly , penicillins , erythromycins , and cephalosporins , although used commonly by pregnant women , were not associated with many birth defects .

Example answer:
{"entities": [{"text": "penicillins", "type": "Chemical"}, {"text": "erythromycins", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Treatment for 2 weeks with Warfarin caused massive focal calcification of the artery media in 20-day-old rats and less extensive focal calcification in 42-day-old rats .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcification of the artery", "type": "Disease"}, {"text": "calcification", "type": "Disease"}]}

Input:
Sentence: Fetal risks due to warfarin therapy during pregnancy .

## Item bc5cdr:test:190
Example input:
Sentence: Both the trigeminal and the cranial parasympathetic systems may be involved in mediating these dysfunctions .

Example answer:
{"entities": []}

Example input:
Sentence: They suggest that , in normal conscious rats , the central tachycardia of bromocriptine appears to predominate and to mask the bradycardia of this agonist at peripheral dopamine D2 receptors .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: Based on these data , it can be postulated that ( +/- ) -PG-9 exerted an antinociceptive effect mediated by a central potentiation of cholinergic transmission .

Example answer:
{"entities": [{"text": ")", "type": "Chemical"}]}

Example input:
Sentence: Removal of the carotid sinuses caused an elevation blood pressure and heart rate and abolished the negative chronotropic effect of norepinephrine .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: The mode of action was said to be comparable to that of the synthetic compound 'carbamylcholin ' ; that is , carbachol .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: INTRODUCTION : Intoxications with carbachol , a muscarinic cholinergic receptor agonist are rare .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , the effects are mediated through dopamine rather than norepinephrine and do not require the carotid sinus baroreceptors .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "isoprenaline-induced", "type": "Chemical"}]}

Input:
Sentence: carbachol ortral and peripheral adrenergic mechanisms , and that the sympathetic trunk is the main pathway .

## Item bc5cdr:test:113
Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: The development of tolerance to the muscular rigidity produced by morphine was studied in rats .

Example answer:
{"entities": [{"text": "muscular rigidity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Progressive improvement occurred in 7 cases after commencement of prednisolone and methotrexate , and in one case spontaneously .

Example answer:
{"entities": [{"text": "prednisolone", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: The pathophysiology of painful temporomandibular disorders is not fully understood , but evidence suggests that muscle pain modulates motor function in characteristic ways .

Example answer:
{"entities": [{"text": "temporomandibular disorders", "type": "Disease"}, {"text": "muscle pain", "type": "Disease"}]}

Example input:
Sentence: What is less well known is a phenomenon whereby statins may induce a myopathy , which persists or may progress after stopping the drug .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "myopathy", "type": "Disease"}]}

Example input:
Sentence: There is evidence that growth hormone may be related to the progression of weakness in Duchenne dystrophy .

Example answer:
{"entities": [{"text": "weakness", "type": "Disease"}, {"text": "Duchenne dystrophy", "type": "Disease"}]}

Example input:
Sentence: In contrast , monkeys with long-term MPTP exposure , slow symptom progression and/or long symptom duration prior to initiation of levodopa therapy were more resistant to developing LIDs ( e.g. , dyskinesia developed no sooner than 146 days of chronic levodopa administration ) .

Example answer:
{"entities": [{"text": "MPTP", "type": "Chemical"}, {"text": "levodopa", "type": "Chemical"}, {"text": "LIDs", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: The mechanism of this myopathy is uncertain but may involve the induction by statins of an endoplasmic reticulum stress response with associated up-regulation of MHC-I expression and antigen presentation by muscle fibres .

Example answer:
{"entities": [{"text": "myopathy", "type": "Disease"}, {"text": "statins", "type": "Chemical"}]}

Example input:
Sentence: Rhabdomyolysis is a potentially lethal syndrome that psychiatric patients seem predisposed to develop .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "Disease"}, {"text": "psychiatric", "type": "Disease"}]}

Example input:
Sentence: Progressive myopathy with up-regulation of MHC-I associated with statin therapy .

Example answer:
{"entities": [{"text": "myopathy", "type": "Disease"}, {"text": "statin", "type": "Chemical"}]}

Input:
Sentence: We are still a long way from discovering an unequivocal pathogenetic interpretation of progressive muscular dystrophy in man .

## Item bc5cdr:test:183
Example input:
Sentence: The first case involved a 59-year-old man who used Dormex , which contains hydrogen cyanamide , without protection after consuming a large amount of alcohol during a meal .

Example answer:
{"entities": [{"text": "Dormex", "type": "Chemical"}, {"text": "hydrogen cyanamide", "type": "Chemical"}, {"text": "alcohol", "type": "Chemical"}]}

Example input:
Sentence: Serum samples from the first and second days contained 3.6 and 1.9 mg/l carbachol , respectively .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: The analysed carbachol concentration exceeded the supposed serum level resulting from a therapeutic dose by a factor of 130 to 260 .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "isoprenaline-induced", "type": "Chemical"}]}

Example input:
Sentence: Case report : acute unintentional carbachol intoxication .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: He bought 25 g of carbachol as pure substance in a pharmacy , and the father was administered 400 to 500 mg. Carbachol concentrations in serum and urine on day 1 and 2 of hospital admission were analysed by HPLC-mass spectrometry .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "Carbachol", "type": "Chemical"}]}

Example input:
Sentence: The mode of action was said to be comparable to that of the synthetic compound 'carbamylcholin ' ; that is , carbachol .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: INTRODUCTION : Intoxications with carbachol , a muscarinic cholinergic receptor agonist are rare .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Input:
Sentence: carbachol ( 1 mug ) was almost completely blocked by i.c .

## Item bc5cdr:test:176
Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: Two separate equimolar doses ( 0.2 and 0.4 mumol ) of either cocaine or BE were injected ventricularly in unanesthetized juvenile rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "BE", "type": "Chemical"}]}

Example input:
Sentence: injection of methyl beta-carboline-3-carboxylate ( beta-CCM ) , an inverse agonist of the GABA ( A ) receptor benzodiazepine site .

Example answer:
{"entities": [{"text": "methyl beta-carboline-3-carboxylate", "type": "Chemical"}, {"text": "beta-CCM", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}, {"text": "benzodiazepine", "type": "Chemical"}]}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: The mode of action was said to be comparable to that of the synthetic compound 'carbamylcholin ' ; that is , carbachol .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: While contractions to carbachol and ATP were the same in inflamed and in control strips when related to a reference potassium response , isoprenaline-induced relaxations were smaller in inflamed strips .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}, {"text": "potassium", "type": "Chemical"}, {"text": "isoprenaline-induced", "type": "Chemical"}]}

Example input:
Sentence: The analysed carbachol concentration exceeded the supposed serum level resulting from a therapeutic dose by a factor of 130 to 260 .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: He bought 25 g of carbachol as pure substance in a pharmacy , and the father was administered 400 to 500 mg. Carbachol concentrations in serum and urine on day 1 and 2 of hospital admission were analysed by HPLC-mass spectrometry .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}, {"text": "Carbachol", "type": "Chemical"}]}

Example input:
Sentence: INTRODUCTION : Intoxications with carbachol , a muscarinic cholinergic receptor agonist are rare .

Example answer:
{"entities": [{"text": "carbachol", "type": "Chemical"}]}

Input:
Sentence: injection of carbachol ( 1 mug ) in anesthetized rats was analyzed .

## Item bc5cdr:test:155
Example input:
Sentence: Pregnant rats were administered one of these calcium channel blockers during the period of cardiac morphogenesis and the offspring examined on day 20 of gestation for cardiovascular malformations .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "cardiovascular malformations", "type": "Disease"}]}

Example input:
Sentence: Postoperatively , the patient refused DC cardioversion and was treated medically .

Example answer:
{"entities": []}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: After delivery of the infant , there should be no contraindication to the use of an alpha-adrenergic vasopressor such as phenylephrine to treat hypotensive patients with tachycardia .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotensive", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Among women who used oral contraceptives , the odds ratio was 2.1 ( 95 percent confidence interval , 1.5 to 3.0 ) for those without a prothrombotic mutation and 1.9 ( 95 percent confidence interval , 0.6 to 5.5 ) for those with a mutation CONCLUSIONS : The risk of myocardial infarction was increased among women who used second-generation oral contraceptives .

Example answer:
{"entities": [{"text": "oral contraceptives", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Within 8 hours after initiation of therapy the patient died with a clinical picture resembling massive pulmonary obstruction due to choriocarcinomic tissue plugs , probably originating from the uterus .

Example answer:
{"entities": [{"text": "pulmonary obstruction", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Reassuringly , penicillins , erythromycins , and cephalosporins , although used commonly by pregnant women , were not associated with many birth defects .

Example answer:
{"entities": [{"text": "penicillins", "type": "Chemical"}, {"text": "erythromycins", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The risk of myocardial infarction was similar among women who used oral contraceptives whether or not they had a prothrombotic mutation .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptives", "type": "Chemical"}]}

Input:
Sentence: In view of the risks to both mother and fetus in women with prosthetic cardiac valves it is recommended that therapeutic abortion be advised as the first alternative .

## Item bc5cdr:test:219
Example input:
Sentence: Patients with renal insufficiency should not be given this regimen .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: We propose that amphotericin , in the setting of reduced effective arterial volume , may activate tubuloglomerular feedback , thereby contributing to acute renal failure .

Example answer:
{"entities": [{"text": "amphotericin", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: We report a case of ranitidine-induced acute interstitial nephritis in a recipient of a cadaveric renal allograft presenting with acute allograft dysfunction within 48 hours of exposure to the drug .

Example answer:
{"entities": [{"text": "ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: Reversibility of captopril-induced renal insufficiency after prolonged use in an unusual case of renovascular hypertension .

Example answer:
{"entities": [{"text": "captopril-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: We have reported a case of acute oliguric renal failure with hyperkalemia in a patient with cirrhosis , ascites , and cor pulmonale after indomethacin therapy .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "cor pulmonale", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: Spironolactone-induced renal insufficiency and hyperkalemia in patients with heart failure .

Example answer:
{"entities": [{"text": "Spironolactone-induced", "type": "Chemical"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Spironolactone-induced hyperkalemia and renal insufficiency are more common in our clinical experience than reported previously .

Example answer:
{"entities": [{"text": "Spironolactone-induced", "type": "Chemical"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Input:
Sentence: Due to an accidental malfunctioning of the infusion pump , the patient was inadvertently administered a toxic dosage of the drug which caused renal insufficiency .

## Item bc5cdr:test:262
Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Patients who developed hyperkalemia were older and more likely to have diabetes , had higher baseline serum potassium levels and lower baseline potassium supplement doses , and were more likely to be treated with beta-blockers than controls ( n = 134 ) .

Example answer:
{"entities": [{"text": "hyperkalemia", "type": "Disease"}, {"text": "diabetes", "type": "Disease"}, {"text": "potassium", "type": "Chemical"}]}

Example input:
Sentence: The rise in blood pressure became less marked when higher concentrations of sevoflurane or enflurane were administered and the blood pressure at convulsions decreased significantly in 1.6 % sevoflurane , and in 0.8 % and 1.6 % enflurane .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "Chemical"}, {"text": "enflurane", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: They are thus more important during absolute hypovolemia than during deliberate hypotension .

Example answer:
{"entities": [{"text": "hypovolemia", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: During HEM-induced hypotension the cardiac output was significantly lower and systemic vascular resistance higher compared with that in the SNP group .

Example answer:
{"entities": [{"text": "HEM-induced", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: There was a significant increase in CBF , although CMRO2 was unchanged , compared with pre-hypotensive values .

Example answer:
{"entities": []}

Example input:
Sentence: The systolic pressure variation ( SPV ) , which is the difference between the maximal and minimal values of the systolic blood pressure ( SBP ) after one positive-pressure breath , was studied in ventilated dogs subjected to hypotension .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Systolic pressure variation is greater during hemorrhage than during sodium nitroprusside-induced hypotension in ventilated dogs .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "sodium", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: It is concluded that increases in the SPV and the delta down are characteristic of a hypotensive state due to a predominant decrease in preload .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Input:
Sentence: Baseline blood pressures were higher in fluctuating patients ; a higher baseline blood pressure correlated with greater hypotensive effects .

## Item bc5cdr:test:274
Example input:
Sentence: The increase in dP/dtejc during infusion of dobutamine in this group was severely impaired as compared to the non-ischemic group .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: The data indicate that audiovisual toxicity is not an infrequent complication in hemodialyzed patients receiving desferrioxamine .

Example answer:
{"entities": [{"text": "audiovisual toxicity", "type": "Disease"}, {"text": "desferrioxamine", "type": "Chemical"}]}

Example input:
Sentence: Because treatments for heart failure have changed since the benefits of spironolactone were reported , the prevalence of these complications may differ in current clinical practice .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "spironolactone", "type": "Chemical"}]}

Example input:
Sentence: The overall incidence of side effects and the frequency and severity of blurred vision , dry mouth , and drowsiness were significantly less with dothiepin than with amitriptyline .

Example answer:
{"entities": [{"text": "blurred vision", "type": "Disease"}, {"text": "dry mouth", "type": "Disease"}, {"text": "dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Long-term use and concomitant use of more than one BZD/RD were common in elderly patients hospitalised because of acute illnesses .

Example answer:
{"entities": []}

Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin is an effective anticancer chemotherapeutic agent known to cause acute and chronic cardiomyopathy .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Dothiepin thus was found to be an effective antidepressant drug associated with fewer side effects than amitriptyline in the treatment of depressed outpatients .

Example answer:
{"entities": [{"text": "Dothiepin", "type": "Chemical"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: Delirium was inconsistently recognized clinically in milder cases and was associated with increased length-of-stay and higher costs , and inferior clinical outcome .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: Dothiepin and amitriptyline were equally effective in alleviating the symptoms of depressive illness , and both were significantly superior to placebo .

Example answer:
{"entities": [{"text": "Dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressive illness", "type": "Disease"}]}

Input:
Sentence: Despite extensive clinical experience the role of digoxin is still not well defined .

## Item bc5cdr:test:266
Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: A lesser degree of orthostatic hypotension occurred with standing .

Example answer:
{"entities": [{"text": "orthostatic hypotension", "type": "Disease"}]}

Example input:
Sentence: They are thus more important during absolute hypovolemia than during deliberate hypotension .

Example answer:
{"entities": [{"text": "hypovolemia", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: There was a significant increase in CBF , although CMRO2 was unchanged , compared with pre-hypotensive values .

Example answer:
{"entities": []}

Example input:
Sentence: During these two episodes , his blood pressure diminished but no severe hypotension was noted .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Systolic pressure variation is greater during hemorrhage than during sodium nitroprusside-induced hypotension in ventilated dogs .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "sodium", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: During HEM-induced hypotension the cardiac output was significantly lower and systemic vascular resistance higher compared with that in the SNP group .

Example answer:
{"entities": [{"text": "HEM-induced", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: It is concluded that increases in the SPV and the delta down are characteristic of a hypotensive state due to a predominant decrease in preload .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Input:
Sentence: The hypotensive effect appears to be related to the higher baseline blood pressure we observed in fluctuating patients relative to stable patients .

## Item bc5cdr:test:289
Example input:
Sentence: RESULTS : Two hundred sixty-five patients were included in this analysis ( n=92 , 93 , and 80 for placebo , low dose , and high dose , respectively ) .

Example answer:
{"entities": []}

Example input:
Sentence: Only 2 patients of our retrospective study experienced a mild or severe neutropenia .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}]}

Example input:
Sentence: The results showed a high prevalence of depression in both groups of patients , with no preponderance in the hypertensive group .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: RESULT ( S ) : A 36-year-old Chinese woman developed central retinal vein occlusion after eight courses of CC .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: Anaphylaxis was seen in 37 patients ( 69 % ) , the other 17 ( 31 % ) having urticaria and/or angioedema .

Example answer:
{"entities": [{"text": "Anaphylaxis", "type": "Disease"}, {"text": "urticaria", "type": "Disease"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: Mild hypoxia ( SO2 < 90 % ) was the most common event ( 11 patients ) ; 3 patients ( 2 % ) presented transient hypoxia due to upper airway obstruction by probe introduction and 8 ( 5.8 % ) due to hypoxia caused by MZ use .

Example answer:
{"entities": [{"text": "hypoxia", "type": "Disease"}, {"text": "airway obstruction", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: In 8 patients the diagnosis of primary pulmonary hypertension was uncertain , 5 of them had taken appetite suppressants .

Example answer:
{"entities": [{"text": "primary pulmonary hypertension", "type": "Disease"}, {"text": "appetite suppressants", "type": "Chemical"}]}

Example input:
Sentence: Eighty-nine new referral hypertensive out-patients and 46 new referral non-hypertensive chronically physically ill out-patients completed a mood rating scale at regular intervals for one year .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Thirty-five patients with primary pulmonary hypertension and 85 matched controls were recruited over 32 months ( 1992-1994 ) in Belgium .

Example answer:
{"entities": [{"text": "primary pulmonary hypertension", "type": "Disease"}]}

Input:
Sentence: 303 Chinese patients with mild to moderate hypertension entered the study .

## Item bc5cdr:test:251
Example input:
Sentence: To clarify the effects of bromocriptine on prolactinoma cells in vivo , immunohistochemical , ultrastructural and morphometrical analyses were applied to estrogen-induced rat prolactinoma cells 1 h and 6 h after injection of bromocriptine ( 3 mg/kg of body weight ) .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "prolactinoma", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Bromocriptine was definitely effective in cases with prolactin greater than 35 ng./ml .

Example answer:
{"entities": [{"text": "Bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: They suggest that , in normal conscious rats , the central tachycardia of bromocriptine appears to predominate and to mask the bradycardia of this agonist at peripheral dopamine D2 receptors .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: In control rats , intravenous bromocriptine ( 150 microg/kg ) induced significant hypotension and tachycardia .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: Although generally regarded as `` safe , '' possible serious cardiac effects of bromocriptine should be acknowledged .

## Item bc5cdr:test:332
Example input:
Sentence: Permeability of the blood-brain barrier was quantitated by clearance of fluorescent-labeled dextran before and during phenylephrine-induced acute hypertension in rats treated with vehicle and Hoe-140 ( 0.1 microM ) .

Example answer:
{"entities": [{"text": "dextran", "type": "Chemical"}, {"text": "phenylephrine-induced", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "Hoe-140", "type": "Chemical"}]}

Example input:
Sentence: Removal of the carotid sinuses caused an elevation blood pressure and heart rate and abolished the negative chronotropic effect of norepinephrine .

Example answer:
{"entities": [{"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: They suggest that , in normal conscious rats , the central tachycardia of bromocriptine appears to predominate and to mask the bradycardia of this agonist at peripheral dopamine D2 receptors .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: It has been shown that bromocriptine-induced tachycardia , which persisted after adrenalectomy , is ( i ) mediated by central dopamine D2 receptor activation and ( ii ) reduced by 5-day isoproterenol pretreatment , supporting therefore the hypothesis that this effect is dependent on sympathetic outflow to the heart .

Example answer:
{"entities": [{"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: An experimental model was developed in the rat to measure changes in lacrimation and intracranial blood flow following noxious chemical stimulation of facial mucosa .

Example answer:
{"entities": []}

Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: Blood pressure response to chronic low-dose intrarenal noradrenaline infusion in conscious rats .

Example answer:
{"entities": [{"text": "noradrenaline", "type": "Chemical"}]}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Example input:
Sentence: Noxious chemical stimulation of rat facial mucosa increases intracranial blood flow through a trigemino-parasympathetic reflex -- an experimental model for vascular dysfunctions in cluster headache .

Example answer:
{"entities": [{"text": "vascular dysfunctions", "type": "Disease"}, {"text": "cluster headache", "type": "Disease"}]}

Example input:
Sentence: These findings indicate that in spontaneously hypertensive rats the effects of central alpha-adrenoceptor stimulation involve activation of opiate receptors .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}]}

Input:
Sentence: We studied the effects of chronic selective neuronal lesion of rostral ventrolateral medulla on mean arterial pressure , heart rate , and neurogenic tone in conscious , unrestrained spontaneously hypertensive rats .

## Item bc5cdr:test:225
Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: Every patient was screened for testosterone and 451 were screened for prolactin on the basis of low sexual desire , gynecomastia or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}]}

Example input:
Sentence: Prolactin exceeded 20 ng./ml .

Example answer:
{"entities": []}

Example input:
Sentence: ( 8 of 12 compared to only 9 of 22 cases with prolactin between 20 and 35 ng./ml . ) .

Example answer:
{"entities": []}

Example input:
Sentence: Endocrine therapy consisted of testosterone heptylate or human chorionic gonadotropin for hypogonadism and bromocriptine for hyperprolactinemia .

Example answer:
{"entities": [{"text": "testosterone heptylate", "type": "Chemical"}, {"text": "hypogonadism", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "hyperprolactinemia", "type": "Disease"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: Chronic hyperprolactinemia induced by the dopamine antagonist sulpiride caused a 40 % reduction LH pulse frequency in ovariectomized rats , but only in the presence of chronic low levels of estradiol .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}, {"text": "sulpiride", "type": "Chemical"}, {"text": "estradiol", "type": "Chemical"}]}

Example input:
Sentence: Bromocriptine was definitely effective in cases with prolactin greater than 35 ng./ml .

Example answer:
{"entities": [{"text": "Bromocriptine", "type": "Chemical"}]}

Example input:
Sentence: Hyperprolactinemia can reduce fertility and libido .

Example answer:
{"entities": [{"text": "Hyperprolactinemia", "type": "Disease"}]}

Input:
Sentence: Daily dosages of 5-10 mg corrected the hyperprolactinemia and restored menstruation in four of the six patients .

## Item bc5cdr:test:288
Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: The mean duration of action was 3.8 hours with ipratropium and 2.4 hours with theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: METHOD : In London and Toronto 154 patients who met DSM-III criteria for panic disorder with agoraphobia were randomised to alprazolam or placebo .

Example answer:
{"entities": [{"text": "panic disorder", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}, {"text": "alprazolam", "type": "Chemical"}]}

Example input:
Sentence: Five hundred fifty-three patients , 264 taking the lozenge and 289 taking the gum , used the study product for > or =4 days per week during the first 2 weeks ( evaluable population ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Ophthalmologists at 15 institutions responded , reporting a total of 3,774 indocyanine green angiograms performed on 2,820 patients between June 1984 and September 1992 .

Example answer:
{"entities": [{"text": "indocyanine green", "type": "Chemical"}]}

Example input:
Sentence: For the cytoprotection study , animals were orally gavaged 100 mg/Kg GSPE for 7-10 days followed by i.p .

Example answer:
{"entities": [{"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: In a 6-week double-blind parallel treatment study , dothiepin and amitriptyline were compared to placebo in the treatment of 33 depressed outpatients .

Example answer:
{"entities": [{"text": "dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: The open study lasted for four weeks ; the drug was administrated in the form of 1 mg tablets .

Example answer:
{"entities": []}

Input:
Sentence: A 6-week open study of the introduction of isradipine treatment was conducted in general practice in Hong Kong .

## Item bc5cdr:test:396
Example input:
Sentence: Discontinuance of effective chemotherapy in this patient during partial remission resulted in fatal disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: In two patients , the arrhythmia degenerated into irreversible ventricular fibrillation and both patients died .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Fatal myeloencephalopathy due to accidental intrathecal vincristin administration : a report of two cases .

Example answer:
{"entities": [{"text": "myeloencephalopathy", "type": "Disease"}, {"text": "vincristin", "type": "Chemical"}]}

Example input:
Sentence: An analysis of the 75 cases that had been adequately followed up suggested that 16 , including three deaths , were probably related to treatment with the drug .

Example answer:
{"entities": [{"text": "deaths", "type": "Disease"}]}

Example input:
Sentence: The leading causes of death were pneumonia and bronchitis ( 44.1 % ) , malignant neoplasms ( 11.6 % ) , heart diseases ( 4.1 % ) , cerebral infarction ( 3.7 % ) and septicaemia ( 3.3 % ) .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}, {"text": "pneumonia", "type": "Disease"}, {"text": "bronchitis", "type": "Disease"}, {"text": "neoplasms", "type": "Disease"}, {"text": "heart diseases", "type": "Disease"}, {"text": "cerebral infarction", "type": "Disease"}, {"text": "septicaemia", "type": "Disease"}]}

Example input:
Sentence: The first patient died without a diagnosis ; the second patient had a dramatic recovery following the administration of vitamin B6 .

Example answer:
{"entities": [{"text": "vitamin B6", "type": "Chemical"}]}

Example input:
Sentence: This was followed by ventricular fibrillation in one patient and sudden death in another .

Example answer:
{"entities": [{"text": "ventricular fibrillation", "type": "Disease"}, {"text": "sudden death", "type": "Disease"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Eight patients were dead in the last follow-up ; two of them died of treatment-related toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Of the 59 cases , 26 ( 44 % ) had a fatal outcome , compared to 136 ( 25 % ) among the non-warfarin patients ( p < 0.01 ) .

Example answer:
{"entities": []}

Input:
Sentence: Two cases had a fatal outcome and one resulted in severe sequelae .

## Item bc5cdr:test:349
Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: We concluded a critical time window for systemic lipopolysaccharide pretreatment in exerting effective protection against methamphetamine-induced nigrostriatal dopamine neurotoxicity .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: The extent of silver-stained CA3 and CA1 hippocampal neurons was evaluated 2 days after SE .

Example answer:
{"entities": [{"text": "silver-stained", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Previous studies have indicated that the globus pallidus receives neurotensinergic innervation from the striatum , and systemic administration of a neurotensin analog could produce antiparkinsonian effects .

Example answer:
{"entities": [{"text": "neurotensin", "type": "Chemical"}]}

Example input:
Sentence: Immunohistochemical studies with antibodies to neurofilament proteins on axonal damage in experimental focal lesions in rat .

Example answer:
{"entities": [{"text": "axonal damage", "type": "Disease"}]}

Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Immunohistochemistry with monoclonal antibodies against neurofilament ( NF ) proteins of middle and high molecular weight class , NF-M and NF-H , was used to study axonal injury in the borderzone of focal lesions in rats .

Example answer:
{"entities": [{"text": "axonal injury", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Immunofluorescence staining with the MRP2 antibody was found to label a high number of microvessels throughout the brain in normal Wistar rats , whereas such labeling was absent in TR ( - ) rats .

Example answer:
{"entities": []}

Input:
Sentence: Nissl-staining and antibodies against the neuron-specific calcium-binding protein , parvalbumin , served to detect neuronal damage in SNR .

## Item bc5cdr:test:356
Example input:
Sentence: Five hours after exposure , he developed disulfiram-like syndrome with flushing , tachycardia , and arterial hypotension after consuming three glasses of wine .

Example answer:
{"entities": [{"text": "disulfiram-like", "type": "Chemical"}, {"text": "flushing", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "arterial hypotension", "type": "Disease"}]}

Example input:
Sentence: Following discontinuation of SNP , blood pressure in the control animals rebounded to 94 torr , as compared with 78 torr in the saralasin-treated rats .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}, {"text": "saralasin-treated", "type": "Chemical"}]}

Example input:
Sentence: Flow and metabolism were measured 5-13 days after the subarachnoid haemorrhage by a modification of the classical Kety-Schmidt technique using xenon-133 i.v .

Example answer:
{"entities": [{"text": "subarachnoid haemorrhage", "type": "Disease"}, {"text": "xenon-133", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: The SPV during hypotension was 15.7 +/- 6.7 mm Hg in the HEM group , compared with 9.1 +/- 2.0 mm Hg in the SNP group ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: The aorta/serum-ratio and the radioactive build-up 24 and 48 hours after injection of 131I-HSA was reduced in animals treated with D-pen for 42 days , indicating an impeded transmural transport of tracer which may be caused by a steric exclusion effect of abundant hyaluronate .

Example answer:
{"entities": [{"text": "D-pen", "type": "Chemical"}, {"text": "hyaluronate", "type": "Chemical"}]}

Example input:
Sentence: During the SNP infusion the control animals demonstrated a progressive increase in blood pressure to 61 torr , whereas the saralasin-treated animals showed no change .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}, {"text": "increase in blood pressure", "type": "Disease"}, {"text": "saralasin-treated", "type": "Chemical"}]}

Example input:
Sentence: In each group , SNP infusion resulted in an initial decrease in blood pressure from 86 torr and 83 torr , respectively , to 48 torr .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Input:
Sentence: By 6 h , vasogenic edema covered the lesioned SNR .

## Item bc5cdr:test:406
Example input:
Sentence: The majority of patients ( > 60 % ) experienced no change in their disease status from baseline .

Example answer:
{"entities": []}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Eleven patients progressed during therapy .

Example answer:
{"entities": []}

Example input:
Sentence: The symptoms occurred around 2 weeks after starting clozapine in an inpatient setting .

Example answer:
{"entities": [{"text": "clozapine", "type": "Chemical"}]}

Example input:
Sentence: Organic mental disorder was observed in a 29-year-old female in the prognostic period after the onset of carmofur-induced leukoencephalopathy .

Example answer:
{"entities": [{"text": "Organic mental disorder", "type": "Disease"}, {"text": "carmofur-induced", "type": "Chemical"}, {"text": "leukoencephalopathy", "type": "Disease"}]}

Example input:
Sentence: He was awake , revealed no changes of mental status and at rest there were no further motor symptoms .

Example answer:
{"entities": []}

Example input:
Sentence: Following the initial period of therapy , emerging difficulties require a reassessment of therapeutic approaches , such as dosage adjustment or introduction of a dopamine agonist .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: None of these well validated cases occurred within the first 10 days after treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Illness occurred within 1 -- 9 weeks of commencement of therapy in 9 patients , the remaining 3 patients having received the drug for 13 months , 15 months and 7 years before experiencing symptoms .

Example answer:
{"entities": []}

Input:
Sentence: The patient 's change in mental status was first reported nine days after the initiation of therapy .

## Item bc5cdr:test:419
Example input:
Sentence: Trifluoroacetyl-adducted proteins were detected in surviving hepatocytes .

Example answer:
{"entities": [{"text": "Trifluoroacetyl-adducted", "type": "Chemical"}]}

Example input:
Sentence: Tissue lipid peroxidation was measured in whole homogenates as well as in lipid extracts from homogenates as thiobarbituric acid reactive substances .

Example answer:
{"entities": [{"text": "thiobarbituric acid", "type": "Chemical"}]}

Example input:
Sentence: Immunostaining for 7H6 , not ZO-1 , decreased and predominantly appeared as discrete signals in the submembranous cytoplasm of periportal hepatocytes after BDL .

Example answer:
{"entities": []}

Example input:
Sentence: This study supports the role of lipid peroxidation in mediating the proteinuric injury in PAN nephropathy .

Example answer:
{"entities": [{"text": "proteinuric injury", "type": "Disease"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}]}

Example input:
Sentence: Furthermore , it was observed that TAM inhibits the peroxidation of human erythrocytes induced by AAPH , thus ruling out TAM-induced cell oxidative stress .

Example answer:
{"entities": [{"text": "TAM", "type": "Chemical"}, {"text": "AAPH", "type": "Chemical"}, {"text": "TAM-induced", "type": "Chemical"}]}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Lipid peroxidation in homogenates was maximal at day 3 and declined rapidly to control levels by day 17 .

Example answer:
{"entities": []}

Example input:
Sentence: These effects suggest that the protection from hemolysis by tocopherols is related to a decreased TAM incorporation in condensed membranes and the structural damage of the erythrocyte membrane is consequently avoided .

Example answer:
{"entities": [{"text": "hemolysis", "type": "Disease"}, {"text": "tocopherols", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}]}

Example input:
Sentence: Biochemical liver function tests indicated hepatocellular necrosis and correlated with histopathological evidence of hepatic injury , the spectrum of which ranged from fatty change and focal hepatocellular necrosis to massive hepatic necrosis .

Example answer:
{"entities": [{"text": "necrosis", "type": "Disease"}, {"text": "hepatic injury", "type": "Disease"}, {"text": "fatty change", "type": "Disease"}, {"text": "massive hepatic necrosis", "type": "Disease"}]}

Example input:
Sentence: Although hepatocyte TJs are impaired in cholestasis , attempts to localize the precise site of hepatocyte TJ damage by freeze-fracture electron microscopy have produced limited information .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}]}

Input:
Sentence: The lack of a significant increase in products of lipid peroxidation suggests that the oxidant stress is of insufficient magnitude to result in irreversible injury to hepatocyte cell membranes .

## Item bc5cdr:test:36
Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: We conclude that phenytoin overdosage does not necessarily result in cerebellar atrophy and it is unlikely that phenytoin medication was the only cause of cerebellar atrophy in the remaining patients .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}, {"text": "overdosage", "type": "Disease"}, {"text": "cerebellar atrophy", "type": "Disease"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "METH", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: In order to elucidate the role of the catecholaminergic system in the cataleptogenic effect of delta 9-tetrahydrocannabinol ( THC ) , the effect of pretreatment with 6-hydroxydopamine ( 6-OHDA ) or with desipramine and 6-OHDA and lesions of the locus coeruleus were investigated in rats .

Example answer:
{"entities": [{"text": "delta 9-tetrahydrocannabinol", "type": "Chemical"}, {"text": "THC", "type": "Chemical"}, {"text": "6-hydroxydopamine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}]}

Example input:
Sentence: Delirium , which may be induced by tricyclic drug therapy in the elderly , can be caused by tricyclics with low anticholinergic potency .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: This case suggests that the psychotic symptoms that occur following phenytoin treatment in some epileptic patients may be the direct result of medication , unrelated to seizures .

Example answer:
{"entities": [{"text": "psychotic symptoms", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "epileptic", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: By using this strategy to study the involvement of MRP2 in brain access of antiepileptic drugs ( AEDs ) , we recently reported that phenytoin is a substrate for MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: Immune mechanisms may be involved in the drug 's hepatotoxicity , as suggested by the T-cell stimulation study reported here .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Input:
Sentence: The exact mechanism by which diphenylhydantoin exerts its toxic effects is not known .

## Item bc5cdr:test:428
Example input:
Sentence: Serum creatinine ( SCr ) levels and estimated glomerular filtration rate were assessed at baseline and 2 to 5 days after receiving medications .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Secondary outcomes were a postdose SCr increase > or = 25 % , a postdose estimated glomerular filtration rate decrease of > or = 25 % , and the mean peak change in SCr .

Example answer:
{"entities": []}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: The SPV during hypotension was 15.7 +/- 6.7 mm Hg in the HEM group , compared with 9.1 +/- 2.0 mm Hg in the SNP group ( P less than 0.02 ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: In each group , SNP infusion resulted in an initial decrease in blood pressure from 86 torr and 83 torr , respectively , to 48 torr .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: During HEM-induced hypotension the cardiac output was significantly lower and systemic vascular resistance higher compared with that in the SNP group .

Example answer:
{"entities": [{"text": "HEM-induced", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Input:
Sentence: Also , systemic vascular resistance ( SVR ) decreased during the eight-minute observation period ( P less than 0.01 ) .

## Item bc5cdr:test:197
Example input:
Sentence: In addition , PD female rats showed increased ( 3 ) H-MK-801 binding in the striatum and hippocampus , but not in the cortex .

Example answer:
{"entities": [{"text": "H-MK-801", "type": "Chemical"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: The effects of METH in CX3CR1 knockout mice were not gender-dependent and did not extend beyond the striatum .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: The results obtained indicate that with all three carcinogens , administration of 5-AzC during repair synthesis increased the incidence of initiated hepatocytes , for example 10-20 foci/cm2 in 5-AzC and carcinogen-treated rats compared with 3-5 foci/cm2 in rats treated with carcinogen only .

Example answer:
{"entities": [{"text": "5-AzC", "type": "Chemical"}]}

Example input:
Sentence: PD female rats also showed increased ( 3 ) H-haloperidol binding and decreased dopamine transporter binding in striatum .

Example answer:
{"entities": [{"text": "H-haloperidol", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: This treatment with CBZ had no apparent adverse effect on folate concentrations in the rat , and , indeed , the folate concentration increased in liver after 6 weeks of treatment and in plasma at 8 weeks of treatment .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: Phenobarbitone-induced enlargement of the liver in the rat : its relationship to carbon tetrachloride-induced cirrhosis .

Example answer:
{"entities": [{"text": "Phenobarbitone-induced", "type": "Chemical"}, {"text": "enlargement of the liver", "type": "Disease"}, {"text": "carbon", "type": "Chemical"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: Male Wistar rats were challenged intragastrically once daily for 9 days with 1.0 ml/kg of corn oil containing vitamin D2 and cholesterol to induce atherosclerosis .

Example answer:
{"entities": [{"text": "vitamin D2", "type": "Chemical"}, {"text": "cholesterol", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: The yield of severe cirrhosis of the liver ( defined as a shrunken finely nodular liver with micronodular histology , ascites greater than 30 ml , plasma albumin less than 2.2 g/dl , splenomegaly 2-3 times normal , and testicular atrophy approximately half normal weight ) after 12 doses of carbon tetrachloride given intragastrically in the phenobarbitone-primed rat was increased from 25 % to 56 % by giving the initial `` calibrating '' dose of carbon tetrachloride at the peak of the phenobarbitone-induced enlargement of the liver .

Example answer:
{"entities": [{"text": "cirrhosis of the liver", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "splenomegaly", "type": "Disease"}, {"text": "atrophy", "type": "Disease"}, {"text": "carbon tetrachloride", "type": "Chemical"}, {"text": "phenobarbitone-primed", "type": "Chemical"}, {"text": "phenobarbitone-induced", "type": "Chemical"}, {"text": "enlargement of the liver", "type": "Disease"}]}

Input:
Sentence: In the intact male and female rat , no direct relationship was observed between dose of tetracycline and hepatic accumulation of triglyceride .

## Item bc5cdr:test:472
Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: All patients were on a regular transfusion-chelation program maintaining a mean hemoglobin level of 9.5 gr/dl .

Example answer:
{"entities": []}

Example input:
Sentence: The blood amounts and hematoma volumes were significantly correlated , and the hematoma induced by 0.014-unit collagenase was adequate to detect ICH deterioration .

Example answer:
{"entities": [{"text": "hematoma", "type": "Disease"}, {"text": "ICH", "type": "Disease"}]}

Example input:
Sentence: HBsAg , anti-HBs , anti-HBc , and anti-HIV 1/2 were determined as part of routine diagnosis using Axsym assays ( Abbott Laboratories , North Chicago , IL ) .

Example answer:
{"entities": [{"text": "HBsAg", "type": "Chemical"}]}

Example input:
Sentence: Data suggest that this sensitive hemoglobin assay is useful for ICH detection , and that a model with a small ICH induced with a low-dose collagenase should be used for evaluation of drugs that may affect ICH .

Example answer:
{"entities": [{"text": "ICH", "type": "Disease"}]}

Example input:
Sentence: The serum of six affected workers and five controls was tested for autoantibodies that react with human liver cytochrome-P450 2E1 ( P450 2E1 ) and P58 protein disulphide isomerase isoform ( P58 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Severe and clinically evident anemia of Hb < 11 g/dl with clinical symptoms was detected in 6 patients ( 14.3 % ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Admission laboratory tests were as follows : alanine aminotransferase , 67 U/L ( reference range , 10-37 U/L ) ; aspartate aminotransferase , 98 U/L ( 10-40 U/L ) ; alkaline phosphatase , 513 U/L ( 0-270 U/L ) ; gamma-glutamyltransferase , 32 U/L ( 7-49 U/L ) ; amylase , 46 U/L ( 0-220 U/L ) ; total bilirubin , 20.1 mg/dL ( 0.2-1.0 mg/dL ) ; direct bilirubin , 14.8 mg/dL ( 0-0.3 mg/dL ) ; and albumin , 4.7 mg/dL ( 3.5-5.4 mg/dL ) .

Example answer:
{"entities": [{"text": "alanine", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Two weeks after the initiation of therapy , her hematocrit had decreased from 44.1 % to 20.4 % , and she had a positive direct Coombs antiglobulin test and an elevated indirect bilirubin .

Example answer:
{"entities": [{"text": "bilirubin", "type": "Chemical"}]}

Input:
Sentence: Evaluation revealed a hemoglobin of three grams , 3+ Coombs ' test with polyspecific anti-human globulin and monospecific IgG reagents , and a warm reacting autoantibody .

## Item bc5cdr:test:474
Example input:
Sentence: This study analyzed the incidence of neurological complications during ALL treatment in a single pediatric institution , focusing on clinical , radiological , and electrophysiological findings .

Example answer:
{"entities": [{"text": "neurological complications", "type": "Disease"}, {"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: Rhabdomyolysis is a potentially lethal syndrome that psychiatric patients seem predisposed to develop .

Example answer:
{"entities": [{"text": "Rhabdomyolysis", "type": "Disease"}, {"text": "psychiatric", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Example input:
Sentence: Neither the patient nor the anaesthetist was aware of the diagnosis before this potentially lethal complication occurred .

Example answer:
{"entities": []}

Example input:
Sentence: At presentation , advanced encephalopathy and cerebral edema were present in 51 ( 76 % ) and 29 ( 41.4 % ) patients , respectively .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "cerebral edema", "type": "Disease"}]}

Example input:
Sentence: This case documents acute drug-related vanishing bile duct syndrome in the pediatric age group and suggests shared immune mechanisms in the pathogenesis of both Stevens-Johnson syndrome and vanishing bile duct syndrome .

Example answer:
{"entities": [{"text": "vanishing bile duct syndrome", "type": "Disease"}, {"text": "Stevens-Johnson syndrome", "type": "Disease"}]}

Example input:
Sentence: A previously healthy child who developed acute , severe , rapidly progressive vanishing bile duct syndrome shortly after Stevens-Johnson syndrome is described ; this was temporally associated with ibuprofen use .

Example answer:
{"entities": [{"text": "vanishing bile duct syndrome", "type": "Disease"}, {"text": "Stevens-Johnson syndrome", "type": "Disease"}, {"text": "ibuprofen", "type": "Chemical"}]}

Example input:
Sentence: Further studies are necessary to determine the exact extent of this problem and to improve the efficacy of diagnostic methods .

Example answer:
{"entities": []}

Example input:
Sentence: It is necessary that both oncologists and neurologists be fully aware of this unusual complication .

Example answer:
{"entities": []}

Example input:
Sentence: Incorrect diagnosis of the syndrome will lead to a significant reduction of life quality in patients suffering from CIPS .

Example answer:
{"entities": [{"text": "CIPS", "type": "Disease"}]}

Input:
Sentence: Emergency physicians treating children must be aware of this syndrome in order to diagnose and treat it correctly .

## Item bc5cdr:test:465
Example input:
Sentence: The Receiver Operative Characteristic Curve showed that OD > 1.27 in the isolated-HIT group had a significantly higher chance of developing thrombosis by day 30 .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: cTnI ( ng/ml ) , CK-MB mass and CK remained unchanged in DOX rats compared with controls .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: Most patients showed improvement in individual parameters and global score of quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: Heart rate ( HR ) did not change in either group .

Example answer:
{"entities": []}

Example input:
Sentence: These variables returned to baseline when rigidity was abolished with metocurine .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}, {"text": "metocurine", "type": "Chemical"}]}

Example input:
Sentence: During the study , vitamin B12 and folate levels were significantly higher in group II patients ; however , no differences in hemoglobin , hematocrit , mean corpuscular volume , and white-cell , neutrophil and platelet counts were observed between groups at 3 , 6 , 9 and 12 months .

Example answer:
{"entities": [{"text": "vitamin B12", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: Dopamine turnover ratios ( DOPAC : DA and HVA : DA ) were found to be lower in those animals exposed to the exploratory box when compared to their home cage counterparts .

Example answer:
{"entities": [{"text": "Dopamine", "type": "Chemical"}, {"text": "DOPAC", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "HVA", "type": "Chemical"}]}

Example input:
Sentence: Bone scans showed an increased tracer uptake of the foot bones .

Example answer:
{"entities": []}

Input:
Sentence: However , there was a significant difference in parameters reflecting bone turnover rates between groups .
