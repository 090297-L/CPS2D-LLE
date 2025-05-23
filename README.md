# CPSLLE

CPSLLE: A Large-scale Low-light Enhancement Dataset for Darkroom Defect Detection in Integrated Circuit Packaging Substrates

## CPSLLE Description

The CPSLLE dataset originates from ceramic package substrate samples gathered in actual factory environments. These samples are selected during critical phases of the production process, such as punching hole, filling hole, and printing, representing actual production conditions and process changes. To obtain images under different lighting conditions, we manually adjust lighting intensity during data acquisition. However, it is important to note that the lighting conditions are constant during the actual operation of the equipment, which results in the generation of low-light data. This comprehensive approach ensures that our dataset captures the dynamic shifts in production processes. Unlike typical open-world scenarios, industrial anomaly data is characterized by its scarcity, strict privacy levels, and limited applicability. The richness of CPSLLE provides a valuable advantage in low-light enhancement.

<div align=center>
  
<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/3.png" width="1500px"> 

<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/5.png" width="1500px">

</div>

## Comparison between different low-light datasets

<div align=center>
  
<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/4.png" width="1500px"> 

</div>

## Data Link
The dataset is uploaded into Google Drive, and the source train and val set data can be download in [Google drive](https://drive.google.com/file/d/1x5JHAQ5zSb8jkneFNg0AXJuy657q_VgB/view?usp=drive_link).


## AOI System and Dataset

We developed an AOI equipment, as shown in Fig. 2 of our paper, focusing on low-light enhancement and defect detection in CPS. The operator places the CPS sample to be inspected at the loading port. The loading tray automatically elevates, positioning the first CPS sample at the designated scanning location, where the camera MV-ID3016 is triggered to perform QR code recognition and decoding. Subsequently, the destacking suction cup moves the tray to the waiting area, and the sample is transported to the visual inspection chamber with MV-CH250-90GC camera for low-light enhancement and defect detection. The visual inspection servo moves and flips the sample using a suction cup to facilitate the capture and detection of defects on both sides. Following visual inspection, the conveyor belt transports the sample to the sorting area and controls the sorting servo and suction cup to move the sample. The operator presses the unloading permission key and retrieves the completed samples from the unloading area.

<div align=center>

<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/1.png" width="800px"> <img src="https://github.com/090297-L/CPSLLE/blob/main/Images/2.png" width="800px">

</div>

## Benchmark Methodology

To further validate the contribution of CPSLLE in integrated circuit research, we design a novel low-light enhancement algorithm called Light-MMamba. As illustrated in Fig. 6 in our paper, our framework consists of two primary components: the Illumination Estimator and the Multi-scale Equalization Vision Mamba. Initially, the Illumination Estimator employs Retinex technology to enhance low-light images. However, the enhanced images often face common issues inherent to image enhancement techniques, such as increased noise and color space imbalance. To address these challenges, we design the Multi-scale Equalization Vision Mamba, which proposes a Multi-scale Equalization State Space Model for noise reduction, the enhancement and balance of image color feature space in the process of image enhancement.

<div align=center>
  
<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/6.png" width="1500px">

</div>

## Display video

Display video of AOI can be download in [Google drive](https://drive.google.com/file/d/1ULLhjB4qRHoLopkfPxRJsr2Fpq56n0c3/view?usp=drive_link).

## Experiments results

All comparison algorithms can be found in the folders

### [CPSLLE Dataset](https://drive.google.com/file/d/1x5JHAQ5zSb8jkneFNg0AXJuy657q_VgB/view?usp=drive_link)

<div align=center>

<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/7.png" width="1500px">

<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/8.png" width="1500px">

</div>

## Ablation Study

<div align=center>

<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/9.png" width="800px">

<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/11.png" width="800px">

<img src="https://github.com/090297-L/CPSLLE/blob/main/Images/10.png" width="1200px">

</div>

## Licenses

The code and dataset are released under the CC BY 4.0 license. All data collection processes are authorized by the relevant companies.
