
## DICOM RT

Development of DICOM RT Information Objects started in January, 1995
Radiotherapy Information Objects (Supp 11, Final Text June 1997)
* RT Structure Set – image segmentation
* RT Plan – beam/source geometry and dosimetry
* RT Image – projection image in beam geometry
* RT Dose – dose matrix and DVHs

Radiotherapy Treatment Record (Supp 29, Final Text May 1999)
* RT Beams Treatment Record
* RT Brachy Treatment Record
* RT Treatment Summary Record

Radiotherapy Extensions for Ion Therapy (Supp 102, Final Text Mar 2006)
- RT Ion Plan 
- RT Ion Beams Treatment Record

### tools for DICOM-RT

SlicerRT project in 3D Slicer
https://www.slicer.org/wiki/Documentation/Nightly/Modules/DicomRtImport
DICOM-RT import export (handle datasets of types RT Structure Set, RT Dose, RT Plan, RT Image)
DICOM-SRO import/export (handles DICOM Spatial Registration object, both rigid and deformable)

learn from a package in Matlab ( DICOM-RT to Matlab) https://github.com/ulrikls/dicomrt2matlab
1. Load DICOM headers
2. read contours sequences (reading and converting RT structures) 
Basically in this step, it will load ROINames, Points, VoxelPoints, Segmentation files 
in each slice by looping through contours
3. Save segmentations


