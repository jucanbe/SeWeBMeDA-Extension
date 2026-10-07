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

## Item bc5cdr:test:2692
Input:
Sentence: The risk of ESRD associated with aspirin was related to the cumulated dose and duration of use , and it was particularly high among the subset of patients with vascular nephropathy as underlying disease [ 2.35 ( 1.17-4.72 ) ] .

## Item bc5cdr:test:3162
Input:
Sentence: Two patients needed a lateral tarsorrhaphy for persistent epithelial defects .

## Item bc5cdr:test:3281
Input:
Sentence: CONCLUSIONS : Sural nerve SAP amplitude reduction is a reliable and sensitive marker of degeneration and recovery of sensory fibres .

## Item bc5cdr:test:3156
Input:
Sentence: METHODS : Review of all cases of corneal ulcers associated with drug abuse seen at our institution from July 2006 to December 2006 .

## Item bc5cdr:test:2978
Input:
Sentence: CONCLUSIONS : Clinical outcomes with risperidone were equal to those with olanzapine , and response may be more stable .

## Item bc5cdr:test:3303
Input:
Sentence: Two control groups ( SH ( 6 ) , SH ( 12 ) ) received vehicle .

## Item bc5cdr:test:3306
Input:
Sentence: twice in a 3-week interval .

## Item bc5cdr:test:3022
Input:
Sentence: Three hours later the patient felt better , the frequency of PVC reduced to 4 - 5 x/minute and on the third day ECG was normal , potassium level was 3.34 meq/L .

## Item bc5cdr:test:3175
Input:
Sentence: Overall , as an entity , ATIN remains under-diagnosed , as symptoms resolve spontaneously if the medication is stopped .

## Item bc5cdr:test:3021
Input:
Sentence: Quinine infusion was discontinued and changed with sulfate quinine tablets .

## Item bc5cdr:test:3199
Input:
Sentence: Anti-HCV was negative in all of them .

## Item bc5cdr:test:3167
Input:
Sentence: Myo-inositol-1-phosphate ( MIP ) synthase inhibition : in-vivo study in rats .

## Item bc5cdr:test:3034
Input:
Sentence: A dramatic drop in blood pressure following prehospital GTN administration .

## Item bc5cdr:test:3218
Input:
Sentence: CYP-induced cystitis increased ( P < or = 0.001 ) p75 ( NTR ) expression in the superficial lateral and medial dorsal horn in L1-L2 and L6-S1 spinal segments .

## Item bc5cdr:test:3322
Input:
Sentence: This difference was also significant in the primary valve surgery and the high risk surgery subgroups ( 7.9 % vs 1.2 % , P = 0.003 ; 7.3 % vs 2.4 % , P = 0.035 , respectively ) .

## Item bc5cdr:test:3206
Input:
Sentence: BACKGROUND : In addition to blocking nociceptive input from surgical sites , long-acting local anesthetics might directly modulate inflammation .

## Item bc5cdr:test:3221
Input:
Sentence: Retrograde dye-tracing techniques with Fastblue were used to identify presumptive bladder afferent cells in the lumbosacral DRG .

## Item bc5cdr:test:2783
Input:
Sentence: Such a temporal relationship between the use of mirtazapine and the symptoms of RLS in our patient did not support a potentiating effect of domperione on mirtazapine-associated RLS .

## Item bc5cdr:test:2929
Input:
Sentence: We report a 23-year-old woman who developed acute renal failure following prolonged use of a proprietary Chinese herbal slimming pill that contained anthraquinone derivatives , extracted from Rhizoma Rhei ( rhubarb ) .

## Item bc5cdr:test:3225
Input:
Sentence: These studies demonstrate that p75 ( NTR ) expression in micturition reflexes is present constitutively and modified by bladder inflammation .

## Item bc5cdr:test:3091
Input:
Sentence: However , the direct benefits of this possible reshaping on LV function in the absence of underlying MR remain incompletely understood .

## Item bc5cdr:test:3228
Input:
Sentence: BACKGROUND : Azathioprine is widely used as an immunosuppressive drug .

## Item bc5cdr:test:2623
Input:
Sentence: There was a significant difference in insulin sensitivity index among groups ( F ( 33 ) = 10.66 ; P < .001 ) ( clozapine < olanzapine < risperidone ) , with subjects who received clozapine and olanzapine exhibiting significant insulin resistance compared with subjects who were treated with risperidone ( clozapine vs risperidone , t ( 33 ) = -4.29 ; P < .001 ; olanzapine vs risperidone , t ( 33 ) = -3.62 ; P = .001 [ P < .001 ] ) .

## Item bc5cdr:test:3359
Input:
Sentence: By routinely monitoring serum calcium levels , healthcare providers can improve the quality of life of this patient group .

## Item bc5cdr:test:3256
Input:
Sentence: RESULTS : Three patients ( 8.1 % ) in the unilateral group and 5 ( 13.5 % ) in the conventional group developed hypotension , P= 0.71 .

## Item bc5cdr:test:2875
Input:
Sentence: In this study , we evaluate the role DRD2 plays in chlorpromazine-induced EPS in schizophrenic patients .

## Item bc5cdr:test:3386
Input:
Sentence: DATA SOURCES : MEDLINE and Cochrane Library ( search dates , 1 January 2001 to 28 August 2008 ) , recent systematic reviews , reference lists of retrieved articles , and suggestions from experts .

## Item bc5cdr:test:2960
Input:
Sentence: The purpose of this study was to assess the use of galantamine , an acetylcholinesterase inhibitor and nicotinic receptor modulator , in the treatment of interfering behaviors in children with autism .

## Item bc5cdr:test:3118
Input:
Sentence: Temporary ipsilateral vocal nerve palsies due to local anesthetics have been described , however .

## Item bc5cdr:test:2957
Input:
Sentence: The results provide new insight into the potential role of ectopic hilar granule cells in the pilocarpine model of temporal lobe epilepsy .

## Item bc5cdr:test:3166
Input:
Sentence: Comprehensive care may provide the patient the opportunity to discontinue their substance abuse , improve their overall health , and prevent future corneal complications .

## Item bc5cdr:test:3219
Input:
Sentence: The number of p75 ( NTR ) -immunoreactive ( -IR ) cells in the lumbosacral dorsal root ganglia ( DRG ) also increased ( P < or = 0.05 ) with CYP-induced cystitis ( acute , intermediate , and chronic ) .

## Item bc5cdr:test:3282
Input:
Sentence: This electrophysiological parameter provides information about subclinical neurotoxic potential of thalidomide but is not helpful in predicting the appearance of sensory symptoms .

## Item bc5cdr:test:3295
Input:
Sentence: RESULTS : The 76 cases of CAD were compared with 152 controls .

## Item bc5cdr:test:2976
Input:
Sentence: Significantly more weight gain occurred with olanzapine than with risperidone : the increase in weight at 4 months relative to baseline weight was 17.3 % ( 95 % CI=14.2 % -20.5 % ) with olanzapine and 11.3 % ( 95 % CI=8.4 % -14.3 % ) with risperidone .

## Item bc5cdr:test:2975
Input:
Sentence: Extrapyramidal symptom severity scores were 1.4 ( 95 % CI=1.2-1.6 ) with risperidone and 1.2 ( 95 % CI=1.0-1.4 ) with olanzapine .

## Item bc5cdr:test:3419
Input:
Sentence: METHOD : A clinical case description .

## Item bc5cdr:test:3190
Input:
Sentence: BACKGROUND : Lamivudine is used for the treatment of chronic hepatitis B patients .

## Item bc5cdr:test:3325
Input:
Sentence: The 1-yr mortality was significantly higher after aprotinin treatment in the high risk surgery group ( 17.7 % vs 9.8 % , P = 0.034 ) .

## Item bc5cdr:test:2855
Input:
Sentence: Methadone dose , presence of cytochrome P-450 3A4 inhibitors , potassium level , and liver function contribute to QT prolongation .

## Item bc5cdr:test:3038
Input:
Sentence: Several minutes after the GTN the patient experienced a sudden drop in blood pressure and heart rate , this was rectified by atropine sulphate and a fluid challenge .

## Item bc5cdr:test:3339
Input:
Sentence: At the effective dose level of ( + ) -propranolol there was a significant prolongation of the PR interval of the electrocardiogram .

## Item bc5cdr:test:3379
Input:
Sentence: He was referred to us for neurological evaluation because he had difficulty in getting up from squatting position and was suspected to have myositis .

## Item bc5cdr:test:3397
Input:
Sentence: The dose of aspirin used in the RCTs varied , which prevented the estimation of the most appropriate dose for primary prevention .

## Item bc5cdr:test:3407
Input:
Sentence: Argatroban 0.5-1.2 microg/kg/min typically supports therapeutic aPTTs .

## Item bc5cdr:test:3278
Input:
Sentence: Five patients complained of paresthesias and leg cramps .

## Item bc5cdr:test:3173
Input:
Sentence: Non-steroidal anti-inflammatory drugs-associated acute interstitial nephritis with granular tubular basement membrane deposits .

## Item bc5cdr:test:3267
Input:
Sentence: Women were significantly more likely to experience lactic acidosis , while men were significantly more likely to experience immune reconstitution syndrome ( p < 0.05 ) .

## Item bc5cdr:test:3415
Input:
Sentence: fewer argatroban medication errors ) .

## Item bc5cdr:test:3405
Input:
Sentence: Contemporary experiences indicate that reduced doses are also needed in patients with conditions associated with hepatic hypoperfusion , e.g .

## Item bc5cdr:test:3474
Input:
Sentence: Primary objective was overall response rate ( ORR ) .

## Item bc5cdr:test:3170
Input:
Sentence: Lithium inhibits IMPase and valproate inhibits MIP synthase .

## Item bc5cdr:test:3502
Input:
Sentence: Seventy-nine percent had a normal or nonspecific ECG and 85 % had a TIMI score < 2 .

## Item bc5cdr:test:3418
Input:
Sentence: Methadone may aggravate this problem .

## Item bc5cdr:test:3423
Input:
Sentence: In the ER , his opiate level was 4497 ng/ml .

## Item bc5cdr:test:3365
Input:
Sentence: RESULTS : Controlled hypotension was achieved within a shorter period using laryngeal mask using lower rates of remifentanil infusion and lower total dose of remifentanil .

## Item bc5cdr:test:3426
Input:
Sentence: After MRI , we found cerebral ischemic infarction .

## Item bc5cdr:test:3201
Input:
Sentence: CONCLUSION : Although the natural occurrence of YMDD motif mutants in lamivudine-untreated patients with chronic hepatitis B has been reported , these mutants were not detected in Iranian lamivudine-untreated chronic hepatitis B patients .

## Item bc5cdr:test:3358
Input:
Sentence: PRACTICAL IMPLICATIONS : As much as 15 % of lithium-treated patients become hypercalcemic .

## Item bc5cdr:test:2316
Input:
Sentence: Multivariable logistic regression was used to estimate the odds ratio ( OR ) of pacemaker insertion associated with amiodarone use , controlling for baseline risk factors and exposure to sotalol , Class I antiarrhythmic agents , beta-blockers , calcium channel blockers , and digoxin .

## Item bc5cdr:test:3075
Input:
Sentence: In contrast , succimer treatment of rats not previously exposed to Pb produced lasting and pervasive cognitive and affective dysfunction comparable in magnitude to that produced by the higher Pb exposure regimen .

## Item bc5cdr:test:3353
Input:
Sentence: Long-term lithium therapy leading to hyperparathyroidism : a case report .

## Item bc5cdr:test:3250
Input:
Sentence: Efforts must therefore continue to be made to obviate this setback OBJECTIVE : To evaluate the cardiovascular and respiratory changes during unilateral and conventional spinal anaesthesia .

## Item bc5cdr:test:3464
Input:
Sentence: Her delirium resolved 3 days later .

## Item bc5cdr:test:2738
Input:
Sentence: In relatively healthy women , combined continuous HT significantly increased the risk of venous thromboembolism or coronary event ( after one year 's use ) , stroke ( after 3 years ) , breast cancer ( after 5 years ) and gallbladder disease .

## Item bc5cdr:test:3237
Input:
Sentence: Levetiracetam as an adjunct to phenobarbital treatment in cats with suspected idiopathic epilepsy .

## Item bc5cdr:test:3589
Input:
Sentence: Urine volume was increased , while urine osmolality and free water reabsorption were decreased .

## Item bc5cdr:test:3396
Input:
Sentence: LIMITATIONS : New evidence on aspirin for the primary prevention of CVD is limited .

## Item bc5cdr:test:3367
Input:
Sentence: Nonalcoholic fatty liver disease during valproate therapy .

## Item bc5cdr:test:3257
Input:
Sentence: Four ( 10.8 % ) patients in the conventional group and 1 ( 2.7 % ) in the unilateral group , P= 0.17 required epinephrine infusion to treat hypotension .

## Item bc5cdr:test:3478
Input:
Sentence: Overall disease control rate was 47.1 % .

## Item bc5cdr:test:3078
Input:
Sentence: However , they also suggest that succimer treatment should be strongly discouraged for children who do not have elevated tissue levels of Pb or other heavy metals .

## Item bc5cdr:test:3029
Input:
Sentence: During the follow-up of our patient , penicillamine was interrupted after the appearance of a lichenoid dermatitis , and zinc acetate permitted to continue the successful treatment of the patient without side-effects .

## Item bc5cdr:test:3403
Input:
Sentence: The objective of this review is to summarize practical considerations of argatroban therapy in HIT .

## Item bc5cdr:test:3065
Input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

## Item bc5cdr:test:3633
Input:
Sentence: Hippocampal integrity is essential for cognitive functions .

## Item bc5cdr:test:3518
Input:
Sentence: After an initially uneventful course after the transplant , the patient rapidly fell into deep coma .

## Item bc5cdr:test:3297
Input:
Sentence: The hazard decreased 0.3-fold ( 0.7-1.7 , P=0.385 ) with glimepiride , 0.4-fold ( 0.7-1.3 , P=0.192 ) with gliclazide , and 0.4-fold ( 0.7-1.1 , P=0.09 ) with either .

## Item bc5cdr:test:3560
Input:
Sentence: In particular this anti mitotic drug could reduce cell proliferation in the neurogenic regions of the adult brain .

## Item bc5cdr:test:3114
Input:
Sentence: Piperacillin-induced encephalopathy should be considered in any uremic patients with unexplained neurological manifestations .

## Item bc5cdr:test:3315
Input:
Sentence: The risks of aprotinin and tranexamic acid in cardiac surgery : a one-year follow-up of 1188 consecutive patients .

## Item bc5cdr:test:3549
Input:
Sentence: METHODS : We included data from people participating in the Vancouver Injection Drug Users Study who reported injecting illicit drugs at least once in the month before enrolment , lived in the greater Vancouver area , were HIV-negative at enrolment and completed at least 1 follow-up study visit .

## Item bc5cdr:test:3553
Input:
Sentence: The mean proportion of participants who reported daily smoking of crack cocaine increased from 11.6 % in period 1 to 39.7 % in period 3 .

## Item bc5cdr:test:3316
Input:
Sentence: BACKGROUND : Our aim was to investigate postoperative complications and mortality after administration of aprotinin compared to tranexamic acid in an unselected , consecutive cohort .

## Item bc5cdr:test:3514
Input:
Sentence: Late fulminant posterior reversible encephalopathy syndrome after liver transplant .

## Item bc5cdr:test:3561
Input:
Sentence: In contrast reports indicate that hippocampal dependent neurogenesis and cognition are enhanced by the SSRI antidepressant Fluoxetine .

## Item bc5cdr:test:3573
Input:
Sentence: Wild-type ( WT ) and ILK : liver-/- mice were given PB ( 0.1 % in drinking water ) for 10 days .

## Item bc5cdr:test:3460
Input:
Sentence: Flecainide had been started 2 weeks prior for atrial fibrillation .

## Item bc5cdr:test:2919
Input:
Sentence: Anticonvulsant effect of eslicarbazepine acetate ( BIA 2-093 ) on seizures induced by microperfusion of picrotoxin in the hippocampus of freely moving rats .

## Item bc5cdr:test:3406
Input:
Sentence: heart failure , yet are unnecessary for renal dysfunction , adult age , sex , race/ethnicity or obesity .

## Item bc5cdr:test:3385
Input:
Sentence: PURPOSE : To determine the benefits and harms of taking aspirin for the primary prevention of myocardial infarctions , strokes , and death .

## Item bc5cdr:test:3342
Input:
Sentence: The dose of ( - ) -propranolol was significantly smaller than that of ( + ) -propranolol in both species but much higher than that required to produce evidence of beta-blockade.8 .

## Item bc5cdr:test:3597
Input:
Sentence: During induction therapy , he suffered ileal perforation and ileostomy was performed .

## Item bc5cdr:test:3399
Input:
Sentence: CONCLUSION : Aspirin reduces the risk for myocardial infarction in men and strokes in women .

## Item bc5cdr:test:3468
Input:
Sentence: CONCLUSIONS : Supratherapeutic flecainide plasma concentrations may cause delirium .

## Item bc5cdr:test:3203
Input:
Sentence: A case of branch retinal vein occlusion associated with fluoxetine-induced secondary hypertension is described .

## Item bc5cdr:test:3615
Input:
Sentence: CCR2 is a chemokine receptor for CCL2 and their interaction mediates monocyte infiltration in the neuroinflammatory cascade triggered in different brain pathologies .

## Item bc5cdr:test:3603
Input:
Sentence: The study included 871 women with HIV who were recruited from 1993-1995 in four US cities .

## Item bc5cdr:test:2302
Input:
Sentence: Moreover , all adenosine receptor agonists : 2-p- ( 2-carboxyethyl ) phenethylamino-5'-N-ethylcarboxamidoadenosine ( CGS 21680 ) , A2A receptor agonist , N6-cyclopentyladenosine ( CPA ) , A1 receptor agonist , and 5'-N-ethylcarboxamidoadenosine ( NECA ) , A2/A1 receptor agonist significantly and dose-dependently decreased cocaine-induced locomotor activity .

## Item bc5cdr:test:3630
Input:
Sentence: Seizures also result in changes to CCR2 receptor expression in neurons and astrocytes .
