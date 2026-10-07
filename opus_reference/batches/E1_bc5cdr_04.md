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

## Item bc5cdr:test:672
Example input:
Sentence: Rizatriptan was also superior to ergotamine/caffeine in the proportions of patients with no nausea , vomiting , phonophobia or photophobia and for patients with normal function 2 h after drug intake ( p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "Rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "phonophobia", "type": "Disease"}, {"text": "photophobia", "type": "Disease"}]}

Example input:
Sentence: In a 6-week double-blind parallel treatment study , dothiepin and amitriptyline were compared to placebo in the treatment of 33 depressed outpatients .

Example answer:
{"entities": [{"text": "dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressed", "type": "Disease"}]}

Example input:
Sentence: Zyban , a sustained-release formulation of bupropion hydrochloride , was recently released in Ireland , as a smoking cessation aid .

Example answer:
{"entities": [{"text": "Zyban", "type": "Chemical"}, {"text": "bupropion hydrochloride", "type": "Chemical"}]}

Example input:
Sentence: Phenylpropanolamine ( PPA ) , a synthetic sympathomimetic that is structurally similar to amphetamine , is available over the counter in anorectics , nasal congestants , and cold preparations .

Example answer:
{"entities": [{"text": "Phenylpropanolamine", "type": "Chemical"}, {"text": "PPA", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: Mean peak forced expiratory volume in 1 second ( FEV1 ) increases over baseline and the proportion of patients attaining at least a 15 % increase in the FEV1 ( responders ) were 31 % and 90 % , respectively , for ipratropium and 17 % and 50 % , respectively , for theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Dothiepin and amitriptyline were equally effective in alleviating the symptoms of depressive illness , and both were significantly superior to placebo .

Example answer:
{"entities": [{"text": "Dothiepin", "type": "Chemical"}, {"text": "amitriptyline", "type": "Chemical"}, {"text": "depressive illness", "type": "Disease"}]}

Example input:
Sentence: The mean duration of action was 3.8 hours with ipratropium and 2.4 hours with theophylline .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Acute bronchodilating effects of ipratropium bromide and theophylline in chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: The bronchodilator effects of a single dose of ipratropium bromide aerosol ( 36 micrograms ) and short-acting theophylline tablets ( dose titrated to produce serum levels of 10-20 micrograms/mL ) were compared in a double-blind , placebo-controlled crossover study in 21 patients with stable , chronic obstructive pulmonary disease .

Example answer:
{"entities": [{"text": "ipratropium bromide", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic obstructive pulmonary disease", "type": "Disease"}]}

Example input:
Sentence: These results show that ipratropium is a more potent bronchodilator than oral theophylline in patients with chronic airflow obstruction .

Example answer:
{"entities": [{"text": "ipratropium", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "chronic airflow obstruction", "type": "Disease"}]}

Input:
Sentence: Oxitropium proves to be a valuable alternative to theophylline in nocturnal asthma , since it is equally potent , safer and does not require the titration of dosage .

## Item bc5cdr:test:777
Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: The administration of phenobarbitone and carbamazepine for 21days caused a significant impairment of learning and memory as well as an increased oxidative stress .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "impairment of learning and memory", "type": "Disease"}]}

Example input:
Sentence: Ticlopidine-induced aplastic anemia : report of three Chinese patients and review of the literature .

Example answer:
{"entities": [{"text": "Ticlopidine-induced", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}]}

Example input:
Sentence: Antithymocyte globulin in the treatment of D-penicillamine-induced aplastic anemia .

Example answer:
{"entities": [{"text": "Antithymocyte globulin", "type": "Chemical"}, {"text": "D-penicillamine-induced", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}]}

Example input:
Sentence: Hypersensitivity to carbamazepine presenting with a leukemoid reaction , eosinophilia , erythroderma , and renal failure .

Example answer:
{"entities": [{"text": "Hypersensitivity", "type": "Disease"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "leukemoid reaction", "type": "Disease"}, {"text": "eosinophilia", "type": "Disease"}, {"text": "erythroderma", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Two patients with signs of carbamazepine neurotoxicity after combined treatment with verapamil showed complete recovery after discontinuation of the calcium entry blocker .

Example answer:
{"entities": [{"text": "carbamazepine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Carbamazepine ( CBZ ) , a commonly used AED , has been implicated in some clinical studies .

Example answer:
{"entities": [{"text": "Carbamazepine", "type": "Chemical"}, {"text": "CBZ", "type": "Chemical"}]}

Example input:
Sentence: Use of antithymocyte globulin may be the optimal treatment of D-penicillamine-induced aplastic anemia .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "D-penicillamine-induced", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}]}

Example input:
Sentence: A patient who received antithymocyte globulin therapy for aplastic anemia due to D-penicillamine therapy is described .

Example answer:
{"entities": [{"text": "antithymocyte globulin", "type": "Chemical"}, {"text": "aplastic anemia", "type": "Disease"}, {"text": "D-penicillamine", "type": "Chemical"}]}

Example input:
Sentence: We report a patient in whom hypersensitivity to carbamazepine presented with generalized erythroderma , a severe leukemoid reaction , eosinophilia , hyponatremia , and renal failure .

Example answer:
{"entities": [{"text": "hypersensitivity", "type": "Disease"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "erythroderma", "type": "Disease"}, {"text": "leukemoid reaction", "type": "Disease"}, {"text": "eosinophilia", "type": "Disease"}, {"text": "hyponatremia", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Input:
Sentence: Fatal aplastic anemia in a patient treated with carbamazepine .

## Item bc5cdr:test:906
Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with the vehicle ( 2 mL/kg of distilled water and 5 % w/v cellulose , 10 days ) , gum Arabic ( 2 mL/kg of a 10 % w/v aqueous suspension of gum Arabic powder , orally for 10 days ) , or gum Arabic concomitantly with GM ( 80mg/kg/day intramuscularly , during the last six days of the treatment period ) .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}]}

Example input:
Sentence: Ten rats received saline as a control group .

Example answer:
{"entities": []}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Sham-operated rats served as normotensive controls ( 128 +/- 3 mm Hg , n = 8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Rats were treated with seven day intravenous infusion of fucoidan ( 30 micrograms h-1 ) or vehicle .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}]}

Example input:
Sentence: Male SD rats ( n = 30 ) were treated with Ato ( 50 mg/kg per day in drinking water ) or tap water for 15 days .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}]}

Example input:
Sentence: Thirty male Sprague-Dawley rats were divided randomly into four treatment groups : saline , dexamethasone ( dex ) , allopurinol plus saline , and allopurinol plus dex .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "dex", "type": "Chemical"}, {"text": "allopurinol", "type": "Chemical"}]}

Input:
Sentence: Four groups of rats ( n = 7 ) were studied : jj and jJ rats treated either with aspirin 300 mg/kg every other day or sham-treated .

## Item bc5cdr:test:541
Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Provocation of postural hypotension by nitroglycerin in diabetic autonomic neuropathy ?

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Bradykinin receptors antagonists and nitric oxide synthase inhibitors in vincristine and streptozotocin induced hyperalgesia in chemotherapy and diabetic neuropathy rat model .

Example answer:
{"entities": [{"text": "Bradykinin", "type": "Chemical"}, {"text": "nitric oxide", "type": "Chemical"}, {"text": "vincristine", "type": "Chemical"}, {"text": "streptozotocin", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "diabetic neuropathy", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Diabetes mellitus was the major cause of autonomic neuropathy .

Example answer:
{"entities": [{"text": "Diabetes mellitus", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: The magnitude and time course of the increase in heart rate and the decrease in systolic blood pressure after nitroglycerin were similar in the normal and diabetic subjects without autonomic neuropathy , whereas a lesser increase in heart rate and a greater decrease in systolic blood pressure occurred in the diabetic subjects with autonomic neuropathy .

Example answer:
{"entities": [{"text": "nitroglycerin", "type": "Chemical"}, {"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Input:
Sentence: Nifedipine induced bradycardia in a patient with autonomic neuropathy .

## Item bc5cdr:test:1022
Example input:
Sentence: The median duration of survival in the 12 patients was 54 weeks ( range 21 to more than 156 weeks ) , with an 18-month survival rate of 42 % .

Example answer:
{"entities": []}

Example input:
Sentence: Eleven patients ( six male ) with median age 47 years ( range 27-73 ) , median disease duration 50 months ( range 9-178 ) and median follow-up period of patients 13.8 months ( range 5-27 ) were enrolled in this study .

Example answer:
{"entities": []}

Example input:
Sentence: Illness occurred within 1 -- 9 weeks of commencement of therapy in 9 patients , the remaining 3 patients having received the drug for 13 months , 15 months and 7 years before experiencing symptoms .

Example answer:
{"entities": []}

Example input:
Sentence: With current treatment regimens including combined surgery , radiation and chemotherapy , the average life expectancy of the patients is limited to approximately 1 year .

Example answer:
{"entities": []}

Example input:
Sentence: The median duration of response was 21 weeks ( range , 17 to 28 ) .

Example answer:
{"entities": []}

Example input:
Sentence: This imply an incidence of 1.7/100,000 treatment years .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment duration longer than 1 year was associated with an eightfold increased risk ( OR = 7.7 , 95 % CI 0.9 to 69 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment was administered every 3 weeks until disease progression .

Example answer:
{"entities": []}

Example input:
Sentence: Treatment was from weeks 0 to 8 and was then tapered from weeks 8 to 16 .

Example answer:
{"entities": []}

Example input:
Sentence: and the treatment was planned to last 8 weeks .

Example answer:
{"entities": []}

Input:
Sentence: The mean treatment period was 18 months .

## Item bc5cdr:test:1018
Example input:
Sentence: CONCLUSION : Our results suggest that high-dose testosterone therapy may adversely affect atherosclerosis in postmenopausal women and indicate that androgen replacement in these women may not be harmless .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Intramuscular hormone therapy use for 1 year or longer was reported by 25 women .

Example answer:
{"entities": []}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In almost half of these women severe atherosclerosis of the aorta was present ( n=11 ) , while in women without hormone use severe atherosclerosis of the aorta was present in less than 20 % ( OR 3.1 ; 95 % CI , 1.1-8.5 , adjusted for age , years since menopause , smoking , and body mass index ) .

Example answer:
{"entities": [{"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: Seven patients had previously received radiotherapy and seven had received hormone therapy .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : The Multiple Outcomes of Raloxifene Evaluation , a multicenter , randomized , double-blind trial , enrolled 7,705 postmenopausal women with osteoporosis .

Example answer:
{"entities": [{"text": "Raloxifene", "type": "Chemical"}, {"text": "osteoporosis", "type": "Disease"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: METHODS : Thirty-nine postmenopausal women with osteopenia or osteoporosis were included in this prospective , controlled clinical study .

Example answer:
{"entities": [{"text": "osteopenia", "type": "Disease"}, {"text": "osteoporosis", "type": "Disease"}]}

Input:
Sentence: This paper reports the results of a study of 50 menopausal women receiving hormonal replacement therapy .

## Item bc5cdr:test:746
Example input:
Sentence: It is therefore suggested that caution should be exercised when prescribing vasodilator drugs in diabetic patients , particularly those with autonomic neuropathy .

Example answer:
{"entities": [{"text": "diabetic", "type": "Disease"}, {"text": "autonomic neuropathy", "type": "Disease"}]}

Example input:
Sentence: Since the cranial condition precluded use of more usual methods , lidocaine was given intra-arterially , with careful cardiovascular monitoring , to counteract the vasospasm .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: The authors present a 10-year-old boy chronically treated with lisinopril , an angiotensin converting enzyme inhibitor , to control hypertension who developed hypotension following the addition of tizanidine , an alpha-2 agonist , for the treatment of spasticity .

Example answer:
{"entities": [{"text": "lisinopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}, {"text": "tizanidine", "type": "Chemical"}, {"text": "spasticity", "type": "Disease"}]}

Example input:
Sentence: Nitroprusside caused significant decreases in arterial blood pressure and systemic vascular resistance and increases in heart rate , but did not change cardiac output or QS/QT .

Example answer:
{"entities": [{"text": "Nitroprusside", "type": "Chemical"}, {"text": "decreases in arterial blood pressure", "type": "Disease"}]}

Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: The effect of a 6-week treatment with the calcium channel blocker nitrendipine or the angiotensin converting enzyme inhibitor enalapril on blood pressure , albuminuria , renal hemodynamics , and morphology of the nonclipped kidney was studied in rats with two-kidney , one clip renovascular hypertension .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nitrendipine", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "albuminuria", "type": "Disease"}, {"text": "renovascular hypertension", "type": "Disease"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND AND PURPOSE : The Intravenous Nimodipine West European Stroke Trial ( INWEST ) found a correlation between nimodipine-induced reduction in blood pressure ( BP ) and an unfavorable outcome in acute stroke .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "Stroke", "type": "Disease"}, {"text": "nimodipine-induced", "type": "Chemical"}, {"text": "reduction in blood pressure", "type": "Disease"}, {"text": "acute stroke", "type": "Disease"}]}

Example input:
Sentence: Nimodipine treatment resulted in a statistically significant reduction in systolic BP ( SBP ) and diastolic BP ( DBP ) from baseline compared with placebo during the first few days .

Example answer:
{"entities": [{"text": "Nimodipine", "type": "Chemical"}, {"text": "reduction in systolic BP", "type": "Disease"}]}

Example input:
Sentence: These results suggest that spasm provocation tests , which use an intracoronary injection of a relatively low dose of methylergonovine , have a high sensitivity in variant angina and the vasoreactivity of the right coronary artery may be greater than that of the other coronary arteries .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "methylergonovine", "type": "Chemical"}, {"text": "variant angina", "type": "Disease"}]}

Input:
Sentence: The coronary vasodilating properties of nisoldipine have led to the investigation of this agent for use in angina .

## Item bc5cdr:test:942
Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Clonidine-induced bradycardia in conscious alpha2ABC-/- mice was 32.3 % ( 10 microg/kg ) and 26.6 % ( 100 microg/kg ) of the effect in wild-type mice .

Example answer:
{"entities": [{"text": "Clonidine-induced", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: In contrast , no artery calcification could be detected in 10-month-old adult rats even after 4 weeks of Warfarin treatment .

Example answer:
{"entities": [{"text": "artery calcification", "type": "Disease"}, {"text": "Warfarin", "type": "Chemical"}]}

Example input:
Sentence: Concurrent treatment of both dietary groups with Warfarin produced massive focal calcification of the artery media in the ad libitum-fed rats but no detectable artery calcification in the restricted-diet , growth-inhibited group .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcification of the artery", "type": "Disease"}, {"text": "artery calcification", "type": "Disease"}]}

Example input:
Sentence: Atherosclerosis could produce gastric hemorrhagic ulcer via aggravation of gastric acid back-diffusion , LPO generation , histamine release and microvascular permeability that could be ameliorated by verapamil in rats .

Example answer:
{"entities": [{"text": "Atherosclerosis", "type": "Disease"}, {"text": "gastric hemorrhagic", "type": "Disease"}, {"text": "ulcer", "type": "Disease"}, {"text": "histamine", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: To directly examine the importance of growth to Warfarin-induced artery calcification in animals of the same age , 20-day-old rats were fed for 2 weeks either an ad libitum diet or a 6-g/d restricted diet that maintains weight but prevents growth .

Example answer:
{"entities": [{"text": "Warfarin-induced", "type": "Chemical"}, {"text": "artery calcification", "type": "Disease"}]}

Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The first series of experiments examined the influence of age and growth status on artery calcification in Warfarin-treated rats .

Example answer:
{"entities": [{"text": "artery calcification", "type": "Disease"}, {"text": "Warfarin-treated", "type": "Chemical"}]}

Example input:
Sentence: Preclinical toxicologic investigation suggested that a new calcium channel blocker , Ro 40-5967 , induced cardiovascular alterations in rat fetuses exposed to this agent during organogenesis .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "Ro 40-5967", "type": "Chemical"}, {"text": "cardiovascular alterations", "type": "Disease"}]}

Example input:
Sentence: Treatment for 2 weeks with Warfarin caused massive focal calcification of the artery media in 20-day-old rats and less extensive focal calcification in 42-day-old rats .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcification of the artery", "type": "Disease"}, {"text": "calcification", "type": "Disease"}]}

Input:
Sentence: These experimental findings represent the first indication that life-long barium ingestion may have significant adverse effects on the mammalian cardiovascular system .

## Item bc5cdr:test:1027
Example input:
Sentence: From October 1993 to November 1995 , we treated 13 patients with previously chemotherapy-treated metastatic breast cancer by mitoxantrone , 12 mg/m2 , on day 1 and continuous infusion of 5-FU , 3000 mg/m2 , together with leucovorin , 300 mg/m2 , for 48 h from day 1 to 2 .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}]}

Example input:
Sentence: Seven patients had previously received radiotherapy and seven had received hormone therapy .

Example answer:
{"entities": []}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: After 2 weeks of treatment , patients tested 5-8 h after the last dose of medication did not show any decrement of performance .

Example answer:
{"entities": []}

Example input:
Sentence: Administration of this regimen to breast cancer patients who have been treated by chemotherapy and those with impaired heart function requires careful attention .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "impaired heart function", "type": "Disease"}]}

Example input:
Sentence: Treatment of previously treated metastatic breast cancer by mitoxantrone and 48-hour continuous infusion of high-dose 5-FU and leucovorin ( MFL ) : low palliative benefit and high treatment-related toxicity .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "MFL", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Intramuscular hormone therapy use for 1 year or longer was reported by 25 women .

Example answer:
{"entities": []}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Input:
Sentence: These results suggest that hormonal replacement therapy can be safely prescribed if the following criteria are satisfied : 1 ) preliminary evaluation of patients from a clinical , metabolic , cytologic , and mammographic perspective ; 2 ) cyclic treatment schedule , with a progestative phase of 10 days ; and 3 ) periodic complete follow-up , with accurate thermographic evaluation of the breast target tissues .

## Item bc5cdr:test:805
Example input:
Sentence: INTRODUCTION : Cyclophosphamide is an alkylating agent given frequently as a component of many conditioning regimens .

Example answer:
{"entities": [{"text": "Cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: Anthracyclines are effective antineoplastic drugs , but they frequently cause dose-related cardiotoxicity .

Example answer:
{"entities": [{"text": "Anthracyclines", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: The risk of bladder cancer doubled for every 10 g increment in cyclophosphamide ( OR = 2.0 , 95 % confidence interval ( CI ) 0.8 to 4.9 ) .

Example answer:
{"entities": [{"text": "bladder cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: Cyclophosphamide therapy increases the risk of carcinoma of the bladder .

Example answer:
{"entities": [{"text": "Cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: Routine EKG monitoring during infusional cyclophosphamide did not predict CHF development .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CHF", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The median cumulative doses of cyclophosphamide among cases ( n = 11 ) and controls ( n = 25 ) were 113 g and 25 g , respectively .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : The results indicate a dose-response relationship between cyclophosphamide and the risk of bladder cancer , high cumulative risks in the entire cohort , and also the possibility of risk factors operating even before Wegener 's granulomatosis .

Example answer:
{"entities": [{"text": "cyclophosphamide", "type": "Chemical"}, {"text": "bladder cancer", "type": "Disease"}, {"text": "Wegener 's granulomatosis", "type": "Disease"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: Incidence of transient cyclophosphamide-related cardiac toxicity ( 10 % ) is comparable to previous recorded literature .

Example answer:
{"entities": [{"text": "cyclophosphamide-related", "type": "Chemical"}, {"text": "cardiac toxicity", "type": "Disease"}]}

Example input:
Sentence: Cardiac toxicity observed in association with high-dose cyclophosphamide-based chemotherapy for metastatic breast cancer .

Example answer:
{"entities": [{"text": "Cardiac toxicity", "type": "Disease"}, {"text": "cyclophosphamide-based", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Input:
Sentence: Cyclophosphamide cardiotoxicity : an analysis of dosing as a risk factor .

## Item bc5cdr:test:761
Example input:
Sentence: Abnormal movements and deafness occurred only in rats treated during the preweaning period ; within this period the greatest sensitivities for these abnormalities occurred from 2 to 11-17 and 5 to 11 days of age , respectively , indicating that the cochlea is more sensitive to streptomycin than the site ( vestibular or central ) responsible for the dyskinesias .

Example answer:
{"entities": [{"text": "Abnormal movements", "type": "Disease"}, {"text": "deafness", "type": "Disease"}, {"text": "streptomycin", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Male rats that received prenatal dexamethasone on days 15 and 16 , 17 and 18 , and 13 and 14 of gestation had elevated blood pressures at 6 months of age ; the latter group did not have a reduction in glomerular number .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "elevated blood pressures", "type": "Disease"}, {"text": "reduction in glomerular number", "type": "Disease"}]}

Example input:
Sentence: All rats were terminated either 24 h or 3 weeks after the DFP injection .

Example answer:
{"entities": [{"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: Groups of 5-week old male Fischer-344 rats were fed for 7-25 months semipurified choline-devoid or choline-supplemented diets , containing or not 0.06 % phenobarbital .

Example answer:
{"entities": [{"text": "choline-devoid", "type": "Chemical"}, {"text": "choline-supplemented", "type": "Chemical"}, {"text": "phenobarbital", "type": "Chemical"}]}

Example input:
Sentence: Rats were treated with a single IV injection of puromycin aminonucleoside , ( PAN , 7.5 mg/kg ) and 24 hour urine samples were obtained prior to sacrifice on days 3,5,7,10,17,27,41 ( N = 5-10 per group ) .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: Pregnant rats were given either vehicle or 2 daily intraperitoneal injections of dexamethasone ( 0.2 mg/kg body weight ) on gestational days 11 and 12 , 13 and 14 , 15 and 16 , 17 and 18 , or 19 and 20 .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Drugs were separately , orally once daily dosed to pregnant rats from day 8 to 21 ( GD1=plug day ) .

Example answer:
{"entities": []}

Example input:
Sentence: Male Sprague-Dawley rats were treated with D-penicillamine ( D-pen ) 500 mg/kg/day for 10 or 42 days .

Example answer:
{"entities": [{"text": "D-penicillamine", "type": "Chemical"}, {"text": "D-pen", "type": "Chemical"}]}

Example input:
Sentence: All of the rats in the saline-treated epileptic control group developed SRS , whereas none of the BMC-treated epileptic animals had seizures in the short term ( 15 days after transplantation ) , regardless of the BMC source .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "SRS", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: Sprague-Dawley rats that were 20 days pregnant and nonpregnant rats of the same age and strain received infusions of aminophylline until onset of maximal seizures which occurred after 28 and 30 minutes respectively .

## Item bc5cdr:test:825
Example input:
Sentence: During the course of nephrotic syndrome , serum urea concentrations increased significantly faster in sgk1 ( -/- ) mice than in sgk1 ( +/+ ) mice leading to uremia and a reduced median survival in sgk1 ( -/- ) mice ( 29 vs. 40 days in sgk1 ( +/+ ) mice ) .

Example answer:
{"entities": [{"text": "nephrotic syndrome", "type": "Disease"}, {"text": "urea", "type": "Chemical"}, {"text": "uremia", "type": "Disease"}]}

Example input:
Sentence: Epithelial sodium channel ( ENaC ) subunit mRNA and protein expression in rats with puromycin aminonucleoside-induced nephrotic syndrome .

Example answer:
{"entities": [{"text": "sodium", "type": "Chemical"}, {"text": "puromycin", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Example input:
Sentence: The nephrotoxic action of anticancer drugs such as nitrogranulogen ( NG ) , methotrexate ( MTX ) , 5-fluorouracil ( 5-FU ) and cyclophosphamide ( CY ) administered alone or in combination [ MTX + 5-FU + CY ( CMF ) ] was evaluated in experiments on Wistar rats .

Example answer:
{"entities": [{"text": "nephrotoxic", "type": "Disease"}, {"text": "nitrogranulogen", "type": "Chemical"}, {"text": "NG", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: We suggest that our patient 's tubular dysfunction and myopathy may have resulted from mitochondrial dysfunction which is triggered by tacrolimus and augmented by lamivudine .

Example answer:
{"entities": [{"text": "tubular dysfunction", "type": "Disease"}, {"text": "myopathy", "type": "Disease"}, {"text": "mitochondrial dysfunction", "type": "Disease"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: In this study , 62 patients with confirmed initial normal renal function and treated with 2 to 5 mg/kg/day of gentamicin sulfate or tobramycin sulfate for a minimum of seven days were followed up prospectively for the development of aminoglycoside-related renal failure , defined as at least a one-third reduction in renal function .

Example answer:
{"entities": [{"text": "gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "aminoglycoside-related", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Input:
Sentence: These models may also be useful in developing insights into the pathophysiology of aminoglycoside-induced nephrotoxicity .

## Item bc5cdr:test:618
Example input:
Sentence: On the other hand , pretreatment with p-chlorophenylalamine ( 3 X 320 mg/kg i.p. , 24 hr ) , a serotonin depletor , caused no significant change in the hyperactivity .

Example answer:
{"entities": [{"text": "p-chlorophenylalamine", "type": "Chemical"}, {"text": "serotonin", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}]}

Example input:
Sentence: METHODS : For a period of 2 weeks , CsA 15 mg/kg/day ( given orally ) , FK506 3.0 mg/kg/day ( given orally ) or SRL 0.4 mg/kg/day ( given intraperitoneally ) was administered once a day as these doses have earlier been found to achieve a significant immunosuppressive effect in Sprague-Dawley rats .

Example answer:
{"entities": [{"text": "CsA", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: Newborn rats were given terbutaline ( 10 mg/kg ) daily on postnatal days ( PN ) 2 to 5 or PN 11 to 14 and examined 24 h after the last dose and at PN 30 .

Example answer:
{"entities": [{"text": "terbutaline", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: They were given a ten day pretreatment with either L-alpha-GFC or placebo , p.o. , and on the eleventh day either scopolamine or placebo , i.m .

Example answer:
{"entities": [{"text": "L-alpha-GFC", "type": "Chemical"}, {"text": "scopolamine", "type": "Chemical"}]}

Example input:
Sentence: A nonregenerative anemia was the most compromising of the cytopenias and occurred in approximately 50 % of dogs receiving 400-500 mg/kg cefonicid or 540-840 mg/kg cefazedone .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "cytopenias", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Input:
Sentence: After pretreatment with 3 mg of cyproheptadine , 2 mg mianserin , or 2 mg chlorpheniramine , only 5 of 105 animals ( 5 % ) died after receiving BSA on day +7 ( p less than 0.001 ) .

## Item bc5cdr:test:857
Example input:
Sentence: Mitochondrial radiocalcium uptakes were significantly decreased in animals pretreated with acetylsalicylic acid or dipyridamole or when hydrocortisone was added to the epinephrine infusion ( 2,682,2,803 , and 3,424 counts per minute per gram of dried fraction , respectively ) .

Example answer:
{"entities": [{"text": "radiocalcium", "type": "Chemical"}, {"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: Neither dose of pentoxifylline significantly decreased the dipyridamole-induced hyperemia , while peak coronary blood flow was significantly lower after theophylline ( p less than 0.01 ) .

Example answer:
{"entities": [{"text": "pentoxifylline", "type": "Chemical"}, {"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "hyperemia", "type": "Disease"}, {"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: Therefore , we studied the hyperemic response to dipyridamole in seven open-chest anesthetized dogs after pretreatment with either pentoxifylline ( 0 , 7.5 , or 15 mg/kg i.v . )

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "pentoxifylline", "type": "Chemical"}]}

Example input:
Sentence: Dipyridamole-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "Dipyridamole-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: Dipyridamole-thallium-201 imaging is often performed in patients unable to exercise because of peripheral vascular disease .

Example answer:
{"entities": [{"text": "Dipyridamole-thallium-201", "type": "Chemical"}, {"text": "peripheral vascular disease", "type": "Disease"}]}

Example input:
Sentence: To our knowledge , this has not previously been reported as a side effect of preoperative dipyridamole therapy , although dipyridamole-induced myocardial ischemia has been demonstrated to occur in animals and humans with coronary artery disease .

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}]}

Example input:
Sentence: Dipyridamole significantly increased coronary blood flow before and after 7.5 or 15 mm/kg i.v .

Example answer:
{"entities": [{"text": "Dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: Angina and ischemic electrocardiographic changes occurred after administration of oral dipyridamole in four patients awaiting urgent myocardial revascularization procedures .

Example answer:
{"entities": [{"text": "Angina", "type": "Disease"}, {"text": "dipyridamole", "type": "Chemical"}]}

Input:
Sentence: Electrocardiographic changes after dipyridamole infusion ( 0.568 mg/kg/4 min ) were studied in 41 patients with coronary artery disease and compared with those after submaximal treadmill exercise by use of the body surface mapping technique .

## Item bc5cdr:test:760
Example input:
Sentence: Effects of aminophylline on the threshold for initiating ventricular fibrillation during respiratory failure .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "respiratory failure", "type": "Disease"}]}

Example input:
Sentence: The effects of aminophylline on the ventricular fibrillation threshold during normal acid-base conditions and during respiratory failure were studied in anesthetized open chest dogs .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "respiratory failure", "type": "Disease"}]}

Example input:
Sentence: We studied a patient with no prior history of neuromuscular disease who became virtually quadriplegic after parenteral magnesium administration for preeclampsia .

Example answer:
{"entities": [{"text": "neuromuscular disease", "type": "Disease"}, {"text": "quadriplegic", "type": "Disease"}, {"text": "magnesium", "type": "Chemical"}, {"text": "preeclampsia", "type": "Disease"}]}

Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: During the infusion of aminophylline , the ventricular fibrillation threshold was reduced by 30 to 40 percent of the control when pH and partial pressures of oxygen ( PO2 ) and carbon dioxide ( CO2 ) were kept within normal limits .

Example answer:
{"entities": [{"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "PO2", "type": "Chemical"}, {"text": "carbon dioxide", "type": "Chemical"}, {"text": "CO2", "type": "Chemical"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Whether pentoxifylline inhibits dipyridamole-induced coronary hyperemia like other methylxanthines such as theophylline and should be stopped prior to dipyridamole-thallium-201 imaging is unknown .

Example answer:
{"entities": [{"text": "pentoxifylline", "type": "Chemical"}, {"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "hyperemia", "type": "Disease"}, {"text": "methylxanthines", "type": "Chemical"}, {"text": "theophylline", "type": "Chemical"}, {"text": "dipyridamole-thallium-201", "type": "Chemical"}]}

Example input:
Sentence: While side effects were rare , those experienced after theophylline use did involve the cardiovascular and gastrointestinal systems .

Example answer:
{"entities": [{"text": "theophylline", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Reassuringly , penicillins , erythromycins , and cephalosporins , although used commonly by pregnant women , were not associated with many birth defects .

Example answer:
{"entities": [{"text": "penicillins", "type": "Chemical"}, {"text": "erythromycins", "type": "Chemical"}, {"text": "cephalosporins", "type": "Chemical"}, {"text": "birth defects", "type": "Disease"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Input:
Sentence: The purpose of this investigation was to determine whether the neurotoxicity of theophylline is altered in advanced pregnancy .

## Item bc5cdr:test:586
Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: Effects of acetylsalicylic acid , dipyridamole , and hydrocortisone on epinephrine-induced myocardial injury in dogs .

Example answer:
{"entities": [{"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine-induced", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: By using this strategy to study the involvement of MRP2 in brain access of antiepileptic drugs ( AEDs ) , we recently reported that phenytoin is a substrate for MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}]}

Example input:
Sentence: Alpha2ABC-/- mice were completely unresponsive to the analgesic and hypnotic effects of clonidine ; however , clonidine significantly lowered heart rate in alpha2ABC-/- mice by up to 150 bpm .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Nitroglycerin has been shown to reduce ST-segment elevation during acute myocardial infarction , an effect potentiated in the dog by agents that reverse nitroglycerin-induced hypotension .

Example answer:
{"entities": [{"text": "Nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}, {"text": "nitroglycerin-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The [ verapamil ] o that arrested atrial beating ( AC ) was also potentiated with the order LNa = LNa+LCa = LNa+HCa = LCa > HCa = N. The results indicate that rat atrial spontaneous beating is more dependent on [ Na ] o than on [ Ca ] o in a range of +/- 50 % of their normal concentration .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: Recurrent seizures were treated with diazepam and broad complex tachycardia was successfully treated with adenosine .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "diazepam", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "adenosine", "type": "Chemical"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Input:
Sentence: ACC-9653 and phenytoin sodium have similar antiarrhythmic activity against ouabain-induced ventricular tachycardia in anesthetized dogs .

## Item bc5cdr:test:807
Example input:
Sentence: The most common signs of cardiotoxicity were chest pain , ST-T wave changes and atrial fibrillation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "chest pain", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: In high doses , its nonhematological dose-limiting toxicity is cardiomyopathy .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Major toxicities were cardiotoxicity and leukopenia .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "leukopenia", "type": "Disease"}]}

Example input:
Sentence: In individuals with preexisting , high-grade coronary arterial narrowing , acute myocardial infarction may result from an increase in myocardial oxygen demand associated with cocaine-induced increase in rate-pressure product .

Example answer:
{"entities": [{"text": "acute myocardial infarction", "type": "Disease"}, {"text": "oxygen", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: Anthracyclines are effective antineoplastic drugs , but they frequently cause dose-related cardiotoxicity .

Example answer:
{"entities": [{"text": "Anthracyclines", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Cardiac toxicity observed in association with high-dose cyclophosphamide-based chemotherapy for metastatic breast cancer .

Example answer:
{"entities": [{"text": "Cardiac toxicity", "type": "Disease"}, {"text": "cyclophosphamide-based", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Example input:
Sentence: The incidence of cardiotoxicity was not higher in patients with signs of cardiovascular disease than in those without in the pre-treatment evaluation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "cardiovascular disease", "type": "Disease"}]}

Input:
Sentence: At these high doses of CYA , serious cardiotoxicity may occur , but definitive risk factors for the development of such cardiotoxicity have not been described .

## Item bc5cdr:test:865
Example input:
Sentence: Epicardial coronary collateral vessels were demonstrated in all four patients ; a coronary `` steal '' phenomenon may be the mechanism of the dipyridamole-induced ischemia observed .

Example answer:
{"entities": [{"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: To our knowledge , this has not previously been reported as a side effect of preoperative dipyridamole therapy , although dipyridamole-induced myocardial ischemia has been demonstrated to occur in animals and humans with coronary artery disease .

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "dipyridamole-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "coronary artery disease", "type": "Disease"}]}

Example input:
Sentence: Acetylsalicylic acid , dipyridamole , and hydrocortisone all appear to have cardioprotective effects when tested in this model .

Example answer:
{"entities": [{"text": "Acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}]}

Example input:
Sentence: Dipyridamole-induced myocardial ischemia .

Example answer:
{"entities": [{"text": "Dipyridamole-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: Simultaneous measurements of ECG and brachial artery dP/dtejc were performed at each dobutamine level .

Example answer:
{"entities": [{"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Dipyridamole-thallium-201 imaging is often performed in patients unable to exercise because of peripheral vascular disease .

Example answer:
{"entities": [{"text": "Dipyridamole-thallium-201", "type": "Chemical"}, {"text": "peripheral vascular disease", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: Dipyridamole significantly increased coronary blood flow before and after 7.5 or 15 mm/kg i.v .

Example answer:
{"entities": [{"text": "Dipyridamole", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : If ECG alone is used for specificity , the combination with dP/dtejc improved the sensitivity of the test and could be a cost-savings alternative to cardiac imaging or perfusion studies to detect myocardial ischemia , especially in patients unable to exercise .

Example answer:
{"entities": [{"text": "myocardial ischemia", "type": "Disease"}]}

Example input:
Sentence: Angina and ischemic electrocardiographic changes occurred after administration of oral dipyridamole in four patients awaiting urgent myocardial revascularization procedures .

Example answer:
{"entities": [{"text": "Angina", "type": "Disease"}, {"text": "dipyridamole", "type": "Chemical"}]}

Input:
Sentence: We conclude that the dipyridamole ECG test is as useful as the exercise ECG test for the assessment of coronary artery disease .

## Item bc5cdr:test:808
Example input:
Sentence: After the administration of NG , 5-FU and CY neither a statistically significant increase in creatinine concentration nor an increase in creatinine clearance was observed compared to the group receiving no cytostatics .

Example answer:
{"entities": [{"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: These data suggest that during concomitant treatment with cinacalcet , dose adjustment may be necessary for drugs that demonstrate a narrow therapeutic index and are metabolized by CYP2D6 .

Example answer:
{"entities": [{"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: Following polytherapy according to the CMF regimen , a statistically significant decrease ( p = 0.0343 ) in creatinine clearance was found , but creatinine concentration did not increase significantly compared to controls .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Multiple cytotoxic drug administration is the generally accepted treatment of patients with a high-risk stage of choriocarcinoma .

Example answer:
{"entities": [{"text": "choriocarcinoma", "type": "Disease"}]}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: Cardiac toxicity is a major complication which limits the use of adriamycin as a chemotherapeutic agent .

Example answer:
{"entities": [{"text": "Cardiac toxicity", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Although a dose-response effect has been observed with cisplatin , the dose-limiting toxicities associated with cisplatin ( e.g. , nephrotoxicity , ototoxicity , and neurotoxicity ) have limited its use as a treatment for breast carcinoma .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "toxicities", "type": "Disease"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "ototoxicity", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "breast carcinoma", "type": "Disease"}]}

Example input:
Sentence: Incidence of transient cyclophosphamide-related cardiac toxicity ( 10 % ) is comparable to previous recorded literature .

Example answer:
{"entities": [{"text": "cyclophosphamide-related", "type": "Chemical"}, {"text": "cardiac toxicity", "type": "Disease"}]}

Example input:
Sentence: Cardiac toxicity observed in association with high-dose cyclophosphamide-based chemotherapy for metastatic breast cancer .

Example answer:
{"entities": [{"text": "Cardiac toxicity", "type": "Disease"}, {"text": "cyclophosphamide-based", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Input:
Sentence: Since chemotherapeutic agent toxicity generally correlates with dose per body surface area , we retrospectively calculated the dose of CYA in patients transplanted at our institution to determine whether the incidence of CYA cardiotoxicity correlated with the dose per body surface area .

## Item bc5cdr:test:912
Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: METHODS : The expression of MRP2 and Pgp in brain and liver sections of TR ( - ) rats and normal Wistar rats was determined with immunohistochemistry , by using a novel , highly selective monoclonal MRP2 antibody and the monoclonal Pgp antibody C219 , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: High levels of matrix Gla protein are found at sites of artery calcification in rats treated with vitamin D plus Warfarin , and chemical analysis showed that the protein that accumulated was indeed not gamma-carboxylated .

Example answer:
{"entities": [{"text": "artery calcification", "type": "Disease"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "Warfarin", "type": "Chemical"}, {"text": "gamma-carboxylated", "type": "Chemical"}]}

Example input:
Sentence: TR ( - ) rats exhibited a significant up-regulation of Pgp in brain capillary endothelial cells compared with wild-type controls .

Example answer:
{"entities": []}

Example input:
Sentence: Experiments with systemic administration of the Pgp substrate phenobarbital and the selective Pgp inhibitor tariquidar in TR ( - ) rats substantiated that Pgp is functional and compensates for the lack of MRP2 in the BBB .

Example answer:
{"entities": [{"text": "phenobarbital", "type": "Chemical"}, {"text": "tariquidar", "type": "Chemical"}]}

Example input:
Sentence: A comparable overexpression of Pgp in the BBB was obtained after pilocarpine-induced seizures in wild-type Wistar rats .

Example answer:
{"entities": [{"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The data on TR ( - ) rats indicate that Pgp plays an important role in the compensation of MRP2 deficiency in the BBB .

Example answer:
{"entities": []}

Example input:
Sentence: PG-9 was also able to increase the amount of NGF secreted in vitro by astrocytes in a dose-dependent manner .

Example answer:
{"entities": []}

Example input:
Sentence: An autoradiographic study was performed on male F-344 rats fed diet containing FANFT at a level of 0.2 % and/or aspirin at a level of 0.5 % to evaluate the effect of aspirin on the increased cell proliferation induced by FANFT in the forestomach and bladder .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Input:
Sentence: PGF2 alpha was also significantly higher in the outer medulla of jj rats with and without aspirin administration ( p less than 0.05 ) .

## Item bc5cdr:test:847
Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: Thirty minutes after 99mTc-glucarate administration the standardised heart uptake value S ( h ) UV was 4.7 in infarcted rat heart which is six times more than in normal rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}]}

Example input:
Sentence: Dopamine turnover ratios ( DOPAC : DA and HVA : DA ) were found to be lower in those animals exposed to the exploratory box when compared to their home cage counterparts .

Example answer:
{"entities": [{"text": "Dopamine", "type": "Chemical"}, {"text": "DOPAC", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "HVA", "type": "Chemical"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: At termination of the experiments , mice underwent echocardiography , quantitation of abundance of molecular markers of CM ( ventricular mRNA encoding atrial natriuretic factor [ ANF ] and sarcoplasmic calcium ATPase [ SERCA2 ] ) , and determination of plasma LA .

Example answer:
{"entities": [{"text": "CM", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "LA", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: Myocardial levels of VIP were assayed before and after the development of heart failure in two canine models .

## Item bc5cdr:test:890
Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: They showed significantly more rapid improvement of motor function in the first week following hemorrhage and better memory retention in the passive avoidance test .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: OUTCOME : Following discontinuation of LEV , EEG and neuropsychological findings improved and seizure frequency decreased .

Example answer:
{"entities": [{"text": "LEV", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: All three had been diagnosed earlier with epilepsy , and their electroencephalogram ( EEG ) findings were abnormal .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}]}

Example input:
Sentence: An electroencephalogram showed continuous , generalized irregular slowing with admixed periodic triphasic waves indicating symptomatic encephalopathy .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Repeated cerebral perfusion SPECT scans revealed decreased basal ganglia perfusion while the movement disorder was present , and a return to normal perfusion when the rabbit syndrome resolved .

Example answer:
{"entities": [{"text": "decreased basal ganglia perfusion", "type": "Disease"}, {"text": "movement disorder", "type": "Disease"}, {"text": "rabbit syndrome", "type": "Disease"}]}

Example input:
Sentence: The EEG shows characteristic triphasic waves in most patients with this complication .

Example answer:
{"entities": []}

Example input:
Sentence: The interictal electroencephalogram ( EEG ) showed a generalized slowing to 5 per second theta rhythms with bilateral generalized high-amplitude discharges .

Example answer:
{"entities": []}

Input:
Sentence: Improvement of abnormal EEG was noticed in 76 % of diffuse paroxysms and in 67 % of focal paroxysms .

## Item bc5cdr:test:893
Example input:
Sentence: In both cases normal plasma and urinary free cortisol levels had been achieved following ketoconazole therapy , yet continuous blood pressure monitoring demonstrated hypertension 31 ( patient 1 ) and 52 weeks ( patient 2 ) after treatment .

Example answer:
{"entities": [{"text": "cortisol", "type": "Chemical"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Ximelagatran , an oral direct thrombin inhibitor , was found to be as efficient as vitamin K antagonist drugs in the prevention of embolic events , but has been recently withdrawn because of abnormal liver function tests .

Example answer:
{"entities": [{"text": "Ximelagatran", "type": "Chemical"}, {"text": "vitamin K", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}, {"text": "abnormal liver function", "type": "Disease"}]}

Example input:
Sentence: Patients who received enalapril experienced clinically and statistically significantly less symptomatic hypotension ( 5.2 % ) than the patients who received prazosin ( 12.9 % ) .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}]}

Example input:
Sentence: The timolol-treated patients showed a small but significant increase in heart size from baseline in contrast to a decrease in the placebo group .

Example answer:
{"entities": [{"text": "timolol-treated", "type": "Chemical"}]}

Example input:
Sentence: Design and analysis of the HYPREN-trial : safety of enalapril and prazosin in the initial treatment phase of patients with congestive heart failure .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "prazosin", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: METHOD : prospective study with 137 patients that underwent TEE with MZ associated to moderate sedation .

Example answer:
{"entities": [{"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: Eight glaucomatous patients chronically treated with timolol 0.5 % /12h , suffering from depression diagnosed through DMS-III-R criteria , were included in the study .

Example answer:
{"entities": [{"text": "glaucomatous", "type": "Disease"}, {"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: To assess the safety of the ACE inhibitor enalapril a multicenter , randomized , prazosin-controlled trial was designed that compared the incidence and severity of symptomatic hypotension on the first day of treatment .

Example answer:
{"entities": [{"text": "ACE inhibitor", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "prazosin-controlled", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The effect of long-term timolol treatment on heart size after myocardial infarction was evaluated by X-ray in a double-blind study including 241 patients ( placebo 126 , timolol 115 ) .

Example answer:
{"entities": [{"text": "timolol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In a double blind cross-over study with control group , the patients under timolol treatment presented higher depression values measured through the Beck and the Zung-Conde scales ( p < 0.001 vs control ) .

Example answer:
{"entities": [{"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Input:
Sentence: Postmarketing study of timolol-hydrochlorothiazide antihypertensive therapy .

## Item bc5cdr:test:922
Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Our results suggest that addition of phenylephrine to nitroglycerin is not beneficial in the treatment of patients with acute myocardial infarction .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}, {"text": "acute myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Due to the risk of this tachycardia inducing myocardial ischemia , we would not recommend the use in elderly patients of any of the ephedrine/propofol/mixtures studied .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "ephedrine/propofol/mixtures", "type": "Chemical"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "drowsiness", "type": "Disease"}]}

Example input:
Sentence: Since the cranial condition precluded use of more usual methods , lidocaine was given intra-arterially , with careful cardiovascular monitoring , to counteract the vasospasm .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "vasospasm", "type": "Disease"}]}

Example input:
Sentence: Reduction in injection pain using buffered lidocaine as a local anesthetic before cardiac catheterization .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: The patient had no apparent associated conditions which might have predisposed him to the development of bradyarrhythmias ; and , thus , this probably represented a true idiosyncrasy to lidocaine .

Example answer:
{"entities": [{"text": "bradyarrhythmias", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Input:
Sentence: We can not advocate the administration of lidocaine prophylactically in the early hours of suspected myocardial infarction .

## Item bc5cdr:test:935
Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: By implantation of electrodes and electrophysiological recording in vivo , the results showed that Rg1 restored the long-term potentiation ( LTP ) impaired by morphine in both freely moving and anaesthetised rats .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: In Group 1 the rats were trained under the influence of pentobarbital to run to the same shelf as in the normal state .

Example answer:
{"entities": [{"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: They suggest that , in normal conscious rats , the central tachycardia of bromocriptine appears to predominate and to mask the bradycardia of this agonist at peripheral dopamine D2 receptors .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "bromocriptine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: The [ verapamil ] o that arrested atrial beating ( AC ) was also potentiated with the order LNa = LNa+LCa = LNa+HCa = LCa > HCa = N. The results indicate that rat atrial spontaneous beating is more dependent on [ Na ] o than on [ Ca ] o in a range of +/- 50 % of their normal concentration .

Example answer:
{"entities": [{"text": "verapamil", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: The effects of varying the extracellular concentrations of Na and Ca ( [ Na ] o and [ Ca ] o ) on both , the spontaneous beating and the negative chronotropic action of verapamil , were studied in the isolated rat atria .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: In control rats , intravenous bromocriptine ( 150 microg/kg ) induced significant hypotension and tachycardia .

Example answer:
{"entities": [{"text": "bromocriptine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}]}

Input:
Sentence: Under barbiturate anesthesia , virtually all of the myocardial contractile indices were depressed significantly in barium-exposed rats relative to the corresponding control-fed rats .

## Item bc5cdr:test:633
Example input:
Sentence: Adriamycin-induced autophagic cardiomyocyte death plays a pathogenic role in a rat model of heart failure .

Example answer:
{"entities": [{"text": "Adriamycin-induced", "type": "Chemical"}, {"text": "death", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: This study assessed the ability of IH636 grape seed proanthocyanidin extract ( GSPE ) to prevent acetaminophen ( AAP ) -induced nephrotoxicity , amiodarone ( AMI ) -induced lung toxicity , and doxorubicin ( DOX ) -induced cardiotoxicity in mice .

Example answer:
{"entities": [{"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}, {"text": "GSPE", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "AAP", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: From these results , we conclude that ribavirin has an antiviral effect in advanced cases of AHF , and that anemia , the only secondary reaction observed , can be easily managed .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "AHF", "type": "Disease"}, {"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to investigate whether autophagy was involved in the progression of heart failure induced by adriamycin , so that we can develop a novel treatment strategy for heart failure .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Amifostine subsequently was shown to protect normal tissues from the toxic effects of alkylating agents and cisplatin without decreasing the antitumor effect of the chemotherapy .

Example answer:
{"entities": [{"text": "Amifostine", "type": "Chemical"}, {"text": "alkylating agents", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: A possible involvement of energy metabolism was suggested previously , and in this study the adenylate energy charge and phosphorylcreatine mole fraction were determined in the adriamycin-treated cells .

Example answer:
{"entities": [{"text": "phosphorylcreatine", "type": "Chemical"}, {"text": "adriamycin-treated", "type": "Chemical"}]}

Example input:
Sentence: Nitro-L-arginine methyl ester : a potential protector against gentamicin ototoxicity .

Example answer:
{"entities": [{"text": "Nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "ototoxicity", "type": "Disease"}]}

Example input:
Sentence: Acetaminophen ( up to 150 micrograms/mL ) did not retard the incorporation of radioactive adenosine into ATP in slices of rat cerebral cortex .

Example answer:
{"entities": [{"text": "Acetaminophen", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Example input:
Sentence: In the adriamycin-treated cells , the addition of adenosine increased the adenylate charge and , concomitant with this inrcease , the cells ' functional integrity , in terms of percentage of beating cells and rate of contractions , was maintained .

Example answer:
{"entities": [{"text": "adriamycin-treated", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}]}

Input:
Sentence: The lack of any consistent protective effect noted with the alkylxanthines tested in the present study indicates that adenosine plays little , if any , pathophysiological role in gentamicin-induced ARF .

## Item bc5cdr:test:749
Example input:
Sentence: Doxorubicin treatment resulted in heavy proteinuria ( > 100 mg protein/mg crea ) in 15/44 of sgk1 ( +/+ ) and 15/44 of sgk1 ( -/- ) mice leading to severe nephrotic syndrome with ascites , lipidemia , and hypoalbuminemia in both genotypes .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "proteinuria", "type": "Disease"}, {"text": "nephrotic syndrome", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "lipidemia", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}]}

Example input:
Sentence: Baseline renal ACE positively correlated with the relative rise in proteinuria after adriamycin ( r = 0.62 , P < 0.01 ) , renal interstitial alpha-smooth muscle actin ( r = 0.49 , P < 0.05 ) , interstitial macrophage influx ( r = 0.56 , P < 0.05 ) , interstitial collagen III ( r = 0.53 , P < 0.05 ) , glomerular alpha-smooth muscle actin ( r = 0.74 , P < 0.01 ) and glomerular desmin ( r = 0.48 , P < 0.05 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : As anticipated , adriamycin elicited nephrotic range proteinuria , renal interstitial damage and mild focal glomerulosclerosis .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal interstitial damage", "type": "Disease"}, {"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: In this study , 62 patients with confirmed initial normal renal function and treated with 2 to 5 mg/kg/day of gentamicin sulfate or tobramycin sulfate for a minimum of seven days were followed up prospectively for the development of aminoglycoside-related renal failure , defined as at least a one-third reduction in renal function .

Example answer:
{"entities": [{"text": "gentamicin sulfate", "type": "Chemical"}, {"text": "tobramycin sulfate", "type": "Chemical"}, {"text": "aminoglycoside-related", "type": "Chemical"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Input:
Sentence: The enhancement of aminonucleoside nephrosis by the co-administration of protamine .

## Item bc5cdr:test:947
Example input:
Sentence: Pretreatment with either VPU ( 50 and 100 mg/kg ) or VPA ( 300 and 600 mg/kg ) completely abolished pilocarpine-evoked increases in extracellular glutamate and aspartate .

Example answer:
{"entities": [{"text": "VPU", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}, {"text": "pilocarpine-evoked", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: After administration of phenylephrine , MAP increased ( 51 +/- 12 to 81 +/- 13 mmHg ; P < 0.001 ; mean +/- SD ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: Systolic blood pressure was elevated by an average of 7 mm Hg .

Example answer:
{"entities": []}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: An initial dose of 0.1 microgram.kg-1.min-1 of PGE1 ( 15 patients ) , or 10 micrograms.kg-1.min-1 of TMP ( 15 patients ) was administered intravenously after the dural opening and the dose was adjusted to maintain the mean arterial blood pressure ( MAP ) at about 60 mmHg .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: d-1 given for 4 weeks , elevated blood pressure from 102+/-13 to 152+/-15 mm Hg and increased the synthesis of ET-1 and the levels of ET-1 mRNA in the mesenteric artery ( 240 % and 230 % , respectively ) .

Example answer:
{"entities": []}

Input:
Sentence: PPA , 75 mg alone , increased blood pressure ( 31 +/- 14 mm Hg systolic , 20 +/- 5 mm Hg diastolic ) , and propranolol pretreatment antagonized this increase ( 12 +/- 10 mm Hg systolic , 10 +/- 7 mm Hg diastolic ) .

## Item bc5cdr:test:1168
Example input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

Example answer:
{"entities": []}

Example input:
Sentence: In inflamed preparations , the muscarinic receptor antagonism on the phasic component of the electrical field stimulation-evoked contraction was decreased and the pirenzepine and 4-DAMP antagonism on the tonic component was much less efficient than in controls .

Example answer:
{"entities": [{"text": "pirenzepine", "type": "Chemical"}, {"text": "4-DAMP", "type": "Chemical"}]}

Example input:
Sentence: End-diastolic ( ED ) and end-systolic ( ES ) LV diameters/BW significantly increased , whereas LV FS was decreased after 9 weeks in the DOX group ( p < 0.001 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Example input:
Sentence: By using transthoracic echocardiography , anterior and posterior wall thickness , LV diameters and LV fractional shortening ( FS ) were measured in all rats before DOX or saline , and at weeks 6 and 9 after treatment in all surviving rats .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: It is concluded that increases in the SPV and the delta down are characteristic of a hypotensive state due to a predominant decrease in preload .

Example answer:
{"entities": [{"text": "hypotensive", "type": "Disease"}]}

Example input:
Sentence: After recovery from hypertension , the activity of ( Na , K ) -ATPase increased , due to higher affinity of the ATP-binding site , as revealed from the lowered Km value for ATP .

Example answer:
{"entities": [{"text": "hypertension", "type": "Disease"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "ATP-binding", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: As a consequence of blocking I ( f ) , clonidine reduced the slope of the diastolic depolarization and the frequency of pacemaker potentials in sinoatrial node cells from wild-type and alpha2ABC-knockout mice .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Input:
Sentence: This effect , which results in a flattening of the phase 0 and phase 4 slope , together with a longer AP duration , may be due to an increase in the time constants of slow inward ionic currents ( already demonstrated elsewhere ) , but also to an increased time constant for deactivation of the outward potassium current ( Ip ) .

## Item bc5cdr:test:1025
Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: Every patient was screened for testosterone and 451 were screened for prolactin on the basis of low sexual desire , gynecomastia or testosterone less than 4 ng./ml .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}]}

Example input:
Sentence: Hysterosalpingography was performed on both patients and , in 1 instance , an abnormal x-ray film was reflected by the gross appearance of the uterine cavity found in the surgical specimen .

Example answer:
{"entities": []}

Example input:
Sentence: After her strength returned , repetitive stimulation was normal , but single fiber EMG revealed increased jitter and blocking .

Example answer:
{"entities": []}

Example input:
Sentence: Laryngeal electromyography ( thyroarytenoid muscle ) showed ample denervation potentials .

Example answer:
{"entities": []}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Input:
Sentence: Themography confirmed the existence of an excessive breast stimulation in 1 women who complained of moderate mastodynia and in 5 of the 7 women who complained of severe mastodynia .

## Item bc5cdr:test:1189
Example input:
Sentence: Alpha2ABC-/- mice were completely unresponsive to the analgesic and hypnotic effects of clonidine ; however , clonidine significantly lowered heart rate in alpha2ABC-/- mice by up to 150 bpm .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: Effects of acetylsalicylic acid , dipyridamole , and hydrocortisone on epinephrine-induced myocardial injury in dogs .

Example answer:
{"entities": [{"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine-induced", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: The effects of continuous positive airway pressure ( CPAP ) on cardiovascular dynamics and pulmonary shunt ( QS/QT ) were investigated in 12 dogs before and during sodium nitroprusside infusion that decreased mean arterial blood pressure 40-50 per cent .

Example answer:
{"entities": [{"text": "sodium nitroprusside", "type": "Chemical"}]}

Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: UM-272 ( N , N-dimethylpropranolol ) , a quaternary antiarrhythmic agent , was administered sublingually to dogs with ouabain-induced ventricular tachycardias .

Example answer:
{"entities": [{"text": "UM-272", "type": "Chemical"}, {"text": "N , N-dimethylpropranolol", "type": "Chemical"}, {"text": "ouabain-induced", "type": "Chemical"}, {"text": "ventricular tachycardias", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Therefore , we studied the hyperemic response to dipyridamole in seven open-chest anesthetized dogs after pretreatment with either pentoxifylline ( 0 , 7.5 , or 15 mg/kg i.v . )

Example answer:
{"entities": [{"text": "dipyridamole", "type": "Chemical"}, {"text": "pentoxifylline", "type": "Chemical"}]}

Example input:
Sentence: Upon rechallenge with either cephalosporin , the hematologic syndrome was reproduced in most dogs tested ; cefonicid ( but not cefazedone ) -treated dogs showed a substantially reduced induction period ( 15 +/- 5 days ) compared to that of the first exposure to the drug ( 61 +/- 24 days ) .

Example answer:
{"entities": [{"text": "cephalosporin", "type": "Chemical"}, {"text": "hematologic syndrome", "type": "Disease"}, {"text": "cefonicid", "type": "Chemical"}, {"text": "cefazedone", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Input:
Sentence: We investigated how these two drugs act on the cardiovascular systems of 20 dogs whose hearts had been denervated by a procedure we had devised .

## Item bc5cdr:test:1201
Example input:
Sentence: The differences in mortality and morbidity between the two groups were not significant .

Example answer:
{"entities": []}

Example input:
Sentence: However , age was seen to interfere with the responses exhibited by the young and old rats .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The patients in the study group were significantly younger than the patients in the control group ( P < 0.002 ) .

Example answer:
{"entities": []}

Example input:
Sentence: For almost all cognitive measures , there were no medication by age-interaction effects , which indicates that the 2 age groups exhibited similar responses to the medication challenge .

Example answer:
{"entities": []}

Example input:
Sentence: Therefore , old age may be a risk factor for developing this complication .

Example answer:
{"entities": []}

Example input:
Sentence: Older subjects tended to display more side effects .

Example answer:
{"entities": []}

Example input:
Sentence: Older age was significantly correlated with the CHF development ; with median ages for the entire group and for patients developing CHF of 45 and 59 , respectively .

Example answer:
{"entities": [{"text": "CHF", "type": "Disease"}]}

Example input:
Sentence: The occurrence of this ADR was more frequent in patients aged between 61 and 80 years .

Example answer:
{"entities": []}

Example input:
Sentence: This age group had an increased risk of myelosuppression .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}]}

Example input:
Sentence: These differences were not observed during puberty .

Example answer:
{"entities": []}

Input:
Sentence: These differences occur especially in the age groups under 30 years .

## Item bc5cdr:test:977
Example input:
Sentence: MPEP administered into the striatum at high concentrations ( 500 microM ) increased extracellular dopamine levels , while lower concentrations ( 50-100 microM ) were devoid of any effect .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: The correlation between neuropathic damage and inhibition of neurotoxic esterase or neuropathy target enzyme ( NTE ) was examined in rats acutely exposed to Mipafox ( N , N'-diisopropylphosphorodiamidofluoridate ) , a neurotoxic organophosphate .

Example answer:
{"entities": [{"text": "neuropathic damage", "type": "Disease"}, {"text": "neurotoxic", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "Mipafox", "type": "Chemical"}, {"text": "N , N'-diisopropylphosphorodiamidofluoridate", "type": "Chemical"}, {"text": "organophosphate", "type": "Chemical"}]}

Example input:
Sentence: In addition , glomerular size was higher in the nitrendipine-treated group ( 14.9 +/- 0.17 10 ( -3 ) mm2 ) but lower in the enalapril-treated group ( 11.5 +/- 0.15 10 ( -3 ) mm2 ) compared with the hypertensive controls ( 12.1 +/- 0.17 10 ( -3 ) mm2 ) .

Example answer:
{"entities": [{"text": "nitrendipine-treated", "type": "Chemical"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: On the other hand , BNP did not increase in the patients without heart failure given DNR , even at more than 700 mg/m ( 2 ) .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "DNR", "type": "Chemical"}]}

Example input:
Sentence: We measured the plasma level of brain natriuretic peptide ( BNP ) to determine whether BNP might serve as a simple diagnostic indicator of anthracycline-induced cardiotoxicity in patients with acute leukemia treated with a daunorubicin ( DNR ) -containing regimen .

Example answer:
{"entities": [{"text": "anthracycline-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "acute leukemia", "type": "Disease"}, {"text": "daunorubicin", "type": "Chemical"}, {"text": "DNR", "type": "Chemical"}]}

Example input:
Sentence: At day 5 , GLEPP1 protein and mRNA were reduced from the normal range ( 265.2 +/- 79.6 x 10 ( 6 ) moles/glomerulus and 100 % ) to 15 % of normal ( 41.8 +/- 4.8 x 10 ( 6 ) moles/glomerulus , p < 0.005 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In both types , purinoceptor desensitization with alpha , beta-methylene adenosine-5'-triphosphate ( alpha , beta-meATP ) caused further reductions at low frequencies ( < 10 Hz ) .

Example answer:
{"entities": [{"text": "alpha , beta-methylene adenosine-5'-triphosphate", "type": "Chemical"}, {"text": "alpha , beta-meATP", "type": "Chemical"}]}

Example input:
Sentence: The plasma levels of BNP in all the patients with clinical and subclinical heart failure increased above the normal limit ( 40 pg/ml ) before the detection of clinical or subclinical heart failure by radionuclide angiography .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}]}

Example input:
Sentence: Acetaminophen ( up to 150 micrograms/mL ) did not retard the incorporation of radioactive adenosine into ATP in slices of rat cerebral cortex .

Example answer:
{"entities": [{"text": "Acetaminophen", "type": "Chemical"}, {"text": "adenosine", "type": "Chemical"}, {"text": "ATP", "type": "Chemical"}]}

Example input:
Sentence: GLEPP1 receptor tyrosine phosphatase ( Ptpro ) in rat PAN nephrosis .

Example answer:
{"entities": [{"text": "tyrosine", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Input:
Sentence: BNPP ( 1 to 8 mM ) reduced APAP deacetylation and covalent binding in F344 renal cortical homogenates in a concentration-dependent manner .

## Item bc5cdr:test:984
Example input:
Sentence: Pretreatment of mice with alpha-methyltyrosine ( 20 mg/kg i.p. , one hour ) , an inhibitor of tyrosine hydroxylase , significantly decreased the activity-increasing effects of morphine .

Example answer:
{"entities": [{"text": "alpha-methyltyrosine", "type": "Chemical"}, {"text": "tyrosine", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: The morphine-induced hyperactivity was potentiated by scopolamine and attenuated by physostigmine .

Example answer:
{"entities": [{"text": "morphine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "physostigmine", "type": "Chemical"}]}

Example input:
Sentence: Rats treated for 11 days with morphine and withdrawn for 36-40 h showed differences in the development of tolerance : about half of the animals showed a rigidity after the test dose of morphine that was not significantly less than in the controls and were akinetic ( A group ) .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "rigidity", "type": "Disease"}, {"text": "akinetic", "type": "Disease"}]}

Example input:
Sentence: The results suggest that rigidity , which is assumed to be due to an action of morphine in the striatum , can be antagonized by another process leading to dopaminergic activation in the striatum .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: The study suggests that the activity-increasing effects of morphine are mediated by the release of catecholamines from adrenergic neurons in the brain .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "catecholamines", "type": "Chemical"}]}

Example input:
Sentence: And the results are consistent with the hypothesis that morphine acts by retarding the release of acetylcholine at some central cholinergic synapses .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "acetylcholine", "type": "Chemical"}]}

Example input:
Sentence: The development of tolerance to the muscular rigidity produced by morphine was studied in rats .

Example answer:
{"entities": [{"text": "muscular rigidity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: Neonatal pyridoxine responsive convulsions due to isoniazid therapy .

Example answer:
{"entities": [{"text": "pyridoxine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: Fentanyl , an opioid analgesic , is frequently used in the neonatal intensive care unit setting for these very purposes .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "Chemical"}]}

Example input:
Sentence: Amnesia produced by scopolamine and cycloheximide were reversed by morphine given 30 min before the test trial ( pre-test ) , and pre-test morphine also facilitated the memory retrieval in the animals administered naloxone during the training trial .

Example answer:
{"entities": [{"text": "Amnesia", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}]}

Input:
Sentence: Morphine-induced seizures in newborn infants .

## Item bc5cdr:test:985
Example input:
Sentence: All of the rats in the saline-treated epileptic control group developed SRS , whereas none of the BMC-treated epileptic animals had seizures in the short term ( 15 days after transplantation ) , regardless of the BMC source .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "SRS", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Sedation has been commonly used in the neonate to decrease the stress and pain from the noxious stimuli and invasive procedures in the neonatal intensive care unit , as well as to facilitate synchrony between ventilator and spontaneous breaths .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}]}

Example input:
Sentence: We describe a case of transient neurological deficit that occurred after unilateral spinal anaesthesia with 8 mg of 1 % hyperbaric bupivacaine slowly injected through a 25-gauge pencil-point spinal needle .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Amnesia produced by scopolamine and cycloheximide were reversed by morphine given 30 min before the test trial ( pre-test ) , and pre-test morphine also facilitated the memory retrieval in the animals administered naloxone during the training trial .

Example answer:
{"entities": [{"text": "Amnesia", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "cycloheximide", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "naloxone", "type": "Chemical"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: infusion of morphine ( mean 73.6 mg ) and five patients receiving a continuous extradural infusion of 0.25 % bupivacaine ( mean 192 mg ) in the 24-h period following upper abdominal surgery .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: In this study , the severity of response to other seizure-inducing agents was tested in mice 1 and 24 h after intraperitoneal administration of 80 mg/kg gamma-HCH .

Example answer:
{"entities": [{"text": "seizure-inducing", "type": "Disease"}, {"text": "gamma-HCH", "type": "Chemical"}]}

Example input:
Sentence: Fentanyl , an opioid analgesic , is frequently used in the neonatal intensive care unit setting for these very purposes .

Example answer:
{"entities": [{"text": "Fentanyl", "type": "Chemical"}]}

Input:
Sentence: Two neonates suffered from generalized seizures during the course of intravenous morphine sulfate for post-operative analgesia .

## Item bc5cdr:test:911
Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Therefore , like VPA , the finding that VPU could drastically reduce pilocarpine-induced increases in glutamate and aspartate should account , at least partly , for its anticonvulsant activity observed in pilocarpine-induced seizure in experimental animals .

Example answer:
{"entities": [{"text": "VPA", "type": "Chemical"}, {"text": "VPU", "type": "Chemical"}, {"text": "pilocarpine-induced", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: An autoradiographic study was performed on male F-344 rats fed diet containing FANFT at a level of 0.2 % and/or aspirin at a level of 0.5 % to evaluate the effect of aspirin on the increased cell proliferation induced by FANFT in the forestomach and bladder .

Example answer:
{"entities": [{"text": "FANFT", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: Effect of aspirin on N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ] -formamide-induced epithelial proliferation in the urinary bladder and forestomach of the rat .

Example answer:
{"entities": [{"text": "aspirin", "type": "Chemical"}, {"text": "N- [ 4- ( 5-nitro-2-furyl ) -2-thiazolyl ]", "type": "Chemical"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Input:
Sentence: Aspirin treatment reduced PGE2 synthesis in all regions , but outer medullary PGE2 remained higher in jj ( 18 +/- 3 ) than jJ rats ( 9 +/- 2 ) ( p less than 0.05 ) .

## Item bc5cdr:test:1223
Example input:
Sentence: At normal [ Na ] o , decrease ( 0.675 mM ) or increase ( 3.6 mM ) of [ Ca ] o did not modify BF ; a reduction of ten times ( 0.135 mM of normal [ Ca ] o was effective to reduce BF by 40 +/- 13 % .

Example answer:
{"entities": [{"text": "Na", "type": "Chemical"}, {"text": "Ca", "type": "Chemical"}]}

Example input:
Sentence: The drug was withdrawn on presentation to hospital in 11 patients , with rapid clinical improvement in 9 .

Example answer:
{"entities": []}

Example input:
Sentence: The majority of patients ( > 60 % ) experienced no change in their disease status from baseline .

Example answer:
{"entities": []}

Example input:
Sentence: Lipid peroxidation in homogenates was maximal at day 3 and declined rapidly to control levels by day 17 .

Example answer:
{"entities": []}

Example input:
Sentence: Significant declines in simple and sustained attention , working memory , and verbal memory were observed at 1 hour postdose compared to baseline for both age groups with a trend toward return to baseline by 5 hours postdose .

Example answer:
{"entities": []}

Example input:
Sentence: However , a 14 % ( from 70 +/- 8 % to 60 +/- 7 % ) reduction in S ( c ) O ( 2 ) ( P < 0.05 ) followed with no change in CO ( 3.7 +/- 1.1 to 3.4 +/- 0.9 l min ( -1 ) ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

Example answer:
{"entities": []}

Example input:
Sentence: At day 5 , GLEPP1 protein and mRNA were reduced from the normal range ( 265.2 +/- 79.6 x 10 ( 6 ) moles/glomerulus and 100 % ) to 15 % of normal ( 41.8 +/- 4.8 x 10 ( 6 ) moles/glomerulus , p < 0.005 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The rigidity was considerably decreased in both groups after 20 days ' treatment .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}]}

Example input:
Sentence: Ninety-nine percent ( sixty-eight ) of the sixty-nine parents present during the reduction were pleased with the sedation and would allow it to be used again in a similar situation .

Example answer:
{"entities": []}

Input:
Sentence: At 1 day their number was reduced to about 1/10 of the original number .

## Item bc5cdr:test:1224
Example input:
Sentence: Urinary volume and serum creatinine levels recovered to the normal range , with urinary protein disappearing completely within 40 days .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Her aminotransferase levels returned to normal by postoperative day 23 , and her 2-year follow-up showed no adverse events .

Example answer:
{"entities": []}

Example input:
Sentence: The patient recovered within 1 week following discontinuation of antianginal therapy .

Example answer:
{"entities": []}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Flow and metabolism were measured 5-13 days after the subarachnoid haemorrhage by a modification of the classical Kety-Schmidt technique using xenon-133 i.v .

Example answer:
{"entities": [{"text": "subarachnoid haemorrhage", "type": "Disease"}, {"text": "xenon-133", "type": "Chemical"}]}

Example input:
Sentence: The rigidity was considerably decreased in both groups after 20 days ' treatment .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}]}

Example input:
Sentence: Bone marrow recovery and peripheral blood recovery were complete 1 month and 3 months , respectively , after treatment , and blood transfusion or other therapies were not necessary in a follow-up period of more than 2 years .

Example answer:
{"entities": []}

Example input:
Sentence: Hepatitis was usually reversible when treatment was stopped , with the results of liver function tests returning to normal after an average of 3.1 months .

Example answer:
{"entities": [{"text": "Hepatitis", "type": "Disease"}]}

Example input:
Sentence: All three cytopenias were completely reversible following cessation of treatment ; the time required for recovery of the erythron ( approximately 1 month ) was considerably longer than that of the granulocytes and platelets ( hours to a few days ) .

Example answer:
{"entities": [{"text": "cytopenias", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Input:
Sentence: By 7 days the vessel was almost restored to normal .

## Item bc5cdr:test:1226
Example input:
Sentence: Acute normal tissue toxicities ( i.e. , leukopenia and thrombocytopenia ) and late normal tissue toxicities ( i.e. , myocardial and kidney injury ) were evaluated by functional/physiological assays and by morphological techniques .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "leukopenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: Inflammatory cells are postulated to mediate some of the brain damage following ischemic stroke .

Example answer:
{"entities": [{"text": "brain damage", "type": "Disease"}, {"text": "ischemic stroke", "type": "Disease"}]}

Example input:
Sentence: The finding of cocaine-induced vasoconstriction in segments of ( noninnervated ) human umbilical artery suggests that the presence or absence of intact innervation is not sufficient to explain the discrepant data involving the possibility of alpha-mediated effects .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}]}

Example input:
Sentence: In experimental animals excess deposition of collagen and glycoaminoglycans was observed in the subendothelial and medial layer of the aortic wall , together with prominent basal membrane substance around aortic smooth muscle cells .

Example answer:
{"entities": []}

Example input:
Sentence: This study shows that prolonged analgesic treatment in Fischer 344 rats causes progressive and irreversible damage to the interstitial matrix and type 1 interstitial cells leading to RPN .

Example answer:
{"entities": [{"text": "RPN", "type": "Disease"}]}

Example input:
Sentence: Increased sensitivity of the fusimotor system during acute muscle pain could be one likely mechanism to explain the findings .

Example answer:
{"entities": [{"text": "muscle pain", "type": "Disease"}]}

Example input:
Sentence: Pathologically , granular cytoplasmic changes were found in cardiac myocytes , indicating enlarged , damaged mitochondria .

Example answer:
{"entities": []}

Example input:
Sentence: The rapid alternations of rigidity and the signs of dopaminergic activation observed in the animals of the AS/KS group might be due to rapid shifts in the predominance of various DA-innervated structures .

Example answer:
{"entities": [{"text": "rigidity", "type": "Disease"}]}

Example input:
Sentence: Damage to the capillary was accompanied by marked damage to neuroglial cells , mainly to perivascular processes of astrocytes .

Example answer:
{"entities": []}

Input:
Sentence: These findings suggest that smooth muscle cells are susceptible to damage in the course of their specific function .

## Item bc5cdr:test:954
Example input:
Sentence: On the contrary , the cataleptogenic effect of haloperidol was significantly reduced in rats treated with desipramine and 6-OHDA but not in rats treated with 6-OHDA or in rats with lesions of the locus coeruleus .

Example answer:
{"entities": [{"text": "haloperidol", "type": "Chemical"}, {"text": "desipramine", "type": "Chemical"}, {"text": "6-OHDA", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 is over 20,000fold more potent at the dopamine D4.2 receptor compared with the human cloned dopamine D2L receptor .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Furthermore , the effects are mediated through dopamine rather than norepinephrine and do not require the carotid sinus baroreceptors .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}, {"text": "yohimbine", "type": "Chemical"}]}

Example input:
Sentence: In addition , reflex bradycardia caused by injected norepinephrine was significantly enhanced by L-dopa , DL-Threo-dihydroxyphenylserine had no effect on blood pressure , heart rate or reflex responses to norepinephrine .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}, {"text": "DL-Threo-dihydroxyphenylserine", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine significantly reversed the disruption of prepulse inhibition ( PPI ) in rats produced by apomorphine .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "apomorphine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In this study , we evaluated the performance of dopamine beta-hydroxylase knockout ( Dbh -/- ) mice , which lack norepinephrine ( NE ) , in the elevated plus maze ( EPM ) to examine the contribution of noradrenergic signaling to cocaine-induced anxiety .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "NE", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}]}

Example input:
Sentence: The lung weights were lower and PaO2 was improved in rats given this enzyme-blocking agent .

Example answer:
{"entities": []}

Example input:
Sentence: However , L-dopa restored the bradycardia caused by norepinephrine in addition to decreasing blood pressure and heart rate .

Example answer:
{"entities": [{"text": "L-dopa", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}]}

Example input:
Sentence: Phenylpropanolamine ( PPA ) , a synthetic sympathomimetic that is structurally similar to amphetamine , is available over the counter in anorectics , nasal congestants , and cold preparations .

Example answer:
{"entities": [{"text": "Phenylpropanolamine", "type": "Chemical"}, {"text": "PPA", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Input:
Sentence: This is probably because PPA has less beta 2 activity than does norepinephrine .
