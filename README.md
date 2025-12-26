# utility_scripts
Random utility scripts in various programming languages for a variety of purposes. Many for computational chemistry or data processing purposes.

## Guide
- absorption_spectrum.py: Process vertical excitation energies and oscillator strengths sampled from MD into a linear absorption spectrum for an ensemble of trajectories. Data format matches the Schwartz lab MQC-MD code
- absorption_spectrum_single.py: Process vertical excitation energies and oscillator strengths sampled from MD into a linear absorption spectrum for a single trajectory. Data format matches the Schwartz lab MQC-MD code
- centerEl_miwat.wls: Center an xyz file about the final atom coordinates. Specific to systems of water + a single solute given as the final atomic position. Obeys periodic boundary conditions and water topology.
- ecom_SPIN.py: Calculate the center of mass of a spin density cube file with periodic boundary conditions.
- lmpToXyz.wls: Convert a lammps data output to xyz file.
- radius_gy_SPIN.py: Calculate the radius of gyration for a spin density cube file with periodic boundary conditions. Needs center of mass position, which can be calculated using ecom_SPIN.py.
- xyzToWater.wls: Convert an xyz file to Schwartz lab MQC-MD input format for a single xyz file.
- xyzToWaterMap.wls: Convert an xyz file to Schwartz lab MQC-MD input format for a xyz file trajectory.
