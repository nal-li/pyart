"""
========================================
Radar Retrievals (:mod:`pyart.retrieve`)
========================================

.. currentmodule:: pyart.retrieve

Radar retrievals.

Radar retrievals
================

.. autosummary::
    :toctree: generated/

    kdp_maesaka
    kdp_schneebeli
    kdp_vulpiani
    kdp_leastsquare_single_window
    kdp_leastsquare_double_window
    calculate_snr_from_reflectivity
    compute_snr
    compute_l
    compute_cdr
    compute_noisedBZ
    compute_vol_refl
    compute_bird_density
    fetch_radar_time_profile
    map_profile_to_gates
    steiner_conv_strat
    hydroclass_semisupervised
    get_freq_band
    texture_of_complex_phase
    grid_displacement_pc
    grid_shift
    est_rain_rate_zpoly
    est_rain_rate_z
    est_rain_rate_kdp
    est_rain_rate_a
    est_rain_rate_zkdp
    est_rain_rate_za
    est_rain_rate_hydro
    est_wind_vel
    est_vertical_windshear
    get_coeff_attg
    est_wind_profile
    detect_ml
    melting_layer_giangrande
    melting_layer_hydroclass

"""
from .ml import detect_ml, melting_layer_giangrande, melting_layer_hydroclass
from .kdp_proc import kdp_maesaka, kdp_schneebeli, kdp_vulpiani
from .kdp_proc import kdp_leastsquare_single_window
from .kdp_proc import kdp_leastsquare_double_window
from .echo_class import steiner_conv_strat, hydroclass_semisupervised
from .echo_class import get_freq_band
from .gate_id import map_profile_to_gates, fetch_radar_time_profile
from .simple_moment_calculations import calculate_snr_from_reflectivity
from .simple_moment_calculations import calculate_velocity_texture
from .simple_moment_calculations import compute_snr, compute_l, compute_cdr
from .simple_moment_calculations import compute_noisedBZ, compute_signal_power
from .simple_moment_calculations import get_coeff_attg, compute_vol_refl
from .simple_moment_calculations import compute_bird_density
from .qpe import est_rain_rate_z, est_rain_rate_zpoly, est_rain_rate_kdp
from .qpe import est_rain_rate_a, est_rain_rate_zkdp, est_rain_rate_za
from .qpe import est_rain_rate_hydro
from .advection import grid_displacement_pc, grid_shift
from .wind import est_wind_vel, est_vertical_windshear, est_wind_profile

__all__ = [s for s in dir() if not s.startswith('_')]
