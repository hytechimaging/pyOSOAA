def ChooseLevel(s, level, direction):
    """Retrieve the values of the parameters of the OSOAA advanced files for a chosen level.

    Args:
        s (OSOAA object): Contains the parameters of the advanced output files of an OSOAA simulation
        level (int32): Value of the level to be retrieved
        direction (str): Specify the file in which to retrieve the values (up/down)
    """
    if direction == "up":
        level_values = s.outputs.advup.level
        indexm = len(level_values)
        indexM = 0
        for i in range(len(level_values)):
            if level_values[i] == level:
                if i < indexm:
                    indexm = i
                if i > indexM:
                    indexM = i
        z = s.outputs.advup.z[indexm : indexM + 1]
        vza = s.outputs.advup.vza[indexm : indexM + 1]
        sca = s.outputs.advup.scaang[indexm : indexM + 1]
        I = s.outputs.advup.I[indexm : indexM + 1]
        Q = s.outputs.advup.Q[indexm : indexM + 1]
        U = s.outputs.advup.U[indexm : indexM + 1]
        Ang = s.outputs.advup.polang[indexm : indexM + 1]
        DoLP = s.outputs.advup.polrate[indexm : indexM + 1]
        Ipol = s.outputs.advup.lpol[indexm : indexM + 1]

    if direction == "down":
        level_values = s.outputs.advdown.level
        indexm = len(level_values)
        indexM = 0
        for i in range(len(level_values)):
            if level_values[i] == level:
                if i < indexm:
                    indexm = i
                if i > indexM:
                    indexM = i
        z = s.outputs.advdown.z[indexm : indexM + 1]
        vza = s.outputs.advdown.vza[indexm : indexM + 1]
        sca = s.outputs.advdown.scaang[indexm : indexM + 1]
        I = s.outputs.advdown.I[indexm : indexM + 1]
        Q = s.outputs.advdown.Q[indexm : indexM + 1]
        U = s.outputs.advdown.U[indexm : indexM + 1]
        Ang = s.outputs.advdown.polang[indexm : indexM + 1]
        DoLP = s.outputs.advdown.polrate[indexm : indexM + 1]
        Ipol = s.outputs.advdown.lpol[indexm : indexM + 1]
    return z, vza, sca, I, Q, U, Ang, DoLP, Ipol


def ChooseDepth(s, z, direction):
    """Retrieve the values of the parameters of the OSOAA advanced files for a chosen depth or height.

    Args:
        s (OSOAA object): Contains the parameters of the advanced output files of an OSOAA simulation
        z (float64): Value of the depth/height to be retrieved
        direction (str): Specify the file in which to retrieve the values (up/down)
    """
    if direction == "up":
        z_values = s.outputs.advup.z
        indexm = len(z_values)
        indexM = 0
        for i in range(len(z_values)):
            if z_values[i] == z:
                if i < indexm:
                    indexm = i
                if i > indexM:
                    indexM = i
        level = s.outputs.advup.level[indexm : indexM + 1]
        vza = s.outputs.advup.vza[indexm : indexM + 1]
        sca = s.outputs.advup.scaang[indexm : indexM + 1]
        I = s.outputs.advup.I[indexm : indexM + 1]
        Q = s.outputs.advup.Q[indexm : indexM + 1]
        U = s.outputs.advup.U[indexm : indexM + 1]
        Ang = s.outputs.advup.polang[indexm : indexM + 1]
        DoLP = s.outputs.advup.polrate[indexm : indexM + 1]
        Ipol = s.outputs.advup.lpol[indexm : indexM + 1]

    if direction == "down":
        z_values = s.outputs.advdown.z
        indexm = len(z_values)
        indexM = 0
        for i in range(len(z_values)):
            if z_values[i] == level:
                if i < indexm:
                    indexm = i
                if i > indexM:
                    indexM = i
        level = s.outputs.advdown.level[indexm : indexM + 1]
        vza = s.outputs.advdown.vza[indexm : indexM + 1]
        sca = s.outputs.advdown.scaang[indexm : indexM + 1]
        I = s.outputs.advdown.I[indexm : indexM + 1]
        Q = s.outputs.advdown.Q[indexm : indexM + 1]
        U = s.outputs.advdown.U[indexm : indexM + 1]
        Ang = s.outputs.advdown.polang[indexm : indexM + 1]
        DoLP = s.outputs.advdown.polrate[indexm : indexM + 1]
        Ipol = s.outputs.advdown.lpol[indexm : indexM + 1]
    return level, vza, sca, I, Q, U, Ang, DoLP, Ipol


def StandardOutput(s, filetype):
    """Retrieve the values of the parameters of the OSOAA standard output files.

    Args:
        s (OSOAA object): Contains the parameters of the standard output files of an OSOAA simulation
        filetype (str): Specify the file in which to retrieve the values (vza/z)
    """
    if filetype == "vza":
        vza = s.outputs.vsvza.vza
        sca = s.outputs.vsvza.scaang
        I = s.outputs.vsvza.I
        Refl = s.outputs.vsvza.refl
        DoLP = s.outputs.vsvza.polrate
        Ipol = s.outputs.vsvza.lpol
        Reflpol = s.outputs.vsvza.reflpol
        return vza, sca, I, Refl, DoLP, Ipol, Reflpol

    if filetype == "z":
        z = s.outputs.vsz.z
        sca = s.outputs.vsz.scaang
        I = s.outputs.vsz.I
        Refl = s.outputs.vsz.refl
        DoLP = s.outputs.vsz.polrate
        Ipol = s.outputs.vsz.lpol
        Reflpol = s.outputs.vsz.reflpol
        return z, sca, I, Refl, DoLP, Ipol, Reflpol
