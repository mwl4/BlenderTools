# ##### BEGIN GPL LICENSE BLOCK #####
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# Copyright (C) 2013-2019: SCS Software

import bpy
from bpy.props import IntProperty


class ActionSCSTools(bpy.types.PropertyGroup):
    """
    SCS Tools Action Variables - ...Action.scs_props...
    :return:
    """

    anim_export_step: IntProperty(
        name="Export Step",
        description="Number of frames to step in action for each iteration trough exporting.",
        default=1,
        min=0, max=128,
        step=1,
        options={'HIDDEN'},
        subtype='NONE',
    )


classes = (
    ActionSCSTools,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
