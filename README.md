# Dataset Notes

This CSV was supplied with the original academic project. It contains **953 tracks and 25 columns**.

The portfolio loader performs defensive cleaning before insertion into MySQL:

- numeric strings are converted safely;
- commas in numeric fields are removed;
- invalid numeric values are converted to SQL `NULL`;
- release year/month/day are combined into a database date;
- comma-separated artist names are normalized into the `Artist` and `Track_Artist` tables.

One source row (`Love Grows (Where My Rosemary Goes)`) contains a malformed value in the `streams` field. The loader preserves the track and stores its stream count as `NULL`.
