import re, shutil, sys
from pathlib import Path
REPO = Path(sys.argv[1])
rename = {
  'aAIControlledSmart2024':'aAIControlledSmart2024a', 'Ahlamine2024':'ahlamineMathematicalAnalysisAnaerobic2024',
  'ahmedAgricultureClimateChange2020':'AgricultureClimateChangea', 'ait-kaddourTransformingPlantbasedWaste2024':'ait-kaddourTransformingPlantbasedWaste2024a',
  'allan2023':'allanSummaryPolicymakers2023', 'arrese2010insect':'arreseInsectFatBody2010',
  'bekker2021impact':'bekkerImpactSubstrateMoisture2021a', 'bekkerImpactSubstrateMoisture2021':'bekkerImpactSubstrateMoisture2021a',
  'bermudez2023comprehensive':'bermudez-serranoComprehensiveUtilizationBlack2023', 'bermudezComprehensiveUtilizationBlack2023':'bermudez-serranoComprehensiveUtilizationBlack2023',
  'biagiDevelopmentMachineLearningbased2024':'biagiDevelopmentMachineLearningbased2024a', 'burrelHowMachineThinks2016':'burrellHowMachineThinks2016',
  'Camperio2025':'camperioWasteFunctionalFeed2025', 'carolan2020automated':'carolanAutomatedAgrifoodFutures2020',
  'chenOptimizationModelProcess2021':'chenOptimizationModelProcess2021a', 'chia2018':'chiaBlackSoldierFly2019',
  'colombia2020ndc':'tiriaACTUALIZACIONCONTRIBUCIONDETERMINADA', 'diener2009conversion':'dienerConversionOrganicMaterial2011',
  'dienerblack2011':'dienerConversionOrganicMaterial2011', 'dienerConversionOrganicMaterial2009':'dienerConversionOrganicMaterial2011',
  'duobiene2022development':'duobieneDevelopmentWirelessSensor2022', 'elsayedConversionProteinrichWaste2024':'elsayedConversionProteinrichWaste2024a',
  'Eriksen2022':'eriksenDynamicModellingFeed2022', 'eriksen2022dynamic':'eriksenDynamicModellingFeed2022',
  'FAO2021':'lacknerAgriculturalWasteChallenges2025', 'fao2021waste':'lacknerAgriculturalWasteChallenges2025',
  'foodandagricultureorganizationoftheunitednationsfaoAgriculturalWasteManagement2021':'lacknerAgriculturalWasteChallenges2025', 'fuhrmann2025comprehensive':'fuhrmannComprehensiveIndustryrelevantBlack2025a',
  'fuhrmannComprehensiveIndustryrelevantBlack2025':'fuhrmannComprehensiveIndustryrelevantBlack2025a', 'galan-diazCarbonWaterFootprint2024':'galan-diazCarbonWaterFootprint2024a',
  'ginerFoodLossWaste2025':'oecdFoodLossWaste2025', 'ginerFoodLossWaste2025a':'oecdFoodLossWaste2025',
  'Gold2020':'goldBiowasteTreatmentBlack2020', 'gold2020biowaste':'goldBiowasteTreatmentBlack2020',
  'herrinCollateralDataQuality2021':'herrinCollateralDataQualitya', 'IPCC2014':'groupedexpertsintergouvernementalsurlevolutionduclimatClimateChange20142014',
  'ipcc2021ar6':'intergovernmentalpanelonclimatechangeipccClimateChange20212023', 'jenkins2025processing':'jenkinsProcessingPoultryManure2025',
  'johnson2019deep':'kamilarisDeepLearningAgriculture2018', 'kamilaris2017review':'kamilarisReviewPracticeBig2017',
  'klerkx2019review':'klerkxReviewSocialScience2019a', 'klerkxReviewSocialScience2019':'klerkxReviewSocialScience2019a',
  'kobelskiModelbasedProcessOptimization2024':'kobelskiProcessOptimizationBlack2024', 'kobelskiModelbasedProcessOptimization2024a':'kobelskiProcessOptimizationBlack2024',
  'kok2021':'kokPreliminaryProjectDesign2021', 'kok2021preliminary':'kokPreliminaryProjectDesign2021',
  'kong2012evaluating':'kongEvaluatingGreenhouseGas2012', 'koyunogluBiofuelProductionUtilizing2024':'koyunogluBiofuelProductionUtilizing2024a',
  'laganaro2021growth':'laganaroGrowthMetabolicPerformance2021a', 'laganaroGrowthMetabolicPerformance2021':'laganaroGrowthMetabolicPerformance2021a',
  'larisaWastetofeedBioconversionUsing2025':'larisaWastetofeedBioconversionUsing2025a', 'lecun2015deep':'lecunDeepLearning2015',
  'Leddin2024':'leddinImpactClimateChange2024a', 'leddinImpactClimateChange2024':'leddinImpactClimateChange2024a',
  'li2015simultaneous':'liSimultaneousUtilizationGlucose2015', 'lindbergProcessEfficiencyGreenhouse2022':'lindbergProcessEfficiencyGreenhouse2022a',
  'liuOptimizingDataPipelines2023':'liuOptimizingDataPipelines2023a', 'makkar2014insects':'makkarStateoftheartUseInsects2014',
  'meneguz2018effect':'meneguzEffectRearingSubstrate2018', 'nayakHermetiaIllucensDiptera2024':'nayakHermetiaIllucensDiptera2023',
  'nordahl2023greenhouse':'nordahlGreenhouseGasAir2023a', 'nordahlGreenhouseGasAir2023':'nordahlGreenhouseGasAir2023a',
  'padmanabha2020comprehensive':'padmanabhaComprehensiveDynamicGrowth2020', 'padmanabhaModellingOptimalControl2023':'padmanabhaModellingOptimalControl2023a',
  'parodiBioconversionEfficienciesGreenhouse2020':'parodiBioconversionEfficienciesGreenhouse2020a', 'parodiBlackSoldierFly2021':'parodiBlackSoldierFly2021a',
  'raissiPhysicsinformedNeuralNetworks2019':'raissiPhysicsinformedNeuralNetworks2019a', 'raj2023real':'rajRealTimeEstimation2023a',
  'rajRealTimeEstimation2023':'rajRealTimeEstimation2023a', 'republicadecolombiacomoinstitucionContribucionDeterminadaNivel':'tiriaACTUALIZACIONCONTRIBUCIONDETERMINADA',
  'Rossi2024':'rossiEstimatingDynamicsGreenhouse2024a', 'rossi2024estimating':'rossiEstimatingDynamicsGreenhouse2024a',
  'rossiEstimatingDynamicsGreenhouse2024':'rossiEstimatingDynamicsGreenhouse2024a', 'salam2022effect':'salamEffectDifferentEnvironmental2022',
  'singh2019inclusive':'singhInclusiveApproachOrganic2019a', 'singhInclusiveApproachOrganic2019':'singhInclusiveApproachOrganic2019a',
  'smetana2019sustainable':'smetanaSustainableUseHermetia2019a', 'smetanaSustainableUseHermetia2019':'smetanaSustainableUseHermetia2019a',
  'Surendra2016':'surendraBioconversionOrganicWastes2016', 'surendra2016bioconversion':'surendraBioconversionOrganicWastes2016',
  'vanIntegrationInternetofThingsSustainable2022':'vanIntegrationInternetofThingsSustainable2022a', 'verraVCSStandardV472024':'VCSStandardv47FINAL41524',
  'winAnaerobicDigestionBlack2018':'winAnaerobicDigestionBlack2018a', 'wmo2025':'ak-bhdWEATHERCLIMATEWATER',
  'wmoWMOGreenhouseGas2025':'ak-bhdWEATHERCLIMATEWATER', 'Xiang2024':'xiangBlackSoldierFly2024',
  'zhangApplicationBigData2024':'zhangApplicationBigData2024a',
}
n=0
for tex in REPO.rglob('*.tex'):
    s=o=tex.read_text(encoding='utf-8', errors='ignore')
    for vieja,nueva in rename.items():
        s=re.sub(r'(?<![A-Za-z0-9])'+re.escape(vieja)+r'(?![A-Za-z0-9])', nueva, s)
    if s!=o:
        shutil.copy(tex, str(tex)+'.bak'); tex.write_text(s, encoding='utf-8')
        print('  actualizado:', tex.relative_to(REPO)); n+=1
print(f'Listo: {n} archivos modificados')
