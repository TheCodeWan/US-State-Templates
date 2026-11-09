# State government trifectas

The current HTML and PNG show the incoming governments following the November 3, 2026 elections, using results available November 9. They do not describe the outgoing officeholders still serving. Results remain unofficial.

## Compare maps

- [Updated PNG](us-states-state-government-trifectas.png)
- [Editable map](us-states-state-government-trifectas.html)
- [Original June 2026 PNG](history/us-states-state-government-trifectas-june-2026.png), preserved byte for byte from commit `52a4c756958f99a09088b5d30395204ee101a74f`.

| Category | States |
| --- | ---: |
| Democratic trifecta | 22 |
| Republican trifecta | 18 |
| Divided / coalition | 9 |
| Pending | 1 |

## Changes from the original map

| States | Before | After |
| --- | --- | --- |
| Arizona, Michigan, Minnesota, Nevada, Pennsylvania, Wisconsin | Divided | Democratic trifecta |
| Georgia, Iowa, New Hampshire, Ohio, Texas | Republican trifecta | Divided |
| Kansas | Divided | Pending |

A trifecta requires the governor and both legislative chambers to be controlled by the same party. Alaska remains purple because its incoming chambers are organized under bipartisan coalitions, regardless of the unresolved gubernatorial result. Nebraska is classified by its legislators’ party affiliations despite its formally nonpartisan unicameral legislature. D.C. retains blue for Democratic local control and is excluded from the 50-state counts.

Kansas is gray because its gubernatorial call could not be consistently verified: some trackers project a Democratic win, while other reports still list the contest as uncalled. A Democratic win would mean divided government; a Republican win would mean a Republican trifecta. The map intentionally leaves that outcome pending.

## Sources

- [Ballotpedia: 2026 trifecta election results](https://ballotpedia.org/Election_results,_2026:_State_government_trifectas), for the eleven confirmed changes and baseline categories.
- [NCSL: 2026 state legislative election results](https://www.ncsl.org/news/details/2026-state-legislative-elections-the-results-and-what-they-mean), cross-checking the named changes. Aggregate totals on that page differ from its narrative; this map uses state-level classifications.
- [Alaska Public Media: incoming legislature](https://alaskapublic.org/news/politics/2026-11-05/what-to-expect-when-youre-expecting-a-new-alaska-legislature-a-reporter-explains), for continuing bipartisan coalitions.
- [MultiState: Kansas results](https://www.multistate.us/elections/results/kansas-2026) and [Kansas governor tracker](https://www.multistate.us/elections/governor-race/kansas-2026); the pages differ on whether the governor race has been called.
- [DDHQ: Kansas governor](https://votes.decisiondeskhq.com/races/2026-11-03/kansas-governor-general-election), showing the close count without an unambiguous candidate-specific call.

## Regenerate

From the repository root:

```bash
python png-generator/generate-pngs.py --file "Maps of the entire US/examples/state-government-trifectas/us-states-state-government-trifectas.html"
```

The historical PNG has no paired HTML, so the generator leaves it untouched.
