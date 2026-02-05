
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import math

# Create your views here.
from rest_framework import viewsets
from .models import Vendor, Item
from .serializers import VendorSerializer, ItemSerializer


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



@api_view(['POST'])
def inventory_vendor_list(request):
    try:
        page = int(request.data.get("page", 1))
        per_page = int(request.data.get("per_page", 10))
        offset = (page - 1) * per_page

        # COUNT
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM inventory_vendor")
            total_records = cursor.fetchone()[0]

        # DATA
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id,
                    abbreviation,
                    firm_name,
                    city,
                    phone_no,
                    email
                FROM inventory_vendor
                ORDER BY id DESC
                LIMIT %s OFFSET %s
            """, [per_page, offset])

            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response({
            "status": "1",
            "message": "Vendor list fetched successfully",
            "pagination": {
                "current_page": page,
                "per_page": per_page,
                "total_records": total_records,
                "total_pages": math.ceil(total_records / per_page)
            },
            "data": data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": "0",
            "message": "Error fetching vendor list",
            "error": str(e),
            "data": []
        }, status=status.HTTP_200_OK)



@api_view(['POST'])
def inventory_item_list(request):
    try:
        page = int(request.data.get("page", 1))
        per_page = int(request.data.get("per_page", 10))
        offset = (page - 1) * per_page

        # COUNT
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM inventory_item")
            total_records = cursor.fetchone()[0]

        # DATA
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id,
                    ohe_code,
                    rin_no,
                    description,
                    drawing_no
                FROM inventory_item
                ORDER BY id DESC
                LIMIT %s OFFSET %s
            """, [per_page, offset])

            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response({
            "status": "1",
            "message": "Item list fetched successfully",
            "pagination": {
                "current_page": page,
                "per_page": per_page,
                "total_records": total_records,
                "total_pages": math.ceil(total_records / per_page)
            },
            "data": data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": "0",
            "message": "Error fetching item list",
            "error": str(e),
            "data": []
        }, status=status.HTTP_200_OK)


@api_view(['POST'])
def inventory_item_vendor_list(request):
    try:
        page = int(request.data.get("page", 1))
        per_page = int(request.data.get("per_page", 10))
        offset = (page - 1) * per_page

        # COUNT
        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM inventory_item_vendors")
            total_records = cursor.fetchone()[0]

        # DATA
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id,
                    item_id,
                    vendor_id
                FROM inventory_item_vendors
                ORDER BY id DESC
                LIMIT %s OFFSET %s
            """, [per_page, offset])

            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response({
            "status": "1",
            "message": "Item–Vendor mapping fetched successfully",
            "pagination": {
                "current_page": page,
                "per_page": per_page,
                "total_records": total_records,
                "total_pages": math.ceil(total_records / per_page)
            },
            "data": data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": "0",
            "message": "Error fetching item-vendor mapping",
            "error": str(e),
            "data": []
        }, status=status.HTTP_200_OK)

# get all Vendors
@api_view(['GET'])
def get_all_vendors(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, abbreviation, firm_name, city, phone_no, email
                FROM inventory_vendor
                ORDER BY id DESC
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response({
            "status": "1",
            "message": "Vendors fetched successfully",
            "data": data
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "status": "0",
            "message": str(e),
            "data": []
        }, status=status.HTTP_200_OK)


# get single vendor(by id)
@api_view(['GET'])
def get_vendor_by_id(request, vendor_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, abbreviation, firm_name, city, phone_no, email
                FROM inventory_vendor
                WHERE id = %s
            """, [vendor_id])

            row = cursor.fetchone()
            if not row:
                return Response({"status": "0", "message": "Vendor not found"}, status=200)

            columns = [col[0] for col in cursor.description]
            data = dict(zip(columns, row))

        return Response({
            "status": "1",
            "data": data
        }, status=200)

    except Exception as e:
        return Response({"status": "0", "message": str(e)}, status=200)

# delete vendor 
@api_view(['DELETE'])
def delete_vendor(request, vendor_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM inventory_vendor WHERE id = %s", [vendor_id])

        return Response({
            "status": "1",
            "message": "Vendor deleted successfully"
        }, status=200)

    except Exception as e:
        return Response({"status": "0", "message": str(e)}, status=200)


# inventory_items_api

# get all items 
@api_view(['GET'])
def get_all_items(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, ohe_code, rin_no, description, drawing_no
                FROM inventory_item
                ORDER BY id DESC
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response({
            "status": "1",
            "data": data
        }, status=200)

    except Exception as e:
        return Response({"status": "0", "message": str(e)}, status=200)


# get single item
@api_view(['GET'])
def get_item_by_id(request, item_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, ohe_code, rin_no, description, drawing_no
                FROM inventory_item
                WHERE id = %s
            """, [item_id])

            row = cursor.fetchone()
            if not row:
                return Response({"status": "0", "message": "Item not found"}, status=200)

            columns = [col[0] for col in cursor.description]
            data = dict(zip(columns, row))

        return Response({"status": "1", "data": data}, status=200)

    except Exception as e:
        return Response({"status": "0", "message": str(e)}, status=200)

# delete item 
@api_view(['DELETE'])
def delete_item(request, item_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM inventory_item WHERE id = %s", [item_id])

        return Response({
            "status": "1",
            "message": "Item deleted successfully"
        }, status=200)

    except Exception as e:
        return Response({"status": "0", "message": str(e)}, status=200)



# inventory_item_vendor_api

# get_all_item_vendor_mappings
@api_view(['GET'])
def get_item_vendor_mappings(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, item_id, vendor_id
                FROM inventory_item_vendors
                ORDER BY id DESC
            """)
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]

        return Response({
            "status": "1",
            "data": data
        }, status=200)

    except Exception as e:
        return Response({"status": "0", "message": str(e)}, status=200)


# delete item_vendor_mapping
@api_view(['DELETE'])
def delete_item_vendor_mapping(request, mapping_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM inventory_item_vendors WHERE id = %s",
                [mapping_id]
            )

        return Response({
            "status": "1",
            "message": "Mapping deleted successfully"
        }, status=200)

    except Exception as e:
        return Response({"status": "0", "message": str(e)}, status=200)
