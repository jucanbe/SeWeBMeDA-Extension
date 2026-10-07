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

## Item bc5cdr:test:3201
Example input:
Sentence: Lamivudine for the prevention of hepatitis B virus reactivation in hepatitis-B surface antigen ( HBSAG ) seropositive cancer patients undergoing cytotoxic chemotherapy .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "hepatitis-B surface antigen", "type": "Chemical"}, {"text": "HBSAG", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: The objective of this study was to report our experience concerning the effectiveness of the prophylactic administration of lamivudine in hepatitis B virus surface antigen ( HBs Ag ) positive patients with rheumatologic disease .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis B virus surface antigen", "type": "Chemical"}, {"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic disease", "type": "Disease"}]}

Example input:
Sentence: In the prophylactic lamivudine group severe hepatitis were observed only in 1 patient ( 2.7 % ) of 37 patients ( p < 0.006 ) .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: Serum samples were PCR amplified with HBV reverse transcriptase ( RT ) primers , followed by direct sequencing across the tyrosine-methionine-aspartate-aspartate ( YMDD ) motif of the major catalytic region in the C domain of the HBV RT enzyme .

Example answer:
{"entities": [{"text": "tyrosine-methionine-aspartate-aspartate", "type": "Chemical"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "Chemical"}, {"text": "LAM-resistant", "type": "Chemical"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "LAM", "type": "Chemical"}, {"text": "HBeAg", "type": "Chemical"}]}

Example input:
Sentence: Lamivudine was added because of de nova hepatitis B infection during her follow-up .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B infection", "type": "Disease"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}]}

Example input:
Sentence: Differential impact of immune escape mutations G145R and P120T on the replication of lamivudine-resistant hepatitis B virus e antigen-positive and -negative strains .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B virus e", "type": "Chemical"}]}

Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "Chemical"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "Disease"}, {"text": "HIV co-infection", "type": "Disease"}]}

Input:
Sentence: CONCLUSION : Although the natural occurrence of YMDD motif mutants in lamivudine-untreated patients with chronic hepatitis B has been reported , these mutants were not detected in Iranian lamivudine-untreated chronic hepatitis B patients .

## Item bc5cdr:test:3295
Example input:
Sentence: RESULTS : One hundred sixty-five courses were administered , with a median of 3 .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The age-adjusted incidence rate ratio for CPA/EE versus conventional COCs was 2.20 [ 95 % confidence interval ( CI ) 1.35-3.58 ] .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Nineteen patients finished the trial , and in 18 cases the therapeutic result was considered very good to good .

Example answer:
{"entities": []}

Example input:
Sentence: Age-matched controls ( n = 14 ) were given only calcium .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: The historical controls consisted of 50 consecutive patients who underwent CT without prophylactic lamivudine .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Over the period 1993-1996 , 551 cases of VTE were identified in Germany and the UK along with 2066 controls .

Example answer:
{"entities": [{"text": "VTE", "type": "Disease"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: Totals of 128 cases and 650 controls were analysed for repeat use and 135 cases and 622 controls for switching patterns .

Example answer:
{"entities": []}

Input:
Sentence: RESULTS : The 76 cases of CAD were compared with 152 controls .

## Item bc5cdr:test:3359
Example input:
Sentence: There was a close parallel between the effect of vitamin D dose on artery calcification and the effect of vitamin D dose on the elevation of serum calcium , which suggests that vitamin D may induce artery calcification through its effect on serum calcium .

Example answer:
{"entities": [{"text": "vitamin D", "type": "Chemical"}, {"text": "artery calcification", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: We conclude that careful screening for medications and underlying conditions predisposing to hypocalcemia is recommended to help prevent severe reactions due to citrate toxicity .

Example answer:
{"entities": [{"text": "hypocalcemia", "type": "Disease"}, {"text": "citrate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Because Warfarin treatment had no effect on the elevation in serum calcium produced by vitamin D , the synergy between Warfarin and vitamin D is probably best explained by the hypothesis that Warfarin inhibits the activity of matrix Gla protein as a calcification inhibitor .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "calcification", "type": "Disease"}]}

Example input:
Sentence: The events are consistent with a severe reaction to calcium chelation by sodium citrate anticoagulant resulting in symptomatic systemic hypocalcemia .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "sodium citrate", "type": "Chemical"}, {"text": "hypocalcemia", "type": "Disease"}]}

Example input:
Sentence: Thus , clinicians should address patients ' concerns about adverse effects and attempt to choose medications that will improve their patients ' quality of life as well as overall health .

Example answer:
{"entities": []}

Example input:
Sentence: Myocardial calcium concentrations also were decreased ( 11.2 , 8.3 , and 8.9 mg. per 100 Gm .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Most patients showed improvement in individual parameters and global score of quality of life .

Example answer:
{"entities": []}

Example input:
Sentence: Myocardial concentrations of calcium also increased significantly ( 12.0 vs. 5.0 mg.per 100 Gm .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Infusions of calcium chloride sufficient to raise serum calcium concentrations 2 mEq .

Example answer:
{"entities": [{"text": "calcium chloride", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: Laboratory measurement of pre-procedure serum calcium levels in selected donors may identify cases requiring heightened vigilance .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Input:
Sentence: By routinely monitoring serum calcium levels , healthcare providers can improve the quality of life of this patient group .

## Item bc5cdr:test:2929
Example input:
Sentence: This study assessed the ability of IH636 grape seed proanthocyanidin extract ( GSPE ) to prevent acetaminophen ( AAP ) -induced nephrotoxicity , amiodarone ( AMI ) -induced lung toxicity , and doxorubicin ( DOX ) -induced cardiotoxicity in mice .

Example answer:
{"entities": [{"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}, {"text": "GSPE", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "AAP", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: We describe a 25-year-old woman with pre-existing mitral valve prolapse who developed intractable ventricular fibrillation after consuming a `` natural energy '' guarana health drink containing a high concentration of caffeine .

Example answer:
{"entities": [{"text": "mitral valve prolapse", "type": "Disease"}, {"text": "ventricular fibrillation", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}]}

Example input:
Sentence: We have reported a case of acute oliguric renal failure with hyperkalemia in a patient with cirrhosis , ascites , and cor pulmonale after indomethacin therapy .

Example answer:
{"entities": [{"text": "renal failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "ascites", "type": "Disease"}, {"text": "cor pulmonale", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: In the present work we assessed the effect of treatment of rats with gum Arabic on acute renal failure induced by gentamicin ( GM ) nephrotoxicity .

Example answer:
{"entities": [{"text": "gum Arabic", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "GM", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: A patient with cryptogenic cirrhosis and disseminated sporotrichosis developed acute renal failure immediately following the administration of amphotericin B on four separate occasions .

Example answer:
{"entities": [{"text": "cirrhosis", "type": "Disease"}, {"text": "sporotrichosis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "amphotericin B", "type": "Chemical"}]}

Example input:
Sentence: The case of a schizophrenic patient is reported to illustrate massive rhabdomyolysis and subsequent acute renal failure following molindone administration .

Example answer:
{"entities": [{"text": "schizophrenic", "type": "Disease"}, {"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "molindone", "type": "Chemical"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Input:
Sentence: We report a 23-year-old woman who developed acute renal failure following prolonged use of a proprietary Chinese herbal slimming pill that contained anthraquinone derivatives , extracted from Rhizoma Rhei ( rhubarb ) .

## Item bc5cdr:test:3339
Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: In the seventh patient , a permanent ventricular pacemaker was inserted and , despite continuation of procainamide therapy , polymorphous ventricular tachycardia did not reoccur .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol pretreatment for 15 days caused cardiac hypertrophy without affecting baseline blood pressure and heart rate .

Example answer:
{"entities": [{"text": "Isoproterenol", "type": "Chemical"}, {"text": "cardiac hypertrophy", "type": "Disease"}]}

Example input:
Sentence: For both experiments the drug intake led to significant increases in PRL secretion , acting preferentially on tonic secretion as pulse amplitude and frequency did not differ significantly from corresponding control values .

Example answer:
{"entities": []}

Example input:
Sentence: The effects of oral doses of diazepam ( single dose of 10 mg and a median dose of 30 mg/day for 2 weeks ) and propranolol ( single dose of 80 mg and a median dose of 240 mg/day for 2 weeks ) on psychological performance of patients with panic disorders and agoraphobia were investigated in a double-blind , randomized and crossover design .

Example answer:
{"entities": [{"text": "diazepam", "type": "Chemical"}, {"text": "propranolol", "type": "Chemical"}, {"text": "panic disorders", "type": "Disease"}, {"text": "agoraphobia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: In four patients , polymorphous ventricular tachycardia appeared after intravenous administration of 200 to 400 mg of procainamide for the treatment of sustained ventricular tachycardia .

Example answer:
{"entities": [{"text": "ventricular tachycardia", "type": "Disease"}, {"text": "procainamide", "type": "Chemical"}]}

Example input:
Sentence: Seven patients suffering from Parkinson 's disease ( PD ) with severely disabling dyskinesia received low-dose propranolol as an adjunct to the currently used medical treatment .

Example answer:
{"entities": [{"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "dyskinesia", "type": "Disease"}, {"text": "propranolol", "type": "Chemical"}]}

Example input:
Sentence: These results show that 15-day isoproterenol pretreatment not only abolished but reversed bromocriptine-induced tachycardia to bradycardia , an effect that is mainly related to further cardiac beta-adrenoceptor desensitization rather than to impairment of autonomic regulation of the heart .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: At the effective dose level of ( + ) -propranolol there was a significant prolongation of the PR interval of the electrocardiogram .

## Item bc5cdr:test:3065
Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Example input:
Sentence: Patients who developed renal insufficiency had lower baseline body weight and higher baseline serum creatinine , required higher doses of loop diuretics , and were more likely to be treated with thiazide diuretics than controls .

Example answer:
{"entities": [{"text": "renal insufficiency", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "thiazide", "type": "Chemical"}]}

Example input:
Sentence: Forty-nine percent of patients were pain free 2 h after rizatriptan , compared with 24.3 % treated with ergotamine/caffeine ( p < or = 0.001 ) , rizatriptan being superior within 1 h of treatment .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : A 50 % reduction in the incidence of akathisia when prochlorperazine was administered by means of 15-minute intravenous infusion versus a 2-minute intravenous push was not detected .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}, {"text": "prochlorperazine", "type": "Chemical"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Recurrence rates were 31.4 % with rizatriptan and 15.3 % with ergotamine/caffeine .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Patients who received enalapril experienced clinically and statistically significantly less symptomatic hypotension ( 5.2 % ) than the patients who received prazosin ( 12.9 % ) .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : A previous randomized controlled trial evaluating the use of spironolactone in heart failure patients reported a low risk of hyperkalemia ( 2 % ) and renal insufficiency ( 0 % ) .

Example answer:
{"entities": [{"text": "spironolactone", "type": "Chemical"}, {"text": "heart failure", "type": "Disease"}, {"text": "hyperkalemia", "type": "Disease"}, {"text": "renal insufficiency", "type": "Disease"}]}

Input:
Sentence: The incidence of hypokalemia was lower with VAL/HCTZ combinations ( 1.8 % -6.1 % ) than with HCTZ monotherapies ( 7.1 % -13.3 % ) .

## Item bc5cdr:test:3266
Example input:
Sentence: The results of serum liver function tests suggested hepatocellular injury in 10 ( 63 % ) ; the rest showed a mixed pattern .

Example answer:
{"entities": [{"text": "hepatocellular injury", "type": "Disease"}]}

Example input:
Sentence: Of our control group ( n= 50 ) , 21 patients ( 42 % ) were established hepatitis .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: Admission laboratory tests were as follows : alanine aminotransferase , 67 U/L ( reference range , 10-37 U/L ) ; aspartate aminotransferase , 98 U/L ( 10-40 U/L ) ; alkaline phosphatase , 513 U/L ( 0-270 U/L ) ; gamma-glutamyltransferase , 32 U/L ( 7-49 U/L ) ; amylase , 46 U/L ( 0-220 U/L ) ; total bilirubin , 20.1 mg/dL ( 0.2-1.0 mg/dL ) ; direct bilirubin , 14.8 mg/dL ( 0-0.3 mg/dL ) ; and albumin , 4.7 mg/dL ( 3.5-5.4 mg/dL ) .

Example answer:
{"entities": [{"text": "alanine", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: Twelve ( 24 % ) of them were evaluated as severe hepatitis .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: The development of severe anemia at 6 months post-CAB was predictable by the reduction of Hb baseline value of more than 2.5 g/dl after 3 months of CAB ( p = 0.01 ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: RESULTS : The mean hemoglobin ( Hb ) levels were significantly declined in all patients from baseline of 14.2 g/dl to 14.0 g/dl , 13.5 g/dl , 13.2 g/dl and 12.7 g/dl at 1 , 2 , 3 and 6 months post-CAB , respectively .

Example answer:
{"entities": []}

Example input:
Sentence: All patients were on a regular transfusion-chelation program maintaining a mean hemoglobin level of 9.5 gr/dl .

Example answer:
{"entities": []}

Example input:
Sentence: Severe hematologic toxicity ( neutrophil count < 1000/mm3 and/or hemoglobin < 8 g/dl ) occurred in 4 patients assigned to group I and 7 assigned to group II .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: At six months post-CAB , patients with severe anemia had a Hb mean value of 10.2 +/- 0.1 g/dl ( X +/- SE ) , whereas the other patients had mild anemia with Hb mean value of 13.2 +/- 0.17 ( X +/- SE ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Severe and clinically evident anemia of Hb < 11 g/dl with clinical symptoms was detected in 6 patients ( 14.3 % ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Input:
Sentence: Clinically significant anemia ( hemoglobin < 7 g/dL ) was observed in 5.4 % of patients ( CD4 , 165 cells/microL ) and hepatitis ( clinical jaundice with alanine aminotransferase > 5 times upper limits of normal ) in 3.5 % of patients ( CD4 , 260 cells/microL ) .

## Item bc5cdr:test:3379
Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: We studied a 37-year-old man who developed persistent segmental dystonia within 2 months after starting sulpiride therapy .

Example answer:
{"entities": [{"text": "dystonia", "type": "Disease"}, {"text": "sulpiride", "type": "Chemical"}]}

Example input:
Sentence: Clinically , the onset was characterized by the signs of opistothonus , sensory and motor dysfunction and ascending paralysis .

Example answer:
{"entities": [{"text": "paralysis", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 13-year-old boy was treated with ampicillin and gentamicin because of suspected septicemia .

Example answer:
{"entities": [{"text": "ampicillin", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "septicemia", "type": "Disease"}]}

Example input:
Sentence: He developed pneumonitis , pleural and pericardial effusions , and a predominantly proximal motor neuropathy .

Example answer:
{"entities": [{"text": "pneumonitis", "type": "Disease"}, {"text": "proximal motor neuropathy", "type": "Disease"}]}

Example input:
Sentence: Anaesthetists ' nightmare : masseter spasm after induction in an undiagnosed case of myotonia congenita .

Example answer:
{"entities": [{"text": "masseter spasm", "type": "Disease"}, {"text": "myotonia congenita", "type": "Disease"}]}

Example input:
Sentence: In 24 patients with this complication , the marked slowing of motor nerve conduction velocity and the electromyographic changes imply mainly a demyelinating disorder .

Example answer:
{"entities": [{"text": "demyelinating disorder", "type": "Disease"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Input:
Sentence: He was referred to us for neurological evaluation because he had difficulty in getting up from squatting position and was suspected to have myositis .

## Item bc5cdr:test:3140
Example input:
Sentence: In contrast to the protection provided by the putative antagonists , the well-characterized sigma receptor agonist di-o-tolylguanidine ( DTG ) and the novel sigma receptor agonist BD1031 ( 3R-1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -1,4-diazabicyclo [ 4.3.0 ] nonane ) each worsened the behavioral toxicity of cocaine .

Example answer:
{"entities": [{"text": "di-o-tolylguanidine", "type": "Chemical"}, {"text": "DTG", "type": "Chemical"}, {"text": "BD1031", "type": "Chemical"}, {"text": "3R-1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -1,4-diazabicyclo [ 4.3.0 ] nonane", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: There was no significant difference in the frequency of signs or symptoms between the two groups although neurotoxicity symptoms presented mostly with lower scores of severity in group G. However , this difference reached statistical significance only with regard to reported pain sensation ( P = 0.011 ) .

Example answer:
{"entities": [{"text": "neurotoxicity", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: Choreatiform hyperkinesias are known to be occasional movement abnormalities during intoxications with cocaine but not opiates .

Example answer:
{"entities": [{"text": "movement abnormalities", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Current animal models of obsessive-compulsive disorder ( OCD ) typically involve acute , drug-induced symptom provocation or a genetic association with stereotypies or anxiety .

Example answer:
{"entities": [{"text": "obsessive-compulsive disorder", "type": "Disease"}, {"text": "OCD", "type": "Disease"}, {"text": "anxiety", "type": "Disease"}]}

Example input:
Sentence: The Receiver Operative Characteristic Curve showed that OD > 1.27 in the isolated-HIT group had a significantly higher chance of developing thrombosis by day 30 .

Example answer:
{"entities": [{"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: cTnI ( ng/ml ) , CK-MB mass and CK remained unchanged in DOX rats compared with controls .

Example answer:
{"entities": [{"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: These analyses suggest that the higher risk observed for the newer OC in other studies may be the result of inadequate comparisons of pill users with different patterns of pill use .

Example answer:
{"entities": [{"text": "OC", "type": "Chemical"}]}

Example input:
Sentence: Visual analogue scores ( mean +/- SD ) during induction were lower in Groups L ( 3.3 +/- 2.5 ) and T ( 4.1 +/- 2.7 ) than in Group C ( 5.6 +/- 2.3 ) ; P = 0.0031 .

Example answer:
{"entities": []}

Example input:
Sentence: It is concluded that WR242511 should not be pursued as a pretreatment for CN poisoning unless the anti-CN characteristics of this compound can be successfully dissociated from those producing undesirable toxicity .

Example answer:
{"entities": [{"text": "WR242511", "type": "Chemical"}, {"text": "poisoning", "type": "Disease"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Eastern Cooperative Oncology Group performance status improved in 35 % of those patients with an initial value > 0 , whereas relief of at least 1 symptom without worsening of other symptoms was noted in 27 patients ( 55 % ) .

Example answer:
{"entities": []}

Input:
Sentence: The OC group was slower than CN when correctly identifying disgust .

## Item bc5cdr:test:3257
Example input:
Sentence: Phenylephrine but not ephedrine reduces frontal lobe oxygenation following anesthesia-induced hypotension .

Example answer:
{"entities": [{"text": "Phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}, {"text": "reduces frontal lobe oxygenation", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The release rate of epinephrine ( control , 6.7 +/- 0.6 ng/kg/min ) declined immediately during infusions of atrial natriuretic factor to a minimum of 49 +/- 5 % of control ( p less than 0.001 ) during 0.1 microgram/kg/min and to 63 +/- 5 % ( 0.1 greater than p greater than 0.05 ) or 95 +/- 13 % ( not significant ) during 0.3 or 1.0 microgram/kg/min .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}]}

Example input:
Sentence: Subsequent addition of phenylephrine infusion , sufficient to re-elevate mean arterial pressure to 106 +/- 4 mm Hg ( P less than 0.001 ) for 30 minutes , increased left ventricular filling pressure to 17 +/- 2 mm Hg ( P less than 0.05 ) and also significantly increased sigmaST ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension to an average MAP of 50-55 mm Hg was induced by increasing the dose of isoflurane , and maintained at an inspired concentration of 2.2 +/- 0.2 % .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "Hg", "type": "Chemical"}, {"text": "isoflurane", "type": "Chemical"}]}

Example input:
Sentence: Mean arterial pressure ( as a percentage of control +/- SEM ) during randomized infusions of 0.03 , 0.1 , 0.3 , or 1.0 microgram/kg/min was 99 +/- 1 , 95 +/- 1 ( p less than 0.05 ) , 93 +/- 1 ( p less than 0.01 ) , or 79 +/- 6 % ( p less than 0.001 ) , respectively , but no tachycardia and no augmentation of the norepinephrine release rate ( up to 0.3 microgram/kg/min ) were observed , which is in contrast to comparable hypotension induced by hydralazine or nitroglycerin .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "hydralazine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Example input:
Sentence: However , a bolus of epinephrine injected through an alternative catheter provoked a hypertensive crisis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : The utilization of phenylephrine to correct hypotension induced by anesthesia has a negative impact on S ( c ) O ( 2 ) while ephedrine maintains frontal lobe oxygenation potentially related to an increase in CO .

Example answer:
{"entities": [{"text": "phenylephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Input:
Sentence: Four ( 10.8 % ) patients in the conventional group and 1 ( 2.7 % ) in the unilateral group , P= 0.17 required epinephrine infusion to treat hypotension .

## Item bc5cdr:test:3218
Example input:
Sentence: In streptozotocin-induced hyperalgesia , inducible NO synthase participates in pronociceptive activity of bradykinin , whereas in vincristine-induced hyperalgesia bradykinin seemed to activate neuronal NO synthase pathway .

Example answer:
{"entities": [{"text": "streptozotocin-induced", "type": "Chemical"}, {"text": "hyperalgesia", "type": "Disease"}, {"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "vincristine-induced", "type": "Chemical"}]}

Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: CY caused hemorrhagic cystitis in 40 % of rats , but it did not cause this complication when combined with 5-FU and MTX .

Example answer:
{"entities": [{"text": "CY", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}]}

Example input:
Sentence: The Calcineurin-inhibitor Induced Pain Syndrome ( CIPS ) is a rare but severe side effect of cyclosporine or tacrolimus and is accurately diagnosed by its typical presentation , magnetic resonance imaging and bone scans .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "CIPS", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: Whether or not the neuronal transmission may be affected by cystitis was presently investigated .

Example answer:
{"entities": [{"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Thus , in cystitis substantial changes of the efferent functional responses occur .

Example answer:
{"entities": [{"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: In vitro characterization of parasympathetic and sympathetic responses in cyclophosphamide-induced cystitis in the rat .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Input:
Sentence: CYP-induced cystitis increased ( P < or = 0.001 ) p75 ( NTR ) expression in the superficial lateral and medial dorsal horn in L1-L2 and L6-S1 spinal segments .

## Item bc5cdr:test:3219
Example input:
Sentence: The expression of arginine vasopressin ( AVP ) gene in the paraventricular ( PVN ) and supraoptic nuclei ( SON ) was investigated in rats with lithium ( Li ) -induced polyuria , using in situ hybridization histochemistry and radioimmunoassay .

Example answer:
{"entities": [{"text": "arginine vasopressin", "type": "Chemical"}, {"text": "AVP", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "Li", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}]}

Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: The electrophysiological recording in vitro showed that Rg1 restored the LTP in slices from the rats treated with morphine , but not changed LTP in the slices from normal saline- or morphine/Rg1-treated rats ; this restoration could be inhibited by N-methyl-D-aspartate ( NMDA ) receptor antagonist MK801 .

Example answer:
{"entities": [{"text": "Rg1", "type": "Chemical"}, {"text": "morphine", "type": "Chemical"}, {"text": "morphine/Rg1-treated", "type": "Chemical"}, {"text": "N-methyl-D-aspartate", "type": "Chemical"}, {"text": "NMDA", "type": "Chemical"}, {"text": "MK801", "type": "Chemical"}]}

Example input:
Sentence: Sulpiride induced only SOCS-1 in the medial preoptic area , where GnRH neurons are regulated , but in the arcuate nucleus and choroid plexus , PRL-R , SOCS-3 , and CIS mRNA levels were also induced .

Example answer:
{"entities": [{"text": "Sulpiride", "type": "Chemical"}]}

Example input:
Sentence: This study shows that prolonged analgesic treatment in Fischer 344 rats causes progressive and irreversible damage to the interstitial matrix and type 1 interstitial cells leading to RPN .

Example answer:
{"entities": [{"text": "RPN", "type": "Disease"}]}

Example input:
Sentence: Thus , in cystitis substantial changes of the efferent functional responses occur .

Example answer:
{"entities": [{"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: CY caused hemorrhagic cystitis in 40 % of rats , but it did not cause this complication when combined with 5-FU and MTX .

Example answer:
{"entities": [{"text": "CY", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "MTX", "type": "Chemical"}]}

Example input:
Sentence: In vitro characterization of parasympathetic and sympathetic responses in cyclophosphamide-induced cystitis in the rat .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: In cyclophosphamide-induced cystitis in the rat , detrusor function is impaired and the expression and effects of muscarinic receptors altered .

Example answer:
{"entities": [{"text": "cyclophosphamide-induced", "type": "Chemical"}, {"text": "cystitis", "type": "Disease"}]}

Input:
Sentence: The number of p75 ( NTR ) -immunoreactive ( -IR ) cells in the lumbosacral dorsal root ganglia ( DRG ) also increased ( P < or = 0.05 ) with CYP-induced cystitis ( acute , intermediate , and chronic ) .

## Item bc5cdr:test:3478
Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: One patient had complete response , seven had stable disease , none had partial response and five had progressive disease .

Example answer:
{"entities": []}

Example input:
Sentence: The majority of patients ( > 60 % ) experienced no change in their disease status from baseline .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate was 26 % ( 95 % confidence interval , 15-41 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The overall objective response rate was 7.6 % .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate is 72 % .

Example answer:
{"entities": []}

Example input:
Sentence: The excess event rate was 1.8 per 1,000 woman-years ( 95 % CI -0.5-4.1 ) , and the number needed to treat to cause 1 event was 170 ( 95 % CI 100-582 ) over 3.3 years .

Example answer:
{"entities": []}

Example input:
Sentence: According to intention-to-treat , the overall response rate was 71.4 % ( 95 % CI , 53 .

Example answer:
{"entities": []}

Example input:
Sentence: The prevalence rate for CIMD was 12 % at baseline .

Example answer:
{"entities": [{"text": "CIMD", "type": "Disease"}]}

Example input:
Sentence: The overall response rate ( World Health Organization [ WHO ] criteria ) was 15 % ( CR , 2 % ; PR 13 % ; 95 % CI , 6 % to 29 % ) .

Example answer:
{"entities": []}

Input:
Sentence: Overall disease control rate was 47.1 % .

## Item bc5cdr:test:3474
Example input:
Sentence: Response rates according to three sets of criteria were greater with the standard dose ( 55 % -60 % ) than the low dose ( 25 % -35 % ) and placebo ( 25 % -30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Six partial responses were observed for an overall response rate of 16 % .

Example answer:
{"entities": []}

Example input:
Sentence: The primary response variable was based on central reading of 24 hour ambulatory electrocardiographic recordings and was defined as the occurrence of 30 or more single premature ventricular complexes in any two consecutive 30 minute blocks or one or more runs of two or more premature ventricular complexes in the entire 24 hour electrocardiographic recording .

Example answer:
{"entities": []}

Example input:
Sentence: According to intention-to-treat , the overall response rate was 71.4 % ( 95 % CI , 53 .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate was 26 % ( 95 % confidence interval , 15-41 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: An objective response was observed in 73.5 % of the patients ( 95 % confidence interval [ CI ] , 55.6-87.1 % ) , including 4 complete responses ( 11.7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate is 72 % .

Example answer:
{"entities": []}

Example input:
Sentence: The overall response rate ( World Health Organization [ WHO ] criteria ) was 15 % ( CR , 2 % ; PR 13 % ; 95 % CI , 6 % to 29 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: The overall objective response rate was 7.6 % .

Example answer:
{"entities": []}

Input:
Sentence: Primary objective was overall response rate ( ORR ) .

## Item bc5cdr:test:3267
Example input:
Sentence: Blood pressure ( BP ) is more salt sensitive in men than in premenopausal women .

Example answer:
{"entities": [{"text": "salt", "type": "Chemical"}]}

Example input:
Sentence: Combined antiretroviral therapy causes cardiomyopathy and elevates plasma lactate in transgenic AIDS mice .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "lactate", "type": "Chemical"}, {"text": "AIDS", "type": "Disease"}]}

Example input:
Sentence: Radiotelemetric BP was similar between males and castrated rats on LS diet .

Example answer:
{"entities": []}

Example input:
Sentence: In this study , the hypothesis was tested that there is a sexual dimorphism in HS-induced upregulation of intrarenal angiotensinogen mediated by testosterone that also causes increases in BP and renal injury .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: Impotence was more common among male patients than controls and was found to be associated with co-morbidity and the taking of methotrexate .

Example answer:
{"entities": [{"text": "Impotence", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: In one patient , reintroduction of FK506 led to rapid recurrence of MAHA .

Example answer:
{"entities": [{"text": "FK506", "type": "Chemical"}, {"text": "MAHA", "type": "Disease"}]}

Example input:
Sentence: HS diet for 4 wk caused a progressive increase in BP , protein and albumin excretion , and glomerular sclerosis in male DS rats , which were attenuated by castration .

Example answer:
{"entities": [{"text": "glomerular sclerosis", "type": "Disease"}]}

Example input:
Sentence: The full syndrome of subacute myelo-optic neuropathy was more frequent in women , but they tended to have taken greater quantities of the drug .

Example answer:
{"entities": []}

Example input:
Sentence: Two subsets of patients were identified from this latter group : the first included four patients ( 5 % of the total population ) who developed major toxicity resulting in Fanconi 's syndrome ( TDFS ) ; and the second group included five patients with elevated beta 2 microglobulinuria and low phosphate reabsorption .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}, {"text": "Fanconi 's syndrome", "type": "Disease"}, {"text": "TDFS", "type": "Disease"}, {"text": "phosphate", "type": "Chemical"}]}

Example input:
Sentence: On a low-salt ( LS ) diet , male DS had higher levels of intrarenal angiotensinogen mRNA than females .

Example answer:
{"entities": []}

Input:
Sentence: Women were significantly more likely to experience lactic acidosis , while men were significantly more likely to experience immune reconstitution syndrome ( p < 0.05 ) .

## Item bc5cdr:test:3278
Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: We report an undiagnosed case of myotonia congenita in a 24-year-old previously healthy primigravida , who developed life threatening masseter spasm following a standard dose of intravenous suxamethonium for induction of anaesthesia .

Example answer:
{"entities": [{"text": "myotonia congenita", "type": "Disease"}, {"text": "masseter spasm", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Transient neurologic symptoms after spinal anesthesia : a lower incidence with prilocaine and bupivacaine than with lidocaine .

Example answer:
{"entities": [{"text": "Transient neurologic symptoms", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Nine of 30 patients receiving lidocaine experienced TNSs , 1 of 30 patients receiving prilocaine ( P = 0.03 ) had them , and none of 30 patients receiving bupivacaine had TNSs .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "TNSs", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: Three hours later , she complained of perineal numbness and lower extremity weakness .

Example answer:
{"entities": [{"text": "numbness", "type": "Disease"}, {"text": "lower extremity weakness", "type": "Disease"}]}

Example input:
Sentence: CLINICAL FEATURES : A 50-year-old woman with low back and right leg pain was scheduled for epidural steroid injection .

Example answer:
{"entities": [{"text": "steroid", "type": "Chemical"}]}

Example input:
Sentence: Twenty patients were asked to quantify the severity of pain after receiving standard lidocaine in one femoral area and buffered lidocaine in the opposite femoral area .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: The surgery and anaesthesia were uneventful , but 3 days after surgery , the patient reported an area of hypoaesthesia over L3-L4 dermatomes of the leg which had been operated on ( loss of pinprick sensation ) without reduction in muscular strength .

Example answer:
{"entities": [{"text": "loss of pinprick sensation", "type": "Disease"}]}

Example input:
Sentence: A 49-year-old woman was transferred to our department because of quadriparesis , lancinating pain , sensory loss , and paresthesia of the distal limbs .

Example answer:
{"entities": [{"text": "quadriparesis", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "sensory loss", "type": "Disease"}, {"text": "paresthesia", "type": "Disease"}]}

Example input:
Sentence: Although the United States Food and Drug Administration banned its use for nocturnal leg cramps due to lack of safety and efficacy , quinine is widely available in beverages including tonic water and bitter lemon .

Example answer:
{"entities": [{"text": "nocturnal leg cramps", "type": "Disease"}, {"text": "quinine", "type": "Chemical"}]}

Input:
Sentence: Five patients complained of paresthesias and leg cramps .

## Item bc5cdr:test:3397
Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: However , three case control studies , one each in North Carolina , northern Maryland , and West Berlin , Germany , showed that habitual use of acetaminophen is also associated with chronic renal failure and ESRD , with a relative risk in the range of 2 to 4 .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Six epidemiologic studies in the United States and Europe indicate that habitual use of phenacetin is associated with the development of chronic renal failure and end-stage renal disease ( ESRD ) , with a relative risk in the range of 4 to 19 .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "end-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: A control group was included for comparison with the lower dose range of glycopyrrolate and atropine .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}]}

Example input:
Sentence: Patients were divided into three groups : Controls , no CRF or ESRD , n=748 ; CRF , sustained serum creatinine > 2.5 mg/dl , n=41 ; and ESRD , n=45 .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}]}

Example input:
Sentence: These studies suggest that both phenacetin and acetaminophen may contribute to the burden of ESRD , with the risk of the latter being somewhat less than that of the former .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: In patients requiring the concurrent use of statins and CYP3A4 inhibitors , pravastatin , fluvastatin , and rosuvastatin carry the lowest risk of drug interactions ; atorvastatin carries moderate risk , whereas simvastatin and lovastatin have the highest risk and should be avoided in patients taking concomitant CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "pravastatin", "type": "Chemical"}, {"text": "fluvastatin", "type": "Chemical"}, {"text": "rosuvastatin", "type": "Chemical"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "lovastatin", "type": "Chemical"}]}

Example input:
Sentence: Pooled data from trials comparing antithrombotic treatment with placebo have shown that warfarin reduces the risk of stroke by 62 % , and that aspirin alone reduces the risk by 22 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "stroke", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}]}

Example input:
Sentence: A high proportion of patients had consumed ATT empirically , which could have been prevented .

Example answer:
{"entities": []}

Example input:
Sentence: Overall , in high-risk patients , warfarin is superior to aspirin in preventing strokes , with a relative risk reduction of 36 % .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "aspirin", "type": "Chemical"}, {"text": "strokes", "type": "Disease"}]}

Input:
Sentence: The dose of aspirin used in the RCTs varied , which prevented the estimation of the most appropriate dose for primary prevention .

## Item bc5cdr:test:3502
Example input:
Sentence: Of 24 evaluable patients , two achieved a complete remission and one achieved a partial remission for an overall response rate of 12.5 % ( 95 % confidence interval : 2.6-32.4 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: His bundle recordings showed an atrial tachycardia with intermittent exit block and greatly prolonged BH and HV intervals ( 40 and 100 msec , respectively ) .

Example answer:
{"entities": [{"text": "atrial tachycardia", "type": "Disease"}]}

Example input:
Sentence: Of the 59 cases , 26 ( 44 % ) had a fatal outcome , compared to 136 ( 25 % ) among the non-warfarin patients ( p < 0.01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Fifty-eight patients ( 78 % ) had normal renal tests , whereas 16 patients ( 22 % ) had renal abnormalities .

Example answer:
{"entities": [{"text": "renal abnormalities", "type": "Disease"}]}

Example input:
Sentence: An objective response was observed in 73.5 % of the patients ( 95 % confidence interval [ CI ] , 55.6-87.1 % ) , including 4 complete responses ( 11.7 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: RESULTS : There were more incidents of bradycardia in subjects treated with clonidine compared with those not treated with clonidine ( 17.5 % versus 3.4 % ; p =.02 ) , but no other significant group differences regarding electrocardiogram and other cardiovascular outcomes .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Compared to controls , aortic regurgitation ( OR : 3.1 ; 95 % IC : 1.1-8.8 ) and mitral regurgitation ( OR : 10.7 ; 95 % IC : 2.1-53 ) were more frequent in PD patients ( tricuspid : NS ) .

Example answer:
{"entities": [{"text": "aortic regurgitation", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Also the frequency of abnormal electro-diagnostic findings showed similarity between the two groups ( G : 7/23 = 30.4 % ; P : 6/20 = 30 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: A frequency of bradycardia of 50 % was noted in the control group , but this was not significantly different from the frequency with the active drugs .

Example answer:
{"entities": [{"text": "bradycardia", "type": "Disease"}]}

Input:
Sentence: Seventy-nine percent had a normal or nonspecific ECG and 85 % had a TIMI score < 2 .

## Item bc5cdr:test:3282
Example input:
Sentence: Abnormal brain responses to somatosensory stimuli have been found in patients with hyperalgesia as well as in normal subjects during experimental central sensitization .

Example answer:
{"entities": [{"text": "hyperalgesia", "type": "Disease"}]}

Example input:
Sentence: Diffusion-weighted imaging may be useful in predicting the outcomes of the lesions of tacrolimus-induced neurotoxicity .

Example answer:
{"entities": [{"text": "tacrolimus-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Both plasma pethidine and norpethidine were elevated in the range associated with clinical manifestations of central nervous system excitation .

Example answer:
{"entities": [{"text": "pethidine", "type": "Chemical"}, {"text": "norpethidine", "type": "Chemical"}]}

Example input:
Sentence: An electroencephalogram showed continuous , generalized irregular slowing with admixed periodic triphasic waves indicating symptomatic encephalopathy .

Example answer:
{"entities": [{"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: THP exhibited an antipsychotic-like profile by potentiating haloperidol-induced catalepsy , reducing amphetamine-induced hyperactivity and reducing apomorphine-induced climbing in mice .

Example answer:
{"entities": []}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: The gamma-aminobutyric acid-transmitted thalamocortical circuitry accounts for a major part of the underlying neurophysiology of the absence epilepsy .

Example answer:
{"entities": [{"text": "gamma-aminobutyric", "type": "Chemical"}, {"text": "absence epilepsy", "type": "Disease"}]}

Example input:
Sentence: There was no significant difference in the frequency of signs or symptoms between the two groups although neurotoxicity symptoms presented mostly with lower scores of severity in group G. However , this difference reached statistical significance only with regard to reported pain sensation ( P = 0.011 ) .

Example answer:
{"entities": [{"text": "neurotoxicity", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Input:
Sentence: This electrophysiological parameter provides information about subclinical neurotoxic potential of thalidomide but is not helpful in predicting the appearance of sensory symptoms .

## Item bc5cdr:test:3415
Example input:
Sentence: Captopril may , by the same mechanism , reduce the increase in glomerular filtration that is known to occur after an injection of thrombin , thereby diminishing the aggregation of fibrin monomers in the glomeruli , with the result that less fibrin will be deposited and thus less kidney damage will be produced .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "kidney damage", "type": "Disease"}]}

Example input:
Sentence: Faster relief of headache was the most important reason for preference , cited by 67.3 % of patients preferring rizatriptan and 54.2 % of patients who preferred ergotamine/caffeine .

Example answer:
{"entities": [{"text": "headache", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Treatment-related adverse events ( AEs ) occurred in 44 % and 52 % , 57 % , and 41 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: STUDY DESIGN AND METHODS : Plasma samples from before and after CPB were analyzed postoperatively for argatroban concentration using a modified ecarin clotting time ( ECT ) assay .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Correlation of plasma argatroban concentration versus the patient 's coagulation variables and clinical course suggest that prolonged elevated levels of plasma argatroban may have contributed to the patient 's extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Unexpectedly high concentrations of argatroban were measured in these samples ( range , 0-32 microg/mL ) , and a prolonged plasma argatroban half life ( t ( 1/2 ) ) of 514 minutes was observed ( published elimination t ( 1/2 ) is 39-51 minutes [ < or = 181 minutes with hepatic impairment ] ) .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "hepatic impairment", "type": "Disease"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: This is the first report to measure plasma argatroban concentration in the context of CPB and extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Input:
Sentence: fewer argatroban medication errors ) .

## Item bc5cdr:test:3190
Example input:
Sentence: Mutations associated with lamivudine-resistance in therapy-na ve hepatitis B virus ( HBV ) infected patients with and without HIV co-infection : implications for antiretroviral therapy in HBV and HIV co-infected South African patients .

Example answer:
{"entities": [{"text": "lamivudine-resistance", "type": "Chemical"}, {"text": "hepatitis B virus ( HBV ) infected", "type": "Disease"}, {"text": "HIV co-infection", "type": "Disease"}]}

Example input:
Sentence: In the prophylactic lamivudine group severe hepatitis were observed only in 1 patient ( 2.7 % ) of 37 patients ( p < 0.006 ) .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: HBV lamivudine-resistant strains were detected in 3 of 15 mono-infected chronic hepatitis B patients and 10 of 20 HBV-HIV co-infected patients .

Example answer:
{"entities": [{"text": "lamivudine-resistant", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}]}

Example input:
Sentence: In this study , cancer patients who have solid and hematological malignancies with chronic HBV infection received the antiviral agent lamivudine prior and during CT compared with historical control group who did not receive lamivudine .

Example answer:
{"entities": [{"text": "cancer", "type": "Disease"}, {"text": "hematological malignancies", "type": "Disease"}, {"text": "HBV infection", "type": "Disease"}, {"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Prophylactic administration of lamivudine in patients who required immunosuppressive therapy seems to be safe , well tolerated and effective in preventing HBV reactivation .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: Lamivudine was added because of de nova hepatitis B infection during her follow-up .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B infection", "type": "Disease"}]}

Example input:
Sentence: Our study suggests that prophylactic lamivudine significantly decreases the incidence of HBV reactivation and overall morbidity in cancer patients during and after immunosuppressive therapy .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: The objectives were to assess the efficacy of lamivudine in reducing the incidence of HBV reactivation , and diminishing morbidity and mortality during CT. Two groups were compared in this study .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}]}

Example input:
Sentence: The objective of this study was to report our experience concerning the effectiveness of the prophylactic administration of lamivudine in hepatitis B virus surface antigen ( HBs Ag ) positive patients with rheumatologic disease .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis B virus surface antigen", "type": "Chemical"}, {"text": "HBs Ag", "type": "Chemical"}, {"text": "rheumatologic disease", "type": "Disease"}]}

Example input:
Sentence: Lamivudine for the prevention of hepatitis B virus reactivation in hepatitis-B surface antigen ( HBSAG ) seropositive cancer patients undergoing cytotoxic chemotherapy .

Example answer:
{"entities": [{"text": "Lamivudine", "type": "Chemical"}, {"text": "hepatitis B", "type": "Disease"}, {"text": "hepatitis-B surface antigen", "type": "Chemical"}, {"text": "HBSAG", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Input:
Sentence: BACKGROUND : Lamivudine is used for the treatment of chronic hepatitis B patients .

## Item bc5cdr:test:3405
Example input:
Sentence: These 6 patients had both renal and liver dysfunction ( P less than 0.05 ) , as well as cimetidine trough-concentrations of more than 1.25 microgram/ml ( P less than 0.05 ) .

Example answer:
{"entities": [{"text": "cimetidine", "type": "Chemical"}]}

Example input:
Sentence: In the prophylactic lamivudine group severe hepatitis were observed only in 1 patient ( 2.7 % ) of 37 patients ( p < 0.006 ) .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Example input:
Sentence: We propose that the paracetamol dose should not exceed 2 g/day in such patients and that their liver function should be monitored closely while being treated with paracetamol .

Example answer:
{"entities": [{"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: Myelosuppression was more in patients with hepatic dysfunction .

Example answer:
{"entities": [{"text": "Myelosuppression", "type": "Disease"}, {"text": "hepatic dysfunction", "type": "Disease"}]}

Example input:
Sentence: Combined effects of prolonged prostaglandin E1-induced hypotension and haemodilution on human hepatic function .

Example answer:
{"entities": [{"text": "prostaglandin", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: Combined effects of prolonged prostaglandin E1 ( PGE1 ) -induced hypotension and haemodilution on hepatic function were studied in 30 patients undergoing hip surgery .

Example answer:
{"entities": [{"text": "prostaglandin E1", "type": "Chemical"}, {"text": "PGE1", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: Patients with a DBP reduction of > or =20 % in the high-dose group had a significantly increased adjusted OR for the compound outcome variable death or dependency ( Barthel Index < 60 ) ( n/N=25/26 , OR 10 .

Example answer:
{"entities": [{"text": "DBP reduction", "type": "Disease"}, {"text": "death", "type": "Disease"}]}

Example input:
Sentence: The results suggest that a prolonged combination of more than 120 min of PGE1-induced hypotension and moderate haemodilution would cause impairment of hepatic function .

Example answer:
{"entities": [{"text": "PGE1-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}, {"text": "impairment of hepatic function", "type": "Disease"}]}

Input:
Sentence: Contemporary experiences indicate that reduced doses are also needed in patients with conditions associated with hepatic hypoperfusion , e.g .

## Item bc5cdr:test:3297
Example input:
Sentence: In phase A , extrapyramidal signs tended to be greater with the standard dose than in the other two conditions , primarily because of a subgroup ( 20 % ) who developed moderate to severe signs .

Example answer:
{"entities": [{"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: Mean post-SCr increases were significantly less with iopamidol ( all patients : 0.07 versus 0.12 mg/dL , 6.2 versus 10.6 micromol/L , P=0.03 ; patients with diabetes : 0.07 versus 0.16 mg/dL , 6.2 versus 14.1 micromol/L , P=0.01 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "diabetes", "type": "Disease"}]}

Example input:
Sentence: SCr increases > or = 0.5 mg/dL occurred in 4.4 % ( 9 of 204 patients ) after iopamidol and 6.7 % ( 14 of 210 patients ) after iodixanol ( P=0.39 ) , whereas rates of SCr increases > or = 25 % were 9.8 % and 12.4 % , respectively ( P=0.44 ) .

Example answer:
{"entities": [{"text": "iopamidol", "type": "Chemical"}, {"text": "iodixanol", "type": "Chemical"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Enalapril treatment blunted but did not prevent reduction in GFR in group 4 ( 0.86 +/- 0.15 ml/min at 4 months , 0.69 +/- 0.13 ml/min at 6 months , both P less than 0.05 vs. group 3 ) .

Example answer:
{"entities": [{"text": "Enalapril", "type": "Chemical"}]}

Example input:
Sentence: Interestingly , all the drugs , such as , AAP , AMI and DOX induced apoptotic death in addition to necrosis in the respective organs which was very effectively blocked by GSPE .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}, {"text": "necrosis", "type": "Disease"}, {"text": "GSPE", "type": "Chemical"}]}

Example input:
Sentence: Risk in the raloxifene group was higher than in the placebo group for the first 2 years , but decreased to about the same rate as in the placebo group thereafter .

Example answer:
{"entities": [{"text": "raloxifene", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

Example answer:
{"entities": []}

Example input:
Sentence: With last observations carried forward ( LOCF ) , mean Positive and Negative Syndrome Scale total score reductions from baseline to endpoint were significantly greater with asenapine at 5 mg BID ( -16.2 ) and haloperidol ( -15.4 ) than placebo ( -10.7 ; both P < 0.05 ) ; using mixed model for repeated measures ( MMRM ) , changes at day 42 were significantly greater with asenapine at 5 and 10 mg BID ( -21.3 and -19.4 , respectively ) and haloperidol ( -20.0 ) than placebo ( -14.6 ; all P < 0.05 ) .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Input:
Sentence: The hazard decreased 0.3-fold ( 0.7-1.7 , P=0.385 ) with glimepiride , 0.4-fold ( 0.7-1.3 , P=0.192 ) with gliclazide , and 0.4-fold ( 0.7-1.1 , P=0.09 ) with either .

## Item bc5cdr:test:3078
Example input:
Sentence: In Mg ( 2+ ) -free bathing medium containing bicuculline , conditions designed to increase excitability in the slices , electrical stimulation of the hilus resulted in a single population spike in granule cells from control mice and pilocarpine-treated mice that did not experience SE .

Example answer:
{"entities": [{"text": "Mg", "type": "Chemical"}, {"text": "bicuculline", "type": "Chemical"}, {"text": "pilocarpine-treated", "type": "Chemical"}, {"text": "SE", "type": "Disease"}]}

Example input:
Sentence: should immediately precede induction of anaesthesia , in children , if the repeated administration of suxamethonium is anticipated .

Example answer:
{"entities": [{"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: We conclude that careful screening for medications and underlying conditions predisposing to hypocalcemia is recommended to help prevent severe reactions due to citrate toxicity .

Example answer:
{"entities": [{"text": "hypocalcemia", "type": "Disease"}, {"text": "citrate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Apart from the reduction in the patient 's level of consciousness , there were no signs of motor neurone damage or of any of the other known predisposing conditions for hyperkalaemia following the administration of suxamethonium .

Example answer:
{"entities": [{"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: Topiramate prevented all the alterations observed , showing novel neuroprotective properties .

Example answer:
{"entities": [{"text": "Topiramate", "type": "Chemical"}]}

Example input:
Sentence: This literature review suggests that general practitioners should prescribe scabicides with increased caution for certain at-risk groups , and give adequate warnings regarding potential toxicity .

Example answer:
{"entities": [{"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Suxamethonium causes prolonged apnea in patients in whom pseudocholinesterase enzyme gets deactivated by organophosphorus ( OP ) poisons .

Example answer:
{"entities": [{"text": "Suxamethonium", "type": "Chemical"}, {"text": "apnea", "type": "Disease"}, {"text": "organophosphorus ( OP ) poisons", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: glycopyrrolate and atropine in the prevention of bradycardia and arrhythmias following repeated doses of suxamethonium in children .

Example answer:
{"entities": [{"text": "glycopyrrolate", "type": "Chemical"}, {"text": "atropine", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}, {"text": "arrhythmias", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Input:
Sentence: However , they also suggest that succimer treatment should be strongly discouraged for children who do not have elevated tissue levels of Pb or other heavy metals .

## Item bc5cdr:test:3418
Example input:
Sentence: Impotence was more common among male patients than controls and was found to be associated with co-morbidity and the taking of methotrexate .

Example answer:
{"entities": [{"text": "Impotence", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Methamphetamine is a very addictive , powerful stimulant that increases wakefulness and physical activity and can produce other effects such as cardiac dysrhythmias , hypertension , hallucinations , and violent behavior .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "cardiac dysrhythmias", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "hallucinations", "type": "Disease"}, {"text": "violent behavior", "type": "Disease"}]}

Example input:
Sentence: The possibility that habitual use of acetaminophen alone increases the risk of ESRD has not been clearly demonstrated , but can not be dismissed .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: In this study , the hypothesis was tested that there is a sexual dimorphism in HS-induced upregulation of intrarenal angiotensinogen mediated by testosterone that also causes increases in BP and renal injury .

Example answer:
{"entities": [{"text": "testosterone", "type": "Chemical"}, {"text": "renal injury", "type": "Disease"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "METH", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: The morphine-induced hyperactivity was potentiated by scopolamine and attenuated by physostigmine .

Example answer:
{"entities": [{"text": "morphine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "scopolamine", "type": "Chemical"}, {"text": "physostigmine", "type": "Chemical"}]}

Example input:
Sentence: Progressive improvement occurred in 7 cases after commencement of prednisolone and methotrexate , and in one case spontaneously .

Example answer:
{"entities": [{"text": "prednisolone", "type": "Chemical"}, {"text": "methotrexate", "type": "Chemical"}]}

Example input:
Sentence: Choreoathetoid movements associated with rapid adjustment to methadone .

Example answer:
{"entities": [{"text": "Choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Input:
Sentence: Methadone may aggravate this problem .

## Item bc5cdr:test:3315
Example input:
Sentence: A patient is reported who developed progressive cardiomyopathy two and one-half years after receiving 580 mg/m2 which apparently represents late , late cardiotoxicity .

Example answer:
{"entities": [{"text": "cardiomyopathy", "type": "Disease"}, {"text": "cardiotoxicity", "type": "Disease"}]}

Example input:
Sentence: Pneumonitis , bilateral pleural effusions , echocardiographic evidence of cardiac tamponade , and positive autoantibodies developed in a 43-year-old man , who was receiving long-term sulfasalazine therapy for chronic ulcerative colitis .

Example answer:
{"entities": [{"text": "Pneumonitis", "type": "Disease"}, {"text": "pleural effusions", "type": "Disease"}, {"text": "cardiac tamponade", "type": "Disease"}, {"text": "sulfasalazine", "type": "Chemical"}, {"text": "ulcerative colitis", "type": "Disease"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Ophthalmologists at 15 institutions responded , reporting a total of 3,774 indocyanine green angiograms performed on 2,820 patients between June 1984 and September 1992 .

Example answer:
{"entities": [{"text": "indocyanine green", "type": "Chemical"}]}

Example input:
Sentence: Since the introduction of angiotensin converting enzyme ( ACE ) inhibitors into the adjunctive treatment of patients with congestive heart failure , cases of severe hypotension , especially on the first day of treatment , have occasionally been reported .

Example answer:
{"entities": [{"text": "angiotensin converting enzyme ( ACE ) inhibitors", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: In patients requiring the concurrent use of statins and CYP3A4 inhibitors , pravastatin , fluvastatin , and rosuvastatin carry the lowest risk of drug interactions ; atorvastatin carries moderate risk , whereas simvastatin and lovastatin have the highest risk and should be avoided in patients taking concomitant CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "statins", "type": "Chemical"}, {"text": "pravastatin", "type": "Chemical"}, {"text": "fluvastatin", "type": "Chemical"}, {"text": "rosuvastatin", "type": "Chemical"}, {"text": "atorvastatin", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "lovastatin", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Nine of 30 patients receiving lidocaine experienced TNSs , 1 of 30 patients receiving prilocaine ( P = 0.03 ) had them , and none of 30 patients receiving bupivacaine had TNSs .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "TNSs", "type": "Disease"}, {"text": "prilocaine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: During treatment , adverse cardiac effects were observed in 14 patients ( 18 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Design and analysis of the HYPREN-trial : safety of enalapril and prazosin in the initial treatment phase of patients with congestive heart failure .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "prazosin", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: Recently , synthetic fibrinolysis inhibitors such as tranexamic acid ( tAMCA ) have been considered as substitutes for aprotinin .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "Chemical"}, {"text": "tAMCA", "type": "Chemical"}]}

Input:
Sentence: The risks of aprotinin and tranexamic acid in cardiac surgery : a one-year follow-up of 1188 consecutive patients .

## Item bc5cdr:test:2302
Example input:
Sentence: Effects of 5-HT1B receptor ligands microinjected into the accumbal shell or core on the cocaine-induced locomotor hyperactivity in rats .

Example answer:
{"entities": [{"text": "cocaine-induced", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to examine the effect of 5-HT1B receptor ligands microinjected into the subregions of the nucleus accumbens ( the shell and the core ) on the locomotor hyperactivity induced by cocaine in rats .

Example answer:
{"entities": [{"text": "locomotor hyperactivity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}, {"text": "yohimbine", "type": "Chemical"}]}

Example input:
Sentence: To further validate the hypothesis that the anti-cocaine effects of the novel ligands involved antagonism of sigma receptors , an antisense oligodeoxynucleotide against sigma1 receptors was also shown to significantly attenuate the convulsive and locomotor stimulatory effects of cocaine .

Example answer:
{"entities": [{"text": "oligodeoxynucleotide", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: At doses where alone , they produced no significant effects on locomotion , BD1018 , BD1063 and LR132 significantly attenuated the locomotor stimulatory effects of cocaine .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: Conformationally restricted analogs of BD1008 and an antisense oligodeoxynucleotide targeting sigma1 receptors produce anti-cocaine effects in mice .

Example answer:
{"entities": [{"text": "BD1008", "type": "Chemical"}, {"text": "oligodeoxynucleotide", "type": "Chemical"}]}

Example input:
Sentence: GR 55562 ( 0.1-10 microg/side ) , administered intra-accumbens shell prior to cocaine , dose-dependently attenuated the psychostimulant-induced locomotor hyperactivity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: In contrast to the protection provided by the putative antagonists , the well-characterized sigma receptor agonist di-o-tolylguanidine ( DTG ) and the novel sigma receptor agonist BD1031 ( 3R-1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -1,4-diazabicyclo [ 4.3.0 ] nonane ) each worsened the behavioral toxicity of cocaine .

Example answer:
{"entities": [{"text": "di-o-tolylguanidine", "type": "Chemical"}, {"text": "DTG", "type": "Chemical"}, {"text": "BD1031", "type": "Chemical"}, {"text": "3R-1- [ 2- ( 3,4-dichlorophenyl ) ethyl ] -1,4-diazabicyclo [ 4.3.0 ] nonane", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: When injected into the accumbens shell ( but not the core ) before cocaine , CP 93129 ( 0.1-10 microg/side ) enhanced the locomotor response to cocaine ; the maximum effect being observed after 10 microg/side of the agonist .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Input:
Sentence: Moreover , all adenosine receptor agonists : 2-p- ( 2-carboxyethyl ) phenethylamino-5'-N-ethylcarboxamidoadenosine ( CGS 21680 ) , A2A receptor agonist , N6-cyclopentyladenosine ( CPA ) , A1 receptor agonist , and 5'-N-ethylcarboxamidoadenosine ( NECA ) , A2/A1 receptor agonist significantly and dose-dependently decreased cocaine-induced locomotor activity .

## Item bc5cdr:test:3203
Example input:
Sentence: We report a case of severe hypertension with an occluded renal artery to a solitary kidney , who developed sudden deterioration of renal function following treatment with captopril .

Example answer:
{"entities": [{"text": "hypertension", "type": "Disease"}, {"text": "sudden deterioration of renal function", "type": "Disease"}, {"text": "captopril", "type": "Chemical"}]}

Example input:
Sentence: The typical fluoxetine-induced symptoms of restlessness , constant pacing , purposeless movements of the feet and legs , and marked anxiety were indistinguishable from those of neuroleptic-induced akathisia .

Example answer:
{"entities": [{"text": "fluoxetine-induced", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: We report the increased amount of motor disability in four patients with idiopathic Parkinson 's disease after exposure to the antidepressant fluoxetine .

Example answer:
{"entities": [{"text": "motor disability", "type": "Disease"}, {"text": "idiopathic Parkinson 's disease", "type": "Disease"}, {"text": "antidepressant", "type": "Chemical"}, {"text": "fluoxetine", "type": "Chemical"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: RESULT ( S ) : A 36-year-old Chinese woman developed central retinal vein occlusion after eight courses of CC .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: In the present paper the authors describe 2 female patients who developed incontinence secondary to the selective serotonin reuptake inhibitors paroxetine and sertraline , as well as a third who developed this side effect on venlafaxine .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "sertraline", "type": "Chemical"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: OBJECTIVE : To report a case of central retinal vein occlusion associated with clomiphene citrate ( CC ) .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "clomiphene citrate", "type": "Chemical"}, {"text": "CC", "type": "Chemical"}]}

Example input:
Sentence: Central retinal vein occlusion associated with clomiphene-induced ovulation .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "clomiphene-induced", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION ( S ) : This is the first reported case of central retinal vein occlusion after treatment with CC .

Example answer:
{"entities": [{"text": "retinal vein occlusion", "type": "Disease"}, {"text": "CC", "type": "Chemical"}]}

Input:
Sentence: A case of branch retinal vein occlusion associated with fluoxetine-induced secondary hypertension is described .

## Item bc5cdr:test:3316
Example input:
Sentence: We prospectively evaluated the adverse reactions of apraclonidine in 20 normal volunteers by instilling a single drop of 1 % apraclonidine in their right eyes .

Example answer:
{"entities": [{"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: Design and analysis of the HYPREN-trial : safety of enalapril and prazosin in the initial treatment phase of patients with congestive heart failure .

Example answer:
{"entities": [{"text": "enalapril", "type": "Chemical"}, {"text": "prazosin", "type": "Chemical"}, {"text": "congestive heart failure", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Omission of fentanyl did not reduce the overall incidence of postoperative nausea and vomiting , but did reduce the incidence of vomiting and/or moderate to severe nausea prior to discharge from 20 % and 17 % with fentanyl and fentanyl-dexamethasone , respectively , to 5 % ( P = 0.013 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "postoperative nausea and vomiting", "type": "Disease"}, {"text": "vomiting", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "fentanyl-dexamethasone", "type": "Chemical"}]}

Example input:
Sentence: To assess the safety of the ACE inhibitor enalapril a multicenter , randomized , prazosin-controlled trial was designed that compared the incidence and severity of symptomatic hypotension on the first day of treatment .

Example answer:
{"entities": [{"text": "ACE inhibitor", "type": "Chemical"}, {"text": "enalapril", "type": "Chemical"}, {"text": "prazosin-controlled", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: The ocular hypotensive effects were statistically significant for apraclonidine-treated eyes throughout the study and also statistically significant for contralateral eyes from three hours after topical administration of 1 % apraclonidine .

Example answer:
{"entities": [{"text": "ocular hypotensive", "type": "Disease"}, {"text": "apraclonidine-treated", "type": "Chemical"}, {"text": "apraclonidine", "type": "Chemical"}]}

Example input:
Sentence: Side effects of postoperative administration of methylprednisolone and gentamicin into the posterior sub-Tenon 's space .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}]}

Example input:
Sentence: PURPOSE : To assess the incidence of postoperative emetic side effects after the administration of methylprednisolone and gentamicin into the posterior sub-Tenon 's space at the end of routine cataract surgery .

Example answer:
{"entities": [{"text": "methylprednisolone", "type": "Chemical"}, {"text": "gentamicin", "type": "Chemical"}, {"text": "cataract", "type": "Disease"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: In contrast , FS containing aprotinin did not evoke any paroxysmal activity .

Example answer:
{"entities": []}

Example input:
Sentence: Recently , synthetic fibrinolysis inhibitors such as tranexamic acid ( tAMCA ) have been considered as substitutes for aprotinin .

Example answer:
{"entities": [{"text": "tranexamic acid", "type": "Chemical"}, {"text": "tAMCA", "type": "Chemical"}]}

Input:
Sentence: BACKGROUND : Our aim was to investigate postoperative complications and mortality after administration of aprotinin compared to tranexamic acid in an unselected , consecutive cohort .

## Item bc5cdr:test:3038
Example input:
Sentence: RESULTS : Minutes after oral administration , the patient developed nausea , sweating and hypotension , and finally collapsed .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Ten cm H2O CPAP before nitroprusside infusion produced a further decrease in arterial blood pressure and significantly increased heart rate and decreased cardiac output and QS/QT .

Example answer:
{"entities": [{"text": "H2O", "type": "Chemical"}, {"text": "nitroprusside", "type": "Chemical"}, {"text": "decrease in arterial blood pressure", "type": "Disease"}, {"text": "decreased cardiac output", "type": "Disease"}]}

Example input:
Sentence: The role of the renin -- angiotensin system in the maintenance of blood pressure during halothane anesthesia and sodium nitroprusside ( SNP ) -induced hypotension was evaluated .

Example answer:
{"entities": [{"text": "angiotensin", "type": "Chemical"}, {"text": "halothane", "type": "Chemical"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: After starting PGE1 or TMP , MAP and rate pressure product ( RPP ) decreased significantly compared with preinfusion values ( P < 0.01 ) , and the degree of hypotension due to PGE1 remained constant until 60 min after its discontinuation .

Example answer:
{"entities": [{"text": "PGE1", "type": "Chemical"}, {"text": "TMP", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: In each group , SNP infusion resulted in an initial decrease in blood pressure from 86 torr and 83 torr , respectively , to 48 torr .

Example answer:
{"entities": [{"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Transient hypotension ( SAP < 90mmHg ) occurred in 1 patient ( 0.7 % ) .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Under such conditions , angiotensin II receptor blockade by losartan probably induced a critical fall in glomerular filtration pressure .

Example answer:
{"entities": [{"text": "angiotensin II", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: In group C , AKBR showed a significant decrease at 120 min ( -40 % ) and at 180 min ( -49 % ) after the start of hypotension and at 60 min ( -32 % ) after recovery of normotension , and SGOT , SGPT , LDH and total bilirubin showed significant increases after operation .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "bilirubin", "type": "Chemical"}]}

Input:
Sentence: Several minutes after the GTN the patient experienced a sudden drop in blood pressure and heart rate , this was rectified by atropine sulphate and a fluid challenge .

## Item bc5cdr:test:3075
Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: Curcumin ameliorates cognitive dysfunction and oxidative damage in phenobarbitone and carbamazepine administered rats .

Example answer:
{"entities": [{"text": "Curcumin", "type": "Chemical"}, {"text": "cognitive dysfunction", "type": "Disease"}, {"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}]}

Example input:
Sentence: In rats treated with Dex alone , SBP was increased from 109 +/- 2 to 133 +/- 2 mmHg on Days 4 and Day 14 , respectively ( P < 0.001 ) .

Example answer:
{"entities": [{"text": "Dex", "type": "Chemical"}]}

Example input:
Sentence: Brain and spinal cord NTE activities were measured in Long-Evans male rats 1 hr post-exposure to various dosages of Mipafox ( ip , 1-15 mg/kg ) .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: Furthermore , our data suggest that TR ( - ) rats are an interesting tool to study consequences of overexpression of Pgp in the BBB on access of drugs in the brain , without the need of inducing seizures or other Pgp-enhancing events for this purpose .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether maltolyl p-coumarate could improve cognitive decline in scopolamine-injected rats and in amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive decline", "type": "Disease"}, {"text": "scopolamine-injected", "type": "Chemical"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Dissociated learning of rats in the normal state and the state of amnesia produced by pentobarbital ( 15 mg/kg , ip ) was carried out .

Example answer:
{"entities": [{"text": "amnesia", "type": "Disease"}, {"text": "pentobarbital", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Clomipramine exposure in immature rats produced significant behavioral and biochemical changes that include enhanced anxiety ( elevated plus maze and marble burying ) , behavioral inflexibility ( perseveration in the spontaneous alternation task and impaired reversal learning ) , working memory impairment ( e.g. , win-shift paradigm ) , hoarding , and corticostriatal dysfunction .

Example answer:
{"entities": [{"text": "Clomipramine", "type": "Chemical"}, {"text": "anxiety", "type": "Disease"}, {"text": "behavioral inflexibility", "type": "Disease"}, {"text": "memory impairment", "type": "Disease"}, {"text": "hoarding", "type": "Disease"}, {"text": "corticostriatal dysfunction", "type": "Disease"}]}

Input:
Sentence: In contrast , succimer treatment of rats not previously exposed to Pb produced lasting and pervasive cognitive and affective dysfunction comparable in magnitude to that produced by the higher Pb exposure regimen .

## Item bc5cdr:test:3560
Example input:
Sentence: PG-9 was also able to increase the amount of NGF secreted in vitro by astrocytes in a dose-dependent manner .

Example answer:
{"entities": []}

Example input:
Sentence: Our results demonstrate that both cisplatin and paclitaxel cause early mitochondrial impairment with loss of membrane potential and induction of autophagic vacuoles in neurons .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "mitochondrial impairment", "type": "Disease"}]}

Example input:
Sentence: Alpha-lipoic acid prevents mitochondrial damage and neurotoxicity in experimental chemotherapy neuropathy .

Example answer:
{"entities": [{"text": "Alpha-lipoic acid", "type": "Chemical"}, {"text": "mitochondrial damage", "type": "Disease"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}]}

Example input:
Sentence: The effects of PG-9 ( 3alpha-tropyl 2- ( p-bromophenyl ) propionate ) , the acetylcholine releaser , on memory processes and nerve growth factor ( NGF ) synthesis were evaluated .

Example answer:
{"entities": [{"text": "PG-9", "type": "Chemical"}, {"text": "3alpha-tropyl 2- ( p-bromophenyl ) propionate", "type": "Chemical"}, {"text": "acetylcholine", "type": "Chemical"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: Maltolyl p-coumarate was found to attenuate cognitive deficits in both rat models using passive avoidance test and to reduce apoptotic cell death observed in the hippocampus of the amyloid beta peptide ( 1-42 ) -infused rats .

Example answer:
{"entities": [{"text": "Maltolyl p-coumarate", "type": "Chemical"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "amyloid beta peptide ( 1-42 )", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: In conclusion , the NF-kappaB inhibitor and antioxidant PDTC protected the piriform cortex , whereas it did not affect hilar neuronal loss .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "neuronal loss", "type": "Disease"}]}

Example input:
Sentence: Taking these in vitro and in vivo results together , our study suggests that maltolyl p-coumarate is a potentially effective candidate against Alzheimer 's disease that is characterized by wide spread neuronal death and progressive decline of cognitive function .

Example answer:
{"entities": [{"text": "maltolyl p-coumarate", "type": "Chemical"}, {"text": "Alzheimer 's disease", "type": "Disease"}, {"text": "neuronal death", "type": "Disease"}, {"text": "decline of cognitive function", "type": "Disease"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Input:
Sentence: In particular this anti mitotic drug could reduce cell proliferation in the neurogenic regions of the adult brain .

## Item bc5cdr:test:3407
Example input:
Sentence: Injection of Captopril ( 1 mg/kg ) , an inhibitor of angiotensin converting enzyme ( ACE ) , reduced both pulmonary and renal insufficiency in this rat model .

Example answer:
{"entities": [{"text": "Captopril", "type": "Chemical"}, {"text": "angiotensin", "type": "Chemical"}]}

Example input:
Sentence: In vitro , gamma-HCH , pentylenetetrazol and picrotoxin were shown to inhibit 3H-TBOB binding in mouse whole brain , with IC50 values of 4.6 , 404 and 9.4 microM , respectively .

Example answer:
{"entities": [{"text": "gamma-HCH", "type": "Chemical"}, {"text": "pentylenetetrazol", "type": "Chemical"}, {"text": "picrotoxin", "type": "Chemical"}, {"text": "3H-TBOB", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : Correlation of plasma argatroban concentration versus the patient 's coagulation variables and clinical course suggest that prolonged elevated levels of plasma argatroban may have contributed to the patient 's extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: Antituberculosis therapy ( ATT ) -associated acute liver failure ( ATT-ALF ) is the commonest drug-induced ALF in South Asia .

Example answer:
{"entities": [{"text": "Antituberculosis", "type": "Chemical"}, {"text": "acute liver failure", "type": "Disease"}, {"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: STUDY DESIGN AND METHODS : Plasma samples from before and after CPB were analyzed postoperatively for argatroban concentration using a modified ecarin clotting time ( ECT ) assay .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}]}

Example input:
Sentence: Prolonged elevation of plasma argatroban in a cardiac transplant patient with a suspected history of heparin-induced thrombocytopenia with thrombosis .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "heparin-induced", "type": "Chemical"}, {"text": "thrombocytopenia", "type": "Disease"}, {"text": "thrombosis", "type": "Disease"}]}

Example input:
Sentence: This is the first report to measure plasma argatroban concentration in the context of CPB and extended coagulopathy .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "coagulopathy", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Unexpectedly high concentrations of argatroban were measured in these samples ( range , 0-32 microg/mL ) , and a prolonged plasma argatroban half life ( t ( 1/2 ) ) of 514 minutes was observed ( published elimination t ( 1/2 ) is 39-51 minutes [ < or = 181 minutes with hepatic impairment ] ) .

Example answer:
{"entities": [{"text": "argatroban", "type": "Chemical"}, {"text": "hepatic impairment", "type": "Disease"}]}

Example input:
Sentence: In the following report , a 65-year-old critically ill patient with a suspected history of HITT was administered argatroban for anticoagulation on bypass during heart transplantation .

Example answer:
{"entities": [{"text": "critically ill", "type": "Disease"}, {"text": "HITT", "type": "Disease"}, {"text": "argatroban", "type": "Chemical"}]}

Input:
Sentence: Argatroban 0.5-1.2 microg/kg/min typically supports therapeutic aPTTs .

## Item bc5cdr:test:3589
Example input:
Sentence: Proteinuria increased significantly from a median of 0.13 g/day ( range 0-5.7 ) preswitch to 0.23 g/day ( 0-9.88 ) at 24 months postswitch ( p = 0.0024 ) .

Example answer:
{"entities": []}

Example input:
Sentence: The restoration of continence was accompanied by a substantial rise in maximum urethral pressure , maximum urethral closure pressure , and functional urethral length .

Example answer:
{"entities": []}

Example input:
Sentence: The amount of daily urinary protein decreased from 15.6 to 2.8 g. Within 14 days of the oral bisphosphonate ( alendronate sodium ) administration , the amount of daily urinary protein increased rapidly up to 12.8 g with acute renal failure .

Example answer:
{"entities": [{"text": "bisphosphonate", "type": "Chemical"}, {"text": "alendronate sodium", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: She was treated with heparin , dipyridamole and hemodialysis ; and after more than three months , her urinary output rose above 500 ml ; and six months after the onset of anuria , dialysis treatment was stopped .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}]}

Example input:
Sentence: CONCLUSIONS : Urine volume can be reduced by giving lithium once daily and/or by lowering the total daily dose .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: This occurred in association with an increase in urinary protein content from 1.8 +/- 1 to 99.0 +/- 61 mg/day ( p < 0.001 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Here , 2 cases of urinary bladder retention leading to renal pelvocalyceal dilatation mimicking hydronephrosis as a result of continuous infusion of fentanyl are reported .

Example answer:
{"entities": [{"text": "urinary bladder retention", "type": "Disease"}, {"text": "hydronephrosis", "type": "Disease"}, {"text": "fentanyl", "type": "Chemical"}]}

Example input:
Sentence: Proteinuria increased from 0.445 ( 0 to 1.5 ) g/d before conversion to 3.2 g/dL ( 0.2 to 12 ) after conversion ( P = 0.001 ) .

Example answer:
{"entities": [{"text": "Proteinuria", "type": "Disease"}]}

Example input:
Sentence: Morphometric analysis revealed that the volume density of secretory granules increased , while the volume density of cytoplasmic microtubules decreased .

Example answer:
{"entities": []}

Example input:
Sentence: Patients without proteinuria had increased renal function ( median 42.5 vs. 64.1 , p = 0.25 ) , whereas patients who developed high-grade proteinuria showed decreased renal function at the end of follow-up ( median 39.6 vs. 29.2 , p = 0.125 ) .

Example answer:
{"entities": [{"text": "proteinuria", "type": "Disease"}]}

Input:
Sentence: Urine volume was increased , while urine osmolality and free water reabsorption were decreased .

## Item bc5cdr:test:3167
Example input:
Sentence: PURPOSE : The influence of an irreversible inhibitor of constitutive NO synthase ( L-NOArg ; 1.0 mg/kg ip ) , a relatively selective inhibitor of inducible NO synthase ( L-NIL ; 1.0 mg/kg ip ) and a relatively specific inhibitor of neuronal NO synthase ( 7-NI ; 0.1 mg/kg ip ) , on antihyperalgesic action of selective antagonists of B2 and B1 receptors : D-Arg- [ Hyp3 , Thi5 , D-Tic7 , Oic8 ] bradykinin ( HOE 140 ; 70 nmol/kg ip ) or des Arg10 HOE 140 ( 70 nmol/kg ip ) respectively , in model of diabetic ( streptozotocin-induced ) and toxic ( vincristine-induced ) neuropathy was investigated .

Example answer:
{"entities": [{"text": "NO", "type": "Chemical"}, {"text": "bradykinin", "type": "Chemical"}, {"text": "HOE 140", "type": "Chemical"}, {"text": "des Arg10 HOE 140", "type": "Chemical"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: To assess the molecular basis of disturbances in transmembraneous transport of Na+ , we studied the response of cardiac ( Na , K ) -ATPase to NO-deficient hypertension induced in rats by NO-synthase inhibition with 40 mg/kg/day N ( G ) -nitro-L-arginine methyl ester ( L-NAME ) for 4 four weeks .

Example answer:
{"entities": [{"text": "Na+", "type": "Chemical"}, {"text": "Na", "type": "Chemical"}, {"text": "K", "type": "Chemical"}, {"text": "NO-deficient", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}, {"text": "NO-synthase", "type": "Chemical"}, {"text": "N ( G ) -nitro-L-arginine methyl ester", "type": "Chemical"}, {"text": "L-NAME", "type": "Chemical"}]}

Example input:
Sentence: In vivo microdialysis demonstrated that an intraperitoneal administration of pilocarpine induced a pronounced increment of hippocampal glutamate and aspartate whereas no significant change was observed on the level of glycine and GABA .

Example answer:
{"entities": [{"text": "pilocarpine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "GABA", "type": "Chemical"}]}

Example input:
Sentence: In the present study , we investigated whether 50 mg/kg per day , p.o. , Ato could prevent endothelial NO synthase ( eNOS ) downregulation and the increase in O2- in Sprague-Dawley ( SD ) rats , thereby reducing blood pressure .

Example answer:
{"entities": [{"text": "Ato", "type": "Chemical"}, {"text": "NO", "type": "Chemical"}, {"text": "O2-", "type": "Chemical"}]}

Example input:
Sentence: Induction of intravascular coagulation and inhibition of fibrinolysis by injection of thrombin and tranexamic acid ( AMCA ) in the rat gives rise to pulmonary and renal insufficiency resembling that occurring after trauma or sepsis in man .

Example answer:
{"entities": [{"text": "intravascular coagulation", "type": "Disease"}, {"text": "tranexamic acid", "type": "Chemical"}, {"text": "AMCA", "type": "Chemical"}, {"text": "trauma", "type": "Disease"}, {"text": "sepsis", "type": "Disease"}]}

Example input:
Sentence: Brain and spinal cord NTE activities were measured in Long-Evans male rats 1 hr post-exposure to various dosages of Mipafox ( ip , 1-15 mg/kg ) .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}]}

Example input:
Sentence: These data indicate that a critical percentage of NTE inhibition in brain and spinal cord sampled shortly after Mipafox exposure can predict neuropathic damage in rats several weeks later .

Example answer:
{"entities": [{"text": "Mipafox", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Example input:
Sentence: The correlation between neuropathic damage and inhibition of neurotoxic esterase or neuropathy target enzyme ( NTE ) was examined in rats acutely exposed to Mipafox ( N , N'-diisopropylphosphorodiamidofluoridate ) , a neurotoxic organophosphate .

Example answer:
{"entities": [{"text": "neuropathic damage", "type": "Disease"}, {"text": "neurotoxic", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "Mipafox", "type": "Chemical"}, {"text": "N , N'-diisopropylphosphorodiamidofluoridate", "type": "Chemical"}, {"text": "organophosphate", "type": "Chemical"}]}

Example input:
Sentence: The correlation between neurotoxic esterase inhibition and mipafox-induced neuropathic damage in rats .

Example answer:
{"entities": [{"text": "neurotoxic", "type": "Disease"}, {"text": "mipafox-induced", "type": "Chemical"}, {"text": "neuropathic damage", "type": "Disease"}]}

Input:
Sentence: Myo-inositol-1-phosphate ( MIP ) synthase inhibition : in-vivo study in rats .

## Item bc5cdr:test:3358
Example input:
Sentence: OBJECTIVE : This study was designed to determine whether patients maintained on a regimen of lithium on a once-per-day schedule have lower urine volumes than do patients receiving multiple doses per day .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : In this preliminary report , divalproex sodium was a superior alternative to lithium in bipolar patients experiencing cognitive deficits , loss of creativity , and functional impairments .

Example answer:
{"entities": [{"text": "divalproex sodium", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}, {"text": "bipolar", "type": "Disease"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "loss of creativity", "type": "Disease"}, {"text": "functional impairments", "type": "Disease"}]}

Example input:
Sentence: Although much has been written about the management of the more common adverse effects of lithium , such as polyuria and tremor , more subtle lithium side effects such as cognitive deficits , loss of creativity , and functional impairments remain understudied .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "polyuria", "type": "Disease"}, {"text": "tremor", "type": "Disease"}, {"text": "cognitive deficits", "type": "Disease"}, {"text": "loss of creativity", "type": "Disease"}, {"text": "functional impairments", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : The frequency of mood switching associated with acute antidepressant therapy may be reduced by lithium treatment .

Example answer:
{"entities": [{"text": "antidepressant", "type": "Chemical"}, {"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Lithium remains a first-line treatment for the acute and maintenance treatment of bipolar disorder .

Example answer:
{"entities": [{"text": "Lithium", "type": "Chemical"}, {"text": "bipolar disorder", "type": "Disease"}]}

Example input:
Sentence: When comparing all lithium treated versus non-lithium-treated groups , lithium caused a reduction in glomerular filtration rate ( GFR ) without significant changes in effective renal plasma flow ( as determined by a marker secreted into the proximal tubules ) or lithium clearance .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: Lithium-associated cognitive and functional deficits reduced by a switch to divalproex sodium : a case series .

Example answer:
{"entities": [{"text": "Lithium-associated", "type": "Chemical"}, {"text": "cognitive and functional deficits", "type": "Disease"}, {"text": "divalproex sodium", "type": "Chemical"}]}

Example input:
Sentence: After 3 days of combined treatment , a marked elevation in plasma and tissue lithium levels accompanied a reduction in water intake .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : We report seven cases where substitution of lithium , either fully or partially , with divalproex sodium was extremely helpful in reducing the cognitive , motivational , or creative deficits attributed to lithium in our bipolar patients .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}, {"text": "divalproex sodium", "type": "Chemical"}, {"text": "cognitive , motivational , or creative deficits", "type": "Disease"}, {"text": "bipolar", "type": "Disease"}]}

Example input:
Sentence: In contrast , mood switches were less frequent in patients receiving lithium ( 15 % , 4/26 ) than in patients not treated with lithium ( 44 % , 8/18 ; p = .04 ) .

Example answer:
{"entities": [{"text": "lithium", "type": "Chemical"}]}

Input:
Sentence: PRACTICAL IMPLICATIONS : As much as 15 % of lithium-treated patients become hypercalcemic .

## Item bc5cdr:test:3426
Example input:
Sentence: Medical records were studied retrospectively to evaluate whether warfarin and warfarin-drug interactions could have caused the cerebral haemorrhage .

Example answer:
{"entities": [{"text": "warfarin", "type": "Chemical"}, {"text": "warfarin-drug", "type": "Chemical"}, {"text": "cerebral haemorrhage", "type": "Disease"}]}

Example input:
Sentence: We consider drug-induced cerebral vasculitis as the most likely cause of recurrent ischaemic strokes in the absence of any pathological findings during the diagnostic work-up .

Example answer:
{"entities": [{"text": "cerebral vasculitis", "type": "Disease"}, {"text": "ischaemic strokes", "type": "Disease"}]}

Example input:
Sentence: Cerebral infarction occurred in 10 patients ( 22 % ) , intracerebral hemorrhage in 22 ( 49 % ) , and subarachnoid hemorrhage in 13 ( 29 % ) .

Example answer:
{"entities": [{"text": "Cerebral infarction", "type": "Disease"}, {"text": "intracerebral hemorrhage", "type": "Disease"}, {"text": "subarachnoid hemorrhage", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Of the 14 patients , 5 ( 35.7 % ) had white matter abnormalities , 1 ( 7.1 % ) had putaminal hemorrhage , and 8 ( 57.1 % ) had normal findings on initial MR images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}, {"text": "putaminal hemorrhage", "type": "Disease"}]}

Example input:
Sentence: Intracranial aneurysms or arteriovenous malformations were present in 17 of 32 patients studied angiographically or at autopsy ; cerebral vasculitis was present in two patients .

Example answer:
{"entities": [{"text": "Intracranial aneurysms", "type": "Disease"}, {"text": "arteriovenous malformations", "type": "Disease"}, {"text": "cerebral vasculitis", "type": "Disease"}]}

Example input:
Sentence: Intracerebral hemorrhage is associated with more inflammation than ischemic stroke .

Example answer:
{"entities": [{"text": "Intracerebral hemorrhage", "type": "Disease"}, {"text": "inflammation", "type": "Disease"}, {"text": "ischemic stroke", "type": "Disease"}]}

Example input:
Sentence: Cranial magnetic resonance imaging and extensive laboratory studies failed to reveal structural lesions of the brain and metabolic abnormalities .

Example answer:
{"entities": [{"text": "structural lesions of the brain", "type": "Disease"}, {"text": "metabolic abnormalities", "type": "Disease"}]}

Example input:
Sentence: Inflammatory cells are postulated to mediate some of the brain damage following ischemic stroke .

Example answer:
{"entities": [{"text": "brain damage", "type": "Disease"}, {"text": "ischemic stroke", "type": "Disease"}]}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Input:
Sentence: After MRI , we found cerebral ischemic infarction .

## Item bc5cdr:test:3114
Example input:
Sentence: Two patients developed acute tubular necrosis , characterized clinically by acute oliguric renal failure , while they were receiving a combination of cephalothin sodium and gentamicin sulfate therapy .

Example answer:
{"entities": [{"text": "acute tubular necrosis", "type": "Disease"}, {"text": "cephalothin sodium", "type": "Chemical"}, {"text": "gentamicin sulfate", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSION : Pericarditis may be the initial manifestation of drug-induced vasculitis attributable to propylthio- uracil therapy .

Example answer:
{"entities": [{"text": "Pericarditis", "type": "Disease"}, {"text": "vasculitis", "type": "Disease"}, {"text": "propylthio- uracil", "type": "Chemical"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: We examined the abundance of ENaC subunit mRNAs and proteins in puromycin aminonucleoside ( PAN ) -induced nephrotic syndrome .

Example answer:
{"entities": [{"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephrotic syndrome", "type": "Disease"}]}

Example input:
Sentence: Propylthiouracil-induced perinuclear-staining antineutrophil cytoplasmic autoantibody-positive vasculitis in conjunction with pericarditis .

Example answer:
{"entities": [{"text": "Propylthiouracil-induced", "type": "Chemical"}, {"text": "vasculitis", "type": "Disease"}, {"text": "pericarditis", "type": "Disease"}]}

Example input:
Sentence: Puromycin aminonucleoside nephrosis was induced by single intraperitoneal injection of puromycin aminonucleoside ( PAN , 20 mg/100g BW ) .

Example answer:
{"entities": [{"text": "Puromycin aminonucleoside", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}]}

Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: The results suggest a possible involvement of the renin-angiotensin system in the development of puromycin aminonucleoside-induced nephrosis .

Example answer:
{"entities": [{"text": "puromycin", "type": "Chemical"}, {"text": "nephrosis", "type": "Disease"}]}

Example input:
Sentence: Reactive oxygen species have been implicated in the pathogenesis of acute puromycin aminonucleoside ( PAN ) -induced nephropathy , with antioxidants significantly reducing the proteinuria .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "PAN", "type": "Chemical"}, {"text": "nephropathy", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}]}

Example input:
Sentence: The appearance of nephrotic syndromes such as proteinuria , hypoalbuminemia , hypercholesterolemia and increase in blood nitrogen urea , induced in rats by injection of puromycin aminonucleoside was markedly inhibited by oral administration of Dup 753 ( losartan ) , a novel angiotensin II receptor antagonist , at a dose of 1 or 2 mg/kg per day .

Example answer:
{"entities": [{"text": "nephrotic syndromes", "type": "Disease"}, {"text": "proteinuria", "type": "Disease"}, {"text": "hypoalbuminemia", "type": "Disease"}, {"text": "hypercholesterolemia", "type": "Disease"}, {"text": "blood nitrogen urea", "type": "Chemical"}, {"text": "puromycin aminonucleoside", "type": "Chemical"}, {"text": "Dup 753", "type": "Chemical"}, {"text": "losartan", "type": "Chemical"}, {"text": "angiotensin II", "type": "Chemical"}]}

Input:
Sentence: Piperacillin-induced encephalopathy should be considered in any uremic patients with unexplained neurological manifestations .

## Item bc5cdr:test:3464
Example input:
Sentence: Her vocal change and weakness began to improve spontaneously about 3 weeks after transfer .

Example answer:
{"entities": []}

Example input:
Sentence: An elderly patient treated with low dose Desipramine developed a delirium while her plasma level was in the `` subtherapeutic '' range .

Example answer:
{"entities": [{"text": "Desipramine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: All of the symptoms were completely resolved over the next 8 hours .

Example answer:
{"entities": []}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Delirium was inconsistently recognized clinically in milder cases and was associated with increased length-of-stay and higher costs , and inferior clinical outcome .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Example input:
Sentence: She subsequently died some 5 weeks after the commencement of her drug therapy.Post-mortem examination showed evidence of massive hepatocellular necrosis , acute hypersensitivity myocarditis , focal acute tubulo-interstitial nephritis and extensive bone marrow necrosis , with no evidence of malignancy .

Example answer:
{"entities": [{"text": "massive hepatocellular necrosis", "type": "Disease"}, {"text": "myocarditis", "type": "Disease"}, {"text": "nephritis", "type": "Disease"}, {"text": "bone marrow necrosis", "type": "Disease"}, {"text": "malignancy", "type": "Disease"}]}

Example input:
Sentence: Drowsiness was common on clonidine , but generally resolved by 6 to 8 weeks .

Example answer:
{"entities": [{"text": "Drowsiness", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}]}

Example input:
Sentence: She was treated with heparin , dipyridamole and hemodialysis ; and after more than three months , her urinary output rose above 500 ml ; and six months after the onset of anuria , dialysis treatment was stopped .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "dipyridamole", "type": "Chemical"}, {"text": "anuria", "type": "Disease"}]}

Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Delirium was diagnosed in 14 ( 10.1 % incidence , or 1.48 cases/person-years of exposure ) ; 71.4 % of cases were moderate or severe .

Example answer:
{"entities": [{"text": "Delirium", "type": "Disease"}]}

Input:
Sentence: Her delirium resolved 3 days later .

## Item bc5cdr:test:3365
Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: When respiratory failure was produced by hypoventilation ( pH 7.05 to 7.25 ; PC02 70 to 100 mm Hg : P02 20 to 40 mm Hg ) , infusion of aminophylline resulted in an even greater decrease in ventricular fibrillation threshold to 60 percent of the control level .

Example answer:
{"entities": [{"text": "respiratory failure", "type": "Disease"}, {"text": "hypoventilation", "type": "Disease"}, {"text": "aminophylline", "type": "Chemical"}, {"text": "ventricular fibrillation", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Orthostatic hypotension was ameliorated 4 days after withdrawal of selegiline and totally abolished 7 days after discontinuation of the drug .

Example answer:
{"entities": [{"text": "Orthostatic hypotension", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}]}

Example input:
Sentence: More patients were ( completely , very or somewhat ) satisfied 2 h after treatment with rizatriptan ( 69.8 % ) than at 2 h after treatment with ergotamine/caffeine ( 38.6 % , p < or = 0.001 ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: Forty-nine percent of patients were pain free 2 h after rizatriptan , compared with 24.3 % treated with ergotamine/caffeine ( p < or = 0.001 ) , rizatriptan being superior within 1 h of treatment .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}]}

Example input:
Sentence: The patients were randomly allocated to one of three groups ; those in group A ( n = 10 ) were subjected to controlled hypotension alone , those in group B ( n = 10 ) to haemodilution alone and those in group C ( n = 10 ) to both controlled hypotension and haemodilution .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "haemodilution", "type": "Disease"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension to an average MAP of 50-55 mm Hg was induced by increasing the dose of isoflurane , and maintained at an inspired concentration of 2.2 +/- 0.2 % .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "Hg", "type": "Chemical"}, {"text": "isoflurane", "type": "Chemical"}]}

Input:
Sentence: RESULTS : Controlled hypotension was achieved within a shorter period using laryngeal mask using lower rates of remifentanil infusion and lower total dose of remifentanil .
