import pyOSOAA


resroot = ""  # working directory
s = pyOSOAA.OSOAA(resroot=resroot)  # OSOAA simulation object


## CLASS SEA

s.sea.surfalb = 0.0  # lambertian reflectance of the foam
s.sea.bottype = 1  # type of seabed composition
s.sea.botalb = 0.0  # seabed albedo
s.sea.wind = 0.0  # wind speed
s.sea.ind = 0.0  # refractive index sea/atmosphere
s.sea.depth = 0.0  # sea depth


## CLASS LOG
# All values are field in by default

s.log.osoaa = "log_osoaa.txt"  # main log file
s.log.ang = "log_ang.txt"  # angle calculation log file
s.log.profile = "log_profile.txt"  # profile log file
s.log.aer = " log_aer.txt"  # OSOAA_PHASE_MATRIX routine log file
s.log.aermie = "log_aermie.txt"  # aerosol Mie calculations log file
s.log.hyd = "log_hyd.txt"  # hydrosol radiative properties log file
s.log.hydmie = "log_hydmie.txt"  # Mie calculation for hydrosols log file
s.log.sea = "log_sea.txt"  # surface properties log file
s.log.sos = "log_sos.txt"  # model core radiative transfer calculations log file


## CLASS RESULTS

s.results.profileatm = "PROFILE_ATM.txt"  # atmospheric profile
s.results.profilesea = "PROFILE_SEA.txt"  # sea profile
s.results.aer = "PM_AER.txt"  # radiative properties of aerosols
s.results.phyto = "PM_PHYTO.txt"  # radiative properties calculated for phytoplankton
s.results.mlp = "PM_MLP.txt"  # properties calculated for mineral particles
s.results.angrad = "RAD_UsedAngles.txt"  # angles for the calc. of radiance, BRDS/BPDF
s.results.angmie = "MIE_UsedAngles.txt"  # angles for the calc. of the phase matrix
s.results.sosbin = "LUM_SF.bin"  # SOS binary output
s.results.vsvza = "LUM_vsVZA.txt"  # output ascii file providing radiance vs vza
s.results.vsz = "LUM_vsZ.txt"  # output ascii file providing the radiance vs z
s.results.advup = "LUM_Adv_Up.txt"  # output ascii file providing the upward radiance
s.results.advdown = "LUM_Adv_Down.txt"  # output ascii file providing the down. radiance
s.results.hydiop = "HYD_IOP.txt"  # output ascii file providing the hydrosols IOPs
s.results.aeriop = "AER_IOP.txt"  # output ascii file providing the aerosols IOPs


## CLASS DIRMIE

s.dirmie.aer = resroot  # Mie file repository directory for aerosols
s.dirmie.hyd = resroot  # Mie files repository directory for hydrosols
s.dirmie.sea = resroot  # surface files repository directory


## CLASS PHYTO

####################################### if profiltype is Homogeneous
# profiltype = 1
# s.phyto.chl = 0.0  # chlorophyll concentration
# s.phyto.SetProfilType(profiltype)
####################################################################


########################################## if profiltype is Gaussian
# profiltype = 2
# chlbg = 0.0  # background concentration
# chlzmax = 0.0  # maximum chlorophyll concentration
# deep = 0.0  # depth of the peak of maximum concentration
# width = 0.0  # width of the gaussian peak
# s.phyto.SetProfilType(profiltype, chlbg, chlzmax, deep, width)
####################################################################


###################################### if profiltype is User defined
# profiltype = 3
# userfile = ""  # user defined file path for phytoplankton profile
# s.phyto.SetProfilType(profiltype, userfile=userfile)
####################################################################


# Primary mode
# All values are field in by default

mrwa1 = 0.0  # real part of the refractive index
miwa1 = 0.0  # imaginary part of the refractive index
slope1 = 4  # slope of Junge's law
## To be changed in expert mode only ##
rmin1 = 0.01  # min radius of phytoplankton particles
## To be changed in expert mode only ##
rmax1 = 200  # max radius of phytoplankton particles
rate1 = 0.0  # ratio of the main mode relatively to the overall distribution
s.phyto.SetPrimaryMode(
    mrwa=mrwa1, miwa=miwa1, slope=slope1, rmin=rmin1, rmax=rmax1, rate=rate1
)


############################################ if secondary mode
# mrwa2 = 0.0  # real part of the refractive index
# miwa2 = 0.0  # imaginary part of the refractive index
# sdradius2 = 0.0  # modal radius
# sdvar2 = 0.0  # standard deviation
# rate2 = 0.0  # ratio of the mode relatively to the overall distribution
# s.phyto.SetSecondaryMode(mrwa2, miwa2, sdradius2, sdvar2, rate2)

############################################ if tertiary mode
# mrwa3 = 0.0  # real part of the refractive index
# miwa3 = 0.0  # imaginary part of the refractive index
# sdradius3 = 0.0  # modal radius
# sdvar3 = 0.0  # standard deviation
# rate3 = 0.0  # ratio of the mode relatively to the overall distribution
# s.phyto.SetTertiaryMode(mrwa3, miwa3, sdradius3, sdvar3, rate3)


## CLASS SED
s.sed.csed = 0.0  # sediment concentration


# Primary mode

mrwased1 = 0.0  # real part of the refractive index
miwased1 = -0.0  # imaginary part of the refractive index
slopesed1 = 4  # slope of Junge's law
## To be changed in expert mode only ##
rminsed1 = 0.01  # min radius of sediments
## To be changed in expert mode only ##
rmaxsed1 = 200  # max radius of sediments
ratesed1 = 0.0  # ratio of the main mode relatively to the overall distribution
s.sed.SetPrimaryMode(
    mrwa=mrwased1,
    miwa=miwased1,
    slope=slopesed1,
    rmin=rminsed1,
    rmax=rmaxsed1,
    rate=ratesed1,
)


############################################ if secondary mode
# mrwased2 = 0.0  # real part of the refractive index
# miwased2 = 0.0  # imaginary part of the refractive index
# sdradiussed2 = 0.0  # modal radius
# sdvarsed2 = 0.0  # standard deviation
# ratesed2 = 0.0  # ratio of the mode relatively to the overall distribution
# s.sed.SetSecondaryMode(mrwased2, miwased2, sdradiussed2, sdvarsed2, ratesed2)

############################################ if tertiary mode
# mrwased3 = 0.0  # real part of the refractive index
# miwased3 = 0.0  # imaginary part of the refractive index
# sdradiussed3 = 0.0  # modal radius
# sdvarsed3 = 0.0  # standard deviation
# ratesed3 = 0.0 # ratio of the mode relatively to the overall distribution
# s.sed.SetTertiaryMode(mrwased3, miwased3, sdradiussed3, sdvarsed3, ratesed3)


## CLASS YS

s.ys.abs440 = 0.0  # absorption coefficient of yellow substances
## To be changed in expert mode only ##
s.ys.swa = 0.014  # exponential slope of the spectral var of ys abs. coeff.


## CLASS DET

s.det.abs440 = 0.0  # absorption coefficient of detritus
## To be changed in expert mode only ##
s.det.swa = 0.011  # exponential slope of the spectral var of the detritus abs. coeff.


## CLASS AP

mot = None  # molecular optical thickness
pressure = None  # atmospheric pressure at sea level
s.ap.hr = 0.0  # molecular height scale
s.ap.ha = 0.0  # aerosol height scale

####################### if molecular optical thickness
# s.ap.SetMot(mot, s.ap.hr)

####################### if pressure
# s.ap.SetPressure(pressure)


## CLASS AER

s.aer.waref = 0.0  # reference wavelength for the aerosol optical thickness
s.aer.aotref = 0.0  # aerosol optical thickness
s.aer.tronca = 1  # Phase function truncation

############################################ if aerosol model is mono-modal
################### if size distribution is log normal
# s.aer.SetModel(model=0, sdtype=1)
# s.aer.mm.mrwa = 0.0  # real part of the aerosols refr. ind. for calc. wav.
# s.aer.mm.miwa = 0.0  # imaginary part of the aerosols refr. ind. for calc. wav.
# s.aer.mm.mrwaref = 0.0  # real part of the aerosols refr. ind. for ref. wav.
# s.aer.mm.miwaref = 0.0  # imaginary part of the aerosols ref. ind. for ref. wav.
# s.aer.mm.sdradius = 0.0  # modal radius
# s.aer.mm.sdvar = 0.00  # standard deviation
################### if size distribution is Junge law
# s.aer.SetModel(model=0, sdtype=2)
# s.aer.mm.mrwa = 0.0 # real part of the aerosols refr. ind. for calc. wav.
# s.aer.mm.miwa = 0.0  # imaginary part of the aerosols refr. ind. for calc. wav.
# s.aer.mm.mrwaref = 0.0  # real part of the aerosols refr. ind. for ref. wav.
# s.aer.mm.miwaref = 0.0  # imaginary part of the aerosols ref. ind. for ref. wav.
# s.aer.mm.slope = 0  # Junge law slope
# s.aer.mm.rmin = 0.0  # min radius
# ## To be changed in expert mode only ##
# s.aer.mm.rmax = 0 # max radius
##########################################################################

###################################### if aerosol model is WMO multi-modal
# wmotype = 0  # wmo type
# dl = 0.0  # volume concentration for dust-like components
# ws = 0.0  # volume concentration for water-soluble components
# oc = 0.0  # volume concentration for oceanic components
# so = 0.0  # volume concentration for soot components
# s.aer.SetModel(model=1, wmotype=wmotype, dl=dl, ws=ws, oc=oc, so=so)
##########################################################################

################################ if aerosol model is Shettle&Fenn bi-modal
# sfmodel = 0  # Shettle & Fenn model
# rh = 0.0  # relative humidity
# s.aer.SetModel(model=2, sfmodel=sfmodel, rh=rh)
##########################################################################

################################## if aerosol model is Log-normal bi-modal
######### if mixture type is predefined by volumetric concentrations
# s.aer.SetModel(model=3, vcdef=1)
# s.aer.lnb.cmrwa = 0.0  # coarse mode real part of the refr. ind. for calc. wav.
# s.aer.lnb.cmiwa = -0.0  # coarse mode imaginary part of the refr. ind. for calc. wav.
# s.aer.lnb.csdradius = 0.0  # coarse mode modal radius
# s.aer.lnb.csdvar = 0.0  # coarse mode standard deviation
# s.aer.lnb.cmrwaref = 0.0  # coarse mode real part of the refr. ind. for ref. wav.
# s.aer.lnb.cmiwaref = -0.0  # coarse mode imaginary part of the refr. ind. for ref. wav.
# s.aer.lnb.fmrwa = 0.0  # fine mode real part of the refr. ind. for calc. wav.
# s.aer.lnb.fmiwa = -0.0  # fine mode imaginary part of the refr. ind. for calc. wav.
# s.aer.lnb.fsdradius = 0.0  # fine mode modal radius
# s.aer.lnb.fsdvar = 0.0  # fine mode standard deviation
# s.aer.lnb.fmrwaref = 0.0  # fine mode real part of the refr. ind. for ref. wav.
# s.aer.lnb.fmiwaref = -0.0  # fine mode imaginary part of the refr. ind. for ref. wav.
# s.aer.lnb.coarsevc = 0.0  # coarse mode volume concentration
# s.aer.lnb.finevc = 0.0  # fine mode volume concentration
######## if mixture type is defined by the ratio of coarse/fine mode
# s.aer.SetModel(model=3, vcdef=2)
# s.aer.lnb.cmrwa = 0.0  # coarse mode real part of the refr. ind. for calc. wav.
# s.aer.lnb.cmiwa = -0.0  # coarse mode imaginary part of the refr. ind. for calc. wav.
# s.aer.lnb.csdradius = 0.0  # coarse mode modal radius
# s.aer.lnb.csdvar = 0.0  # coarse mode standard deviation
# s.aer.lnb.cmrwaref = 0.0  # coarse mode real part of the refr. ind. for ref. wav.
# s.aer.lnb.cmiwaref = -0.0  # coarse mode imaginary part of the refr. ind. for ref. wav.
# s.aer.lnb.fmrwa = 0.0  # fine mode real part of the refr. ind. for calc. wav.
# s.aer.lnb.fmiwa = -0.0  # fine mode imaginary part of the refr. ind. for calc. wav.
# s.aer.lnb.fsdradius = 0.0  # fine mode modal radius
# s.aer.lnb.fsdvar = 0.0  # fine mode standard deviation
# s.aer.lnb.fmrwaref = 0.0  # fine mode real part of the refr. ind. for ref. wav.
# s.aer.lnb.fmiwaref = -0.0  # fine mode imaginary part of the refr. ind. for ref. wav.
# s.aer.lnb.raot = 0.0  # ratio coarse_mode/fine_mode
#########################################################################

################################# """### if aerosol model is User defined
# extdata = ""  # file path for the user defined phase function
# s.aer.SetModel(model=4, extdata=extdata)
##################################### """################################


## CLASS HYD

############################# if size ditribution model
# s.hyd.model = 1

############################# if user defined phase function
# s.hyd.model = 2
# s.hyd.extdata = ""  # file path for the external phase function


## CLASS ANG
# All values are field in by default

s.ang.thetas = 0.0  # solar zenith angle
## To be changed in expert mode only ##
s.ang.rad.nbgauss = 48  # number of Gauss angles for intensity
s.ang.rad.userangfile = None  # file name of user-defined supplementary angles
## To be changed in expert mode only ##
s.ang.mie.nbgauss = 40  # number of Gauss angles for phase function
s.ang.mieuser = (
    None  # file name of user-defined supplementary angles for phase function
)


## CLASS SOS

## To be changed in expert mode only ##
s.sos.igmax = 100  # scattering maximum order


## CLASS VIEW

s.view.phi = 0  # relative azimuth angle

######################## if TOA
# s.view.level = 1

######################## if Bottom of the sea
# s.view.level = 2

######################## if 0+
# s.view.level = 3

######################## if 0-
# s.view.level = 4

######################## if User defined
# s.view.level = 5
# s.view.vza = 0.0  # viewing zenith angle (for LUM_vsZ.txt standard output file)
# s.view.z = 0.0  # altitude/depth for which the radiance will be provided (for LUM_vsVZA.txt standard output file)


## CLASS OSOAA

s.wa = 0.0  # wavelength of the simulation
s.logfile = "log_res.txt"  # log file for the results
s.cleanup = False  # True to erase the results files

# root = ""  # path for the osoaa repertory
# forcerun = False  # True to run the simulation even if it already exists
# fatm_null = False  # True to run a simulation without atmosphere
# # but the file needs to be compiled before
# s.run(root, forcerun, fatm_null)

s.run()
