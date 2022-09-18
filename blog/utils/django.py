def get_or_none_for_manager(manager, select_related=[], **kwargs):
    # common get or none logic extended by all
    # other get or none utils

    # using .last() instead of .first() because old logic used the same

    queryset = manager.filter(**kwargs)

    if select_related:
        queryset = queryset.select_related(*select_related)

    try:
        return queryset.last()
    except (
        manager.model.DoesNotExist,
        ValueError,
        TypeError,
        IndexError,
    ):
        return None


def get_or_none(model, select_related=[], **kwargs):
    return get_or_none_for_manager(model.objects, select_related=select_related, **kwargs)