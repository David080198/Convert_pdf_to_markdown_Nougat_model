Reconstructing Mayotte 2018-19 Rift Valley Fever outbreak in humans by combining serological and surveillance data

Jonathan Bastard

1Santte publique France, French national public health agency, F-94415 Saint-Maurice, France. 2French Armed Forces Bormedical Research Institute, National Reference Laboratory for Arboviruses, Marseille, France. 3Unite des Virus Emergents (LVF: Aix-Marseille Univ-IRD 190-Inserm 1207), Marseille, France. 4Gropuement de Defense Santante 976, Coconi, Mayotte. 5Mathematical Modelling of Infectious Diseases Unit, Institut Pasteur, Universite Paris C rte, UMR2000, CNRS, Paris, France. 6Sorbonne Universite, INSERM, Institut Pierre Louis d'epidemologie et de Sarlet Publique (IPLESP, UMRS 1136), Paris, France. 8Formal: b4753@columbia.edu

Guillaume Andre Durand

23

Fanny Parenton

1Santte publique France, French national public health agency, F-94415 Saint-Maurice, France. 2French Armed Forces Bormedical Research Institute, National Reference Laboratory for Arboviruses, Marseille, France. 3Unite des Virus Emergents (LVF: Aix-Marseille Univ-IRD 190-Inserm 1207), Marseille, France. 4Gropuement de Defense Santante 976, Coconi, Mayotte. 5Mathematical Modelling of Infectious Diseases Unit, Institut Pasteur, Universite Paris C rte, UMR2000, CNRS, Paris, France. 6Sorbonne Universite, INSERM, Institut Pierre Louis d'epidemologie et de Sarlet Publique (IPLESP, UMRS 1136), Paris, France. 8Formal: b4753@columbia.edu

Youssouf Hassani

1Santte publique France, French national public health agency, F-94415 Saint-Maurice, France. 2French Armed Forces Bormedical Research Institute, National Reference Laboratory for Arboviruses, Marseille, France. 3Unite des Virus Emergents (LVF: Aix-Marseille Univ-IRD 190-Inserm 1207), Marseille, France. 4Gropuement de Defense Santante 976, Coconi, Mayotte. 5Mathematical Modelling of Infectious Diseases Unit, Institut Pasteur, Universite Paris C rte, UMR2000, CNRS, Paris, France. 6Sorbonne Universite, INSERM, Institut Pierre Louis d'epidemologie et de Sarlet Publique (IPLESP, UMRS 1136), Paris, France. 8Formal: b4753@columbia.edu

Laure Dommergues

4Gropuement de Defense Santante 976, Coconi, Mayotte. 5Mathematical Modelling of Infectious Diseases Unit, Institut Pasteur, Universite Paris C rte, UMR2000, CNRS, Paris, France. 6Sorbonne Universite, INSERM, Institut Pierre Louis d'epidemologie et de Sarlet Publique (IPLESP, UMRS 1136), Paris, France. 8Formal: b4753@columbia.edu

Juliette Paireau

5Mathematical Modelling of Infectious Diseases Unit, Institut Pasteur, Universite Paris C rte, UMR2000, CNRS, Paris, France. 6Sorbonne Universite, INSERM, Institut Pierre Louis d'epidemologie et de Sarlet Publique (IPLESP, UMRS 1136), Paris, France. 8Formal: b4753@columbia.edu

Nathanael Hoze

5Mathematical Modelling of Infectious Diseases Unit, Institut Pasteur, Universite Paris C rte, UMR2000, CNRS, Paris, France. 6Sorbonne Universite, INSERM, Institut Pierre Louis d'epidemologie et de Sarlet Publique (IPLESP, UMRS 1136), Paris, France. 8Formal: b4753@columbia.edu

Marc Ruello

6Santte publique France, French national public health agency, F-94415 Saint-Maurice, France. 7French Armed Forces Bormedical Research Institute, National Reference Laboratory for Arboviruses, Marseille, France. 3Unite des Virus Emergents (LVF: Aix-Marseille Univ-IRD 190-Inserm 1207), Marseille, France. 4Gropuement de Defense Santante 976, Coconi, Mayotte. 5Mathematical Modelling of Infectious Diseases Unit, Institut Pasteur, Universite Paris C rte, UMR2000, CNRS, Paris, France. 6Sorbonne Universite, INSERM, Institut Pierre Louis d'epidemologie et de Sarlet Publique (IPLESP, UMRS 1136), Paris, France. 8Formal: b4753@columbia.edu

Gilda Grard

23Rept. of Physics of Medicine, University of Chicago 

# RVF surveillance system in humans

Rift Valley Fever (RVF) is a viral mosquito-borne disease affecting both food-producing animals and humans, reported in most parts of Africa and the Arabian Peninsula. In some regions, the enzootic reservoir of Rift Valley Fever virus (RVFV) may consist of domestic or wild animals1,2. Following particular environmental conditions (such as heavy rains) and/or introduction to new geographical areas, the virus can then cause large epizootics in food-producing animals, especially ruminants, and may result to numerous spill-over human cases (of all ages) infected by animals via mosquito bites, contacts with infected animals or animal products, or aerosols2,3,4,5. Estimating the burden of RVF epidemics in animals and humans is important to improve disease surveillance and control.

[MISSING_PAGE_POST]

Footnote 14: https://www

**Statistics and reproducibility**

_Model_. We developed a model to estimate RVFV attack rate and IgG seroprevalence in humans aged over 15 years old, during the course of 2018-2019 Mayotte outbreak, in two subpopulations i, determined by their place of residence (Central or Outer Communes) [29].

First, we modelled the epidemic curve using a lognormal function \(\mathrm{F_{i}(t)}\), defined as the weekly number of incident human infections (both reported and unreported to the surveillance system) in subpopulation i on week \(t\):

\[F_{i}(t)=\frac{p_{1,i}}{t.\sqrt{2.\pi.p_{3,i}}}e^{\frac{-\log(\pi t-p_{2,i})^{2 }}{2p_{3,i}}}\] (1)

where \(t\) represents weekly time steps from week 2018-41 (October 2018) to week 2019-40 (October 2019). \(\mathrm{p_{1,i}}\) corresponds to the total number of people infected during the outbreak in subpopulation i. \(\mathrm{p_{2,i}}\) and \(\mathrm{p_{3,i}}\) determine the shape of the epidemic curve including its duration, its starting date (i.e. the week \(t\) for which \(\mathrm{F_{i}(t)\geq 1}\)) and the date of its peak (i.e. the mode of the distribution). The three parameters were estimated from the data (Table 1).

Second, I(t) was the number of infections on week \(t\) in subpopulation i that were detected by surveillance (reported cases). I(t) was assumed to follow a binomial distribution:

\[I_{i}(t)\sim Bin(\tau,F_{i}(t))\] (2)

where \(\tau\) was estimated from the data and represents the reporting fraction, i.e. the proportion of overall human infections that were reported to the surveillance system (Table 1). \(\tau\) was assumed to be constant over the course of the epidemic and similar in all subpopulations. Because both RVFV incubation time [2, 7, 8] and viremia [2, 31, 32, 33, 34] are less than a week, we considered that the week of infection was the week of symptoms onset reported in the

Figure 1: **RVF data collected between week 2018-47 (November 2018) and week 2019-30 July 2019) in people aged over 15 years old. A Number of reported human cases by week from the surveillance system, and (B) number of blood samples collected by week as part of Unono Wa Moore survey. Light blue represents data collected from people living in the Outer communes of Mayotte Island, and dark blue in the Central communes, as depicted on the map at the top-right corner (see Supplementary Note 1 for details). For reported cases (A), we represent the week of symptoms onset or, if missing, the week of RT-PCR confirmation. For the seroprevalence study (B), we represent the week of sampling. Geographical information was missing for six reported cases aged over 15 years old.**surveillance data or, when missing, the week of RT-PCR confirmation.

Third, we modelled S\({}_{i}\)(t), the RVFV IgG seroprevalence over time:

\[S_{i}(t)=S_{0,i}+\frac{\sum_{m=1}^{t-D}F_{i}(w)}{N_{i}}\] (3)

where S\({}_{0,i}\) was IgG seroprevalence in subpopulation i prior to the outbreak, D was the delay between the infection of an individual and the detectability of IgG antibodies in their blood, and N\({}_{i}\) the subpopulation size. Here, S\({}_{0,i}\) and D were estimated from the data as well (Table 1).

Finally, the weekly number of IgG positive samples in subpopulation i, p\({}_{i}\)(t), was modelled as:

\[P_{i}(t)\sim Bin(S_{i}(t),T_{i}(t))\] (4)

with T\({}_{i}\)(t) being the number of individuals sampled on week \(t\) in subpopulation i.

_Model fitting._ The model was fitted to the case count data and serological data using a Markov Chain Monte Carlo (MCMC) algorithm, implemented with R version 4.0.3 and _rjags_ package [35]. The log-likelihoods of the "number of reported cases" and "number of IgG positive samples" components of the model for all weeks and for both geographical areas were summed together. Three chains were run for 200,000 iterations each, and every 200th value was sampled. For each chain, a burn-in of 150 samples was removed, as it was enough to allow the convergence of Markov chains. The effective sample size was at least 2340 for all parameters. Autocorrelation in the Markov chains was checked. The Gelman-Rubin statistic was below 1.2 for all parameters.

Estimated parameters are summarized in Table 1. We used non informative priors for most parameters (Fig. 2 and Supplementary Table S1). The prior of p\({}_{2,i}\) was set in order to search the mode of F\({}_{1}\) lognormal distribution (i.e. the true epidemic peak) between week 2018-50 (i.e. \(t=10\), December 2018) and week 2019-18 (i.e. \(t=30\), May 2019). This is why its prior distribution was uniform between p\({}_{3,i}+\log(10)\) and p\({}_{3,i}+\log(30)\). Moreover, P\({}_{1,i}\), the total number of people in subpopulation i infected over the course of the outbreak could not exceed N\({}_{o}\) the size of this subpopulation (Supplementary Table S1).

We then simulated the fitted model by computing 5000 repetitions, each of them using a different set of parameters randomly selected from the posterior chains.

_Sensitivity analyses._ We performed additional independent analyses to assess the sensitivity of our results to assumptions. First, we applied the method to the whole island data without geographical stratification, instead of differentiating Central and Outer communes in the main analysis. Second, we ran the stratified analysis by considering that, in the serological data, samples were IgG positive when the OD ratio was >2.5, rather than >3 in the main analysis.

**Reporting summary.** Further information on research design is available in the Nature Portfolio Reporting Summary linked to this article.

**Cases reported to the surveillance system**. As previously described [16, 20], a RVF outbreak was declared in Mayotte with a total of 143 human cases reported between week 2018-47 (November 2018) and week 2019-30 (July 2019), including 137 who were \(\geq\)15 years old. The epidemic peaked early February 2019 (on week 2019-06) with 20 reported human cases (Fig. 1 and Supplementary Data 1). Geographical information was missing for 6 reported cases aged \(\geq\)15 years old.

**Serological data.** Mayotte seroprevalence survey was led in humans from week 2018-49 (December 2018) to week 2019-21 (May 2019) (Fig. 1). The distribution of the values of OD ratio obtained from the 2853 collected sera is displayed in Supplementary Fig. S1, suggesting that the cut-off of 3 correctly discriminated positive and negative samples. Using this cut-off, 254 out of 2854 samples were RVFV IgG positive. The positivity of samples depended on the timing of their collection, with a lower positivity around the beginning of the outbreak (Fig. 3 and Supplementary Data 1), hence justifying the need for a model reconstructing the temporal evolution of RVF seroprevalence and attack rate in humans. Indeed, in Central communes (resp. Outer communes), the observed IgG seroprevalence was 8.4% (19/225) (resp. 2.9% (2/69)) in the first three weeks of sampling compared to 12.2% (25/205) (resp. 8.2% (19/233)) in the last three analyzed weeks of sampling (Supplementary Data 1). Among sampling weeks included in the analysis, the maximum observed seroprevalence was 17.5% (11/63) on week 2019-14 (April 2019) in Central communes and 19.5% (8/41) on week 2019-08 (February 2019) in Outer communes.

**Estimates of seroprevalence, attack rate and reporting fraction.** Our model succeeded in fitting both case count data and seroprevalence data for each subpopulation, as most of the observed data were in the model 95% prediction intervals (Fig. 3B, C, E, F).

\begin{table}
\begin{tabular}{l l l l}
**Parameter** & **Description** & **Unit** & **Value** \\ \hline p\({}_{1,i}\) & Number of people over 15 years old in subpopulation i infected during the outbreak (parameter of F\({}_{i}\) lognormal distribution) & - & Estimated \\ p\({}_{2,i}\) & Parameter of F\({}_{i}\) lognormal distribution (determines the shape of the epidemic curve) & - & Estimated \\ p\({}_{3,i}\) & Parameter of F\({}_{i}\) lognormal distribution (determines the shape of the epidemic curve) & - & Estimated \\ r\({}_{1}\) & Reporting fraction & - & Estimated \\ S\({}_{0,i}\) & IgG seroprevalence in subpopulation i before the outbreak & - & Estimated \\ D\({}_{1}\) & Time between infection and IgG detectability & Weeks & Estimated \\ N\({}_{\text{Moyotte}}\) & Number of people over 15 years old living in Mayotte & - & 144,2621 [FOOTNOTE:1]Footnote 1: \(\text{Moyotte}\) denotes We estimated that a total of 10,797 people over 15 years old (95% Credible Interval, CrI: 4,728-16,127) were infected by RVFV in Mayotte during 2018-2019 epidemic. This represented 7.5% (3.3%-11.2%) of the total population of this age. The reporting fraction during the outbreak was estimated at 1.2% (0.67%-2.2%). Furthermore, Central and Outer communes were similarly affected overall, with 6.8% (3.2%-10.9%) and 8.1% (3.4%-12.2%) of their population over 15 years old infected, respectively (Fig. 2 and Supplementary Table S2).

The estimated IgG seroprevalence increased from 5.5% (3.6%-7.7%) before the outbreak to 12.9% (10.4%-16.3%) thereafter, for the whole island. Split by place of residence, we estimated an increase of the estimated IgG seroprevalence from 7.2% (4.9%-9.7%) to 13.9% (11.3%-17.3%) in Central communes, and from 4.0% (1.8%-6.4%) to 12.0% (8.5%-15.5%) in Outer communes.

We also estimated a delay of 1 week (0-4 weeks) between infection and the detectability of IgG antibodies in humans (Fig. 2 and Supplementary Table S2).

When simulating the model using posterior estimates of parameters (Fig. 3), the peak in human infections--both reported and unreported to the surveillance system--was predicted to occur on median on week 2019-06 in Central communes and on week 2019-07 in Outer communes (February 2019 in both areas).

**Sensitivity analyses.** In both sensitivity analyses, we obtained estimates similar to the baseline analysis, as detailed in Supplementary Notes 2, 3. In particular, the reporting fraction was estimated to 1.3% (0.70%-2.4%) and 1.2% (0.66%-2.2%) in the analyses using unstratified data and using a different serological cut-off, respectively.

## Discussion

In this analysis, we fitted a model to both serological and surveillance data collected during the 2018-2019 RVF outbreak in Mayotte, which allowed us to estimate key parameters of the epidemic.

We estimated that 10,797 persons (aged over 15 years) were infected by RVFV throughout the 2018-2019 outbreak in Mayotte. This represented 7.5% of the population of this age on the island. However, only an estimated 1.2% of these infections were reported, despite the presence of a syndromic surveillance system on the island. This suggests that a large part of human cases were not diagnosed, although our study cannot determine whether the reason was because they presented no or mild symptoms, because they did not reach medical care while symptomatic, or both. Consistently with the first hypothesis, the proportion of RVFV infected humans with no or mild symptoms is generally considered to be >90%[38, 3]. In the future, including a question about recent illness in seroprevalence surveys may help to disentangle the factors of under-reporting. Furthermore, strengthening surveillance at the interface between animal and human health sectors might allow to increase the reporting fraction and to detect potential incursions of RVFV in the island as early as possible, in order to implement control measures in a cost-effective way if needed[16, 1].

The estimated IgG seroprevalence in people of Mayotte was 5.5% (95% CrI 3.6%-7.7%) just before the outbreak, as compared to the 3.5% (2.6%-4.8%) found in 2011[15]. Although we cannot rule out a small number of cryptic RVFV infections in humans may have occurred[36, 37], this result suggests that the circulation of the virus was negligible on the island between these dates. Moreover, no human RVF case was confirmed on the island between 2011 and 2018, and RVFV IgG seroprevalence in ruminants of Mayotte decreased continuously between 2011 and early 2018[38]. The small difference between the 2011 and the present studies may be due to difference in the sampled populations: contrary to our study, 5-14 years old were included in the 2011 survey and had a seroprevalence of 0.4%[15].

After the outbreak, in 2019, RVFV IgG seroprevalence in humans was estimated at 12.9% (10.4%-16.3%). This result is consistent with a recent review which reported that, across published seroprevalence studies, 12.6% of samples collected in

Fig. 2: Prior (light blue) and posterior (dark blue) distributions of the model’s parameters estimated by the Markov Chain Monte Carlo algorithm. For each parameter, dashed vertical lines represent the posterior 95% credible interval (highest posterior density interval).

 humans in the year following a RVF outbreak were positive for RVFV antibodies3. Even assuming IgG antibodies confer long-term protection against infection, this proportion would not prevent a hypothetical large outbreak of RVF in people of Mayotte in the future.

The estimated pre-epidemic seroprevalence was higher in Central (7.2%) than in Outer communes (4.0%), reflecting a higher exposure to RVFV in the past for people living in this area. This may be explained by an average higher proximity of these people to infected livestock animals in the past. Indeed, direct

Fig. 3: **Time course of the RVF outbreak in humans.** Predicted number of weekly incident human infections, reported or unreported to the surveillance system (**A**, **D**), number of incident human infections reported to the surveillance system (**B**, **E**), and IgG seroprevalence in humans (**C**, **F**), in the population over 15 years old. **A-C** Represent Central Communes while **D–F** represent Outer Commumes of Mayotte. Lines (solid and dashed) are model predictions (median and 95% prediction interval respectively, 5000 repetitions of the model). Dots are observed data (number of reported cases (**B**, **E**) and proportion of IgG seropositive tests (**C**, **F**)). Vertical bars (**C** and **F**) are 95% confidence interval for the proportion (Clopper-Pearson method). Serological data from week 2019-18 (early May 2019) onwards were not used for model fitting, because the representativeness of the sampled population was compromised (see Methods). In **C** and **F**, for visualization purposes, the \(Y\)-axis is cut between 40 and 80.

 contacts [15] and a closer spatial proximity [30] with food-producing animals have been identified as increasing the risk of infection. However, the proportion of people infected during the 2018-2019 outbreak was overall similar in both areas, probably as a result of the wide spread of RVFV among livestock populations of the whole island. Yet, the peak of human infections in Central communes was determined to occur 1 week ahead that in Outer communes, possibly reflecting the timing of the diffusion of RVFV in livestock, globally affecting Central before Outer communes [30].

In Outer communes, despite large confidence intervals, weekly seroprevalence data seemed to show a decrease starting on week 2019-08 (February 2019), which might be attributable to reducing levels of RVFV [rgb]0.999969, in people that were infected earlier in the outbreak. Nevertheless, no comparable decreasing trend was observed in Central communes, and the sensitivity analysis performed with a lower serological cut-off did not result in different model estimates. In addition, IgG antibodies are generally considered to persist for several years [31, 39], which makes their decline during the time of our study unlikely.

We estimated the period between infection by RVFV and the detectability of IgG antibodies to be 1 week, although with a wide 95% credible interval (0-4 weeks). We may have under-estimated this duration, since we considered that the week of infection was the week of symptoms onset (or, when missing, the week of RT-PCR confirmation) in reported cases. However, this under-estimation is probably \(<\)1 week, as much as RVFV incubation [2, 7, 8] and vireni [31, 32, 33, 34]. Furthermore, our estimation is in line with the range of values reported by Ref. [2, 7, 23, 24, 25], giving weight to our results.

This study has some limitations. First, some variables such as the age, gender, place of birth or occupational contacts with livestock were not accounted for in the analysis. The reason is some of these data were not collected as part of the cases reporting (for the place of birth) or serodology survey (for the occupational contacts with livestock) datasets. Moreover, in a previous survey led in Mayotte in 2011 [15], RVFV seroprevalence was not significantly associated with the age (after 15 years old) and gender.

Second, our modelling study did not include animal data. Indeed, rather than mechanistically simulating RVFV spill-over from animals to humans as in [16], our objective was to combine two independent sources of data to assess the extent of 2018-2019 RVF outbreak in humans. Consequently, our model did not explore the mechanisms that led to a decreased number of human cases. Yet, a previous publication [16] showed the epidemic fade out very likely resulted from the depletion of susceptible animals by natural infection, thus reducing the spill-over to humans. In the future, our results will be useful to parameterize such mechanistic models.

Third, we assumed that the reporting fraction was constant over time, although it might have varied throughout the course of the outbreak. However, the testing of all patients with dengue-like symptoms and negative to other infections (described above) has been implemented since 2008, and it is reasonable to suppose that the surveillance system had a steady capacity to detect RVF cases who sought medical care.

Fourth, we made the assumption that the IgG detection technique in serum had a sensitivity and a specificity of 1. If the sensitivity was \(<\)1 and the specificity was unchanged, the estimated outbreak's attack rate would be higher, and therefore the reporting fraction would be lower. On the other hand, the specificity of 1 is justified by the fact no other phleovirus is known to circulate in this geographical area, preventing serological cross-reactivity with other viruses.

To conclude, combining incidence and seroprevalence data into a model, we estimated pre- and post-outbreak seroprevalence levels and reconstructed the true attack rate. This allowed us to provide the first estimate of RVF case reporting fraction during an epidemic, a key epidemiological parameter [40] which has rarely been assessed for other important infectious diseases [41, 42, 43].

### Data availability

The source data for Fig. 1 is in Supplementary Data 1.

### Code availability

Analyses were performed using R version 4.2.0. The code reproducing this article is available from https://doi.org/10.5281/zenodo.73435664.

Received: 15 June 2022; Accepted: 12 December 2022; Published online: 21 December 2022

## References

* [1] Tennant, W. S. D. et al. Modelling the persistence and control of Rift Valley fever virus in a spatially heterogeneous landscape. Nat. Commun.12, 5593 (2021).
* [2] Bird, B. H., Kisazek, T. G., Nichol, S. T., & MacLaChlan, N. J. Ritt Valley fever virus. J. Am. Ver. Med. Assoc.234, 883-893 (2009).
* [3] Broen, G. M. et al. Over 100 years of Rift Valley fever: a patchwork of data on pathogen spread and spillover. _Pathoscal Swift. Pathoscal Swift._**10**, 708 (2021).
* [4] WHO WHO _Rept Street on Rift Valley Fever_. https://www.who.int/news-room/fact-sheets/detail/irl-valley fever (2018).
* Une fumble de flevre de la Valle de Rift enrique etreiteite, 1997-1998. Wylb. _Epidenol. Rec. Rolev Epidemiologic Height._**73**, 105-109 (1998).
* [6] Peyre, M. et al. A systematic scoping study of the socio-economic impact of Rift valley fever: research gaps and needs. _Exomoues Public Health_**62**, 309-325 (2015).
* [7] van Leeuwen, L. P. M. et al. Exotic viral hepatitis a review on epidemiology, pathogenesis, and treatment. _J. Hepatol._**77**, 1431-1443 (2022).
* [8] CDC. _Signs and Symptoms--Rift Valley Fever_. https://www.cdc.gov/vrh/rrf/ symptom/index.html (2020).
* [9] Ikegami, T. & Makino, S. The pathogenesis of Rift Valley fever. _Viruses_**3**, 493-519 (2011).
* [10] Henderson, A. D. et al. Interactions between timing and transmissibility explain diverse fluvivviv dynamics in Fiji. _Nat. Commun._**12**, 1671 (2021).
* [11] Cauchemez, S., Hose, N., Cousian, A. & Nikolay, B. S. ten bosch, Q. How modelling can enhance the analysis of imperfect epidemic data. _Trends Parasit_**35**, 369-379 (2019).
* [12] Dellagi, K. et al. Serological evidence of contrasted exposure to Arboviral infections between islands of the Union of Comoros (Indian Ocean). _PLoS Nspf. Trop. Dis._**10**, e0004840 (2016).
* [13] Alhaji, N. B. et al. Seropositivity and associated intrinsic and extrinsic factors for Rift Valley fever virus occurrence in pattoral herds of Nigeria: a cross sectional survey. _BMC Ver. Res._**16**, 243 (2020).
* [14] Cook, E. A. J. et al. The zero-epidemiology of Rift Valley fever in people in the Lake Victoria Basin of western Kenya. _PLoS Nspf. Trop. Dis._**11**, e0005731 (2017).
* [15] Lernout, T. et al. Rift Valley fever in humans and animals in Mayotte, an Endemic situation. _PLoS One_**6**, e7492 (2013).
* [16] Metras, R. et al. Estimation of Rift Valley fever virus spillover to humans during the Mayotte 2018-2019 epidemic. _Proc. Natl. Acad. Sci._**117**, 24567-24574 (2020).
* [17] Olive, M.-M. et al. Reconstruction of Rift Valley fever transmission dynamics in Madagascar: estimation of force of infection from seroprevalence surveys using Bayesian modelling. _Sci. Rep._**7**, 39870 (2017).
* [18] INSEE. _Reconsument de la population de Mayotte et al._**2017**. https://www.insee.fr/statistics/3284395?seminate=149939393 (2019).
* [19] Metras, R. et al. The Epidemiology of Rift Valley fever in Mayotte insights and perspectives from 11 years of data. _PLoS Nspf. Trop. Dis._**10**, e0004783 (2016).
* [20] Youssouf, H. et al. Rift Valley fever outbreak, Mayotte, France, 2018-2019.
* [21]_Emerg. Infect. Dis._**26**, 769-772 (2020).

 * [21] Ruello, M. & Richard, J. _Ezquiete de sant & Mayotte 2019\(-\)Umono Wa Moore. Methode_ (Sante publique France, 2022).
* [22] INSE. _Register of Localized Buildings_. https://www.inse.fr/en/metadonness/definition/i/e1815 (2019).
* [23] Williams, R. et al. Validation of an lg/att antibody capture ELISA based on a recombinant nucleoprotein for identification of domestic ruminants infected with Rift Valley fever virus. _J. Virol. Methods_**177**, 140-146 (2011).
* [24] Paweska, J. T., Burt, F. J. & Searnepol, R. Validation of lg/g-sandwich and IgM-capture ELISA for the detection of antibody to Rift Valley fever virus in humans. _J. Virol. Methods_**124**, 173-181 (2005).
* [25] Maurice, A. et al. Rift valley fever viral load correlates with the human inflammatory response and coagulation pathway abnormalities in humans with hemorrhagic manifestations. _PLoS Nsp. Trop. Dis._**21**, e000646 (2018).
* [26] Drnis, J. et al. High specificity and sensitivity of Zika EDII-based ELISA diagnosis highlighted by a large human reference panel. _PLoS Nsp. Trop. Dis._**13**, e000747 (2019).
* [27] Peyrthet, C. N. et al. _Dengue Type 3 Virus, Saint Martin_, 2003-2004. Energ. Infect. Dis._**11**, 75-71 (2005).
* [28] Tong, C. et al. Tracking Rift Valley fever: from Mali to Europe and other countries, 2016. _EuroSurvillance_**24**, 1800213 (2019).
* [29] Kim, Y. et al. Livestock trade network: potential for disease transmission and implications for risk-based surveillance on the island of Mayotte. _Sci. Rep._**8**, 11550 (2018).
* [30] Kim, Y. et al. The role of livestock movements in the spread of Rift Valley fever virus in animals and humans in Mayotte, 2018-19. _PLoS Nsp. Trop. Dis._**15**, e0009202 (2021).
* [31] Mansfield, K. L. et al. Rift Valley fever virus: a review of diagnosis and vaccination, and implications for emergence in Europe. _Vaccine_**33**, 5520-5531 (2015).
* [32] Wilson, W. C. et al. Experimental infection of Calves by two Genetically-distinct strains of Rift Valley fever virus. _Viruses_**8**, 145 (2016).
* [33] Drolet, B. S. et al. Development and evaluation of one-step RT-PCR and immunohistochemical methods for detection of Rift Valley fever virus in biosafety level 2 diagnostic laboratories. _J. Virol. Methods_**179**, 373-382 (2012).
* [34] Nakland, J. et al. Kinetics of Rift Valley Fever Virus in experimentally infected mice using quantitative real-time RT-PCR. _J. Virol. Methods_**151**, 277-282 (2008).
* [35] Plummer, M., Stukalov, A., Demwood, M. & Plummer, M. M. _Praudage 'jrqs' (Vienna Astron., 2016)._
* [36] Sunaye, R. D. et al. Inter-epidemic Acquisition of Rift Valley Fever Virus in humans in Tanzania. _PLoS Nsp. Trop. Dis._**9**, e000356 (2015).
* [37] Paweska, J. T. et al. Rift Valley fever virus seroprevalence among humans, Northern KouZulu-Natal Province, South Africa, 2018-2019. _Energ. Infect. Dis._**27**, 107 (2021).
* [38] Nielsen, S. S. et al. Rift Valley Fever: risk of persistence, spread and impact in Mayotte (France). _FESA J_**18**, 406093 (2020).
* [39] CDC. Diagnosis-Rf/ _Valley Fever_. https://www.cdc.gov/th/rvf/diagnosis/indexhtml (2020).
* [40] Shoemaker, T. R. et al. Impact of enhanced viral haemorrhagic fever surveillance on outbreak detection and response in Uganda. _Lancet Infect. Dis._**18**, 373-375 (2018).
* [41] Pullano, G. et al. Undredetection of cases of COVID-19 in France threatens epidemic control. _Nature_**590**, 13-193 (2021).
* [42] Fraser, C. et al. Pandemic potential of a strain of influenza A (H1N1): early findings. _Science_**324**, 1557-1561 (2009).
* [43] Barber, R. M. et al. Estimating global, regional, and national daily and cumulative infections with SARS-CoV-2: through Nov 14, 2021: a statistical analysis. _Lancet_https://doi.org/10.1016/S0140-736(22)0484-6 (2022).
* [44] JonathanBass. _JordanbanBas/RVF_Mayotte: Myotte RVF Outbreak_. https://doi.org/10.5281/zenodo.7343566 (Zenodo, 2022).

## Acknowledgements

We are thankful to Marien Faury, Jean-Burgste Richard, Jean-Louis Solt, Laurent Filbel, Deibine Jezewski-Serra and Julie Chesneau for participating in Un Unon Wa Moore project conception, to the "URPS Informers Ocean Indian" for conducting blood samplings, and to Marie-Claire Paty and Henriette de Valk for their proofreading. This work was funded by internal resources of Santle Publique France.

## Author contributions

J.B. performed the modeling analysis with inputs from L.D., J.P., N.M., R.M. and H.N. and wrote the first version of the manuscript. G.A.D., and G.G. conducted the serological analysis of blood samples. F.P., Y.H. and H.N. were involved in the collection of the surveillance data in humans, and M.R. in the design of Unon Wa Moore survey. H.N. supervised the greedy. All authors discussed the analysis and revised the manuscript.

## Competing interests

The authors declare the following competing interest: Raphaile Mitras is an Editorial Board Member for Communications Medicine, but was not involved in the editorial review or peer review, nor in the decision to publish this article. The other authors declare no competing interests.

## Additional information

Supplementary informationThe online version contains supplementary material available at https://doi.org/10.1038/s43856-022-00230-4.

**Correspondence** and requests for materials should be addressed to Jonathan Bastard.

**Peer review information**_Communications Mathematiches_ thanks Alsadir Henderson and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available.

**Reprints and permission information** is available at http://www.nature.com/reprints

**Publisher's note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Appendix A Open Access

This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate it changes here made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by tautory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creatvcommons.org/licenses/by/4.0/.

 