

# Developments in cluster randomized trials and

_Statistics in Medicine_

M. J. Campbell

1Medical Statistics Group, School of Health and Related Research, University of Sheffield, Sheffield, U.K.

2Department of Epidemiology and Biostatistics, University of Western Ontario, Canada

3Robarts Clinical Trials, Robarts Research Institute, London, Canada

A. Donner

3Robarts Clinical Trials, Robarts Research Institute, London, Canada

N. Klar

2Department of Epidemiology and Biostatistics, University of Western Ontario, Canada

3Robarts Clinical Trials, Robarts Research Institute, London, Canada

###### Abstract

The design and analysis of cluster randomized trials has been a recurrent theme in _Statistics in Medicine_ since the early volumes. In celebration of 25 years of _Statistics in Medicine_, this paper reviews recent developments, particularly those that featured in the journal. Issues in design such as sample size calculations, matched paired designs, cohort _versus_ cross-sectional designs, and practical design problems are covered. Developments in analysis include modification of robust methods to cope with small numbers of clusters, generalized estimation equations, population averaged and cluster specific models. Finally, issues on presenting data, some other clustering issues and the general problem of evaluating complex interventions are briefly mentioned. Copyright \(\copyright\) 2006 John Wiley & Sons, Ltd.

cluster randomized trial; matched pair design; generalized estimating equations; population averaged models; cluster specific models; Consort statement

## 1 Introduction

Trials where groups of subjects, rather than individuals, are randomized, commonly called cluster randomized or group randomized trials are a common theme in _Statistics in Medicine_, with a special issue [1] devoted to this topic and many important developments chronicled. In celebration of 25 years of _Statistics in Medicine_, this paper will review developments in cluster randomized trials, particularly, but not exclusively, those published in the journal.

Cluster randomized trials are now a key tool in the evaluation of interventions in health services research. They are widely used and two main types of trial are as follows: (1) interventions that involve training or education of health professionals, with the aim of finding a benefit for patients; (2) community randomized trials where the clusters are complete communities (some authors call these 'large field trials'). These are generally characterized by a relatively small number of clusters each enrolling a large number of subjects. A well-known example of this is the COMMIT smoking intervention trial to be discussed in Section 3.

It is worth defining a few terms first. The _intraclass correlation (ICC)_ is the ratio of the between cluster variance to the total variance of an outcome variable and is often denoted by \(\rho\). Different designs can lead to different formulas for estimating \(\rho\). The _design effect (DE)_ is the ratio of the variance of an outcome measure when clustering is accounted for to the variance of the outcome measure when clustering is not accounted for. It is often referred to as the _variance inflation factor_, since DE measures the amount that one should increase a variance estimate obtained by ignoring clustering to allow for the clustering effect. For clusters of equal size \(m\), it can be shown that \(\mbox{DE}\!=\!1+(m-1)\rho\). Extensions of this formula to the case of variable cluster sizes are given in Section 2.4.

There have been a number of reviews of cluster randomized trials. In 2001 and in _Statistics in Medicine_, Klar and Donner [2], following on from their book [3] published the previous year, reviewed developments up until that time and suggested areas of further research. These areas included: ethical issues; sample size estimation; analytic issues; economic analysis; meta-analysis of cluster randomized trials and recommendations for trial reporting. The analytic issues included population averaged _versus_ cluster specific (CS) models, methods involving a small number of clusters, issues arising from matched paired designs, overlapping cluster membership, and issues involving missing data. Some related issues were also covered more recently by the same authors [4]. Methodological developments for cluster randomized trials have also been reviewed by Murray _et al._[5]. This paper will update the earlier reviews, in particular the 2001 review in _Statistics in Medicine_.

This paper is structured as follows. Sections 2-4 concern design issues: Section 2 presents issues concerning power and sample size, Section 3 matched pair designs and Section 4 cohort _versus_ cross-sectional designs. In Section 5 we will discuss issues in the analysis of cluster randomized trials. Section 6 describes issues on presentation and reporting and Section 7 deals with some further issues.

## 2 Issues arising in the assessment of power and sample size

### Number of clusters and number of subjects per cluster

Often the number of clusters available to be enrolled in a cluster randomized trial is limited. This has led to considerable interest in developing reliable methods of sample size estimation. Two early papers in _Statistics in Medicine_ reviewed sample size issues in clinical trials in general [6] and particularly in cluster randomized trials [7]. Although values of \(\rho\) in cluster randomized trials tend to be small (typically around 0.05 for primary care trials [8]) and in community randomized trials even smaller (usually less than 0.01 and often near 0.001 [3]) the resulting DE may be very substantial when combined with clusters of large size. Thus, the practice of ignoring clustering effects in the design stage of a trial can lead to an elevated type 2 error, while ignoring it at the analysis stage inevitably leads to an elevated type 1 error.

 In cluster randomized trials there are often two sample size choices to be made: the number of clusters and the number of subjects per cluster. A useful rule of thumb is that the power does not increase appreciably once the number of subjects per cluster exceeds \(1/\rho\)[4]. Thus, if it is believed that the ICC is about 0.05 then it is not worth enrolling more than about 20 subjects per cluster. However, if the ICC is near 0.001, which is often typical of community intervention trials, then a sample of 1000 subjects per cluster may be worthwhile, particularly if recruiting new clusters is difficult.

The sample size formulas we give here assume that data for sample size estimation are obtained from a single sample of clusters from the population of interest, that is the intervention itself has no effect on the cluster size. Examples where this is not true have been given by Campbell [8], and we will return to this topic in Section 7.2.

### Sample sizes for trials involving survival data

One of the earliest (and highest cited) papers in _Statistics in Medicine_ is by Freedman [9] on the sample size required in a study when the outcome is survival. The total number of events, \(e\), required for a power \(\beta\) and two-sided significance \(\alpha\) to detect an expected hazard ratio \(\theta\) is given by

\[e=(z_{\alpha/2}+z_{\beta})^{2}\frac{(1+\phi\theta)^{2}}{\phi(1-\theta)^{2}}\] (1)

where \(z_{\alpha/2}\) and \(z_{\beta}\) are the normal ordinates associated with probabilities \(\alpha/2\) and \(\beta\), \(\phi\) is the ratio of the sample size in group 2 to group 1 and \(\theta\) is the expected hazard ratio between groups 2 and 1.

Xie and Waksman [10] generalized equation (1) to cluster randomized trials. An important issue in applying this formula is whether one should estimate \(\rho\) from the clustered survival data or, alternatively, from the censoring indicators. Xie and Waksman [10] chose to estimate \(\rho\) from the indicators, since this approach is widely used in the clustered binary data literature. Thus, in what follows \(\rho\) is estimated as a simple correlation of the 0,1's indicating whether or not an event is censored, although further research on this estimation question would be useful. They found that the number of events \(e_{\mathrm{c}}\) required is a simple generalization of Freedman's formula:

\[e_{\mathrm{c}}=e(1+(\overline{m}-1)\rho)\]

where \(\overline{m}=\sum_{i=1}^{K}m_{i}/K\), is the average number of subjects per cluster and \(K\) is the number of clusters.

The number of subjects required is then given by

\[n=\frac{(1+\phi)e_{\mathrm{c}}}{\overline{m}((1-P_{1})+\phi(1-P_{2}))}\]

where \(P_{1}\) and \(P_{2}\) are the proportion of individuals with non-events in groups 1 and 2.

### Allowing for imprecision in the ICC

Much of the sample size literature deals with the difficulty of obtaining accurate estimates of between-community variation, and hence of \(\rho\), that are needed for sample size planning.

 In practice estimates of \(\rho\) for a given outcome variable are usually derived from previously reported studies using similar randomization units. However, these estimates are frequently based on studies which themselves are of small size, and thus their inherent inaccuracy may lend the investigators a false sense of confidence.

Ukoumunne [11] has given a series of methods for calculating confidence intervals for the ICC, including an application of the bootstrap. However, it is difficult to know how to use these for planning purposes. As Turner _et al_. [12] have pointed out, for planning purposes it may be better to select a design on the basis of power averaged across uncertainty rather than calculate power from an informally assessed ICC value. Moreover, substitution of a conservative ICC such as the upper value from a 95 per cent confidence interval usually reduces the power for a fixed sample size estimate much more than a method which allows for the imprecision of the ICC. They discuss the use of prior distributions for the ICC and in a Bayesian context show how the uncertainty about this parameter can be expressed in the form of a parametric distribution which naturally leads to a distribution of projected power for any particular design. This Bayesian approach towards the determination of sample size could then be followed by a statistical analysis within the traditional frequentist framework. Turner _et al_. [12] showed that increasing the number of clusters enables the total sample size to be reduced for a given power. With a given number of subjects estimated from an unclustered design, increasing the number of clusters also considerably reduces the lower limit of the posterior distribution of power. In other words, uncertainty in the ICC will produce uncertainty in the actual power of a study, but a design based on a greater number of clusters has less chance of having a very low power.

An alternative approach to dealing with uncertainty in observed values of \(\rho\) is described by Feng and Grizzle [13], who proposed the use of a method similar in principle to the bootstrap procedure. Their approach requires the simulation of results of studies of the same size that yielded the observed estimate. One then can substitute the values of \(\rho\) obtained from each simulation into the appropriate sample size formula to generate a distribution of projected powers, followed by the selection of a point on this distribution, e.g. the 90th percentile, that reflects the degree of conservativeness desired.

### Allowing for varying cluster sizes

Variation in cluster size is another source of imprecision and Kerry and Bland [14] following Donner _et al_. [15] suggest using

\[\mathrm{DE}=1+(m_{a}-1)\rho\quad\mathrm{where}\ m_{a}=\sum m_{i}^{2}/\sum m_{i}\] (2)

The problem of using this formula is that the individual cluster sizes must be known prior to conducting the trial.

Eldridge _et al_. [16] modified (2) to give

\[\mathrm{DE}=1+\left(\left(\mathrm{cv}^{2}\frac{(k-1)}{k}+1\right)\overline{m }-1\right)\rho\] (3)

where \(\mathrm{cv}=s_{m}/\overline{m}\) and \(s_{m}\) is the s.d. of the cluster size. They suggest that formula (3) is more practical than (2) since the value of \(\mathrm{cv}\) (coefficient of variation) may often be known in advance. Eldridge _et al_. [16] also provide some examples of the coefficient of variation for sample sizes typically seen in cluster randomized trials. A further issue is that the estimated ICC will have sampling variation. Eldridge _et al_. [16] give an empirical correction for the DE in this case.

 This formula is appropriate for cluster level analyses that weight by cluster size. For the much more common GEE analysis, which we describe in Section 5, this formula is likely to be conservative.

### Sample size re-estimation

When prior knowledge of the value of the variance components required to ascertain the sample size is unavailable, we can undertake an internal pilot study to provide these estimates, using a well cited paper in this area by Wittes and Brittain [17], and as extended to cluster randomized trials by Lake _et al._[18]. With this approach, several nuisance parameters, including \(\rho\), the mean cluster size and measures of cluster size variation, are estimated at an interim point in the study, followed by re-estimation of the final required trial size. Although this procedure is most suited to trials that randomize a relatively large number of clusters, such as families or households, over an extended period of time, Lake _et al._[18] point out that it could also be applied to at least some community intervention trials provided the participating clusters are recruited prospectively. Turner _et al._[12] state that imprecision in the estimate of \(\rho\) is not accounted for in this application, but their own method could easily be extended to do so. More experience on the application of internal pilot studies to such trials is clearly needed.

### Empirical investigations of design effects

Empirical investigations of design effects likely to arise in cluster randomized trials implemented in a specific setting are also helpful to investigators. An example of such an investigation is given by Mickey _et al._[19], who presented design effects from a trial designed to intervene on breast cancer mortality. Ukoumunne _et al._[20] presented variance components for some common outcomes, as did Gulliford _et al._[21].

Several authors have shown that adjusting for covariates either at the community or individual-level can improve the power of a trial by reducing the magnitude of the between-cluster variation [8, 22]. Additional gains in power may be realized by modelling individual level covariates (e.g. age) and also at the cluster level (e.g. mean cluster age) as described by Klar and Darlington [23].

## 3 Issues in the design and analysis of matched pair community randomized trials

### Design of matched pair studies

Matched pair studies are not frequently seen in clinical trials randomizing individual subjects to different intervention groups. However, they have proved to be the design of choice for many investigators embarking on a community intervention trial, largely because of the perceived ability of this design to create intervention groups that are comparable at baseline with respect to important prognostic factors, including, for example, community size and geographic area. The relatively small number of communities that can be enrolled in such studies further enhances the attractiveness of pair matching as a method of reducing the probability of substantively important imbalances that may detract from the credibility of the reported results. _Statistics in Medicine_ has been the forum for much of the debate surrounding the advantages and disadvantages of this design.

 Freedman _et al_. [24] were among the first authors to investigate the gain in efficiency obtained from matching in a community intervention trial. This was done in the context of COMMIT (Community Intervention Trial for Smoking Cessation), a community programme designed to encourage citizens to stop smoking. As discussed by Gail _et al_. [25], 11 pairs of communities were matched on the basis of several factors expected to be related to the smoking quit rates, such as community size, geographical proximity and demographic profile. Within each matched pair, one community was allocated at random to the intervention group, with the other acting as the control. It is also interesting to note that this trial was one of the first large-scale community intervention studies to use formal power considerations at the planning stage, and, perhaps not coincidentally, to be substantially larger in size than its predecessors.

Assuming the gain in efficiency due to matching may be quantified by the factor \(G=1/(1-\rho_{m})\), where \(\rho_{m}\) is the correlation between members of a pair with respect to the outcome variable, Freedman _et al_. [24] showed that matching can lead to considerable gains in statistical precision when it is based on an effective surrogate for outcome. However, since \(G\) is simply the ratio of population variances ignoring or accounting for pair-matching, it does not take into account the difference in degrees of freedom for estimating these variances, a factor which is particularly relevant in trials enrolling a small number of communities. For example, in the COMMIT study, the degrees of freedom available for estimating error from the paired differences in event rates would be only 10, as compared to the 20 degrees of freedom available for an unmatched analysis.

This issue was subsequently addressed in detail by Martin _et al_. [26], who evaluated the relative efficiency of a matched to an unmatched analysis by using percentiles of the non-central \(t\)-distribution to account for the differences in degrees of freedom. On the basis of these results they concluded that for studies having no more than 20 pairs, matching should be used for the purpose of increasing power only if the investigators are confident that \(\rho_{m}\) exceeds 0.20. By considering the practical difficulties that often arise in securing 'good' matches, they also concluded more generally that 'matching may be overused as a design tool' in community intervention trials.

These considerations suggest that a tempting strategy in practice may be to perform an unmatched analysis of data arising from a matched pair design, particularly when matching is adopted mainly for the purpose of avoiding a 'bad' randomization. The effectiveness of such a strategy was investigated by Diehr _et al_. [27], who concluded on the basis of an extensive simulation study that breaking the matches can actually result in an increase in power when the number of pairs is less than ten. Thus, the loss in precision identified by Martin _et al_. [26] in the presence of weak matching correlations can be at least partially regained.

A secondary objective of many community intervention trials is to investigate the effect of individual-level risk factors on one or more outcome variables. Focusing on the case of a continuous outcome variable, Donner _et al_. [28] showed that the practice of performing an unmatched analysis on data arising from a pair-matched design can lead to bias in the estimated regression coefficient, and a corresponding test of significance which is overly liberal. However, for large-scale community intervention trials, which typically recruit a relatively small number of large clusters, such an analysis will generally be both valid and efficient.

Perhaps the most commonly adopted matching factors in large-scale community randomized trials have been cluster size and geographic area (e.g. urban _versus_ rural). Matching by cluster size is attractive not only because it protects against large imbalances in the number of subjects per intervention group, an efficiency consideration, but also because cluster size may be associated with other important but unaccounted for baseline variables, such as socioeconomic status and access to health care resources (Lewsey [29]). Matching by categorized levels of baseline versions of the trial outcome rate would also seem attractive. However, results reported by Feng _et al_. [22] suggest that if primary interest is changed from the baseline, such matching is not likely to add benefits in power beyond that yielded by an analysis of change scores.

### Limitations of matched pair designs

Klar and Donner [30] explored some further limitations of the matched pair designs that are more general in nature. These limitations arise largely from the total confounding of the intervention effect with the natural variation that exists between two members of a matched pair. One consequence of such confounding is that it precludes the use of standard methods for estimating the underlying ICC, which in turn reduces analytic flexibility. For example, a secondary objective of many studies is to estimate the effect of selected individual level risk factors on one or more outcome variables using regression modelling. However, the calculation of appropriate standard errors for the regression coefficients obtained from such a model requires a valid estimator of \(\rho\). Thus, although it is possible to perform adjustments for the effect of such risk factors using a two-stage residualized approach e.g. Gail _et al_. [31], the task of testing for their independent relationship with outcome is more difficult (Donner _et al_. [28]). Moreover the matched pair design frequently does not bring large gains in precision. This led Klar and Donner [30] to recommend that greater attention be paid to the possibility of adopting a stratified design, in which two or more clusters are randomized to each intervention group within the strata. This design may be particularly attractive when investigators find it challenging to create matched pairs that correspond to unique estimates of risk for each pair. Most importantly, the cluster level replication inherent in this less rigid allocation scheme removes many of the analytic limitations associated with pair-matching, while increasing the degrees of freedom available for estimating error.

## 4 Other design issues

### Cohort versus cross-sectional designs

Many community intervention trials are longitudinal in nature, allowing a choice between a cohort design and a cross-sectional design. For a cohort design, clusters are randomly assigned to intervention groups, with or without stratification. Cohorts sampled from each cluster are then measured over two or more time points, with at least the first measurement occurring before randomization. The cross-sectional design is similar, except that samples are selected independently within each cluster at each time point. Because responses within the same subject often have a strong positive correlation, the cohort design is theoretically more efficient.

Feldman and McKinlay [32] presented a unified statistical model that embraces both designs as special cases, thus allowing an assessment of how the values of different design parameters affect their relative precision. A principal conclusion from their investigation was that cohort designs have unique disadvantages that may outweigh any advantage in theoretical efficiency. The first of these is related to possible instability in cohorts of large size, with the resulting likelihood of subject loss to follow-up. Although this disadvantage can be compensated for by oversampling at baseline, this might well negate the original reasons for adopting a cohort design. Differential loss to follow-up by intervention group also creates the risk of bias.

The second disadvantage is related to the issue of representativeness of the target population, which is invariably hampered by the ageing of the cohort over time. Assuming that changes related to the ageing process are independent of the intervention assignment, this effect will not invalidate the principal comparison of interest. However, it does imply that a difference observed in a cohort trial with respect to a given outcome variable cannot be directly compared to the corresponding difference between observed cross-sectional samples. Thus, if the primary questions of interest focus on change at the community level rather than at the level of the individual, cohort samples are the less natural choice. This point is discussed by others [33, 34], who describe and compare several approaches that might be taken to the analysis of repeated cross-sectional samples. Additional discussion is provided by Murray _et al_. [35].

### Practical design issues

There are two useful papers in _Statistics in Medicine_ that look at practical issues for the conduct of cluster randomized trials. Flynn _et al_. [36] address the issue of whether it is worth recruiting an extra cluster or to recruit more individuals to existing clusters. They show how the use of contour graphs of power by number of clusters per treatment arm and cluster size can be usefully exploited. Moerbeek [37] suggests that often a cheaper strategy than recruiting another cluster would be to measure additional covariates related to the outcome, in order to reduce the variance. This, of course, requires the cost of measuring the covariate to be relatively small and the correlation of the covariate and the outcome to be reasonably high.

## 5 Issues in the analysis of cluster randomized trials

### Cluster specific versus marginal models

Consider an outcome variable \(Y\) (which may be continuous or binary), with expected value \(\mu\) and a generalized link of the form

\[g(\mu)=\eta=\beta_{0}+\beta_{1}X+Z\] (4)

where the function \(g\) is assumed strictly monotone and differentiable. We further assume that \(Z\) is a random variable \(E(Z)=0\) and \(\operatorname{var}(Z)=\sigma_{Z}^{2}\) and so is independent of the fixed effect \(X\).

Equation (4) may be a suitable model for clustered data. We assume that the clusters are sampled from a larger population and the effect of any particular cluster \(i\) is to add a random effect \(Z_{i}\) to all the outcomes. For a cluster randomized we could set \(X=1\) for intervention and \(X=0\) for control. A CS model measures the effect on \(Y\) of changing \(X\), while \(Z\) is held constant. This is a common model for longitudinal data, where it is possible to imagine, say in a cross-over trial, a treatment value changing over time. However, in a cluster randomized, everyone in a cluster receives the same treatment, and although a CS model can be fitted, the result can be interpreted only theoretically. The alternative is to fit a model which looks at the average effect of \(X\) over the range of \(Z\). This is the so-called _population averaged_ (\(PA\)) or _marginal_ model.

Consider a model where we fit only \(X\), so that

\[\eta=\beta_{0}^{*}+\beta_{1}^{*}X\] (5)

Fitting model (5) is equivalent to fitting a PA model, that is we estimate the effect of \(X\) on \(Y\) as averaged over all the clusters \(Z\).

Neuhaus and Jewell [38] approach the contrast between CS models and PA models by observing that model (5) is simply model (4) with the variable \(Z\) omitted. If we assume that the coefficients for \(X\) in the two models are related by \(\beta_{1}^{*}\approx B\,\beta\), where \(B\) is the bias factor, then they show that for a linear model \(B=1\), and so the interpretation of CS and marginal models is the same. However, for a logistic link, \(\mu=\log\)it(\(P\,(Y=1\,|\,X,\,Z)\) is a random variable and

\[B=1-\frac{\sigma_{z}^{2}}{E(\mu)\{1-E(\mu)\}}=1-\rho\]

where \(\rho\) is the correlation of the \(Y\)'s within clusters assuming \(\beta_{1}=0\). Since, as discussed earlier, the value of \(\rho\) in community randomized trials is usually less than 0.01, this suggests that the bias in incorrectly assuming a marginal model should not be great.

In this case 0\(<\)\(B<\)1, so the general effect of using a PA model is to attenuate the regression coefficient. One can also see that for a logistic link the greater the variability of the random variable \(Z\), and so the greater the intracluster correlation, the greater the attenuation.

Neuhaus and Jewell [38] also show that \(B=1\) for a log link, which would suggest that in prospective studies such as clinical trials it would be advantageous to use a log-linear model which estimates the relative risk rather than a logistic model for odds ratios. Until recently the software for accurately estimating the standard errors of the estimates for cluster log-linear models was not available, but Zou [39] has recently demonstrated how it can be done using Poisson regression and robust standard errors.

The fact that log-linear models estimate the same population parameter for CS and marginal models does not appear well known. For example Murray _et al._[5] state that 'in the case of binary data the coefficient from a marginal model is smaller than that from a conditional model...'.

### Inflating the standard error

For a linear model we write

\[y_{ij}=\beta_{0}+\beta_{1}X_{i}+Z_{i}+\varepsilon_{ij}\] (6)

where \(y_{ij}\) is the outcome of the \(j\)th subject (\(j=1,\ldots,\,K\)) in the \(i\)th cluster (\(i=1,\ldots,\,m_{j}\)), and we assume \(E(\varepsilon_{ij})=E(Z_{i})=0\), \(\varepsilon_{ij}\) and \(Z_{i}\) are independent, \(V(\varepsilon_{ij})=\sigma^{2}\) and \(V(Z_{i})=\sigma_{Z}^{2}\). Here \(X_{i}\) is an intervention indicator variable (\(0\), \(1\)) which depends only on the cluster. An _exchangeable_ correlation structure is assumed, which effectively means that one can exchange subjects \(j\) and \(j^{\prime}\) within a cluster without changing the covariance. This breaks down if the subjects are measured more than once (for example, at baseline and at follow-up) since the correlation of the same subject measured twice will not be the same as the correlation of two different subjects within a cluster. It also means that the ICC must be assumed to be the same within each arm of the trial, an assumption which is guaranteed in a randomized trial under the null hypothesis of no intervention effect.

We can rewrite (6) as

\[y_{ij}=\beta_{0}+\beta_{1}X_{i}+\eta_{ij}\] (7)

where the \(\eta_{ij}\) are random errors which are not independent, but are typically assumed to have an exchangeable structure defined by the clusters. This is the PA model described in Section 5.1.

We can fit model (7) but not account for the correlated nature of the errors terms. Provided that \(Z_{i}\) is uncorrelated with \(X_{i}\) then we get a valid estimate of the treatment effect but the standard error of the treatment effect is underestimated, and should be inflated. A technique originating in sample survey research is to simply multiply the standard error by the DE. For example, the DE given in Section 1 may be estimated by replacing the ICC with its sample estimate [3]. A simple test of whether a parameter is zero, known as a modified Wald test, is to divide an estimate of the parameter by its modified standard error which is then compared to a standard normal distribution. Donner and Klar [3] give a number of methods for continuous and binary outcomes which modify the standard error associated with either the \(t\)-test or the chi-squared test, respectively. It is important to note that the estimate of the treatment effect is unchanged, only the standard error is inflated. An alternative method is to use the so-called 'sandwich' or Huber-White estimator which has a long history in econometrics for estimators with continuous data and with heterogeneous variances. This fits a model where the variance of the error term \(V(\eta)=\sigma_{i}^{2}\) is not assumed constant, and is estimated through the residuals of the model. The advantage of the robust standard error is that one does not need to estimate the ICC separately before conducting the analysis. The disadvantage is that it may be less efficient and so would need a greater number of clusters than does use of the model-dependent standard error. The use of robust standard errors for cluster randomized trials was first suggested by Brook _et al._[40], and implemented in a number of statistical packages, for example in _Stata_ by Rogers [41].

In general, Donner and Klar's [3] methods which adjust the standard error give an estimate of the treatment effect which, in effect, weights each cluster by the size of the cluster, so that larger clusters have greater weight. An alternative is to use the method of summary measures, as popularized by Matthews _et al._[42]. This gives equal weight to each cluster, irrespective of size and is a CS method. This approach has a great deal to recommend it since it simply uses the summary statistics (mean or proportion) for each cluster and is easy to apply without specialist software. However, one cannot adjust for individual level covariates directly using this approach.

### Fitting models to data

The generalized estimating equation (GEE) method, developed by Liang and Zeger [43] in the context of longitudinal studies, has proved to very popular for the analysis of data arising from cluster randomized trials. It fits the PA model and uses an iteratively reweighting algorithm to estimate the parameters and a robust method for the standard error. Use of the GEE is a 'shrinkage' approach which is a compromise between no weighting and weighting by the sample size. Assuming an exchangeable correlation structure, it effectively weights each mean by \(m_{i}/(m_{i}\sigma_{z}^{2}+\sigma^{2})\), which weights the means by the sample size when \(\sigma_{Z}^{2}=0\) and gives equal weight when \(\sigma^{2}=0\). In practice, estimates of the variance components are used.

The analysis of continuous data is relatively straightforward and a comparison of maximum likelihood assuming a normal mixed model, GEE, a bootstrap and a '4-stage method' have been given by Feng _et al._[44]. The bootstrap used by Feng _et al._ draws a random sample of size \(K\) from the original \(K\) clusters. Then one can use ordinary least squares to estimate the \(\beta\)'s and repeat a large number of times. The four stage method is non-iterative, where the first step is to estimate the \(\beta\)'s by ordinary least squares and obtain the residuals \(e_{i}=Y_{i}-X_{i}\widehat{\beta}\). Then the \(e_{i}\)'s are regressed against the \(Z_{i}\)'s, leading to estimates of \(\sigma^{2}\) and \(\sigma_{Z}^{2}\). One can then use these estimates in a weighted least squares regression of \(Y_{i}\)_versus_\(X_{i}\).

For small numbers of clusters (\(<\)10 per arm) and for near balanced data the bootstrap has been shown to do well, especially if one does not wish to assume normality. For larger numbers of clusters, the maximum likelihood method performed better than GEE.

GEE is used widely for hypothesis testing and confidence interval construction because it can control for the influence of potential confounders on outcome without the need to specify an underlying distribution for the sample observations. The robust variance estimation relies on between-cluster information to assure the validity of the resulting inferences. It is therefore important to be wary of this approach to community intervention trials, where the amount of such information tends to be relatively small.

Feng _et al_. [44] recommended for continuous data that GEE should not be applied to trials having 20 or fewer communities. Recent research has shown that for studies enrolling few clusters one should take account of the fact that the observed residuals, which are used in robust estimation, are biased estimates of the error variable, because of the requirement that they sum to zero. This bias can be removed by dividing the squared error by the diagonal of the 'hat' matrix. It has also been found that using a \(t\)-distribution (or a Satterthwaite type degrees of freedom correction) and a jack-knife improves the estimate of the standard error [45, 46, 47]. Pan and Wall [47] proposed replacing the GEE Wald test by approximate \(t\)- or \(F\)-tests. Although the proposed procedures showed type 1 errors closer to nominal than the usual Wald test, they were shown to be strictly applicable only in clusters of small sizes. It is therefore clear that more research is needed on the development of adjusted GEE procedures that can be applied to clusters of the size that typically arise in community intervention trials.

Recently Guo _et al_. [48] discussed not only the use of a robust standard error in the Wald test, but also the robust score test, particularly for cluster randomized trials. They show that the use of the Wald test is too liberal (more likely to give a significant value) and the score test is too conservative and suggest that a simple correction \(K/(K-1)\) to the score statistic will give a test size closer to the nominal value.

It is worth commenting that the use of the sandwich estimator has been associated with the GEE method so many times that they may appear synonymous. In fact they are not, and one can use robust standard error without GEE as described in Section 5.2.

### Analysis of binary data

As discussed in Section 5.1 binary models can estimate different population parameters and so deserve special consideration.

Let \(Y_{ij}\) (0 or 1) be the \(j\)th observation (\(j=1,\,\ldots,\,m_{i}\)) in the \(i\)th cluster (\(i=1,\,2,\,\ldots,\,K\)). The intervention variable is \(X_{i}\) (0 or 1). The CS logistic model is

\[\log it\,(\pi_{ij})=\beta_{0}+\beta X_{i}+Z_{i}\] (8)

where \(Z_{i}\) is the effect of being in cluster \(i\) and where \(\pi_{ij}=E(Y_{ij}|X_{i},\,Z_{i})\). This model can be extended to include individual specific covariates \(X_{ij}\). The random variable \(Z_{i}\) is assumed independent of \(X_{i}\) and is usually assumed to be normally distributed with mean 0 and variance \(\sigma_{Z}^{2}\). Given the \(Z_{i}\), the \(Y_{ij}\)'s are assumed independently distributed with binomial parameter \(\pi_{ij}\).

Recently Heo and Leon [49] compared different methods of analysis under (8): (i) full likelihood; (ii) penalized quasi-likelihood; (iii) GEE and (iv) fixed effects logistic regression. The third method is a marginal method which, following the discussion in Section 5.1, estimates a different population parameter than the regression coefficient in (8). However, it does not require one to assume a normal distribution for the \(Z_{i}\). The last method does not take the ICC into account, and is an invalid method in general for cluster randomized trials. However if \(\sigma_{Z}^{2}=0\) it may be expected to yield valid tests and efficient estimates.

 The full likelihood \(L\) is given by

\[L=\prod_{i=1}^{K}\int\prod_{j=1}^{m_{i}}\mu_{ij}(\beta,\,Z_{i})^{y_{ij}}\{1-\mu_{ ij}(\beta,\,Z_{i})\}^{1-y_{ij}}\,f\,(Z_{i};\,\sigma^{2})\,\mathrm{d}Z_{i}\] (9)

where \(f(.)\) is the normal distribution function.

Equation (9) can be maximized using Gaussian quadrature or other numerical methods to obtain estimates of the regression coefficients.

Penalized quasi-likelihood is a method of maximizing the likelihood whilst avoiding the integration, using a Laplace method for approximating the integral (Breslow and Clayton [50]).

Heo and Leon [49] found that the full likelihood method and the penalized likelihood methods to be similar and no worse than the fixed effects method even when the within-cluster correlations are zero. As expected the GEE method gave biased estimates of \(\beta_{\mathrm{cs}}\). They did not investigate the effects of estimating \(\beta_{\mathrm{PA}}\).

Preisser _et al_. [51] showed how to apply a PA model to a pre-test post-test cross-sectional design, where the assumption of an exchangeable correlation matrix breaks down. They state that the GEE approach is asymptotically equivalent to the summary measure approach, and quote Mancl and De Rouen [46] to the effect that using bias-corrected variances can yield valid test sizes even with unequal cluster sizes and with as few as 10 clusters.

### Bayesian methods

The likelihood given in (9) requires numerical integration to solve. An alternative method is to use simulation via Monte Carlo Markov Chain (MCMC) algorithms. These are normally associated with a Bayesian analysis, but choice of suitable non-informative priors will yield results similar to the conventional likelihood methods.

Spiegelhalter [52] described the method for the Bayesian analysis of cluster randomized trials with a continuous response. This was extended to a binary outcome by Turner _et al_. [53].

They used model (8) and looked at different prior distributions for \(\sigma_{Z}^{2}\). Since \(\sigma_{Z}^{2}\) is closely related to the ICC, they argued that often it is more appropriate to use a prior distribution on the ICC, since prior information on the ICC is now becoming available [21, 22]. They experimented with different prior distributions and showed that the estimate of the treatment effect is not entirely robust to the distributional assumptions of the model, and suggested caution in using the conventional normality assumption. They contrasted their results to an earlier study by Omar and Thompson [54] who used a multilevel model and a penalized quasi-likelihood procedure to obtain the estimates. Turner _et al_. [53] showed that the variance components tend to be underestimated when using the non-Bayesian approach.

Thompson _et al_. [55] argue that often in a clinical trial one is interested in a risk difference rather than an odds ratio, and describe how to carry out a Bayesian analysis in such a situation.

### Modelling in matched pairs designs

Thompson _et al_. [56] replaced standard modelling approaches by techniques borrowed from meta-analysis. Thus, an intervention/control pair replaces an individual clinical trial of a meta-analysis. This is essentially equivalent to relying on between-stratum information to estimate \(\rho\) under the assumption of no intervention by stratum interaction. An attractive feature of this is that the forest plot can show which pairs appear to be outliers. However, this approach requires a large number of strata (pairs) to ensure its validity, and is therefore not applicable to many community intervention studies.

The meta-analysis method as applied to the matched pairs design was extended to binary data by Alexander and Emerson [57] using a Bayesian approach. Their technique was illustrated by applying it to incidence rates of trachoma in Africa. Methods that may be applied to data arising from a stratified cluster randomized design are discussed by Dobbins and Simpson [58] and Song and Ahn [59]. However, they restrict themselves to a comparison of the performance of specific tests in terms of the size and power, rather than on the general problem of estimation.

The strict lack of applicability of the \(t\)-test to binary outcomes in a matched pair design has led some investigators to alternatively recommend non-parametric approaches, such as Fisher's one sample randomization (permutation) test. Simulations performed by Gail _et al._[31] showed that inferences for matched pair binary data using permutation procedures will have significance levels near nominal under conditions likely to arise in community intervention trials. Essentially, the same conclusions were reached by Brookmeyer and Chen [60] for person-time data arising from matched pair trials. It is useful to note, however, that the one sample permutation test requires a minimum of six pairs to yield a two-sided \(p\)-value of less than 0.05, reflecting its relatively weak power. Donner and Donald [61] showed that a weighted paired \(t\)-test based on a logistic transformation of the crude event rates tends to be more powerful than both the permutation test and the standard paired \(t\)-test in trials having a small number of strata.

## 6 Presenting data

### CONSORT statement

It is a perennial complaint amongst analysts that cluster randomized trials are poorly reported [62]. The original CONSORT statement was an attempt to improve reporting of individually randomized trials. This statement was subsequently adapted for cluster randomized trials, published in _Statistics in Medicine_[63], and has been well cited. It has now been revised and published in a medical journal [64, 65]. The most important distinctions from the original are: (i) to give a rationale for adopting a cluster design; (ii) to describe how the effects of clustering were incorporated into the sample size calculations; (iii) to describe how the effects of clustering were incorporated into the analysis; and (iv) to describe the flow of both clusters and participants through the trial, from assignment to analysis. Thus, in a primary care trial, for example, one would like to know how many primary care groups were approached, how many agreed to participate, how many were randomized, and how many dropped out during the trial, as well as the characteristics of the patients in the study. The most up-to-date statement is available at www.consort-statement.org

### Improvements in reporting

A recent review by Bland [66] contrasted the years 1983, 88, 93, 98 and 2003. He suggests that cluster randomized trials are becoming more prevalent and the presentation of cluster randomized trials has improved, particularly after 1998. He suggests that statistical pressure has contributed to this and it is of note that the two seminal books were published in that period [3, 67].

 

## 7 Other Considerations

### Clustering by practitioner

Investigators may need to contend with clustering of subjects' responses even for trials using individual randomization. For example, patients may be randomized as they enter a trial by whether or not they will receive a new intervention (say acupuncture). However, there may be a limited number of acupuncturists and so a single acupuncturist may treat a number of patients. The outcomes will thus be affected not only by whether the patient received acupuncture but by which acupuncturist.

The model is

\[y_{ijk}=\beta_{0}+\beta_{1}X_{i}+\gamma Z_{k}+\varepsilon_{ij}\]

where the subscript \(k\) indicates the effect of different acupuncturists and \(Z_{k}=0\) for the control group. However, it is important to note that the subjects in the control group are not naturally clustered. Issues in the analysis of these trials have been covered by Roberts and Roberts [68]. Lee and Thompson [69] discuss a Bayesian approach to the analysis of such trials, and point out that taking into account clustering in the analysis can affect the results.

### Compliance and recruitment

We now discuss some potential sources of bias that are peculiar to cluster randomization trials. For example, if the subjects in a trial are newly diagnosed patients and the intervention is some new approach to treating a disease, then it is possible that practitioners in the intervention arm, being newly educated about this disease, may be more likely to diagnose it [8]. This can lead to serious problems of selection bias. Also compliance to treatment may well vary over the participating clusters in a cluster randomized trial (Loeys _et al._[70]). While this will not affect the conclusions of an intent to treat analysis, it has major implications for any attempt at casual modelling. Loeys _et al._[70] demonstrate how to use standard GEE and random effects models to allow for variable compliance among clusters.

### Complex interventions

The use of cluster randomized trials is now well appreciated in the medical world, and methods for analysis are increasingly becoming available in standard software. The main area of further advance would seem to be in the design and planning of the interventions. These are often _complex_, by which we mean that they depend on a number of interventions. Thus, even a relatively simple study, such as a patient education trial in diabetes raises a number of issues: (i) standardizing what to teach the educators; (ii) training the educators; (iii) deciding how many classes to have; (iv) deciding how many students to allow in each class; and (v) tailoring the education to the needs of the participants. Phase III drug trials are usually preceded by Phase I and Phase II studies in order to decide on issues such as timing and dosage. These are often missing in cluster randomized trials of complex interventions. However, methods of designing complex trials have been described in a set of guidelines produced by the British Medical research Council [71]. These has been criticized on two grounds [72, 73]. First ,the guidelines imply that planning of complex interventions is a linear process, whereas often there is no clear ordering to the respective planning stages. Second, they suggest that one should attempt to standardize the intervention, whereas effective interventions,particularly educational ones, may have to be tailored to the participants. This can lead to problems of understanding exactly what is being tested, which components in an intervention are important, and whether the intervention is replicable.

Due to the large number of possible inter-relations in complex trials, computer modelling is playing an increasing role in the planning of such studies. We expect to see an increasing role played in such pre-trial modelling to decide on the optimum design of the intervention.

## 8 Discussion

There is now a vast literature on the design and analysis of cluster randomized trials. The level of understanding has increased greatly since the papers published in early volumes of Statistics in Medicine [6, 7, 13, 26]. However, there is still a need for more empirical work to help the user decide which methods might give better results in particular situations.

This review has, of necessity been partial, and biased towards papers published in _Statistics in Medicine_. However, we feel that many of the key papers have appeared in that journal, and hope that this will continue in the future!

## Acknowledgements

The authors are grateful to Obi Ukoumunne and Sandra Eldridge for useful comments on a previous draft. The work of Dr Campbell was supported by a visiting scholarship grant from the Royal Society. The work of Drs Donner and Klar has been partially supported by grants from the Natural Sciences Engineering Research Council of Canada.

## References

* [1] Campbell MJ, Donner A, Elbourne DR. Design and analysis of cluster randomized trials--preface. _Statistics in Medicine_ 2001; **20**:329-330.
* [2] Klar N, Donner A. Current and future challenges in the design and analysis of cluster randomization trials. _Statistics in Medicine_ 2001; **20**:3729-3740.
* [3] Donner A, Klar N. _Design and Analysis of Cluster Randomization Trials_. Arnold: London, 2000.
* [4] Donner A, Klar N. Pitfalls of and controversies in cluster randomized trials. _American Journal of Public Health_ 2004; **94**:416-422.
* [5] Murray DM, Vernell SP, Bliststein JL. Design and analysis of group-randomized trials: a review of recent methodological developments. _American Journal of Public Health_ 2004; **94**:423-432.
* [6] Donner A. Approaches to sample size estimation in the design of clinical trials. _Statistics in Medicine_ 1984; **3**:199-214.
* [7] Hsieh FY. Sample size formulae for intervention studies with the cluster as unit of randomization. _Statistics in Medicine_ 1988; **8**:1195-1201.
* [8] Campbell MJ. Cluster randomized trials in general (family) practice research. _Statistical Methods in Medical Research_ 200; **9**:81-94.
* [9] Freedman LS. Tables of the number of patients required in clinical trials using the logrank test. _Statistics in Medicine_ 1982; **1**:121-129.
* [10] Xie T, Waksman J. Design and sample size estimation in clinical trials with clustered survival times as the primary endpoint. _Statistics in Medicine_ 2003; **22**:2835-2846.
* [11] Ukoumunne O. Confidence intervals for the intradess correlation coefficient in cluster randomized trials. _Ph.D. Thesis_, King's College, University of London, 2004.
* [12] Turner RM, Prevost AT, Thompson SG. Allowing for imprecision of the intracluster correlation coefficient in the design of cluster randomized trials. _Statistics in Medicine_ 2004; **23**:1195-1214.
* [13] Copyright (c) 2006 John Wiley & Sons, Ltd. _Statist. Med._ 2007; **26**:2-19 DOI: 10.1002/sim * [13] Feng Z, Grizzle JE. Correlated binomial variates: properties of estimator of intraclass correlation and its effect on sample size calculation. _Statistics in Medicine_ 1992; **11**:1607-1614.
* [14] Kerry SM, Bland JM. Unequal cluster sizes for trials in English and Welsh general practice: implications for sample size calculations. _Statistics in Medicine_ 2001; **20**:377-390.
* [15] Donner A, Birkett N, Buck C. Randomization by cluster: sample size requirements and analysis. _American Journal of Epidemiology_ 1981; **114**:906-914.
* [16] Eldridge S, Kerry S, Ashby D. Sample size for cluster randomized trials: effect of coefficient of variation of cluster size and analysis method. _International Journal of Epidemiology_ 2006; **35**:1292-1300.
* [17] Wittes J, Brittain E. The role of internal pilot studies in increasing the efficiency of clinical trials. _Statistics in Medicine_ 1990; **9**:65-72.
* [18] Lake S, Kamman E, Klar N, Betensky R. Sample size re-estimation in cluster randomization trials. _Statistics in Medicine_ 2002; **21**:1337-1350.
* [19] Mickey RM, Goodwin GD, Costanza MC. Estimation of the design effect in community intervention studies. _Statistics in Medicine_ 1991; **10**:53-64.
* [20] Ukoumunne OC, Gulliford MC, Chinn S, Sterne JAC, Burney PGJ. Methods for evaluating area-wide and organisation-based interventions in health and health care. A methodological systematic review for the NHS research and development health technology assessment programme. _Health Technology Assessment_ 1999; **3**.
* [21] Gulliford MC, Adams G, Ukoumunne OC, Latinovic R, Chinn S, Campbell MJ. Intraclass correlation coefficient and outcome prevalence are associated in clustered binary data. _Journal of Clinical Epidemiology_ 2005; **58**: 246-251.
* [22] Feng F, Diehr P, Yasui Y, Evans B, Beresford S, Koepsell TD. Explaining community level-variance in group randomized trials. _Statistics in Medicine_ 1999; **18**:539-556.
* [23] Klar N, Darlington G. Methods for modelling change in cluster randomization trials. _Statistics in Medicine_ 2004; **23**:2341-2357.
* [24] Freedman LS, Green SB, Byar DP. Assessing the gain in efficiency due to matching in a community intervention study. _Statistics in Medicine_ 1990; **9**:943-953.
* [25] Gail MH, Byar DP, Pechacek TF, Corle DK. Aspects of statistical design for the community intervention trial for smoking cessation (COMMIT). _Controlled Clinical Trials_ 1992; **13**:6-21.
* [26] Martin DC, Diehr P, Perrin EB, Koepsell TD. The effect of matching on the power of randomized community intervention studies. _Statistics in Medicine_ 1993; **12**:329-338.
* [27] Diehr P, Martin DC, Koepsell T, Cheadle A. Breaking the matches in a paired \(t\)-test for community interventions when the number of pairs is small. _Statistics in Medicine_ 1995; **14**:1491-1504.
* [28] Donner A, Talijaard M, Klar N. The merits of breaking the matches in community intervention studies: a cautionary late. _Statistics in Medicine_, in press.
* [29] Lewsey JD. Comparing completely and stratified randomization designs in cluster randomized trials when the stratifying factor is cluster size: a simulation study. _Statistics in Medicine_ 2004; **23**:897-905.
* [30] Klar N, Donner A. The merits of matching in community intervention trials. _Statistics in Medicine_ 1997; **16**:1753-1764.
* [31] Gail MH, Mark SD, Carroll RJ, Green SB, Pee D. On design considerations and randomization-based inference for community intervention trials. _Statistics in Medicine_ 1996; **15**:1069-1092.
* [32] Feldman HA, McKinlay SM. Cohort versus cross-sectional design in large field trials: precision, sample size, and a unifying model. _Statistics in Medicine_ 1994; **13**:61-78.
* [33] Okounmunne OC, Thompson SG. Analysis of cluster randomized trials with repeated cross-sectional binary measurements. _Statistics in Medicine_ 2001; **20**:417-434.
* [34] Nixon RM, Thompson SG. Baseline adjustments for binary data in repeated cross-sectional cluster randomized trials. _Statistics in Medicine_ 2003; **22**:2673-2692.
* [35] Murray DM, Hannan PJ, Wolfinger RD, Baker WL, Dwyer JH. Analysis of data from group-randomized trials with repeat observations on the same groups. _Statistics in Medicine_ 1998; **17**:1581-1600.
* [36] Flynn TN, Whitley E, Peters TJ. Recruitment strategies in a cluster randomize trial-cost implications. _Statistics in Medicine_ 2002; **21**:397-405.
* [37] Moerbeek M. Power and money in cluster randomized trials: when is it worth measuring a covariate? _Statistics in Medicine_ 2005; **15**:2607-2617.
* [38] Neuhaus JM, Jewell NP. A geometric approach to assess bias due to omitted covariates in generalized linear models. _Biometrika_ 1993; **80**:807-815.
* [39] Zou GY. A modified Poisson regression approach to prospective studies with binary data. _American Journal of Epidemiology_ 2004; **159**:702-706.
* [40] Copyright (c) 2006 John Wiley & Sons, Ltd. _Statist. Med._ 2007; **26**:2-19 DOI: 10.1002/sim * [40] Brook RH, Ware JE, Rogers WH _et al_. Does free care improve adult's health? Results from a randomized trial. _New England Journal of Medicine_ 1983; **309**:1426-1434.
* [41] Rogers WIl. Regression standard errors in clustered samples. _Stata Technical Bulletin_ 1994; **13**:19-23. (Reprinted in _Stata Technical Bulletin Reprints_, vol. 3, 88-94.)
* [42] Matthews JNS, Altman DG, Campbell MJ, Royston P. Analysis of serial data using summary measures _British Medical Journal_ 1990; **300**:230-235.
* [43] Liang K-Y, Zeger SL. Longitudinal data analysis using generalized linear models. _Biometrika_ 1986; **73**:13-22.
* [44] Feng Z, McLaran D, Grizzle J. A comparison of statistical methods for clustered data analysis with Gaussian error. _Statistics in Medicine_ 1996; **15**:1793-1806.
* [45] Long JS, Ervin LH. Using heterogeneity consistent standard errors in the linear regression model. _American Statistical_ 2000; **54**:217-224.
* [46] Mancl L, DeRouen TA. A covariance estimator for GEE with improved small sample properties. _Biometrics_ 2001; **57**:126-134.
* [47] Pan W, Wall MM. Small sample adjustments in using the sandwich variance estimator in generalized estimating equations. _Statistics in Medicine_ 2002; **21**:1429-1441.
* [48] Guo X, Pan W, Connett JE, Hannan PJ, French SA. Small-sample performance of the robust score test and its modifications in generalized estimating equations. _Statistics in Medicine_ 2005; **24**:3479-3495.
* [49] Heo M, Leon AC. Comparison of statistical methods for analysis of clustered binary observations. _Statistics in Medicine_ 2005; **24**:911-923.
* [50] Breslow NE, Clayton DG. Approximate inference in generalized linear mixed models. _Journal of the American Statistical Association_ 1993; **88**:125-134.
* [51] Preisser JJ, Young ML, Zaccaro DJ, Wolfson M. An integrated population average approach to the design, analysis and sample size determination of cluster unit trials. _Statistics in Medicine_ 2003; **22**:1235-1254.
* [52] Spiegelhalter DJ. Bayesian methods for cluster randomized trials with continuous response. _Statistics in Medicine_ 2001; **20**:435-452.
* [53] Turner RM, Omar RZ, Thompson SG. Bayesian methods of analysis for cluster randomized trials with binary outcome data. _Statistics in Medicine_ 2001; **20**:453-472.
* [54] Omar RZ, Thompson SG. Analysis of a cluster randomized trial with binary outcome data using a multi-level model. _Statistics in Medicine_ 2000; **19**:2675-2688.
* [55] Thompson SG, Warm DE, Turner RM. Bayesian methods for analysis of binary outcome data in cluster randomized trials on the absolute risk scale. _Statistics in Medicine_ 2004; **23**:389-410.
* [56] Thompson SG, Pyke SDM, Hardy RJ. The design and analysis of paired cluster randomized trials: an application of meta-analysis techniques. _Statistics in Medicine_ 1997; **16**:2063-2980.
* [57] Alexander N, Emerson P. Analysis of incidence rates in cluster-randomized trials of interventions against recurrent infections, with an application to trachoma. _Statistics in Medicine_ 2005; **24**:2637-2647.
* [58] Dobbins TA, Simpson JM. Comparison of tests for categorical data from a stratified cluster randomized trial. _Statistics in Medicine_ 2002; **21**:3835-3846.
* [59] Song JX, Ahn CW. An evaluation of methods for the stratified analysis of clustered binary data in community intervention trials. _Statistics in Medicine_ 2003; **22**:2205-2216.
* [60] Brookmeyer R, Chen Y-Q. Person-time analysis of paired community intervention trials when the number of communities is small. _Statistics in Medicine_ 1998; **17**:2121-2132.
* [61] Donner A, Donald A. Analysis of data arising from a stratified design with the cluster as unit of randomization. _Statistics in Medicine_ 1987; **6**:43-52.
* [62] Eldridge SM, Ashby D, Feder GS, Rudnicka AR, Ukoumune OC. Lessons for cluster randomized trials in the twenty-first century: a systematic review of trials in primary care. _Clinical Trials_ 2004; **1**:80-90.
* [63] Elbourne DR, Campbell MK. Extending the CONSORT statement to cluster randomized trials: for discussion. _Statistics in Medicine_ 2001; **20**:489-496.
* [64] Campbell MJ. Editorial: extending CONSORT to include cluster randomized trials. _British Medical Journal_ 2004; **328**:654-655.
* [65] Campbell MK, Elbourne DR, Altman DG. CONSORT statement: extension to cluster randomized trials. _British Medical Journal_ 2004; **328**:707-708.
* [66] Bland JM. Cluster randomized trials in the medical literature: two bibliometric surveys. _BMC Medical Research Methodology_ 2004; **4**:21. Doi: 10.1118/1471-2288-4-2.
* [67] Murray DM. _The Design and Analysis of Group-Randomized Trials_. University Press: Oxford, 1998.
* [68] Roberts C, Roberts SA. Design and analysis of clinical trials with clustering effects due to treatment. _Clinical Trials_ 2002; **2**:152-162.

Copyright (c) 2006 John Wiley & Sons, Ltd.

_Statist. Med._ 2007; **26**:2-19 * [69] Lee KJ, Thompson SG. The use of random effects models to allow for clustering in individually randomized trials. _Clinical Trials_ 2005; **2**:163-173.
* [70] Loeys T, Vansteeland S, Goerbigheur E. Accounting for correlation and compliance in cluster randomized trials. _Statistics in Medicine_ 2001; **20**:3753-3767.
* [71] Medical Research Council. _A Framework for the Development and Evaluation of Randomized Controlled Trials for Complex Interventions to Improve Health_. MRC: London, 2000.
* [72] Hawe P, Sheill A, Riley T. Complex interventions: how 'out of control' can a randomized controlled trial be? _British Medical Journal_ 2004; **328**:1561-1563.
* [73] Campbell MJ. Complex interventions: more thought needed. _British Medical Journal_ 2004; /bmj.328.7455.1561 