from enum import Enum
from drf_yasg import openapi
from .responses import (
    ErrorResponse, SuccessResponse, SuccessResponseExample, ErrorResponseExample
)


class ErrorCode(Enum):
    error_400 = (
        openapi.Response(
            description=ErrorResponse.data_not_valid.ERROR_MSG,
            examples={
                'application/json': ErrorResponseExample.data_not_valid.EXAMPLE
            }
        )
    )
    error_401 = (
        openapi.Response(
            description=ErrorResponse.unauthorized.ERROR_MSG,
            examples={
                'application/json': ErrorResponseExample.unauthorized.EXAMPLE
            }
        )
    )
    error_404 = (
        openapi.Response(
            description=ErrorResponse.no_match.ERROR_MSG,
            examples={
                'application/json': ErrorResponseExample.no_match.EXAMPLE
            }
        )
    )
    error_409 = (
        openapi.Response(
            description=ErrorResponse.item_exists.ERROR_MSG,
            examples={
                'application/json': ErrorResponseExample.item_exists.EXAMPLE
            }
        )
    )

    def __init__(self, RESPONSE):
        self.RESPONSE = RESPONSE


class SuccessCode(Enum):
    success_200 = (
        openapi.Response(
            description=SuccessResponse.detail_listed.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.list_user_detail.EXAMPLE
            }
        ),
        openapi.Response(
            description=SuccessResponse.detail_listed.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.list_like.EXAMPLE
            }
        ),
        openapi.Response(
            description=SuccessResponse.detail_listed.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.list_cart.EXAMPLE
            }
        ),
        openapi.Response(
            description=SuccessResponse.detail_listed.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.list_order_detail.EXAMPLE
            }
        )
    )
    success_201 = (
        None,
        openapi.Response(
            description=SuccessResponse.item_added.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.update_like.EXAMPLE
            }
        ),
        openapi.Response(
            description=SuccessResponse.item_added.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.update_cart.EXAMPLE
            }
        ),
        openapi.Response(
            description=SuccessResponse.item_added.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.post_new_order.EXAMPLE
            }
        )
    )
    success_204 = (
        openapi.Response(
            description=SuccessResponse.delivery_info_updated.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.update_delivery_info.EXAMPLE
            }
        ),
        openapi.Response(
            description=SuccessResponse.item_removed.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.update_like.EXAMPLE
            }
        ),
        openapi.Response(
            description=SuccessResponse.item_removed.SUCCESS_MSG,
            examples={
                'application/json': SuccessResponseExample.update_cart.EXAMPLE
            }
        ),
        None
    )

    def __init__(self, USER, LIKE, CART, ORDER):
        self.USER_RESPONSE = USER
        self.LIKE_RESPONSE = LIKE
        self.CART_RESPONSE = CART
        self.ORDER_RESPONSE = ORDER


class Swagger(Enum):
    list_user_detail_response = (
        {
            '200': SuccessCode.success_200.USER_RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
        }
    )
    update_delivery_info_response = (
        {
            '204': SuccessCode.success_204.USER_RESPONSE,
            '400':ErrorCode.error_400.RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
        }
    )
    list_like_item_detail_response = (
        {
            '200': SuccessCode.success_200.LIKE_RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
        }
    )
    add_like_item_response = (
        {
            '201': SuccessCode.success_201.LIKE_RESPONSE,
            '400':ErrorCode.error_400.RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
            '404': ErrorCode.error_404.RESPONSE,
            '409': ErrorCode.error_409.RESPONSE
        }
    )
    del_like_item_response = (
        {
            '204': SuccessCode.success_204.LIKE_RESPONSE,
            '400':ErrorCode.error_400.RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
            '404': ErrorCode.error_404.RESPONSE
        }
    )
    list_cart_item_detail_response = (
        {
            '200': SuccessCode.success_200.CART_RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
        }
    )
    add_cart_item_response = (
        {
            '201': SuccessCode.success_201.CART_RESPONSE,
            '400':ErrorCode.error_400.RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
            '404': ErrorCode.error_404.RESPONSE,
            '409': ErrorCode.error_409.RESPONSE
        }
    )
    del_cart_item_response = (
        {
            '204': SuccessCode.success_204.CART_RESPONSE,
            '400':ErrorCode.error_400.RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
            '404': ErrorCode.error_404.RESPONSE
        }
    )
    list_order_detail_response = (
        {
            '200': SuccessCode.success_200.ORDER_RESPONSE,
            '404': ErrorCode.error_404.RESPONSE
        }
    )
    post_new_order_response = (
        {
            '201': SuccessCode.success_201.ORDER_RESPONSE,
            '400':ErrorCode.error_400.RESPONSE,
            '401': ErrorCode.error_401.RESPONSE,
            '404': ErrorCode.error_404.RESPONSE
        }
    )

    def __init__(self, RESPONSE):
        self.RESPONSE = RESPONSE
