# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-02 09:35:01 EDT`
Last processed slot: `manage_0930`

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

- Cash: `$33,669.25`
- Equity: `$33,669.25`
- Realized PnL: `$23,669.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-02)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           84.85               33            1.10              7.95       1031.33               101.73         0.730          pass              0.481             41.7                           0.276               50.16              4.591                      ok            True                  False
  MELI           94.74               38            0.59              7.13       1727.93                60.28         0.606          pass              0.831             63.6                           0.514                8.51              0.778                      ok            True                  False
   WDC           97.37               38            0.62              2.35        545.19                59.04         0.532          pass              0.792             50.8                           0.336               18.35              2.061                      ok            True                  False
   ADP          100.00               10            2.41              3.94        232.05                34.26         0.527          pass              0.453              0.0                           0.197                2.32              0.298                      ok            True                  False
  CRWD           85.71               21            1.56              8.52        778.52                48.77         0.514          pass              0.464             62.2                           0.631               24.43              2.214                      ok            True                  False
  CDNS           90.48               21            1.93              5.59        411.77                44.19         0.502          pass              0.506             34.4                           0.485               17.40              1.725                      ok            True                  False
  INSM           53.85               13            3.42              2.54        104.94               110.78         0.714          pass              0.142             16.9                           0.171               -4.43             -0.297 downtrend_blocked_slope           False                  False
  FTNT          100.00                9            2.37              2.44        146.09                71.69         0.686          pass              0.603             44.8                           0.616               13.56              1.219                      ok           False                  False
  QCOM           97.56               41            0.12              0.20        228.91               102.92         0.680          pass              0.956             96.0                           0.502               12.31              1.906                      ok           False                  False
    ZS           50.00                4            6.86              7.47        152.51               157.27         0.667          pass              0.074              2.3                           0.237              -16.98             -2.712 downtrend_blocked_slope           False                  False
  SHOP           73.33               15            3.56              3.09        122.79                84.68         0.587          pass              0.092              0.0                           0.235               16.91              1.993                      ok           False                  False
  MNST           97.83               46            0.18              0.11         89.05                49.60         0.544          pass              0.878             74.6                           0.413                0.45              0.232                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot     event_type                                                                                                                                                                                detail
2026-06-02T09:20:05.650957-04:00     data_refresh   data_refresh                                                                                                                                                                         {'saved': 92}
2026-06-01T15:10:04.135705-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:05:05.129733-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T15:00:02.274373-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:55:05.958850-04:00       entry_1500   slot_skipped                                                                                                                                                       {"reason": "already_processed"}
2026-06-01T14:50:06.115038-04:00       entry_1500  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T14:50:06.115038-04:00       entry_1500 timing_overlay                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-01", "training_samples": 5165, "window": 5}
2026-06-01T12:50:07.149920-04:00      manage_1300           exit {"asset_type": "option", "contract_symbol": "SNPS260717C00470000", "fill_price": 42.3, "pnl": 2820.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 20.0, "ticker": "SNPS"}
2026-06-01T12:00:03.957402-04:00 early_entry_1200  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
2026-06-01T11:55:05.058620-04:00 early_entry_1155  entry_skipped                                                                                                                                                       {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260602093501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260602093501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260602093501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260602093501)

</details>
