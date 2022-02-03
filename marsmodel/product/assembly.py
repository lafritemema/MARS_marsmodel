from ._product import Product
# from .part import Instance as PartInstance
from neomodel.properties import ArrayProperty, IntegerProperty, StringProperty, FloatProperty
from neomodel.contrib.spatial_properties import PointProperty
from neomodel.relationship_manager import RelationshipTo, RelationshipFrom, StructuredRel

class AssembleRS(StructuredRel):
  stackThickness = FloatProperty()
  stackMaterial = StringProperty()
  stackIndex = IntegerProperty()

class Assembly(Product):
  orient=ArrayProperty(base_property=IntegerProperty())
  origin=PointProperty(crs='cartesian-3d')
  assemble = RelationshipTo('marsmodel.product.part.Instance', 'ASSEMBLE', model=AssembleRS)
  fastener = RelationshipFrom('marsmodel.product.fastener.Instance', 'FASTEN')
  pattern = RelationshipTo('marsmodel.process.pattern.Pattern', 'ELEMENT_OF')