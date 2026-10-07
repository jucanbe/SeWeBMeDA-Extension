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

## Item bc5cdr:test:4024
Example input:
Sentence: CASE REPORT : We describe 2 patients who were regular consumers of alcohol and who developed liver failure within 3-5 days after hospitalization and stopping alcohol consumption while being treated with 4 g paracetamol/day .

Example answer:
{"entities": [{"text": "alcohol", "type": "Chemical"}, {"text": "liver failure", "type": "Disease"}, {"text": "paracetamol/day", "type": "Chemical"}]}

Example input:
Sentence: Cancer patients who are chronic carriers of HBV have a higher hepatic complication rate while receiving cytotoxic chemotherapy ( CT ) and this has mainly been attributed to HBV reactivation .

Example answer:
{"entities": [{"text": "Cancer", "type": "Disease"}, {"text": "hepatic complication", "type": "Disease"}]}

Example input:
Sentence: At diagnosis there was no significant difference in OD between HIT patients with thrombosis and those with isolated-HIT .

Example answer:
{"entities": [{"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: Of our control group ( n= 50 ) , 21 patients ( 42 % ) were established hepatitis .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: The results of serum liver function tests suggested hepatocellular injury in 10 ( 63 % ) ; the rest showed a mixed pattern .

Example answer:
{"entities": [{"text": "hepatocellular injury", "type": "Disease"}]}

Example input:
Sentence: INTERPRETATION : Repeated exposure of human beings to HCFCs 123 and 124 can result in serious liver injury in a large proportion of the exposed population .

Example answer:
{"entities": [{"text": "liver injury", "type": "Disease"}]}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: Of the 59 cases , 26 ( 44 % ) had a fatal outcome , compared to 136 ( 25 % ) among the non-warfarin patients ( p < 0.01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Four patients ( 1.7 % ) were identified with toxic hepatitis which could reasonably be attributed to the use of antithyroid agent .

Example answer:
{"entities": [{"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Forty of 94 HIT patients had thrombosis at diagnosis ; 54/94 had isolated-HIT without thrombosis .

Example answer:
{"entities": [{"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Input:
Sentence: CONCLUSIONS : The incidence of HIT in patients with end-stage hepatic failure is , with about 1.95 % , rare .

## Item bc5cdr:test:4092
Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : We found that cocaine dose-dependently increased anxiety-like behavior in control ( Dbh +/- ) mice , as measured by a decrease in open arm exploration .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}]}

Example input:
Sentence: Ecstasy users performed significantly worse in learning and memory compared to controls and cannabis users .

Example answer:
{"entities": [{"text": "Ecstasy", "type": "Chemical"}, {"text": "cannabis", "type": "Chemical"}]}

Example input:
Sentence: It has been consistently shown that ecstasy users display impairments in learning and memory performance .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Cocaine-induced anxiety was also attenuated in Dbh +/- mice following administration of disulfiram , a dopamine beta-hydroxylase ( DBH ) inhibitor .

Example answer:
{"entities": [{"text": "Cocaine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "disulfiram", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Compared with MDMA-free polydrug controls , MDMA polydrug users showed impairments in set shifting and memory updating , and also in social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA-free", "type": "Chemical"}, {"text": "MDMA", "type": "Chemical"}]}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: MDMA polydrug users show process-specific central executive impairments coupled with impaired social and emotional judgement processes .

Example answer:
{"entities": [{"text": "MDMA", "type": "Chemical"}, {"text": "impaired social and emotional judgement processes", "type": "Disease"}]}

Example input:
Sentence: Fifteen polydrug ecstasy users and 15 polydrug non-ecstasy user controls completed a general drug use questionnaire , the Brixton Spatial Anticipation task ( set shifting ) , Backward Digit Span procedure ( memory updating ) , Inhibition of Return ( inhibition ) , an emotional intelligence scale , the Tromso Social Intelligence Scale and the Dysexecutive Questionnaire ( DEX ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Input:
Sentence: CONCLUSIONS : The increases in anxiety and depression are in line with previous observations in recreational ecstasy-polydrug users .

## Item bc5cdr:test:4393
Example input:
Sentence: He had been prescribed telithromycin 400 mg/d PO to treat an upper respiratory tract infection 7 days prior .

Example answer:
{"entities": [{"text": "telithromycin", "type": "Chemical"}, {"text": "upper respiratory tract infection", "type": "Disease"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: After intravenous administration of labetalol , metoprolol and midazolam the patient 's condition improved , and 15 min later he woke up .

Example answer:
{"entities": [{"text": "labetalol", "type": "Chemical"}, {"text": "metoprolol", "type": "Chemical"}, {"text": "midazolam", "type": "Chemical"}]}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: The girl died seven days , the man four weeks after intrathecal injection of vincristine .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}]}

Example input:
Sentence: The fits ceased within 4 hours of administering intramuscular pyridoxine , suggesting an aetiology of pyridoxine deficiency secondary to isoniazid medication .

Example answer:
{"entities": [{"text": "fits", "type": "Disease"}, {"text": "pyridoxine", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : He was treated with intravenous administration of corticosteroids and glycerin for 6 days after the injection .

Example answer:
{"entities": [{"text": "glycerin", "type": "Chemical"}]}

Example input:
Sentence: Despite pharmacological and supportive interventions , laboratory parameters worsened and the patient died 17 hours after admission .

Example answer:
{"entities": []}

Input:
Sentence: Despite immediate intravenous antimicrobial therapy , he succumbed 23 h after the onset .

## Item bc5cdr:test:4207
Example input:
Sentence: 164 patients ( mean age +/- standard deviation [ SD ] 81.6 +/- 6.8 years ) were admitted .

Example answer:
{"entities": []}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: The median age of those patients developing Grade 3-4 neutropenia was significantly higher than that of the remaining patients ( 75 years vs. 72 years ; P = 0.047 ) .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: METHODS : Forty-nine patients with advanced NSCLC were included , 38 of whom were age > /= 70 years and 11 were age < 70 years but who had some contraindication to receiving cisplatin .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: During a 9-year period , we retrospectively collected 27 neurological events ( 11 % ) in as many patients , from 253 children enrolled in the ALL front-line protocol .

Example answer:
{"entities": [{"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Central nervous system ( CNS ) complications during treatment of childhood acute lymphoblastic leukemia ( ALL ) remain a challenging clinical problem .

Example answer:
{"entities": [{"text": "Central nervous system ( CNS ) complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "ALL", "type": "Disease"}]}

Example input:
Sentence: Central nervous system complications during treatment of acute lymphoblastic leukemia in a single pediatric institution .

Example answer:
{"entities": [{"text": "Central nervous system complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Input:
Sentence: A total of 66 children from 16 Pediatric Oncology Group institutions with `` standard-risk '' acute lymphoblastic leukemia , 1.00 to 9.99 years at diagnosis , without evidence of CNS leukemia at diagnosis were enrolled on ACCL0131 : 28 from P9201 and 38 from P9605 .

## Item bc5cdr:test:3811
Example input:
Sentence: This drug occasionally has been associated with acute interstitial nephritis in native kidneys .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: A 14-year-old girl is reported with recurrent , azithromycin-induced , acute interstitial nephritis .

Example answer:
{"entities": [{"text": "azithromycin-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Doxorubicin-induced nephropathy leads to epithelial sodium channel ( ENaC ) -dependent volume retention and renal fibrosis .

Example answer:
{"entities": [{"text": "Doxorubicin-induced", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "sodium", "type": "Chemical"}, {"text": "volume retention", "type": "Disease"}, {"text": "fibrosis", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: Ranitidine-induced acute interstitial nephritis in a cadaveric renal allograft .

Example answer:
{"entities": [{"text": "Ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: We report a case of ranitidine-induced acute interstitial nephritis in a recipient of a cadaveric renal allograft presenting with acute allograft dysfunction within 48 hours of exposure to the drug .

Example answer:
{"entities": [{"text": "ranitidine-induced", "type": "Chemical"}, {"text": "interstitial nephritis", "type": "Disease"}]}

Example input:
Sentence: Recurrent acute interstitial nephritis induced by azithromycin .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}, {"text": "azithromycin", "type": "Chemical"}]}

Example input:
Sentence: Although most cases of antibiotic induced acute interstitial nephritis are benign and self-limited , some patients are at risk for permanent renal injury .

Example answer:
{"entities": [{"text": "interstitial nephritis", "type": "Disease"}, {"text": "renal injury", "type": "Disease"}]}

Input:
Sentence: DISCUSSION : Daptomycin was initiated in our patient secondary to possible nafcillin-induced acute interstitial nephritis and relapsing bacteremia .

## Item bc5cdr:test:4023
Example input:
Sentence: The Receiver Operative Characteristic Curve showed that OD > 1.27 in the isolated-HIT group had a significantly higher chance of developing thrombosis by day 30 .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: Six patients ( 12 % ) had World Health Organization Grade 3-4 neutropenia , 2 patients ( 4 % ) had Grade 3-4 thrombocytopenia , and 2 patients ( 4 % ) had Grade 3 neurotoxicity .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: World Health Organization Grade 3-4 neutropenia and thrombocytopenia occurred in 39.9 % and 11.4 % of patients , respectively .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: However , OD was significantly higher in all patients with thrombosis ( n = 48 , 1.34 +/- 0.89 ) , including isolated-HIT patients who later developed thrombosis within 30 d ( n = 8 , 1.84 +/- 0.64 ) as compared to isolated-HIT patients who did not develop thrombosis ( 0.96 +/- 0.75 ; P = 0.011 and P = 0.008 ) .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Eight of the isolated-HIT patients developed thrombosis within the next 30 d ; thus , a total of 48 patients had thrombosis at day 30 .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: During the study , vitamin B12 and folate levels were significantly higher in group II patients ; however , no differences in hemoglobin , hematocrit , mean corpuscular volume , and white-cell , neutrophil and platelet counts were observed between groups at 3 , 6 , 9 and 12 months .

Example answer:
{"entities": [{"text": "vitamin B12", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Forty of 94 HIT patients had thrombosis at diagnosis ; 54/94 had isolated-HIT without thrombosis .

Example answer:
{"entities": [{"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Input:
Sentence: The platelet count exceeded 100,000/uL in most of the patients ( n = 193 ) at a medium of 7 d. Regarding HIT II , there were four ( 1.95 % ) patients with a background of HIT type II .

## Item bc5cdr:test:4250
Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Direct inhibition of cardiac HCN pacemaker channels contributes to the bradycardic effects of clonidine gene-targeted mice in vivo , and thus , clonidine-like drugs represent novel structures for future HCN channel inhibitors .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}, {"text": "clonidine-like", "type": "Chemical"}]}

Example input:
Sentence: A significant relationship was observed between maximal cTnT and the extent of myocardial morphological changes , and between LV diameters/BW and histological findings .

Example answer:
{"entities": []}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: Evaluation of cardiac troponin I and T levels as markers of myocardial damage in doxorubicin-induced cardiomyopathy rats , and their relationship with echocardiographic and histological findings .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Although there was a discrepancy between the amount of cTnI and cTnT after DOX , probably due to heterogeneity in cross-reactivities of mAbs to various cTnI and cTnT forms , it is likely that cTnT in rats after DOX indicates cell damage determined by the magnitude of injury induced and that cTnT should be a useful marker for the prediction of experimentally induced cardiotoxicity and possibly for cardioprotective experiments .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Among markers of ischemic injury after DOX in rats , cTnT showed the greatest ability to detect myocardial damage assessed by echocardiographic detection and histological changes .

Example answer:
{"entities": [{"text": "ischemic injury", "type": "Disease"}, {"text": "DOX", "type": "Chemical"}, {"text": "myocardial damage", "type": "Disease"}]}

Example input:
Sentence: We investigated the diagnostic value of cTnI and cTnT for the diagnosis of myocardial damage in a rat model of doxorubicin ( DOX ) -induced cardiomyopathy , and we examined the relationship between serial cTnI and cTnT with the development of cardiac disorders monitored by echocardiography and histological examinations in this model .

Example answer:
{"entities": [{"text": "myocardial damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiac disorders", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Cardiac troponins I ( cTnI ) and T ( cTnT ) have been shown to be highly sensitive and specific markers of myocardial cell injury .

Example answer:
{"entities": [{"text": "myocardial cell injury", "type": "Disease"}]}

Input:
Sentence: AIMS : To investigate whether alterations of myocardial strain and high-sensitive cardiac troponin T ( cTnT ) could predict future cardiac dysfunction in patients after epirubicin exposure .

## Item bc5cdr:test:4256
Example input:
Sentence: Analysis was performed on 61 women with chemotherapy-responsive metastatic breast cancer receiving 96-h infusional cyclophosphamide as part of a triple sequential high-dose regimen to assess association between presence of peritransplant congestive heart failure ( CHF ) and the following pretreatment characteristics : presence of electrocardiogram ( EKG ) abnormalities , age , hypertension , prior cardiac history , smoking , diabetes mellitus , prior use of anthracyclines , and left-sided chest irradiation .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "CHF", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "diabetes mellitus", "type": "Disease"}, {"text": "anthracyclines", "type": "Chemical"}]}

Example input:
Sentence: Cardiomyopathy is frequent when the total dose exceeds 600 mg/m2 and occurs within one to six months after cessation of therapy .

Example answer:
{"entities": [{"text": "Cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Bradycardia ( defined as a decrease in heart rate to less than 50 beat min-1 ) was prevented when the larger dose of either active drug was used .

Example answer:
{"entities": [{"text": "Bradycardia", "type": "Disease"}]}

Example input:
Sentence: Major toxicities were cardiotoxicity and leukopenia .

Example answer:
{"entities": [{"text": "toxicities", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "leukopenia", "type": "Disease"}]}

Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Late , late doxorubicin cardiotoxicity .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: The cardiotoxicity of conventional anthracycline therapy highlights a need to search for methods that are highly sensitive and capable of predicting cardiac dysfunction .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "anthracycline", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}]}

Example input:
Sentence: The incidence of cardiotoxicity was not higher in patients with signs of cardiovascular disease than in those without in the pre-treatment evaluation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "cardiovascular disease", "type": "Disease"}]}

Example input:
Sentence: The most common signs of cardiotoxicity were chest pain , ST-T wave changes and atrial fibrillation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "chest pain", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}]}

Input:
Sentence: Cardiotoxicity was defined as a reduction of the LVEF of > 5 % to < 55 % with symptoms of heart failure or an asymptomatic reduction of the LVEF of > 10 % to < 55 % .

## Item bc5cdr:test:4449
Example input:
Sentence: Central nervous system complications during treatment of acute lymphoblastic leukemia in a single pediatric institution .

Example answer:
{"entities": [{"text": "Central nervous system complications", "type": "Disease"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: SETTING : National Institutes of Health clinical research center .

Example answer:
{"entities": []}

Example input:
Sentence: Exclusion criteria included CNS leukemic infiltration at diagnosis , therapy-related peripheral neuropathy , late-onset encephalopathy , or long-term neurocognitive defects .

Example answer:
{"entities": [{"text": "leukemic infiltration", "type": "Disease"}, {"text": "peripheral neuropathy", "type": "Disease"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "neurocognitive defects", "type": "Disease"}]}

Example input:
Sentence: Six patients ( 12 % ) had World Health Organization Grade 3-4 neutropenia , 2 patients ( 4 % ) had Grade 3-4 thrombocytopenia , and 2 patients ( 4 % ) had Grade 3 neurotoxicity .

Example answer:
{"entities": [{"text": "neutropenia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Intra-arterial BCNU chemotherapy for treatment of malignant gliomas of the central nervous system .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}, {"text": "malignant gliomas", "type": "Disease"}]}

Example input:
Sentence: Because of the rapid systemic clearance of BCNU ( 1,3-bis- ( 2-chloroethyl ) -1-nitrosourea ) , intra-arterial administration should provide a substantial advantage over intravenous administration for the treatment of malignant gliomas .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}, {"text": "1,3-bis- ( 2-chloroethyl ) -1-nitrosourea", "type": "Chemical"}, {"text": "malignant gliomas", "type": "Disease"}]}

Example input:
Sentence: SETTING : Ophthalmology clinic of an academic hospital .

Example answer:
{"entities": []}

Example input:
Sentence: Neuromuscular blocking agents ( NMBAs ) are often used for patients requiring prolonged mechanical ventilation .

Example answer:
{"entities": []}

Example input:
Sentence: It is necessary that both oncologists and neurologists be fully aware of this unusual complication .

Example answer:
{"entities": []}

Example input:
Sentence: Neuromuscular monitoring was used in two patients .

Example answer:
{"entities": []}

Input:
Sentence: SETTING : Neurocritical care units at two academic medical centers with dedicated neurocritical care teams and board-certified neurointensivists .

## Item bc5cdr:test:4340
Example input:
Sentence: In contrast , both methscopolamine and neostigmine , which do not penetrate the blood-brain barrier , had no effect on the hyperactivity produced by morphine .

Example answer:
{"entities": [{"text": "methscopolamine", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "morphine", "type": "Chemical"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: The aim of this study was to evaluate the relationship between phenytoin medication and cerebellar atrophy in patients who had experienced clinical intoxication .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}, {"text": "cerebellar atrophy", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: These results indicate that noradrenergic neurons have an important role in the manifestation of catalepsy induced by THC , whereas dopaminergic neurons are important in catalepsy induced by haloperidol .

Example answer:
{"entities": [{"text": "catalepsy", "type": "Disease"}, {"text": "THC", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: A healthy 17-year-old male received standard intermittent doses of pethidine via a patient-controlled analgesia ( PCA ) pump for management of postoperative pain control .

Example answer:
{"entities": [{"text": "pethidine", "type": "Chemical"}, {"text": "postoperative pain", "type": "Disease"}]}

Example input:
Sentence: We conclude that phenytoin overdosage does not necessarily result in cerebellar atrophy and it is unlikely that phenytoin medication was the only cause of cerebellar atrophy in the remaining patients .

Example answer:
{"entities": [{"text": "phenytoin", "type": "Chemical"}, {"text": "overdosage", "type": "Disease"}, {"text": "cerebellar atrophy", "type": "Disease"}]}

Example input:
Sentence: Pethidine-associated seizure in a healthy adolescent receiving pethidine for postoperative pain control .

Example answer:
{"entities": [{"text": "Pethidine-associated", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "pethidine", "type": "Chemical"}, {"text": "postoperative pain", "type": "Disease"}]}

Example input:
Sentence: Both plasma pethidine and norpethidine were elevated in the range associated with clinical manifestations of central nervous system excitation .

Example answer:
{"entities": [{"text": "pethidine", "type": "Chemical"}, {"text": "norpethidine", "type": "Chemical"}]}

Input:
Sentence: On the contrary , though not clinically apparent , pethidine potentially causes inhibitory impacts on the CNS and impairs normal cerebellar and oculomotor function in the short term .

## Item bc5cdr:test:3999
Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: Eight glaucomatous patients chronically treated with timolol 0.5 % /12h , suffering from depression diagnosed through DMS-III-R criteria , were included in the study .

Example answer:
{"entities": [{"text": "glaucomatous", "type": "Disease"}, {"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: A case of triamterene nephrolithiasis is reported in a man after 4 years of hydrochlorothiazide-triamterene therapy for hypertension .

Example answer:
{"entities": [{"text": "triamterene", "type": "Chemical"}, {"text": "nephrolithiasis", "type": "Disease"}, {"text": "hydrochlorothiazide-triamterene", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: The ocular myasthenia associated with combination therapy of pegylated IFN alpha-2b and ribavirin for CHC is very rarely reported ; therefore , we present this case with a review of the various eye complications of IFN therapy .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "CHC", "type": "Disease"}, {"text": "IFN", "type": "Chemical"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: A 61-year-old man was treated with combination chemotherapy incorporating cisplatinum , etoposide , high-dose 5-fluorouracil ( 2,250 mg/m2/24 hours ) and folinic acid for an inoperable gastric adenocarcinoma .

Example answer:
{"entities": [{"text": "cisplatinum", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "gastric adenocarcinoma", "type": "Disease"}]}

Example input:
Sentence: This patient underwent a 10-month regimen of rifampin and isoniazid for pulmonary tuberculosis and was discovered to have developed signs of severe renal failure five weeks after completion of therapy .

Example answer:
{"entities": [{"text": "rifampin", "type": "Chemical"}, {"text": "isoniazid", "type": "Chemical"}, {"text": "pulmonary tuberculosis", "type": "Disease"}, {"text": "renal failure", "type": "Disease"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Input:
Sentence: A 45-year-old male patient who was on treatment with multiple second-line anti-tuberculous drugs including linezolid and ethambutol for extensively drug-resistant tuberculosis ( XDR-TB ) presented to us with painless progressive loss of vision in both eyes .

## Item bc5cdr:test:4272
Example input:
Sentence: Chloroacetaldehyde and its contribution to urotoxicity during treatment with cyclophosphamide or ifosfamide .

Example answer:
{"entities": [{"text": "Chloroacetaldehyde", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "ifosfamide", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Severe and long lasting cholestasis after high-dose co-trimoxazole treatment for Pneumocystis pneumonia in HIV-infected patients -- a report of two cases .

Example answer:
{"entities": [{"text": "cholestasis", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}, {"text": "Pneumocystis pneumonia", "type": "Disease"}, {"text": "HIV-infected", "type": "Disease"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Cholestatic hepatitis is a rare adverse effect of ticlopidine that may be immune mediated .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Example input:
Sentence: When CPA , diazepam or 2PAM was given immediately after DFP-atropine , these treatments prevented , delayed or shortened the occurrence of serious signs of poisoning .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "DFP-atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}]}

Example input:
Sentence: DISCUSSION : Cholestatic hepatitis is a rare complication of the antiplatelet agent ticlopidine ; several cases have been reported but few in the English literature .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Input:
Sentence: Cholestatic presentation of yellow phosphorus poisoning .

## Item bc5cdr:test:4268
Example input:
Sentence: A single MPEP ( 5 mg/kg ip ) injection reduced the basal extracellular dopamine level in the striatum , as well as dopamine release stimulated either by methamphetamine ( 10 mg/kg sc ) or by intrastriatally administered veratridine ( 100 microM ) .

Example answer:
{"entities": [{"text": "MPEP", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "veratridine", "type": "Chemical"}]}

Example input:
Sentence: Animals were administered nicotine , carbachol , or neostigmine via timed tail vein infusion , and the latencies to onset of tremor and clonus were recorded and converted to threshold dose .

Example answer:
{"entities": [{"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}, {"text": "tremor", "type": "Disease"}]}

Example input:
Sentence: Forty seconds after injection of suxamethonium , bradycardia and cardiac arrest occurred .

Example answer:
{"entities": [{"text": "suxamethonium", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "cardiac arrest", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: The animals that had experienced cyclic sucrose and chow were hyperactive in response to amphetamine compared with four control groups ( ad libitum 10 % sucrose and chow followed by amphetamine injection , cyclic chow followed by amphetamine injection , ad libitum chow with amphetamine , or cyclic 10 % sucrose and chow with a saline injection ) .

Example answer:
{"entities": [{"text": "sucrose", "type": "Chemical"}, {"text": "hyperactive", "type": "Disease"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: Depletion of dopamine in the striatum was also antagonized when LY274614 was given after the injection of amphetamine ; LY274614 protected when given up to 4 hr after but not when given 8 or 24 hr after amphetamine .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}, {"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: While she was weak , 2-Hz repetitive stimulation revealed a decrement without significant facilitation at rapid rates or after exercise , suggesting postsynaptic neuromuscular blockade .

Example answer:
{"entities": [{"text": "postsynaptic neuromuscular blockade", "type": "Disease"}]}

Example input:
Sentence: When the metoclopramide administration was discontinued , the abnormal movements gradually improved to a considerable extent .

Example answer:
{"entities": [{"text": "metoclopramide", "type": "Chemical"}, {"text": "abnormal movements", "type": "Disease"}]}

Example input:
Sentence: Similarly , in patient diaries , although both treatments caused reduction in subjective dyskinesia scores during the days of intervention , the effect was sustained for 3 days after the intervention for the real rTMS only .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Input:
Sentence: Myoclonic movements are evaluated , which were observed and graded according to clinical severity during the 2 minutes after etomidate injection .

## Item bc5cdr:test:4015
Example input:
Sentence: Effects of acetylsalicylic acid , dipyridamole , and hydrocortisone on epinephrine-induced myocardial injury in dogs .

Example answer:
{"entities": [{"text": "acetylsalicylic acid", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "hydrocortisone", "type": "Chemical"}, {"text": "epinephrine-induced", "type": "Chemical"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: However , a bolus of epinephrine injected through an alternative catheter provoked a hypertensive crisis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: A reproducible model for producing diffuse myocardial injury ( epinephrine infusion ) has been developed to study the cardioprotective effects of agents or maneuvers which might alter the evolution of acute myocardial infarction .

Example answer:
{"entities": [{"text": "myocardial injury", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Severe reversible left ventricular systolic and diastolic dysfunction due to accidental iatrogenic epinephrine overdose .

Example answer:
{"entities": [{"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "epinephrine", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: Infusions of epinephrine ( 4 mug per kilogram per minute for 6 hours ) increased radiocalcium uptakes into intact myocardium and each of its subcellular components with the mitochondrial fraction showing the most consistent changes when compared to saline-infused control animals ( 4,957 vs. 827 counts per minute per gram of dried tissue or fraction ) .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "radiocalcium", "type": "Chemical"}]}

Example input:
Sentence: However , marked tachycardia associated with the use of ephedrine in combination with propofol occurred in the majority of patients , occasionally reaching high levels in individual patients .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}]}

Example input:
Sentence: Epinephrine has a proven role in cardiac arrest in prehospital care ; however , use by paramedics in patients with suspected allergic reaction and severe hypertension should be viewed with caution .

Example answer:
{"entities": [{"text": "Epinephrine", "type": "Chemical"}, {"text": "cardiac arrest", "type": "Disease"}, {"text": "allergic reaction", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Input:
Sentence: Epinephrine alone or in combination with lipid was associated with an increased number of ECG abnormalities compared with lipid emulsion alone .

## Item bc5cdr:test:4369
Example input:
Sentence: We describe a 15-yr-old girl who had orthotopic liver transplantation because of Wilson 's disease .

Example answer:
{"entities": [{"text": "Wilson 's disease", "type": "Disease"}]}

Example input:
Sentence: From June 2004 to October 2006 , 11 HBs Ag positive patients with rheumatologic diseases , who were on both immunosuppressive and prophylactic lamivudine therapies , were retrospectively assessed .

Example answer:
{"entities": [{"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic diseases", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Between July 2001 and April 2004 , 24 patients with relapsed/refractory indolent lymphomas received thalidomide 200 mg daily with escalation by 100 mg daily every 1-2 weeks as tolerated , up to a maximum of 800 mg daily .

Example answer:
{"entities": [{"text": "lymphomas", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: Based on this principle a 27-year old woman , classified as being in the high-risk group ( Goldstein and Berkowitz score : 11 ) , was treated with multiple cytotoxic drugs .

Example answer:
{"entities": []}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: High-dose intravenous methotrexate is an effective treatment for the induction of remission after meningeal relapse in acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: Salvage therapy with nelarabine , etoposide , and cyclophosphamide in relapsed/refractory paediatric T-cell lymphoblastic leukaemia and lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Input:
Sentence: A 37-year-old Caucasian woman with a history of T-cell lymphoblastic lymphoma was admitted for relapsed disease .

## Item bc5cdr:test:4018
Example input:
Sentence: CONCLUSIONS : Cholestatic hepatitis is a rare adverse effect of ticlopidine that may be immune mediated .

Example answer:
{"entities": [{"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: End-stage renal disease ( ESRD ) after orthotopic liver transplantation ( OLTX ) using calcineurin-based immunotherapy : risk of development and treatment .

Example answer:
{"entities": [{"text": "End-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Immune mechanisms may be involved in the drug 's hepatotoxicity , as suggested by the T-cell stimulation study reported here .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Simvastatin-ezetimibe-induced hepatic failure necessitating liver transplantation .

Example answer:
{"entities": [{"text": "Simvastatin-ezetimibe-induced", "type": "Chemical"}, {"text": "hepatic failure", "type": "Disease"}]}

Example input:
Sentence: To our knowledge , this is the first case report of simvastatin-ezetimibe-induced liver failure that resulted in liver transplantation .

Example answer:
{"entities": [{"text": "simvastatin-ezetimibe-induced", "type": "Chemical"}, {"text": "liver failure", "type": "Disease"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: Higher optical density of an antigen assay predicts thrombosis in patients with heparin-induced thrombocytopenia .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To correlate optical density and percent inhibition of a two-step heparin-induced thrombocytopenia ( HIT ) antigen assay with thrombosis ; the assay utilizes reaction inhibition characteristics of a high heparin concentration .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Input:
Sentence: The impact of immune-mediated heparin-induced thrombocytopenia type II ( HIT type II ) as a cause of thrombocytopenia after liver transplantation is not yet understood , with few literature citations reporting contradictory results .

## Item bc5cdr:test:4027
Example input:
Sentence: After detailing the course of events , we discuss the role of paradoxical coronary spasm and hypotension-mediated myocardial ischemia occurring downstream to significant coronary arterial stenosis in the pathophysiology of acute coronary insufficiency .

Example answer:
{"entities": [{"text": "spasm", "type": "Disease"}, {"text": "hypotension-mediated", "type": "Disease"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "coronary arterial stenosis", "type": "Disease"}, {"text": "acute coronary insufficiency", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : To assess the added diagnostic value of a new cardiac performance index ( dP/dtejc ) measurement , based on brachial artery flow changes , as compared to standard 12-lead ECG , for detecting dobutamine-induced myocardial ischemia , using Tc99m-Sestamibi single-photon emission computed tomography as the gold standard of comparison to assess the presence or absence of ischemia .

Example answer:
{"entities": [{"text": "dobutamine-induced", "type": "Chemical"}, {"text": "myocardial ischemia", "type": "Disease"}, {"text": "Tc99m-Sestamibi", "type": "Chemical"}, {"text": "ischemia", "type": "Disease"}]}

Example input:
Sentence: Further signs were hyperhidrosis , hypersalivation , bronchorrhoea , and severe miosis ; the electrocardiographic finding was atrio-ventricular dissociation .

Example answer:
{"entities": [{"text": "hyperhidrosis", "type": "Disease"}, {"text": "hypersalivation", "type": "Disease"}, {"text": "bronchorrhoea", "type": "Disease"}, {"text": "miosis", "type": "Disease"}, {"text": "atrio-ventricular dissociation", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: These patients had Q-T prolongation and recurrent syncope due to polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Q-T prolongation", "type": "Disease"}, {"text": "syncope", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: The most common signs of cardiotoxicity were chest pain , ST-T wave changes and atrial fibrillation .

Example answer:
{"entities": [{"text": "cardiotoxicity", "type": "Disease"}, {"text": "chest pain", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}]}

Example input:
Sentence: In a patient with WPW syndrome and idiopathic dilated cardiomyopathy , intractable atrioventricular reentrant tachycardia ( AVRT ) was iatrogenically induced .

Example answer:
{"entities": [{"text": "WPW syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}, {"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "AVRT", "type": "Disease"}]}

Example input:
Sentence: Torsades de pointes ( TDP ) is a potentially fatal ventricular tachycardia associated with increases in QT interval and monophasic action potential duration ( MAPD ) .

Example answer:
{"entities": [{"text": "Torsades de pointes", "type": "Disease"}, {"text": "TDP", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: Takotsubo syndrome ( TS ) , also known as broken heart syndrome , is characterized by left ventricle apical ballooning with elevated cardiac biomarkers and electrocardiographic changes suggestive of an acute coronary syndrome ( ie , ST-segment elevation , T wave inversions , and pathologic Q waves ) .

## Item bc5cdr:test:4288
Example input:
Sentence: The number of previous manic episodes did not affect the probability of switching , whereas a high score on the hyperthymia component of the Semistructured Affective Temperament Interview was associated with a greater risk of switching ( p = .008 ) .

Example answer:
{"entities": [{"text": "manic", "type": "Disease"}]}

Example input:
Sentence: Akathisia appeared to be a common side effect of fluoxetine and generally responded well to treatment with the beta-adrenergic antagonist propranolol , dose reduction , or both .

Example answer:
{"entities": [{"text": "Akathisia", "type": "Disease"}, {"text": "fluoxetine", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: The main outcome was the number of study participants experiencing akathisia within 60 minutes of administration .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Switches to hypomania or mania occurred in 27 % of all patients ( N = 12 ) ( and in 24 % of the subgroup of patients treated with SSRIs [ 8/33 ] ) ; 16 % ( N = 7 ) experienced manic episodes , and 11 % ( N = 5 ) experienced hypomanic episodes .

Example answer:
{"entities": [{"text": "hypomania", "type": "Disease"}, {"text": "mania", "type": "Disease"}, {"text": "SSRIs", "type": "Chemical"}, {"text": "manic", "type": "Disease"}, {"text": "hypomanic", "type": "Disease"}]}

Example input:
Sentence: Patients who experienced a manic or hypomanic switch were compared with those who did not on several variables including age , sex , diagnosis ( DSM-IV bipolar I vs. bipolar II ) , number of previous manic episodes , type of antidepressant therapy used ( electroconvulsive therapy vs. antidepressant drugs and , more particularly , selective serotonin reuptake inhibitors [ SSRIs ] ) , use and type of mood stabilizers ( lithium vs. anticonvulsants ) , and temperament of the patient , assessed during a normothymic period using the hyperthymia component of the Semi-structured Affective Temperament Interview .

Example answer:
{"entities": [{"text": "manic", "type": "Disease"}, {"text": "hypomanic", "type": "Disease"}, {"text": "DSM-IV bipolar I", "type": "Disease"}, {"text": "bipolar II", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "serotonin reuptake inhibitors", "type": "Chemical"}, {"text": "SSRIs", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Three patients who had experienced neuroleptic-induced akathisia in the past reported that the symptoms of fluoxetine-induced akathisia were identical , although somewhat milder .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}, {"text": "fluoxetine-induced", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : A 50 % reduction in the incidence of akathisia when prochlorperazine was administered by means of 15-minute intravenous infusion versus a 2-minute intravenous push was not detected .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}, {"text": "prochlorperazine", "type": "Chemical"}]}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Five patients receiving fluoxetine for the treatment of obsessive compulsive disorder or major depression developed akathisia .

Example answer:
{"entities": [{"text": "fluoxetine", "type": "Chemical"}, {"text": "obsessive compulsive disorder", "type": "Disease"}, {"text": "major depression", "type": "Disease"}, {"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Akathisia was defined as either a spontaneous report of restlessness or agitation or a change of 2 or more in the patient-reported akathisia rating scale and a change of at least 1 in the investigator-observed akathisia rating scale .

Example answer:
{"entities": [{"text": "agitation", "type": "Disease"}, {"text": "akathisia", "type": "Disease"}]}

Input:
Sentence: The diagnoses of manic shift and akathisia were dismissed .

## Item bc5cdr:test:3799
Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: METHOD : FS containing aprotinin or different concentrations of tAMCA ( 0.5-47.5 mg/ml ) were applied to the pial surface of the cortex of anaesthetized rats .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}]}

Example input:
Sentence: Streptomycin sulfate ( 300 mg/kg s.c. ) was injected for various periods into preweanling rats and for 3 weeks into weanling rats .

Example answer:
{"entities": [{"text": "Streptomycin", "type": "Chemical"}]}

Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : FS containing tAMCA caused paroxysmal brain activity which was associated with distinct convulsive behaviours .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: A literature review revealed no prior reports of pericarditis in anti-MPO pANCA-positive vasculitis associated with propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Example input:
Sentence: Propylthiouracil-induced perinuclear-staining antineutrophil cytoplasmic autoantibody-positive vasculitis in conjunction with pericarditis .

Example answer:
{"entities": [{"text": "Propylthiouracil-induced", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}, {"text": "pericarditis", "type": "Disease"}]}

Example input:
Sentence: The cerebrospinal fluid : serum ratio of cimetidine concentrations was 0.24:1 and indicates that cimetidine passes the blood-brain barrier ; it also raises the possibility that M.S .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: Macrophage-migration inhibition ( MIF ) test with ampicillin was positive .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Input:
Sentence: OBJECTIVE : To report a case of methicillin-sensitive Staphylococcus aureus ( MSSA ) bacteremia with suspected MSSA meningitis treated with high-dose daptomycin assessed with concurrent serum and cerebrospinal fluid ( CSF ) concentrations .

## Item bc5cdr:test:4177
Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: In SE survivors , similar stimulation resulted in a population spike followed , at a variable latency , by negative DC shifts and repetitive afterdischarges of 3-60 s duration , which were blocked by ionotropic glutamate receptor antagonists .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: We tested the sulfated polysaccharide fucoidan , which has been reported to reduce inflammatory brain damage , in a rat model of intracerebral hemorrhage induced by injection of bacterial collagenase into the caudate nucleus .

Example answer:
{"entities": [{"text": "fucoidan", "type": "Chemical"}, {"text": "brain damage", "type": "Disease"}, {"text": "intracerebral hemorrhage", "type": "Disease"}]}

Example input:
Sentence: In this study , we investigated the therapeutic potential of bone marrow mononuclear cells ( BMCs ) in a model of epilepsy induced by pilocarpine in rats .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "pilocarpine", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: NFkappaB activity was decreased in the frontal cortex of cocaine treated rats , as well as GSH concentration and glutathione peroxidase activity in the hippocampus , whereas nNOS activity in the hippocampus was increased .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "GSH", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: Because the CNS damage caused by METH and MPTP is highly selective for the DA neuronal system in mouse models of neurotoxicity , we hypothesized that the CX3CR1 plays a role in METH-induced neurotoxicity and microglial activation .

Example answer:
{"entities": [{"text": "CNS damage", "type": "Disease"}, {"text": "METH", "type": "Chemical"}, {"text": "MPTP", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "METH-induced", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Mice in which the CX3CR1 gene has been deleted and replaced with a cDNA encoding enhanced green fluorescent protein ( eGFP ) were treated with METH and examined for striatal neurotoxicity .

Example answer:
{"entities": [{"text": "METH", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: At hippocampal Schaeffer collateral-CA1 synapses , long-term potentiation was preserved in BMC-transplanted rats compared to epileptic controls .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}]}

Input:
Sentence: Glial activation and post-synaptic neurotoxicity : the key events in Streptozotocin ( ICV ) induced memory impairment in rats .

## Item bc5cdr:test:4196
Example input:
Sentence: These responses were blocked by systemic pre-administration of hexamethonium chloride ( 20 mg/kg ) .

Example answer:
{"entities": [{"text": "hexamethonium chloride", "type": "Chemical"}]}

Example input:
Sentence: We describe a case of transient neurological deficit that occurred after unilateral spinal anaesthesia with 8 mg of 1 % hyperbaric bupivacaine slowly injected through a 25-gauge pencil-point spinal needle .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The rate of contrast-induced nephropathy , defined by multiple end points , is not statistically different after the intraarterial administration of iopamidol or iodixanol to high-risk patients , with or without diabetes mellitus .

Example answer:
{"entities": [{"text": "nephropathy", "type": "Disease"}, {"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}, {"text": "diabetes mellitus", "type": "Disease"}]}

Example input:
Sentence: 2 and 10 mg/kg/i.p. , or an equal volume of saline for the control group ( n = 20 ) ; 15 minutes later , all the animals were injected with a single 50 mg/kg/i.p .

Example answer:
{"entities": []}

Example input:
Sentence: However , we suggest that a low solution concentration should be preferred for unilateral spinal anaesthesia with a hyperbaric anaesthetic solution ( if pencil-point needle and slow injection rate are employed ) , in order to minimize the risk of a localized high peak anaesthetic concentration , which might lead to a transient neurological deficit .

Example answer:
{"entities": [{"text": "neurological deficit", "type": "Disease"}]}

Example input:
Sentence: Haemodilution in groups B and C was produced by withdrawing approximately 1000 mL of blood and replacing it with the same amount of dextran solution , and final haematocrit values were 21 or 22 % .

Example answer:
{"entities": [{"text": "Haemodilution", "type": "Disease"}, {"text": "dextran", "type": "Chemical"}]}

Example input:
Sentence: Intravenous hydration and mannitol was administered before and after cisplatin .

Example answer:
{"entities": [{"text": "mannitol", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: injection of flunitrazepam significantly more often than with isotonic saline .

Example answer:
{"entities": [{"text": "flunitrazepam", "type": "Chemical"}]}

Example input:
Sentence: Sodium chloride solution ( 0.9 % ) or noradrenaline in doses of 4 , 12 and 36 micrograms h-1 kg-1 was infused for five consecutive days , either intrarenally ( by a new technique ) or intravenously into rats with one kidney removed .

Example answer:
{"entities": [{"text": "Sodium chloride", "type": "Chemical"}, {"text": "noradrenaline", "type": "Chemical"}]}

Example input:
Sentence: Patients in Group C received 2 ml normal saline , Group L , 2 ml , lidocaine 2 % ( 40 mg ) and Group T , 2 ml thiopentone 2.5 % ( 50 mg ) .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "thiopentone", "type": "Chemical"}]}

Input:
Sentence: The first group of patients was administered isotonic sodium chloride ; the second group was administered a solution that of 5 % dextrose and sodium bicarbonate , while the third group was administered isotonic sodium chloride before and after the contrast injection .

## Item bc5cdr:test:4223
Example input:
Sentence: Gamma-hexachlorocyclohexane ( gamma-HCH ) , the active ingredient of the insecticide lindane , has been shown to decrease seizure threshold to pentylenetrazol ( PTZ ) 3 h after exposure to gamma-HCH and conversely increase threshold to PTZ-induced seizures 24 h after exposure to gamma-HCH ( Vohland et al .

Example answer:
{"entities": [{"text": "Gamma-hexachlorocyclohexane", "type": "Chemical"}, {"text": "gamma-HCH", "type": "Chemical"}, {"text": "lindane", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "PTZ-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Neonatal pyridoxine responsive convulsions due to isoniazid therapy .

Example answer:
{"entities": [{"text": "pyridoxine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "isoniazid", "type": "Chemical"}]}

Example input:
Sentence: DISCUSSION : To our knowledge , this is the first reported case of venlafaxine overdose that resulted in a generalized seizure .

Example answer:
{"entities": [{"text": "venlafaxine", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : The venlafaxine overdose in our patient resulted in a single episode of generalized seizure but elicited no further sequelae .

Example answer:
{"entities": [{"text": "venlafaxine", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: Zyban caused significant neurological and cardiovascular toxicity in overdose .

Example answer:
{"entities": [{"text": "Zyban", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sensitivity to several convulsion endpoints induced by nicotine , carbachol , and neostigmine were significantly greater in WSR versus WSP mice .

Example answer:
{"entities": [{"text": "convulsion", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}, {"text": "carbachol", "type": "Chemical"}, {"text": "neostigmine", "type": "Chemical"}]}

Example input:
Sentence: FINDINGS : FS containing tAMCA caused paroxysmal brain activity which was associated with distinct convulsive behaviours .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Seizure activity due to PTZ and picrotoxin ( PTX ) was significantly decreased ; however , seizure activity due to 3-mercaptopropionic acid ( MPA ) , bicuculline ( BCC ) , methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate ( DMCM ) , or strychnine ( STR ) was not different from control .

Example answer:
{"entities": [{"text": "Seizure", "type": "Disease"}, {"text": "PTZ", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "PTX", "type": "Chemical"}, {"text": "seizure", "type": "Disease"}, {"text": "3-mercaptopropionic acid", "type": "Chemical"}, {"text": "MPA", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "BCC", "type": "Chemical"}, {"text": "methyl 6,7-dimethoxy-4-ethyl-B-carboline-3-carboxylate", "type": "Chemical"}, {"text": "DMCM", "type": "Chemical"}, {"text": "strychnine", "type": "Chemical"}, {"text": "STR", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Input:
Sentence: Thus , the precipitating cause of convulsions was believed to be an overdose of TNA .

## Item bc5cdr:test:4062
Example input:
Sentence: On a low-salt ( LS ) diet , male DS had higher levels of intrarenal angiotensinogen mRNA than females .

Example answer:
{"entities": []}

Example input:
Sentence: Pretreatment with the D2 agonist PHNO enhanced nicotine-induced hyperactivity , whereas the D1 agonist SKF 38393 had no effect .

Example answer:
{"entities": [{"text": "PHNO", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "SKF 38393", "type": "Chemical"}]}

Example input:
Sentence: The use and toxicity of didanosine ( ddI ) in HIV antibody-positive individuals intolerant to zidovudine ( AZT ) One hundred and fifty-one patients intolerant to zidovudine ( AZT ) received didanosine ( ddI ) to a maximum dose of 12.5 mg/kg/day .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "didanosine", "type": "Chemical"}, {"text": "ddI", "type": "Chemical"}, {"text": "HIV antibody-positive", "type": "Disease"}, {"text": "zidovudine", "type": "Chemical"}, {"text": "AZT", "type": "Chemical"}]}

Example input:
Sentence: There was a remarkable reduction in total cholesterol level as well , to the extent of 23 % in young and 21 % in aged animals with this dose of DCE .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}, {"text": "DCE", "type": "Chemical"}]}

Example input:
Sentence: Both agents show substantial clinical efficacy , with reductions in total cholesterol of over 30 % and in LDL-cholesterol of 40 % in clinical studies .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}]}

Example input:
Sentence: When CPA , diazepam or 2PAM was given immediately after DFP-atropine , these treatments prevented , delayed or shortened the occurrence of serious signs of poisoning .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "DFP-atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}]}

Example input:
Sentence: This toxicity appeared in patients receiving the higher doses of desferrioxamine or coincided with the normalization of ferritin or aluminium serum levels .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "desferrioxamine", "type": "Chemical"}, {"text": "aluminium", "type": "Chemical"}]}

Example input:
Sentence: This treatment with CBZ had no apparent adverse effect on folate concentrations in the rat , and , indeed , the folate concentration increased in liver after 6 weeks of treatment and in plasma at 8 weeks of treatment .

Example answer:
{"entities": [{"text": "CBZ", "type": "Chemical"}, {"text": "folate", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: In conclusion , CPA , diazepam and 2PAM in combination with atropine prevented the occurrence of serious signs of poisoning and thus reduced the toxicity of DFP in rat .

Example answer:
{"entities": [{"text": "CPA", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}, {"text": "DFP", "type": "Chemical"}]}

Input:
Sentence: RESULTS : Our data showed that subacute exposure to diazinon significantly increased concentrations of cholesterol , triglyceride and LDL .

## Item bc5cdr:test:4217
Example input:
Sentence: INTERPRETATION : Tranexamic acid retains its convulsive action within FS .

Example answer:
{"entities": [{"text": "Tranexamic acid", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Recently , synthetic fibrinolysis inhibitors such as tranexamic acid ( tAMCA ) have been considered as substitutes for aprotinin .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "Chemical"}, {"text": "tAMCA", "type": "Chemical"}]}

Example input:
Sentence: METHODS : In a population-based study in 513 naturally postmenopausal women aged 54-67 years , we studied the association between self-reported intramuscularly administered high-dose estrogen-testosterone therapy ( estradiol- and testosterone esters ) and aortic atherosclerosis .

Example answer:
{"entities": [{"text": "estrogen-testosterone", "type": "Chemical"}, {"text": "estradiol- and testosterone esters", "type": "Chemical"}, {"text": "atherosclerosis", "type": "Disease"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Optimal control of the absences was achieved with sodium valproate , lamotrigine , or ethosuximide alone or in combination .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "lamotrigine", "type": "Chemical"}, {"text": "ethosuximide", "type": "Chemical"}]}

Example input:
Sentence: FANFT-induced cell proliferation in the bladder was significantly suppressed by aspirin co-administration after 4 weeks but not after 12 weeks .

Example answer:
{"entities": [{"text": "FANFT-induced", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Estrogen replacement ( 17beta-estradiol subcutaneous pellet , 14.2 microg/day , 12 wk ) of Ovx rats restored the hemodynamic and locomotor effects of alpha-methyldopa to sham-operated levels .

Example answer:
{"entities": [{"text": "17beta-estradiol", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}]}

Example input:
Sentence: Conservative treatment , including bladder irrigation with physiological saline and instillation of prostaglandin F2 alpha , failed to totally control hemorrhage .

Example answer:
{"entities": [{"text": "prostaglandin F2 alpha", "type": "Chemical"}, {"text": "hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Input:
Sentence: Tranexamic acid ( TNA ) 1 g 8-hourly was administered to her to control bleeding per vaginum .

## Item bc5cdr:test:3956
Example input:
Sentence: To assess the molecular basis of disturbances in transmembraneous transport of Na+ , we studied the response of cardiac ( Na , K ) -ATPase to NO-deficient hypertension induced in rats by NO-synthase inhibition with 40 mg/kg/day N ( G ) -nitro-L-arginine methyl ester ( L-NAME ) for 4 four weeks .

Example answer:
{"entities": [{"text": "Na+", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "NO-deficient", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "NO-synthase", "type": "Chemical"}, {"text": "N ( G ) -nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: Mitochondrial abnormalities have been associated with several aspects of epileptogenesis , such as energy generation , control of cell death , neurotransmitter synthesis , and free radical ( FR ) production .

Example answer:
{"entities": [{"text": "Mitochondrial abnormalities", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: Together , these results suggest that the beta4 and the alpha3 subunits are mediators of nicotine-induced seizures and hypolocomotion .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: We examined the role of the beta4 subunits in nicotine-induced seizures and hypolocomotion in beta4 homozygous null ( beta4 -/- ) and alpha3 heterozygous ( +/- ) mice .

Example answer:
{"entities": [{"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: Previous research in this laboratory has shown that a diet of intermittent excessive sugar consumption produces a state with neurochemical and behavioral similarities to drug dependency .

Example answer:
{"entities": [{"text": "drug dependency", "type": "Disease"}]}

Example input:
Sentence: The alpha3 and beta4 nicotinic acetylcholine receptor subunits are necessary for nicotine-induced seizures and hypolocomotion in mice .

Example answer:
{"entities": [{"text": "acetylcholine", "type": "Chemical"}, {"text": "nicotine-induced", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}, {"text": "hypolocomotion", "type": "Disease"}]}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Upregulation of brain expression of P-glycoprotein in MRP2-deficient TR ( - ) rats resembles seizure-induced up-regulation of this drug efflux transporter in normal rats .

Example answer:
{"entities": [{"text": "seizure-induced", "type": "Disease"}]}

Example input:
Sentence: We conclude that in streptozotocin-diabetic rats with an increased urinary albumin excretion , a reduced heparan sulphate charge barrier/density is found at the lamina rara externa of the glomerular basement membrane .

Example answer:
{"entities": [{"text": "streptozotocin-diabetic", "type": "Chemical"}, {"text": "heparan sulphate", "type": "Chemical"}]}

Example input:
Sentence: This prompted us to study the brain expression of P-glycoprotein ( Pgp ) , a major drug efflux transporter in many tissues , including the BBB , in TR ( - ) rats compared with nonmutant ( wild-type ) Wistar rats .

Example answer:
{"entities": []}

Input:
Sentence: An alternative source of energy is d-galactose ( the C-4-epimer of d-glucose ) which is transported into the brain by insulin-independent GLUT3 transporter where it might be metabolized to glucose via the Leloir pathway .

## Item bc5cdr:test:4111
Example input:
Sentence: Serum creatinine values did not change significantly : 1.98 +/- 0.8 mg/dL before SRL therapy and 2.53 +/- 1.9 mg/dL at last follow-up ( P = .14 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: The Calcineurin-inhibitor Induced Pain Syndrome ( CIPS ) is a rare but severe side effect of cyclosporine or tacrolimus and is accurately diagnosed by its typical presentation , magnetic resonance imaging and bone scans .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "CIPS", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: Following polytherapy according to the CMF regimen , a statistically significant decrease ( p = 0.0343 ) in creatinine clearance was found , but creatinine concentration did not increase significantly compared to controls .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Maximal cTnI ( pg/ml ) and cTnT levels were significantly increased in DOX rats compared with controls ( p=0.006 , 0.007 ) .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: The yield of severe cirrhosis of the liver ( defined as a shrunken finely nodular liver with micronodular histology , ascites greater than 30 ml , plasma albumin less than 2.2 g/dl , splenomegaly 2-3 times normal , and testicular atrophy approximately half normal weight ) after 12 doses of carbon tetrachloride given intragastrically in the phenobarbitone-primed rat was increased from 25 % to 56 % by giving the initial `` calibrating '' dose of carbon tetrachloride at the peak of the phenobarbitone-induced enlargement of the liver .

Example answer:
{"entities": [{"text": "cirrhosis of the liver", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "splenomegaly", "type": "Disease"}, {"text": "atrophy", "type": "Disease"}, {"text": "carbon tetrachloride", "type": "Chemical"}, {"text": "phenobarbitone-primed", "type": "Chemical"}, {"text": "phenobarbitone-induced", "type": "Chemical"}, {"text": "enlargement of the liver", "type": "Disease"}]}

Example input:
Sentence: Relative to desipramine alone , mean AUC and C ( max ) of desipramine increased 3.6- and 1.8-fold when coadministered with cinacalcet .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: After the administration of NG , 5-FU and CY neither a statistically significant increase in creatinine concentration nor an increase in creatinine clearance was observed compared to the group receiving no cytostatics .

Example answer:
{"entities": [{"text": "NG", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "CY", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: The ratio of cimetidine clearance to creatinine clearance ( Rc ) averaged 4.8 +/- 2.0 , indicating net tubular secretion for cimetidine .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Mean serum creatinine level before conversion was 2.21 mg/dL and thereafter , 4.93 mg/dL ( P = .02 ) .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}]}

Input:
Sentence: CIN was defined as an increase in serum creatinine ( Cr ) of 0.5 mg/dl or more , or elevation of Cr to 25 % over baseline .

## Item bc5cdr:test:4426
Example input:
Sentence: Glucocorticoid-induced hypertension ( GC-HT ) in the rat is associated with nitric oxide-redox imbalance .

Example answer:
{"entities": [{"text": "hypertension", "type": "Disease"}, {"text": "nitric", "type": "Chemical"}]}

Example input:
Sentence: An experimental model was developed in the rat to measure changes in lacrimation and intracranial blood flow following noxious chemical stimulation of facial mucosa .

Example answer:
{"entities": []}

Example input:
Sentence: Plasma aldosterone levels increased in nephrotic mice of both genotypes and was followed by increased SGK1 protein expression in sgk1 ( +/+ ) mice .

Example answer:
{"entities": [{"text": "aldosterone", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Adult rats given dexamethasone on days 15 and 16 of gestation had more glomeruli with glomerulosclerosis than control rats .

Example answer:
{"entities": [{"text": "dexamethasone", "type": "Chemical"}, {"text": "glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Allopregnanolone ( 3alpha-hydroxy-5alpha-pregnan-20-one ) , pregnanolone ( 3alpha-hydroxy-5beta-pregnan-20-one ) and ganaxolone ( a synthetic derivative of allopregnanolone 3alpha-hydroxy-3beta-methyl-5alpha-pregnan-20-one ) were tested for their ability to suppress the expression ( anticonvulsant effect ) and development ( antiepileptogenic effect ) of cocaine-kindled seizures in male , Swiss-Webster mice .

Example answer:
{"entities": [{"text": "Allopregnanolone", "type": "Chemical"}, {"text": "3alpha-hydroxy-5alpha-pregnan-20-one", "type": "Chemical"}, {"text": "pregnanolone", "type": "Chemical"}, {"text": "3alpha-hydroxy-5beta-pregnan-20-one", "type": "Chemical"}, {"text": "ganaxolone", "type": "Chemical"}, {"text": "allopregnanolone", "type": "Chemical"}, {"text": "3alpha-hydroxy-3beta-methyl-5alpha-pregnan-20-one", "type": "Chemical"}, {"text": "cocaine-kindled", "type": "Chemical"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Male Wistar rats were implanted bilaterally with cannulae into the accumbens shell or core , and then were locally injected with GR 55562 ( an antagonist of 5-HT1B receptors ) or CP 93129 ( an agonist of 5-HT1B receptors ) .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: Eight glaucomatous patients chronically treated with timolol 0.5 % /12h , suffering from depression diagnosed through DMS-III-R criteria , were included in the study .

Example answer:
{"entities": [{"text": "glaucomatous", "type": "Disease"}, {"text": "timolol", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: BMCs obtained from green fluorescent protein ( GFP ) transgenic mice or rats were transplanted intravenously after induction of status epilepticus ( SE ) .

Example answer:
{"entities": [{"text": "status epilepticus", "type": "Disease"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Input:
Sentence: Here , we developed a murine model of glucocorticoid-induced glaucoma that exhibits glaucoma features that are observed in patients .

## Item bc5cdr:test:4327
Example input:
Sentence: Suxamethonium causes prolonged apnea in patients in whom pseudocholinesterase enzyme gets deactivated by organophosphorus ( OP ) poisons .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}, {"text": "organophosphorus ( OP ) poisons", "type": "Chemical"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproic acid induced encephalopathy -- 19 new cases in Germany from 1994 to 2003 -- a side effect associated to VPA-therapy not only in young children .

Example answer:
{"entities": [{"text": "Valproic acid", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "VPA-therapy", "type": "Chemical"}]}

Example input:
Sentence: Encephalopathy induced by levetiracetam added to valproate .

Example answer:
{"entities": [{"text": "Encephalopathy", "type": "Disease"}, {"text": "levetiracetam", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: The possible influence of the hepatic damage , mainly hyperammonemia , upon the development of valproate encephalopathy is discussed .

Example answer:
{"entities": [{"text": "hepatic damage", "type": "Disease"}, {"text": "hyperammonemia", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Morphological features of encephalopathy after chronic administration of the antiepileptic drug valproate to rats .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}]}

Example input:
Sentence: A case of valproate-induced encephalopathy is presented .

Example answer:
{"entities": [{"text": "valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: Valproate-induced encephalopathy is a rare syndrome that may manifest in otherwise normal epileptic individuals .

Example answer:
{"entities": [{"text": "Valproate-induced", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}, {"text": "epileptic", "type": "Disease"}]}

Input:
Sentence: Normoammonemic encephalopathy : solely valproate induced or multiple mechanisms ?

## Item bc5cdr:test:4128
Example input:
Sentence: Desferrioxamine withdrawal resulted in a complete recovery of visual function in 1 patient and partial recovery in 3 , and a complete reversal of hearing loss in 3 patients and partial recovery in 3 .

Example answer:
{"entities": [{"text": "Desferrioxamine", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Minutes after oral administration , the patient developed nausea , sweating and hypotension , and finally collapsed .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: It is postulated that her death was caused by hypersensitivity to suxamethonium , associated with her 5-day immobilization .

Example answer:
{"entities": [{"text": "death", "type": "Disease"}, {"text": "hypersensitivity", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: In the present paper the authors describe 2 female patients who developed incontinence secondary to the selective serotonin reuptake inhibitors paroxetine and sertraline , as well as a third who developed this side effect on venlafaxine .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "sertraline", "type": "Chemical"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : FS containing tAMCA caused paroxysmal brain activity which was associated with distinct convulsive behaviours .

Example answer:
{"entities": [{"text": "tAMCA", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}]}

Example input:
Sentence: Fewer subjects reported adverse events following treatment with desipramine alone than when receiving desipramine with cinacalcet ( 33 versus 86 % ) , the most frequent of which ( nausea and headache ) have been reported for patients treated with either desipramine or cinacalcet .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}, {"text": "nausea", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: Tamoxifen ( TAM ) , the antiestrogenic drug most widely prescribed in the chemotherapy of breast cancer , induces changes in normal discoid shape of erythrocytes and hemolytic anemia .

Example answer:
{"entities": [{"text": "Tamoxifen", "type": "Chemical"}, {"text": "TAM", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 40-year-old woman with major depression took an overdose of venlafaxine in an apparent suicide attempt .

Example answer:
{"entities": [{"text": "major depression", "type": "Disease"}, {"text": "overdose", "type": "Disease"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Input:
Sentence: Her medications included desvenlafaxine , and symptoms included nausea , anxiety and confusion .

## Item bc5cdr:test:4346
Example input:
Sentence: Arterial hypertension as a complication of prolonged ketoconazole treatment .

Example answer:
{"entities": [{"text": "hypertension", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}]}

Example input:
Sentence: Ketoconazole-induced neurologic sequelae .

Example answer:
{"entities": [{"text": "Ketoconazole-induced", "type": "Chemical"}, {"text": "neurologic sequelae", "type": "Disease"}]}

Example input:
Sentence: Ketoconazole induced torsades de pointes without concomitant use of QT interval-prolonging drug .

Example answer:
{"entities": [{"text": "Ketoconazole", "type": "Chemical"}, {"text": "torsades de pointes", "type": "Disease"}]}

Example input:
Sentence: This calls for attention when ketoconazole is administered to patients with risk factors for acquired long QT syndrome .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "long QT syndrome", "type": "Disease"}]}

Example input:
Sentence: Ketoconazole was introduced in the United Kingdom in 1981 .

Example answer:
{"entities": [{"text": "Ketoconazole", "type": "Chemical"}]}

Example input:
Sentence: Two of 14 patients with Cushing 's syndrome treated on a long-term basis with ketoconazole developed sustained hypertension .

Example answer:
{"entities": [{"text": "Cushing 's syndrome", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Hepatic reactions associated with ketoconazole in the United Kingdom .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}]}

Example input:
Sentence: In two of the three deaths probably associated with ketoconazole treatment the drug had been continued after the onset of jaundice and other symptoms of hepatitis .

Example answer:
{"entities": [{"text": "deaths", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "jaundice", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: A 77-y-old patient developed weakness of extremities , legs paralysis , dysarthria and tremor 1 h after ingestion of 200 mg ketoconazole for the first time in his life .

Example answer:
{"entities": [{"text": "weakness of extremities", "type": "Disease"}, {"text": "legs paralysis", "type": "Disease"}, {"text": "dysarthria", "type": "Disease"}, {"text": "tremor", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Input:
Sentence: To the best of our knowledge , this is the first reported case of ketoconazole-induced baboon syndrome in the English literature .

## Item bc5cdr:test:4026
Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: In this report we describe the case of a 37-year-old white woman with Ebstein 's anomaly , who developed a rare syndrome called platypnea-orthodeoxia , characterized by massive right-to-left interatrial shunting with transient profound hypoxia and cyanosis .

Example answer:
{"entities": [{"text": "Ebstein 's anomaly", "type": "Disease"}, {"text": "platypnea-orthodeoxia", "type": "Disease"}, {"text": "hypoxia", "type": "Disease"}, {"text": "cyanosis", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Head-up tilt caused systolic orthostatic hypotension which was marked in six of 20 PD patients on selegiline , one of whom lost consciousness with unrecordable blood pressures .

Example answer:
{"entities": [{"text": "systolic orthostatic hypotension", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: Simvastatin-induced bilateral leg compartment syndrome and myonecrosis associated with hypothyroidism .

Example answer:
{"entities": [{"text": "Simvastatin-induced", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}, {"text": "hypothyroidism", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Transient platypnea-orthodeoxia-like syndrome induced by propafenone overdose in a young woman with Ebstein 's anomaly .

Example answer:
{"entities": [{"text": "platypnea-orthodeoxia-like syndrome", "type": "Disease"}, {"text": "propafenone", "type": "Chemical"}, {"text": "overdose", "type": "Disease"}, {"text": "Ebstein 's anomaly", "type": "Disease"}]}

Example input:
Sentence: Nitrofurantoins were associated with anophthalmia or microphthalmos ( AOR = 3.7 ; 95 % CI , 1.1-12.2 ) , hypoplastic left heart syndrome ( AOR = 4.2 ; 95 % CI , 1.9-9.1 ) , atrial septal defects ( AOR = 1.9 ; 95 % CI , 1.1-3.4 ) , and cleft lip with cleft palate ( AOR = 2.1 ; 95 % CI , 1.2-3.9 ) .

Example answer:
{"entities": [{"text": "Nitrofurantoins", "type": "Chemical"}, {"text": "anophthalmia", "type": "Disease"}, {"text": "microphthalmos", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "atrial septal defects", "type": "Disease"}, {"text": "cleft lip", "type": "Disease"}, {"text": "cleft palate", "type": "Disease"}]}

Input:
Sentence: Takotsubo syndrome ( or apical ballooning syndrome ) secondary to Zolmitriptan .

## Item bc5cdr:test:4565
Example input:
Sentence: Cranial magnetic resonance imaging and extensive laboratory studies failed to reveal structural lesions of the brain and metabolic abnormalities .

Example answer:
{"entities": [{"text": "structural lesions of the brain", "type": "Disease"}, {"text": "metabolic abnormalities", "type": "Disease"}]}

Example input:
Sentence: High-signal intensity lesions on DWI tended to show low signal intensity on ADC map ( 3/4 ) , but in one patient , high signal intensity was shown at bilateral dentate nuclei on not only DWI but also ADC map .

Example answer:
{"entities": []}

Example input:
Sentence: The first ultrastructural changes in structural elements of the blood-brain-barrier ( BBB ) in the cerebellar cortex were detectable after 3 months of the experiment .

Example answer:
{"entities": []}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The images were subsequently processed to obtain volumetric data for the cerebellum .

Example answer:
{"entities": []}

Example input:
Sentence: Alterations in the structural elements of the BBB coexisted with marked lesions of neurons of the cerebellum ( Purkinje cells are earliest ) .

Example answer:
{"entities": []}

Example input:
Sentence: Magnetic resonance volumetry of the cerebellum in epileptic patients after phenytoin overdosages .

Example answer:
{"entities": [{"text": "epileptic", "type": "Disease"}, {"text": "phenytoin", "type": "Chemical"}, {"text": "overdosages", "type": "Disease"}]}

Example input:
Sentence: Brain CT revealed a periventricular low density area in the frontal white matter and moderate dilatation of the lateral ventricles especially at the bilateral anterior horns .

Example answer:
{"entities": []}

Example input:
Sentence: All the lesions in dentate , inferior colliculus , pons , and medullas had been resolved completely on follow-up MRIs in 5 patients , but in 1 patient of them , corpus callosal lesion persisted .

Example answer:
{"entities": [{"text": "callosal lesion", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Input:
Sentence: Magnetic resonance imaging ( MRI ) brain showed abnormal signal intensity involving both dentate nuclei of cerebellum and splenium of corpus callosum .

## Item bc5cdr:test:4243
Example input:
Sentence: This case report shows that ciprofloxacin may precipitate life-threatening thrombocytopenia and haemolytic anaemia , even in the early phases of treatment and without apparent previous exposures .

Example answer:
{"entities": [{"text": "ciprofloxacin", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "haemolytic anaemia", "type": "Disease"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: We describe a patient who developed dilated cardiomyopathy and clinical congestive heart failure after 2 months of therapy with amphotericin B ( AmB ) for disseminated coccidioidomycosis .

Example answer:
{"entities": [{"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "heart failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}, {"text": "AmB", "type": "Chemical"}, {"text": "coccidioidomycosis", "type": "Disease"}]}

Example input:
Sentence: In both cases , discontinuation of FK506 and treatment with plasma exchange , fresh frozen plasma replacement , corticosteroids , aspirin , and dipyridamole led to resolution of MAHA .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "corticosteroids", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "MAHA", "type": "Disease"}]}

Example input:
Sentence: We report a case of a living donor renal transplant recipient who developed cyclosporine-induced TMA that responded to the withdrawal of cyclosporine in conjunction with plasmapheresis and fresh frozen plasma replacement therapy .

Example answer:
{"entities": [{"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}]}

Example input:
Sentence: Five patients with carcinoma developed thrombotic microangiopathy ( characterized by renal insufficiency , microangiopathic hemolytic anemia , and usually thrombocytopenia ) after treatment with cisplatin , bleomycin , and a vinca alkaloid .

Example answer:
{"entities": [{"text": "carcinoma", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}, {"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "bleomycin", "type": "Chemical"}, {"text": "vinca alkaloid", "type": "Chemical"}]}

Example input:
Sentence: Severe thrombocytopenia and haemolytic anaemia associated with ciprofloxacin : a case report with fatal outcome .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "haemolytic anaemia", "type": "Disease"}, {"text": "ciprofloxacin", "type": "Chemical"}]}

Example input:
Sentence: Agranulocytosis occurred 3-20 weeks after initiation of ticlopidine , so frequent examination of white cell count during treatment is recommended .

Example answer:
{"entities": [{"text": "Agranulocytosis", "type": "Disease"}, {"text": "ticlopidine", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Input:
Sentence: CASE : We describe a second case of fluconazole associated agranulocytosis with thrombocytopenia and recovery upon discontinuation of therapy .

## Item bc5cdr:test:3967
Example input:
Sentence: Diagnosis of this potentially fatal complication may be delayed or missed if renal tissue or the peripheral blood smear is not examined , because renal failure may be ascribed to cisplatin nephrotoxicity and the anemia and thrombocytopenia to drug-induced bone marrow suppression .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "anemia", "type": "Disease"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "bone marrow suppression", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVE : To report a case of a severe interaction between simvastatin , amiodarone , and atazanavir resulting in rhabdomyolysis and acute renal failure .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}, {"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Dup 753 prevents the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "Dup 753", "type": "Chemical"}, {"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Combined antiretroviral therapy causes cardiomyopathy and elevates plasma lactate in transgenic AIDS mice .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "lactate", "type": "Chemical"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: RESULTS : As anticipated , adriamycin elicited nephrotic range proteinuria , renal interstitial damage and mild focal glomerulosclerosis .

Example answer:
{"entities": [{"text": "adriamycin", "type": "Chemical"}, {"text": "nephrotic", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "renal interstitial damage", "type": "Disease"}, {"text": "focal glomerulosclerosis", "type": "Disease"}]}

Example input:
Sentence: Groups 3 and 4 were studied at four and at six months to assess the effect of enalapril on progression of renal injury in adriamycin nephrosis .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "renal injury", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Input:
Sentence: We undertook a descriptive analysis of Yellow Card records of 407 HIV-positive persons taking tenofovir disoproxil fumarate ( TDF ) as part of their antiretroviral therapy regimen and submitted to the Medicines and Healthcare Products Regulatory Agency ( MHRA ) with suspected kidney adverse effects .

## Item bc5cdr:test:4071
Example input:
Sentence: It was administered by 15 min infusion to 16 evaluable patients with non-small cell lung cancer ( NSCLC ) ( 7 with no prior treatment , 9 patients in relapse following surgery/radiotherapy ) at a dose ( 648 mg/m2 divided over 3 days , repeated every 3 weeks ) determined by phase I trial .

Example answer:
{"entities": [{"text": "non-small cell lung cancer", "type": "Disease"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: High-dose intravenous methotrexate is an effective treatment for the induction of remission after meningeal relapse in acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: Older reports suggest an objective response rate of 8 % when 60-120 mg/m2 of cisplatin is administered every 3-4 weeks .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The combination of paclitaxel , cisplatin , and gemcitabine is well tolerated and shows high activity in metastatic NSCLC .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "NSCLC", "type": "Disease"}]}

Example input:
Sentence: Treatment was comprised of VNB , 25 mg/m ( 2 ) , plus GEM , 1000 mg/m ( 2 ) , both on Days 1 , 8 , and 15 every 28 days .

Example answer:
{"entities": [{"text": "VNB", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}]}

Example input:
Sentence: After 154 courses of therapy , the median dose intensity was 131 mg/m ( 2 ) for paclitaxel ( 97.3 % ) , 117 mg/m ( 2 ) for cisplatin ( 97.3 % ) , and 1378 mg/m ( 2 ) for gemcitabine ( 86.2 % ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Example input:
Sentence: In the present study , cis-platin ( 80-120 mg/m2BSA ) and 5-FU ( 1000 mg/m2BSA daily as a continuous infusion during 5 days ) were given to 76 patients before radiotherapy and surgery .

Example answer:
{"entities": [{"text": "cis-platin", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}]}

Example input:
Sentence: Treatment , given every 21 days for a maximum of three cycles , consisted of paclitaxel by 3-hour infusion followed the next day by a fixed dose of cisplatin ( 75 mg/m2 ) .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Between July 2001 and April 2004 , 24 patients with relapsed/refractory indolent lymphomas received thalidomide 200 mg daily with escalation by 100 mg daily every 1-2 weeks as tolerated , up to a maximum of 800 mg daily .

Example answer:
{"entities": [{"text": "lymphomas", "type": "Disease"}, {"text": "thalidomide", "type": "Chemical"}]}

Example input:
Sentence: Thirty-five consecutive chemotherapy-naive patients with Stage IV NSCLC and an Eastern Cooperative Oncology Group performance status of 0-2 were treated with a combination of paclitaxel ( 135 mg/m ( 2 ) given intravenously in 3 hours ) on Day 1 , cisplatin ( 120 mg/m ( 2 ) given intravenously in 6 hours ) on Day 1 , and gemcitabine ( 800 mg/m ( 2 ) given intravenously in 30 minutes ) on Days 1 and 8 , every 4 weeks .

Example answer:
{"entities": [{"text": "NSCLC", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}]}

Input:
Sentence: In this retrospective single-centre analysis , patients with relapsed or refractory HL treated with gemcitabine 1,000 mg/m ( 2 ) day ( D ) 1 , D8 and D15 ; methylprednisolone 1,000 mg D1-5 ; and cisplatin 100 mg/m ( 2 ) D15 , every 28 days ( GEM-P ) were included .

## Item bc5cdr:test:4500
Example input:
Sentence: The subcutaneous administration of 10 mg/kg of morphine-HC1 produced a marked increase in locomotor activity in mice .

Example answer:
{"entities": [{"text": "morphine-HC1", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Systemic cocaine ( 10 mg/kg ) significantly increased the locomotor activity of rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The locomotor activity was decreased from corresponding controls in all strains studied , except for the ICR mice , during an overnight drug-free period following the fourth amantadine treatment .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: At doses where alone , they produced no significant effects on locomotion , BD1018 , BD1063 and LR132 significantly attenuated the locomotor stimulatory effects of cocaine .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: ) , while apomorphine ( 1.5 mg/kg s.c. ) and amphetamine ( 2 mg/kg s.c. ) were used for studying climbing behavior and locomotor activities , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: Nicotine ( 1.0 mg/kg ) caused a significant increase in locomotor activity in rats that were habituated to the test environment , but had only a weak and delayed stimulant action in rats that were unfamiliar with the test environment .

Example answer:
{"entities": [{"text": "Nicotine", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Among these behavioral effects are decreases in food intake and decreases in amphetamine-induced locomotor activity .

Example answer:
{"entities": [{"text": "amphetamine-induced", "type": "Chemical"}]}

Example input:
Sentence: Compared with sham-operated controls , lesions significantly ( p < 0.25 ) blunted the early ( < 60 min ) free-field locomotor hypoactivity caused by nicotine ( 0.5 mg kg ( -1 ) , i.m .

Example answer:
{"entities": [{"text": "locomotor hypoactivity", "type": "Disease"}, {"text": "nicotine", "type": "Chemical"}]}

Example input:
Sentence: Nine days later locomotor activity was measured in response to a single low dose of amphetamine ( 0.5 mg/kg ) .

Example answer:
{"entities": [{"text": "amphetamine", "type": "Chemical"}]}

Input:
Sentence: RESULTS : In the amphetamine-induced locomotion test , there were significant increases in all movements compared with the amphetamine-free group .

## Item bc5cdr:test:4025
Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Higher optical density of an antigen assay predicts thrombosis in patients with heparin-induced thrombocytopenia .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}]}

Example input:
Sentence: The recommended starting dose for Phase II trials is 60 mg/m2 IV bolus every 3 weeks .

Example answer:
{"entities": []}

Example input:
Sentence: The ACTIVE-W ( Atrial Fibrillation Clopidogrel Trial with Irbesartan for Prevention of Vascular Events ) study has demonstrated that warfarin is superior to platelet therapy ( clopidogrel plus aspirin ) in the prevention af embolic events .

Example answer:
{"entities": [{"text": "Atrial Fibrillation", "type": "Disease"}, {"text": "Clopidogrel", "type": "Chemical"}, {"text": "Irbesartan", "type": "Chemical"}, {"text": "warfarin", "type": "Chemical"}, {"text": "clopidogrel", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "embolic events", "type": "Disease"}]}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND : Although different methods to prevent bruising and pain following the subcutaneous injection of heparin have been widely studied and described , the effect of injection duration on the occurrence of bruising and pain is little documented .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVES : To correlate optical density and percent inhibition of a two-step heparin-induced thrombocytopenia ( HIT ) antigen assay with thrombosis ; the assay utilizes reaction inhibition characteristics of a high heparin concentration .

Example answer:
{"entities": [{"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "HIT", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: PATIENTS AND METHODS : Patients with more than 50 % decrease in platelet count or thrombocytopenia ( < 150 x 10 ( 9 ) /L ) after exposure to heparin , who had a positive two-step antigen assay [ optical density ( OD ) > 0.4 and > 50 inhibition with high concentration of heparin ] were included in the study .

Example answer:
{"entities": [{"text": "thrombocytopenia", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Input:
Sentence: For further reduction of HIT type II , the use of intravenous heparin should be avoided and the prophylactic anticoagulation should be performed with low-molecular-weight heparin after normalization of platelet count .

## Item bc5cdr:test:4372
Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: The incidence calculation revealed that one of 215 therapeutic users had reactions , compared with one of 13,000 in the prophylaxis group , making the risk of neuropsychiatric reactions after mefloquine treatment 60 times higher than after prophylaxis .

Example answer:
{"entities": [{"text": "mefloquine", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Seventeen subjects who were genotyped as CYP2D6 extensive metabolizers were enrolled in this randomized , open-label , crossover study to receive a single oral dose of desipramine ( 50 mg ) on two separate occasions , once alone and once after multiple doses of cinacalcet ( 90 mg for 7 days ) .

Example answer:
{"entities": [{"text": "desipramine", "type": "Chemical"}, {"text": "cinacalcet", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Input:
Sentence: She was re-induced with nelarabine 1500 mg/m ( 2 ) on days 1 , 3 , and 5 with 1 dose of IT cytarabine 100 mg on day 2 as central nervous system ( CNS ) prophylaxis .

## Item bc5cdr:test:4367
Example input:
Sentence: Because of the rapid systemic clearance of BCNU ( 1,3-bis- ( 2-chloroethyl ) -1-nitrosourea ) , intra-arterial administration should provide a substantial advantage over intravenous administration for the treatment of malignant gliomas .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}, {"text": "1,3-bis- ( 2-chloroethyl ) -1-nitrosourea", "type": "Chemical"}, {"text": "malignant gliomas", "type": "Disease"}]}

Example input:
Sentence: We report on two fatal cases of accidental intrathecal vincristine instillation in a 5-year old girl with recurrent acute lymphoblastic leucemia and a 57-year old man with lymphoblastic lymphoma .

Example answer:
{"entities": [{"text": "vincristine", "type": "Chemical"}, {"text": "acute lymphoblastic leucemia", "type": "Disease"}, {"text": "lymphoblastic lymphoma", "type": "Disease"}]}

Example input:
Sentence: The pathogenesis of 5-fluorouracil neurotoxicity may be due to a Krebs cycle blockade by fluoroacetate and fluorocitrate , thiamine deficiency , or dihydrouracil dehydrogenase deficiency .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "fluoroacetate", "type": "Chemical"}, {"text": "fluorocitrate", "type": "Chemical"}, {"text": "thiamine", "type": "Chemical"}, {"text": "dihydrouracil", "type": "Chemical"}]}

Example input:
Sentence: Twenty children with acute lymphoblastic leukemia who developed meningeal disease were treated with a high-dose intravenous methotrexate regimen that was designed to achieve and maintain CSF methotrexate concentrations of 10 ( -5 ) mol/L without the need for concomitant intrathecal dosing .

Example answer:
{"entities": [{"text": "acute lymphoblastic leukemia", "type": "Disease"}, {"text": "meningeal disease", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: In conclusion mitochondrial toxicity is an early common event both in paclitaxel and cisplatin induced neurotoxicity .

Example answer:
{"entities": [{"text": "mitochondrial toxicity", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Intra-arterial BCNU chemotherapy for treatment of malignant gliomas of the central nervous system .

Example answer:
{"entities": [{"text": "BCNU", "type": "Chemical"}, {"text": "malignant gliomas", "type": "Disease"}]}

Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Input:
Sentence: Nelarabine neurotoxicity with concurrent intrathecal chemotherapy : Case report and review of literature .

## Item bc5cdr:test:4277
Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Physicians prescribing clonidine should monitor for bradycardia and advise patients about the high likelihood of initial drowsiness .

Example answer:
{"entities": [{"text": "clonidine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "drowsiness", "type": "Disease"}]}

Example input:
Sentence: A 40-year-old man with leukemia and no history of cardiac disease developed recurrent , brief episodes of apparent sinus arrest while receiving continuous-infusion cimetidine 50 mg/hour .

Example answer:
{"entities": [{"text": "leukemia", "type": "Disease"}, {"text": "cardiac disease", "type": "Disease"}, {"text": "sinus arrest", "type": "Disease"}, {"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: immediately before the induction of anaesthesia , to prevent arrhythmia and bradycardia following repeated doses of suxamethonium in children , was studied .

Example answer:
{"entities": [{"text": "arrhythmia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Example input:
Sentence: Forty seconds after injection of suxamethonium , bradycardia and cardiac arrest occurred .

Example answer:
{"entities": [{"text": "suxamethonium", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "cardiac arrest", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Input:
Sentence: We report syncope and bradycardia in an 11-year-old girl following administration of intranasal dexmedetomidine for sedation for a voiding cystourethrogram .
