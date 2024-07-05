
class LayerUtils:
    
    LayerChangeCommand = "M117 OCTOAPP_LAYER_CHANGE"
    DisableLegacyLayerCommand = "M117 OCTOAPP_DISABLE_LAYER_MAGIC"

    @staticmethod
    def CreateLayerChangeCommand(layer):
        return LayerUtils.LayerChangeCommand + " LAYER=" + str(layer)
    
    @staticmethod
    def IsLayerChange(line, context):
        if line.startswith("; generated by PrusaSlicer") or line.startswith("; generated by OrcaSlicer") or line.startswith("; generated by SuperSlicer"):
            context["slicer"] = "prusa"

        if line.startswith(";Generated with Cura"):
            context["slicer"] = "cura"

        if line.startswith("; generated by Slic3r"):
            context["slicer"] = "slic3r" # Doesn't mark layer changes

        if line.startswith("; Generated by Kiri:Moto"):
            context["slicer"] = "kirimoto"

        if line.startswith("; G-Code generated by Simplify3D"):
            context["slicer"] = "simplify"

        slicer =  context.get("slicer", None)

        if slicer == "prusa":
            return line.startswith(";LAYER_CHANGE")
        
        if slicer == "cura":
            return line.startswith(";LAYER:") 
        
        if slicer == "kirimoto":
            return line.startswith(";; --- layer")
        
        if slicer == "simplify":
            return line.startswith("; layer ") 
        
        return line.startswith("; OCTOAPP_LAYER_CHANGE") 