from collections import namedtuple
from sqlalchemy import asc, desc


def get_all_query(db, model, args):
    args = _extract_query_arguments(args)
    sort_arg = (
        asc(args.sort_by) if args.sort_order == "ascending" else desc(args.sort_by)
    )

    return (
        db.session.query(model)
        .filter_by(**args.filter_dict)
        .order_by(sort_arg)
        .paginate(page=args.page, per_page=args.per_page, error_out=False)
        .items
    )


def get_query(db, model, id):
    return db.session.query(model).filter_by(id=id).first()


def _extract_query_arguments(args):
    '''
    Split query arguments into:
        - per_page: Number of entries to return per page (Pagination).
        - page: Page number to return (Pagination).
        - sort_by: Column to sort return entries by (Sorting).
        - sort_order: Whether sort by ascending or descending (Sorting).
        - filter_dict: The rest of the query arguments, used for filtering.
    '''
    filter_dict = dict(args)

    # Pagination. 
    # per_page and page removed from args_dict because we don't want them in query filter.
    per_page = int(filter_dict.pop("per_page")) if "per_page" in filter_dict else 10
    page = int(filter_dict.pop("page")) if "page" in filter_dict else 1

    # Sorting
    # sort_by and sort_order removed from args_dict because we don't want them in query filter.
    sort_by = filter_dict.pop("sort_by") if "sort_by" in filter_dict else "id"
    sort_order = filter_dict.pop("sort_order") if "sort_order" in filter_dict else "ascending"

    QueryArguments = namedtuple("QueryArguments", "per_page page sort_by sort_order filter_dict")

    return QueryArguments(per_page, page, sort_by, sort_order, filter_dict)