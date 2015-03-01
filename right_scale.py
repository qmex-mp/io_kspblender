# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

from mathutils import Vector

def make():
    '''Makes the right_scale dictionary to fix scaling'''

    right_scale = {}
    
    right_scale['Mark1Cockpit'] = Vector((1.25,1.25,1.25))
    right_scale['Mark2Cockpit'] = Vector((1.25,1.25,1.25))
    right_scale['fuelTank'] = Vector((1.25,1.25,1.25))
    right_scale['fuelTankSmall'] = Vector((1.25,1.25,1.25))
    right_scale['noseConeAdapter'] = Vector((1.25,1.25,1.25))
    right_scale['standardNoseCone'] = Vector((1.25,1.25,1.25))
    right_scale['liquidEngine'] = Vector((1.25,1.25,1.25))
    right_scale['liquidEngine2'] = Vector((1.25,1.25,1.25))
    right_scale['science.module'] = Vector((1.25,1.25,1.25))
    right_scale['fuelTank.long'] = Vector((1.25,1.25,1.25))
    right_scale['Mk1Fuselage'] = Vector((1.25,1.25,1.25))
    right_scale['Mk1FuselageStructural'] = Vector((1.25,1.25,1.25))
    right_scale['Mk1IntakeFuselage'] = Vector((1.25,1.25,1.25))
    right_scale['nacelleBody'] = Vector((1.25,1.25,1.25))
    right_scale['radialEngineBody'] = Vector((1.25,1.25,1.25))
    right_scale['turboFanEngine'] = Vector((1.25,1.25,1.25))
    right_scale['CircularIntake'] = Vector((1.25,1.25,1.25))
    right_scale['toroidalAerospike'] = Vector((1.25,1.25,1.25))
    right_scale['ramAirIntake'] = Vector((1.25,1.25,1.25))
    right_scale['JetEngine'] = Vector((1.25,1.25,1.25))
    right_scale['RAPIER'] = Vector((1.25,1.25,1.25))
    right_scale['winglet'] = Vector((1.25,1.25,1.25))
    right_scale['R8winglet'] = Vector((1.25,1.25,1.25))
    right_scale['solidBooster'] = Vector((1.25,1.25,1.25))

    return right_scale
