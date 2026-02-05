from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, ItemViewSet, delete_item, delete_vendor, get_all_items, get_item_by_id, get_item_vendor_mappings,get_all_vendors,get_vendor_by_id, delete_item_vendor_mapping,get_vendor_by_id

router = DefaultRouter()
router.register('vendors', VendorViewSet)
router.register('items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from django.urls import path
from .views import (
    inventory_vendor_list,
    inventory_item_list,
    inventory_item_vendor_list
)

urlpatterns = [
    path('inventory-vendors/', inventory_vendor_list),
    path('inventory-items/', inventory_item_list),
    path('inventory-item-vendors/', inventory_item_vendor_list),

    # Vendors
    path('vendors/', get_all_vendors),
    path('vendors/<int:vendor_id>/', get_vendor_by_id),
    path('vendors/delete/<int:vendor_id>/', delete_vendor),

    # Items
    path('items/', get_all_items),
    path('items/<int:item_id>/', get_item_by_id),
    path('items/delete/<int:item_id>/', delete_item),
    
    # Item-Vendor Mapping
    path('item-vendors/', get_item_vendor_mappings),
    path('item-vendors/delete/<int:mapping_id>/', delete_item_vendor_mapping),
    

    
]
