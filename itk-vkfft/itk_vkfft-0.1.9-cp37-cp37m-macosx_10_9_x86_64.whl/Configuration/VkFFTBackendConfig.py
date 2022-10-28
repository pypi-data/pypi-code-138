depends = ('ITKPyBase', 'ITKStatistics', 'ITKSmoothing', 'ITKRegistrationCommon', 'ITKImageSources', 'ITKFFT', 'ITKConvolution', 'ITKCommon', )
templates = (  ('VkComplexToComplex1DFFTImageFilter', 'itk::VkComplexToComplex1DFFTImageFilter', 'itkVkComplexToComplex1DFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('VkComplexToComplex1DFFTImageFilter', 'itk::VkComplexToComplex1DFFTImageFilter', 'itkVkComplexToComplex1DFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('VkComplexToComplex1DFFTImageFilter', 'itk::VkComplexToComplex1DFFTImageFilter', 'itkVkComplexToComplex1DFFTImageFilterICD2', True, 'itk::Image< std::complex< double >,2 >'),
  ('VkComplexToComplex1DFFTImageFilter', 'itk::VkComplexToComplex1DFFTImageFilter', 'itkVkComplexToComplex1DFFTImageFilterICD3', True, 'itk::Image< std::complex< double >,3 >'),
  ('VkComplexToComplexFFTImageFilter', 'itk::VkComplexToComplexFFTImageFilter', 'itkVkComplexToComplexFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('VkComplexToComplexFFTImageFilter', 'itk::VkComplexToComplexFFTImageFilter', 'itkVkComplexToComplexFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('VkComplexToComplexFFTImageFilter', 'itk::VkComplexToComplexFFTImageFilter', 'itkVkComplexToComplexFFTImageFilterICD2', True, 'itk::Image< std::complex< double >,2 >'),
  ('VkComplexToComplexFFTImageFilter', 'itk::VkComplexToComplexFFTImageFilter', 'itkVkComplexToComplexFFTImageFilterICD3', True, 'itk::Image< std::complex< double >,3 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterISS4ISS4', True, 'itk::Image< signed short,4 >, itk::Image< signed short,4 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIUC4IUC4', True, 'itk::Image< unsigned char,4 >, itk::Image< unsigned char,4 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIUS4IUS4', True, 'itk::Image< unsigned short,4 >, itk::Image< unsigned short,4 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterIF4IF4', True, 'itk::Image< float,4 >, itk::Image< float,4 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('VkDiscreteGaussianImageFilter', 'itk::VkDiscreteGaussianImageFilter', 'itkVkDiscreteGaussianImageFilterID4ID4', True, 'itk::Image< double,4 >, itk::Image< double,4 >'),
  ('VkFFTImageFilterInitFactory', 'itk::VkFFTImageFilterInitFactory', 'itkVkFFTImageFilterInitFactory', True),
  ('VkForward1DFFTImageFilter', 'itk::VkForward1DFFTImageFilter', 'itkVkForward1DFFTImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('VkForward1DFFTImageFilter', 'itk::VkForward1DFFTImageFilter', 'itkVkForward1DFFTImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('VkForward1DFFTImageFilter', 'itk::VkForward1DFFTImageFilter', 'itkVkForward1DFFTImageFilterID2', True, 'itk::Image< double,2 >'),
  ('VkForward1DFFTImageFilter', 'itk::VkForward1DFFTImageFilter', 'itkVkForward1DFFTImageFilterID3', True, 'itk::Image< double,3 >'),
  ('VkForwardFFTImageFilter', 'itk::VkForwardFFTImageFilter', 'itkVkForwardFFTImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('VkForwardFFTImageFilter', 'itk::VkForwardFFTImageFilter', 'itkVkForwardFFTImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('VkForwardFFTImageFilter', 'itk::VkForwardFFTImageFilter', 'itkVkForwardFFTImageFilterID2', True, 'itk::Image< double,2 >'),
  ('VkForwardFFTImageFilter', 'itk::VkForwardFFTImageFilter', 'itkVkForwardFFTImageFilterID3', True, 'itk::Image< double,3 >'),
  ('VkGlobalConfiguration', 'itk::VkGlobalConfiguration', 'itkVkGlobalConfiguration', True),
  ('VkHalfHermitianToRealInverseFFTImageFilter', 'itk::VkHalfHermitianToRealInverseFFTImageFilter', 'itkVkHalfHermitianToRealInverseFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('VkHalfHermitianToRealInverseFFTImageFilter', 'itk::VkHalfHermitianToRealInverseFFTImageFilter', 'itkVkHalfHermitianToRealInverseFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('VkHalfHermitianToRealInverseFFTImageFilter', 'itk::VkHalfHermitianToRealInverseFFTImageFilter', 'itkVkHalfHermitianToRealInverseFFTImageFilterICD2', True, 'itk::Image< std::complex< double >,2 >'),
  ('VkHalfHermitianToRealInverseFFTImageFilter', 'itk::VkHalfHermitianToRealInverseFFTImageFilter', 'itkVkHalfHermitianToRealInverseFFTImageFilterICD3', True, 'itk::Image< std::complex< double >,3 >'),
  ('VkInverse1DFFTImageFilter', 'itk::VkInverse1DFFTImageFilter', 'itkVkInverse1DFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('VkInverse1DFFTImageFilter', 'itk::VkInverse1DFFTImageFilter', 'itkVkInverse1DFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('VkInverse1DFFTImageFilter', 'itk::VkInverse1DFFTImageFilter', 'itkVkInverse1DFFTImageFilterICD2', True, 'itk::Image< std::complex< double >,2 >'),
  ('VkInverse1DFFTImageFilter', 'itk::VkInverse1DFFTImageFilter', 'itkVkInverse1DFFTImageFilterICD3', True, 'itk::Image< std::complex< double >,3 >'),
  ('VkInverseFFTImageFilter', 'itk::VkInverseFFTImageFilter', 'itkVkInverseFFTImageFilterICF2', True, 'itk::Image< std::complex< float >,2 >'),
  ('VkInverseFFTImageFilter', 'itk::VkInverseFFTImageFilter', 'itkVkInverseFFTImageFilterICF3', True, 'itk::Image< std::complex< float >,3 >'),
  ('VkInverseFFTImageFilter', 'itk::VkInverseFFTImageFilter', 'itkVkInverseFFTImageFilterICD2', True, 'itk::Image< std::complex< double >,2 >'),
  ('VkInverseFFTImageFilter', 'itk::VkInverseFFTImageFilter', 'itkVkInverseFFTImageFilterICD3', True, 'itk::Image< std::complex< double >,3 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterISS2ISS2', True, 'itk::Image< signed short,2 >, itk::Image< signed short,2 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterISS3ISS3', True, 'itk::Image< signed short,3 >, itk::Image< signed short,3 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterISS4ISS4', True, 'itk::Image< signed short,4 >, itk::Image< signed short,4 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIUC2IUC2', True, 'itk::Image< unsigned char,2 >, itk::Image< unsigned char,2 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIUC3IUC3', True, 'itk::Image< unsigned char,3 >, itk::Image< unsigned char,3 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIUC4IUC4', True, 'itk::Image< unsigned char,4 >, itk::Image< unsigned char,4 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIUS2IUS2', True, 'itk::Image< unsigned short,2 >, itk::Image< unsigned short,2 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIUS3IUS3', True, 'itk::Image< unsigned short,3 >, itk::Image< unsigned short,3 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIUS4IUS4', True, 'itk::Image< unsigned short,4 >, itk::Image< unsigned short,4 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIF2IF2', True, 'itk::Image< float,2 >, itk::Image< float,2 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIF3IF3', True, 'itk::Image< float,3 >, itk::Image< float,3 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterIF4IF4', True, 'itk::Image< float,4 >, itk::Image< float,4 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterID2ID2', True, 'itk::Image< double,2 >, itk::Image< double,2 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterID3ID3', True, 'itk::Image< double,3 >, itk::Image< double,3 >'),
  ('VkMultiResolutionPyramidImageFilter', 'itk::VkMultiResolutionPyramidImageFilter', 'itkVkMultiResolutionPyramidImageFilterID4ID4', True, 'itk::Image< double,4 >, itk::Image< double,4 >'),
  ('VkMultiResolutionPyramidImageFilterFactory', 'itk::VkMultiResolutionPyramidImageFilterFactory', 'itkVkMultiResolutionPyramidImageFilterFactory', True),
  ('VkRealToHalfHermitianForwardFFTImageFilter', 'itk::VkRealToHalfHermitianForwardFFTImageFilter', 'itkVkRealToHalfHermitianForwardFFTImageFilterIF2', True, 'itk::Image< float,2 >'),
  ('VkRealToHalfHermitianForwardFFTImageFilter', 'itk::VkRealToHalfHermitianForwardFFTImageFilter', 'itkVkRealToHalfHermitianForwardFFTImageFilterIF3', True, 'itk::Image< float,3 >'),
  ('VkRealToHalfHermitianForwardFFTImageFilter', 'itk::VkRealToHalfHermitianForwardFFTImageFilter', 'itkVkRealToHalfHermitianForwardFFTImageFilterID2', True, 'itk::Image< double,2 >'),
  ('VkRealToHalfHermitianForwardFFTImageFilter', 'itk::VkRealToHalfHermitianForwardFFTImageFilter', 'itkVkRealToHalfHermitianForwardFFTImageFilterID3', True, 'itk::Image< double,3 >'),
)
factories = (("FFTImageFilterInit","Vk"),)
