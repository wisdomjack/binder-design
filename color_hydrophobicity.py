from pymol import cmd

# Define the hydrophobicity scale (Kyte-Doolittle)
hydrophobicity = {
    'ALA': 1.8, 'ARG': -4.5, 'ASN': -3.5, 'ASP': -3.5,
    'CYS': 2.5, 'GLN': -3.5, 'GLU': -3.5, 'GLY': -0.4,
    'HIS': -3.2, 'ILE': 4.5, 'LEU': 3.8, 'LYS': -3.9,
    'MET': 1.9, 'PHE': 2.8, 'PRO': -1.6, 'SER': -0.8,
    'THR': -0.7, 'TRP': -0.9, 'TYR': -1.3, 'VAL': 4.2
}

def color_hydrophobicity(selection="all", print_values=False):
    """
    Colors the given selection based on hydrophobicity and creates a color ramp legend.
    Uses blue for strongly hydrophilic, transitioning through cyan and white, then yellow to orange
    for strongly hydrophobic residues.
    
    Parameters:
      selection (str): The PyMOL selection or object to operate on.
      print_values (bool): If True, prints each residue's hydrophobicity.
    """
    # Assign hydrophobicity values to each atom's b-factor (defaulting to 0 if not found)
    cmd.alter(selection, "b=hydrophobicity.get(resn, 0)")
    cmd.rebuild()
    
    # Optionally print the hydrophobicity value for each unique residue.
    if print_values:
        model = cmd.get_model(selection)
        printed = set()
        print("Residue hydrophobicity values:")
        for atom in model.atom:
            key = (atom.chain, atom.resn, atom.resi)
            if key not in printed:
                printed.add(key)
                print("Chain: {}, Residue: {} {}, Hydrophobicity: {:.2f}".format(
                    atom.chain, atom.resn, atom.resi, atom.b
                ))
    
    # Apply a gradient color spectrum: blue -> cyan -> white -> yellow -> orange.
    cmd.spectrum("b", "blue cyan white yellow orange", selection, minimum=-4.5, maximum=4.5)
    cmd.rebuild()
    
    # Create a color ramp (legend) for the hydrophobicity scale using the same gradient.
    try:
        cmd.ramp_new("hydro_scale", selection, [-4.5, -2.25, 0, 2.25, 4.5], ["blue", "cyan", "white", "yellow", "orange"])
        print("Color ramp 'hydro_scale' created for selection:", selection)
    except Exception as e:
        print("Error creating ramp:", e)

# Make the command available in PyMOL
cmd.extend("color_hydrophobicity", color_hydrophobicity)
