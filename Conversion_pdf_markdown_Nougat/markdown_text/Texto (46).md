

[
primary care facilities in lower-resource settings as a cheaper alternative, but has low sensitivity and is not able to detect drug-resistance[2]. In recent years, more advanced molecular platforms (e.g., GeneXpert PCR machines) have been scaled up as smear-replacement tools that offer greater sensitivity and quicker turnaround times for TB diagnosis[8, 9]. Culture, smear microscopy, and GeneXpert are commonly used as reference standards when evaluating the performance and accuracy of newer diagnostics. While active TB is curable, the long regimens (6 months for drug-susceptible TB) and adverse events caused by the antibiotics used, complicate treatment and increase the risk of drug-resistance emerging[10, 11].

As coughing is a common TB symptom, it can be used to diagnose TB and assess effectiveness of treatment. This Perspective discusses advances in acoustic epidemiology and AI-based methods to assess cough and how these can be used during TB diagnosis and treatment.

### Using cough as an objective biomarker for TB control and care

Cough is a complex physiological phenomenon as it is both a symptom of, and a defense mechanism against, respiratory diseases. Cough is a hallmark symptom of pulmonary TB and is clinically assessed throughout the cascade of TB care, for example, as a triage tool to trigger TB testing or to monitor response to therapy. Cough patterns vary depending on the amount of \(M\). _tuberculosis_ in the lungs, and cough tends to regress with successful TB therapy[12, 13, 14, 15].

While many TB screening programs use cough duration and symptoms to determine when TB testing is required, this symptom screening approach lacks sensitivity. In low-resource settings, peripheral health centers, and communities, triage tools such as chest X-rays are not available, thus symptom-based screening remains the only available strategy to identify people with TB. The World Health Organization (WHO) recommends testing people reporting symptoms compatible with TB, including prolonged cough (usually interpreted as a cough that lasts two weeks or longer)[16]. According to the 2021 WHO TB screening guidelines, the sensitivity of prolonged cough alone is 42% among HIV-negative individuals, well below the WHO community-based triage test target product profile (TPP) of \(\geq\)90% sensitivity[16, 17].

It is difficult for people to describe their cough symptoms, and it is as challenging for clinicians to identify the cause. Individuals tend to have poor recall of the duration of their symptoms, and symptom severity is subjective[18, 19]. Given our current inability to objectively detect and monitor cough sounds, patients and providers systematically reduce this data-rich symptom into subjective and dichotomous information (e.g., cough versus no cough, chronic versus acute, getting better versus getting worse), precluding rigorous understanding of cough data, and preventing the use of cough to its full clinical potential. By making cough an objective and measurable component of TB care, either by helping individuals recognize abnormal cough patterns, or by harnessing artificial intelligence (AI) technology (using computer systems to recognize and interpret the implications of a cough sound)[20] to differentiate types of coughs, we can potentially improve patient management and clinical outcomes at different stages during the cascade of TB care.

### Advances in acoustics for objective cough monitoring

Questionnaire-based tools and scales have been used to collect and evaluate the severity of coughs of varying etiology in an attempt to transform subjective cough reporting into objective data. Such tools include the visual analog scale (VAS), cough symptom score (CSS), and cough diaries[21]. Both the VAS and CSS attempt to quantify the severity of cough based on a patient's perception of their cough. Cough diaries can take various forms, but all depend on patients tracking the frequency and severity of their coughs over time. Other questionnaires expand their assessment of cough to incorporate questions on health-related quality of life[21]. For example, the Leicester Cough Questionnaire (LCQ) is a validated self-completed questionnaire that measures the quality of life of individuals with a chronic cough, and has previously been used to evaluate cohorts of people with TB undergoing anti-TB therapy[22, 23, 24]. While such tools are easy to use and implement in clinical settings, they remain subject to bias related to self-perception of health and attention to symptoms, ultimately limiting their clinical application.

Objectivity in cough analysis is improved when using recording devices and computer-assisted acoustic interpretation algorithms. As early as the 1960s, Loudon and Spohn used tape recorders to record and count the coughs of people with TB at night[25]. Other forms of early ambulatory cough meters involved the integration of audio recording devices and electromyogram (EMG) electrodes[26], which simultaneously recorded cough sounds and chest muscle contractions when the person coughed. In 2006, Paul et al. developed and evaluated a self-contained cough monitor composed of an accelerometer (for measuring cough-related vibrations) that stored data on a CompactFlash memory card[27]. This device was attached to the patient's neck in the suprasternal notch (jugular notch) and demonstrated good agreement with coughing seen on video footage. Over the years, more advanced 24 h recording devices have been developed. These devices typically have a microphone (e.g. free-field microphone necklace or one that attaches to the patient's lapel), which sends the cough sounds to a digital sound recorder, usually attached at the hip of the patient[28]. Such recording devices include the Leicester Cough Monitor (LCM), the Cayetano Cough Monitor (CayeCoM), and the VitaloJak[29, 30, 31].

Cough counts and patterns were the first objective markers used to analyze cough severity and variation over time. The LCM, CayCoM and VitaloJak have all been validated for the measurement of cough frequency[29, 30, 31]. The LCM and VitaloJak are currently the most widely used cough monitoring tools, with reported cough detection sensitivities of 91% and \(>\)99%, respectively[28]. The LCM uses a largely automated algorithm for detecting cough sounds, requiring operator input for calibrating the device (approximately 5 min for every 24 h of recording)[28]. The LCM and the CayCoM have been used to investigate cough among people with pulmonary TB. Turner et al. used the LCM as part of a cross-sectional survey of cough frequency among people with TB and their contacts[32]. Williams et al. used the LCM to correlate exhaled \(M\). _tuberculosis_ with cough frequency[15]. The CayCoM has been used in various studies to measure cough frequency among cohorts of people with pulmonary TB undergoing treatment[12, 13, 34, 35, 14]. A summary of studies that use various tools for objective cough monitoring in the context of TB care can be found in Supplementary Table 1.

While ambulatory recording devices have enabled continuous cough recording, many of the devices used to date are bulky and obtrusive. Cough is an obvious and stigmatizing symptom, especially among people with TB, and the COVID-19 pandemic has dramatically heightened this stigmatization[35]. In order to efficiently monitor people with cough, recording strategies must be inconspicuous to avoid adding to the stigmatization of respiratory conditions. Smartphones with cough detection and recording applications provide a more discreet approach to monitoring TB coughs. Several cough recording applications have already been developed, including Hyfe Research, AI4COVID-19, and ResAppDx[36, 37, 38].

### Data acquisition

The data acquisition system is a collection of 240 

### Developments in artificial intelligence allow for rigorous assessment of cough

Advances in machine learning, a subset of AI that enables machines to apply algorithms on available data to automatically "learn" and make autonomous decisions [20], has given rise to a variety of algorithms for cough monitoring that can be deployed on digital recording devices, including smartphones (see Supplementary Table 1 for examples of the types of algorithms used for cough detection and cough classification). This new technology allows the analysis of both the frequency and the nature of cough sounds. For example, some algorithms first transform sound recordings into spectrograms--a visual representation of the frequency, amplitude, and time characteristics of sounds--before running an algorithm on the spectrogram to visually analyze the cough's features (Fig. 1).

These algorithms are being trained to identify human coughs from ambient sounds (cough detection), as well as to differentiate coughs from patients with distinct clinical conditions or at different stages of disease (cough classification), though the latter use case is yet to be validated [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 1

**Improving community-based monitoring and active case finding.** Very preliminary data suggests that cough classification algorithms could be developed that meet WHO TPPs for a community-based TB screening test[44, 45]. Further validation is needed using cohorts of large sample size and diverse populations before any definite conclusions can be made regarding their sensitivities and specificities. AI-based cough screening could complement other available community-based screening approaches, such as chest X-rays, increasing the number of people with presumed TB appropriately referred to facilities for confirmatory testing in a timely manner. Indeed, using cough to predict chest X-ray abnormalities could trigger radiology testing for which multiple automated interpretation algorithms have now been thoroughly validated[50]. If deployed on mobile devices, AI-based cough screening could allow for low-cost remote active case finding and self-screening, with subsequent referral to a health facility for confirmatory TB testing and linkage to care. The vignette in Fig. 3 illustrates how a cough monitoring tool may help refer people with a cough to a physician.

For individuals at higher risk of developing active pulmonary TB, such as household contacts, cough detection and longitudinal monitoring could objectively document an increase in TB-compatible symptoms, prompting early care-seeking and limiting transmission. This approach could also help address subclinical pulmonary TB[51]. Individuals who have mild symptoms, but do not recognize them as being significant, are also considered subclinical[51]. In such cases, digital cough monitoring could be used to identify the presence or significance of cough that would otherwise have gone unrecognized or unreported. However, digital cough monitoring would not extend to truly asymptomatic individuals with subclinical TB, limiting its application as an active case finding tool in this subgroup. A study of 24 people with TB found that cough frequency may not be associated with _M. tuberculosis_ output collected on face masks[15]. That is, some participants who did not cough very often still expelled a lot of _M. tuberculosis_ (and vice versa). While further investigations are needed, this raises potential limitations of relying on cough monitoring for evaluating active case-finding and reducing TB transmission.

**Enhancing the performance of diagnostic algorithms.** Even when people with presumed TB reach the health facility, it is not guaranteed that they will access proper confirmatory testing. One reason for this is a lack of awareness and training among healthcare workers to recognize key TB symptoms. This problem has been demonstrated by studies involving standardized patients (SPs), healthy persons trained to visit health facilities with fake TB symptoms, without the healthcare providers being aware that these symptoms are not real[52]. A systematic review on SPs in India found that only half of healthcare providers knew that prolonged cough (>2 weeks) may be associated with TB[52].

Fig. 2: **Potential use cases for digital cough monitoring in the tuberculosis cascade of care.** Each step in the TB care cascade is represented as a bar. The gaps in the cascade are in red between each step. Boxes pointing at the gaps represent possible digital cough-based solutions to address various gaps. The height of the bar graphs and the length of the gaps are not scaled to represent true values. They are intended to help illustrate the different steps of the care cascade and points at which people with TB may fail to benefit from care. (Cascade of care adapted from Fig. 1 of Subbaraman et al.)[49].


Figure 3: **Example use of smartphone-based cough screening application for community-based monitoring.** In this vignette, a female is experiencing symptoms of disease, including cough. Using a phone with the example Health App (not a real app), she is prompted to cough and report any other symptoms she is experiencing. The AI algorithm in the Heath App uses the information to provide likely causes of disease (in this case, COVID-19 or TB) and refers here to consult a physician for confirmatory testing. (Vignette originally created for _The Lancet Citites’ Commission on Reimagining India’s Health System_, by Raghu Dharmaraju, Vijay Chandra, Umakant Son, and Shubraneel Ghosh, ARTPARK (AI & Robotics Technology Park) at Indian Institute of Science. “_A vignette from 2030 in rural India: How might technology enable citizen-centered health journeys?_”https://www.artparkir/reimagie-health/2030_rural_India).

 Another study in India found that SPs presenting with TB symptoms were severely under-tested [53].

Similar to community-based screening and active case-finding, health providers may potentially use AI-based cough classification applications to help triage people with presumed TB, complementing less sensitive symptom-based triage methods and increasing the proportion of individuals with presumed TB who undergo confirmatory testing. Because symptom screening is also non-specific, cough classification tools may also help reduce the proportion of people without TB who unnecessarily undergo TB testing.

**Monitoring the effect of treatment**. Smartphones are globally available and can act as recording devices. They are already used for TB treatment-adherence monitoring with video Directly Observed Therapy (vDOT), which allows people with TB to send videos of themselves ingesting anti-TB treatment to their health provider, instead of having to travel to the clinic to take their anti-TB treatment in front of a health provider, as required under traditional DOT methods [54]. Given that cough symptoms regress with successful treatment, cough detection applications could be used as a low-cost, person-centric approach for clinicians to remotely monitor people with TB's clinical response to treatment, or even for people to self-monitor their cough as treatment progresses [13]. Objectively-documented unfavorable cough evolution patterns could prompt patients and providers to investigate whether the treatment regimen being used is effective, allowing for early recognition of drug resistance or poor adherence.

**Achieving relapse-free cures and minimizing long-term lung damage**. A significant proportion of people who are successfully cured of TB are at risk of TB recurrence within the first year following completion of anti-TB treatment [55]. The prospective cough monitoring used during treatment could be continued during this high risk period to identify early signs of TB recurrence. Even if people do not experience TB recurrence or relapse, they are at increased risk of experiencing post-TB lung damage, an aspect of TB care that is often overlooked in TB management pathway [56]. Thus, cough monitoring, if validated, could also be useful as a starting point in identifying individuals with post-TB lung disease and related lung function decline.

**Supporting drug development and TB research**. AI-based cough detection technology could also play a role in TB research and development. Digital cough monitoring could be used as a secondary endpoint in clinical drug development trials. Drug development trials have so far relied on evaluating whether sputum culture test results change from positive to negative during the first 8 weeks of therapy as a proxy for anti-TB treatment efficacy [57]. Such culture methods are resource- and time-intensive, and do not allow the monitoring of intermediate outcomes, including patient symptoms. In addition, regulatory agencies may request data on patient-reported improvement in cough, though again this is subjective and can have variable accuracy [58, 59]. Similar to symptom-based screening, self-assessment of cough in the context of experimental therapy-efficacy measurement is unlikely to be fully accurate. Objective monitoring of cough may allow for more nuanced monitoring of intermediate endpoints by acting as a complement to conventional culture-based endpoints and patient-reported outcomes.

**Furthering the clinical use of digital cough monitoring**

The recent progress in acoustics and cough analysis, combined with the urgent need to improve respiratory disease detection and tracking methods in the context of COVID-19, have accelerated applications of acoustic epidemiology in clinical research [37, 42, 60]. This emerging field depends on increasingly less obtrusive ways to collect cough data as well as more sophisticated analytics that go beyond cough detection to infer clinical etiology based on cough patterns and spectral characteristics.

The development, validation, and roll-out of digital cough monitoring tools for TB will require global coordinated data collection, curation, and analysis effort. Training and validation cough datasets need to be collected from people in the intended use population and settings. They must include large numbers of people with different demographic characteristics (e.g. age, sex, ethnicity) as well as different forms of pulmonary TB in clinical settings with variable background epidemiology of respiratory diseases. This 'big data' approach is mandatory for the development and refinement of AI algorithms to achieve high external validity. Since cough is not specific to TB, such datasets should not be limited to the development of AI algorithms for TB but should also be used to develop and refine cough algorithms for other respiratory diseases and conditions that are linked to cough. To accelerate this endeavour, we must avoid the multiplication of isolated algorithm development efforts that use data from homogeneous patient populations [47].

Collective efforts to aggregate and annotate cough data may accelerate research and tool development. For example, Global Health Labs, the Bill and Melinda Gates Foundation, and the Patrick J. McGovern Foundation are currently supporting efforts to collect cough data and are investing in infrastructure to build an extensive database of cough sounds. Researchers interested in cough and acoustic epidemiology--in the context of TB or any other respiratory disease or condition linked to cough--can contribute to this growing anonymized database and use the existing data to develop and refine AI. While this effort is an important step towards integrating cough into TB care, there is still a need for a broader recognition of the potential advantages of integrated AI-based cough tools into TB care. As more AI-based cough detection tools and applications become available, increased effort should be made to routinely collect cough data within TB programs, prevalence surveys, and clinical studies in order to contribute to the growing field of acoustic epidemiology. Such efforts will help characterize the natural evolution of TB cough, objectively describe the impact of specific interventions on TB symptoms, and iteratively improve operational and performance characteristics of cough-based TB solutions. Like other biomarkers, collected cough data must be anonymized, annotated with clinical metadata, and shared in open-source repositories. TB cough data must also be made available in the same way that digital chest X-ray libraries are available for the validation of electronic interpretation algorithms, or that TB genomic sequences are available to support novel drug development and validation of drug resistance assays [61, 62]. Through such collective efforts, we can accelerate algorithm development and the roll-out of cough-based clinical tools. This data sharing approach should also improve partnerships between academia and industry by allowing faster hypothesis-testing as well as rapid product design and translation into user-friendly tools that can be deployed at scale in TB care. In conclusion, AI and acoustic epidemiology have the potential to revolutionize the fight against TB.

## References

* [1] World Health Organization. Global tuberculosis report 2020. https://www.who.int/publications/i/item/9789240013131 (2020).
* [2] * [2] Zimmer, A. J. et al. Tuberculosis in times of COVID-19. _J. Epidemiol. Community Health_**76**, 310-316 (2022).
* [3] Pai, M. et al. Tuberculosis. Nat. Rev. Dis. Prin. **2**, 1-23 (2016).
* [4] Migliori, G. B. et al. The definition of tuberculosis instead on the spectrum of tuberculosis disease. _Berable_**17**, 210079 (2021).
* [5] Sharma, S. K., Mohan, A., & Kohli, M. Extrapulmonary tuberculosis. _Expert Rev. Respir. Med._**15**, 931-948 (2021).
* [6] Vonghhahi-Moeung, R., Poncet, A., Renzi, G., Schrenzel, J. & Jansness, J. P. Time to detection of growth for mycobacterium tuberculosis in a low incidence area. _Front. Cell. Infect. Microbiol._**11**, 775 (2021).
* [7] Kak, S. V., Denkinger, C. M., Chodero, P. & Pai, M. Replacing smear microscopy for the diagnosis of tuberculosis: what is the market potential? _Exp. Respir. J._**4**, 1793-1796 (2014).
* [8] Steingart, K. R. et al. Xpert MTR/RF assay for pulmonary tuberculosis and rifampicin resistance in adults. _Cofrane Database Syst. Rev._**2014**, CD009593 (2014).
* [9] Acharya, B. et al. Advances in diagnosis of Tuberculosis: an update into molecular diagnosis of Mycobacterium tuberculosis. _Mol. Biol. Rep._**47**, 4065-4075 (2020).
* [10] Nahid, P. et al. Executive summary: official American Thoracic Society/ Centers for disease control and prevention/infectious diseases Society of America Clinical Practice Guidelines: treatment of drug-susceptible tuberculosis. _Clin. Infect. Dis._**63**, 853-867 (2016).
* [11] Forget, E. J. & Menrieu, D. Adverse reactions to first-line antither tuberculosis drugs. _Expert Opin. Drug Syst._**5**, 231-249 (2006).
* [12] Prozato, A. et al. Cough frequency during treatment associated with baseline cavitary volume and proximity to the airway in pulmonary TB. _Chest_**153**, 1358-1367 (2018).
* [13] Prozato, A. et al. Dynamics of cough frequency in adults undergoing treatment for pulmonary tuberculosis. _Clin. Infect. Dis._**64**, 1174-1181 (2017). (Coughing among TB patients decreased significantly after two weeks of anti-TB treatment, highlighting the potential of using cough as a marker for TB treatment response).
* [14] Lee, G. O. et al. Cough dynamics in adults receiving tuberculosis treatment. _PLoS One_**15**, e0231167 (2020).
* [15] Williams, C. M. et al. Exhaled Mycobacterium tuberculosis output and detection of subclinical disease by face-mask sampling prospective observational studies. _Laserl. Infect. Dis._**20**, 607-617 (2020).
* systematic screening for tuberculosis disease._ https://www.who.nl/publications/int/978920026124 (2021).
* [17] World Health Organization. _High-priority target product profiles for new tuberculosis diagnosis diagnosis: report of a consensus meeting._ https://apps.who.int/its/handle/10665/13561/ (2014).
* [18] Cho, P. S. P., Birring, S. S., Fletcher, H. V. & Turner, R. D. Methods of cough assessment. _J. Alberg Clin. Immunol. Pract._**7**, 1715-1723 (2019).
* [19] Fekin, D. R. et al. Evaluation of the optimal recall period for disease symptoms in home-based morbidity surveillance in rural and urban Kenya. _Int. J. Epidemiol._**39**, 450-458 (2010).
* [20] Holm, J. M. et al. Machine learning and artificial intelligence definitions, applications, and future directions. _Curr. Rev. Musculoskeletal. Med._**13**, 69-76 (2020).
* [21] Wang, Z., Wang, M., Wen, S., Yu, L. & Xu, X. Types and applications of cough-related questionnaires. _J. Thorac. Dis._**11**, 4379-4388 (2019).
* [22] Suzuki, T. et al. Improved cough- and sputum-related quality of life after initiation of treatment in pulmonary tuberculosis. _Respir. Investig._**57**, 252-259 (2019).
* [23] Turner, R., Bothamley, G. & Birring, S. P240 Validation of the Licester Cough Questionnaire in pulmonary tuberculosis. _Thorax_**76**, A1972-A198 (2015).
* [24] Birring, S. S. et al. Development of a symptom specific health status measure for patients with chronic cough: Leicester Cough Questionnaire (LCO). _Thorax_**58**, 339-343 (2003).
* [25] Loudon, R. G. & Spohn, S. K. Cough frequency and infectivity in patients with pulmonary tuberculosis. _Am. Rev. Respir. Dis._**99**, 109-111 (1969).
* [26] Hsu, J. Y. et al. Coughing frequency in patients with persistent cough: Assessment using a 24 hour ambulatory reorder. _Eur. Respir. J._**7**, 1246-1253 (1994).
* [27] Paul, I., Wai, K., Jewell, S., Shaffer, M. & Varadan, V. Evaluation of a new self-contained, ambulatory, objective cough monitor. _Cough_**2**, 1-7 (2006).
* [28] Hall, J. Lozano, M., Estrada-Petrocelli, L., Birring, S. & Turner, R. The present and future of cough counting tools. _J. Thorac. Dis._**12**, 5207-5223 (2020). (A thorough review on the field of cough detection tools for respiratory diseases, and overview on how such tools could improve clinical management of respiratory diseases).
* [29] Smith, J. & Woodcock, A. New developments in the objective assessment of cough. _Lang_**186**, 548-554 (2008).
* [30] Matos, S., Birring, S. S., Pavord, I. D. & Evans, D. H. An automated system for 24-h monitoring of cough frequency: The Leicester cough monitor. _IEEE Trans. Biomed._**52**, 4472-479 (2007).
* [31] Birring, S. S. et al. The Leicester Cough Monitor: Preliminary validation of an automated cough detection system in chronic cough. _Eur. Respir. J._**31**, 1013-1018 (2008).
* [32] Turner, R., Repossi, A., Matos, S., Birring, S. & Bothamley, G. S79 cough prevalence and frequency in pulmonary tuberculosis. _Thorax_**69**, A43-A44 (2014).
* [33] Tracey, B. H. et al. Cough detection algorithm for monitoring patient recovery from pulmonary tuberculosis. _Proceedings of the Annual International Conference of the IEEE Engineering in Medicine and Biology Society, EMBS_. **2011**, 6017-6020 (2011).
* [34] Larson, S. et al. Validation of an automated cough detection algorithm for tracking recovery of pulmonary tuberculosis patients. _PLoS One_**7**, e46229 (2012).
* [35] Cremers, A. L. et al. Assessing the consequences of stigma for tuberculosis patients in urban Zambia. _PLoS One_**10**, e0119861 (2015).
* [36] Gabaldon-Figuiraira, J. C. et al. Digital acoustic surveillance for early detection of respiratory disease outbreaks in Spain: a protocol for an observational study. _BMI Open_**11**, e015278 (2021).
* [37] Imran, A. et al. AltoCOVID-19: A1 enabled preliminary diagnosis for COVID-19 from cough samples via an app. _Informatics Mod. Unlocked_**20**, 100378 (2020).
* [38] Moschovis, P. P. et al. The diagnosis of respiratory disease in children using a phone-based cough and symptom analysis algorithm: The smartphone recordings of cough sounds 2 (SMARTCOUGH-C 2) trial design. _Contemp. Clin. Trials_**101**, 106278 (2021).
* [39] Bales, C. et al. Can machine learning be used to recognize and diagnose cough in 2020 _International Conference on e-Health and Bioengineering (EHB)_ 1-4 (2020).
* [40] Coppock, H. et al. End-to-end convolutional neural network enables COVID-19 detection from breath and cough audio: a pilot study. _RMI Innov._**7**, 356-362 (2021).
* IEEE Symposium on Computer-Based Medical Systems_ vol. 2021-June 18-188 (2021).
* [42] Lagatura, I., Hueto, F. & Suhrana, B. COVID-19 artificial intelligence diagnosis using only cough recordings. _IEEE Open J. Eng. Med. Biol._**1**, 275-281 (2020).
* [43] Kavpilova, L. et al. Continuous sound collection using smartphones and machine learning to measure cough. _Digit. Biomarkers_**3**, 166-175 (2019).
* [44] Pathir, R., has, Tandon, S. & GangSherty, S. Acoustic epidemiology of pulmonary tuberculosis (TB) & Covid-19 leveraging AI/ML. _J. Pharmacol. Res. Reports_**4**, 2-6 (2022).
* [45] Pahar, M. et al. Automatic cough classification for tuberculosis screening in a real-world environment. _Physiol. Meas._**42**, 105014 (2021). (Preliminary investigation of an AI-based cough classification algorithm to differentially screen TB coughs vs non-TB coughs, achieving a sensitivity of 93% and specificity of 93%).
* [46] Botha, G. H. R. et al. Detection of tuberculosis by automatic cough sound analysis. _Physiol. Meas._**39**, 054005 (2018).
* [47] Topol, E. J. Is any cough COVID-19_Izect_**396**, 1874 (2020).
* [48] Ruijes, A. W. S. et al. Evidence of bias and variation in diagnostic accuracy studies. _Can. Med. Assoc. J._**174**, 469-476 (2006).
* [49] Subbarama, R. et al. Contracting care cascades for active tuberculosis: a strategy for program monitoring and identifying gaps in quality of care. _PLoS Med._**16**, e102754 (2019).
* [50] Qin, Z. et al. Tuberculosis detection from chest x-rays for triaging in a high tuberculosis-burden setting an evaluation of five artificial intelligence algorithms. _Laserl. Digit. Biol._**3**, e543-e554 (2021).
* [51] Kendall, E. A., Shrestha, S. & Dowdy, D. W. The epidemiological importance of subclinical tuberculosis is a critical reappraisal. _Am. J. Respir. Crit. Care Med._**203**, 168-174 (2021).
* [52] Satyanarayana, S. et al. Quality of tuberculosis care in India: a systematic review. _Int. J. Thorac. Imag. Dis._**19**, 751-763 (2015).
* [53] Das, J. et al. Use of * [36] Meghi, J., Simpson, H., Squire, S. B. & Mortimer, K. A systematic review of the prevalence and pattern of imaging defined Post-TB lung disease. _PLoS One_**11**, 061116 (2016).
* [37] Davies, G., Borex, M., Hermann, D. & Hoelscher, M. Accelerating the transition of new tuberculosis drug combinations from Phase II to Phase III trials: New technologies and innovative designs. _PLoS Med._**16**, e1002851 (2019).
* [38] Cruz Rivera, S. et al. The impact of patient-reported outcome data from clinical trials perspectives from international stakeholders. _J. Patient-Reported Outcomes_**4**, 51 (2020).
* [39] Inamed Incorporated. Validation of patient reported outcome measures in participants with nontuberculous mycobacterial lung infection caused by mychoceleriumium complex (ARISE). https://clinicaltrials.gov/t2/show/NCT04677543 (2021).
* [40] Bagd, P. et al. Coqbi Against COVID. Evidence of COVID-19 Signature in Coqbi Sounds. _arXiv:2009.08790_ (2020).
* [41] Jaeger, S. et al. Two public chest X-ray datasets for computer-aided screening of pulmonary diseases. _Quant. Imaging Med. Surg._**4**, 475-477 (2014).
* [42] GleyPTIC Consortium and the 10000 Genomes Project. et al. Prediction of Susceptibility to First-Line Tuberculosis Drugs by DNA Sequencing. _N. Engl. J. Med._**379**, 1403-1415 (2018).

## Acknowledgements

We would like to thank all people with TB, providers and researchers who have and will contribute acoustic data to the tuberculosis scientific community to make cough count in tuberculosis. We would also like to thank Ragh Pharmaway, Vay Chandra, Umukant Son, and Subramed Ghosh from ARTPARK (AI & Robotics Technology Park) at the Indian Institute of Science for allowing us to use the wignette they developed that illustrates the use of smartphone-based cough detection for community-based screening.

## Author contributions

Conceptualization (A.I.Z., S.G.L.) literature article review (A.I.Z., D.J., S.G.L.), cascade of TB care design and assessment of clinical applications (A.I.Z., C.U.G., R.P., P.D., D.I., A.C., M.P., S.G.L.), machine learning perspective and tuberculosis digital cough analysis (R.P.), collaborative cough consortium design and funding acquisition (P.D., A.C., S.G.L.), writing original draft (A.I.Z., S.G.L.), writing review and editing (C.U.G., R.P., P.D., D.J., A.C., M.P.), visualization (A.I.Z.).

## Competing interests

The authors declare no competing interests.

## Additional information

Supplementary informationThe online version contains supplementary material available at https://doi.org/10.1038/s43856-022-00149-w.

## Correspondence

and requests for materials should be addressed to Simon Grandjean Lapiner.

Peer review information Communications Medicine thanks Byeru Schuller, Mirjan Bakker, Robert Wilkinson and Graeme Meintes for their contribution to the peer review of this work. Peer reviewer reports are available.

## Reprints and permission information

is available at http://www.nature.com/reprints

## Publisher's note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Appendix A Open Access

This article is licensed under a Creative Common Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.

 