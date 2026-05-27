# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:00:05 EDT`
Last processed slot: `manage_1000`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$31,585.25`
- Equity: `$31,585.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  NXPI           88.24               34            0.60              1.40        332.07                92.16         0.658          pass              0.565             39.9                           0.206               12.38              1.230                      ok            True                  False
  SOXL           84.62               26            2.58              4.08        224.04               148.29         0.626          pass              0.474             60.6                           0.315               27.50              2.178                      ok            True                  False
  INTC           95.45               22            2.84              2.45        122.47                91.80         0.602          pass              0.677             45.7                           0.332               -0.49              0.407                      ok            True                  False
  ASML           90.62               32            1.01             11.49       1627.11                54.27         0.548          pass              0.644             53.1                           0.332                6.22              0.624                      ok            True                  False
  ISRG           86.67               15            2.13              6.52        433.84                35.34         0.522          pass              0.290              8.8                           0.201               -1.05              0.149                      ok            True                  False
  AMAT           80.77               26            1.22              3.90        453.22                55.57         0.514          pass              0.317             46.2                           0.267                4.33              0.289                      ok            True                  False
  LRCX           84.85               33            0.82              1.84        321.89                57.65         0.509          pass              0.482             49.4                           0.249               10.65              0.990                      ok            True                  False
  MSFT           86.96               23            1.01              2.95        414.77                23.55         0.503          pass              0.426             34.6                           0.457                1.21              0.211                      ok            True                  False
  INSM           78.72               47            0.01              0.01        108.87               110.60         0.743          pass              0.573             99.4                           0.724               -6.16             -0.799 downtrend_blocked_slope           False                  False
   TRI           85.71               28            0.02              0.01         83.71                55.63         0.645          pass              0.632             98.4                           0.558               -3.37              0.226                      ok           False                  False
  FTNT          100.00                6            3.63              3.41        132.50                66.88         0.613          pass              0.578             38.9                           0.315               13.37              1.420                      ok           False                  False
   AEP           75.00               16            0.48              0.44        130.71                25.21         0.605          pass              0.275             58.0                           0.514               -1.27              0.160                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                       detail
2026-05-27T10:00:05.617204-04:00 early_entry_1000  entry_skipped                                                                                   {"reason": "no_candidate"}
2026-05-27T09:20:01.591516-04:00     data_refresh   data_refresh                                                                                                {'saved': 92}
2026-05-26T15:10:03.526476-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:05:01.431933-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T15:00:02.550660-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:55:02.435729-04:00       entry_1500   slot_skipped                                                                              {"reason": "already_processed"}
2026-05-26T14:50:05.434333-04:00       entry_1500  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T14:50:05.434333-04:00       entry_1500 timing_overlay {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-05-26", "training_samples": 5069, "window": 5}
2026-05-26T12:00:02.390044-04:00 early_entry_1200  entry_skipped                                                                              {"reason": "daily_entry_limit"}
2026-05-26T11:55:03.347264-04:00 early_entry_1155  entry_skipped                                                                              {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527100005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527100005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527100005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527100005)

</details>
