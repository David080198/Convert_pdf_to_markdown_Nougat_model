

# An ECG-based artificial intelligence model for assessment of sudden cardiac death risk

Lauri Holmstrom

Harpriya Chugh

Kotoka Nakamura

Ziana Bhanji

Madison Seifter

Audrey Uy-Evanado

Kyndaron Reiier

David Ouyang

& Sumeet S. Chugh

###### Abstract

Background Conventional ECG-based algorithms could contribute to sudden cardiac death (SCD) risk stratification but demonstrate moderate predictive capabilities. Deep learning (DL) models use the entire digital signal and could potentially improve predictive power. We aimed to train and validate a 12 lead ECG-based DL algorithm for SCD risk assessment.

Methods Out-of-hospital SCD cases were prospectively ascertained in the Portland, Oregon, metro area. A total of 1,827 pre- cardiac arrest 12 lead ECGs from 1,796 SCD cases were retrospectively collected and analyzed to develop an ECG-based DL model. External validation was performed in 714 ECGs from 714 SCD cases from Ventura County, CA. Two separate control group samples were obtained from 1342 ECGs taken from 1325 individuals of which at least 50% had established coronary artery disease. The DL model was compared with a previously validated conventional 6 variable ECG risk model.

Results The DL model achieves an AUROC of 0.889 (95% Cl 0.861-0.917) for the detection of SCD cases vs. controls in the internal held-out test dataset, and is successfully validated in external SCD cases with an AUROC of 0.820 (0.794-0.847). The DL model performs significantly better than the conventional ECG model that achieves an AUROC of 0.712 (0.668-0.756) in the internal and 0.743 (0.711-0.775) in the external cohort.

Conclusions An ECG-based DL model distinguishes SCD cases from controls with improved accuracy and performs better than a conventional ECG risk model. Further detailed investigation is warranted to evaluate how the DL model could contribute to improved SCD risk stratification.

Sudden cardiac death (SCD) is a major, global public health problem1. In Europe and the United States, \(\sim\)700,000 individuals will suffer from this mostly lethal condition on a yearly basis2. Given the high mortality rate of SCD, effective primary prevention could make a substantial positive impact but the current approach needs augmentation3. Based on randomized clinical trials, patients identified to be at high risk based on severely reduced left ventricular systolic function (LVEF \(\leq\) 35%) receive implantable cardi Converter-defibrillators4. However, there is no existing risk stratification methodology for individuals with LVEF \(>\) 35% that make up 70% of community SCD5. Moreover, \(\sim\)40-50% of all SCD cases occur in individuals without previously diagnosed cardiac disease, which is a prerequisite for SCD risk assessment.

Footnote 1: Center for Cardiac Arrest Prevention, Department of Cardiology, Smidt Heart Institute, Cedars-Sinai Medical Center, Los Angeles, CA, USA. \({}^{\dagger}\)Division of Artificial Intelligence in Medicine, Department of Medicine, Cedars-Sinai Medical Center, Los Angeles, CA, USA. \({}^{\dagger}\)e-mail: sumeet.chugh@cshs.org

Some novel prediction methodologies that extend beyond the left ventricular ejection fraction have been developed2 but these are still in the research domain. Especially, the standard 12 lead ECG has received a lot of interest in the research field in anticipation of improving long-term SCD risk stratification3. Various ECG abnormalities have been identified to associate with an increased long-term risk of SCD[31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 82, 84, 86, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169,previously published a 6 variable ECG electrical risk score that identifies individuals at an increased risk of SCD1. However, conventional ECG-based risk stratification tools are usually limited by low accuracy or practicality, since they include measurements that are not part of a usual ECG interpretation, thus requiring customized measurement or trained medical personnel interpretation.

In recent years, ECG-based deep learning (DL) algorithms have been developed and are being deployed for diagnostic purposes [13]. ECG-based DL models have been successfully trained to detect various cardiac conditions, e.g., LV dysfunction [14], HCM3 or to recognize patients at high risk for atrial fibrillation [14]. As opposed to conventional ECG analysis, DL models do not require manual selecting and extracting of relevant features, which enables them to capture the entire ECG signal and achieve higher prediction accuracy.

In the current study, we train, test, and validate an ECG-based DL model to identify individuals at high risk of SCD, and compare the predictions with a previously published and validated conventional ECG electrical risk score [10]. The model accurately distinguishes sudden cardiac death cases from controls, performing better than the conventional ECG risk score.

## Methods

### Study design

We used two geographically separate community-based, prospective, and ongoing studies of out-of-hospital SCDs in the general population: Oregon SUDS (training, validation, and testing) and Ventura PRESTO (external validation). Given that CAD is the most common underlying substrate for SCD, our control group was designed to represent a control sample with a similar prevalence of previously diagnosed CAD.

### SCD cohorts (Oregon SUDS & Ventura PRESTO)

Detailed methods for Oregon SUDS and Ventura PRESTO studies have also been published earlier [27, 28, 29]. Both Oregon SUDS and Ventura PRESTO studies ascertain all out-of-hospital SCDs from the Portland Oregon metro area (population \(\sim\)1 million, Oregon SUDS, since 2002), and Ventura County, California (population \(\sim\)850,000, Ventura PRESTO, since 2015) using an identical approach. Potential SCD cases in the community are identified in collaboration with each region's emergency medical services (EMS) system. Subsequently, established adjudication methods to confirm likely cardiac etiology of SCD were employed by trained physicisearchers; using all available medical record data for each potential SCD case, EMS prehospital care reports, medical examiner's reports, and death certificates from Oregon and California state vital statistics records. SCD was defined as a sudden loss of pulse due to a likely cardiac etiology that occurred with a rapid witnessed collapse, or if unwitnessed, the subject should have been seen alive within 24 h. We included successfully resusculated cases in addition to non-survivors. Cases of likely non-cardiac etiology (e.g., trauma or substance abuse) or chronic minimal illness were excluded.

All cases with archived resting 12 lead ECGs available for analysis were included (Fig. 1). These ECGs were recorded prior to and unrelated to the SCD event, with a calibration of 10 mm/mV and paper speed of 25 mm/s. ECGs with pac rhythm, atrial fibrillation, or atrial flutter were excluded a priori to create a DL model that could be applied to ECGs in sinus rhythm. Pre-arrest clinical records and ECGs were available if the patient provided written consent or was deceased, in which case consent was waived by the institutional review boards. Institutional review boards of Ventura County Medical Center, Oregon Health and Science University, Cedars-Sinai Health System, and all other relevant health systems and participating hospitals approved the study protocol.

### Control population

We recruited control subjects from the Portland Oregon metro area to represent individuals at intermediate risk of SCD with a large proportion having CAD. Institutional review boards of Ventura County Medical Center, Oregon Health and Science University, Cedars-Sinai Health System, and all other relevant health systems and participating hospitals approved the study protocol, and all other relevant health systems and participating hospitals approved the study protocol, and all control subjects gave informed consent for their data to be used in the study. Control subjects were identified through multiple sources, including patients undergoing angiography, patients having their chest pain assessed by EMS, or patients visiting an outpatient cardiology clinic. We ascertained the control subjects so that the prevalence of CAD and MI was comparable to SCD cases. Control patients had no previous history of cardiac arrest or ventricular arrhythmias. Matching cases and controls for underlying CAD enables the development of a DL model that identifies high-risk patients from a clinically comparable 'intermediate-risk' group. ECGs were obtained and archived in an identical manner to cases.

In all SCD cases and controls, paper 12 lead ECG recordings were scanned, and digitized using software (ECGScan), which has been demonstrated to provide a robust reconstruction of a digital ECG waveform [3]. Due to the variable length of ECG leads, we restricted the length of each lead in each sample to a 2.5 s strip, which was the minimum length of ECG waveform for each lead. Hence, digital 2.5 s strips of each lead in the 12 lead ECG were used as input for the DL model. ECGScan produces time series ECG signal, and with a sampling rate of 500 Hz, the final shape of each ECG arrays was \(12\times 1250\).

### Deep learning model development and training

To identify SCD cases using 12 lead ECG waveforms, we developed a convolutional neural network for ECG interpretation (Fig. 2). We trained the model to identify SCD cases with 1,101 prearrest 12 lead ECGs from 1,076 SCD cases from Oregon SUDS and 613 12 lead ECGs from 597 controls. A separate validation cohort of 366 prearrest ECGs and 200 control ECGs was used to determine when to stop model training. The study sample was divided at the patient level so that multiple ECGs from the same patient were included in the same cohort. In the training and validation datasets we used multiple ECGs per patient, but in the internal testing dataset and external validation dataset we used only one ECG per patient (the closest ECG that was unrelated to the SCD event). The mean time from ECG to SCD was \(2.0\pm 2.7\) years in Oregon SUDS and \(1.6\pm 2.1\) years in Ventura PRESTO. We trained the model using the PyTorch DL framework, and the Adam optimizer with default parameters (initial learning rate of 1e-3) with a batch size of 500 and for 55 epochs. Based on the area under the curve of the receiver operating characteristic (AUROC) curve in the validation dataset, we performed early stopping for training.

The DL model was designed to interpret 12 lead ECG waveforms starting with atrous convolutions which were followed by multi-channel 1D convolutions. We limited the number of layers to less than 1/10th the size of previously described architectures [13, 14, 15] to minimize model complexity and optimize model runtime. The DL model incorporated convolutional layers after initial atrous layers, with an inverted residual structure. In the DL model, input and output are bottleneck 9 layers with an intermediate expansion layer. To allow information integration across the 12 lead ECGs, the number of input channels increased gradually in each set of expansion layers that were preceded by bottleneck layers. The model was optimized for a lightweight architecture while still maximizing performance [1]. Given that we used ECG waveform instead of images as input data, our deep learning model is a 1D equivalent, and our model is smaller than other ECG models in prior literature with similar performance More details regarding the model architecture can be found in the original papers [23, 24].

### Statistical analyses

All continuous variables are expressed as mean \(\pm\) standard deviation. After model development and training, we performed all statistical analyses on the internal held-out test set and external validation dataset which were never seen during model training. We calculated the model's performance in identifying SCD cases by the AUROC. The model was compared to a previously developed conventional ECG electronic risk score, which evaluates the sum of 6 ECG risk markers: resting heart rate \(>\) 75 bpm, LVH, delayed QRS transition, QRS-T angle \(>\) 90\({}^{\circ}\), prolonged QTc, and prolonged Tpeak-to-Tend interval1. We performed logistic regression models in the internal test dataset and external validation dataset using clinical variables (age, sex, heart failure, coronary artery disease, myocardial infarction, diabetes, chronic obstructive pulmonary disease, seizure, and cerebrovascular accident) with and without DL-ECG analysis output value (DL-ECG index). We selected the best threshold for the model by maximizing the F1 metric on the validation set and used this threshold to report sensitivity and specificity on the test sets. Similarly, the threshold to report sensitivity and specificity for the conventional ECG electronic risk score and logistic regression models was also selected by maximizing the F1 metric. For each calculation, two-sided 95% confidence intervals (CI) were computed by bootstrapping randomly sampled 50% of the test set for 1,000 iterations. We performed statistical analyses using Python and R.

Footnote 1: https://github.com/google-research/

## Reporting summary

Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

Fig. 1: Description of internal and external cohorts. Study subject selection for the training dataset, validation dataset, testing dataset, and external validation. Afib atrial fibrillation, AFI. atrial flutter, ECG electrocardiography, SCD sudden cardiac death.

Fig. 2: Model development. Development of deep learning 12-lead ECG model showing input data, model architecture, validation and performance. ECG electrocardiography, SCD sudden cardiac death.

 

## Results

### Demographic and clinical findings

Our study sample consists of a total of 2,510 SCD cases: 1,796 SCD cases from the Oregon Sudden Unexpected Death Study (SUDS, Portland OR; training, validation, and testing) and 714 SCD cases from the geographically distinct Ventra Prediction of Sudden Death in Multi-ethnic Communities study (PRESTO, Ventura CA; external validation). In comparison to Oregon SUD SCD cases, Ventura PRESTO SCD cases were older (\(72.3\pm 14.2\) years vs. \(67.5\pm 14.9\) years) and more often female (41.3% vs. 35.4%). The prevalence of Hispanic ethnicity (30.7% vs. 2.4%) and Asian race (7.8% vs. 3.3%) was higher in Ventura PRESTO, while the prevalence of White (82.0% vs. 57.6%) and Black race (10.1% vs. 2.1%) was higher in Oregon SUDs. The prevalence of diabetes was 53.2% in Ventura PRESTO and 45.4% in Oregon SUDs. Previously diagnosed heart failure (31.1% vs. 39.8%) and history of myocardial infarction (MI) (27.5% vs. 38.4%) were lower in Ventura PRESTO compared to Oregon SUDs, respectively. The prevalence of COPD was similar (26.6% in Oregon SUDs vs. 22.3% in Ventura PRESTO).

In comparison to SCD cases, control subjects had a similar prevalence of previously diagnosed coronary artery disease (CAD) (51.2%) and MI (30.7%). However, control subjects were slightly younger (\(65.4\pm 11.6\) years) and had a somewhat lower prevalence of previously diagnosed diabetes (27.8%), atrial fibrillation (13.4%), heart failure (12.8%), and COPD (9.1%). Demographics and clinical characteristics of SCD cases and control subjects are presented in Table 1.

### DL model performance

In the internal testing dataset, the DL model achieved an AUROC of 0.889 (95% CI 0.861-0.917) in detecting SCD cases from controls. Sensitivity and specificity were 0.843 (0.809-0.878) and 0.818 (0.764-0.872), respectively.

In the external validation dataset, the DL model achieved a comparable AUROC of 0.820 (0.794-0.847) in detecting SCD cases. The sensitivity was 0.763 (0.733-0.796), while the specificity was 0.796 (0.753-0.838). Model performance metrics in internal and external cohorts are presented in Table 2 and AUROC curves in Fig. 3.

We evaluated the AUCs of models stratified by sex and age. The DL model performed similarly in men and women in the internal cohort (test for difference in AUCs across subgroups, \(p=0.36\)), and marginally better in the external cohort among men (AUC = 0.842, 95% CI 0.81-0.874) than among women (AUC = 0.775, 95% CI 0.718-0.831) (\(p=0.043\)). No differences were observed in model performance comparing age \(>\) 70 years vs. age \(\approx\) 70 years in the internal or external cohorts (\(p=0.56\) and \(p=0.16\), respectively).

### Conventional ECG electrical risk score performance

We compared the DL model's performance to a previously developed and validated 6-variable ECG electrical risk score that was independently associated with SCD\({}^{\text{th}}\). In the internal and external datasets, the ECG electrical risk score achieved AUROCs of 0.712 (0.668-0.756) and 0.743 (0.711-0.775) in detecting SCD cases from controls, respectively. The sensitivity was 0.779 (0.721-0.837) in the internal testing dataset and 0.569 (0.515-0.623) in the external validation cohort. The specificity was 0.506 (0.454-0.558) in the internal testing dataset and 0.802 (0.773-0.832) in the external validation cohort (Table 2 and Fig. 3).

### Logistic regression models

To evaluate the predictive power of DL-ECG index beyond conventional clinical SCD risk factors, we performed logistic regression analyses including clinical variables with and without DL-ECG index in the internal and external datasets. In the internal test dataset, addition of the DL-ECG index into clinical variables improved the discriminative value of SCD from an AUROC of 0.780 (0.741-0.818) to an AUROC of 0.919 (0.895-0.943). Similar results were obtained in the external test set, in which addition of the DL-ECG index into clinical variables improved the discriminative value of SCD from an AUROC of 0.806 (0.778-0.833) to an AUROC of 0.899 (0.878-0.920). Using a cut-point of 0.70 for predicting case status, the net redasfication improvement using the DL model and clinical variables compared to the model with clinical variables in the internal cohort was 28.7% (95% CI 21.0-36.5%) and in the external cohort was 15.3% (95% CI 9.7-20.9%). Regression model performance metrics in internal and external

\begin{table}
\begin{tabular}{l l l l l} \hline  & \multicolumn{2}{c}{**Internal cohort**} & \multicolumn{2}{c}{**External cohort**} \\  & \multicolumn{2}{c}{**SCD cases in Oregon**} & \multicolumn{2}{c}{**Control subjects (\(n=906\))**} & \multicolumn{2}{c}{**SCD cases in Ventura PRE-**} & \multicolumn{2}{c}{**Control subjects (\(n=329\))**} \\  & \multicolumn{2}{c}{**SUDS (\(n=1796\))**} & \multicolumn{2}{c}{**STO (\(n=714\))**} & \multicolumn{2}{c}{**STO (\(n=714\))**} \\ \hline Age. years & 67.5 \(\pm\) 14.9 & 65.3 \(\pm\) 11.6 & 72.3 \(\pm\) 14.2 & 65.7 \(\pm\) 11.7 \\ \hline Female sex, \(n\) (50) & 635/1796 (85.4%) & 327/996 (32.8%) & 295/714 (41.3%) & 98/329 (29.8%) \\ \hline Race/ethnicity, \(n\) (50) & & & & \\ \hline White & 1,448/1765 (82.0%) & 836/979 (85.4%) & 411/714 (57.6%) & 273/328 (83.2%) \\ \hline Black & 178/1765 (10.1%) & 105/979 (10.7%) & 15/714 (2.1%) & 33/28 (10.1%) \\ \hline Asian & 59/1765 (3.3%) & 15/979 (1.5%) & 56/714 (7.8%) & 4/328 (1.2%) \\ \hline Hispanic & 43/1765 (2.4%) & 13/979 (1.3%) & 219/714 (30.7%) & 11/328 (3.4%) \\ \hline Other & 37/1765 (2.1%) & 10/979 (1.0%) & 13/714 (1.8%) & 7/328 (2.1%) \\ \hline Prior medical history & & & & \\ \hline Coronary artery disease, \(n\) (50) & 850/1796 (47.3%) & 502/996 (50.4%) & 257/714 (36.0%) & 176/329 (53.5%) \\ \hline Diabetes, \(n\) (50) & 815/1795 (45.4%) & 282/984 (28.7%) & 380/714 (53.2%) & 87/328 (26.5%) \\ \hline History of MI, \(n\) (50) & 689/1796 (88.4%) & 302/996 (30.3%) & 196/714 (27.5%) & 105/329 (31.9%) \\ \hline Atrial fibrillation, \(n\) (50) & 428/1796 (23.8%) & 137/996 (13.8%) & 187/714 (26.2%) & 41/229 (12.5%) \\ \hline CVA, \(n\) (50) & 337/1795 (18.8%) & 83/984 (8.4%) & 120/714 (16.8%) & 18/628 (5.5%) \\ \hline Heart failure, \(n\) (50) & 714/1796 (98.9%) & 136/996 (13.7%) & 222/714 (31.1%) & 33/229 (10.0%) \\ \hline COPD, \(n\) (50) & 478/1795 (26.6%) & 89/84 (0.0%) & 159/714 (22.3%) & 31/228 (9.5%) \\ \hline Seizure, \(n\) (50) & 150/1795 (8.4%) & 25/984 (2.5%) & 36/714 (5.0%) & 7/328 (2.1%) \\ \hline Syncope, \(n\) (50) & 186/1795 (10.4%) & 50/984 (5.1%) & 78/714 (10.9%) & 11/328 (3.4%) \\ \hline \end{tabular}
\end{table}
Table 1: Demographic and clinical characteristics of the study subjects in the internal and external datasetscohorts are presented in Table 3 and AUROC curves in Fig. 4. Examples of Local Interpretable Model-agnostic Explanations (LIME) highlighted ECGs from two SCD cases and two controls from the external cohort are presented in the Supplementary Figure. LIME highlighted a wide range of ECG features including PR interval, QRS complex, and ST- and T-wave changes.

## Discussion

We utilized data from two large geographically distinct community-based out-of-hospital SCD cohorts to train, test, and validate a 12 lead ECG waveform-based DL model, which was compared to a previously validated conventional ECG model. The DL model achieved a higher accuracy with an AUROC of 0.889 for internal cohort and 0.820 for external validation, and outperformed the conventional ECG risk score. A slightly lower performance in the external cohort may be related to differences in demographics and clinical profiles, which may affect the accuracy of the model's prediction. However, despite such differences, the overall performance remained good in the external cohort. To our knowledge, this is the first report of an ECG-based DL model that has outperformed a conventional ECG risk model in predicting out-of-hospital SCD at the community level.

There are some unique aspects of study design that made this work feasible. SCD is a dynamic and unexpected event that requires prospective ascertainment1. Since annual incidence is in the range of 50-100/100,000deg, existing cohorts of 5000-10,000 subjects cannot yield sufficient numbers of SCD cases for viable analyses, especially those that employ deep learning models. Furthermore, we were able to include both survivors and non-survivors of SCD in our datasets, which avoids the bias of predicting only non-survivors or survivors. The establishment of the two population cohorts Oregon SUDS1 and Ventura RESTO1 consisting of -1.85 million US residents, provided sufficient numbers for deep learning. Equally important, both studies have been obtaining and archiving digitized 12 lead ECGs performed prior, and unrelated to SCD events. While this is a challenging process for the SCD phenotype, it is a pre-requisite for discovery of prediction models.

Footnote 1: https://github.com/ wearable device technology have enabled recording of the ECG beyond the healthcare environment, during activities of daily living.

As compared to a previously developed and validated 6 variable conventional ECG risk score, the DL model achieved significantly higher performance in detecting SCD cases, which supports the higher utility of DL-based models. In contrast to conventional risk calculators, DL models do not require manual feature selection and extraction but instead can utilize the entire digital signal to incorporate novel indices of risk. Consequently, ECG DL models are not biased in focusing on pre-specified ECG parameters and thus have the potential to achieve higher throughput and broader scope while preserving accuracy (Fig. 5). Another major advantage of DL techniques in comparison to conventional statistical tools is that they require making fewer assumptions about data structure. Hence, DL models can be more accurate for evaluation of complex nonlinear relationships in large datasets. However, DL techniques may also have some disadvantages which need to be considered during development, and also prior to deployment. These include model-specific requirements for inputting data, vulnerability to systemic bias and lack of the ability to explain mechanisms of findings which is still a work in progress.

SCD is a complex trait as well as a multifactorial event, and pathophysiology is based on the interplay between the underlying substrate and a variety of triggers. ECG abnormalities that have been associated with an increased risk of SCD are often surrogates of the underlying cardiac substrate (e.g, LVH, myocardial scarring, repolarization abnormality), and accurate risk stratification requires a combination of several nonspecific ECG abnormalities [11]. Even though ECG may reflect widespread cardiac and noncardiac conditions [12, 13, 14], the logistic regression model showed that DL-ECG index improved the discriminative value of SCD over clinical variables. Similar findings were found in a recent DL-ECG model among heart failure patients [15]. In comparison to conventional dichotomous analytical methods, deep learning-based ECG analysis may provide more precise and comprehensive quantification of ECG abnormalities and deeper phenotyping.

The vast majority of SCD cases are not identified as high risk prior to their mostly lethal event, which highlights the importance of extending SCD risk assessment beyond left ventricle ejection fraction. While the overall

Fig. 4: **Utility of deep learning ECG index beyond clinical risk predictors.** Receiver operating curves for the identification of sudden cardiac death cases in the internal (**a**, \(n=2792\)) and external cohort (**b**, \(n=1043\)) with logistic regression models. Clinical variables include age, sex, heart failure, coronary artery disease, myocardial infarction, diabetes, chronic obstructive pulmonary disease, seizure, and cerebrovascular accident.

\begin{table}
\begin{tabular}{l l l l l}  & **AUROC (85\% CI)** & **Sensitivity (85\% CI)** & **Specificity (85\% CI)** & **Maximum F1 Metric** \\ \hline Internal cohort (\(n=2.792\)) & & & & \\ \hline Clinical variables & 0.780 (0.741–0.818) & 0.773 (0.714–0.831) & 0.644 (0.595–0.694) & 0.639 \\ Clinical variables + Deep learning ECG index & 0.919 (0.895–0.943) & 0.763 (0.703–0.822) & 0.914 (0.885–0.943) & 0.794 \\ \hline External cohort (\(n=1.043\)) & & & & \\ \hline Clinical variables & 0.806 (0.778–0.833) & 0.777 (0.732–0.823) & 0.702 (0.668–0.735) & 0.641 \\ Clinical variables + Deep learning ECG index & 0.899 (0.878–0.920) & 0.808 (0.765–0.85) & 0.842 (0.815–0.869) & 0.751 \\ \hline \end{tabular}
\end{table}
Table 3: Performance of logistic regression models including clinical variables with and without deep learning ECG index in the internal and external datasets incidence of SCD in the community has remained relatively stable, the incidence of SCD in heart failure with reduced ejection fraction has decreased[4], suggesting that the use of LVEF < 35% in risk prediction is progressively less effective. An effective risk stratification would require both optimal screening population and accurate screening tools, which is likely to consist of a combination of several risk assessment modalities (e.g., ECG, imaging, omics, etc.). ECG abnormalities have already been included in recent SCD risk models[4], and usage of DL based ECG analysis as a pre-screening tool for identification of individuals who could be triaged for more comprehensive risk evaluation could prove effective in selected individuals. Due to the high proportion of CAD and prior MI without a history of ventricular arrhythmias, we think that the control subjects in the present study represent intermediate-risk patients, and given the increased baseline SCD risk, this patient group may represent a reasonable target for screening efforts. However, our study represents the first steps in ECG-DL based SCD risk assessment. As for all DL models that have the potential to be clinically useful, further prospective studies followed by randomized trials are needed to study if DL-based ECG analysis has the potential to provide an inexpensive, high throughput, and widely deployable pre-screening tool to augment current SCD risk stratification.

A strength of our study is a large sample of carefully adjudicated out-of-hospital SCD cases with prearrest resting 12 lead ECG. In addition, we were able to create balanced datasets by including clinically comparable control patients. However, some limitations should be considered while interpreting these findings. We matched cases and controls geographically in the training, validation, and internal testing datasets, but we had no geographically matched controls in external validation dataset. However, there was no overlap of control samples between the internal and external validation datasets. The necessity of using a large control group with digitized paper ECGs divided into two was driven by the goal of minimizing the differences in the quality of ECG recordings between cases and controls. The Oregon SUDS study was initiated in 2002 when only paper ECGs were made available, and all case and control ECGs were digitized before providing them to the DL-ECG model. Control ECGs were also obtained randomly from multiple community hospitals and health systems, which further reduces the likelihood of systemic bias in quality of ECG recordings. Since SCD is the first manifestation of heart disease in a substantial subgroup, a prearrest ECG was not available if individuals had not undergone a cardiac evaluation prior to their SCD event, creating potential for selection bias. Although we aimed to match cases and controls based on the underlying CAD status, some differences in other SCD risk factors remained between SCD cases and controls, which may have affected the model performance. However, some of these differences are important contributors to the development of SCD, and the prediction of SCD is based on the identification and combination of risk markers. We used a case-control study design to collect sufficient numbers of carefully adjudicated SCD cases, which does not allow us to reliably estimate the positive predictive value and negative predictive value. We used a relatively short 2.5 s ECG strip, and further studies are probably needed to investigate whether longer ECG strip usage will result in higher prediction accuracies. Our model is only applicable to sinus rhythm ECGs since atrial fibrillation/flutter and pac ECGs were excluded during algorithm development. Lastly, the majority of our study subjects were White, and further studies are needed to study ECG-DL performance in racially/ethnically distinct subgroups. Additionally, future prospective studies are needed to validate model performance in clinically diverse settings.

## Conclusions

We trained an ECG-based DL model that achieved high accuracy in distinguishing SCD cases from control patients. The model was successfully validated in a geographically distinct SCD cohort and outperformed a previously validated conventional ECG risk score. These results suggest that DL-based ECG analysis has advantages over conventional ECG based SCD risk assessment and yields better accuracy. Further detailed investigation is warranted to evaluate how the DL model could contribute to improved SCD risk stratification.

## Data availability

All analytical methods applied for the deep learning algorithm are included in this published article. Based on institutional review board guidance patient data is not publicly available and is de-identified. De-identified data is only available by contacting the corresponding author.

## Code availability

Code is available at https://github.com/ccg-net/scd-oregon[13]

Received: 27 May 2023; Accepted: 2 February 2024; Published online: 27 February 2024

## References

* [1] Tsao, C. W. et al. Heart disease and stroke statistics-2022 update: a report from the American Heart Association. _Circulation_**145**, e153-e639 (2022).
* [2] Empana, J. P. et al. Incidence of sudden cardiac death in the European union. _J. Am. Coll. Cardiol._**79**, 1818-1827 (2022).
* [3] Chugh, S. S. Disrupting the approach to sudden cardiac death: from vulnerable ejection fraction to vulnerable patient. _Circulation_**137**, 7-9 (2018).
* [4] Sabbag, A. et al. Contemporary rates of appropriate shock therapy in patients who receive implantable device therapy in a real-world

Fig. 5: **Summary of deep learning versus conventional ECG analysis.** Schematic illustration of the advantage of deep learning-based ECG analysis over conventional methods. LVH left ventricular hypertrophy, SCD sudden cardiac death.

 setting: from the Israeli ICD registry. _Heart Rhythm_. **12**, 2426-2433 (2015).
* [5] Kober, L. et al. Defibrilator implantation in patients with nonischemic systolic heart failure. _N. Engl. J. Med._**375**, 1221-1230 (2016).
* [6] Shen, L. et al. Declining disk of sudden death in heart failure. _N. Engl. J. Med._**377**, 41-51 (2017).
* [7] Stecker, E. C. et al. Population-based analysis of sudden cardiac death with and without left ventricular systolic dysfunction: two-year findings from theregon sudden unexpected death study. _J. Am. Coll. Cardiol._**47**, 1161-1166 (2006).
* [8] Chugh, S. S. et al. Prediction of sudden cardiac death manifesting With documented ventricular fibrillation or pulseless ventricular tachycardia. _JACC Clin. Electrophysiol._**8**, 411-423 (2022).
* [9] Narayanan, K. & Chugh, S. S. The 12-lead electrocardiogram and risk of sudden death: current utility and future prospects. _Europace_**17**, ii7-i13 (2015).
* [10] Aro, A. L. et al. Electrical risk score beyond the left ventricular ejection fraction: prediction of sudden cardiac death in the Oregon sudden unexpected death study and the atherosclerosis risk in communities study. _Eur. Heart J._**38**, 3017-3025 (2017).
* [11] Chatterjee, N. A. et al. Simple electrocardiogram measures improve sudden arrhythmia death prediction in coronary disease. _Eur. Heart J._**41**, 1988-1999 (2020).
* [12] Waks, J. W. et al. Global electric heterogeneity risk score for prediction of sudden cardiac death in the general population: the atherosclerosis risk in communities (ARIC) and Cardiovascular Health (CHS) studies. _Circulation_**133**, 2222-2234 (2016).
* [13] Attia, Z. I. et al. Prospective evaluation of smartwatch-enabled detection of left ventricular dysfunction. _Nat. Med._**28**, 2497-2503 (2022).
* [14] Attia, Z. I. et al. Screening for cardiac contractile dysfunction using an artificial intelligence-enabled electrocardiogram. _Nat. Med._**25**, 70-74 (2019).
* [15] Ko, W. Y. et al. Detection of hypertrophic cardiomyopathy using a convolutional neural network-enabled electrocardiogram. _J. Am. Coll. Cardiol_**75**, 722-733 (2020).
* [16] Attia, Z. I. et al. An artificial intelligence-enabled ECG algorithm for the identification of patients with atrial fibrillation during sinus rhythm: a retrospective analysis of outcome prediction. _Lancet_**394**, 861-867 (2019).
* [17] Chugh, S. S. et al. Current burden of sudden cardiac death: multiple source surveillance versus retrospective death certificate-based review in a large U.S. community. _J. Am. Coll. Cardiol._**44**, 1268-1275 (2004).
* [18] Reinier, K. et al. Evaluation of sudden cardiac arrest by race/ethnicity among residents of ventura county, California, 2015-2020. _JAMA Netw. Open_**4**, e2118537 (2021).
* [19] Baldini, F., Erdem, T., Zareba, W. & Moss, A. J. ECGScan: a method for conversion of paper electrocardiographic printouts to digital electrocardiographic files. _J. Electrocardiol._**38**, 310-318 (2005).
* [20] Ouyang, D. et al. Electrocardiographic deep learning for predicting post-procedural mortality: a model development and validation study. _Lancet Digt. Health_**6**, e70-e78 (2024).
* [21] Davis, C., Taft, G., Carroll, J., Wijesundera, D. N. & Beattie, W. S. The revised cardiac risk index in the new millennium: a single-centre prospective cohort re-evaluation of the original variables in 9,519 consecutive elective surgical patients. _Can. J. Anaesth_**60**, 855-863 (2013).
* [22] Ford, M. K., Beattie, W. S. & Wijesundera, D. N. Systematic review: prediction of perioperative cardiac complications and mortality by the revised cardiac risk index. _Ann. Intern. Med._**152**, 26-35 (2010).
* [23] Gupta, P. K. et al. Development and validation of a risk calculator for prediction of cardiac risk after surgery. _Circulation_**124**, 381-387 (2011).
* [24] Holmstrom, L. et al. Deep learning-based electrocardiographic screening for chronic kidney disease. _Commun. Med. (Lond)_**3**, 73 (2023).
* [25] Okada, D. R. et al. Substrate spatial complexity analysis for the prediction of ventricular arrhythmias in patients with ischemic cardiomyopathy. _Circ. Artythmiz. Electrophysiol._**13**, e007975 (2020).
* [26] Popescu, D. M. et al. Arrhythmic sudden death survival prediction using deep learning analysis of scarring in the heart. _Nat. Cardiovasc. Res._**1**, 334-343 (2022).
* [27] Rogers, A. J. et al. Machine learned cellular phenotypes in cardiomyopathy predict sudden death. _Circ Res._**128**, 172-184 (2021).
* [28] Wu, K. C. et al. Baseline and dynamic risk predictors of appropriate implantable cardiover defibrilator Therapy. _J. Am. Heart Assoc_**9**, e017002 (2020).
* [29] Attia, Z. I. et al. Age and sex estimation using artificial intelligence from standard 12-lead ECGs. _Circ. Artythm Electrophysiol._**12**, e007284 (2019).
* [30] Gallowary, C. D. et al. Development and validation of a deep-learning model to screen for hyperkendemia from the electrocardiogram. _JAMA Cardiol._**4**, 428-436 (2019).
* [31] Kwon, J. M. et al. A deep learning algorithm to detect anaemia with ECGs: a retrospective, multicentre study. _Lancet Digt. Health_**2**, e358-e367 (2020).
* [32] Shiraishi, Y. et al. Improved prediction of sudden cardiac death in patients with heart failure through digital processing of electrocardiography. _Europace._**3**, 922-930 (2023).
* [33] Chugh, S. S. Oregon SCD ECG Deep Learning. _Example Data for the VISIBLE Software Package_ (Zenodo, 2023).

## Acknowledgements

This work is funded, in part, the by National Institutes of Health, National Heart Lung and Blood Institute Grants R01HL145675 and R01HL147358 to SSC. SSC holds the Pauline and Harold Price Chair in Cardiac Electrophysiology at Cedars-Sinai. _It is a postdoctoral fellow visiting from the Research Unit of Internal Medicine, Medical Research Center_ _Oulu, University of Oulu and Oulu University Hospital, Oulu, Finland, and is funded by the Sigrid Juselius Foundation, the Finnish Cultural Foundation, the Instrumentarium Science Foundation, the Orion Research Foundation, and the Paavo Nurmi Foundation. The funding sources had no involvement in the preparation of this work or the decision to submit it for publication.

## Author contributions

Study design and conception: L.H., D.O., and S.S.C. Acquisition, analysis or interpretation of data: L.H., H.C., K.N., Z.B., M.S., A.U.-E., K.R., D.O., and S.S.C. Drafting of the manuscript: L.H., and S.S.C. Statistical analysis: H.C., K.R., D.O., and S.S.C. Critical revision of the manuscript for important intellectual content: L.H., H.C., K.N., Z.B., M.S., A.U.-E., K.R., D.O., and S.S.C. Administrative and material support: D.O., and S.S.C. Obtained funding: S.S.C. Supervision: S.S.C. Full access to the data: S.S.C. All authors reviewed and approved the final version of the manuscript.

## Competing interests

The authors declare the following competing interests: The deep learning techniques for predicting sudden cardiac death risk discussed in this manuscript relate to pending US provisional patent application 63/ 500,550 naming Cedars-Sinai Medical Center as the applicant and listing S.S.C and D.O. as the inventors. The remaining authors declare no competing interests.

 https://doi.org/10.1038/s43856-024-00451-9

## Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/10.1038/s43856-024-00451-9.

## Correspondence and requests for materials should be addressed to Sumset S. Chugh.

## Peer review information

_Communications Medicine_ thanks Patrick Boyle, Donchach O'Sullivan and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

## Reprints and permissions information

is available at http://www.nature.com/reprints

## Publisher's note

_Published claims in published maps and institutional affiliations._

## Open Access

This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

 