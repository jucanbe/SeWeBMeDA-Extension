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

## Item bc5cdr:test:2479
Example input:
Sentence: Three cases were related to cyclosporine , and 1 case was secondary to both cyclosporine and tacrolimus .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: However , literature regarding the incidence of the recurrence of TMA in patients exposed sequentially to cyclosporine and tacrolimus is limited .

Example answer:
{"entities": [{"text": "TMA", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: Diffusion-weighted imaging may be useful in predicting the outcomes of the lesions of tacrolimus-induced neurotoxicity .

Example answer:
{"entities": [{"text": "tacrolimus-induced", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: Other causes include drug-related ( cyclosporine , tacrolimus ) toxicity , procoagulant status , and antibody-mediated rejection .

Example answer:
{"entities": [{"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: Brain MR studies , including DW imaging , were prospectively performed in 14 organ transplant patients receiving tacrolimus who developed neurologic complications .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "neurologic complications", "type": "Disease"}]}

Example input:
Sentence: Although tacrolimus was suspected to be the cause of late post-transplant renal acidosis and was replaced by sirolimus , acidosis , and electrolyte imbalance got worse .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "acidosis", "type": "Disease"}, {"text": "sirolimus", "type": "Chemical"}]}

Example input:
Sentence: Two groups of patients receiving tacrolimus were compared over a period of 1 year , one group comprising hypertensive patients who were receiving nifedipine , and the other comprising nonhypertensive patients not receiving nifedipine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: Introduction of tacrolimus as an alternative immunosuppressive agent resulted in the recurrence of TMA and the subsequent loss of the renal allograft .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: Recovery of tacrolimus-associated brachial neuritis after conversion to everolimus in a pediatric renal transplant recipient -- case report and review of the literature .

Example answer:
{"entities": [{"text": "tacrolimus-associated", "type": "Chemical"}, {"text": "brachial neuritis", "type": "Disease"}, {"text": "everolimus", "type": "Chemical"}]}

Input:
Sentence: We report on rosaceiform dermatitis as a complication of treatment with tacrolimus ointment .

## Item bc5cdr:test:2351
Example input:
Sentence: The frequency of sound-induced seizures after 12.5 or 25 mg/kg caffeine was reduced from 50 to 5 % by acetaminophen .

Example answer:
{"entities": [{"text": "seizures", "type": "Disease"}, {"text": "caffeine", "type": "Chemical"}, {"text": "acetaminophen", "type": "Chemical"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Serial epilepsy caused by levodopa/carbidopa administration in two patients on hemodialysis .

Example answer:
{"entities": [{"text": "epilepsy", "type": "Disease"}, {"text": "levodopa/carbidopa", "type": "Chemical"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: Long-term intragastric application of the antiepileptic drug sodium valproate ( Vupral `` Polfa '' ) at the effective dose of 200 mg/kg b. w. once daily to rats for 1 , 3 , 6 , 9 and 12 months revealed neurological disorders indicating cerebellum damage ( `` valproate encephalopathy '' ) .

Example answer:
{"entities": [{"text": "sodium valproate", "type": "Chemical"}, {"text": "neurological disorders", "type": "Disease"}, {"text": "cerebellum damage", "type": "Disease"}, {"text": "valproate", "type": "Chemical"}, {"text": "encephalopathy", "type": "Disease"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: Although the transaminases gradually returned to baseline after withholding the beta lactam antibiotic , there was a gradual increase in serum bilirubin and a decrease in hemoglobin concentration caused by an autoimmune hemolytic anemia and erythroblastocytopenia .

Example answer:
{"entities": [{"text": "beta lactam", "type": "Chemical"}, {"text": "bilirubin", "type": "Chemical"}, {"text": "autoimmune hemolytic anemia", "type": "Disease"}, {"text": "erythroblastocytopenia", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: FINDINGS : A 28-year-old man suffering from idiopathic epilepsy with generalized seizures was treated with LEV ( 3000 mg ) added to valproate ( VPA ) ( 2000 mg ) .

Example answer:
{"entities": [{"text": "idiopathic epilepsy", "type": "Disease"}, {"text": "seizures", "type": "Disease"}, {"text": "LEV", "type": "Chemical"}, {"text": "valproate", "type": "Chemical"}, {"text": "VPA", "type": "Chemical"}]}

Input:
Sentence: Immediately after the administration of levobupivacaine 0.5 % with epinephrine 2.5 microgram/mL , the patients developed grand mal seizures , despite negative aspiration for blood and no clinical signs of intravenous epinephrine administration .

## Item bc5cdr:test:2718
Example input:
Sentence: Previous reports have suggested that pain associated with the injection of lidocaine is related to the acidic pH of the solution .

Example answer:
{"entities": [{"text": "pain", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: SE was induced 20 h following the second injection and terminated 3 h later .

Example answer:
{"entities": [{"text": "SE", "type": "Disease"}]}

Example input:
Sentence: injections of organ specific three drugs ( AAP : 500 mg/Kg for 24 h ; AMI : 50 mg/Kg/day for four days ; DOX : 20 mg/Kg for 48 h ) .

Example answer:
{"entities": [{"text": "AAP", "type": "Chemical"}, {"text": "AMI", "type": "Chemical"}, {"text": "DOX", "type": "Chemical"}]}

Example input:
Sentence: CONCLUSIONS : It was determined that injection duration had an effect on bruising and pain following the subcutaneous administration of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: AIM : This study was carried out to determine the effect of injection duration on bruising and pain following the administration of the subcutaneous injection of heparin .

Example answer:
{"entities": [{"text": "bruising", "type": "Disease"}, {"text": "pain", "type": "Disease"}, {"text": "heparin", "type": "Chemical"}]}

Example input:
Sentence: However , a bolus of epinephrine injected through an alternative catheter provoked a hypertensive crisis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}]}

Example input:
Sentence: He complained of pain and visual disturbance in the ipsilateral eye 30 h after the injection .

Example answer:
{"entities": []}

Example input:
Sentence: Pain intensity and pain period were statistically significantly lower for the 30-second injection than for the 10-second injection .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: After the injection , there was a reduction in radicular symptoms .

Example answer:
{"entities": []}

Example input:
Sentence: Before and 0.5 , 1 , 2 , 3 , and 6 h after injection the subjects were given attention and mnemonic tests .

Example answer:
{"entities": []}

Input:
Sentence: injections .

## Item bc5cdr:test:2720
Example input:
Sentence: In a placebo-controlled , single-blinded , crossover study , we assessed the effect of `` real '' repetitive transcranial magnetic stimulation ( rTMS ) versus `` sham '' rTMS ( placebo ) on peak dose dyskinesias in patients with Parkinson 's disease ( PD ) .

Example answer:
{"entities": [{"text": "dyskinesias", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: Ten patients with PD and prominent dyskinesias had rTMS ( 1,800 pulses ; 1 Hz rate ) delivered over the motor cortex for 4 consecutive days twice , once real stimuli and once sham stimulation were used ; evaluations were done at the baseline and 1 day after the end of each of the treatment series .

Example answer:
{"entities": [{"text": "PD", "type": "Disease"}, {"text": "dyskinesias", "type": "Disease"}]}

Example input:
Sentence: Motor behavior , passive avoidance , and skilled forelimb function were tested repeatedly for six weeks .

Example answer:
{"entities": []}

Example input:
Sentence: NRA0160 and clozapine antagonized locomotor hyperactivity induced by methamphetamine ( MAP ) in mice .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "MAP", "type": "Chemical"}]}

Example input:
Sentence: Given alone to any accumbal subregion , GR 55562 ( 0.1-10 microg/side ) or CP 93129 ( 0.1-10 microg/side ) did not change basal locomotor activity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: Locomotor activity was assessed in male Sprague-Dawley rats tested in photocell cages .

Example answer:
{"entities": []}

Example input:
Sentence: Locomotor activity was measured again for 30 min at the beginning of days 1 and 21 of sugar access .

Example answer:
{"entities": []}

Example input:
Sentence: The locomotor activity was decreased from corresponding controls in all strains studied , except for the ICR mice , during an overnight drug-free period following the fourth amantadine treatment .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Example input:
Sentence: Nine days later locomotor activity was measured in response to a single low dose of amphetamine ( 0.5 mg/kg ) .

Example answer:
{"entities": [{"text": "amphetamine", "type": "Chemical"}]}

Input:
Sentence: Locomotor activity was recorded for individual groups by using the same treatment protocol with the EPM test .

## Item bc5cdr:test:2723
Example input:
Sentence: No changes in haloperidol-induced catalepsy or MK-801-induced locomotion were seen following PD .

Example answer:
{"entities": [{"text": "haloperidol-induced", "type": "Chemical"}, {"text": "catalepsy", "type": "Disease"}, {"text": "MK-801-induced", "type": "Chemical"}]}

Example input:
Sentence: Nicotine ( 1.0 mg/kg ) caused a significant increase in locomotor activity in rats that were habituated to the test environment , but had only a weak and delayed stimulant action in rats that were unfamiliar with the test environment .

Example answer:
{"entities": [{"text": "Nicotine", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: The effect of humoral modulators on the morphine-induced increase in locomotor activity of mice was studied .

Example answer:
{"entities": [{"text": "morphine-induced", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: Nine days later locomotor activity was measured in response to a single low dose of amphetamine ( 0.5 mg/kg ) .

Example answer:
{"entities": [{"text": "amphetamine", "type": "Chemical"}]}

Example input:
Sentence: NRA0160 and clozapine antagonized locomotor hyperactivity induced by methamphetamine ( MAP ) in mice .

Example answer:
{"entities": [{"text": "NRA0160", "type": "Chemical"}, {"text": "clozapine", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "MAP", "type": "Chemical"}]}

Example input:
Sentence: Systemic cocaine ( 10 mg/kg ) significantly increased the locomotor activity of rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The subcutaneous administration of 10 mg/kg of morphine-HC1 produced a marked increase in locomotor activity in mice .

Example answer:
{"entities": [{"text": "morphine-HC1", "type": "Chemical"}, {"text": "increase in locomotor activity", "type": "Disease"}]}

Example input:
Sentence: TRI given repeatedly to rats increases the locomotor hyperactivity induced by d-amphetamine , quinpirole and ( + ) -7-hydroxy-dipropyloaminotetralin ( dopamine D2 and D3 effects ) .

Example answer:
{"entities": [{"text": "TRI", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "d-amphetamine", "type": "Chemical"}, {"text": "quinpirole", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: At doses where alone , they produced no significant effects on locomotion , BD1018 , BD1063 and LR132 significantly attenuated the locomotor stimulatory effects of cocaine .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: The locomotor activity was decreased from corresponding controls in all strains studied , except for the ICR mice , during an overnight drug-free period following the fourth amantadine treatment .

Example answer:
{"entities": [{"text": "amantadine", "type": "Chemical"}]}

Input:
Sentence: Administration of each drug and their combinations did not produce any effect on locomotor activity .

## Item bc5cdr:test:2501
Example input:
Sentence: Amiodarone and atazanavir are recognized CYP3A4 inhibitors .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: Reduction in the dosage of amiodarone resulted in the disappearance of the sinoatrial block and the persistence of asymptomatic sinus bradycardia .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "sinoatrial block", "type": "Disease"}, {"text": "sinus bradycardia", "type": "Disease"}]}

Example input:
Sentence: Severe rhabdomyolysis and acute renal failure secondary to concomitant use of simvastatin , amiodarone , and atazanavir .

Example answer:
{"entities": [{"text": "rhabdomyolysis", "type": "Disease"}, {"text": "acute renal failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: The patient was admitted to the hospital , anticoagulated with unfractionated heparin , and given intravenous diltiazem for rate control and intravenous amiodarone for rate and rhythm control .

Example answer:
{"entities": [{"text": "heparin", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}]}

Example input:
Sentence: A case is presented of a reversible intra-Hisian block occurring under amiodarone treatment for atrial tachycardia in a patient without clear intraventricular conduction abnormalities .

Example answer:
{"entities": [{"text": "intra-Hisian block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atrial tachycardia", "type": "Disease"}, {"text": "intraventricular conduction abnormalities", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Input:
Sentence: Amiodarone , an efficacious and widely used antiarrhythmic agent , has been reported to cause hepatotoxicity in some patients .

## Item bc5cdr:test:2484
Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: He had been prescribed telithromycin 400 mg/d PO to treat an upper respiratory tract infection 7 days prior .

Example answer:
{"entities": [{"text": "telithromycin", "type": "Chemical"}, {"text": "upper respiratory tract infection", "type": "Disease"}]}

Example input:
Sentence: Jaundice disappeared within 3 months but was followed by prolonged anicteric cholestasis marked by pruritus and high levels of alkaline phosphatase and gammaglutamyltransferase activities .

Example answer:
{"entities": [{"text": "Jaundice", "type": "Disease"}, {"text": "cholestasis", "type": "Disease"}, {"text": "pruritus", "type": "Disease"}]}

Example input:
Sentence: A 54-year-old hypothyroid male taking thyroxine and simvastatin presented with bilateral leg compartment syndrome and myonecrosis .

Example answer:
{"entities": [{"text": "hypothyroid", "type": "Disease"}, {"text": "thyroxine", "type": "Chemical"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "compartment syndrome", "type": "Disease"}, {"text": "myonecrosis", "type": "Disease"}]}

Example input:
Sentence: METHODS : We present the first case report of a woman with hyperthyroidism treated with propylthiouracil in whom a syndrome of pericarditis , fever , and glomerulonephritis developed .

Example answer:
{"entities": [{"text": "hyperthyroidism", "type": "Disease"}, {"text": "propylthiouracil", "type": "Chemical"}, {"text": "pericarditis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}]}

Example input:
Sentence: A case of triamterene nephrolithiasis is reported in a man after 4 years of hydrochlorothiazide-triamterene therapy for hypertension .

Example answer:
{"entities": [{"text": "triamterene", "type": "Chemical"}, {"text": "nephrolithiasis", "type": "Disease"}, {"text": "hydrochlorothiazide-triamterene", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: Propylthiouracil therapy was withdrawn , and she was treated with a 1-month course of prednisone , which alleviated her symptoms .

Example answer:
{"entities": [{"text": "Propylthiouracil", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Input:
Sentence: In 1 patient with atopic dermatitis , telangiectatic and papular rosacea insidiously appeared after 5 months of treatment .

## Item bc5cdr:test:2531
Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Both the temporal relationship of events and the response to treatment suggest that a rapid systemic absorption of mepivacaine with adrenaline and/or interaction of these drugs with the patient 's cardiovascular medications were responsible for the perioperative complications .

Example answer:
{"entities": [{"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}]}

Example input:
Sentence: A healthy 17-year-old male received standard intermittent doses of pethidine via a patient-controlled analgesia ( PCA ) pump for management of postoperative pain control .

Example answer:
{"entities": [{"text": "pethidine", "type": "Chemical"}, {"text": "postoperative pain", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Sixty percent in Group A developed postoperative emetic symptoms , headache , or both ; 1 patient in Group B developed symptoms .

Example answer:
{"entities": [{"text": "postoperative emetic symptoms", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: In the present paper the authors describe 2 female patients who developed incontinence secondary to the selective serotonin reuptake inhibitors paroxetine and sertraline , as well as a third who developed this side effect on venlafaxine .

Example answer:
{"entities": [{"text": "incontinence", "type": "Disease"}, {"text": "serotonin", "type": "Chemical"}, {"text": "paroxetine", "type": "Chemical"}, {"text": "sertraline", "type": "Chemical"}, {"text": "venlafaxine", "type": "Chemical"}]}

Example input:
Sentence: An elderly patient treated with low dose Desipramine developed a delirium while her plasma level was in the `` subtherapeutic '' range .

Example answer:
{"entities": [{"text": "Desipramine", "type": "Chemical"}, {"text": "delirium", "type": "Disease"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: CASE SUMMARY : A 40-year-old woman with major depression took an overdose of venlafaxine in an apparent suicide attempt .

Example answer:
{"entities": [{"text": "major depression", "type": "Disease"}, {"text": "overdose", "type": "Disease"}, {"text": "venlafaxine", "type": "Chemical"}]}

Input:
Sentence: A case of postoperative anxiety due to low dose droperidol used with patient-controlled analgesia .

## Item bc5cdr:test:2730
Example input:
Sentence: CONCLUSION : This case started with a media report in a popular newspaper , initiated by published , peer-reviewed research on herbals , and involved human failure in a case history , medical examination and clinical treatment .

Example answer:
{"entities": []}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: However , cost-effective screening strategies recommended so far missed 40 to 50 % of cases improved with endocrine therapy and the pituitary tumors .

Example answer:
{"entities": [{"text": "pituitary tumors", "type": "Disease"}]}

Example input:
Sentence: We first tested whether chronic hyperprolactinemia inhibited two neuroendocrine parameters necessary for female fertility : pulsatile LH secretion and the estrogen-induced LH surge .

Example answer:
{"entities": [{"text": "hyperprolactinemia", "type": "Disease"}, {"text": "estrogen-induced", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Uni- and multivariate analyses were used to test the influence of the clinical variables : age , sex , stroke , myocardiopathy ( MP ) , duration of the test , mitral regurgitation ( MR ) and the MZ dose .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "myocardiopathy", "type": "Disease"}, {"text": "MP", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "MR", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: The pooled statistical analysis for ventricular septal ( VSD ) and midline ( MD ) defects was performed for rat fetuses exposed to piroxicam , selective and non-selective COX-2 inhibitor based on present and historic data .

Example answer:
{"entities": [{"text": "piroxicam", "type": "Chemical"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Main clinical criteria tested regarding efficiency in hormone determination were low sexual desire , small testes and gynecomastia .

Example answer:
{"entities": [{"text": "low sexual desire", "type": "Disease"}, {"text": "gynecomastia", "type": "Disease"}]}

Example input:
Sentence: On the Positive and Negative Syndrome Scale positive subscale , all treatments were superior to placebo with LOCF and MMRM ; asenapine at 5 mg BID was superior to placebo on the negative subscale with MMRM and on the general psychopathology subscale with LOCF and MMRM .

Example answer:
{"entities": [{"text": "asenapine", "type": "Chemical"}]}

Input:
Sentence: SEARCH STRATEGY : We searched the following databases up to November 2004 : the Cochrane Menstrual Disorders and Subfertility Group Trials Register , Cochrane Central Register of Controlled Trials ( CENTRAL ) , MEDLINE , EMBASE , Biological Abstracts .

## Item bc5cdr:test:2162
Example input:
Sentence: RESULTS : Six of 61 women ( 10 % ) developed clinically reversible grade 3 CHF following infusional cyclophosphamide with a median percent decline in ejection fraction of 31 % .

Example answer:
{"entities": [{"text": "CHF", "type": "Disease"}, {"text": "cyclophosphamide", "type": "Chemical"}]}

Example input:
Sentence: Dexamethasone ( 10 microg/kg per day , s.c. ) or saline was started after 4 days in Ato-treated and non-treated rats and continued for 11-13 days .

Example answer:
{"entities": [{"text": "Dexamethasone", "type": "Chemical"}, {"text": "Ato-treated", "type": "Chemical"}]}

Example input:
Sentence: Multivariate stepwise logistic regression analysis using preoperative and postoperative variables identified that an increase of serum creatinine compared with average at 1 year , 3 months , and 4 weeks postoperatively were independent risk factors for the development of CRF or ESRD with odds ratios of 2.6 , 2.2 , and 1.6 , respectively .

Example answer:
{"entities": [{"text": "creatinine", "type": "Chemical"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Using as the reference group women who were not using oral contraception , had no recent pregnancy or menopausal symptoms , the case-control analysis gave an adjusted odds ratio ( OR ( adj ) ) of 7.44 ( 95 % CI 3.67-15.08 ) for CPA/EE use compared with an OR ( adj ) of 2.58 ( 95 % CI 1.60-4.18 ) for use of conventional COCs .

Example answer:
{"entities": [{"text": "CPA/EE", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Cyproterone acetate combined with ethinyl estradiol ( CPA/EE ) is licensed in the UK for the treatment of women with acne and hirsutism and is also a treatment option for polycystic ovary syndrome ( PCOS ) .

Example answer:
{"entities": [{"text": "Cyproterone acetate", "type": "Chemical"}, {"text": "ethinyl estradiol", "type": "Chemical"}, {"text": "CPA/EE", "type": "Chemical"}, {"text": "acne", "type": "Disease"}, {"text": "hirsutism", "type": "Disease"}, {"text": "polycystic ovary syndrome", "type": "Disease"}, {"text": "PCOS", "type": "Disease"}]}

Example input:
Sentence: Forty-three ovarian cancer patients were available for analysis following six cycles of the same PAC-containing regimen : 23 had been supplemented by glutamate all along the treatment period , at a daily dose of three times 500 mg ( group G ) , and 20 had received a placebo ( group P ) .

Example answer:
{"entities": [{"text": "ovarian cancer", "type": "Disease"}, {"text": "PAC-containing", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}]}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: 17beta-Estradiol did not alter the onset of first clonus in ovariectomized rats but accelerated it in males .

Example answer:
{"entities": [{"text": "17beta-Estradiol", "type": "Chemical"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: We investigated this association , according to the type of progestagen included in third-generation ( i.e. , desogestrel or gestodene ) and second-generation ( i.e. , levonorgestrel ) oral contraceptives , the dose of estrogen , and the presence or absence of prothrombotic mutations METHODS : In a nationwide , population-based , case-control study , we identified and enrolled 248 women 18 through 49 years of age who had had a first myocardial infarction between 1990 and 1995 and 925 control women who had not had a myocardial infarction and who were matched for age , calendar year of the index event , and area of residence .

Example answer:
{"entities": [{"text": "progestagen", "type": "Chemical"}, {"text": "desogestrel", "type": "Chemical"}, {"text": "gestodene", "type": "Chemical"}, {"text": "levonorgestrel", "type": "Chemical"}, {"text": "oral contraceptives", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: In an open , cross-over , controlled design , patients were randomized to receive either DCF per os or GTN patches the first days of menses , when menstrual cramps became unendurable .

## Item bc5cdr:test:2631
Example input:
Sentence: Paclitaxel/cisplatin is an effective first-line regimen for locoregionally advanced head and neck cancer and continued study is warranted .

Example answer:
{"entities": [{"text": "Paclitaxel/cisplatin", "type": "Chemical"}, {"text": "head and neck cancer", "type": "Disease"}]}

Example input:
Sentence: Treatment with 150 mg/kg PDTC before and following status epilepticus significantly increased the mortality rate to 100 % .

Example answer:
{"entities": [{"text": "PDTC", "type": "Chemical"}, {"text": "status epilepticus", "type": "Disease"}]}

Example input:
Sentence: End-stage renal disease ( ESRD ) after orthotopic liver transplantation ( OLTX ) using calcineurin-based immunotherapy : risk of development and treatment .

Example answer:
{"entities": [{"text": "End-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: High-dose 5-fluorouracil/folinic acid infusion therapy has recently become a popular regimen for various cancers .

Example answer:
{"entities": [{"text": "5-fluorouracil/folinic acid", "type": "Chemical"}, {"text": "cancers", "type": "Disease"}]}

Example input:
Sentence: Recent reports indicate that single agent therapy with vinorelbine ( VNB ) or gemcitabine ( GEM ) may obtain a response rate of 20-30 % in elderly patients , with acceptable toxicity and improvement in symptoms and quality of life .

Example answer:
{"entities": [{"text": "vinorelbine", "type": "Chemical"}, {"text": "VNB", "type": "Chemical"}, {"text": "gemcitabine", "type": "Chemical"}, {"text": "GEM", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: A combination of 5 d of nelarabine ( AraG ) with 5 d of etoposide ( VP ) and cyclophosphamide ( CPM ) and prophylactic intrathecal chemotherapy was used as salvage therapy in seven children with refractory or relapsed T-cell leukaemia or lymphoma .

Example answer:
{"entities": [{"text": "nelarabine", "type": "Chemical"}, {"text": "AraG", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "VP", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "CPM", "type": "Chemical"}]}

Example input:
Sentence: We used an in vitro model of chemotherapy induced peripheral neuropathy that closely mimic the in vivo condition by exposing primary cultures of dorsal root ganglion ( DRG ) sensory neurons to paclitaxel and cisplatin , two widely used and highly effective chemotherapeutic drugs .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "cisplatin", "type": "Chemical"}]}

Example input:
Sentence: Toxic peripheral neuropathy is still a significant limiting factor for chemotherapy with paclitaxel ( PAC ) , although glutamate and its closely related amino acid glutamine were claimed to ameliorate PAC neurotoxicity .

Example answer:
{"entities": [{"text": "peripheral neuropathy", "type": "Disease"}, {"text": "paclitaxel", "type": "Chemical"}, {"text": "PAC", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "amino acid", "type": "Chemical"}, {"text": "glutamine", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}]}

Example input:
Sentence: High-dose intravenous methotrexate is an effective treatment for the induction of remission after meningeal relapse in acute lymphoblastic leukemia .

Example answer:
{"entities": [{"text": "methotrexate", "type": "Chemical"}, {"text": "acute lymphoblastic leukemia", "type": "Disease"}]}

Example input:
Sentence: STUDY DESIGN : We combined paclitaxel , melphalan and high-dose cyclophosphamide , thiotepa , and carboplatin in a triple sequential high-dose regimen for patients with metastatic breast cancer .

Example answer:
{"entities": [{"text": "paclitaxel", "type": "Chemical"}, {"text": "melphalan", "type": "Chemical"}, {"text": "cyclophosphamide", "type": "Chemical"}, {"text": "thiotepa", "type": "Chemical"}, {"text": "carboplatin", "type": "Chemical"}, {"text": "breast cancer", "type": "Disease"}]}

Input:
Sentence: High-dose intravenous melphalan followed by peripheral blood stem cell transplant ( PBSCT ) appears to be the most promising therapy , but treatment mortality can be high .

## Item bc5cdr:test:2491
Example input:
Sentence: The antiepileptic drugs , phenobarbitone and carbamazepine are well known to cause cognitive impairment on chronic use .

Example answer:
{"entities": [{"text": "phenobarbitone", "type": "Chemical"}, {"text": "carbamazepine", "type": "Chemical"}, {"text": "cognitive impairment", "type": "Disease"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Using functional imaging and a face-learning task , we investigated neural correlates of encoding and recalling face-name associations in 20 recreational drug users whose predominant drug use was ecstasy and 20 controls .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "Disease"}, {"text": "MDMA", "type": "Chemical"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "Chemical"}, {"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Brain MR studies , including DW imaging , were prospectively performed in 14 organ transplant patients receiving tacrolimus who developed neurologic complications .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "neurologic complications", "type": "Disease"}]}

Example input:
Sentence: Initial brain magnetic resonance imaging ( MRI ) were obtained after the hospitalization , including DWI ( 8/8 ) , apparent diffusion coefficient ( ADC ) map ( 4/8 ) , FLAIR ( 7/8 ) , and T2-weighted image ( 8/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: These data lend further support to the proposal that cognitive processes mediated by the prefrontal cortex may be impaired by recreational ecstasy use .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Cranial magnetic resonance imaging and extensive laboratory studies failed to reveal structural lesions of the brain and metabolic abnormalities .

Example answer:
{"entities": [{"text": "structural lesions of the brain", "type": "Disease"}, {"text": "metabolic abnormalities", "type": "Disease"}]}

Input:
Sentence: Using magnetic resonance imaging ( MRI ) and new computational brain-mapping techniques , we determined the pattern of structural brain alterations associated with chronic MA abuse in human subjects and related these deficits to cognitive impairment .

## Item bc5cdr:test:2354
Example input:
Sentence: Although generally consisted safe when given intramuscularly , intravenous administration is known to cause respiratory and cardiovascular depression .

Example answer:
{"entities": []}

Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: Epinephrine has a proven role in cardiac arrest in prehospital care ; however , use by paramedics in patients with suspected allergic reaction and severe hypertension should be viewed with caution .

Example answer:
{"entities": [{"text": "Epinephrine", "type": "Chemical"}, {"text": "cardiac arrest", "type": "Disease"}, {"text": "allergic reaction", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: We report a case in which myocardial infarction coincided with the introduction of captopril and the withdrawal of verapamil in a previously asymptomatic woman with severe hypertension .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "captopril", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "hypertension", "type": "Disease"}]}

Example input:
Sentence: During the first day of hospitalization ( while intubated ) , intravenous metoprolol was given , resulting in severe angioedema .

Example answer:
{"entities": [{"text": "metoprolol", "type": "Chemical"}, {"text": "angioedema", "type": "Disease"}]}

Example input:
Sentence: One of the twins developed complete heart block and dilated cardiomyopathy related to lopinavir/ritonavir therapy , a boosted protease-inhibitor agent , while the other twin developed mild bradycardia .

Example answer:
{"entities": [{"text": "heart block", "type": "Disease"}, {"text": "dilated cardiomyopathy", "type": "Disease"}, {"text": "lopinavir/ritonavir", "type": "Chemical"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: The patient had no apparent associated conditions which might have predisposed him to the development of bradyarrhythmias ; and , thus , this probably represented a true idiosyncrasy to lidocaine .

Example answer:
{"entities": [{"text": "bradyarrhythmias", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Input:
Sentence: Both patients were treated preoperatively with beta-adrenergic antagonist medications , which may have masked the cardiovascular signs of the unintentional intravascular administration of levobupivacaine with epinephrine .

## Item bc5cdr:test:2546
Example input:
Sentence: The possible beneficial effect of ribavirin during the initial days of AHF is discussed .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "AHF", "type": "Disease"}]}

Example input:
Sentence: In the present study , we have investigated the molecular mechanisms by which female hormones influence cholesterol metabolism in macrophages in response to the HIV protease inhibitor ritonavir .

Example answer:
{"entities": [{"text": "cholesterol", "type": "Chemical"}, {"text": "ritonavir", "type": "Chemical"}]}

Example input:
Sentence: Can angiogenesis be a target of treatment for ribavirin associated hemolytic anemia ?

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: Future research with larger number of patients is needed to find out modifiable factors that will improve the safety of ribavirin therapy .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Tolerance and antiviral effect of ribavirin in patients with Argentine hemorrhagic fever .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "Argentine hemorrhagic fever", "type": "Disease"}]}

Example input:
Sentence: Administration of ribavirin resulted in a neutralization of viremia and a drop of endogenous interferon titers .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "viremia", "type": "Disease"}]}

Example input:
Sentence: Tolerance and antiviral effect of ribavirin was studied in 6 patients with Argentine hemorrhagic fever ( AHF ) of more than 8 days of evolution .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "Argentine hemorrhagic fever", "type": "Disease"}, {"text": "AHF", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: From these results , we conclude that ribavirin has an antiviral effect in advanced cases of AHF , and that anemia , the only secondary reaction observed , can be easily managed .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "AHF", "type": "Disease"}, {"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This is the first study in the literature investigating a link between angiogenesis soluble markers and ribavirin induced anemia in patients with hepatitis C and we could not find any relation .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}, {"text": "hepatitis C", "type": "Disease"}]}

Input:
Sentence: This study was conducted to identify the factors contributing to ribavirin-induced anemia .

## Item bc5cdr:test:2737
Example input:
Sentence: CONCLUSIONS : The combination of cisplatin and amifostine in this study resulted in an overall response rate of 16 % .

Example answer:
{"entities": [{"text": "cisplatin", "type": "Chemical"}, {"text": "amifostine", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : Six of 30 patients ( 20 % ) without prior chemotherapy achieved a partial response ( PR ) ( 95 % confidence interval [ CI ] , 8 % to 39 % ) .

Example answer:
{"entities": []}

Example input:
Sentence: Prospective multicentre studies with a large population and a long follow-up should be performed in order to evaluate the incidence of this unusual side effect .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : Fourteen subjects completed both treatment arms .

Example answer:
{"entities": []}

Example input:
Sentence: Uni- and multivariate analyses were used to test the influence of the clinical variables : age , sex , stroke , myocardiopathy ( MP ) , duration of the test , mitral regurgitation ( MR ) and the MZ dose .

Example answer:
{"entities": [{"text": "stroke", "type": "Disease"}, {"text": "myocardiopathy", "type": "Disease"}, {"text": "MP", "type": "Disease"}, {"text": "mitral regurgitation", "type": "Disease"}, {"text": "MR", "type": "Disease"}, {"text": "MZ", "type": "Chemical"}]}

Example input:
Sentence: We believe the results of those studies may have been affected by residual confounding .

Example answer:
{"entities": []}

Example input:
Sentence: In addition , a statistically significant reduction was also observed on the level of GABA and glycine but less than a drastic reduction of glutamate and aspartate level .

Example answer:
{"entities": [{"text": "GABA", "type": "Chemical"}, {"text": "glycine", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}]}

Example input:
Sentence: Nineteen patients finished the trial , and in 18 cases the therapeutic result was considered very good to good .

Example answer:
{"entities": []}

Example input:
Sentence: Secondary outcomes were a postdose SCr increase > or = 25 % , a postdose estimated glomerular filtration rate decrease of > or = 25 % , and the mean peak change in SCr .

Example answer:
{"entities": []}

Example input:
Sentence: RESULTS : The sensitivity improved dramatically from 16 % to 79 % , positive predictive value increased from 60 % to 68 % and negative predictive value from 54 % to 78 % , and specificity decreased from 90 % to 67 % .

Example answer:
{"entities": []}

Input:
Sentence: MAIN RESULTS : All the statistically significant results were derived from the two biggest trials .

## Item bc5cdr:test:2685
Example input:
Sentence: These 13 included cases of malignant hypertension , thrombotic microangiopathy , lupus nephritis , Henoch-Schonlein nephritis , crescentic glomerulonephritis , and cocaine-related acute renal failure .

Example answer:
{"entities": [{"text": "malignant hypertension", "type": "Disease"}, {"text": "thrombotic microangiopathy", "type": "Disease"}, {"text": "lupus nephritis", "type": "Disease"}, {"text": "Henoch-Schonlein nephritis", "type": "Disease"}, {"text": "glomerulonephritis", "type": "Disease"}, {"text": "cocaine-related", "type": "Chemical"}, {"text": "acute renal failure", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: Overall survival from the time of OLTX was not significantly different among groups , but by year 13 , the survival of the patients who had ESRD was only 28.2 % compared with 54.6 % in the control group .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Patients who develop ESRD have a higher preoperative and 1-year serum creatinine and are more likely to have hepatorenal syndrome .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: RESULTS : At 13 years after OLTX , the incidence of severe renal dysfunction was 18.1 % ( CRF 8.6 % and ESRD 9.5 % ) .

Example answer:
{"entities": [{"text": "renal dysfunction", "type": "Disease"}, {"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Recently , however , we have had an increase of patients who are presenting after OLTX with end-stage renal disease ( ESRD ) .

Example answer:
{"entities": [{"text": "end-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: This retrospective study examines the incidence and treatment of ESRD and chronic renal failure ( CRF ) in OLTX patients .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "CRF", "type": "Disease"}]}

Example input:
Sentence: The development of ESRD decreases survival , particularly in those patients treated with dialysis only .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Patients developing ESRD had a 6-year survival after onset of ESRD of 27 % for the patients receiving hemodialysis versus 71.4 % for the patients developing ESRD who subsequently received kidney transplants .

Example answer:
{"entities": [{"text": "ESRD", "type": "Disease"}]}

Input:
Sentence: METHODS : The cases were all patients entering the local dialysis program because of ESRD in the study area between June 1 , 1995 and November 30 , 1997 .

## Item bc5cdr:test:2682
Example input:
Sentence: Habitual use of acetaminophen as a risk factor for chronic renal failure : a comparison with phenacetin .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}]}

Example input:
Sentence: This study shows that prolonged analgesic treatment in Fischer 344 rats causes progressive and irreversible damage to the interstitial matrix and type 1 interstitial cells leading to RPN .

Example answer:
{"entities": [{"text": "RPN", "type": "Disease"}]}

Example input:
Sentence: Renal papillary necrosis ( RPN ) and a decreased urinary concentrating ability developed during continuous long-term treatment with aspirin and paracetamol in female Fischer 344 rats .

Example answer:
{"entities": [{"text": "Renal papillary necrosis", "type": "Disease"}, {"text": "RPN", "type": "Disease"}, {"text": "aspirin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: The risk of renal papillary necrosis was increased nearly 20-fold by consumption of phenacetin , which also increased the risk for cancer of the renal pelvis and bladder but not for ureteric cancer .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "ureteric cancer", "type": "Disease"}]}

Example input:
Sentence: Renal structure and concentrating ability were examined after a recovery period of up to 18 weeks , when no analgesics were given , to investigate whether the analgesic-induced changes were reversible .

Example answer:
{"entities": []}

Example input:
Sentence: Hyperkalemia has recently been recognized as a complication of nonsteroidal antiinflammatory agents ( NSAID ) such as indomethacin .

Example answer:
{"entities": [{"text": "Hyperkalemia", "type": "Disease"}, {"text": "indomethacin", "type": "Chemical"}]}

Example input:
Sentence: The risk of developing renal papillary necrosis or cancer of the renal pelvis , ureter or bladder associated with consumption of either phenacetin or paracetamol was calculated from data acquired by questionnaire from 381 cases and 808 controls .

Example answer:
{"entities": [{"text": "renal papillary necrosis", "type": "Disease"}, {"text": "phenacetin", "type": "Chemical"}, {"text": "paracetamol", "type": "Chemical"}]}

Example input:
Sentence: Six epidemiologic studies in the United States and Europe indicate that habitual use of phenacetin is associated with the development of chronic renal failure and end-stage renal disease ( ESRD ) , with a relative risk in the range of 4 to 19 .

Example answer:
{"entities": [{"text": "phenacetin", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "end-stage renal disease", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: However , three case control studies , one each in North Carolina , northern Maryland , and West Berlin , Germany , showed that habitual use of acetaminophen is also associated with chronic renal failure and ESRD , with a relative risk in the range of 2 to 4 .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "chronic renal failure", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}]}

Example input:
Sentence: Since nonsteroidal anti-inflammatory agents interfere with this compensatory mechanism and may cause acute renal failure , they should be used with caution in such patients .

Example answer:
{"entities": [{"text": "acute renal failure", "type": "Disease"}]}

Input:
Sentence: Case-control study of regular analgesic and nonsteroidal anti-inflammatory use and end-stage renal disease .

## Item bc5cdr:test:2489
Example input:
Sentence: Immunological activation has been proposed to play a role in methamphetamine-induced dopaminergic terminal damage .

Example answer:
{"entities": [{"text": "methamphetamine-induced", "type": "Chemical"}, {"text": "dopaminergic terminal damage", "type": "Disease"}]}

Example input:
Sentence: Methamphetamine ( 10 mg/kg sc ) , administered five times , reduced the levels of dopamine and its metabolites in striatal tissue when measured 72 h after the last injection .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Moreover , systemic lipopolysaccharide pretreatment ( 1 mg/kg ) attenuated local methamphetamine infusion-produced dopamine and 3,4-dihydroxyphenylacetic acid depletions in the striatum , indicating that the protective effect of lipopolysaccharide is less likely due to interrupted peripheral distribution or metabolism of methamphetamine .

Example answer:
{"entities": [{"text": "lipopolysaccharide", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "3,4-dihydroxyphenylacetic acid", "type": "Chemical"}]}

Example input:
Sentence: Dental patients abusing methamphetamine can present with poor oral hygiene , xerostomia , rampant caries ( `` meth mouth '' ) , and excessive tooth wear .

Example answer:
{"entities": [{"text": "methamphetamine", "type": "Chemical"}, {"text": "xerostomia", "type": "Disease"}, {"text": "caries", "type": "Disease"}, {"text": "meth", "type": "Chemical"}, {"text": "mouth", "type": "Disease"}, {"text": "tooth wear", "type": "Disease"}]}

Example input:
Sentence: Learning and memory deficits in ecstasy users and their neural correlates during a face-learning task .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: In addition , working memory processing in ecstasy users has been shown to be associated with neural alterations in hippocampal and/or cortical regions as measured by functional magnetic resonance imaging ( fMRI ) .

Example answer:
{"entities": [{"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: Methamphetamine ( METH ) damages dopamine ( DA ) nerve endings by a process that has been linked to microglial activation but the signaling pathways that mediate this response have not yet been delineated .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "METH", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}, {"text": "DA", "type": "Chemical"}]}

Example input:
Sentence: In recent years working memory deficits have been reported in users of MDMA ( 3,4-methylenedioxymethamphetamine , ecstasy ) .

Example answer:
{"entities": [{"text": "memory deficits", "type": "Disease"}, {"text": "MDMA", "type": "Chemical"}, {"text": "3,4-methylenedioxymethamphetamine", "type": "Chemical"}, {"text": "ecstasy", "type": "Chemical"}]}

Example input:
Sentence: The prolonged depletion of dopamine in the striatum in mice , given multiple injections of methamphetamine , was also antagonized dose-dependently and completely by LY274614 .

Example answer:
{"entities": [{"text": "dopamine", "type": "Chemical"}, {"text": "methamphetamine", "type": "Chemical"}, {"text": "LY274614", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Methamphetamine is a very addictive , powerful stimulant that increases wakefulness and physical activity and can produce other effects such as cardiac dysrhythmias , hypertension , hallucinations , and violent behavior .

Example answer:
{"entities": [{"text": "Methamphetamine", "type": "Chemical"}, {"text": "cardiac dysrhythmias", "type": "Disease"}, {"text": "hypertension", "type": "Disease"}, {"text": "hallucinations", "type": "Disease"}, {"text": "violent behavior", "type": "Disease"}]}

Input:
Sentence: We visualize , for the first time , the profile of structural deficits in the human brain associated with chronic methamphetamine ( MA ) abuse .

## Item bc5cdr:test:2213
Example input:
Sentence: He developed acute neurologic symptoms of mental confusion , disorientation and irritability , and then lapsed into a deep coma , lasting for approximately 40 hours during the first dose ( day 2 ) of 5-fluorouracil and folinic acid infusion .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "disorientation", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "coma", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Acute confusion induced by a high-dose infusion of 5-fluorouracil and folinic acid .

Example answer:
{"entities": [{"text": "confusion", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Treatment of previously treated metastatic breast cancer by mitoxantrone and 48-hour continuous infusion of high-dose 5-FU and leucovorin ( MFL ) : low palliative benefit and high treatment-related toxicity .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "MFL", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: This complication reappeared on day 25 during the second dose of 5-fluorouracil and folinic acid , which were then the only drugs given .

Example answer:
{"entities": [{"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}]}

Example input:
Sentence: Because folinic acid was unlikely to be associated with this condition , neurotoxicity due to high-dose 5-fluorouracil was highly suspected .

Example answer:
{"entities": [{"text": "folinic acid", "type": "Chemical"}, {"text": "neurotoxicity", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}]}

Example input:
Sentence: From October 1993 to November 1995 , we treated 13 patients with previously chemotherapy-treated metastatic breast cancer by mitoxantrone , 12 mg/m2 , on day 1 and continuous infusion of 5-FU , 3000 mg/m2 , together with leucovorin , 300 mg/m2 , for 48 h from day 1 to 2 .

Example answer:
{"entities": [{"text": "breast cancer", "type": "Disease"}, {"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}]}

Example input:
Sentence: Combination chemotherapy with mitoxantrone , high-dose 5-fluorouracil ( 5-FU ) and leucovorin ( MFL regimen ) had been reported as an effective and well tolerated regimen .

Example answer:
{"entities": [{"text": "mitoxantrone", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "leucovorin", "type": "Chemical"}, {"text": "MFL regimen", "type": "Chemical"}]}

Example input:
Sentence: IMPORTANCE OF THE FIELD : Fluoropyrimidines , in particular 5-fluorouracil ( 5-FU ) , have been the mainstay of treatment for several solid tumors , including colorectal , breast and head and neck cancers , for > 40 years .

Example answer:
{"entities": [{"text": "Fluoropyrimidines", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "5-FU", "type": "Chemical"}, {"text": "tumors", "type": "Disease"}]}

Example input:
Sentence: High-dose 5-fluorouracil/folinic acid infusion therapy has recently become a popular regimen for various cancers .

Example answer:
{"entities": [{"text": "5-fluorouracil/folinic acid", "type": "Chemical"}, {"text": "cancers", "type": "Disease"}]}

Example input:
Sentence: A 61-year-old man was treated with combination chemotherapy incorporating cisplatinum , etoposide , high-dose 5-fluorouracil ( 2,250 mg/m2/24 hours ) and folinic acid for an inoperable gastric adenocarcinoma .

Example answer:
{"entities": [{"text": "cisplatinum", "type": "Chemical"}, {"text": "etoposide", "type": "Chemical"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "folinic acid", "type": "Chemical"}, {"text": "gastric adenocarcinoma", "type": "Disease"}]}

Input:
Sentence: High-dose 5-fluorouracil / folinic acid in combination with three-weekly mitomycin C in the treatment of advanced gastric cancer .

## Item bc5cdr:test:2536
Example input:
Sentence: The side effect profiles of the atypical antipsychotics are more advantageous than those of the conventional neuroleptics .

Example answer:
{"entities": []}

Example input:
Sentence: Minor side effects included nausea ( thirteen patients ) , emesis ( eight of the thirteen patients with nausea ) , clumsiness ( evident as ataxic movements in ten patients ) , and dysphoric reaction ( one patient ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "emesis", "type": "Disease"}, {"text": "clumsiness", "type": "Disease"}, {"text": "ataxic movements", "type": "Disease"}, {"text": "dysphoric reaction", "type": "Disease"}]}

Example input:
Sentence: The newer atypical agents have a lower risk of EPS , but are associated in varying degrees with sedation , cardiovascular effects , anticholinergic effects , weight gain , sexual dysfunction , hepatic effects , lowered seizure threshold ( primarily clozapine ) , and agranulocytosis ( clozapine only ) .

Example answer:
{"entities": [{"text": "EPS", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "clozapine", "type": "Chemical"}, {"text": "agranulocytosis", "type": "Disease"}]}

Example input:
Sentence: Previous clinical studies have proposed that risperidone 's pharmacologic profile may produce improved efficacy for negative psychotic symptoms and decreased propensity for extrapyramidal side effects ; features shared by so-called 'atypical ' neuroleptics .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "psychotic symptoms", "type": "Disease"}]}

Example input:
Sentence: Extrapyramidal symptoms reported as AEs occurred in 15 % and 18 % , 34 % , and 10 % of the asenapine at 5 and 10 mg BID , haloperidol , and placebo groups , respectively .

Example answer:
{"entities": [{"text": "Extrapyramidal symptoms", "type": "Disease"}, {"text": "asenapine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: In phase A , extrapyramidal signs tended to be greater with the standard dose than in the other two conditions , primarily because of a subgroup ( 20 % ) who developed moderate to severe signs .

Example answer:
{"entities": [{"text": "extrapyramidal signs", "type": "Disease"}]}

Example input:
Sentence: Extrapyramidal side effects with risperidone and haloperidol at comparable D2 receptor occupancy levels .

Example answer:
{"entities": [{"text": "risperidone", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Although initially thought to be free of extrapyramidal side effects , sulpiride-induced tardive dyskinesia and parkinsonism have been reported occasionally .

Example answer:
{"entities": [{"text": "sulpiride-induced", "type": "Chemical"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "parkinsonism", "type": "Disease"}]}

Example input:
Sentence: Nine patients exhibited mild to moderate extrapyramidal concomitant symptoms ; no other side effects were observed .

Example answer:
{"entities": [{"text": "extrapyramidal concomitant symptoms", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Input:
Sentence: We feel that , although the dramatic extrapyramidal side effects of dopaminergic antiemetics are well known , more subtle manifestations may easily be overlooked .

## Item bc5cdr:test:2289
Example input:
Sentence: The most important findings were that compared with values in control subjects , end-systolic left ventricular posterior wall dimension and percent of left ventricular posterior wall thickening in doxorubicin-treated patients were decreased at baseline study and these findings were more clearly delineated with dobutamine stimulation .

Example answer:
{"entities": [{"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}]}

Example input:
Sentence: Administration of salvianolic acid A for a period of 8 days significantly attenuated isoproterenol-induced cardiac dysfunction and myocardial injury and improved mitochondrial respiratory function .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "cardiac dysfunction", "type": "Disease"}, {"text": "myocardial injury", "type": "Disease"}]}

Example input:
Sentence: Mitochondrial injury may be involved in the progression of heart failure caused by adriamycin via the autophagy pathway .

Example answer:
{"entities": [{"text": "heart failure", "type": "Disease"}, {"text": "adriamycin", "type": "Chemical"}]}

Example input:
Sentence: Dobutamine stress echocardiography : a sensitive indicator of diminished myocardial function in asymptomatic doxorubicin-treated long-term survivors of childhood cancer .

Example answer:
{"entities": [{"text": "Dobutamine", "type": "Chemical"}, {"text": "doxorubicin-treated", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "respiratory dysfunction", "type": "Disease"}, {"text": "ADP/O", "type": "Chemical"}, {"text": "isoproterenol-treated", "type": "Chemical"}]}

Example input:
Sentence: Serious adverse effects are uncommon and mainly have been related to the depression of cardiac contractility and conduction , especially when the drug is combined with beta-blocking agents .

Example answer:
{"entities": [{"text": "depression", "type": "Disease"}]}

Example input:
Sentence: The results of our study suggest that salvianolic acid A possessing antioxidant activity has a significant protective effect against isoproterenol-induced myocardial infarction .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: Doxorubicin is an effective anticancer chemotherapeutic agent known to cause acute and chronic cardiomyopathy .

Example answer:
{"entities": [{"text": "Doxorubicin", "type": "Chemical"}, {"text": "cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: To develop a more sensitive echocardiographic screening test for cardiac damage due to doxorubicin , a cohort study was performed using dobutamine infusion to differentiate asymptomatic long-term survivors of childhood cancer treated with doxorubicin from healthy control subjects .

Example answer:
{"entities": [{"text": "cardiac damage", "type": "Disease"}, {"text": "doxorubicin", "type": "Chemical"}, {"text": "dobutamine", "type": "Chemical"}, {"text": "cancer", "type": "Disease"}]}

Input:
Sentence: The objective of this investigation was to test the hypothesis that carvedilol , a nonselective beta-adrenergic receptor antagonist with potent antioxidant properties , protects against the cardiac and hepatic mitochondrial bioenergetic dysfunction associated with subchronic doxorubicin toxicity .

## Item bc5cdr:test:2342
Example input:
Sentence: CNS complications included posterior reversible leukoencephalopathy syndrome ( n = 10 ) , stroke ( n = 5 ) , temporal lobe epilepsy ( n = 2 ) , high-dose methotrexate toxicity ( n = 2 ) , syndrome of inappropriate antidiuretic hormone secretion ( n = 1 ) , and other unclassified events ( n = 7 ) .

Example answer:
{"entities": [{"text": "leukoencephalopathy", "type": "Disease"}, {"text": "stroke", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}, {"text": "methotrexate", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "inappropriate antidiuretic hormone secretion", "type": "Disease"}]}

Example input:
Sentence: Compared with placebo subjects , alprazolam patients developed more adverse reactions ( 21 % v. 0 % ) of depression , enuresis , disinhibition and aggression ; and more side-effects , particularly sedation , irritability , impaired memory , weight loss and ataxia .

Example answer:
{"entities": [{"text": "alprazolam", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "enuresis", "type": "Disease"}, {"text": "aggression", "type": "Disease"}, {"text": "irritability", "type": "Disease"}, {"text": "impaired memory", "type": "Disease"}, {"text": "weight loss", "type": "Disease"}, {"text": "ataxia", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events were nausea ( 17.2 % and 16.1 % ; 95 % CI , -3.7 to 6.0 ) , hiccups ( 10.7 % and 6.6 % ; 95 % CI , 0.5 to 7.8 ) , and headache ( 8.7 % and 9.9 % ; 95 % Cl , -5.0 to 2.6 ) .

Example answer:
{"entities": [{"text": "nausea", "type": "Disease"}, {"text": "hiccups", "type": "Disease"}, {"text": "headache", "type": "Disease"}]}

Example input:
Sentence: One patient was prematurely discontinued from the study for severe headache and abdominal pain .

Example answer:
{"entities": [{"text": "headache", "type": "Disease"}, {"text": "abdominal pain", "type": "Disease"}]}

Example input:
Sentence: Five hours after exposure , he developed disulfiram-like syndrome with flushing , tachycardia , and arterial hypotension after consuming three glasses of wine .

Example answer:
{"entities": [{"text": "disulfiram-like", "type": "Chemical"}, {"text": "flushing", "type": "Disease"}, {"text": "tachycardia", "type": "Disease"}, {"text": "arterial hypotension", "type": "Disease"}]}

Example input:
Sentence: However , use of BZDs/RDs was associated with dizziness , inability to sleep after awaking at night and tiredness in the mornings during the week prior to admission and with stronger depressive symptoms measured at the beginning of the hospital stay .

Example answer:
{"entities": [{"text": "BZDs/RDs", "type": "Chemical"}, {"text": "dizziness", "type": "Disease"}, {"text": "inability to sleep", "type": "Disease"}, {"text": "tiredness", "type": "Disease"}, {"text": "depressive symptoms", "type": "Disease"}]}

Example input:
Sentence: Conventional agents are associated with unwanted central nervous system effects , including extrapyramidal symptoms ( EPS ) , tardive dyskinesia , sedation , and possible impairment of some cognitive measures , as well as cardiac effects , orthostatic hypotension , hepatic changes , anticholinergic side effects , sexual dysfunction , and weight gain .

Example answer:
{"entities": [{"text": "extrapyramidal symptoms", "type": "Disease"}, {"text": "EPS", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "sexual dysfunction", "type": "Disease"}, {"text": "weight gain", "type": "Disease"}]}

Example input:
Sentence: Other possible adverse effects -- such as gastrointestinal disorders , orthostatic hypotension , levodopa-induced psychosis , sleep disturbances or parasomnias , or drug interactions -- also require carefully monitored individual treatment .

Example answer:
{"entities": [{"text": "gastrointestinal disorders", "type": "Disease"}, {"text": "orthostatic hypotension", "type": "Disease"}, {"text": "levodopa-induced", "type": "Chemical"}, {"text": "psychosis", "type": "Disease"}, {"text": "sleep disturbances", "type": "Disease"}, {"text": "parasomnias", "type": "Disease"}]}

Example input:
Sentence: Grade 3-4 adverse effects included myelosuppression , fatigue , somnolence/depressed mood , neuropathy and dyspnea .

Example answer:
{"entities": [{"text": "myelosuppression", "type": "Disease"}, {"text": "fatigue", "type": "Disease"}, {"text": "somnolence/depressed mood", "type": "Disease"}, {"text": "neuropathy", "type": "Disease"}, {"text": "dyspnea", "type": "Disease"}]}

Example input:
Sentence: The most common adverse events ( incidence > or = 5 % in one group ) after rizatriptan and ergotamine/caffeine , respectively , were dizziness ( 6.7 and 5.3 % ) , nausea ( 4.2 and 8.5 % ) and somnolence ( 5.5 and 2.3 % ) .

Example answer:
{"entities": [{"text": "rizatriptan", "type": "Chemical"}, {"text": "ergotamine/caffeine", "type": "Chemical"}, {"text": "dizziness", "type": "Disease"}, {"text": "nausea", "type": "Disease"}, {"text": "somnolence", "type": "Disease"}]}

Input:
Sentence: Adverse effects included constipation , morning drowsiness , dizziness and rash , and resulted in withdrawal from the study by three men .

## Item bc5cdr:test:2054
Example input:
Sentence: 99mTc-glucarate for detection of isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Example input:
Sentence: These findings indicate the synergistic protective effect of green tea and vitamin E during ISO induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "ISO", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: The present study was aimed to investigate the combined effects of green tea and vitamin E on heart weight , body weight , serum marker enzymes , lipid peroxidation , endogenous antioxidants and membrane bound ATPases in isoproterenol ( ISO ) -induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "ISO", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In vivo protection of dna damage associated apoptotic and necrotic cell deaths during acetaminophen-induced nephrotoxicity , amiodarone-induced lung toxicity and doxorubicin-induced cardiotoxicity by a novel IH636 grape seed proanthocyanidin extract .

Example answer:
{"entities": [{"text": "necrotic", "type": "Disease"}, {"text": "acetaminophen-induced", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}, {"text": "amiodarone-induced", "type": "Chemical"}, {"text": "lung toxicity", "type": "Disease"}, {"text": "doxorubicin-induced", "type": "Chemical"}, {"text": "cardiotoxicity", "type": "Disease"}, {"text": "IH636 grape seed proanthocyanidin extract", "type": "Chemical"}]}

Example input:
Sentence: The present study was designed to evaluate the cardioprotective potential of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Cardioprotective effect of salvianolic acid A on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "salvianolic acid A", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Effect of green tea and vitamin E combination in isoproterenol induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "green tea", "type": "Chemical"}, {"text": "vitamin E", "type": "Chemical"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Cardioprotective effect of tincture of Crataegus on isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "tincture of Crataegus", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Input:
Sentence: The cardioprotective effect of the ethanol extract of Picrorrhiza kurroa rhizomes and roots ( PK ) on isoproterenol-induced myocardial infarction in rats with respect to lipid metabolism in serum and heart tissue has been investigated .

## Item bc5cdr:test:2698
Example input:
Sentence: Bromocriptine-induced hypotension was unaffected by isoproterenol pretreatment , while tachycardia was reversed to significant bradycardia , an effect that was partly reduced by i.v .

Example answer:
{"entities": [{"text": "Bromocriptine-induced", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}, {"text": "bradycardia", "type": "Disease"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Four compounds known to increase QT interval and cause TDP were investigated : terfenadine , terodiline , cisapride and E4031 .

Example answer:
{"entities": [{"text": "TDP", "type": "Disease"}, {"text": "terfenadine", "type": "Chemical"}, {"text": "terodiline", "type": "Chemical"}, {"text": "cisapride", "type": "Chemical"}, {"text": "E4031", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: Iatrogenically induced intractable atrioventricular reentrant tachycardia after verapamil and catheter ablation in a patient with Wolff-Parkinson-White syndrome and idiopathic dilated cardiomyopathy .

Example answer:
{"entities": [{"text": "atrioventricular reentrant tachycardia", "type": "Disease"}, {"text": "verapamil", "type": "Chemical"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "idiopathic dilated cardiomyopathy", "type": "Disease"}]}

Example input:
Sentence: These patients had Q-T prolongation and recurrent syncope due to polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "Q-T prolongation", "type": "Disease"}, {"text": "syncope", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: Development of ocular myasthenia during pegylated interferon and ribavirin treatment for chronic hepatitis C. A 63-year-old male experienced sudden diplopia after 9 weeks of administration of pegylated interferon ( IFN ) alpha-2b and ribavirin for chronic hepatitis C ( CHC ) .

Example answer:
{"entities": [{"text": "ocular myasthenia", "type": "Disease"}, {"text": "pegylated interferon", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}, {"text": "chronic hepatitis", "type": "Disease"}, {"text": "diplopia", "type": "Disease"}, {"text": "pegylated interferon ( IFN ) alpha-2b", "type": "Chemical"}, {"text": "chronic hepatitis C", "type": "Disease"}, {"text": "CHC", "type": "Disease"}]}

Example input:
Sentence: These seven cases demonstrate that procainamide can produce an acquired prolonged Q-T syndrome with polymorphous ventricular tachycardia .

Example answer:
{"entities": [{"text": "procainamide", "type": "Chemical"}, {"text": "prolonged Q-T syndrome", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: The patient 's ophthalmological symptoms improved rapidly 3 weeks after discontinuation of pegylated IFN alpha-2b and ribavirin .

Example answer:
{"entities": [{"text": "pegylated IFN alpha-2b", "type": "Chemical"}, {"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: We postulate that by virtue of its direct blocking action on IKr , ketoconazole alone may prolong QT interval and induce TdP .

Example answer:
{"entities": [{"text": "ketoconazole", "type": "Chemical"}, {"text": "TdP", "type": "Disease"}]}

Input:
Sentence: The QT prolongation appeared to respond to administration of i.v .

## Item bc5cdr:test:2549
Example input:
Sentence: Severe and clinically evident anemia was easily corrected by subcutaneous injections ( 3 times/week for 1 month ) of recombinant erythropoietin ( rHuEPO-beta ) .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}]}

Example input:
Sentence: Future research with larger number of patients is needed to find out modifiable factors that will improve the safety of ribavirin therapy .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}]}

Example input:
Sentence: Can angiogenesis be a target of treatment for ribavirin associated hemolytic anemia ?

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : Our data suggest that rHuEPO-beta correctable CAB-induced anemia occurs in 14.3 % of prostate cancer patients after 6 months of therapy .

Example answer:
{"entities": [{"text": "anemia", "type": "Disease"}, {"text": "prostate cancer", "type": "Disease"}]}

Example input:
Sentence: Tolerance and antiviral effect of ribavirin in patients with Argentine hemorrhagic fever .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "Argentine hemorrhagic fever", "type": "Disease"}]}

Example input:
Sentence: CONCLUSION : This is the first study in the literature investigating a link between angiogenesis soluble markers and ribavirin induced anemia in patients with hepatitis C and we could not find any relation .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "anemia", "type": "Disease"}, {"text": "hepatitis C", "type": "Disease"}]}

Example input:
Sentence: Tolerance and antiviral effect of ribavirin was studied in 6 patients with Argentine hemorrhagic fever ( AHF ) of more than 8 days of evolution .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "Argentine hemorrhagic fever", "type": "Disease"}, {"text": "AHF", "type": "Disease"}]}

Example input:
Sentence: Administration of ribavirin resulted in a neutralization of viremia and a drop of endogenous interferon titers .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "viremia", "type": "Disease"}]}

Example input:
Sentence: BACKGROUND/AIMS : Recently ribavirin has been found to inhibit angiogenesis and a number of angiogenesis inhibitors such as sunitinib and sorafenib have been found to cause acute hemolysis .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "sunitinib", "type": "Chemical"}, {"text": "sorafenib", "type": "Chemical"}, {"text": "hemolysis", "type": "Disease"}]}

Example input:
Sentence: From these results , we conclude that ribavirin has an antiviral effect in advanced cases of AHF , and that anemia , the only secondary reaction observed , can be easily managed .

Example answer:
{"entities": [{"text": "ribavirin", "type": "Chemical"}, {"text": "AHF", "type": "Disease"}, {"text": "anemia", "type": "Disease"}]}

Input:
Sentence: RESULTS : Ribavirin-induced anemia occurred in 18 ( 20.5 % ) patients during treatment .

## Item bc5cdr:test:2478
Example input:
Sentence: It has been shown to be extremely effective in the treatment of peptic ulcer disease , reflux esophagitis , and the Zollinger-Ellison syndrome .

Example answer:
{"entities": [{"text": "peptic ulcer disease", "type": "Disease"}, {"text": "reflux esophagitis", "type": "Disease"}, {"text": "Zollinger-Ellison syndrome", "type": "Disease"}]}

Example input:
Sentence: The aim of this study was to examine further the renal function , including morphological analysis of the kidneys of male Sprague-Dawley rats treated with either cyclosporine A ( CsA ) , tacrolimus ( FK506 ) or SRL as monotherapies or in different combinations .

Example answer:
{"entities": [{"text": "cyclosporine A", "type": "Chemical"}, {"text": "CsA", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "FK506", "type": "Chemical"}, {"text": "SRL", "type": "Chemical"}]}

Example input:
Sentence: BACKGROUND : Sirolimus is the latest immunosuppressive agent used to prevent rejection , and may have less nephrotoxicity than calcineurin inhibitor ( CNI ) -based regimens .

Example answer:
{"entities": [{"text": "Sirolimus", "type": "Chemical"}, {"text": "nephrotoxicity", "type": "Disease"}]}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: The reduction of cyclosporine- or tacrolimus trough levels and the administration of calcium channel blockers led to relief of pain .

Example answer:
{"entities": [{"text": "cyclosporine-", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "pain", "type": "Disease"}]}

Example input:
Sentence: As a result , switching to tacrolimus has been reported to be a viable therapeutic option in the setting of cyclosporine-induced TMA .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: Tacrolimus , MMF , and steroids were given as immunosuppressant .

Example answer:
{"entities": [{"text": "Tacrolimus", "type": "Chemical"}, {"text": "MMF", "type": "Chemical"}, {"text": "steroids", "type": "Chemical"}]}

Example input:
Sentence: Introduction of tacrolimus as an alternative immunosuppressive agent resulted in the recurrence of TMA and the subsequent loss of the renal allograft .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: -Tacrolimus ( FK 506 ) is a powerful , widely used immunosuppressant .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}]}

Example input:
Sentence: The last decade has seen the emergence of tacrolimus as a potent immunosuppressive agent with mechanisms of action virtually identical to those of cyclosporine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "cyclosporine", "type": "Chemical"}]}

Input:
Sentence: BACKGROUND : Tacrolimus ointment is increasingly used for anti-inflammatory treatment of sensitive areas such as the face , and recent observations indicate that the treatment is effective in steroid-aggravated rosacea and perioral dermatitis .

## Item bc5cdr:test:2477
Example input:
Sentence: A 34-year-old lady developed a constellation of dermatitis , fever , lymphadenopathy and hepatitis , beginning on the 17th day of a course of oral sulphasalazine for sero-negative rheumatoid arthritis .

Example answer:
{"entities": [{"text": "dermatitis", "type": "Disease"}, {"text": "fever", "type": "Disease"}, {"text": "lymphadenopathy", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "sulphasalazine", "type": "Chemical"}, {"text": "rheumatoid arthritis", "type": "Disease"}]}

Example input:
Sentence: The Calcineurin-inhibitor Induced Pain Syndrome ( CIPS ) is a rare but severe side effect of cyclosporine or tacrolimus and is accurately diagnosed by its typical presentation , magnetic resonance imaging and bone scans .

Example answer:
{"entities": [{"text": "Pain", "type": "Disease"}, {"text": "CIPS", "type": "Disease"}, {"text": "cyclosporine", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: As a result , switching to tacrolimus has been reported to be a viable therapeutic option in the setting of cyclosporine-induced TMA .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "cyclosporine-induced", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: Two groups of patients receiving tacrolimus were compared over a period of 1 year , one group comprising hypertensive patients who were receiving nifedipine , and the other comprising nonhypertensive patients not receiving nifedipine .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "hypertensive", "type": "Disease"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: -Tacrolimus ( FK 506 ) is a powerful , widely used immunosuppressant .

Example answer:
{"entities": [{"text": "FK 506", "type": "Chemical"}]}

Example input:
Sentence: An allergic reaction consisting of angioneurotic edema secondary to continuous infusion 5-fluorouracil occurred in a patient with recurrent carcinoma of the oral cavity , cirrhosis , and cisplatin-induced impaired renal function .

Example answer:
{"entities": [{"text": "allergic reaction", "type": "Disease"}, {"text": "angioneurotic edema", "type": "Disease"}, {"text": "5-fluorouracil", "type": "Chemical"}, {"text": "carcinoma of the oral cavity", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}, {"text": "cisplatin-induced", "type": "Chemical"}, {"text": "impaired renal function", "type": "Disease"}]}

Example input:
Sentence: We conclude that noxious stimulation of facial mucosa increases intracranial blood flow and lacrimation via a trigemino-parasympathetic reflex .

Example answer:
{"entities": []}

Example input:
Sentence: Despite therapy with ursodeoxycholic acid , prednisone , and then tacrolimus , her cholestatic disease was unrelenting , with cirrhosis shown by biopsy 6 months after presentation .

Example answer:
{"entities": [{"text": "ursodeoxycholic acid", "type": "Chemical"}, {"text": "prednisone", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}, {"text": "cholestatic disease", "type": "Disease"}, {"text": "cirrhosis", "type": "Disease"}]}

Example input:
Sentence: Introduction of tacrolimus as an alternative immunosuppressive agent resulted in the recurrence of TMA and the subsequent loss of the renal allograft .

Example answer:
{"entities": [{"text": "tacrolimus", "type": "Chemical"}, {"text": "TMA", "type": "Disease"}]}

Example input:
Sentence: Recovery of tacrolimus-associated brachial neuritis after conversion to everolimus in a pediatric renal transplant recipient -- case report and review of the literature .

Example answer:
{"entities": [{"text": "tacrolimus-associated", "type": "Chemical"}, {"text": "brachial neuritis", "type": "Disease"}, {"text": "everolimus", "type": "Chemical"}]}

Input:
Sentence: Induction of rosaceiform dermatitis during treatment of facial inflammatory dermatoses with tacrolimus ointment .

## Item bc5cdr:test:2595
Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: OBJECTIVES : The United Kingdom Parkinson 's Disease Research Group ( UKPDRG ) trial found an increased mortality in patients with Parkinson 's disease ( PD ) randomized to receive 10 mg selegiline per day and L-dopa compared with those taking L-dopa alone .

Example answer:
{"entities": [{"text": "Parkinson 's Disease", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}, {"text": "selegiline", "type": "Chemical"}, {"text": "L-dopa", "type": "Chemical"}]}

Example input:
Sentence: There was a significant 40 % improvement in the dyskinesia score without increase of parkinsonian motor disability .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "parkinsonian", "type": "Disease"}, {"text": "motor disability", "type": "Disease"}]}

Example input:
Sentence: Importantly , a decrease in glutamate uptake correlates negatively with an increase in the incidence of orofacial diskinesia .

Example answer:
{"entities": [{"text": "glutamate", "type": "Chemical"}, {"text": "orofacial diskinesia", "type": "Disease"}]}

Example input:
Sentence: In the bolus group , 26.0 % ( 13/50 ) had akathisia compared with 32.7 % ( 16/49 ) in the infusion group ( Delta=-6.7 % ; 95 % confidence interval [ CI ] -24.6 % to 11.2 % ) .

Example answer:
{"entities": [{"text": "akathisia", "type": "Disease"}]}

Example input:
Sentence: Acute reserpine and subchronic haloperidol treatments change synaptosomal brain glutamate uptake and elicit orofacial dyskinesia in rats .

Example answer:
{"entities": [{"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}, {"text": "glutamate", "type": "Chemical"}, {"text": "orofacial dyskinesia", "type": "Disease"}]}

Example input:
Sentence: Levodopa-induced dyskinesias ( LIDs ) present a major problem for the long-term management of Parkinson 's disease ( PD ) patients .

Example answer:
{"entities": [{"text": "Levodopa-induced", "type": "Chemical"}, {"text": "dyskinesias", "type": "Disease"}, {"text": "LIDs", "type": "Disease"}, {"text": "Parkinson 's disease", "type": "Disease"}, {"text": "PD", "type": "Disease"}]}

Example input:
Sentence: In the present study , the authors induced orofacial dyskinesia by acute reserpine and subchronic haloperidol administration to rats .

Example answer:
{"entities": [{"text": "orofacial dyskinesia", "type": "Disease"}, {"text": "reserpine", "type": "Chemical"}, {"text": "haloperidol", "type": "Chemical"}]}

Example input:
Sentence: Ballistic and choreic dyskinesia were markedly ameliorated , whereas dystonia was not .

Example answer:
{"entities": [{"text": "dyskinesia", "type": "Disease"}, {"text": "dystonia", "type": "Disease"}]}

Example input:
Sentence: Reserpine- and haloperidol-induced orofacial dyskinesia are putative animal models of tardive dyskinesia ( TD ) whose pathophysiology has been related to free radical generation and oxidative stress .

Example answer:
{"entities": [{"text": "Reserpine-", "type": "Chemical"}, {"text": "haloperidol-induced", "type": "Chemical"}, {"text": "orofacial dyskinesia", "type": "Disease"}, {"text": "tardive dyskinesia", "type": "Disease"}, {"text": "TD", "type": "Disease"}]}

Input:
Sentence: Nondyskinetic patients , but not the dyskinetic ones , showed less oropharyngeal swallowing efficiency ( OPSE ) for liquid food than controls ( Dunnett , P = 0.02 ) .

## Item bc5cdr:test:2498
Example input:
Sentence: Significant disfiguring changes occur as a result of bone , cartilage , and soft tissue hypertrophy , including the thickening of the skin , coarsening of facial features , and cutis verticis gyrata .

Example answer:
{"entities": [{"text": "hypertrophy", "type": "Disease"}, {"text": "cutis verticis gyrata", "type": "Disease"}]}

Example input:
Sentence: Both , production of reactive oxygen species as well as activation of NF-kappaB have been implicated in severe neuronal damage in different sub-regions of the hippocampus as well as in the surrounding cortices .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: These data might indicate that the generation of reactive oxygen species and activation of NF-kappaB plays a more central role in seizure-associated neuronal damage in the temporal cortex as compared to the hippocampal hilus .

Example answer:
{"entities": [{"text": "oxygen", "type": "Chemical"}, {"text": "seizure-associated", "type": "Disease"}, {"text": "neuronal damage", "type": "Disease"}]}

Example input:
Sentence: Damage to the capillary was accompanied by marked damage to neuroglial cells , mainly to perivascular processes of astrocytes .

Example answer:
{"entities": []}

Example input:
Sentence: These data support the hypothesis that SE-induced mossy fiber sprouting and synaptic reorganization are relevant characteristics of seizure development in these murine strains , resembling rat models of human temporal lobe epilepsy .

Example answer:
{"entities": [{"text": "SE-induced", "type": "Disease"}, {"text": "seizure", "type": "Disease"}, {"text": "temporal lobe epilepsy", "type": "Disease"}]}

Example input:
Sentence: Our findings indicate that beta2-adrenoceptor overstimulation during an early critical period results in microglial activation associated with innate neuroinflammatory pathways and behavioral abnormalities , similar to those described in autism .

Example answer:
{"entities": [{"text": "behavioral abnormalities", "type": "Disease"}, {"text": "autism", "type": "Disease"}]}

Example input:
Sentence: RESULTS : Initial MRIs showed abnormal high signal intensities on DWI and FLAIR ( or T2-weighted image ) at the dentate nucleus ( 8/8 ) , inferior colliculus ( 6/8 ) , corpus callosum ( 2/8 ) , pons ( 2/8 ) , medulla ( 1/8 ) , and bilateral cerebral white matter ( 1/8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: Among the 5 patients with white matter abnormalities , 4 patients ( 80.0 % ) showed higher than normal ADC values on initial MR images , and all showed complete resolution on follow-up images .

Example answer:
{"entities": [{"text": "white matter abnormalities", "type": "Disease"}]}

Example input:
Sentence: These findings suggest that overgrowth of the exencephalic neural tissue causes the altered distribution patterns of vessels , subsequent peripheral circulatory failure and/or hemorrhaging in various parts of the exencephalic head , leading to the multiple modes of tissue reduction during transformation from exencephaly to anencephaly .

Example answer:
{"entities": [{"text": "exencephalic", "type": "Disease"}, {"text": "circulatory failure", "type": "Disease"}, {"text": "hemorrhaging", "type": "Disease"}, {"text": "exencephaly", "type": "Disease"}, {"text": "anencephaly", "type": "Disease"}]}

Example input:
Sentence: Acute white matter edema and eventual neuronal loss in the striatum adjacent to the hematoma did not differ between the two groups .

Example answer:
{"entities": [{"text": "white matter edema", "type": "Disease"}, {"text": "neuronal loss", "type": "Disease"}, {"text": "hematoma", "type": "Disease"}]}

Input:
Sentence: Prominent white-matter hypertrophy may result from altered myelination and adaptive glial changes , including gliosis secondary to neuronal damage .

## Item bc5cdr:test:2863
Example input:
Sentence: In unanesthetized , spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine , 5 to 20 micrograms/kg , was inhibited or reversed by nalozone , 0.2 to 2 mg/kg .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "clonidine", "type": "Chemical"}, {"text": "nalozone", "type": "Chemical"}]}

Example input:
Sentence: Controlled hypotension in groups A and C was induced with PGE1 to maintain mean arterial blood pressure at 55 mmHg for 180 min .

Example answer:
{"entities": [{"text": "hypotension", "type": "Disease"}, {"text": "PGE1", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Thoracic aorta of male Sprague-Dawley rats was exposed to 0.5M CaCl ( 2 ) or normal saline ( NaCl ) .

Example answer:
{"entities": [{"text": "CaCl ( 2 )", "type": "Chemical"}, {"text": "NaCl", "type": "Chemical"}]}

Example input:
Sentence: These rats also showed declines in left ventricular systolic pressure , maximum and minimum rate of developed left ventricular pressure , and elevation of left ventricular end-diastolic pressure and ST-segment .

Example answer:
{"entities": []}

Example input:
Sentence: Mean arterial pressure was decreased to 50 mm Hg for 30 minutes either by hemorrhage ( HEM , n = 7 ) or by continuous infusion of sodium nitroprusside ( SNP , n = 7 ) .

Example answer:
{"entities": [{"text": "hemorrhage", "type": "Disease"}, {"text": "HEM", "type": "Disease"}, {"text": "sodium nitroprusside", "type": "Chemical"}, {"text": "SNP", "type": "Chemical"}]}

Example input:
Sentence: Sham-operated rats served as normotensive controls ( 128 +/- 3 mm Hg , n = 8 ) .

Example answer:
{"entities": []}

Example input:
Sentence: In the five rats that developed somatic rigidity , ICP and CVP increased significantly above baseline ( delta ICP 7.5 +/- 1.0 mmHg , delta CVP 5.9 +/- 1.3 mmHg ) .

Example answer:
{"entities": [{"text": "somatic rigidity", "type": "Disease"}]}

Example input:
Sentence: Six weeks after clipping of one renal artery , hypertensive rats ( 178 +/- 4 mm Hg ) were randomly assigned to three groups : untreated hypertensive controls ( n = 8 ) , enalapril-treated ( n = 8 ) , or nitrendipine-treated ( n = 10 ) .

Example answer:
{"entities": [{"text": "hypertensive", "type": "Disease"}, {"text": "enalapril-treated", "type": "Chemical"}, {"text": "nitrendipine-treated", "type": "Chemical"}]}

Example input:
Sentence: In sham-operated rats , rilmenidine or alpha-methyldopa elicited similar hypotension that lasted at least 5 h and was associated with reductions in standard deviation of mean arterial pressure .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}]}

Example input:
Sentence: Mean arterial pressure ( as a percentage of control +/- SEM ) during randomized infusions of 0.03 , 0.1 , 0.3 , or 1.0 microgram/kg/min was 99 +/- 1 , 95 +/- 1 ( p less than 0.05 ) , 93 +/- 1 ( p less than 0.01 ) , or 79 +/- 6 % ( p less than 0.001 ) , respectively , but no tachycardia and no augmentation of the norepinephrine release rate ( up to 0.3 microgram/kg/min ) were observed , which is in contrast to comparable hypotension induced by hydralazine or nitroglycerin .

Example answer:
{"entities": [{"text": "tachycardia", "type": "Disease"}, {"text": "norepinephrine", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "hydralazine", "type": "Chemical"}, {"text": "nitroglycerin", "type": "Chemical"}]}

Input:
Sentence: Mean arterial pressure of conscious rats was 119 +/- 2 mm Hg in control and 194 +/- 5 mm Hg in LNNA rats ( P < 0.05 ) .

## Item bc5cdr:test:2527
Example input:
Sentence: Effects of long-term pretreatment with isoproterenol on bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: This study was conducted to examine whether prolonged pretreatment with isoproterenol could abolish bromocriptine-induced tachycardia in conscious rats .

Example answer:
{"entities": [{"text": "isoproterenol", "type": "Chemical"}, {"text": "bromocriptine-induced", "type": "Chemical"}, {"text": "tachycardia", "type": "Disease"}]}

Example input:
Sentence: Adult male albino rats , treated with ISO ( 200 mg/kg , s.c. ) for 2 days at an interval of 24 h caused a significant ( P < 0.05 ) elevation of heart weight , serum marker enzymes , lipid peroxidation and Ca+2 ATPase level whereas there was a significant ( P < 0.05 ) decrease in body weight , endogenous antioxidants , Na+/ K+ ATPase and Mg+2 ATPase levels .

Example answer:
{"entities": [{"text": "ISO", "type": "Chemical"}, {"text": "Ca+2", "type": "Chemical"}, {"text": "Na+/", "type": "Chemical"}, {"text": "K+", "type": "Chemical"}, {"text": "Mg+2", "type": "Chemical"}]}

Example input:
Sentence: TCR prevented the isoproterenol-induced decrease in antioxidant enzymes in the heart and increased the rate of ADP-stimulated oxygen uptake and respiratory coupling ratio .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "ADP-stimulated", "type": "Chemical"}, {"text": "oxygen", "type": "Chemical"}]}

Example input:
Sentence: Pretreatment of TCR , at a dose of 0.5 mL/100 g bodyweight per day , orally for 30 days , prevented the increase in lipid peroxidation and activity of marker enzymes observed in isoproterenol-induced rats ( 85 mg kg ( -1 ) s. c. for 2 days at an interval of 24 h ) .

Example answer:
{"entities": [{"text": "TCR", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: The effects of exercise on the severity of isoproterenol-induced myocardial infarction were studied in female albino rats of 20,40,60 and 80 weeks of age .

Example answer:
{"entities": [{"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: In addition , mitochondrial respiratory dysfunction characterized by decreased respiratory control ratio and ADP/O was observed in isoproterenol-treated rats .

Example answer:
{"entities": [{"text": "respiratory dysfunction", "type": "Disease"}, {"text": "ADP/O", "type": "Chemical"}, {"text": "isoproterenol-treated", "type": "Chemical"}]}

Example input:
Sentence: Histological studies demonstrated that the rats developed an infarct 18 h after isoproterenol administration .

Example answer:
{"entities": [{"text": "infarct", "type": "Disease"}, {"text": "isoproterenol", "type": "Chemical"}]}

Example input:
Sentence: In isolated perfused heart preparations from isoproterenol-pretreated rats , the isoproterenol-induced maximal increase in left ventricular systolic pressure was significantly reduced , compared with saline-pretreated rats ( the EC50 of the isoproterenol-induced increase in left ventricular systolic pressure was enhanced approximately 22-fold ) .

Example answer:
{"entities": [{"text": "isoproterenol-pretreated", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}]}

Example input:
Sentence: Isoproterenol-treated rats showed significant increases in the levels of lactate dehydrogenase , aspartate transaminase , creatine kinase and malondialdehyde and significant decreases in the activities of superoxide dismutase , catalase and glutathione peroxidase in serum and heart .

Example answer:
{"entities": [{"text": "Isoproterenol-treated", "type": "Chemical"}, {"text": "lactate", "type": "Chemical"}, {"text": "aspartate", "type": "Chemical"}, {"text": "creatine", "type": "Chemical"}, {"text": "malondialdehyde", "type": "Chemical"}, {"text": "superoxide", "type": "Chemical"}, {"text": "glutathione", "type": "Chemical"}]}

Input:
Sentence: In isoproterenol administered rats , the level of lipid peroxides increased significantly in the serum and heart .

## Item bc5cdr:test:2305
Example input:
Sentence: Nicotine-induced hyperactivity was blocked by the selective D1 antagonist SCH 23390 , the selective D2 antagonist raclopride and the D1/D2 antagonist fluphenazine .

Example answer:
{"entities": [{"text": "Nicotine-induced", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "SCH 23390", "type": "Chemical"}, {"text": "raclopride", "type": "Chemical"}, {"text": "fluphenazine", "type": "Chemical"}]}

Example input:
Sentence: The rats received AChE reactivator pralidoxime-2-chloride ( 2PAM ) ( 30.0 mg/kg BW ) , anticonvulsant diazepam ( 2.0 mg/kg BW ) , A ( 1 ) -adenosine receptor agonist N ( 6 ) -cyclopentyl adenosine ( CPA ) ( 2.0 mg/kg BW ) , NMDA-receptor antagonist dizocilpine maleate ( +-MK801 hydrogen maleate ) ( 2.0 mg/kg BW ) or their combinations with cholinolytic drug atropine sulfate ( 50.0 mg/kg BW ) immediately or 30 min after the single SC injection of DFP .

Example answer:
{"entities": [{"text": "pralidoxime-2-chloride", "type": "Chemical"}, {"text": "2PAM", "type": "Chemical"}, {"text": "diazepam", "type": "Chemical"}, {"text": "N ( 6 ) -cyclopentyl adenosine", "type": "Chemical"}, {"text": "CPA", "type": "Chemical"}, {"text": "NMDA-receptor", "type": "Chemical"}, {"text": "dizocilpine maleate", "type": "Chemical"}, {"text": "atropine sulfate", "type": "Chemical"}, {"text": "DFP", "type": "Chemical"}]}

Example input:
Sentence: When injected into the accumbens shell ( but not the core ) before cocaine , CP 93129 ( 0.1-10 microg/side ) enhanced the locomotor response to cocaine ; the maximum effect being observed after 10 microg/side of the agonist .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}, {"text": "CP 93129", "type": "Chemical"}]}

Example input:
Sentence: The enhanced alpha-methyldopa hypotension in Ovx rats was paralleled with further reduction in SDRR and a reduced locomotor activity .

Example answer:
{"entities": [{"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "hypotension", "type": "Disease"}, {"text": "a reduced locomotor activity", "type": "Disease"}]}

Example input:
Sentence: The present study was designed to examine the effect of 5-HT1B receptor ligands microinjected into the subregions of the nucleus accumbens ( the shell and the core ) on the locomotor hyperactivity induced by cocaine in rats .

Example answer:
{"entities": [{"text": "locomotor hyperactivity", "type": "Disease"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: TRI given repeatedly to rats increases the locomotor hyperactivity induced by d-amphetamine , quinpirole and ( + ) -7-hydroxy-dipropyloaminotetralin ( dopamine D2 and D3 effects ) .

Example answer:
{"entities": [{"text": "TRI", "type": "Chemical"}, {"text": "hyperactivity", "type": "Disease"}, {"text": "d-amphetamine", "type": "Chemical"}, {"text": "quinpirole", "type": "Chemical"}, {"text": "dopamine", "type": "Chemical"}]}

Example input:
Sentence: Systemic cocaine ( 10 mg/kg ) significantly increased the locomotor activity of rats .

Example answer:
{"entities": [{"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: GR 55562 ( 0.1-10 microg/side ) , administered intra-accumbens shell prior to cocaine , dose-dependently attenuated the psychostimulant-induced locomotor hyperactivity .

Example answer:
{"entities": [{"text": "GR 55562", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}, {"text": "locomotor hyperactivity", "type": "Disease"}]}

Example input:
Sentence: At doses where alone , they produced no significant effects on locomotion , BD1018 , BD1063 and LR132 significantly attenuated the locomotor stimulatory effects of cocaine .

Example answer:
{"entities": [{"text": "BD1018", "type": "Chemical"}, {"text": "BD1063", "type": "Chemical"}, {"text": "LR132", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: In experiments using specific adrenergic antagonists , we found that pretreatment with the beta-adrenergic receptor antagonist propranolol blocked cocaine-induced anxiety-like behavior in Dbh +/- and wild-type C57BL6/J mice , while the alpha ( 1 ) antagonist prazosin and the alpha ( 2 ) antagonist yohimbine had no effect .

Example answer:
{"entities": [{"text": "propranolol", "type": "Chemical"}, {"text": "cocaine-induced", "type": "Chemical"}, {"text": "anxiety-like", "type": "Disease"}, {"text": "prazosin", "type": "Chemical"}, {"text": "yohimbine", "type": "Chemical"}]}

Input:
Sentence: The selective blockade of A2 adenosine receptor by DMPX ( 3,7-dimethyl-1-propargylxanthine ) significantly enhanced cocaine-induced locomotor activity of animals .

## Item bc5cdr:test:2355
Example input:
Sentence: A low incidence of cardiovascular malformations was observed after exposure to each of the four calcium channel blockers , but this incidence was statistically significant only for verapamil and nifedipine .

Example answer:
{"entities": [{"text": "cardiovascular malformations", "type": "Disease"}, {"text": "calcium", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}]}

Example input:
Sentence: The influence of sevoflurane on lidocaine-induced convulsions was studied in cats .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "Chemical"}, {"text": "lidocaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}]}

Example input:
Sentence: Patients given prilocaine were more likely to develop hearing loss ( 10 out of 22 ) than those given bupivacaine ( 4 out of 22 ) ( P < 0.05 ) .

Example answer:
{"entities": [{"text": "prilocaine", "type": "Chemical"}, {"text": "hearing loss", "type": "Disease"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Studies in DBA/2J mice showed that : 1 ) pretreatment with acetaminophen ( 100 mg/kg ) increased the interval between the administration of caffeine ( 300 to 450 mg/kg IP ) and the onset of fatal convulsions by a factor of about two ; and 2 ) pretreatment with acetaminophen ( 75 mg/kg ) reduced the incidence of audiogenic seizures produced in the presence of caffeine ( 12.5 to 75 mg/kg IP ) .

Example answer:
{"entities": [{"text": "acetaminophen", "type": "Chemical"}, {"text": "caffeine", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "seizures", "type": "Disease"}]}

Example input:
Sentence: The patient had no apparent associated conditions which might have predisposed him to the development of bradyarrhythmias ; and , thus , this probably represented a true idiosyncrasy to lidocaine .

Example answer:
{"entities": [{"text": "bradyarrhythmias", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}]}

Example input:
Sentence: The purpose of this study was to investigate the influence of calcium channel blockers on bupivacaine-induced acute toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: Effects of calcium channel blockers on bupivacaine-induced toxicity .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}]}

Example input:
Sentence: It is suggested that sevoflurane reduces the convulsive effect of lidocaine toxicity but carries some risk due to circulatory depression .

Example answer:
{"entities": [{"text": "sevoflurane", "type": "Chemical"}, {"text": "convulsive", "type": "Disease"}, {"text": "lidocaine", "type": "Chemical"}, {"text": "toxicity", "type": "Disease"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: The convulsant activity of bupivacaine was not significantly modified but calcium channel blockers decreased the time of latency to obtain bupivacaine-induced convulsions ; this effect was less pronounced with bepridil .

Example answer:
{"entities": [{"text": "bupivacaine", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "bupivacaine-induced", "type": "Chemical"}, {"text": "convulsions", "type": "Disease"}, {"text": "bepridil", "type": "Chemical"}]}

Input:
Sentence: CONCLUSIONS : Although levobupivacaine may have a safer cardiac toxicity profile than racemic bupivacaine , if adequate amounts of levobupivacaine reach the circulation , it will result in convulsions .

## Item bc5cdr:test:2358
Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: Thirty days after amiodarone discontinuation , His bundle electrograms showed atrial flutter without intra-Hisian or infra-Hisian delay .

Example answer:
{"entities": [{"text": "amiodarone", "type": "Chemical"}, {"text": "atrial flutter", "type": "Disease"}]}

Example input:
Sentence: Simvastatin , amiodarone , and the patient 's human immunodeficiency virus medications were all temporarily discontinued and the patient was given forced alkaline diuresis and started on dialysis .

Example answer:
{"entities": [{"text": "Simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "human immunodeficiency virus", "type": "Disease"}]}

Example input:
Sentence: A case is presented of a reversible intra-Hisian block occurring under amiodarone treatment for atrial tachycardia in a patient without clear intraventricular conduction abnormalities .

Example answer:
{"entities": [{"text": "intra-Hisian block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atrial tachycardia", "type": "Disease"}, {"text": "intraventricular conduction abnormalities", "type": "Disease"}]}

Example input:
Sentence: The patient was taking 80 mg simvastatin at bedtime ( initiated 27 days earlier ) ; amiodarone at a dose of 400 mg daily for 7 days , then 200 mg daily ( initiated 19 days earlier ) ; and 400 mg atazanavir daily ( initiated at least 2 years previously ) .

Example answer:
{"entities": [{"text": "simvastatin", "type": "Chemical"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "atazanavir", "type": "Chemical"}]}

Example input:
Sentence: We report a woman with coronary artery disease who developed a markedly prolonged QT interval and torsades de pointes ( TdP ) after taking ketoconazole for treatment of fungal infection .

Example answer:
{"entities": [{"text": "coronary artery disease", "type": "Disease"}, {"text": "prolonged QT interval", "type": "Disease"}, {"text": "torsades de pointes", "type": "Disease"}, {"text": "TdP", "type": "Disease"}, {"text": "ketoconazole", "type": "Chemical"}, {"text": "fungal infection", "type": "Disease"}]}

Example input:
Sentence: A patient with sinuatrial disease and implanted pacemaker was treated with amiodarone ( maximum dose 1000 mg , maintenance dose 800 mg daily ) for 10 months , for control of supraventricular tachyarrhythmias .

Example answer:
{"entities": [{"text": "sinuatrial disease", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "supraventricular tachyarrhythmias", "type": "Disease"}]}

Example input:
Sentence: Amiodarone should be used with caution during long-term oral therapy in patients with or without clear intraventricular conduction defects .

Example answer:
{"entities": [{"text": "Amiodarone", "type": "Chemical"}]}

Example input:
Sentence: Torsades de pointes ( TDP ) is a potentially fatal ventricular tachycardia associated with increases in QT interval and monophasic action potential duration ( MAPD ) .

Example answer:
{"entities": [{"text": "Torsades de pointes", "type": "Disease"}, {"text": "TDP", "type": "Disease"}, {"text": "ventricular tachycardia", "type": "Disease"}]}

Example input:
Sentence: We observed sinoatrial block due to chronic amiodarone administration in a 5-year-old boy with primary cardiomyopathy , Wolff-Parkinson-White syndrome and supraventricular tachycardia .

Example answer:
{"entities": [{"text": "sinoatrial block", "type": "Disease"}, {"text": "amiodarone", "type": "Chemical"}, {"text": "primary cardiomyopathy", "type": "Disease"}, {"text": "Wolff-Parkinson-White syndrome", "type": "Disease"}, {"text": "supraventricular tachycardia", "type": "Disease"}]}

Input:
Sentence: The authors present a case of early ( within 4 days ) development of torsade de pointes ( TdP ) associated with oral amiodarone therapy .

## Item bc5cdr:test:2463
Example input:
Sentence: We describe 3 episodes of microangiopathic hemolytic anemia ( MAHA ) in 2 solid organ recipients under FK506 ( tacrolimus ) therapy .

Example answer:
{"entities": [{"text": "microangiopathic hemolytic anemia", "type": "Disease"}, {"text": "MAHA", "type": "Disease"}, {"text": "FK506", "type": "Chemical"}, {"text": "tacrolimus", "type": "Chemical"}]}

Example input:
Sentence: Whereas patient 1 showed lesions of up to 1 cm readily detectable on magnetic resonance imaging under prolonged co-trimoxazole treatment , therapy of patient 2 was switched early .

Example answer:
{"entities": [{"text": "co-trimoxazole", "type": "Chemical"}]}

Example input:
Sentence: Here , we report two cases of severely immunocompromised HIV-infected patients who developed severe intrahepatic cholestasis , and in one patient lesions mimicking liver abscess formation on radiologic exams , during co-trimoxazole treatment for PCP .

Example answer:
{"entities": [{"text": "HIV-infected", "type": "Disease"}, {"text": "intrahepatic cholestasis", "type": "Disease"}, {"text": "liver abscess", "type": "Disease"}, {"text": "co-trimoxazole", "type": "Chemical"}, {"text": "PCP", "type": "Disease"}]}

Example input:
Sentence: This paper describes the clinical features of six children who developed the haemolytic-uraemic syndrome after treatment with metronidazole .

Example answer:
{"entities": [{"text": "haemolytic-uraemic syndrome", "type": "Disease"}, {"text": "metronidazole", "type": "Chemical"}]}

Example input:
Sentence: Sulfonamides were associated with anencephaly ( adjusted OR [ AOR ] = 3.4 ; 95 % confidence interval [ CI ] , 1.3-8.8 ) , hypoplastic left heart syndrome ( AOR = 3.2 ; 95 % CI , 1.3-7.6 ) , coarctation of the aorta ( AOR = 2.7 ; 95 % CI , 1.3-5.6 ) , choanal atresia ( AOR = 8.0 ; 95 % CI , 2.7-23.5 ) , transverse limb deficiency ( AOR = 2.5 ; 95 % CI , 1.0-5.9 ) , and diaphragmatic hernia ( AOR = 2.4 ; 95 % CI , 1.1-5.4 ) .

Example answer:
{"entities": [{"text": "Sulfonamides", "type": "Chemical"}, {"text": "anencephaly", "type": "Disease"}, {"text": "hypoplastic left heart syndrome", "type": "Disease"}, {"text": "coarctation of the aorta", "type": "Disease"}, {"text": "choanal atresia", "type": "Disease"}, {"text": "transverse limb deficiency", "type": "Disease"}, {"text": "diaphragmatic hernia", "type": "Disease"}]}

Example input:
Sentence: Abnormal involuntary movements appeared in the mouth , tongue , neck and abdomen of a 64-year-old male patient after he took metoclopramide for gastrointestinal disorder in a regimen of 30 mg per day for a total of about 260 days .

Example answer:
{"entities": [{"text": "Abnormal involuntary movements", "type": "Disease"}, {"text": "metoclopramide", "type": "Chemical"}, {"text": "gastrointestinal disorder", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: We report the first case of a serious short-term adverse reaction with the use of omeprazole : hemolytic anemia .

Example answer:
{"entities": [{"text": "omeprazole", "type": "Chemical"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Example input:
Sentence: The present report describes a case of cardiac arrest and subsequent death as a result of hyperkalaemia following the use of suxamethonium in a 23-year-old Malawian woman .

Example answer:
{"entities": [{"text": "cardiac arrest", "type": "Disease"}, {"text": "death", "type": "Disease"}, {"text": "hyperkalaemia", "type": "Disease"}, {"text": "suxamethonium", "type": "Chemical"}]}

Example input:
Sentence: The mechanism by which omeprazole caused the patient 's hemolytic anemia is uncertain , but physicians should be alerted to this possible adverse effect .

Example answer:
{"entities": [{"text": "omeprazole", "type": "Chemical"}, {"text": "hemolytic anemia", "type": "Disease"}]}

Input:
Sentence: We present magnetic resonance imaging findings of a 5-year-old girl who had a rapidly installing hemolytic anemia crisis induced by trimethoprim-sulfomethoxazole , resulting in cerebral anoxia leading to permanent damage .

## Item bc5cdr:test:2533
Example input:
Sentence: Changes evoked by a single intraperitoneal injection of rilmenidine ( 600 microg/kg ) or alpha-methyldopa ( 100 mg/kg ) , selective I1- and alpha2-receptor agonists , respectively , in blood pressure , hemodynamic variability , and locomotor activity were assessed in radiotelemetered sham-operated and ovariectomized ( Ovx ) Sprague-Dawley female rats with or without 12-wk estrogen replacement .

Example answer:
{"entities": [{"text": "rilmenidine", "type": "Chemical"}, {"text": "alpha-methyldopa", "type": "Chemical"}, {"text": "estrogen", "type": "Chemical"}]}

Example input:
Sentence: During an 18-month period of study 41 hemodialyzed patients receiving desferrioxamine ( 10-40 mg/kg BW/3 times weekly ) for the first time were monitored for detection of audiovisual toxicity .

Example answer:
{"entities": [{"text": "desferrioxamine", "type": "Chemical"}, {"text": "audiovisual toxicity", "type": "Disease"}]}

Example input:
Sentence: This is a case report of euphoria and choreoathetoid movements both transiently induced by rapid adjustment to the selective mu-opioid receptor agonist methadone in an inpatient previously abusing heroine and cocaine .

Example answer:
{"entities": [{"text": "choreoathetoid movements", "type": "Disease"}, {"text": "methadone", "type": "Chemical"}, {"text": "heroine", "type": "Chemical"}, {"text": "cocaine", "type": "Chemical"}]}

Example input:
Sentence: METHODS : Following induction of anesthesia by fentanyl ( 0.15 mg kg ( -1 ) ) and propofol ( 2.0 mg kg ( -1 ) ) , 13 patients received phenylephrine ( 0.1 mg iv ) and 12 patients received ephedrine ( 10 mg iv ) to restore mean arterial pressure ( MAP ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "propofol", "type": "Chemical"}, {"text": "phenylephrine", "type": "Chemical"}, {"text": "ephedrine", "type": "Chemical"}]}

Example input:
Sentence: Combining the two fentanyl groups revealed further significant benefits from the avoidance of opioids , reducing postoperative nausea and vomiting and nausea prior to discharge from 35 % and 33 % to 22 % and 19 % ( P = 0.049 and P = 0.035 ) , respectively , while nausea in the first 24 h was decreased from 42 % to 27 % ( P = 0.034 ) .

Example answer:
{"entities": [{"text": "fentanyl", "type": "Chemical"}, {"text": "postoperative nausea and vomiting", "type": "Disease"}, {"text": "nausea", "type": "Disease"}]}

Example input:
Sentence: infusion of morphine ( mean 73.6 mg ) and five patients receiving a continuous extradural infusion of 0.25 % bupivacaine ( mean 192 mg ) in the 24-h period following upper abdominal surgery .

Example answer:
{"entities": [{"text": "morphine", "type": "Chemical"}, {"text": "bupivacaine", "type": "Chemical"}]}

Example input:
Sentence: An increase in blood pressure , accompanied by atrial fibrillation , agitation , incomprehensible shouts and loss of consciousness , was observed in an elderly , ASA classification group II , cardiovascularly medicated male , 12 min after performance of axillary block with mepivacaine 850 mg containing adrenaline 0.225 mg , for correction of Dupuytren 's contracture .

Example answer:
{"entities": [{"text": "increase in blood pressure", "type": "Disease"}, {"text": "atrial fibrillation", "type": "Disease"}, {"text": "agitation", "type": "Disease"}, {"text": "incomprehensible shouts", "type": "Disease"}, {"text": "loss of consciousness", "type": "Disease"}, {"text": "mepivacaine", "type": "Chemical"}, {"text": "adrenaline", "type": "Chemical"}, {"text": "Dupuytren 's contracture", "type": "Disease"}]}

Example input:
Sentence: Intravenous administration of a single 50-mg bolus of lidocaine in a 67-year-old man resulted in profound depression of the activity of the sinoatrial and atrioventricular nodal pacemakers .

Example answer:
{"entities": [{"text": "lidocaine", "type": "Chemical"}, {"text": "depression", "type": "Disease"}]}

Example input:
Sentence: A 35-year-old woman whose cervix uteri was inadvertently injected with 8 mg of epinephrine developed myocardial stunning that was characterized by severe hemodynamic compromise , profound , albeit transient , left ventricular systolic and diastolic dysfunction , and only modestly elevated biochemical markers of myocardial necrosis .

Example answer:
{"entities": [{"text": "epinephrine", "type": "Chemical"}, {"text": "myocardial stunning", "type": "Disease"}, {"text": "left ventricular systolic and diastolic dysfunction", "type": "Disease"}, {"text": "myocardial necrosis", "type": "Disease"}]}

Example input:
Sentence: We report a case of a 31 year old female who required admission to the Intensive Care Unit for ventilation and full supportive therapy , following ingestion of 13.5g bupropion .

Example answer:
{"entities": [{"text": "bupropion", "type": "Chemical"}]}

Input:
Sentence: Postoperatively , she was given a patient-controlled analgesia device delivering boluses of diamorphine 0.5 mg and droperidol 0.025 mg. Whilst using the device she gradually became anxious , the feeling worsening after each bolus .

## Item bc5cdr:test:2878
Example input:
Sentence: SAR studies led to compound 14 with excellent potency ( K ( i ) = 0.4 nM ) , selectivity ( A ( 1 ) /A ( 2A ) > 100 ) , and efficacy ( MED 10 mg/kg p.o . )

Example answer:
{"entities": []}

Example input:
Sentence: To this end , doxorubicin ( 15 mug/g body wt ) was injected intravenously into gene-targeted mice lacking SGK1 ( sgk1 ( -/- ) ) and their wild-type littermates ( sgk1 ( +/+ ) ) .

Example answer:
{"entities": [{"text": "doxorubicin", "type": "Chemical"}]}

Example input:
Sentence: Plasma TAFI , tPA , and PAI-1 antigen levels were measured at baseline and after 3 months of treatment by commercially available ELISA kits .

Example answer:
{"entities": []}

Example input:
Sentence: Chromosome substitution strains ( CSS ) , in which a single chromosome from one inbred strain ( donor ) has been transferred onto a second strain ( host ) by repeated backcrossing , may be used to identify quantitative trait loci ( QTLs ) that contribute to seizure susceptibility .

Example answer:
{"entities": [{"text": "seizure", "type": "Disease"}]}

Example input:
Sentence: RESULTS : We found PTCR in 14 of 15 cases of TG , in 7 transplant biopsy specimens without TG , and in 13 of 143 native kidney biopsy specimens .

Example answer:
{"entities": [{"text": "TG", "type": "Disease"}]}

Example input:
Sentence: We therefore systematically analyzed the functional impact of the most prevalent immune escape variants , the sG145R and sP120T mutants , on the viral replication efficacy and antiviral drug susceptibility of common treatment-associated mutants with resistance to lamivudine ( LAM ) and/or HBeAg negativity .

Example answer:
{"entities": [{"text": "lamivudine", "type": "Chemical"}, {"text": "LAM", "type": "Chemical"}, {"text": "HBeAg", "type": "Chemical"}]}

Example input:
Sentence: The sG145R mutation strongly reduced HBsAg levels and was able to fully restore the impaired replication of LAM-resistant HBV mutants to the levels of wild-type HBV , and PC or BCP mutations further enhanced viral replication .

Example answer:
{"entities": [{"text": "HBsAg", "type": "Chemical"}, {"text": "LAM-resistant", "type": "Chemical"}]}

Example input:
Sentence: RESULTS : in 11 patients , mutations were found in the BCHE gene , the K-variant being the most frequent .

Example answer:
{"entities": []}

Example input:
Sentence: An analysis for factor V Leiden and the G20210A mutation in the prothrombin gene was conducted in 217 patients and 763 controls RESULTS : The odds ratio for myocardial infarction among women who used any type of combined oral contraceptive , as compared with nonusers , was 2.0 ( 95 percent confidence interval , 1.5 to 2.8 ) .

Example answer:
{"entities": [{"text": "myocardial infarction", "type": "Disease"}, {"text": "oral contraceptive", "type": "Chemical"}]}

Example input:
Sentence: Therefore , patients belonging to the poor-metabolizer phenotype of sparteine/debrisoquine polymorphism in drug metabolism , which constitutes 6.4 % of the German population , may experience adverse drug reactions when treated with standard doses of one of these drugs alone .

Example answer:
{"entities": [{"text": "sparteine/debrisoquine", "type": "Chemical"}, {"text": "adverse drug reactions", "type": "Disease"}]}

Input:
Sentence: RESULTS : Polymorphisms TaqID , Ser311Cys and rs6277 were not polymorphic in the population recruited in the present study .

## Item bc5cdr:test:2748
Example input:
Sentence: Twelve patients with liver disease related to methyldopa were seen between 1967 and 1977 .

Example answer:
{"entities": [{"text": "liver disease", "type": "Disease"}, {"text": "methyldopa", "type": "Chemical"}]}

Example input:
Sentence: Simvastatinezetimibe and escitalopram ( which she was taking for depression ) were discontinued , and other potential causes of hepatotoxicity were excluded .

Example answer:
{"entities": [{"text": "Simvastatinezetimibe", "type": "Chemical"}, {"text": "escitalopram", "type": "Chemical"}, {"text": "depression", "type": "Disease"}, {"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: We report the case of a patient who developed acute hepatitis with extensive hepatocellular necrosis , 7 months after the onset of administration of clotiazepam , a thienodiazepine derivative .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}, {"text": "extensive hepatocellular necrosis", "type": "Disease"}, {"text": "clotiazepam", "type": "Chemical"}, {"text": "thienodiazepine", "type": "Chemical"}]}

Example input:
Sentence: With widespread use of antimicrobial agents , however , hepatic injury occurs frequently , and among adverse drug reactions , idiosyncratic reactions are the most serious .

Example answer:
{"entities": [{"text": "hepatic injury", "type": "Disease"}, {"text": "adverse drug reactions", "type": "Disease"}]}

Example input:
Sentence: Although generally well-tolerated , asymptomatic abnormalities of liver function have been recorded and , less commonly , severe hepatitis induced by diclofenac .

Example answer:
{"entities": [{"text": "abnormalities of liver function", "type": "Disease"}, {"text": "hepatitis", "type": "Disease"}, {"text": "diclofenac", "type": "Chemical"}]}

Example input:
Sentence: The remaining patient in the series developed fulminant hepatitis when the drug was accidentally recommenced 1 year after a prior episode of methyldopa-induced hepatitis .

Example answer:
{"entities": [{"text": "fulminant hepatitis", "type": "Disease"}, {"text": "methyldopa-induced", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: Drug-induced hepatotoxicity , although common , has been reported only infrequently with sulfonylureas .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}, {"text": "sulfonylureas", "type": "Chemical"}]}

Example input:
Sentence: Based on a score of 8 on the Naranjo adverse drug reaction probability scale , telithromycin was the probable cause of acute hepatitis in this patient , and pathological findings suggested drug-induced toxic hepatitis .

Example answer:
{"entities": [{"text": "adverse drug reaction", "type": "Disease"}, {"text": "telithromycin", "type": "Chemical"}, {"text": "hepatitis", "type": "Disease"}, {"text": "toxic hepatitis", "type": "Disease"}]}

Example input:
Sentence: By November 1984 the Committee on Safety of Medicines had received 82 reports of possible hepatotoxicity associated with the drug , including five deaths .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}, {"text": "deaths", "type": "Disease"}]}

Input:
Sentence: Drug-induced liver injury : an analysis of 461 incidences submitted to the Spanish registry over a 10-year period .

## Item bc5cdr:test:2699
Example input:
Sentence: Because Warfarin treatment had no effect on the elevation in serum calcium produced by vitamin D , the synergy between Warfarin and vitamin D is probably best explained by the hypothesis that Warfarin inhibits the activity of matrix Gla protein as a calcification inhibitor .

Example answer:
{"entities": [{"text": "Warfarin", "type": "Chemical"}, {"text": "calcium", "type": "Chemical"}, {"text": "vitamin D", "type": "Chemical"}, {"text": "calcification", "type": "Disease"}]}

Example input:
Sentence: Myocardial calcium concentrations also were decreased ( 11.2 , 8.3 , and 8.9 mg. per 100 Gm .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}]}

Example input:
Sentence: A new infarct-avid radiopharmaceutical based on glucaric acid was prepared in the hospital radiopharmacy of the INCMNSZ .

Example answer:
{"entities": [{"text": "infarct-avid", "type": "Disease"}, {"text": "glucaric acid", "type": "Chemical"}]}

Example input:
Sentence: 99mTc-glucarate for detection of isoproterenol-induced myocardial infarction in rats .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Calcium concentrations 1 day postpartum were higher in cows treated with vitamin D3 about 32 days prepartum ( 8.8 mg/100 ml ) than in control cows ( 5.5 mg/100 ml ) .

Example answer:
{"entities": [{"text": "Calcium", "type": "Chemical"}, {"text": "vitamin D3", "type": "Chemical"}]}

Example input:
Sentence: We studied three calcium channel blockers of different structure , nifedipine , diltiazem , and verapamil , along with the new agent .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "nifedipine", "type": "Chemical"}, {"text": "diltiazem", "type": "Chemical"}, {"text": "verapamil", "type": "Chemical"}]}

Example input:
Sentence: 99mTc-glucarate was easy to prepare , stable for 96 h and was used to study its biodistribution in rats with isoproterenol-induced acute myocardial infarction .

Example answer:
{"entities": [{"text": "99mTc-glucarate", "type": "Chemical"}, {"text": "isoproterenol-induced", "type": "Chemical"}, {"text": "myocardial infarction", "type": "Disease"}]}

Example input:
Sentence: Based on clinical data , indicating that chloroacetaldehyde ( CAA ) is an important metabolite of oxazaphosphorine cytostatics , an experimental study was carried out in order to elucidate the role of CAA in the development of hemorrhagic cystitis .

Example answer:
{"entities": [{"text": "chloroacetaldehyde", "type": "Chemical"}, {"text": "CAA", "type": "Chemical"}]}

Example input:
Sentence: The events are consistent with a severe reaction to calcium chelation by sodium citrate anticoagulant resulting in symptomatic systemic hypocalcemia .

Example answer:
{"entities": [{"text": "calcium", "type": "Chemical"}, {"text": "sodium citrate", "type": "Chemical"}, {"text": "hypocalcemia", "type": "Disease"}]}

Example input:
Sentence: Empirical treatment with intravenous calcium gluconate was initiated , and muscle contractions slowly subsided over approximately 10 to 15 minutes .

Example answer:
{"entities": [{"text": "calcium gluconate", "type": "Chemical"}, {"text": "muscle contractions", "type": "Disease"}]}

Input:
Sentence: calcium gluconate .

## Item bc5cdr:test:2756
Example input:
Sentence: Compared with control patients , CRF and ESRD patients had higher preoperative serum creatinine levels , a greater percentage of patients with hepatorenal syndrome , higher percentage requirement for dialysis in the first 3 months postoperatively , and a higher 1-year serum creatinine .

Example answer:
{"entities": [{"text": "CRF", "type": "Disease"}, {"text": "ESRD", "type": "Disease"}, {"text": "creatinine", "type": "Chemical"}, {"text": "hepatorenal syndrome", "type": "Disease"}]}

Example input:
Sentence: Compared with hepatitis E virus ( HEV ) and non-A non-E-induced ALF , ATT-ALF patients had nearly similar presentations except for older age and less elevation of liver enzymes .

Example answer:
{"entities": [{"text": "hepatitis E", "type": "Disease"}, {"text": "ALF", "type": "Disease"}]}

Example input:
Sentence: Cancer patients who are chronic carriers of HBV have a higher hepatic complication rate while receiving cytotoxic chemotherapy ( CT ) and this has mainly been attributed to HBV reactivation .

Example answer:
{"entities": [{"text": "Cancer", "type": "Disease"}, {"text": "hepatic complication", "type": "Disease"}]}

Example input:
Sentence: The mean age of patients in the 16 probable cases was 57.9 , with hepatotoxicity being more common in women .

Example answer:
{"entities": [{"text": "hepatotoxicity", "type": "Disease"}]}

Example input:
Sentence: We describe a 70-year-old Hispanic woman who developed fulminant hepatic failure necessitating liver transplantation 10 weeks after conversion from simvastatin 40 mg/day to simvastatin 10 mg-ezetimibe 40 mg/day .

Example answer:
{"entities": [{"text": "fulminant hepatic failure", "type": "Disease"}, {"text": "simvastatin", "type": "Chemical"}, {"text": "simvastatin 10 mg-ezetimibe 40", "type": "Chemical"}]}

Example input:
Sentence: Of those , 13 ( 26 % ) developed biliary pathology .

Example answer:
{"entities": []}

Example input:
Sentence: The results of serum liver function tests suggested hepatocellular injury in 10 ( 63 % ) ; the rest showed a mixed pattern .

Example answer:
{"entities": [{"text": "hepatocellular injury", "type": "Disease"}]}

Example input:
Sentence: Of the 59 cases , 26 ( 44 % ) had a fatal outcome , compared to 136 ( 25 % ) among the non-warfarin patients ( p < 0.01 ) .

Example answer:
{"entities": []}

Example input:
Sentence: This study is the first to demonstrate that impairment of hepatocyte TJs occurs heterogenously in the liver lobule after BDL and suggests that BDL and EE treatments produce different lobular distributions of increased paracellular permeability .

Example answer:
{"entities": [{"text": "EE", "type": "Chemical"}]}

Example input:
Sentence: Of our control group ( n= 50 ) , 21 patients ( 42 % ) were established hepatitis .

Example answer:
{"entities": [{"text": "hepatitis", "type": "Disease"}]}

Input:
Sentence: Indeed , the incidence of liver transplantation and death in this group was 11.7 % if patients had jaundice at presentation , whereas the corresponding figure was 3.8 % in nonjaundiced patients ( P < .04 ) .
